# Muoviamo Cubetto

Per muovere cubetto usiamo il touch, quando tocchiamo `on_touch_down(touch)` spostiamo il centro di cubetto nel punto
dove abbiamo toccato.

1. Prima capiamo dove scrivere le cose
2. Spostiamo cubetto con il *teletrasporto*
3. Facciamo arrivare cubetto a destinazione *dolcemente*

## Dove scrivere le cose

Noi vogliamo *catturare* il punto dove tocchiamo lo schermo. Sul nostro schermo abbiamo messo il componente `Animator`,
quindi chiediamo a lui quando viene toccato: in `main.py` nella classe `Animator` aggiungiamo

```python
class Animator(FloatLayout):
    def on_touch_down(self, touch):
        print(touch.pos)
```

Ora proviamo, ogni volta che tappiamo (o clickiamo) vengono stampate le coordinate del punto dove clickiamo che sono
contenute in `touch.pos`:

```
(181.0, 357.0)
(554.0, 386.0)
(539.0, 157.99999999999997)
(318.0, 139.99999999999997)
```

## Spostiamo cubetto

Prima di spostare cubetto bisogna fare in maniera che `Animator` conosca cubetto. Per far questo aggiungiamo una
proprietà a `Animator` di tipo oggetto e *attachiamoci* cubetto. Nel file `main.py` bisogna aggiungere in alto
`from kivy.properties import ObjectProperty` e nella classe `Animator` la nuova property:

```python
from kivy.properties import ObjectProperty

...

class Animator(FloatLayout):
    cubetto = ObjectProperty(None)
    
    ....
```

Ora dobbiamo associare questa property al componente `Cubetto` creato nel file `animator.kv`:

```
<Animator>:
    cubetto: cubetto_id

    Cubetto:
        id: cubetto_id
        ...
```

Nota: alla base di `Animator` abbiamo messo `cubetto` come quello della classe per poi associare quel valore a 
`id` del `Cubetto` creato dentro `<Animator>`.


Bene ora possiamo spostare `cubetto` dal componente `Animator` semplicemente cambiandogli le sue
coordinate o il suo centro: se dentro `on_touch_down()` mettiamo `self.cubetto.center = touch.pos` spostiamo cubetto
nel punto toccato ( `touch.pos` ):

```
class Animator(FloatLayout):
    cubetto = ObjectProperty(None)

    def on_touch_down(self, touch):
        self.cubetto.center = touch.pos
```

## Animazione morbida

Invece di usare il teletrasporto vogliamo che cubetto arrivi morbidamente nella nuova posizione. Per fare quasto
`kivy` mette a disposizione uno strumento bellissimo `Animation`. Per usarlo in alto mettete 
`from kivy.animation import Animation` e poi modificate `on_touch_down` così:

```python
    def on_touch_down(self, touch):
        animation = Animation(center=touch.pos)
        animation.start(self.cubetto)
```

State dicendo di costruire una animazione che sposta il centro in `touch.pos` che dura 1 secondo (se non si indica 
`duration` la durata è un secondo), che traforma *linearmente* (se non si indica `t`).

E' possibile cambiare più proprietà contemporaneamente (lo vediamo dopo), cambiare la durata e il tipo di 
trasformazione.

Provate a giocare usando le seguenti modifiche:

* `animation = Animation(center=touch.pos, duration=2)`
* `animation = Animation(center=touch.pos, duration=0.5)`
* `animation = Animation(center=touch.pos, duration=2, t='in_out_quad')`
* `animation = Animation(center=touch.pos, t='out_back')`
* `animation = Animation(center=touch.pos, t='out_bounce')`

tutti i valori possibili di `t` si trovano alla 
[pagina di ducumentazione di kivy](https://kivy.org/docs/api-kivy.animation.html).

Mettete come valore adesso:
```python
animation = Animation(center=touch.pos, t='in_out_quad')
```


* [**NEXT** Cubetto Cambia Dimesione](dimensione.md)
* [**PREV** Cubetto](cubetto.md)
* [**INDEX** Indice](start.md)
