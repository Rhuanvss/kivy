from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class Gerenciador(ScreenManager):
    pass

class PrimeiraTela(Screen):
    pass

class SegundaTela(Screen):
    pass

class Main(App):
    def build(self):
        return Gerenciador()
    
Main().run()