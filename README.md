# Klementynka
Klementynka Engine to czatowy bot w Minecraft umożliwiający wykonywanie różnych akcji przez graczy.
Program pozwala na automatyzację większości zadań dzięki opcji tworzenia własnych komend.

![Klementynka screenshot](https://i.imgur.com/NlC0ab5.png)

Aplikacja jest przystosowana do czatu na serwerze GC2.PL.

## Wprowadzenie

Poniższe instrukcje pomogą Ci uruchomić Klementynkę na Twoim komputerze.

### Wymagania

* [Python 2.7](http://python.org)
* Launcher Minecraft'a zapisujący do pliku Game Output (na przykład [Shiginima](https://teamshiginima.com/update/3100.php))

### Uruchomienie

```
>python main.py
```
lub
```
dwukrotne kliknięcie na główny plik programu
```

### Tworzenie własnych komend

Wymagana jest minimalna znajomość języka programowania Python.

Wszystkie komendy znajdują się w folderze *cmd*. Każda komenda zawiera główny plik *\_\_main\_\_.py* spakowany do archiwum *nazwakomendy.zip*.

Istnieją dwie podstawowe zmienne, które można wykorzystać:

```
user_nick - nick użytkownika wywołującego komendę
target_nick - najczęściej pierwszy parametr komendy, czyli użytkownik na którym jest wywoływana komenda. Na przykład w przypadku !tuli Bigosek zmienna target_nick będzie równa Bigosek.
```

By wysłać wiadomość na czacie za pomocą bota, trzeba użyć funkcji *msg_send()*. Przykład:
```
msg_send('Bot: Jestem botem!')
```

**UWAGA**!
By móc wysyłać wiadomości na czacie, należy skupić się na oknie Minecraft'a. Odradzane jest przełączanie się miedzy oknami podczas działania Klementynki.

## Autorzy

* **workonfire** aka **Buty935** - *główny programista*
* **Bigosek** - *tester*
