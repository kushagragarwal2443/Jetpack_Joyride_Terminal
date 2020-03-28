# Python Terminal Jetpack Joyride

## Introduction

This is the terminal version of Jetpack Joyride written in Python. It uses the basic Python libraries and modules.

This game has been tested on **Linux** based Operating Systems.

## Structure and Features

The game application exhibits the OOP concepts of Inheritance, Encapsulation, Polymorphism, Abstraction along with Function Overloading.


## About the Game

### Controls

* w - Up
* a - Left
* s - Down
* d - Right
* Spacebar - Activating Shield
* m - Bullets
* f - Dragon powerup
* q - Quit the game

### Features and Powerups

1. Shield: The player can activate a shield around using the Spacebar key. The shield prevents the player from losing lives on collision with obstacles or bullets from Enemy. The shield can only be activated for 10 seconds in every 60 seconds.

2. Magnet: A randomly placed magnet appears in front of the player and tries to pull the player towards itself. On contact with the magnet lives are lost in accordance to the extent of the touch

3. Speedboost: A randomly placed speedboost appears in front of the player and on taking the powerup, the speed of the player increases for 10 seconds.

4. Bullets: The player has with him a magazine containing 100 bullets which can destroy obstacles and kill the boss enemy

5. Dragon powerup: The player can turn into a wavy dragon which can be activated with the press of the 'f' key. The powerup is lost only if the dragon collides with any obstacle. This powerup cannot be used in front of the boss enemy(ofcourse!.

6. Boss Enemy: The player reaches the end of the game only to be met with the bossenemy which is the hardest one to kill. The boss enemy chases you in the y axis direction and constantly fires dragonballs at the player from its three dragon ball muzzles "X". 
                To kill the boss enemy the player needs to aim his bullets to destroy his muzzle "X" and then only can he be killed. He has five lives and wont lose that easily.

### Notes
- Every Beam obstacle, be it vertical, horizontal or slanting is derived from the Beam class.
- The Beam slanting uses polymorphism to redefine one of the functions in the parent class.
- Gravitational simulation is used to model the movement of the player
- The obstacles, coins, magnets, speedboost are all defined in the class Scenery and have individual files for their random creation as well.
- The Game Screen has its own class which generates the game map and can blit object, players and enemies onto the screen.
    - The game has a pre-generated level map which is rendered during the run time and is updated according to `Mando's position in the game.

## Running the program

1. Install all the requirements:
    - `pip3 install -r requirements.txt`
2. Run the program:
    - `python3 game.py`

## Project Tree

* alarmexception.py
* background
    * beamsh.txt
    * beamss.txt
    * beamsv.txt
    * cloud.txt
    * coins.txt
    * dragons.txt
    * lost.txt
    * magnet.txt
    * plane.txt
    * quit.txt
    * shield.txt
    * speedboost.txt
    * welx.txt
    * won.txt
    * zappers.txt
* board.py
* bullets.py
* coins.py
* dragonball.py
* dragon.py
* game.py
* Game.py
* getch.py
* magnet.py
* mando.py
* __pycache__
    * alarmexception.cpython-36.pyc
    * board.cpython-36.pyc
    * bullets.cpython-36.pyc
    * coins.cpython-36.pyc
    * dragonball.cpython-36.pyc
    * dragon.cpython-36.pyc
    * getch.cpython-36.pyc
    * magnet.cpython-36.pyc
    * mando.cpython-36.pyc
    * scenery.cpython-36.pyc
    * speedboost.cpython-36.pyc
    * zappers.cpython-36.pyc
* README.txt
* requirements.txt
* scenery.py
* speedboost.py
* zappers.py