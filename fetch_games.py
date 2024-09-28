# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 11:25:44 2024

@author: Bob
"""

"""
This is the Python file to get the games from chess.com or Lichess 
"""

import requests
import json
import sqlite3

#%%
def get_chesscome_games(username, year, month):
    url = f"https://api.chess.com/pub/player/{username}/games/{year}/{month:02d}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    print(url)
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        games = data.get('games', [])
        return games
    else:
        print(f"Error fetching data: {response.status_code}")
        

#%%
# Testing it for a sample year and month
username = "OrwellFan"
year = 2024
month = 5

games = get_chesscome_games(username, year, month)

if games:
    print(f"found {len(games)} game in {year}-{month:02d}")
    
#%%
# Saving the data to a database
conn = sqlite3.connect("database/games.db")

c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS games (
              id TEXT PRIMARY KEY,
              white TEXT,
              black TEXT,
              result TEXT,
              pgn TEXT)
          ''')
          
for game in games:
    white_result = game['white'].get('result')
    black_result = game['black'].get('result')
    if white_result == 'win':
        result = '1-0'  # White wins by checkmate
    elif black_result == 'win':
        result = '0-1'  # Black wins by checkmate
    elif white_result == 'draw':
        result = '1/2-1/2'  # Draw
    else:
        result = 'Unknown'
    c.execute('''
              INSERT OR IGNORE INTO games (id, white, black, result, pgn)
              VALUES (?, ?, ?, ?, ?)
              ''',
              (game['url'],game['white']['username'],game['black']['username'], result, game['pgn']))
    
conn.commit()
conn.close()