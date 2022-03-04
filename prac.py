import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
# To specify the kv design file.
# from kivy.lang import Builder
# Builder.load_file('my.kv')


class MyGridLayout(Widget):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

    name = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def press(self):                                                          # instance is like event, in this context.
        name = self.name.text                                                           # fetching textinput of variable self.name
        pwd = self.pwd.text
        # self.add_widget(Label(text=f"Name:{name}\nPassword:{pwd}"))
        print(f"Name:{name}\nPassword:{pwd}")
        # Clear the input boxes
        self.name.text = ""
        self.password.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()

