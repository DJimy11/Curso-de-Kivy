from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView


class tarefas(BoxLayout):
    def __init__(self, tf, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tf:
            self.ids.box.add_widget(Tarefa(texto=tarefa))

    def addWiget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(texto=texto))
        self.ids.texto.text = ''


class Tarefa(BoxLayout):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = texto


class Teste(App):
    def build(self):
        return tarefas(['Teste', 'testando', 'Sei lá', 'Incluir'])


Teste().run()
