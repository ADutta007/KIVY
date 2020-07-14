import kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from for_kivy import MyKivyFile
from kivy_garden.mapview import MapView
from kivy.logger import Logger
from kivymd.uix.dialog import MDDialog
from plyer import gps
from kivymd.uix.button import *
from kivy.properties import Property
from kivy.uix.popup import Popup
from kivy.clock import Clock
from android.permissions import request_permissions, Permission
request_permissions([Permission.ACCESS_COARSE_LOCATION,
                            #Permission.ACCESS_FINE_LOCATION])



class MainWindow(MDScreen):
    pass

class SecondWindow(MDScreen):
    pass


class ThirdWindow(MDScreen):
    def show_bbox(self,c):

        x=c.split(", ")
        a=[]
        print(x[2])

        for i in range(len(x)):
            a.append(i)
            a[i]=MDRectangleFlatIconButton(text=x[i],text_color=[0,0,1,1])
            print(x[i])
            print(len(a))
        a[0].pos_hint={"x":0,"y":0}
        a[1].pos_hint={"x":0,"top":1}
        a[2].pos_hint={"x":0.82,"y":0}
        a[3].pos_hint={"x":0.82,"top":1}


        for i in range(0,4):
            self.add_widget(a[i])
        #for i in range(0,4):
            #event_trig = Clock.create_trigger(self.remove_widget(a[i]), 50)
            #event_trig()



class WindowManager(ScreenManager):
    pass



class forkivymd(MDScreen):

    pass


class MyMainApp(MDApp):


    def on_start(self):
        Logger.info("Called Start!")
        gps.configure(on_location=self.on_location)
        gps.start()

    def on_location(self,**kwargs):

        Logger.info("Called on Location")
        print('lat:{lat},lon:{lon}'.format(**kwargs))
        #Logger.info(kwargs)
        #self.outputs.item_strings=["","","",str(kwargs['lat']),"","","",str(kwargs['lon']),"","","",str(random.random())]



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.outputs = None
        self.root_widget = Builder.load_string(MyKivyFile)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.icon='greencoin.png'

        return self.root_widget















if __name__ == "__main__":
    MyMainApp().run()
