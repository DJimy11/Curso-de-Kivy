from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


# Uma tela de login que herda característica do GridLayoult
class TelaLogin(GridLayout):
    def __init__(self, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        self.cols = 2
        global c
        c = 0
        self.add_widget(Label(text='Nome de Usuário'))
        self.usuario = TextInput(text=f'Dumilde {c}', multiline=False)
        self.add_widget(self.usuario)
        self.add_widget(Label(text='Senha'))
        self.senha = TextInput(password=True, multiline=False)
        self.add_widget(self.senha)
        self.botão = Button(text='ENTRAR', font_size=30, on_release=self.incrementar)
        self.add_widget(self.botão)

# Função que será acionada sempre que um clique for dado no botão. Acionado pelo evento on_release
    def incrementar(self, botão):
        global c
        c += 1
        self.usuario.text = f'Dumilde {c}'


# Uma classe que constrói todos os Widgets adicionados na classe TelaLogin
class MinhaAplicação(App):
    def build(self):
        return TelaLogin()


# O comando que faz a nossa aplicação funcionar
if __name__ == '__main__':
    MinhaAplicação().run()

