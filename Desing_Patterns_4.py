from abc import ABC, abstractmethod
from asyncio.windows_events import NULL
import requests




class forecast_bilder(ABC):
    def __init__(self,name:str) -> None:
        self.APPID = "ec64d45f232434d9a23b90eebdf1db86"
        self.URL_BASE = "https://api.openweathermap.org/data/2.5/" 
        self.all_info=requests.get(self.URL_BASE + "weather", params=dict(q=str(name),APPID = "ec64d45f232434d9a23b90eebdf1db86")).json()
    @abstractmethod
    def produce_part_a(self) -> None:pass
    @abstractmethod
    def produce_part_b(self) -> None:pass
    @abstractmethod
    def produce_part_c(self) -> None:pass
    @abstractmethod
    def product(self) -> None:pass

class current_info():pass

class forecast_bilder_temp(forecast_bilder):
    def __init__(self,name:str) -> None:
        super().__init__(name)
        self.tempr=current_info(name)   

    def produce_part_a(self) -> None:
        self.tempr.parts['Temp']=self.all_info['main']['temp']-273
    def produce_part_b(self) -> None:
        self.tempr.parts['Feels like']=self.all_info['main']['feels_like']-273
    def produce_part_c(self) -> None:
        self.tempr.parts['Pressure']=self.all_info['main']['pressure']
    def product(self) -> current_info:
        temp=self.tempr
        del self.tempr 
        self.tempr=current_info()
        return temp

class forecast_bilder_weather(forecast_bilder):
    def __init__(self,name:str) -> None:
        super().__init__(name)
        self.weather=current_info(name)

    def reset(self):
        self.weather=current_info()

    def produce_part_a(self) -> None:
        self.weather.parts['Description']=self.all_info['weather'][0]['description']
    def produce_part_b(self) -> None:
        self.weather.parts['Wind']=self.all_info['wind']['speed']
    def produce_part_c(self) -> None:
        self.weather.parts['In nuttshell']=self.all_info['weather'][0]['main']
    def product(self) -> current_info:
        temp=self.weather
        del self.weather 
        self.reset()
        return temp


class current_info():
    def __init__(self,name:str="") -> None:
        self.parts={"name":name}
    def __str__(self) -> str:
        return str("\n".join(list(k+": "+str(self.parts[k]) for k in self.parts)))+"\n"


class WeatherReport():
    #def __init__(self) -> None:
    #    self.builder=None
    @property
    def gs_builder(self) -> forecast_bilder:
        return self.builder
    @gs_builder.setter
    def gs_builder(self, builder: forecast_bilder) -> None:
        self.builder = builder

    def take_all(self):
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

    def take_main(self):
        self.builder.produce_part_a()
        self.builder.produce_part_b()


if __name__ == "__main__":    pass
    #weather=current_info()

    #bild=forecast_bilder_weather("rom")
    #bild.produce_part_a()

    #weather=bild.product()
    #print(weather)



    #direct=WeatherReport()
    #build=forecast_bilder_weather("rom")
    #direct.gs_builder=build
    #direct.take_all()
    #wealher:current_info=build.product()
    #print(wealher)
    #print(build.product())
    


    #build=forecast_bilder_temp("toronto")
    #direct.gs_builder=build
    #direct.take_all()
    #wealher=build.product()
    #print(wealher)



    

    #pprint(current_weather(location))

