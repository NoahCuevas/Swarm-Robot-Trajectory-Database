# Robot Trajectory Analysis

This project is part of a database design course and focuses on analyzing swarm robot movement using data stored in an SQLite database.

## Project Files

- `robot.db`: SQLite database containing robot names, sensor readings (X, Y positions with timestamps), and target intervals.
- `analysis.py`: Python script that runs all SQL queries for Tasks 3.1 to 4.2.
- `README.md`: This file.

## What It Does

The analysis focuses on:
- Finding the **maximum and minimum X/Y coordinates** recorded for each robot.
- Identifying time periods when **'Astro' and 'IamHuman'** robots are within 1 unit of each other.
- Calculating the total **number of seconds** they are in close proximity.

## Task 1. Relational Schema (SQL Format)

```sql
CREATE TABLE Robot (
    robot_id INTEGER PRIMARY KEY,
    robot_name TEXT
);

CREATE TABLE SensorReading (
    reading_id INTEGER PRIMARY KEY AUTOINCREMENT,
    robot_id INTEGER,
    timestamp INTEGER,
    x REAL,
    y REAL,
    FOREIGN KEY (robot_id) REFERENCES Robot(robot_id)
);

CREATE TABLE TargetInterval (
    interval_id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_time INTEGER,
    end_time INTEGER,
    event_type TEXT
);
```

## How to Run

Make sure you have Python 3 and `pandas` installed.

```bash
python analysis.py