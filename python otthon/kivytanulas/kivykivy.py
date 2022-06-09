import os
from tkinter import UNDERLINE
from tkinter.font import ITALIC
from turtle import onclick
os.environ["KIVY_NO_CONSOLELOG"] = "1"
cwd = os.getcwd()
os.environ["KIVY_HOME"] = cwd + "/python otthon/kivytanulas/conf"

from kivy.config import Config
Config.set("graphics","width","1280")
Config.set("graphics","height","720")
Config.set("graphics","resizable","0") #Nem méretezhető / Két értéke lehet, 0 vagy 1
#Config.set("graphics","borderless","0")
#C:\Felhasználók\Atisd\.kivy\config.ini
#Config.write()  #Átírja a fájlt

from kivy.app import App
from kivy.uix.widget import Widget
#from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

"""
class AlapWidget(BoxLayout):
    def __init__(self):
        super().__init__()

        self.orientation = "vertical" #vagy horizontal
        self.spacing = 20
        self.padding = 20
        button1 = Button(text="Button 1", size_hint=(0.2,0.5)) #size=(100,50), pos=(0,0)
        button1.bind(on_press=self.hello_gomb)
        self.add_widget(button1)

        button2 = Button(text="Button 2")
        button2.bind(on_press=self.hello_gomb)
        self.add_widget(button2)

    def hello_gomb(self, instance):
        print("Hello")
"""
class AlapWidget(FloatLayout):
    def __init__(self):
        super().__init__()

        button1 = Button(text="Button 1", size_hint=(0.2,0.5)) #size=(100,50), pos=(0,0)
        button1.bind(on_press=self.hello_gomb)
        self.add_widget(button1)

        button2 = Button(text="Button 2")
        button2.bind(on_press=self.hello_gomb)
        self.add_widget(button2)

def hello_gomb(self, instance):
    print("Hello")
    

class TesztApp(App):
    def build(self):
        #return Label(text="Hello World!", font_size = 60, italic = True, underline = True, color=(1, 0.5, 0, 1))
        #return Label(text="[color=ff0000]Hello[/color][color=00ff00] World! [/color]", markup = True)
        return AlapWidget()


TesztApp().run()