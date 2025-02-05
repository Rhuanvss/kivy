# Arquivo Python (main.py)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder

# Carregar o arquivo KV
Builder.load_file("main.kv")

class FinanceApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.saldo = 0.0
        self.ids.saldo_label.text = f"Saldo Total: R$ {self.saldo:.2f}"

    def atualizar_saldo(self):
        self.ids.saldo_label.text = f"Saldo Total: R$ {self.saldo:.2f}"

    def adicionar_dinheiro(self):
        self.criar_popup("Adicionar", self.add_to_balance)

    def sacar_dinheiro(self):
        self.criar_popup("Sacar", self.subtract_from_balance)

    def criar_popup(self, titulo, funcao_confirmar):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        input_valor = TextInput(hint_text="Digite o valor", input_filter='float', multiline=False)
        layout.add_widget(input_valor)

        buttons_layout = BoxLayout(size_hint=(1, 0.3))
        btn_confirmar = Button(text="Confirmar")
        btn_cancelar = Button(text="Cancelar")
        buttons_layout.add_widget(btn_confirmar)
        buttons_layout.add_widget(btn_cancelar)
        layout.add_widget(buttons_layout)

        popup = Popup(title=titulo, content=layout, size_hint=(0.8, 0.4))

        def confirmar(instance):
            valor = input_valor.text
            if valor:
                funcao_confirmar(float(valor))
                popup.dismiss()

        btn_confirmar.bind(on_press=confirmar)
        btn_cancelar.bind(on_press=popup.dismiss)
        popup.open()

    def add_to_balance(self, valor):
        self.saldo += valor
        self.atualizar_saldo()

    def subtract_from_balance(self, valor):
        if valor > self.saldo:
            self.criar_erro_popup("Saldo insuficiente!")
        else:
            self.saldo -= valor
            self.atualizar_saldo()

    def criar_erro_popup(self, mensagem):
        popup = Popup(title="Erro", content=Label(text=mensagem), size_hint=(0.6, 0.3))
        popup.open()

class FinanceAppMain(App):
    def build(self):
        return FinanceApp()

if __name__ == "__main__":
    FinanceAppMain().run()
