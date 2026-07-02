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


<img width="642" height="502" alt="Screenshot 2026-03-29 231825" src="https://github.com/user-attachments/assets/8b03bf6b-074b-48f2-a8eb-f47fe200c55b" />

<img width="304" height="330" alt="Screenshot 2026-03-29 231703" src="https://github.com/user-attachments/assets/0a2ffc66-bffd-4763-87ea-12883523f605" />

<img width="293" height="325" alt="Screenshot 2026-03-29 231930" src="https://github.com/user-attachments/assets/3d8ae3fd-6618-43d5-84d2-eb8f2879688b" />


