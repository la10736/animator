# Cubetto Cubetto Rotola

Dobbiamo far rotolare, anzi ruotare suse stesso. Sappiamo già come fare per *ruotare il foglio di disegno* dove
cubetto viene disegnato. Dobbiamo solo fare in maniera di poter scegliere l'angolo senza doverlo scrivere a mano.

## Ruotiamo Cubetto

Quindi se vogliamo ruotare cubetto di 32 gradi dobbiamo *ruotare la tela di 32 gradi prima di disegnare il resto*. 
Nella tela ( `canvas` ) di `<Cubetto>`facciamo una rotazione di 32 prima di tutto il resto: `animator.kv`
 
```
<Cubetto>:
    height: self.width
    canvas:
        Rotate:
            angle: 32
            origin: self.center
        ...
```

Adesso cumetto è ruotato.

## angolo, una nuova proprietà di Cubetto

Vogliamo quindi definire una nuova proprità di `Cubetto` come la larghezza ( `width` ) o l'altezza ( `height` ). In
`main.py` cambiamo `Cubetto` aggiungendo la proprietà numerica `angolo`. Mettiamo in alto

```python
from kivy.properties import NumericProperty
```

e cambiamo `Cubetto`

```python
class Cubetto(Widget):
    angolo = NumericProperty(32)
```

**GRANDE** Ora possiamo sostituire nel file `animator.kv` il numero 32 con `self.angolo`:

```
<Cubetto>:
    height: self.width
    canvas:
        Rotate:
            angle: self.angolo
            origin: self.center
        ...
```

Ora cambiando `angolo` di cubetto possiamo ruotarlo. Facciamo a ogni movimento.
 
## Rotazione.... morbida

Ormai abbiamo capito: basta cambiare `Animation()` aggiungendo `angolo=nuovo_angolo` e `nuovo_angolo` lo calcoliamo 
sommando `417` al vecchio.

```python
        animation = Animation(center=touch.pos, width=larghezza, angolo=self.cubetto.angolo + 417 , t='in_out_quad')
```

Ancora un piccolo sforzo:

1. `417` lo chiamiamo `INCREMENTO_ANGOLO`
2. faciamo una funziona `ruota()` per calcolare il `nuovo_angolo`

```python
class Animator(FloatLayout):
    ...
    INCREMENTO_ANGOLO = 417

    def on_touch_down(self, touch):
        ...
        nuovo_angolo = self.ruota()
        animation = Animation(center=touch.pos, width=larghezza, angolo=nuovo_angolo, t='in_out_quad')
        animation.start(self.cubetto)

    def ruota(self):
        return self.cubetto.angolo + self.INCREMENTO_ANGOLO

```

**ECCO FATTO**

`main.py`

```python
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
```

`animator.kv`
```
#:kivy 1.0.9
#:set nero (0, 0, 0)
#:set bianco (1, 1, 1)
#:set rosso (1, 0, 0)
#:set verde (0, 1, 0)
#:set blu (0, 0, 1)

<Cubetto>:
    height: self.width
    canvas:
        Rotate:
            angle: self.angolo
            origin: self.center
        Color:
            rgb: rosso
        Rectangle:
            pos: self.pos
            size: self.size
        Rotate:
            angle: 45
            origin: self.center
        Color:
            rgb: blu
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgb: nero
        Ellipse:
            pos: self.pos
            size: self.size


<Animator>:
    cubetto: cubetto_id

    Cubetto:
        id: cubetto_id
        center: root.width*0.5, root.height * 0.5
        size_hint: None,None
        width: dp(50)
```

* [**NEXT** Cubetto Contest](contest.md)
* [**PREV** Cubetto Cambia Dimesione](dimensione.md)
* [**INDEX** Indice](start.md)
