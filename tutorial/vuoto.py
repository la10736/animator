from kivy.animation import Animation
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class Cubetto(Widget):
    pass


class Animator(FloatLayout):
    cubetto = ObjectProperty(None)

    def on_touch_down(self, touch):
        animation = Animation(center=touch.pos)
        animation.start(self.cubetto)


class AnimatorApp(App):
    def build(self):
        animator = Animator()
        from utils import PrintScreenshoot
        self._print_handler = PrintScreenshoot(animator)
        return animator


if __name__ == "__main__":
    AnimatorApp().run()
