import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# Ultrasonic Sensor class
class Ultrasonic:
    SATTLE_TIME = 0.5
    TRIG_PULSE_TIME = 0.00001
    ULTRASONIC_TIME_TO_DISTANCE = 17150

    def __init__(self, Trig, Echo):
        self.Trig = Trig
        self.Echo = Echo
        GPIO.setup(self.Trig, GPIO.OUT)
        GPIO.setup(self.Echo, GPIO.IN)
        # Turn off trigger and let the sensor sattle
        GPIO.output(self.Trig, False)
        print ("Waiting For Sensor To Settle")
        time.sleep(self.SATTLE_TIME)

    def get_distance(self):
        time.sleep(self.SATTLE_TIME)
        GPIO.output(self.Trig, True)
        time.sleep(self.TRIG_PULSE_TIME)
        GPIO.output(self.Trig, False)

        while GPIO.input(self.Echo)==0:
            pulse_start = time.time()
        while GPIO.input(self.Echo)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * self.ULTRASONIC_TIME_TO_DISTANCE
        return round(distance, 4)

ultasonic = Ultrasonic(23, 24)

while True:
    distance = ultasonic.get_distance()
    print ((distance,))