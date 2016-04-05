from kivy.animation import Animation
from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class Cubetto(Widget):
    angolo = NumericProperty(32)


class Animator(FloatLayout):
    cubetto = ObjectProperty(None)
    INCREMENTO_LARGHEZZA = 1.3
    INCREMENTO_ANGOLO = 417

    def on_touch_down(self, touch):
        x, y = touch.pos
        if x > self.width/2:
            larghezza = self.rimpicciolisci()
        else:
            larghezza = self.ingrandisci()
        nuovo_angolo = self.ruota()
        animation = Animation(center=touch.pos, width=larghezza, angolo=nuovo_angolo, t='in_out_quad')
        animation.start(self.cubetto)

    def ruota(self):
        return self.cubetto.angolo + self.INCREMENTO_ANGOLO

    def ingrandisci(self):
        return self.cubetto.width * self.INCREMENTO_LARGHEZZA

    def rimpicciolisci(self):
        return self.cubetto.width / self.INCREMENTO_LARGHEZZA


class AnimatorApp(App):
    def build(self):
        animator = Animator()
        from utils import PrintScreenshoot
        self._print_handler = PrintScreenshoot(animator)
        return animator


if __name__ == "__main__":
    AnimatorApp().run()
