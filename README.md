# Live Puzzle

## Features
- Interactive gameplay
- Beautiful graphics
- Multiple levels

## Instructions
1. Clone the repository
2. Install the required libraries using `pip install -r requirements.txt`
3. Run the game with the command `python main.py`

## Code Example
Here is the Python code to start the game:

```python
# main.py

import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

if __name__ == '__main__':
    game = Game()
    game.run()
```
