# Expense Tracker

A simple command-line expense tracker built in Python. Add, view, filter, delete, sort, and summarize your expenses — all saved locally to a JSON file.

## Features

- Add expenses with amount, category, date, and an optional note
- View all expenses in a readable, formatted list
- Filter expenses by category (case-insensitive)
- Delete an expense by ID, with confirmation
- View a summary: total spent, total count, and per-category breakdown
- Sort expenses by amount, date, or category
- Data persists between runs via a local JSON file

## Requirements

- Python 3.x
- No external dependencies (uses only the standard library: `json`, `os`, `datetime`)

## Usage

```bash
python expense_tracker.py
```

You'll see a menu:

```
==============================
       Expense Tracker        
==============================
1. Add expense
2. View all expenses
3. View by category
4. Delete expense
5. Summary
6. Sort expenses
7. Exit
==============================
```

Enter a number to choose an action. Expenses are automatically saved to `expenses.json` in the same directory after any add or delete.

## Data Format

Each expense is stored as a JSON object:

```json
{
    "id": 1,
    "amount": 150.0,
    "category": "Food",
    "date": "2024-01-15",
    "note": "dinner with friends"
}
```

## Project Status

First project — built as a learning exercise. Core functionality works; 

## License

MIT
