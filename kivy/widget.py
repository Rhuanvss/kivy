from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Teste(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text='botao 1')
        label = Label(text='texto foda')
        box.add_widget(button)
        box.add_widget(label)
        return box
    
Teste().run()   