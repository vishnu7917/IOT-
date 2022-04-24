import Adafruit_DHT
import requests
import time

KEY = 'YOUR_API_KEY'
url = 'https://api.thingspeak.com/update'
def getData(sensor, pin):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return humidity, temperature

def pushData(temp,humi):
    params = {'key': KEY, 
            'field1': temp, 
            'field2': humi
            }
    res = requests.request('GET', url, params=params)
    return res.status_code
if __name__ == '__main__':
    while True:
        try:
            sensor = 11
            pin = 14
            humidity, temperature = getData(sensor, pin)
            print("Temp: {0:0.1f} C Humidity: {1:0.1f} %".format(temperature, humidity))
            response = pushData(temperature, humidity)
            if response == 200:
                print("Data pushed to thingspeak.com")
            elif response == 400:
                print("Bad request, check your write key")

        except KeyboardInterrupt:
            print("\nExiting program.")
            break
        except Exception as e:
            print("Error: " + str(e))
            time.sleep(2.0)
            continue
        time.sleep(10) # Wait 10 seconds
