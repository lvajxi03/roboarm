#!/usr/bin/env python

"""

.. module:: roboarm
   :platform: Unix, Windows, MacOSX
   :synopsis: Control your KSR10/OWI-535 roboarm

.. moduleauthor:: Marcin Bielewicz <marcin.bielewicz@gmail.com>


``roboarm`` module provides ``RoboArm`` class, a starting point
for controlling *Velleman KSR10*/*OWI-535* roboarm

    **Detecting KSR10/OWI-535 device**

    ``RoboArm`` class contains ``vendor`` and ``product`` numbers hardcoded in
    default constructor: 0x1257 for vendor, 0x001 for product. These numbers are taken directly from ``lsusb`` output::

       $ lsusb
       Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
       Bus 002 Device 002: ID 1058:0740 Western Digital Technologies, Inc. My Passport Essential (WDBACY)
       Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
       Bus 001 Device 005: ID 1267:0001 Logic3 / SpectraVideo plc
       Bus 001 Device 004: ID 046d:c018 Logitech, Inc. Optical Wheel Mouse
       Bus 001 Device 003: ID 413c:2113 Dell Computer Corp.
       Bus 001 Device 002: ID 2109:3431 VIA Labs, Inc. Hub
       Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

    Device ``005`` on Bus ``001``, detected as *Logic3 / SpectraVideo plc* is in fact *Velleman KSR10*/*OWI-535* roboarm USB controller.
"""
import usb.core
import usb.util
import time

DefaultDuration = 0.25
"""
Default duration of RoboArm command.

.. warning::

   Can be changed only by experienced users (motors can stuck if too long)
"""

class RoboArm():
    """
    Control your roboarm with few useful methods
    """

    def __init__(self):
        """
        .. method:: __init__(self)

           Default constructor

        :raise ValueError: when arm is not connected
        """
        self.arm = usb.core.find(
            idVendor=0x1267,
            idProduct=0x001)
        if not self.arm:
            raise ValueError("Arm not connected")

    def __move_arm__(self, command, duration=DefaultDuration):
        """
        Generic roboarm command

        :param list command: list with pre-defined move state
        :param float duration: Lenght of command, in secs

        .. note::
           This is, in general, the method you *might* want to extend (errors, responses, exceptions, and so on)
        """
        # Move motor:
        self.arm.ctrl_transfer(
            0x40,
            6,
            0x100,
            0,
            command,
            3)
        time.sleep(duration)
        # Stop motor:
        Command=[0,0,0]
        self.arm.ctrl_transfer(
            0x40,
            6,
            0x100,
            0,
            command,
            3)

    def light_on(self, duration=DefaultDuration):
        """Turn the light on and sleep for ``duration`` seconds

        :param float duration: Sleep delay after switching LED on
        """
        self.__move_arm__([0,0,1], duration)

    def light_off(self, duration=DefaultDuration):
        """Turn the light off and sleep for ``duration`` seconds

        :param float duration: Sleep delay after switching LED off
        """
        self.__move_arm__([0,0,0], duration)

    def base_counterclockwise(self, duration=DefaultDuration):
        """
        Turn the base counterclockwise by the ``duration`` seconds

        :param float duration: move duration time in seconds

        .. warning::
           Base motor does not detect if end reached
        """
        self.__move_arm__([0,1,0], duration)

    def base_clockwise(self, duration=DefaultDuration):
        """
        Turn the base clockwise by the ``duration`` seconds

        :param float duration: move duration time in seconds

        .. warning::
           Base motor does not detect if end reached
        """
        self.__move_arm__([0,2,0], duration)

    def elbow_up(self, duration=DefaultDuration):
        """
        Move up elbow by the ``duration`` seconds

        :param float duration: move duration time in seconds

        .. warning::
           Elbow motor does not detect if end reached
        """
        self.__move_arm__([16,0,0], duration)

    def elbow_down(self, duration=DefaultDuration):
        """
        Move down the elbow during the ``duration`` seconds

        :param float duration: move duration time in seconds

        .. warning::
           Elbow motor does not detect if end reached
        """
        self.__move_arm__([32,0,0], duration)

    def wrist_up(self, duration=DefaultDuration):
        """
        Move up the wrist during ``duration`` seconds

        :param float duration: move duration time in seconds

        .. warning::
           Wrist motor does not detect if end reached
        """
        self.__move_arm__([4,0,0], duration)

    def wrist_down(self, duration=DefaultDuration):
        """
        Move down the wrist during ``duration`` seconds

        :param float duration: move duration time in seconds

        .. warning::
           Wrist motor does not detect if end reached
        """
        self.__move_arm__([8,0,0], duration)

    def shoulder_up(self, duration=DefaultDuration):
        """
        Move up the shoulder during ``duration`` seconds

        :param float duration: move duration time in seconds

        .. warning::
           Shoulder motor does not detect if end reached
        """
        self.__move_arm__([64,0,0], duration)

    def shoulder_down(self, duration=DefaultDuration):
        """
        Move down the shoulder during ``duration`` seconds

        :param float duration: move duration time in seconds

        .. warning::
           Shoulder motor does not detect if end reached
        """
        self.__move_arm__([128,0,0], duration)

    def grip_open(self, duration=DefaultDuration):
        """
        Widen grip by the ``duration`` seconds

        :param float duration: grip widening duration in seconds

        .. warning::
           Grip motor does not detect if fully open
        """
        self.__move_arm__([2,0,0], duration)

    def grip_close(self, duration=DefaultDuration):
        """
        Narrow grip by the ``duration`` seconds

        :param float duration: grip narrowing duration in seconds

        .. warning::
           Grip motor does not detect if fully closed
        """
        self.__move_arm__([1,0,0], duration)
