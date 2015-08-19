# reset.py
# by Anthony Butler, 2015
#
import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# these are the GPIO pins used by the stepper motor control board
coil_A_1_pin = 17
coil_A_2_pin = 27
coil_B_1_pin = 18
coil_B_2_pin = 22
coil_C_1_pin = 23
coil_C_2_pin = 25
coil_D_1_pin = 24
coil_D_2_pin = 4

# set the GPIO pins as output using GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
GPIO.setup(coil_C_1_pin, GPIO.OUT)
GPIO.setup(coil_C_2_pin, GPIO.OUT)
GPIO.setup(coil_D_1_pin, GPIO.OUT)
GPIO.setup(coil_D_2_pin, GPIO.OUT)

# procedure to turn both motors at the same time - anticlockwise
def antiboth(delay, steps):  
  for i in range(0, steps):
    setStep(1, 0, 1, 0, 1, 0, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 1, 0, 0, 1, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 0, 1, 0, 1, 0, 1)
    time.sleep(delay)
    setStep(1, 0, 0, 1, 1, 0, 0, 1)
    time.sleep(delay)
    
# procedure to turn both motors at the same time - clockwise
def clockboth(delay, steps):  
  for i in range(0, steps):
    setStep(1, 0, 0, 1,1,0,0,1)
    time.sleep(delay)
    setStep(0, 1, 0, 1,0,1,0,1)
    time.sleep(delay)
    setStep(0, 1, 1, 0,0,1,1,0)
    time.sleep(delay)
    setStep(1, 0, 1, 0,1,0,1,0)
    time.sleep(delay)

# procedure to turn LEFT motor only - anticlockwise
def antileft(delay, steps):  
  for i in range(0, steps):
    setStep(1, 0, 1, 0,0,0,0,0)
    time.sleep(delay)
    setStep(0, 1, 1, 0,0,0,0,0)
    time.sleep(delay)
    setStep(0, 1, 0, 1,0,0,0,0)
    time.sleep(delay)
    setStep(1, 0, 0, 1,0,0,0,0)
    time.sleep(delay)

# procedure to turn LEFT motor only - clockwise
def clockleft(delay, steps):  
  for i in range(0, steps):
    setStep(1, 0, 0, 1,0,0,0,0)
    time.sleep(delay)
    setStep(0, 1, 0, 1,0,0,0,0)
    time.sleep(delay)
    setStep(0, 1, 1, 0,0,0,0,0)
    time.sleep(delay)
    setStep(1, 0, 1, 0,0,0,0,0)
    time.sleep(delay)     

# procedure to turn RIGHT motor only - anticlockwise
def antirite(delay, steps):  
  for i in range(0, steps):
    setStep(0,0,0,0,1, 0, 1, 0)
    time.sleep(delay)
    setStep(0,0,0,0,0, 1, 1, 0)
    time.sleep(delay)
    setStep(0,0,0,0,0, 1, 0, 1)
    time.sleep(delay)
    setStep(0,0,0,0,1, 0, 0, 1)
    time.sleep(delay)

# procedure to turn RIGHT motor only - clockwise
def clockrite(delay, steps):  
  for i in range(0, steps):
    setStep(0,0,0,0,1, 0, 0, 1)
    time.sleep(delay)
    setStep(0,0,0,0,0, 1, 0, 1)
    time.sleep(delay)
    setStep(0,0,0,0,0, 1, 1, 0)
    time.sleep(delay)
    setStep(0,0,0,0,1, 0, 1, 0)
    time.sleep(delay)

# this procedure turns the GPIO pins on and off which activates the
# magnets in the stepper motors in the correct sequence
def setStep(w1, w2, w3, w4, w5, w6, w7, w8):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)
  GPIO.output(coil_C_1_pin, w5)
  GPIO.output(coil_C_2_pin, w6)
  GPIO.output(coil_D_1_pin, w7)
  GPIO.output(coil_D_2_pin, w8) 


# main program begine here
# simple version of pi
frac = 3.142

while True:
  # gets the delay between magnet activations, minimum is 2, more than
  # 50 and the motors will take ages to turn
  delay = raw_input("Delay on motion? (2 - 50)")
  if int(delay) < 2 or int(delay) > 50:
    delay = 10
    print ("I'm going to ignore that as it's out of range!")
  print ("Delay = ", delay)
  # gets which motor you want to turn, LEFT, RIGHT or BOTH
  motors = raw_input("Left, Right or Both Motors? (L, R or B)")
  # gets which direction you want the motors to turn in
  direction = raw_input("Clockwise or Anticlockwise (C or A)? ")
  # gets how many degrees to turn the motor/s
  degrees = float(raw_input("How many degrees?"))
  # how much of a full rotation is required
  frac = float(degrees/360)
  # there are 512 steps per full rotation, so how many to turn the
  # requested number of degrees
  steps = (frac * 512)
  # now tell the motors to turn
  if motors[0] == "l":
    # its a LEFT motor only
    if direction[0] == "a":
      # its anticlockwise
      antileft(int(delay) / 1000.0, int(steps))
    else:
      # it's clockwise
      clockleft(int(delay) / 1000.0, int(steps))
  elif motors[0] == "r":
    # its a RIGHT motor only
    if direction[0] == "a":
      # its anticlockwise
      antirite(int(delay) / 1000.0, int(steps))
    else:
      # its clockwise
      clockrite(int(delay) / 1000.0, int(steps))
  else:  # motors[0] == "b":
    # its BOTH motors
    if direction[0] == "a":
      # antoclockwise
      antiboth(int(delay) / 1000.0, int(steps))
    else:
      # clockwise
      clockboth(int(delay) / 1000.0, int(steps))
# now go back to the start of the while-loop
