#!/usr/bin/env python3

from mido2.mido import MidiFile
# from mido import MidiFile
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
import time
import threading


armSpeed = 35
leftArm = -21.5
rightArm = 21.5


portA = LargeMotor(OUTPUT_A)
portB = LargeMotor(OUTPUT_B)
portC = LargeMotor(OUTPUT_C)
portD = LargeMotor(OUTPUT_D)

finish = motorC = motorD = motorE = motorF = motorG = motorA = motorB = motorC2 = False

# test
# 60 - C, 62 - D, 64 -E, 65 - F, 67 - G, 69 - A, 71 - B, 72 - C2 n_for_degrees(armSpeed, leftArm)

def activeMotorC():
    flag = 0
    while finish== False:
        if (motorC == True and flag == 0):
            # motor on/ key down
            portA.on_for_degrees(armSpeed, rightArm)
            print("C state", motorC)
            flag = 1
        elif (motorC == False and flag == 1):
            flag = 0
            portA.on_for_degrees(armSpeed, leftArm)
            # motor off/ key off
            print("C state", motorC)

def activeMotorD():
    flag = 0
    while finish== False:
        if (motorD == True and flag == 0):
            # motor on/ key down
            portA.on_for_degrees(armSpeed, leftArm)
            print("D state", motorD)
            flag = 1
        elif (motorD == False and flag == 1):
            portA.on_for_degrees(armSpeed, rightArm)
            # motor off/ key off
            print("D state", motorD)
            flag = 0

def activeMotorE():
    flag = 0
    while finish== False:
        if (motorE == True and flag == 0):
            # motor on/ key down
            portB.on_for_degrees(armSpeed, rightArm)
            print("E state", motorE)
            flag = 1
        elif (motorE == False and flag == 1):
            portB.on_for_degrees(armSpeed, leftArm)
            # motor off/ key off
            print("E state", motorE)
            flag = 0

def activeMotorF():
    flag = 0
    while finish== False:
        if (motorF == True and flag == 0):
            # motor on/ key down
            portB.on_for_degrees(armSpeed, leftArm)
            print("F state", motorF)
            flag = 1
        elif (motorF == False and flag == 1):
            portB.on_for_degrees(armSpeed, rightArm)
            # motor off/ key off
            print("F state", motorF)
            flag = 0

def activeMotorG():
    flag = 0
    while finish== False:
        if (motorG == True and flag == 0):
            # motor on/ key down
            portC.on_for_degrees(armSpeed, leftArm)
            print("G state", motorG)
            flag = 1
        elif (motorG == False and flag == 1):
            portC.on_for_degrees(armSpeed, rightArm)
            # motor off/ key off
            print("G state", motorG)
            flag = 0

def activeMotorA():
    flag = 0
    while finish== False:
        if (motorA == True and flag == 0):
            # motor on/ key down
            portC.on_for_degrees(armSpeed, rightArm)
            print("A state", motorA)
            flag = 1
        elif (motorA == False and flag == 1):
            portC.on_for_degrees(armSpeed, leftArm)
            # motor off/ key off
            print("A state", motorA)
            flag = 0

def activeMotorB():
    flag = 0
    while finish== False:
        if (motorB == True and flag == 0):
            # motor on/ key down
            portD.on_for_degrees(armSpeed, leftArm)
            print("B state", motorB)
            flag = 1
        elif (motorB == False and flag == 1):
            portD.on_for_degrees(armSpeed, rightArm)
            # motor off/ key off
            print("B state", motorB)
            flag = 0

def activeMotorC2():
    flag = 0
    while finish== False:
        if (motorC2 == True and flag == 0):
            # motor on/ key down
            portD.on_for_degrees(armSpeed, rightArm)
            print("C2 state", motorC2)
            flag = 1
        elif (motorC2 == False and flag == 1):
            # motor off/ key off
            portD.on_for_degrees(armSpeed, leftArm)
            print("C2 state", motorC2)
            flag = 0

# threading.Thread(target= activeMotorC).start()
# threading.Thread(target= activeMotorD).start()
# threading.Thread(target= activeMotorE).start()
# threading.Thread(target= activeMotorF).start()
# threading.Thread(target= activeMotorG).start()
# threading.Thread(target= activeMotorA).start()
# threading.Thread(target= activeMotorB).start()
# threading.Thread(target= activeMotorC2).start()


for msg in MidiFile('beliver.mid'):
    time.sleep(msg.time)
    if not msg.is_meta:

        # C
        if(msg.type == "note_on" and msg.note == 60 ):
            portA.on_for_degrees(armSpeed, rightArm)
            motorC = True
        elif(msg.type == "note_off" and msg.note == 60):
            portA.on_for_degrees(armSpeed, leftArm)
            motorC = False
        
        # D
        if(msg.type == "note_on" and msg.note == 62 ):
            portA.on_for_degrees(armSpeed, leftArm)
            motorD = True
        elif(msg.type == "note_off" and msg.note == 62):
            portA.on_for_degrees(armSpeed, rightArm)
            motorD = False
        
        
        # E
        if(msg.type == "note_on" and msg.note == 64 ):
            portB.on_for_degrees(armSpeed, rightArm)
            motorE = True
        elif(msg.type == "note_off" and msg.note == 64):
            portB.on_for_degrees(armSpeed, leftArm)
            motorE = False

        # F
        if(msg.type == "note_on" and msg.note == 65 ):
            portB.on_for_degrees(armSpeed, leftArm)
            motorF = True
        elif(msg.type == "note_off" and msg.note == 65):
            portB.on_for_degrees(armSpeed, rightArm)
            motorF = False
        
        # G
        if(msg.type == "note_on" and msg.note == 67 ):
            portC.on_for_degrees(armSpeed, leftArm)
            motorG = True
        elif(msg.type == "note_off" and msg.note == 67):
            portC.on_for_degrees(armSpeed, rightArm)
            motorG = False
        
        # A
        if(msg.type == "note_on" and msg.note == 69 ):
            portC.on_for_degrees(armSpeed, rightArm)
            motorA = True
        elif(msg.type == "note_off" and msg.note == 69):
            portC.on_for_degrees(armSpeed, leftArm)
            motorA = False
        
        # B
        if(msg.type == "note_on" and msg.note == 71 ):
            portD.on_for_degrees(armSpeed, leftArm)
            motorB = True
        elif(msg.type == "note_off" and msg.note == 71):
            portD.on_for_degrees(armSpeed, rightArm)
            motorB = False
        
        # C2
        if(msg.type == "note_on" and msg.note == 72 ):
            portD.on_for_degrees(armSpeed, rightArm)
            motorC2 = True
        elif(msg.type == "note_off" and msg.note == 72):
            portD.on_for_degrees(armSpeed, leftArm)
            motorC2 = False

# end
motorC = motorD = motorE = motorF = motorG = motorA = motorB = motorC2 = False
finish = True
print('finish')
raise SystemExit()