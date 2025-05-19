import requests
import json
def weather_timezone(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # print(json.dumps(data,indent = 4))
        # return f"Humidity:{data['humidity']}%\n Temperature:{data['tempF']}°F\n Condition:{data['weatherDesc'][0]['value']}"
        return f"Humidity: {data['weather'][0]['hourly'][0]['humidity']}%\nTemperature: {data['weather'][0]['hourly'][0]['tempF']}°F\nCondition: {data['weather'][0]['hourly'][0]['weatherDesc'][0]['value']}"
    else:
        print("couldn't fetch the data")
# weather_timezone("seattle")
user_weather_city = input(f"enter the city: ")
weather = weather_timezone(user_weather_city)
print (f"Weather in {user_weather_city}:-\n{weather}")

      

    