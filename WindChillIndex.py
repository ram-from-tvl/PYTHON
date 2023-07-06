
temperature = float(input("Enter the temperature in degrees Celsius: "))
wind_speed = float(input("Enter the wind speed in kilometers per hour: "))

wind_chill_index = 13.12 + 0.6215 * temperature - 11.37 * wind_speed**0.16 + 0.3965 * temperature * wind_speed**0.16


print("The wind chill index is:", wind_chill_index)
