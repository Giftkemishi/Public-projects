from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


# Common mobile screen sizes (choose one)
Window.size = (360, 640)   # small phone (e.g. Android 5" display)
# Window.size = (414, 896) # larger phone (e.g. iPhone 11)
# Window.size = (375, 812) # medium (e.g. iPhone X)


class LogInPage(Screen):

    #email = ObjectProperty(None)
    #password = ObjectProperty(None)

    def SignedIn(self):

        app = App.get_running_app()
        previous_screen = app.root.current

        email = self.ids.email.text
        password = self.ids.password.text

        if email.strip() != " " and password.strip() != " ":
            app.root.current = "welcome"
        else:
            self.error_popup ("InvalID login. try again!, Input something to go through")
            app.root.current = previous_screen

    def go_to_signin(self):

        self.manager.current = "sign_in"


    def error_popup(self, message):

        content = BoxLayout(orientation = 'vertical', padding = 10, spacing = 10)
        content.add_widget(Label(text = message, color=(1, 0, 0, 1), bold=True))
        btn = Button(text="Close", size_hint = (1, 0.6))
        content.add_widget(btn)

        popup = Popup (
            title = "Login Failed!",
            content = content,
            size_hint = ( None, None),
            size = (400, 200),
            auto_dismiss = False
        )

        btn.bind(on_release = popup.dismiss)
        popup.open() 

    pass

class SignInPage(Screen):
    pass

class WelcomePage(Screen):

    def go_to_login(self):

        self.manager.current = "log_in"

    pass

class LogIn(App):

    def build(self):

        sm = ScreenManager(transition = FadeTransition(duration = 0.4))
        sm.add_widget(LogInPage(name="log_in"))
        sm.add_widget(SignInPage(name="sign_in"))
        sm.add_widget(WelcomePage(name="welcome"))

        return sm


if __name__ == "__main__":
    LogIn().run()


