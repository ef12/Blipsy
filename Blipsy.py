
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