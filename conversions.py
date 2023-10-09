"""
    Part I ­ Create Tests for Celsius Conversion returns 0.0.
"""


def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = celsius + 273.15
    kelvins = 0

    return kelvins


def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = celsius * (9 / 5) + 32
    fahrenheit = 0

    return fahrenheit

    """
    Part II ­ Implement the Celsius Conversion Functions
    """
    # converting form celsius


def convertCelsiusToKelvin_1(celsius):
    """Takes in  Celsius measurement, and returns  temperature converted into Kelvins"""
    kelvins = celsius + 273.15

    return kelvins


def convertCelsiusToFahrenheit_1(celsius):
    """Takes in  a Celsius measurement, and returns  temperature converted into Fahrenheit"""
    fahrenheit = celsius * (9 / 5) + 32

    return fahrenheit

    # converting from kelvins


def convertKelvinsToCelsius(kelvins):
    celsius = kelvins - 273.15
    return celsius


def convertKelvinsToFahrenheit(kelvins):
    fahrenheit = kelvins * (9 / 5) - 459.67
    return fahrenheit

    # converting from fahrenheit


def converFahrenheitToCelcius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def convertFahrenheitToKelvins(fahrenheit):
    kelvins = (fahrenheit + 459.67) * 5 / 9
    return kelvins
