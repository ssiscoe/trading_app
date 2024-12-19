-- Trends Table
CREATE TABLE trends (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    date DATE NOT NULL,
    trend_score REAL NOT NULL,
    predicted_price REAL,
    actual_price REAL
);

-- Predictions Table
CREATE TABLE predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    date DATE NOT NULL,
    model TEXT NOT NULL,
    prediction REAL NOT NULL,
    confidence REAL NOT NULL
);

-- Win Rates Table
CREATE TABLE win_rates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    model TEXT NOT NULL,
    win_rate REAL NOT NULL
);
