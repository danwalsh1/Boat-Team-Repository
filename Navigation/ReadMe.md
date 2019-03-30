# Navigation

<h2><u>Bearing Calculator</u></h2>

Using math libraray
Calculate the bearing by first converting the input into radians. Then finding the lattitude by subtracting the current and final position longitude.
x and y are calculated for atan2 to find the quadrent for the angle.  atan2 is calculated and is converted in degrees.
The resulting bearing is checked to start the degress from the North and if not, conversion is done.

<h2><u>Navigation</u></h2>

Firstly, the code calculates if tacking will be required (based on the no-go zones for sailing). If tacking isn't needed an array with a single zero in it is returned. If a tack is needed, the waypoints are calculated then returned.

To calculate the waypoints for tacking, the code calculates the number of tacks needed, using getTackSpacing() to tell how far can be travelled in one tack.

The waypoints for tacking are then calculated using, getTackDistance() to calculate the distance to the point furthest from the origin line (the line from the start point to the final destination point) and then getDestCoords() giving it the heading and distances from the previous two functions.
