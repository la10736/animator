from kivy.animation import Animation
from kivy.app import App
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class Component(Widget):
    angle = NumericProperty()


class Animator(FloatLayout):
    component = ObjectProperty(None)
    INCREMENTO_ANGOLO = 476
    INCREMENTO_LARGHEZZA = 1.3
    TRANSIZIONE = "in_out_circ"

    def libera_component(self):
        self.component.pos_hint = {}
        self.component.size_hint = None, None

    def riduci_larghezza(self):
        return self.component.width / self.INCREMENTO_LARGHEZZA

    def aumenta_larghezza(self):
        return self.component.width * self.INCREMENTO_LARGHEZZA

    def on_touch_down(self, touch):
        self.libera_component()

        nuovo_angolo = self.component.angle + self.INCREMENTO_ANGOLO
        nuova_larghezza = self.aumenta_larghezza() if touch.x < self.width/2 else self.riduci_larghezza()
        Animation(center=touch.pos,
                  angle=nuovo_angolo,
                  width=nuova_larghezza,
                  t=self.TRANSIZIONE).start(self.component)


class AnimatorApp(App):
    def build(self):
        animator = Animator()
        from utils import PrintScreenshoot
        self._print_handler = PrintScreenshoot(animator)
        return animator


if __name__ == "__main__":
    AnimatorApp().run()
