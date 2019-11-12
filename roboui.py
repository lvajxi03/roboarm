#!/usr/bin/env python

"""

.. module:: roboui
   :platform: Unix, Windows, MacOSX
   :synopsis: PyQt5 UI interface for KSR10/OWI-535 roboarm

.. moduleauthor: Marcin Bielewicz <marcin.bielewicz@gmail.com>

``roboui`` module provides ``RoboWindow`` class to control
your *Velleman KSR10*/*OWI-535* roboarm

    **Overview**

    *Velleman KSR10*/*OWI-535* roboarm contains following parts:

    * **base** (can be rotated clockwise or counterclockwise)
    * **shoulder** (can be moved up and down)
    * **wrist** (can be moved up and down)
    * **elbow** (can be moved up and down)
    * **grip** (can be opened or closed)
    * **LED light** (can be turned on or off)

    Excluding *LED light*, all other parts are controlled with sending
    appropriate command to *arm USB controller*

    .. warning::
       The command turns on the motor, which stuck if only
       motor was not stopped after a short delay.

    ``roboarm`` module defines all necessary methods in ``RoboArm`` class
    to move all controllable parts with sending a command to USB controller,
    and then to stop all motors after a short duration (predefined
    ``DefaultDuration`` is pretty good for novice users.

    **Start**

    So far *Velleman KSR10*/*OWI-535* roboarm needs to be connected
    via USB and at least be detected by ``lsusb`` utility. If ``usb.core``
    module will not find the arm by querying *USB* with specific vendor
    and product ids, error message is displayed and then application terminates.

    **Permissions**

    You may experience ``permission denied`` errors when controlling your
    roboarm -- need to check your permissions or run application as
    *superuser*/*root*.

    **Linux users**

    You may put ``logic3-spectravideo.rules`` included here into
    ``/etc/udev/rules.d/`` and then restart ``udev`` (or your operating system)
    to have appropriate device in ``/dev/bus/usb/`` with correct permissions
    (``a=rw``)

"""

import sys
import os
import usb.core

try:
    from PySide2.QtGui import QPixmap
    from PySide2.QtWidgets import QAction
    from PySide2.QtWidgets import QApplication
    from PySide2.QtWidgets import QLabel
    from PySide2.QtWidgets import QMainWindow
    from PySide2.QtWidgets import QMenu
    from PySide2.QtWidgets import QMessageBox
    from PySide2.QtWidgets import QPushButton
    from PySide2.QtWidgets import QWidget
except ImportError:
    from PyQt5.QtGui import QPixmap
    from PyQt5.QtWidgets import QAction
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtWidgets import QLabel
    from PyQt5.QtWidgets import QMainWindow
    from PyQt5.QtWidgets import QMenu
    from PyQt5.QtWidgets import QMessageBox
    from PyQt5.QtWidgets import QPushButton
    from PyQt5.QtWidgets import QWidget

import roboarm

class RoboWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__create_ui()
        try:
            self.arm = roboarm.RoboArm()
        except ValueError as ve:
            self.show_err(str(ve))
            self.close()

    def closeEvent(self, event):
        """
        Standard closeEvent handler.

        Stop the motors and accept handler (allow close)
        """
        if self.arm:
            self.arm.stop()
        event.accept()

    def __create_menu(self):
        """
        Create simple app menu
        """
        menubar = self.menuBar()
        menu = menubar.addMenu("&RoboUI")
        item = QAction("&About", self)
        item.triggered.connect(self.on_about)
        menu.addAction(item)
        menu.addSeparator()
        item = QAction("&Quit", self)
        item.triggered.connect(self.close)
        menu.addAction(item)


    def show_err(self, errmsg):
        """
        Generic messagebox with critical error displayed.

        :param str errmsg: Error message to display
        """
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText(errmsg)
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def on_about(self):
        """
        Simple about box for RoboUI
        """
        ad = QMessageBox()
        ad.setIcon(QMessageBox.Information)
        ad.setText("RoboUI\nPyQt/PySide UI for controlling KSR10/OWI-535 roboarm via USB\n(C) Marcin Bielewicz 2019-?")
