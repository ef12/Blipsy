import RPi.GPIO as GPIO
from time import sleep

# D.C. Motor class
class DcMotor():
    def __init__(self, Ena, In1, In2):
        self.Freq = 100
        self.Ena = Ena
        self.In1 = In1
        self.In2 = In2
        GPIO.setup(self.Ena, GPIO.OUT)
        GPIO.setup(self.In1, GPIO.OUT)
        GPIO.setup(self.In2, GPIO.OUT)
        # set pwm to control the speed.
        self.pwm = GPIO.PWM(self.Ena,self.Freq)
        self.pwm.start(0)

    def move(self, speed):
        self.speed = speed
        if self.speed > 0:
            GPIO.output(self.In1, GPIO.LOW)
            GPIO.output(self.In2, GPIO.HIGH)
        if self.speed < 0:
            GPIO.output(self.In1, GPIO.HIGH)
            GPIO.output(self.In2, GPIO.LOW)
        if self.speed == 0:
            GPIO.output(self.In1, GPIO.LOW)
            GPIO.output(self.In2, GPIO.LOW)

        self.pwm.ChangeDutyCycle(abs(self.speed))

STATE_IDLE = 0
STATE_FORWARD_ACCELERATE = 1
STATE_FORWARD_DECCELERATE = 2
STATE_BACKWARD_ACCELERATE = 3
STATE_BACKWARD_DECCELERATE = 4

MINIMUM_SPEED = 20
State = STATE_IDLE

GPIO.setmode(GPIO.BCM)
right_motor = DcMotor(18, 14, 15)
left_motor = DcMotor(22, 17, 27)

speed = 0

while True:
    if State == STATE_IDLE:
        State = STATE_FORWARD_ACCELERATE
        speed = 20

    elif State == STATE_FORWARD_ACCELERATE:
        speed = speed + 1
        if speed > 100:
            speed = 100
            State = STATE_FORWARD_DECCELERATE

    elif State == STATE_FORWARD_DECCELERATE:
        speed = speed - 1
        if speed == 0:
            State = STATE_BACKWARD_ACCELERATE

    elif State == STATE_BACKWARD_ACCELERATE:
        speed = speed - 1
        if speed < -100 :
            speed = -100
            State = STATE_FORWARD_ACCELERATE

    print ((speed,))

    right_motor.move(speed)
    left_motor.move(speed)

    sleep(0.1)