import kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from for_kivy import MyKivyFile
from kivy_garden.mapview import MapView
from plyer import gps



class MainWindow(MDScreen):
    pass

class SecondWindow(MDScreen):
    pass


class ThirdWindow(MDScreen):
    pass

class Map(MapView):
    pass
class WindowManager(ScreenManager):
    pass



class forkivymd(MDScreen):

    pass


class MyMainApp(MDApp):


    def on_start(self):

       gps.configure(on_location=self.on_gps_location)

       gps.start()

    def on_gps_location(self,**kwargs):

       kwargs['lat']=27

       kwargs['lon']=85

       print(kwargs)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root_widget = Builder.load_string(MyKivyFile)

    def build(self):
        self.theme_cls.theme_style = "Dark"

        return self.root_widget


if __name__ == "__main__":
    MyMainApp().run()
