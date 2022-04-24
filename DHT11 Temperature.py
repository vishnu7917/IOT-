import RPi.GPIO as GPIO
import time
import Adafruit_DHT

GPIO.setwarnings(False)

def getData(sensor, pin):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return humidity, temperature

if __name__ == '__main__':
    while True:
        try:
            pin = 14
            sensor = 11
            humidity, temperature = getData(sensor, pin)
            print("Temp: {0:0.1f} C Humidity: {1:0.1f} %".format(temperature, humidity))
        except KeyboardInterrupt:
            print("\nExiting program.")
            break
        except Exception as e:
            print("Error: " + str(e))
        time.sleep(10)
