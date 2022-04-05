from kivy.app import App
from kivy.core.window import Window

Window.size = (400, 600)
Window.clearcolor = (100 / 255.0, 0, 2, 1)

class Login(App):
    def buildTest(self):
        self.title = 'Login'
        pass


if __name__ == '__main__':
    Login().run()
