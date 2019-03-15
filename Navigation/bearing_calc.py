import math

# Created by Dan and Hannia

def calcBearing(latA, lonA, latB, lonB):
    # Convert to radians
    RlatA = math.radians(latA)
    RlatB = math.radians(latB)
    Rlon = math.radians(lonB - lonA)

    # Calculate X & Y for atan2 calculation
    y = math.cos(RlatA)*math.sin(RlatB)-math.sin(RlatA)*math.cos(RlatB)*math.cos(Rlon)
    x = math.sin(Rlon)*math.cos(RlatB)

    result = math.atan2(y, x)
    
    # Convert back to degrees
    result = math.degrees(result)
    return result

def BearingFromNorth(bearing):
    # Make the given degrees start from north
    result = bearing * -1
    result = result + 90
    return result

def getDesiredBearing(latA, lonA, latB, lonB):
    result = calcBearing(latA, lonA, latB, lonB)
    result = BearingFromNorth(result)
    if(result < 0):
        # Ensure given degrees are clockwise from north
        result = 360 - (result * -1)

    return result

#print(BearingFromNorth(calcBearing(52.326148, -1.335490, 52.321689, -1.323136)))
#print(BearingFromNorth(calcBearing(52.321689, -1.323136, 52.326148, -1.335490)))

print(getDesiredBearing(52.326148, -1.335490, 52.321689, -1.323136))
print(getDesiredBearing(52.321689, -1.323136, 52.326148, -1.335490))
