The Hackable Clock
==================

A hackable alarm clock, made for experimentation to learn GPIO and programming.

Project page detailing out the hardware build is available at http://hackaday.io/project/3413-hack-ready-alarm-clock

Lessons and tutorials are coming soon.

Installation
------------

The hack-clock application is intended to be distributed as source, not in binary or packaged form, since
it is intended to be a teaching tool. Unfortunately this means we need to take a few extra steps to
install, but the entire process should take only a few minutes.

I'm assuming that you are starting with the NOOBS Linux distribution. To install the hack-clock distribution on top of it:

1. Make sure your Raspberry Pi is up to date with the latest packages & firmware.
2. Enable I2C in the "Advanced Options" sections within `sudo raspi-config`
3. Add the necessary Python and GStreamer dependencies using `sudo apt-get install wiringpi python-distribute python-dev python-smbus python-rpi.gpio gstreamer0.10-x gstreamer-tools gstreamer0.10-plugins-base gstreamer0.10-plugins-good gstreamer0.10-plugins-bad python-gst0.10`
4. To let the pi user sense button presses, use the WiringPi GPIO Utility to permit non-root access to the pins. As an example: `gpio export 24 in; gpio mode 24 up`
5. Clone or download this repository using `git clone https://github.com/deckerego/hack-clock.git`
6. Install hack-clock's dependencies using `sudo pip install -r requirements.txt`
7. Copy the file `config.sample` to `config.py` and customize it for your environment (e.g. your local weather station)
8. Start the app by executing `./run_server.py` from within the hack-clock/webapp directory

Bear in mind you may want to consider forking the source instead of cloning the parent repository -
that way you can make alterations and save your changes independently!

Starting the Clock at Boot
--------------------------

To start the clock as soon as your Raspberry Pi boots up:

1. Copy the startup script `hack-clock` into the directory `/etc/init.d`
2. Ensure the clock starts at boot using the command `sudo update-rc.d hack-clock defaults`
3. Start the clock with `sudo service hack-clock start`

The start-up script also sets GPIO5 (Broadcom GPIO 24) with the correct input values and resistor states, so this is a helpful
way to make sure your button pins are set correctly.

License
=======

License is Apache Public License 2.0 (APL 2) unless otherwise noted.

The Adafruit libraries located in the /Adafruit directory are licensed separately, see Adafruit/README.md for details.
The original code is available at https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code

CodeMirror is licensed separately as detailed in views/codemirror/LICENSE. The CodeMirror codebase is
not directly committed into this repository (although it appears that way) - it is a subtree of
the repository available at https://github.com/codemirror/codemirror

Drawing of a 0.36" single digit seven-segment display has been released into the Public Domain by Inductiveload,
available at http://commons.wikimedia.org/wiki/File:7-Segment_Display,_0.36in,_Single_(shaded).svg
