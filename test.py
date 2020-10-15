#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
import time
import threading


armSpeed = 22
leftArm = -21.5
rightArm = 21.5



portA = LargeMotor(OUTPUT_A)
portB = LargeMotor(OUTPUT_B)
portC = LargeMotor(OUTPUT_C)
portD = LargeMotor(OUTPUT_D)

# C
portA.on_for_degrees(armSpeed, rightArm)
portA.on_for_degrees(armSpeed, leftArm)

# D
portA.on_for_degrees(armSpeed, leftArm)
portA.on_for_degrees(armSpeed, rightArm)

# E
portB.on_for_degrees(armSpeed, rightArm)
portB.on_for_degrees(armSpeed, leftArm)

# F
portB.on_for_degrees(armSpeed, leftArm)
portB.on_for_degrees(armSpeed, rightArm)


# G
portC.on_for_degrees(armSpeed, leftArm)
portC.on_for_degrees(armSpeed, rightArm)

# A
portC.on_for_degrees(armSpeed, rightArm)
portC.on_for_degrees(armSpeed, leftArm)


# B
portD.on_for_degrees(armSpeed, leftArm)
portD.on_for_degrees(armSpeed, rightArm)

# C2
portD.on_for_degrees(armSpeed, rightArm)
portD.on_for_degrees(armSpeed, leftArm)