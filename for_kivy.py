MyKivyFile='''
#: import MDRaisedButton kivymd.uix.button.MDRaisedButton
#: import MDFillRoundFlatButton kivymd.uix.button.MDFillRoundFlatButton
#: import MDTextField kivymd.uix.textfield.MDTextField
#: import GridLayout kivymd.uix.gridlayout.GridLayout
#: import BoxLayout kivymd.uix.boxlayout.BoxLayout
#: import FloatLayout kivymd.uix.floatlayout.FloatLayout

#: import MapView kivy_garden.mapview.MapView
#: import MapMarker kivy_garden.mapview.MapMarker
#: import storagepath plyer.storagepath
#: import vibrator plyer.vibrator
#: import gps plyer.gps
#: import MDDialog kivymd.uix.dialog.MDDialog
#: import Property kivy.properties.Property




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
        lat:27.671613585742858
        lon:85.36233186721803
        zoom:14
        double_tap_zoom:True
        MapMarkerPopup:
            source:"gps_logo.png"
            lat:27.671613585742858
            lon:85.36233186721803
            MDRaisedButton:
                text:"Get edge coordinates!"                       
                on_release:
                    
                    root.show_bbox(str(ktm.get_bbox()))
                
                      
    FloatLayout:            
        MDRaisedButton:
            text:"Locate"
            pos_hint:{"x":0.5,"y":0}
            on_release:        
                app.on_star()
        MDFillRoundFlatButton:
            text:"Go Back!!"
            pos_hint:{"x":0.35,"y":0}
            color:0,1,0,0
            on_release:
                app.root.current="second"
                root.manager.transition.direction = "right"                                            
       
    
              
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

