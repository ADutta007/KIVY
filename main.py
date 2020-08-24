from kivy.app import App
import numpy as np
from kivy.clock import mainthread, Clock
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from numpy import random
from plyer import gps, vibrator
from kivy_garden.mapview import MapView, MapMarkerPopup, MapMarker
from for_kivy import MyKivyFile
from kivy.animation import Animation
# from FirebaseLoginScreen.firebaseloginscreen import FirebaseLoginScreen
from kivy.vector import Vector
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.factory import Factory
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivy.core.window import Window

global marker_coord
picture = {1: "new_nepal.png", 2: "greencoin.png"}
#marker_coord=[]

# ran_coord=0
# ----Java Classes For Google Login----#
# Gso= autoclass('com.google.android.gms.auth.api.signin.GoogleSignInOptions')
# GsoBuilder= autoclass('com.google.android.gms.auth.api.signin.GoogleSignInOptions$Builder')
# GSignIn= autoclass('com.google.android.gms.auth.api.signin.GoogleSignIn')
# ApiException= autoclass('com.google.android.gms.common.api.ApiException')

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class GreenCoin(MDScreen):
    pass


class AboutApp(MDScreen):
    pass


class FirstWindow(MDScreen):
    pass


class ForMap(MapView):
    gps_location = StringProperty()
    my_lat = NumericProperty()
    my_lon = NumericProperty()
    my_alt = NumericProperty()

    # ran_coord =[[NumericProperty]]

    def __init__(self, **kw):

        super().__init__(**kw)
        self.flag = False
        self.chck = 0
        #self.random_points()

        try:
            from android.permissions import request_permissions, Permission

            def callback(permissions, results):
                if all([res for res in results]):
                    print("callback. All permissions granted.")
                    gps.configure(on_location=self.on_location, on_status=self.on_auth_status)
                    gps.start(10, 0)
                else:
                    print("callback. Some permissions refused.")

            request_permissions([Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION, Permission.CAMERA,
                                 Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE], callback)
        except:
            pass

    @mainthread
    def on_location(self, *args, **kwargs):
        self.my_lat = kwargs['lat']
        self.my_lon = kwargs['lon']
        self.my_alt = kwargs['altitude']
        # print(self.my_lat,self.my_lon)

    def on_auth_status(self, general_status, status_message):
        if general_status == 'provider-enabled':
            pass
        else:
            self.open_gps_access_popup()

    def open_gps_access_popup(self):
        dialog = MDDialog(title="GPS Error", text="You need to enable GPS access for the app to function properly")
        dialog.size_hint = [.8, .8]
        dialog.pos_hint = {'center_x': .5, 'center_y': .5}
        dialog.open()

    # @mainthread
    def random_points(self):
        global marker_coord
        self.c = MapView.get_bbox(self)
        self.arr = np.array(self.c)
        # print(self.arr)
        self.lat_arr = np.random.uniform(low=self.arr[0], high=self.arr[2], size=(5))
        self.lon_arr = np.random.uniform(low=self.arr[1], high=self.arr[3], size=(5))
        marker_coord = (np.dstack((self.lat_arr, self.lon_arr))).reshape(-1, 2)
        # print(marker_coord)
        # print(len(marker_coord))

    def show_points(self):
        global marker_coord
        self.marker = []
        self.comp_logo = []
        self.marker_image = []
        #self.random_points()
        # print(marker_coord)
        for i in range(len(marker_coord)):
            # print("muji")
            self.marker.append(i)
            self.marker_image.append(i)
            self.marker[i] = MapMarkerPopup(lat=float(marker_coord[i][0]), lon=float(marker_coord[i][1]),
                                            source="gps_logo.png")
            self.add_widget(self.marker[i])

            self.marker_image[i] = picture[random.randint(1, 3)]
        # self.distance_gps_random()


    def distance_gps_random(self):
        global marker_coord, gncn, nnpal
        self.vector = []

        print('lat:', self.my_lat, "lon:", self.my_lon)

        if self.my_lat != 0:
            self.coord = Vector(self.my_lat, self.my_lon)
        else:
            self.coord = Vector(27.671585080600895, 85.36235332489015)
        # print(self.coord)
        # print(marker_coord)
        try:
            for i in range(len(marker_coord)):
                self.vector.append(i)
                self.vector[i] = (Vector(marker_coord[i].tolist())).distance(self.coord) * 10 ** 5
                print(self.vector,len(marker_coord))
                if (self.vector[i]) < 100:
                    self.distance_meet(i)
        except:
            print("vaaka")
    def distance_meet(self,i):
        global marker_coord, gncn, nnpal

        self.comp_logo.append(i)

        self.remove_widget(self.marker[i])

        self.marker[i] = MapMarkerPopup(lat=float(marker_coord[i][0]), lon=float(marker_coord[i][1]),
                                        source=self.marker_image[i])
        print("kando!!!!!!")

        self.add_widget(self.marker[i])
        if (self.marker_image[i] == "new_nepal.png"):
            # vibrator.vibrate(time=2)
            nnpal = nnpal + 1
            cam = Camera(resolution=(320, 240), play=True)
            self.add_widget(cam)
            #self.vector.pop(i)
            marker_coord = np.delete(marker_coord, i, 0)
        elif (self.marker_image[i] == "greencoin.png"):
            # vibrator.vibrate(time=2)
            gncn = gncn + 1
            cam = Camera(resolution=(320, 240), play=True)
            self.add_widget(cam)
            #self.vector.pop(i)
            marker_coord = np.delete(marker_coord, i, 0)
                # self.vector.pop(i)
                # marker_coord = np.delete(marker_coord, i, 0)

    def clear_points(self):
        self.chck += 1
        if self.chck > 1:
            for i in range(len(self.marker)):
                print(len(self.marker))
                self.remove_widget(self.marker[i])
            for j in range(len(self.comp_logo)):
                print("greencoins" + str(len(self.comp_logo)))
                self.remove_widget(self.comp_logo[j])

    def quit(self):
        self.ids.quit.disabled = False

    def quit_start(self):
        self.ids.startgame.disabled = False


b = []
nnpal = 0
gncn = 0


class ThirdWindow(MDScreen):
    pass


class UserStatus(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def nnp(self):
        global nnpal
        print("nnp ko value in ustatus" + str(nnpal))
        #print("radikoban")
        # self.ids.userstatus.add_widget(MDLabel(text=str(self.logo_value + 100), halign="center"))
        self.ids.nnp_score.text = str(nnpal)
        print(UserStatus.ids)

    def gc(self):
        global gncn
        print("gc ko value in ustatus" + str(gncn))
        #print("laudalasun")
        print(self.ids)
        self.ids.gc_score.text = str(gncn)
        print(UserStatus.ids)

    def change_it(self):
        self.parent.current = "screen0"

        # self.add_widget(MDRaisedButton(text=str(self.logo_value + 200)))


class WindowManager(ScreenManager):
    pass


class ForEvent(MDScreen):
    def open_cam(self):
        cam = Camera(resolution=(320, 240), play=True)
        self.add_widget(cam)


class MyMainApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        fm = ForMap()

        self.root_widget = Builder.load_string(MyKivyFile)

    def build(self):
        self.theme_cls.theme_style = "Light"
        # self.theme_cls.primary_palette = "Teal"
        return self.root_widget

    def recreate(self):
        self.root.clear_widgets()
        self.root.add_widget(Factory.FirstWindow())


if __name__ == "__main__":
    MyMainApp().run()
