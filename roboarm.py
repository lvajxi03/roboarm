#!/usr/bin/env python

import usb.core
import usb.util
import time

DefaultDuration = 0.25

class RoboArm():
    def __init__(self):
        self.arm = usb.core.find(
            idVendor=0x1267,
            idProduct=0x001)
        if not self.arm:
            raise ValueError("Arm not connected")

    def __move_arm__(self, Command, duration=DefaultDuration):
        # Move motor:
        self.arm.ctrl_transfer(
            0x40,
            6,
            0x100,
            0,
            Command,
            3)
        time.sleep(duration)
        # Stop motor:
        Command=[0,0,0]
        self.arm.ctrl_transfer(
            0x40,
            6,
            0x100,
            0,
            Command,
            3)

    def light_on(self, duration=DefaultDuration):
        self.__move_arm__([0,0,1], duration)

    def light_off(self, duration=DefaultDuration):
        self.__move_arm__([0,0,0], duration)

    def base_anticlockwise(self, duration=DefaultDuration):
        self.__move_arm__([0,1,0], duration)

    def base_clockwise(self, duration=DefaultDuration):
        self.__move_arm__([0,2,0], duration)

    def elbow_up(self, duration=DefaultDuration):
        self.__move_arm__([16,0,0], duration)

    def elbow_down(self, duration=DefaultDuration):
        self.__move_arm__([32,0,0], duration)

    def wrist_up(self, duration=DefaultDuration):
        self.__move_arm__([4,0,0], duration)

    def wrist_down(self, duration=DefaultDuration):
        self.__move_arm__([8,0,0], duration)

    def shoulder_up(self, duration=DefaultDuration):
        self.__move_arm__([64,0,0], duration)

    def shoulder_down(self, duration=DefaultDuration):
        self.__move_arm__([128,0,0], duration)

    def grip_open(self, duration=DefaultDuration):
        self.__move_arm__([2,0,0], duration)

    def grip_close(self, duration=DefaultDuration):
        self.__move_arm__([1,0,0], duration)
