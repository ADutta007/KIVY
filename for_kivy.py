MyKivyFile = '''
#: import MDRaisedButton kivymd.uix.button.MDRaisedButton
#: import MDFillRoundFlatButton kivymd.uix.button.MDFillRoundFlatButton
#: import MDFlatButton kivymd.uix.button.MDFlatButton
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
#: import MDApp kivymd.app.MDApp  
#: import MDDialog kivymd.uix.dialog.MDDialog          
#: import FadeTransition kivy.uix.screenmanager.FadeTransition
#: import RiseInTransition kivy.uix.screenmanager.RiseInTransition


WindowManager:
    FirebaseLoginScreen:            
    FirstWindow:
        id:firstwindow
    AboutApp:
    
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
        app.root.current="aboutapp"
 
 
<AboutApp>:
    id: aboutapp
    name: "aboutapp"
    radius:[40,40,0,0]
    md_bg_color: 59/255,21/255,17/255,1
    ScreenManager:
        id:sm
        name:"sm"
        transition: RiseInTransition() 
        Screen:            
            name:"1"
            
            RelativeLayout:
                
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 59/255,21/255,17/255,1
                    Rectangle:
                        pos: 0, 0
                        size: self.size
                
                Image:
                    source:"walk.gif"
                MDRaisedButton:
                    rgba: 1,0,0,1
                    pos_hint: {'right': 1, 'bottom': 1}
                    text:"Next"
                    pos:self.pos                   
                    on_release:
                        sm.current="2"
                        print(self.width)
                MDRaisedButton:
                    pos_hint: {'left': 1, 'bottom': 1}
                    theme_text_color:"ContrastParentBackground"
                    bg: app.theme_cls.primary_dark
                    text:"Skip"
                    on_release:
                        app.root.current="navigate"        
        Screen:
            name:"2"
            
            RelativeLayout:
                
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 59/255,21/255,17/255,1
                    Rectangle:
                        pos: 0, 0
                        size: self.size
                
                Image:
                    source:"walk.gif"
                MDRaisedButton:
                    md_bg_color: 1,0.3,0,1
                    text:"Next"
                    pos_hint: {'right': 1, 'bottom': 1}                   
                    on_release:
                        sm.current="3"
                        print(self.width)
                MDRaisedButton:
                    theme_text_color:"ContrastParentBackground"
                    bg: app.theme_cls.primary_dark
                    text:"Skip"
                    pos_hint: {'left': 1, 'bottom': 1}
                    on_release:
                        app.root.current="navigate" 
                MDRaisedButton:
                    theme_text_color:"ContrastParentBackground"
                    bg: app.theme_cls.primary_dark
                    pos_hint: {'left': 1, 'top': 1}
                    text:"Previous"
                    pos_hint: {'left': 1, 'top': 1}
                    on_release:
                        sm.current="1" 
        Screen:
            name:"3"
            
            RelativeLayout:                
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 59/255,21/255,17/255,1
                    Rectangle:
                        pos: 0, 0
                        size: self.size
                MDLabel:
                    text:"Screen3"
                Image:
                    source:"walk.gif"
                MDRaisedButton:
                    md_bg_color: 1,0.3,0,1
                    text:"Next"
                    pos_hint: {'right': 1, 'bottom': 1}                    
                    on_release:
                        app.root.current="navigate" 
                MDRaisedButton:
                    theme_text_color:"ContrastParentBackground"
                    bg: app.theme_cls.primary_dark
                    text:"Previous"
                    pos_hint: {'left': 1, 'top': 1}
                    on_release:
                        sm.current="2"
            
                
           
    
    
    
       
       
       
          
            
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
                id: thirdwindow
            ForEvent: 
            UserStatus: 
                
           

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
                    root.screen_manager.current = "forevent"

            OneLineAvatarIconListItem:
                text: "User Status"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "userstatus"

        
<ForMap>:      
    id:mapview
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
        lat: root.my_lat if root.my_lat>0 else 27.671585080600895
        lon:root.my_lon if root.my_lat>0 else 85.36235332489015
        source:"circle_pos.gif"
         
        
            
    BoxLayout:
        id:random
        orientation: 'vertical'
        spacing: dp(20)
        MDRaisedButton:
            id:startgame
            text:"Start Game!!"      
            #pos_hint:{"x":0.5,"y":0.9}                 
            on_release:
                root.zoom=18
                root.show_points()
                self.disabled=True
                Clock.schedule_once(lambda dt: root.quit_start(), 5)
                #root.distance_gps_random()
                Clock.schedule_interval(lambda dt: root.distance_gps_random(), .5)
                #Clock.schedule_once(lambda dt: app.buffer_distance(), 5)
                #app.buffer_distance()
            on_press:
                root.clear_points()
                #disabled:True
       
        MDRaisedButton:
            text:"Center"
            on_release:
                root.center_on(root.my_lat,root.my_lon)
        MDRaisedButton:
            text:"Back"
            on_release:
                root.parent.parent.current="screen0" 
        #MDRaisedButton:
        #    id:quit
        #    text:"Quit"
        #    #disabled:False
        #    on_release:
        #        self.disabled=True
        #        Clock.schedule_once(lambda dt: root.quit(), 2)
        #        md_bg_color: (0,0,0,1)
        #        #root.quit()
        #        #app.root.ids.firstwindow.current="screen0"
    
        
              
                                       
<ThirdWindow>:
    id:thirdwindow
    name:"mapscreen"           
    ForMap:
        id:mapview
        
        
          
<ForEvent>:
    id:forevent
    name:"forevent"    
    on_pre_enter:
        a=(root.parent.parent.parent.ids.thirdwindow.ids.mapview.lat)
        print (a)

    MapView:  
        MDRaisedButton:                                
            text:"Back"                                
            on_release:                                
                root.parent.current="screen0"    
       
                   
<UserStatus>:
    id:us
    name:"userstatus"
    on_pre_enter:
        root.nnp()
        root.gc()
    
    
    
    
    MDToolbar:
        title:"User Status"        
        icon:"flip-to-back"
        elevation:11
        md_bg_color:1,0,0,1
        pos_hint:{"top":1}        
        on_action_button:
            root.parent.current="screen0"
        
    
    FloatLayout:                
        orientation: vertical
        id:userstatus
        orientation:"vertical"   
        
        MDLabel:
            id:gc_score            
            #halign:"center"
            #valign:"center"
            pos_hint:{"x":.55,"y":0.05}
        MDLabel:
            id: nnp_score
            pos_hint:{"x":.55,"y":-0.015}
        Image:             
            source:"new_nepal.png"     
            pos_hint: {"x":0.45,"y":0.45}
            allow_stretch: True
            keep_ratio:False
            size_hint: None, None
            size: 60,60     
        Image:             
            source:"greencoin.png"     
            pos_hint: {"x":0.45,"y":0.53}
            allow_stretch: True
            keep_ratio:False
            size_hint: None, None
            size: 60,60     
           
           
           
        

                   
        
        
        

'''
