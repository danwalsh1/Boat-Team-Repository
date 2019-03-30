# requires "python -m pip install geopy"
from geopy import distance
from geopy import Point
import Bearing_Calculator as bCalc
try:
    import math
except ImportError:
    print("Double import")

SETTING_TACK_OFFSET_DISTANCE = 20 # Metres

def isTackNeeded(desHeading, windDir):
    # Returns angle between desHeading and tack heading if tack is needed, returns False if tack isn't needed
    desHeading = removeMinus(desHeading)
    windDir = removeMinus(windDir)

    if((windDir >= 0 and windDir <= 40) or (windDir >= 320 and windDir <= 360)):
        # No go zone crosses from 0 to 359 boundary
        if((desHeading >= removeMinus(windDir - 40) and desHeading <= 360) or (desHeading >= 0 and desHeading <= removeMinus(windDir + 40))):
            # Inside no go zone
            # Tack needed
            negposDesHeading = addMinus(desHeading)
            negposWindDir = addMinus(windDir)
            if(negposDesHeading <= negposWindDir):
                # Tack angle will be left of desHeading
                return makePositive(negposDesHeading - (negposWindDir - 41))
            else:
                # Tack angle will be right of desHeading
                return makePositive((negposWindDir + 41) - negposDesHeading)
        else:
            # Outside no go zone
            # Tack not needed
            return False
    else:
        # No go zone is from wind direction -40 to windirection +40
        if(desHeading >= windDir - 40 and desHeading <= windDir + 40):
            # Inside no go zone
            # Tack needed
            if(desHeading <= windDir):
                # Tack angle will be left of desHeading
                return desHeading - (windDir - 41)
            else:
                # Tack angle will be right of desHeading
                return (windDir + 41) - desHeading
        else:
            # Outside no go zone
            # Tack not needed
            return False

def makePositive(number):
    # If the given number is negative, it is made positive (multiplied by -1)
    if(number < 0):
        return -number
    else:
        return number

def removeMinus(angle):
    # If a negative angle is given, it is removed from 360 (given turns negative angles into positive angles)
    # NOTE: This is not the same as makePositive()
    if(angle >= 0):
        return angle
    else:
        return 360 + angle

def addMinus(angle):
    # Returns a negative angle if the given angle is above 180
    if(angle > 180):
        return 0 - (180 - (angle - 180))
    else:
        return angle

def getTackDistance(tackAngle):
    # Returns the distance from the start of a tack to the point where the tack is furthest away from the origin line
    return SETTING_TACK_OFFSET_DISTANCE * math.sin(math.radians(90)) / math.sin(math.radians(tackAngle))

def getTackSpacing(tackAngle, tackDistance):
    # Returns the distance from the start of a tack to the point where the tack returns to a point on the origin line
    return tackDistance * math.sin(math.radians(98)) / math.sin(math.radians(180 - 98 - tackAngle))

def getDestCoords(startLat, startLng, heading, distance):
    # Returns the coordinates of a point given the starting position, the heading and the distance travelled from the start point
    start = Point(startLat, startLng)
    tackCoord = distance.distance(kilometers=distance/1000).destination(start, heading)
    tackLat = tackCoord.latitude
    tackLng = tackCoord.longitude
    return [tackLat, tackLng]

def planTack(currLat, currLng, desLat, desLng, windDir, debug = False):
    # Returns a list of waypoint positions to get from the current position to the destination positon, taking wind direction into account
    if(debug):
        # Print debugging information
        print("Current Position: (" + str(currLat) + "," + str(currLng) + ")")
        print("Current Waypoint: (" + str(desLat) + "," + str(desLng) + ")")
        print("Wind direction: " + str(windDir) + " degrees clockwise from North")

    # Calculate and print the desired heading (our bearing)
    bearing = bCalc.getDesiredBearing(currLat, currLng, desLat, desLng)
    if(debug):
        print("Direct Bearing: " + str(bearing) + " degrees")

    # Is a tack needed to travel to destination?
    tackAngleFromBearing = isTackNeeded(bearing, windDir)
    if(tackAngleFromBearing != False):
        # Tack needed
        path = [1]

        # Calculate waypoint list for tacking
        tackDistance = getTackDistance(tackAngleFromBearing)
        if(debug):
            print("Angle between desired heading and tack heading: " + str(tackAngleFromBearing) + " degrees")
            print("Tack distance: " + str(tackDistance) + " metres")

        # Calculate distance between tack returns on direct bearing line
        tackSpacing = getTackSpacing(tackAngleFromBearing, tackDistance)
        if(debug):
            print("Tack spacing: " + str(tackSpacing) + "m")

        return path
    else:
        # Tack not needed
        return [0]

print(planTack(52.321846, -1.329745, 52.329505, -1.325799, 0, True))
