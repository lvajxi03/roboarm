# RoboArm

Yet another repository with `Python` code controlling
*Velleman KSR10*/*OWI-535* robotic arm via ``USB``.

All useful documentation is included in source code of ``roboarm`` module,
however ``docs/`` subdirectory contains all files necessary to build
``Sphinx`` HTML pages.

This repo contains also ``roboui`` module that can be a standalone PyQt5 app
controlling your KSR10/OWI-535 robotic arm.

## Overview

*Velleman KSR10*/*OWI-535* roboarm contains following parts:

* **base** (can be rotated clockwise or counterclockwise)
* **shoulder** (can be moved up and down)
* **wrist** (can be moved up and down)
* **elbow** (can be moved up and down)
* **grip** (can be opened or closed)
* **LED light** (can be turned on or off)

Excluding *LED light*, all other parts are controlled with sending
appropriate command to *arm USB controller*

*Warning*: the command turns on the motor, which stuck if only
motor was not stopped after a short delay.

``roboarm`` module defines all necessary methods in ``RoboArm`` class
to move all controllable parts with sending a command to USB controller,
and then to stop all motors after a short duration (predefined
``DefaultDuration`` is pretty good for novice users.

### Start

So far *Velleman KSR10*/*OWI-535* roboarm needs to be connected
via USB and at least be detected by ``lsusb`` utility. If ``usb.core``
module will not find the arm by querying *USB* with specific vendor
and product ids, error message is displayed and then application terminates.

### Permissions

You may experience ``permission denied`` errors when controlling your
roboarm -- need to check your permissions or run application as
*superuser*/*root*.

#### Linux users

You may put ``logic3-spectravideo.rules`` included here into
``/etc/udev/rules.d/`` and then restart ``udev`` (or your operating system)
to have appropriate device in ``/dev/bus/usb/`` with correct permissions
(``a=rw``)

### KSR10/OWI-535 in action

Here you can see KSR10/OWI-535 in action, controlled with RoboUI

[![KSR10/OWI-535 roboarm in action, controlled with RoboUI](https://img.youtube.com/vi/Th3ZcczmpBA/0.jpg)](https://www.youtube.com/watch?v=Th3ZcczmpBA)
