Snake Game
A console-based version of the beloved [game of Snake](https://www.google.com/search?q=play+snake) using Python 3 and domain driven design.

## Play the game

The user can move the snake using the following commands:
    - `move [n]`. This moves the snake `n` squares, in the direction it is currently facing. `move` with no parameters moves the snake by `1` square.
    - `up | right | down | left` changes the snake's direction accordingly.
    - When the snake eats an apple, its tail grows by `1 square` and a new apple is added to the game area.
    
Game stops when snake eats itself or hits the wall. A GAME OVER! is printed on the command line.

## Running the application
Download the source code from the repository and run the file just as any other Python script (.py) file.

python3 Snake\ Game.py
