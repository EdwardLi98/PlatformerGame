import pygame
import os
from player import Player
from system import System


def main():
    # Initialise window
    system = System(1000, 500, 0, -50)
    system.initialiseGame()
    system.runGame()


if __name__ == "__main__":
    main()
