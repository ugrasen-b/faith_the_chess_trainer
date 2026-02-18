# Faith: Your Chess Coach

This repository is an early-stage chess project with two main building blocks:

1. **Game ingestion** from Chess.com into a local SQLite database.
2. **A basic Pygame chessboard UI** powered by `python-chess`.

There is **no full chess engine implementation yet** (search/evaluation/move selection), but the scaffolding is in place for future work.

## Current project structure

- `faith_ui.py`
  - Opens a Pygame window and draws an 8x8 board.
  - Loads chess piece images from `images/`.
  - Uses `python-chess` for board state.
  - Currently supports clicking pieces and printing the selected square in the terminal.

- `fetch_games.py`
  - Calls the Chess.com public API for a given username/year/month.
  - Parses game results.
  - Stores game metadata + PGN into `database/games.db`.

- `database/games.db`
  - Local SQLite database.
  - Contains a `games` table (`id`, `white`, `black`, `result`, `pgn`).

- `images/`
  - Piece sprites (`wp.png`, `bk.png`, etc.) for rendering the board UI.

- `chess-dev.yml`
  - Conda environment definition with Python 3.12 and dependencies (`pygame`, `requests`, `python-chess`, etc.).

## What you can do right now

### 1) Run the UI board
```bash
python faith_ui.py
```
You’ll get a chessboard window with pieces in starting position. Clicking a piece logs selection info.

### 2) Pull games from Chess.com
Edit the user/month/year values in `fetch_games.py`, then run:
```bash
python fetch_games.py
```
This writes data into `database/games.db`.

### 3) Inspect stored games quickly
```bash
python - <<'PY'
import sqlite3
conn = sqlite3.connect('database/games.db')
cur = conn.cursor()
cur.execute('SELECT COUNT(*) FROM games')
print('games:', cur.fetchone()[0])
conn.close()
PY
```

## Suggested next steps

- Add a move input flow in `faith_ui.py` (select source + destination, validate legal moves, update board).
- Split scripts into reusable modules (e.g., `ui/`, `data/`, `engine/`).
- Add tests for game ingestion and result parsing.
- Add engine foundation:
  - position evaluation,
  - move generation interface,
  - minimax/alpha-beta search loop.
- Add CLI commands so behavior isn’t hardcoded in script globals.
