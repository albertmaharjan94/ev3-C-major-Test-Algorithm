from mido import MidiFile
import time
import threading

finish = motorC = motorD = motorE = motorF = motorG = motorA = motorB = motorC2 = False

# test
# 60 - C, 62 - D, 64 -E, 65 - F, 67 - G, 69 - A, 71 - B, 72 - C2 

def activeMotorC():
    while finish== False:
        if motorC == True:
            # motor on/ key down
            print("C state", motorC)
        else:
            # motor off/ key off
            print("C state", motorC)

def activeMotorD():
    while finish== False:
        if motorD == True:
            # motor on/ key down
            print("D state", motorD)
        else:
            # motor off/ key off
            print("D state", motorD)

def activeMotorE():
    while finish== False:
        if motorE == True:
            # motor on/ key down
            print("E state", motorE)
        else:
            # motor off/ key off
            print("E state", motorE)

def activeMotorF():
    while finish== False:
        if motorF == True:
            # motor on/ key down
            print("F state", motorF)
        else:
            # motor off/ key off
            print("F state", motorF)


def activeMotorG():
    while finish== False:
        if motorG == True:
            # motor on/ key down
            print("G state", motorG)
        else:
            # motor off/ key off
            print("G state", motorG)

def activeMotorA():
    while finish== False:
        if motorA == True:
            # motor on/ key down
            print("A state", motorA)
        else:
            # motor off/ key off
            print("A state", motorA)

def activeMotorB():
    while finish== False:
        if motorB == True:
            # motor on/ key down
            print("B state", motorB)
        else:
            # motor off/ key off
            print("B state", motorB)


def activeMotorC2():
    while finish== False:
        if motorC2 == True:
            # motor on/ key down
            print("C2 state", motorC2)
        else:
            # motor off/ key off
            print("C2 state", motorC2)

threading.Thread(target= activeMotorC).start()
threading.Thread(target= activeMotorD).start()
threading.Thread(target= activeMotorE).start()
threading.Thread(target= activeMotorF).start()
threading.Thread(target= activeMotorG).start()
threading.Thread(target= activeMotorA).start()
threading.Thread(target= activeMotorB).start()
threading.Thread(target= activeMotorC2).start()


for msg in MidiFile('presence.mid'):
    time.sleep(msg.time)
    if not msg.is_meta:

        # C
        if(msg.type == "note_on" and msg.note == 60 ):
            motorC = True
        elif(msg.type == "note_off" and msg.note == 60):
            motorC = False
        
        # D
        if(msg.type == "note_on" and msg.note == 62 ):
            motorD = True
        elif(msg.type == "note_off" and msg.note == 62):
            motorD = False
        
        
        # E
        if(msg.type == "note_on" and msg.note == 64 ):
            motorE = True
        elif(msg.type == "note_off" and msg.note == 64):
            motorE = False

        # F
        if(msg.type == "note_on" and msg.note == 65 ):
            motorF = True
        elif(msg.type == "note_off" and msg.note == 65):
            motorF = False
        
        # G
        if(msg.type == "note_on" and msg.note == 67 ):
            motorG = True
        elif(msg.type == "note_off" and msg.note == 67):
            motorG = False
        
        # A
        if(msg.type == "note_on" and msg.note == 69 ):
            motorA = True
        elif(msg.type == "note_off" and msg.note == 69):
            motorA = False
        
        # B
        if(msg.type == "note_on" and msg.note == 71 ):
            motorB = True
        elif(msg.type == "note_off" and msg.note == 71):
            motorB = False
        
        # C2
        if(msg.type == "note_on" and msg.note == 72 ):
            motorC2 = True
        elif(msg.type == "note_off" and msg.note == 72):
            motorC2 = False

# end
motorC = motorD = motorE = motorF = motorG = motorA = motorB = motorC2 = False
finish = True
print('finish')
exit()