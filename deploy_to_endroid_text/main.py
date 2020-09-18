from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton


class DemoApp(MDApp):
    def build(self):
        label = MDLabel(text='Hello world', halign='center', theme_text_color='Custom',
                        text_color=(0,0,1,1))
        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5}
            )
        )
        return screen


DemoApp().run()
