class ConversionNotPossible(Exception):
    pass


def conversion(fromUnit, toUnit, value):
    """
    Converts a value from one unit to another.

    :param value: The value to be converted.
    :param from_unit: The unit to convert from (e.g., "Celsius" or "Miles").
    :param to_unit: The unit to convert to (e.g., "Kelvin" or "Yards").
    :return: The converted value as a float.
    :raises ConversionNotPossible: If the conversion is not supported.
    """
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()

    if fromUnit == toUnit:
        value = float(value)
        return value

    if fromUnit == "celsius":
        if toUnit == "kelvins":
            value = value + 273.15
            return float(value)

        elif toUnit == "fahrenheit":
            return float(value * (9 / 5) + 32)

    elif fromUnit == "kelvins":
        if toUnit == "celsius":
            value = float(value - 273.15)
            return value

        elif toUnit == "fahrenheit":
            return float(value * (9 / 5) - 459.67)

    elif fromUnit == "fahrenheit":
        if toUnit == "celsius":
            return float((value - 32) * 5 / 9)

        if toUnit == "kelvins":
            return float((value + 459.67) * 5 / 9)
    # Distance conversions
    if fromUnit == "miles":
        if toUnit == "yards":
            return float(value * 1760)

        elif toUnit == "meters":
            return float(value * 1609.34)

    elif fromUnit == "yards":
        if toUnit == "miles":
            return float(value / 1760)

        elif toUnit == "meters":
            return float(value * 0.9144)

    elif fromUnit == "meters":
        if toUnit == "miles":
            return value / 1609.34

        elif toUnit == "yards":
            return float(value / 0.9144)

    raise ConversionNotPossible(
        "Conversion from {} to {} is not supported.".format(fromUnit, toUnit)
    )