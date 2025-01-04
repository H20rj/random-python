##made with claude


import pygame
import random
import sys
from typing import Tuple, Set

# Initialize Pygame
pygame.init()

# Game Constants
CELL_SIZE = 30
GRID_SIZE = 18  # Changed to 18x18
MINES = 40
WINDOW_SIZE = GRID_SIZE * CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
LIGHT_GRAY = (192, 192, 192)
DARK_GRAY = (64, 64, 64)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
SUCCESS = (40, 167, 69)  # Added for win message

# Number Colors
NUMBER_COLORS = {
    1: BLUE,
    2: GREEN,
    3: RED,
    4: PURPLE,
    5: MAGENTA,
    6: CYAN,
    7: BLACK,
    8: GRAY
}


class Minesweeper:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Minesweeper")

        self.font = pygame.font.Font(None, 36)
        self.reset_game()

    def reset_game(self):
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.flags = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.game_over = False
        self.game_won = False
        self.first_click = True
        self.mines_positions: Set[Tuple[int, int]] = set()

    def place_mines(self, first_x: int, first_y: int):
        possible_positions = [(x, y) for x in range(GRID_SIZE) for y in range(GRID_SIZE)
                              if abs(x - first_x) > 1 or abs(y - first_y) > 1]

        self.mines_positions = set(random.sample(possible_positions, MINES))

        # Place mines and calculate numbers
        for x, y in self.mines_positions:
            self.grid[y][x] = -1

            # Update surrounding cells
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    new_x, new_y = x + dx, y + dy
                    if (0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE and
                            self.grid[new_y][new_x] != -1):
                        self.grid[new_y][new_x] += 1

    def reveal_cell(self, x: int, y: int):
        if not (0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE):
            return

        if self.revealed[y][x] or self.flags[y][x]:
            return

        self.revealed[y][x] = True

        if self.grid[y][x] == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    self.reveal_cell(x + dx, y + dy)

    def check_win(self):
        if self.game_over:
            return False

        # Check if all non-mine cells are revealed
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if (x, y) not in self.mines_positions and not self.revealed[y][x]:
                    return False
        return True

    def draw_cell(self, x: int, y: int):
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

        if self.revealed[y][x]:
            pygame.draw.rect(self.screen, WHITE, rect)
            if self.grid[y][x] > 0:
                text = self.font.render(str(self.grid[y][x]), True, NUMBER_COLORS[self.grid[y][x]])
                text_rect = text.get_rect(center=rect.center)
                self.screen.blit(text, text_rect)
            elif self.grid[y][x] == -1:
                pygame.draw.rect(self.screen, RED, rect)
                pygame.draw.circle(self.screen, BLACK, rect.center, CELL_SIZE // 3)
        else:
            pygame.draw.rect(self.screen, LIGHT_GRAY, rect)
            if self.flags[y][x]:
                pygame.draw.polygon(self.screen, RED,
                                    [(x * CELL_SIZE + 10, y * CELL_SIZE + 5),
                                     (x * CELL_SIZE + 20, y * CELL_SIZE + 15),
                                     (x * CELL_SIZE + 10, y * CELL_SIZE + 25)])

        pygame.draw.rect(self.screen, GRAY, rect, 1)

    def draw_game_state(self):
        if self.game_won:
            text = self.font.render("YOU WIN! Press R to restart", True, SUCCESS)
            text_rect = text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2))
            # Add a semi-transparent overlay
            overlay = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE))
            overlay.fill(WHITE)
            overlay.set_alpha(128)
            self.screen.blit(overlay, (0, 0))
            self.screen.blit(text, text_rect)
        elif self.game_over:
            text = self.font.render("Game Over! Press R to restart", True, RED)
            text_rect = text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2))
            self.screen.blit(text, text_rect)

    def draw(self):
        self.screen.fill(WHITE)
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                self.draw_cell(x, y)
        self.draw_game_state()
        pygame.display.flip()

    def handle_click(self, pos: Tuple[int, int], right_click: bool):
        if self.game_won or self.game_over:
            return

        x, y = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE

        if not (0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE):
            return

        if right_click:
            if not self.revealed[y][x]:
                self.flags[y][x] = not self.flags[y][x]
            return

        if self.flags[y][x]:
            return

        if self.first_click:
            self.place_mines(x, y)
            self.first_click = False

        if (x, y) in self.mines_positions:
            self.game_over = True
            # Reveal all mines
            for mine_x, mine_y in self.mines_positions:
                self.revealed[mine_y][mine_x] = True
        else:
            self.reveal_cell(x, y)
            # Check for win after each valid move
            if self.check_win():
                self.game_won = True

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos, event.button == 3)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_game()

            self.draw()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Minesweeper()
    game.run()