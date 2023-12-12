from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial


class botão(App):

    def disable(self, instance, *args):
        instance.disabled = True


    def update(self, instance, *args):
        instance.update = 'Desabiliado'

    def build(self):
        meu_butão = Button(text='Clica para desativar')

        meu_butão.bind(on_press=partial(self.disable, meu_butão))
        meu_butão.bind(on_press= partial(self.update, meu_butão))

        return meu_butão

botão().run()
