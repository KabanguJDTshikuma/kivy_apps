from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


class NoobWidget(BoxLayout):
    def update_label(self):
        self.ids.label_update.text = "Clicked"



class NoobApp(App):
    def build(self):
        return NoobWidget()


if __name__ == '__main__':
    NoobApp().run()