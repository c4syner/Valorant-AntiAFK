# Valorant-AntiAFK
A very simple, but smart, program to keep your character from going AFK in valorant.

## Inspiration
With the official release of Valorant, the community found that the punishment for being AFK was 1 hour. This number also increases with the number of offenses. Unfortunately for those who can't afford to allocate 30 minutes at a time to a game (including myself), there were no options. Thus the program was made.

## How it works
Every 10 seconds, the program polls your mouse to see if it has moved in the last 10 seconds. If it hasn't then the program clicks your left mouse button, thus shooting. However, if it notices that it has changed position, then the program will poll once again after another 10 seconds. This allows users to immediately leave their computer without having to press a keybind, or activate a program, in order to keep from going AFK. 


## Installation
For the non-programmers, a simple `.exe` is available in releases. 
However, if you would like to test the validity of my claims or modify it for your own purposes, the source code is available. Note that it is written in Python 3 and you will need to install `pynput` from pip. 

### Note
Although, this program is not vanguard detected, because of it not interfering with Valorant itself. There is still a risk in using a program like this however small that risk is in reality. Nonetheless, use at your own discretion. 
