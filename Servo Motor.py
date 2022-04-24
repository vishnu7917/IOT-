import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

servo = 14
GPIO.setup(servo, GPIO.OUT)
x = GPIO.PWM(servo, 50)
cycles = [3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
x.start(2.5)

while True:
    try:
        for i in cycles:
            x.ChangeDutyCycle(i)
            time.sleep(0.5)
        for i in range(len(cycles)-1, 0, -1):
            x.ChangeDutyCycle(cycles[i])
            time.sleep(0.5)
    except KeyboardInterrupt:
        x.stop()
        GPIO.cleanup()
    except Exception as e:
        print("Error: " + str(e))
