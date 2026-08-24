# Pygame Spaceship

This is an experimental application for reviweing and remember the basics
of Pygame. The objective is to move a spaceship in two dimensions while 
avoiding collisions with the walls of the window.

## Intro 

### Introduction for the initial version

The ship can be controlled using six actions:

- The four arrow keys change the ship's direction without inertia.
- The Space key accelerates the ship up to a defined speed limit.
- The `B` key applies the brake and reduces the ship's speed.

Negative velocity and backward movement are not implemented in this first
version.

### State-of-the-Art

We encourage you to explore the previous playable versions to see how the
project has evolved.

Let's see what I can build.

## Installation

Create and activate a virtual environment:

```console
python -m venv .venv
```

On WIndows:
```
> .\.venv\Scripts\activate
```

On Mac or Linux:
```
source .venv/bin/activate
```

install the dependencies:

```
> python -m pip install pygame
> python -m pip freeze > requirements.txt
```

if you already have a requirements.txt, use this to install de dependencies:

```
> python -m pip install -r requirements.txt
```

## Run the App

```> python run.py```


## First appearance

The first appearance of the ship also represents my first practical
experience with Pygame in a long time.

![Spaceship first appearance](./images/spaceship_v0.jpg)

## TODOS

Collaboration is welcome. Pull requests are encouraged.

Use the following branch workflow:

* Create and test changes in the dev branch.
* Merge changes into the main branch when they are ready.

Feel free to implement the following topics in the way you consider most
appropriate.

### Game Experience

    [ ] Create a start screen with instructions and a start button.
    [ ] Remove the instructions from the game screen.

### Dynamic Functions

    [ ] Allow the ship to leave one side of the window and appear on the opposite side.
    [ ] Detect collisions with the window limit and trigger a game-over state.
    [ ] Let the player choose between wrap-around and collision mode before the game starts.

    [ ] Implement holding the Space key for continuous acceleration.
    [ ] Implement holding the B key for continuous braking.

    [ ] Change the behavior of the left and right arrows to rotate the ship by a defined number of degrees, allowing curved movement.

    [ ] Implement inertia:
        [ ] Use the Up arrow to accelerate.
        [ ] Use the Down arrow to brake or reduce velocity.
        [ ] Preserve the Space and B keys for their current functions.

    [ ] Improve the inertia system by allowing backward movement up to a defined speed limit.

### Design

    [ ] Replace the triangle with a spaceship icon. See: https://www.flaticon.com/free-icons/spaceship
    [ ] Create a starry background using Pygame.
    [ ] Add the Sun and Moon to the background.
    [ ] Make the celestial bodies move slowly.
    [ ] Add comets and stars that move faster across the background.

### Interaction

    [ ] Add shooting functionality:
        [ ] Replace the current Space key function with normal firing.
        [ ] Use the B key to throw bombs.

    [ ] Add a timer for bombs and display an animation after a few seconds.

    [ ] Add asteroids that can hit the ship and be hit by shots or bombs:
        [ ] Add hit points for the ship.
        [ ] Add hit points for the asteroids.

    [ ] Add an explosion animation when the ship is destroyed.


## About the Author

Cicero Lima is a M.Sc. in Mechanical Engineering, PCAP-certified Python developer,
and father of three children. He has eight years of professional
experience as a software developer in Germany and is currently attending
a German FIAE training program with the goal of becoming an IHK-certified
IT professional.

His interest in programming and games goes back to the 1980s, when
space-invasion games, pinball machines, and arcade cabinets sparked his
curiosity about computers and interactive entertainment. Those early
experiences made games a natural and enjoyable way to explore programming.
Making also his mother sometimes crazy.

This project is motivated by a desire to revisit the fundamentals of
Pygame and strengthen his understanding of game loops, events, movement,
collisions, and rendering. It is an experimental project created for
learning and practice.

Cicero is passionate about challenging projects, especially in IT
security and algorithmic trading. He enjoys learning by building
practical applications and exploring how software works from the ground
up.
