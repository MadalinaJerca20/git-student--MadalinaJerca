def weather_info(temp):
    celsius = (temp - 32) * (5.0 / 9.0)
    if celsius > 0:
        return '{} is above freezing temperature'.format(celsius)
    return '{} is freezing temperature'.format(celsius)


print(weather_info(50), '10.0 is above freezing temperature')
print(weather_info(23), '-5.0 is freezing temperature')


'''
# The wrong code:
    def weather_info (temp):
        c : convert(temp)
        if (c > 0):
            return (c + " is freezing temperature")
        else:
            return (c + " is above freezing temperature")

    def convert_to_celsius (temperature):
    var celsius = (tempertur) - 32 + (5/9)
    return temperature

# Details
    Debug celsius converter
    Your friend is traveling abroad to the United States so he wrote a program to convert fahrenheit to
    celsius. Unfortunately his code has some bugs.
    Find the errors in the code to get the celsius converter working properly.
        To convert fahrenheit to celsius:
        celsius = (fahrenheit - 32) * (5/9)
    Remember that typically temperatures in the current weather conditions are given in whole numbers.
    It is possible for temperature sensors to report temperatures with a higher accuracy such as to the
    nearest tenth. Instrument error though makes this sort of accuracy unreliable for many types of
    temperature measuring sensors.
'''
