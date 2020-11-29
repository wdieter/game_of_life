# game_of_life

## Run a "game of life" simulation in the terminal with custom parameters. 

### Background
Ever since I learned about conway's game of life https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life , I've been totally facinated by it and other self-generating simulations or "automotons".
This repository holds my implementation, and was also a chance to play with some OOP principals and operator overloading in python. 

### Quick start 

After downloading the source code and navigating to the directory, run the following commands to: 
- build a virtualenv

```
$ virtualenv venv
$ . venv/bin/activate
```

- install the code as an executable

```
$ pip install --editable .
```

- and run the code

```
$ game_of_life --width 10 --height 10 --cells 20

```
