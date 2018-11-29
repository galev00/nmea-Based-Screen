# nmea-Based-Screen
nmea Based Screen

My boat uses Raymarine based instruments.
Goal of this project is improve the displays and control some features with an android based phone or tablet.

Hardware
- Serial connector to collect data
- rPi to send data though wifi UDP or TCP
- second rPi to display data
- old laptop screen
- Universal display module
- 5730 chip leds strips for sunlight readable screen
- aluminuim case for display and rpi (something like goose neck)

Software
- to read data from serial (nmea 0183) and broadcast also take sentences and send to raymarine system
- to display data received from UDP or TCP
