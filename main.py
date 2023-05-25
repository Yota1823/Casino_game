import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 3


        self.add_widget(Label(text="Username: "))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.password = TextInput(multiline=False)
        self.add_widget(Label(text="Password: "))
        self.add_widget(self.password)

        button = Button()
        button.text = 'Log in'
        self.add_widget(button)

class MyApp(App):

    def build(self):
        box = BoxLayout(orientation='vertical')
        grid = MyGrid()


        box.add_widget(grid)

        return box



if __name__ == '__main__':
    MyApp().run()