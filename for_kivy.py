MyKivyFile = '''
#: import MDRaisedButton kivymd.uix.button.MDRaisedButton
#: import MDFillRoundFlatButton kivymd.uix.button.MDFillRoundFlatButton
#: import MDTextField kivymd.uix.textfield.MDTextField
#: import GridLayout kivymd.uix.gridlayout.GridLayout
#: import BoxLayout kivymd.uix.boxlayout.BoxLayout
#: import FloatLayout kivymd.uix.floatlayout.FloatLayout
#: import MDLabel kivymd.uix.label.MDLabel
#: import MapView kivy_garden.mapview.MapView
#: import MapMarker kivy_garden.mapview.MapMarker
#: import storagepath plyer.storagepath
#: import vibrator plyer.vibrator
#: import gps plyer.gps
#: import MDDialog kivymd.uix.dialog.MDDialog
#: import Property kivy.properties.Property
#: include FirebaseLoginScreen/firebaseloginscreen.kv
#: import FirebaseLoginScreen FirebaseLoginScreen.firebaseloginscreen.FirebaseLoginScreen
#: import utils kivy.utils
#: import Clock kivy.clock.Clock              



WindowManager:
    FirebaseLoginScreen:        
    FirstWindow:
    
<FirebaseLoginScreen>:
    name: "firebase_login_screen"
    
    canvas.before:
        Rectangle:
            size: self.size
            pos: self.pos
    
            

    
    web_api_key: "AIzaSyB-nrusoHjlBoJstkDk0Inpc38OvLDvLYM"
    primary_color: utils.get_color_from_hex("#EE682A")
    secondary_color: utils.get_color_from_hex("#060809")
    tertiary_color: (.25, .25, .25, 1)
    on_login_success:
        app.user_localId = self.localId
        app.user_idToken = self.idToken
        app.root.current="navigate"
        
            
<FirstWindow>:  
    on_pre_enter:
        print("keraaando")  
    name:"navigate"
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Hello User"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        

    NavigationLayout:
        x: toolbar.height

        WindowManager:
            id: screen_manager
            
            GreenCoin:
                name:"screen0"
                MDFillRoundFlatButton:
                    text:"GREENCOINS"
                    icon:"greencoin.png"
                    pos_hint:{"center_x":0.5,"center_y":0.5}  
                    
                
            ThirdWindow:
            forkivymd: 
            UserStatus:
                name:"userstatus"    
           

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager.__self__
                nav_drawer: nav_drawer.__self__
                
<ContentNavigationDrawer>:

    ScrollView:
        MDList:        
            OneLineAvatarIconListItem:
                text: "Home Page"
                font_style:"Button"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "screen0"

            
            OneLineAvatarIconListItem:    
                text: "Treasure Hunt!"  
                IconLeftWidget:
                    icon:"gamepad"
                    on_touch_down:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "mapscreen"                   
                
                    

            OneLineAvatarIconListItem:
                text: "For Events"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "function"

            OneLineAvatarIconListItem:
                text: "User Status"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "userstatus"

        

<ForMap>:      
    outer_opacity: 1
    lat:root.my_lat if root.my_lat>0 else 27.671585080600895
    lon:root.my_lon if root.my_lat>0 else 85.36235332489015
    zoom:15
    double_tap_zoom:True    
    on_zoom:
        self.zoom=14 if self.zoom<14 else self.zoom
        
    MapMarker:  
        id:blinker   
        default_blink_size: 25
        blink_size: 25    
        lat:root.my_lat if root.my_lat>0 else 27.671585080600895
        lon:root.my_lon if root.my_lat>0 else 85.36235332489015
        source:"green_gps_logo.png"
         
        
            
    BoxLayout:
        id:random
        orientation: 'vertical'
        spacing: dp(20)
        MDRaisedButton:
            text:"Start Game!!"      
            #pos_hint:{"x":0.5,"y":0.9}                 
            on_release:
                root.zoom=18
                root.show_points()
                #disabled:True
                #root.distance_gps_random()
                Clock.schedule_interval(lambda dt: root.distance_gps_random(), 2)
                #Clock.schedule_once(lambda dt: app.buffer_distance(), 5)
                #app.buffer_distance()
            on_press:
                root.clear_points()
       
        MDRaisedButton:
            text:"Center"
            on_release:
                root.center_on(root.my_lat,root.my_lon)
        
                
                                       
<ThirdWindow>:
    name:"mapscreen"           
    ForMap:
        id:mapview
          
<forkivymd>:
    name:"function"
    BoxLayout:
        orientation:"horizontal"
        spacing: dp(20)
        
        MDRaisedButton:
            text:"Vibrate"
            on_release:
                vibrator.vibrate(time=2)
                
<UserStatus>:
    BoxLayout:
        id:userstatus
        orientation:"vertical"
    #Image:
        #source:"walk.gif"
        
        

'''

