import requests, json

#Enter Your API key here
api_key = "6c354a3e64100b9e6d9feca83f29b75e"

#Base Url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

#Taking City Input From User
city_name = input("Enter City Name : ")

#Now Make Complete Url
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

#Return Response Object
response = requests.get(complete_url)

#####################

x = response.json()
print(x)


if x["cod"] != "404":
    y = x["main"]

    current_temperature = y["temp"]

    current_pressure = y["pressure"]

    current_humidity = y["humidity"]

    z = x["weather"]

    weather_description = z[0]["description"]

    print(" Temperature (In Kelvin) = " +
          str(current_temperature) +
          "\n Atmospheric Pressure (In hPa ) = " +
          str("current_pressure") +
          "\n Humidity (In Percentage) = " +
          str(current_humidity) +
          "\n Description = " +
          str(weather_description))
else:
    print("City Not Found ")
