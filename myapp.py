from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (350, 520)


# ---------- HOME SCREEN ----------
class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        # Plus button
        btn = Button(
            text="+",
            font_size="50sp",
            size_hint=(None, None),
            size=(60, 60),
            pos_hint={"right": 0.95, "y": 0.08}
        )

        btn.bind(on_press=self.go_add)

        # Add widgets (order matters)
        layout.add_widget(bg)
        layout.add_widget(btn)

        self.add_widget(layout)

    def go_add(self, instance):
        self.manager.current = "add"


# ---------- ADD SCREEN ----------
class AddScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        back = Button(
            text="Back",
            size_hint=(None, None),
            size=(80, 40),
            pos_hint={"x": 0.05, "y": 0.9}
        )
        
        back.bind(on_press=self.go_back)

        layout.add_widget(bg)        
        layout.add_widget(back)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = "home"


# ---------- APP ----------
class Notes(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(AddScreen(name="add"))
        return sm


Notes().run()