#        ad.setInformativeText()
        ad.setWindowTitle("About RoboUI")
        ad.setDetailedText(
            "Please find more on github: https://github.com/lvajxi03/roboarm.git")
        ad.setStandardButtons(QMessageBox.Ok)
        ad.exec_()

    def on_baseclock(self):
        """
        Rotate the base clockwise with a duration predefined in ``roboarm`` module
        """
        try:
            self.arm.base_clockwise()
        except usb.core.USBError as usbe:
            self.show_err(str(usbe))

    def on_basecounter(self):
        """
        Rotate the base counterclockwise with a duration predefined in ``roboarm`` module
        """
        try:
            self.arm.base_counterclockwise()
        except usb.core.USBError as usbe:
            self.show_err(str(usbe))

    def on_wristup(self):
        """
        Move the wrist up with a duration predefined in ``roboarm`` module
        """
        try:
            self.arm.wrist_up()
        except usb.core.USBError as usbe:
            self.show_err(str(usbe))

    def on_wristdown(self):
        """
        Move the wrist down with a duration predefined in ``roboarm`` module
        """
        try:
            self.arm.wrist_down()
        except usb.core.USBError as usbe:
            self.show_err(str(usbe))

    def on_shoulderup(self):
        """
        Move the shoulder up with a duration predefined in ``roboarm`` module
        """
        try:
            self.arm.shoulder_up()
        except usb.core.USBError as usbe:
            self.show_err(str(usbe))

    def on_shoulderdown(self):
        """
        Move the shoulder down with a duration predefined in ``roboarm`` module
        """
        try:
            self.arm.shoulder_down()
        except usb.core.USBError as usbe:
            self.show_err(str(usbe))

    def on_elbowup(self):
        """
        Move the elbow up with a duration predefined in ``roboarm`` module
        """
        try:
            self.arm.elbow_up()
        except usb.core.USBError as usbe:
            self.show_err(str(usbe))

    def on_elbowdown(self):
        """
        Move the elbow down with a duration predefined in ``roboarm`` module
        """
        try:
            self.arm.elbow_down()
        except usb.core.USBError as usbe:
            self.show_err(str(usbe))

    def on_lighton(self):
        """
        Turn on the LED
        """
        try:
            self.arm.light_on()
        except usb.core.USBError as usbe:
            self.show_err(str(usbe))

    def on_lightoff(self):
        """
        Turn off the LED
        """
        try:
            self.arm.light_off()
        except usb.core.USBError as usbe:
            self.show_err(str(usbe))

    def on_gripopen(self):
        """
        Open the grip with a duration predefined in ``roboarm`` module
        """
        try:
            self.arm.grip_open()
        except usb.core.USBError as usbe:
            self.show_err(str(usbe))

    def on_gripclose(self):
        """
        Close the grip with a duration predefined in ``roboarm`` module
        """
        try:
            self.arm.grip_close()
        except usb.core.USBError as usbe:
            self.show_err(str(usbe))

    def __create_ui(self):
        """
        Create generic user interface
        """
        self.__create_menu()
        self.image = QLabel(self)
        pixmap = QPixmap("av9-ksr10.jpg")
        self.image.setPixmap(pixmap)
        self.baseclock = QPushButton("<<", self.image)
        self.baseclock.clicked.connect(self.on_baseclock)
        self.baseclock.move(150, 320)
        self.baseclock.resize(30, 20)
        self.basecounter = QPushButton(">>", self.image)
        self.basecounter.clicked.connect(self.on_basecounter)
        self.basecounter.move(150, 350)
        self.basecounter.resize(30, 20)
        self.lighton = QPushButton("[*]", self.image)
        self.lighton.clicked.connect(self.on_lighton)
        self.lighton.move(15, 50)
        self.lighton.resize(20, 20)
        self.lightoff = QPushButton("[ ]", self.image)
        self.lightoff.resize(20, 20)
        self.lightoff.move(15, 80)
        self.lightoff.clicked.connect(self.on_lightoff)
        self.elbowup = QPushButton("^", self.image)
        self.elbowup.clicked.connect(self.on_elbowup)
        self.elbowup.resize(20, 20)
        self.elbowup.move(220, 100)
        self.elbowdown = QPushButton("v", self.image)
        self.elbowdown.clicked.connect(self.on_elbowdown)
        self.elbowdown.resize(20, 20)
        self.elbowdown.move(220, 130)
        self.wristup = QPushButton("^", self.image)
        self.wristup.clicked.connect(self.on_wristup)
        self.wristup.resize(20, 20)
        self.wristup.move(450, 60)
        self.wristdown = QPushButton("v", self.image)
        self.wristdown.clicked.connect(self.on_wristdown)
        self.wristdown.resize(20, 20)
        self.wristdown.move(450, 90)
        self.shoulderup = QPushButton("^", self.image)
        self.shoulderup.clicked.connect(self.on_shoulderup)
        self.shoulderup.resize(20, 20)
        self.shoulderup.move(200, 210)
        self.shoulderdown = QPushButton("v", self.image)
        self.shoulderdown.clicked.connect(self.on_shoulderdown)
        self.shoulderdown.resize(20, 20)
        self.shoulderdown.move(200, 240)
        self.gripopen = QPushButton("<-  ->", self.image)
        self.gripopen.clicked.connect(self.on_gripopen)
        self.gripopen.resize(40, 20)
        self.gripopen.move(80, 180)
        self.gripclose = QPushButton("-> <-", self.image)
        self.gripclose.clicked.connect(self.on_gripclose)
        self.gripclose.resize(40, 20)
        self.gripclose.move(80, 210)
        self.setCentralWidget(self.image)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RoboWindow()
    window.show()
    sys.exit(app.exec_())
