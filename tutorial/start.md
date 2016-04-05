# Animator

Si tratta di disegnare un semplice e simpatico personaggio *Cubetto* e muoverlo per lo schermo del telefonino con dei 
semplici tap. Ogni volta che tocchiamo lo schermo cubetto raggiungerà il punto toccato girando e cambiando dimensione.

## Rissumiamo

1. Cubetto è un semplice disegno geometrico
2. Quando tocchiamo lo schermo cubetto raggiunge il punto toccato
3. Cobetto si muove rotolando
4. Se tocchiamo la zona sinistra dello schermo cubetto diventa più grande, se tocchiamo la zona destra diventa più
piccolo.

## Prima di iniziare

Usate [Compilare e Installare](https://github.com/la10736/acchiappa/tree/master/appendici/compila_e_installa.md) per 
provare il gioco vuoto e come metterlo sul vostro telefonino. Facciamo questo prima di iniziare.

Il programma vuoto contiene il file `main.py` così:

```python
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class Animator(FloatLayout):
    pass


class AnimatorApp(App):
    def build(self):
        return Animator()


if __name__ == "__main__":
    AnimatorApp().run()
```

e il file `animator.kv`

```kv
#:kivy 1.0.9

<Animator>:

```


## Percorso

1. [Cubetto](cubetto.md)
2. [Muoviamo Cubetto](muovi.md)
3. [Cubetto Cambia Dimesione](dimensione.md)
4. [Cubetto Rotola](rotola.md)
4. [Contest](contest.md)

