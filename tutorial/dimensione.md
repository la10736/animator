# Cubetto Cambia Dimesione

Per cambiare la dimensione di cubetto basta cambiare la sua `width` che all'inizio abbiamo fissato a `dp(50)`.

1. Prima proviamo a aumentare la dimesione quando facciamo il tap
2. La modifica la facciamo diventare *morbida*
3. Quando tappiamo a destra la dimensione diminuisce e quando tappiamo a sinistra aumenta

## Aumentiamo la dimensione

Aumentiamo la dimensione di `1.3`. Quindi quando facciamo `on_touch_down()` prima della nostra animazione cambiamo
`self.cubetto.width` moltiplicandolo per `1.3`. All'inizio di `on_touch_down()` mettiamo:

```python
    def on_touch_down(self, touch):
        larghezza = self.cubetto.width * 1.3
        self.cubetto.width = larghezza
```

e proviamo...

**Bene** ... ora ripuliamo facendo diventare `1.3` un numero facile da modificare e usando una funzione fare il calcolo.

La classe `Animator` diventa:

```python
class Animator(FloatLayout):
    cubetto = ObjectProperty(None)
    INCREMENTO_LARGHEZZA = 1.3
    
    def on_touch_down(self, touch):
        larghezza = self.ingrandisci()
        self.cubetto.width = larghezza
        animation = Animation(center=touch.pos, t='in_out_quad')
        animation.start(self.cubetto)
    
    def ingrandisci(self):
        return self.cubetto.width * self.INCREMENTO_LARGHEZZA
```

## Cambiamo la dimensione morbidamente

Per cambiare la dimensione *morbidamente* basta cambiare l'animazione `Animator` dicendogli di modificare anche `width`
oltre a `center`: `Animation(center=touch.pos, width=larghezza t='in_out_quad')`. Togliamo anche la modifica istantanea
che ora non serve più.

```python
    def on_touch_down(self, touch):
        larghezza = self.ingrandisci()
        animation = Animation(center=touch.pos, width=larghezza, t='in_out_quad')
        animation.start(self.cubetto)
```

Ora è bello *morbido*.

## Ingrandiamo e Rimpiccioliamo

Prima di far la scelta se ingrandire o rimpicciolire proviamo a cambiare il programma per rimpicciolire. Facciamo una 
nuova funzione `rimpicciolisci()` che divide la dimesione invece di ingrandire e cambiamo `larghezza` usandola:

```python
    def rimpicciolisci(self):
        return self.cubetto.width / self.INCREMENTO_LARGHEZZA
```

e dentro `on_touch_down()` mettiamo: `larghezza = self.rimpicciolisci()`.

Adesso quando la posizione `x` del tocco `touch` è maggiore di metà della larghezza di `Animator` ingrandiamo, 
altrimenti rimpiccioliamo.... chiaro no. Questa frase si traduce in:

```python
        x, y = touch.pos
        if x > self.width/2:
            larghezza = self.rimpicciolisci()
        else:
            larghezza = self.ingrandisci()
```

quindi `on_touch_down()` diventa

```python
    def on_touch_down(self, touch):
        x, y = touch.pos
        if x > self.width/2:
            larghezza = self.rimpicciolisci()
        else:
            larghezza = self.ingrandisci()
        animation = Animation(center=touch.pos, width=larghezza, t='in_out_quad')
        animation.start(self.cubetto)
```

Tutto morbido e si muove come vogliamo.


* [**NEXT** Cubetto Rotola](rotola.md)
* [**PREV** Muoviamo Cubetto](muovi.md)
* [**INDEX** Indice](start.md)
