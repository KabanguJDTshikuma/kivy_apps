from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout


class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        if len(self.name.text) > 1 and len(self.email.text) > 1:
            print(f"Name: {self.name.text}, Email: {self.email.text}")
            self.name.text = ""
            self.email.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
