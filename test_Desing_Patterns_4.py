import unittest
from Desing_Patterns_4 import *

class Test_test_Desing_Patterns_4(unittest.TestCase):
    def test_all(self):
        direct=WeatherReport()
        build=forecast_bilder_weather("rom")
        direct.gs_builder=build
        direct.take_all()
        wealher:current_info=build.product()
        t={"name":"rom",
            "Description": build.all_info['weather'][0]['description'],
            "Wind": build.all_info['wind']['speed'],
            "In nuttshell": build.all_info['weather'][0]['main']}
        self.assertEqual(wealher.parts,t)

    def test_main(self):
        direct=WeatherReport()
        build=forecast_bilder_temp("toronto")
        direct.gs_builder=build
        direct.take_main()
        wealher=build.product()
        t={"name": "toronto",
            "Temp": build.all_info['main']['temp']-273,
            "Feels like": build.all_info['main']['feels_like']-273}
        self.assertEqual(wealher.parts,t)

if __name__ == '__main__':
    unittest.main()
