import cv2
import numpy as np
import random
import time
import pygame


# SOUND SETUP
pygame.mixer.init()

swap_sound = pygame.mixer.Sound("swap.mp3")
win_sound = pygame.mixer.Sound("win.mp3")

swap_sound.set_volume(0.5)
win_sound.set_volume(1.0)


# STEP 1: CAPTURE IMAGE
def capture_face():
    cap = cv2.VideoCapture(0)

    print("Press 'c' to capture your face")

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            img = frame.copy()
            break

    cap.release()
    cv2.destroyAllWindows()
    return img


# SPLIT IMAGE
def split_image(img, grid_size):
    h, w, _ = img.shape
    pieces = []
    ph, pw = h // grid_size, w // grid_size

    for i in range(grid_size):
        for j in range(grid_size):
            piece = img[i*ph:(i+1)*ph, j*pw:(j+1)*pw]
            pieces.append(piece)

    return pieces


# DRAW PUZZLE
def draw_puzzle(pieces, grid_size, selected):
    ph, pw, _ = pieces[0].shape
    canvas = np.zeros((ph*grid_size, pw*grid_size, 3), dtype=np.uint8)

    idx = 0
    for i in range(grid_size):
        for j in range(grid_size):
            y1, y2 = i*ph, (i+1)*ph
            x1, x2 = j*pw, (j+1)*pw

            canvas[y1:y2, x1:x2] = pieces[idx]

            # highlight selected tile
            if idx == selected:
                cv2.rectangle(canvas, (x1, y1), (x2, y2), (0, 255, 0), 3)

            idx += 1

    return canvas


# GAME CLASS
class PuzzleGame:
    def __init__(self, img, grid_size):
        self.grid_size = grid_size
        self.original = split_image(img, grid_size)
        self.pieces = self.original.copy()

        random.shuffle(self.pieces)

        self.selected = None
        self.moves = 0

        self.ph, self.pw, _ = self.pieces[0].shape

    def get_index(self, x, y):
        col = x // self.pw
        row = y // self.ph
        return row * self.grid_size + col

    def swap(self, i, j):
        self.pieces[i], self.pieces[j] = self.pieces[j], self.pieces[i]
        self.moves += 1
        swap_sound.play()

    def is_solved(self):
        return all(np.array_equal(self.pieces[i], self.original[i]) for i in range(len(self.pieces)))

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:

            if x < 0 or y < 0:
                return

            idx = self.get_index(x, y)

            if idx >= len(self.pieces):
                return

            if self.selected is None:
                self.selected = idx

            elif self.selected == idx:
                self.selected = None

            else:
                self.swap(self.selected, idx)
                self.selected = None


# MAIN FUNCTION
def main():

    # Difficulty
    level = int(input("Enter difficulty (3 / 4 / 5): "))

    img = capture_face()
    img = cv2.resize(img, (300, 300))

    game = PuzzleGame(img, level)

    start_time = time.time()

    cv2.namedWindow("Puzzle")
    cv2.setMouseCallback("Puzzle", game.mouse_callback)

    while True:
        canvas = draw_puzzle(game.pieces, game.grid_size, game.selected)

        elapsed = int(time.time() - start_time)
        score = max(1000 - (elapsed*5 + game.moves*10), 0)

        # UI TEXT
        cv2.putText(canvas, f"Time: {elapsed}s", (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

        cv2.putText(canvas, f"Moves: {game.moves}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

        cv2.putText(canvas, f"Score: {score}", (10, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

        cv2.imshow("Puzzle", canvas)

        # WIN CONDITION
        if game.is_solved():
            win_sound.play()

            cv2.putText(canvas, "SOLVED!", (80, 150),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 3)

            cv2.imshow("Puzzle", canvas)
            print("🎉 Puzzle Solved!")
            print("Final Score:", score)

            cv2.waitKey(3000)
            break

        if cv2.waitKey(20) == 27:
            break

    cv2.destroyAllWindows()


# RUN
if __name__ == "__main__":
    main()