import kivy.properties
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.image import Image, AsyncImage
fullscreen = kivy.properties.OptionProperty('auto')


class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)

        # Background Poker Image
        self.add_widget(
            AsyncImage(
                source='https://thumbs.dreamstime.com/b/cards-green-felt-casino-table-background-cards-green-felt-casino-table-background-template-copy-space-center-138053426.jpg')
        )
        # Buttons to get to games
        self.add_widget(
            Button(
                text="Blackjack",
                size_hint=(.30, .20),
                pos_hint={'left_x': .5, 'left_y': .10}))
        self.add_widget(
            Button(
                text="Roulette",
                size_hint=(.30, .20),
                pos_hint={'left_x': .5, 'center_y': .30}))
        self.add_widget(
            Button(
                text="Slots",
                size_hint=(.30, .20),
                pos_hint={'left_x': .5, 'center_y': .50}))
        self.add_widget(
            Button(
                text="Solitaire",
                size_hint=(.30, .20),
                pos_hint={'left_x': .5, 'center_y': .70}))
        self.add_widget(
            Button(
                text="Bacarratt",
                size_hint=(.30, .20),
                pos_hint={'left_x': .5, 'center_y': .90}))
        self.add_widget(
            Button(
                text="Financials",
                size_hint=(.30, .20),
                pos_hint={'x': .7,'y': .8}))

class MainApp(App):

    def build(self):
        self.root = root = RootWidget()

        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size



if __name__ == '__main__':
    MainApp().run()