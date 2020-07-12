MyKivyFile='''
#: import MDRaisedButton kivymd.uix.button.MDRaisedButton
#: import MDTextField kivymd.uix.textfield.MDTextField
#: import GridLayout kivymd.uix.gridlayout.GridLayout
#: import MapView kivy_garden.mapview.MapView
#: import MapMarker kivy_garden.mapview.MapMarker
#: import storagepath plyer.storagepath
#: import vibrator plyer.vibrator
#: import gps plyer.gps




WindowManager:
    MainWindow:
    SecondWindow:
    ThirdWindow:
    forkivymd:

<MainWindow>:


    name: "main"
    GridLayout:
        cols:1
        orientation:"horizontal"
        padding:60                       
        MDTextField:
            hint_text:"Code"
            fill_color:(0,4,2,1)
            pos_hint:{'center_x':0,'center_y':0.5}
            icon_left: 'key-variant'
            icon_right: 'eye-off'
            helper_text_mode: "on_focus"
            id: passw
            max_text_length: 6
            multiline: False
            password: True
            text_color:(236/255.,98/255.,81/255.,1)  
            on_text_validate:
                app.root.current = "second" if passw.text == "ashish" else "main"  
                root.manager.transition.direction = "up"
            on_double_tap:
                app.root.current = "second" if passw.text == "ashish" else "main"
            
       
            



<SecondWindow>:
    name: "second"

    GridLayout:
        cols:2
        Button:
            text:"MAP"
            on_release:
                app.root.current = "map"

        Button:
            text:"Functions"
            on_release:
                app.root.current="function"

<ThirdWindow>:
    name:"map"
    MapView:       
        id:ktm
        lat:27.6922368
        lon:85.3344256
        zoom:14
        double_tap_zoom:True
        MapMarkerPopup:
            source:"gps_logo.png"
            lat:27.6922368
            lon:85.3344256
            MDRaisedButton:
                text:"Go bAck!"                       
                on_release:    
                    print(ktm.get_bbox())
        MDRaisedButton:
            text:"GET GPS"
            on_release:        
                gps.configure(27,85)
                gps.start(10,0.1)                
       
    
              
<forkivymd>:
    name:"function"
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        MDRaisedButton:
            text:"Vibrate"
            on_release:
                vibrator.vibrate(time=4)
        MDRaisedButton:
            text:"Go bAck!"
            on_release:
                app.root.current="second"
                root.manager.transition.direction = "down"

'''

