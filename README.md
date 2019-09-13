# enigma
Enigma encryption machine simulation
A simple simulation of the Enigma cryptographic machine, with three routers.

#### How to use:
Call 'run_enigma()' function in main.py or any where you want. by default this function called in main.py, if you want call somewhere else disable the function 
call in main.py.

#### The steps worked:
The machine by default creates the settings folder with three json files if it doesn't exist.

First you need to specify what settings you want to use, there are five options.
```
1. default_alphabet
2. default_alphabet_and_symbols
3. default_alphabet_symbols_and_numbers
4. create new router
5. enter name of the router
```
The first three options will use the default settings, which have:
```
1. default_alphabet
2. default_alphabet_and_symbols
3. default_alphabet_symbols_and_numbers
```
You can make your own settings using Option 4, you just specify the name and the letters and symbols you want to use. The system itself randomly uses the letters and symbols specified to make the routers, plug-board and reflect-board.

You can use the router that you built with option 5.
It will then prompt you to set up each router. On the actual machine you can rotate each router before it starts.
```
1- don't want to rotate them.
2- rotate router one.
3- rotate router two.
4- rotate router three.
```
If you don't want to do this or your spin is over, select option one.

Then you can enter the text you want.

:warning: Attention:

There are options for you, you can only use them when you are asked to "Enter your message:".

As: reset() or show()

