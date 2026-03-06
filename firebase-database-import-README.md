# Firebase Realtime Database – Import

## How to import

1. Open [Firebase Console](https://console.firebase.google.com/) → your project → **Realtime Database**.
2. Click the **⋮** (three dots) next to the root node → **Import JSON**.
3. Choose `firebase-database-import.json`.

You can delete the `_example_delete_me` game and user in the console after import if you want a clean DB.

---

## Grid state (stored as JSON string under `games/<code>/grid`)

The grid is a 2D array: **grid[row][col]** with rows/cols indexed 0..2n (for gridSize n). Layout:

```
[Dot,    Edge,   Dot,    Edge,   Dot   ]
[Edge,   Square, Edge,   Square, Edge  ]
[Dot,    Edge,   Dot,    Edge,   Dot   ]
[Edge,   Square, Edge,   Square, Edge  ]
[Dot,    Edge,   Dot,    Edge,   Dot   ]
```

- **Dot**: `{ x: int, y: int }` — no claimer/winner.
- **Edge**: `{ x: int, y: int, claimer: int }` — `claimer`: 0 = unclaimed, 1–4 = player index.
- **Square**: `{ x: int, y: int, letter: str, winner: int, point_value: int }` — `winner`: 0 = no one, 1–4 = player index.

Players are **1-indexed** (1, 2, 3, 4). Unclaimed / no winner is **0**.

Example 3×3 (one square, one letter):

```js
[
  [ { x: 0, y: 0 }, { x: 1, y: 0, claimer: 0 }, { x: 2, y: 0 } ],
  [ { x: 0, y: 1, claimer: 0 }, { x: 1, y: 1, letter: "A", winner: 0, point_value: 1 }, { x: 2, y: 1, claimer: 0 } ],
  [ { x: 0, y: 2 }, { x: 1, y: 2, claimer: 0 }, { x: 2, y: 2 } ]
]
```

The backend and frontend expect **snake_case** in the stored JSON: `point_value`, not `pointValue`.

---

## Root structure

- **`/games`** — Key = lobby code. Each game: `singleplayer`, `phase` (0=lobby, 1=dots&boxes, 2=anagrams, 3=results), `grid` (stringified array above), `current_player` (1–4), `players` → `"1"`..`"4"` with `display_name`, `letters_captured` (`""` or object of `{ letter, point_value }`), `final_score` (-1 until set). Anagrams phase adds `total_score`, `done`, `played_words`, `possible_words` on players.
- **`/users`** — Key = username. Each user: `name`, `preferred_palette`, `high_score`.
