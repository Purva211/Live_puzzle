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
<img width="349" height="351" alt="Screenshot 2026-03-29 231930" src="https://github.com/user-attachments/assets/013d1b5a-873f-404f-a245-c014ad04ad8f" />
<img width="849" height="780" alt="Screenshot 2026-03-29 231703" src="https://github.com/user-attachments/assets/b82cd8c8-dfc0-40d6-936d-2c5784eea699" />
<img width="742" height="552" alt="Screenshot 2026-03-29 231825" src="https://github.com/user-attachments/assets/2eb63c59-59ac-475a-b4cb-1cb8637aa2de" />
