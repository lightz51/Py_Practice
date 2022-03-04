import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 1
        self.row_force_default = True
        self.row_default_height = 100
        self.inner_grid = GridLayout(row_force_default=True, row_default_height=50)
        self.inner_grid.cols = 2
        self.inner_grid.add_widget(Label(text="Name: "))
        # self.inner_grid.add_widget(Label(text="Name: ", size_hint_y=None, height=50))

        self.name = TextInput(multiline=False)
        self.inner_grid.add_widget(self.name)

        self.inner_grid.add_widget(Label(text="Password: "))

        self.password = TextInput(multiline=False)
        self.inner_grid.add_widget(self.password)

        self.add_widget(self.inner_grid)

        self.submit = Button(text="Submit", size_hint_y=None, height=50)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):                                                          # instance is like event, in this context.
        name = self.name.text                                                           # fetching textinput of variable self.name
        pwd = self.password.text
        self.add_widget(Label(text=f"Name:{name}\nPassword:{pwd}"))

        #Clear the input boxes
        self.name.text = ""
        self.password.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()

