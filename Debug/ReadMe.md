# Debug

This file allows a log files data to be displayed in a graphical format.

![DebugClientPicture](https://github.com/potato-chip-studios/Boat-Team-Repository/blob/master/Debug/Debug-Client-Pic.png)

The left panel (left half of the webpage) displays the "boat actions" data, and the right panel shows the position of the boat and the waypoint it was heading to at that time.

In the left panel, the black circle represents the boat with North always being at the top of the webpage. The blue line, starting from the boats center, represents the direction the boat was traveling at that time (the boats heading). The orange line, starting from the boats center, represents the direction to the waypoint that the boat was traveling to at that time (the desired heading). Finally, the green line, starting from the boats center, represents the angle of the boats rudder.

On the right panel, the red marker represents the boats position at that time and the orange marker represents the position of the waypoint that the boat was traveling to at that time.

Logs are currently inserted into the code on line 172 as an array of arrays.

<b>NOTE:</b> The file needs to have a Google Maps JavaScript API key given to it on line 37. These keys are given out by Google.
