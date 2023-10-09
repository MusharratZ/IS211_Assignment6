import unittest
from conversions import (
    convertCelsiusToFahrenheit,
    convertCelsiusToKelvin,
    convertCelsiusToFahrenheit_1,
    convertCelsiusToKelvin_1,
    converFahrenheitToCelcius,
    convertFahrenheitToKelvins,
    convertKelvinsToCelsius,
    convertKelvinsToFahrenheit,
)
from conversions_refactored import ConversionNotPossible, conversion


class FahrenheitConversionTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.fahrenheit = convertCelsiusToFahrenheit(10)

    def test_fahrenheit_1(self):
        """
        Test to certain if the function convertCelsiusToFahrenheit function properly
        """
        self.assertEqual(self.fahrenheit, 50, "Incorrect Fahrenheit Temperature")

    def test_fahrenheit_2(self):
        """
        Test to acertain if the function convertCelsiusToFahrenheit function properly
        """
        self.assertEqual(self.fahrenheit, 56, "Incorrect Fahrenheit Temperature")

    def test_fahrenheit_3(self):
        """
        Test 1 to acertain if the function convertCelsiusToFahrenheit function properly
        """
        self.assertEqual(self.fahrenheit, 21, "Incorrect Fahrenheit Temperature")

    def test_fahrenheit_4(self):
        """
        Test 2 to acertain if the function convertCelsiusToFahrenheit function properly
        """
        self.assertEqual(self.fahrenheit, 100, "Incorrect Fahrenheit Temperature")

    def test_fahrenheit_5(self):
        """
        Test 3 to acertain if the function convertCelsiusToFahrenheit function properly
        """
        self.assertEqual(self.fahrenheit, 70, "Incorrect Fahrenheit Temperature")


class KelvinConversionTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.kelvin = convertCelsiusToKelvin(11)

    def test_Kelvins_1(self):
        """
        Test to acertain if the function convertCelsiusToKelvins function properly
        """
        self.assertEqual(self.kelvin, 284.15, "Incorrect Kelvins Temperature")

    def test_Kelvins_2(self):
        """
        Test to acertain if the function convertCelsiusToKelvins function properly
        """
        self.assertEqual(self.kelvin, 56, "Incorrect Kelvins Temperature")

    def test_Kelvins_3(self):
        """
        Test 1 to acertain if the function convertCelsiusToKelvins function properly
        """
        self.assertEqual(self.kelvin, 21, "Incorrect Kelvins Temperature")

    def test_Kelvins_4(self):
        """
        Test 2 to acertain if the function convertCelsiusToKelvins function properly
        """
        self.assertEqual(self.kelvin, 100, "Incorrect Kelvins Temperature")

    def test_Kelvins_5(self):
        """
        Test 3 to acertain if the function convertCelsiusToKelvins function properly
        """
        self.assertEqual(self.kelvin, 70, "Incorrect Kelvins Temperature")


class ConversionTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.fahrenheit_1 = convertCelsiusToFahrenheit_1(32)
        self.kelvin_1 = convertCelsiusToKelvin_1(89)
        self.fah_cel = converFahrenheitToCelcius(21)
        self.fah_kel = convertFahrenheitToKelvins(48)
        self.kel_cel = convertKelvinsToCelsius(35)
        self.kel_fah = convertKelvinsToFahrenheit(29)

    def test_fahrenheit_1(self):
        """
        Test to acertain if the function convertCelsiusToFahrenheit_1 function
        """
        self.assertEqual(self.fahrenheit_1, 89.6)

    def test_kelvin_1(self):
        """
        Test to acertain if the function convertCelsiusToKelvin_1 functions
        """
        self.assertEqual(self.kelvin_1, 362.15)

    def test_fah_cel(self):
        """
        Test 1 to acertain if the function converFahrenheitToCelcius function
        """
        self.assertAlmostEqual(self.fah_cel, -6.11111, places=2)

    def test_fah_kel(self):
        """
        Test 2 to acertain if the function convertFahrenheitToKelvins function
        """
        self.assertAlmostEqual(self.fah_kel, 282.039, places=2)

    def test_kel_cel(self):
        """
        Test 3 to acertain if the function convertKelvinsToCelsius function
        """
        self.assertAlmostEqual(self.kel_cel, -238.15, places=2)

    def test_kel_fah(self):
        """
        Test 3 to acertain if the function convertKelvinsToFahrenheit function
        """
        self.assertEqual(self.kel_fah, -407.47)


class RefactoredConversionTest(unittest.TestCase):
    def test_temperature_conversion(self):
        # from celcius
        self.assertAlmostEqual(conversion("Celsius", "Kelvins", 0), 273.15, places=2)
        self.assertAlmostEqual(conversion("Celsius", "Fahrenheit", 12), 53.6, places=2)

        # # from kelvin
        self.assertAlmostEqual(conversion("Kelvins", "Celsius", 27), -246.15, places=2)
        self.assertAlmostEqual(
            conversion("Kelvins", "Fahrenheit", 23), -418.27, places=2
        )
        # # from fahrenheit
        self.assertAlmostEqual(
            conversion("Fahrenheit", "Kelvins", 1), 255.928, places=2
        )
        self.assertAlmostEqual(
            conversion("Fahrenheit", "Celsius", 2), -16.6667, places=2
        )

    def test_distance_conversion(self):
        # from miles
        self.assertAlmostEqual(conversion("Miles", "Yards", 1), 1760.0, places=2)
        self.assertAlmostEqual(conversion("Miles", "Meters", 1), 1609.34, places=2)
        # # from yards
        self.assertAlmostEqual(
            conversion(
                "Yards",
                "Miles",
                6,
            ),
            0.00340909,
            places=2,
        )
        self.assertAlmostEqual(conversion("Yards", "Meters", 7), 6.4008, places=2)
        # # from meters
        self.assertAlmostEqual(conversion("Meters", "Yards", 5), 5.46807, places=2)
        self.assertAlmostEqual(conversion("meters", "miles", 3), 0.00186411, places=2)

    def test_same_unit_conversion(self):
        self.assertAlmostEqual(conversion("Celsius", "Celsius", 42.0), 42.0, places=2)
        self.assertAlmostEqual(
            conversion("Fahrenheit", "Fahrenheit", 42.0), 42.0, places=2
        )
        self.assertAlmostEqual(conversion("Kelvins", "Kelvins", 42.0), 42.0, places=2)
        self.assertAlmostEqual(conversion("Meters", "Meters", 42.0), 42.0, places=2)
        self.assertAlmostEqual(conversion("Yards", "Yards", 42.0), 42.0, places=2)
        self.assertAlmostEqual(conversion("Miles", "Miles", 1000.0), 1000.0, places=2)

    def test_unsupported_conversion(self):
        with self.assertRaises(ConversionNotPossible):
            conversion("Celsius", "Miles", 13)


if __name__ == "__main__":
    unittest.main()
