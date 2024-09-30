# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:04:57 2024

@author: Bob
"""
import chess
import pygame
import sys
import os

pygame.init()
board = chess.Board()


width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Faith the chess engine")

# Define colors
BOARD_COLOR_1 = (240, 217, 181)
BOARD_COLOR_2 = (181, 136, 99)

def load_images():
    pieces = ['wp', 'wr', 'wn', 'wb', 'wq', 'wk', 'bp', 'br', 'bn', 'bb', 'bq', 'bk']
    images = {}
    for piece in pieces:
        images[piece] = pygame.transform.scale(pygame.image.load(os.path.join('images', f'{piece}.png')), (75, 75))
    return images

def draw_chessboard():
    square_size = width // 8
    for row in range(8):
        for col in range(8):
            color = BOARD_COLOR_1 if (row + col) % 2 == 0 else BOARD_COLOR_2
            pygame.draw.rect(screen, color, pygame.Rect(col * square_size, row * square_size, square_size, square_size))

def get_piece_at_square(board, square):
    piece = board.piece_at(square)
    if piece:
        return f"{piece.color and 'w' or 'b'}{piece.symbol()}".lower()
    return None


def draw_pieces(screen, board, images):
    square_size = width // 8
    for row in range(8):
        for col in range(8):
            square = chess.square(col, 7 - row)
            piece = get_piece_at_square(board, square)
            if piece:
                screen.blit(images[piece], pygame.Rect(col * square_size, row * square_size, square_size, square_size))
                
def game_loop():
    images = load_images()  # Load chess piece images
    square_size = width // 8
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Translate Pygame mouse click to a chess move
                x, y = pygame.mouse.get_pos()
                col = x // square_size
                row = 7 - (y // square_size)
                square = chess.square(col, row)

                if board.piece_at(square):
                    # Example: select the piece at the clicked square
                    print(f"Selected: {board.piece_at(square)} at {chess.square_name(square)}")

        # Draw board and pieces
        draw_chessboard()
        draw_pieces(screen, board, images)

        pygame.display.flip()
        
game_loop()
pygame.quit()
    