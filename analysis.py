import sqlite3
import pandas as pd

def run_queries():
    conn = sqlite3.connect('robot.db')
    cur = conn.cursor()

    print("\n--- Task 3.1: Max/Min X per Robot ---")
    q1 = """
    SELECT r.robot_name, MAX(s.x) AS max_x, MIN(s.x) AS min_x
    FROM SensorReading s
    JOIN Robot r ON s.robot_id = r.robot_id
    GROUP BY s.robot_id
    """
    print(pd.read_sql_query(q1, conn))



    print("\n--- Task 3.2: Max/Min Y per Robot ---")
    q2 = """
    SELECT r.robot_name, MAX(s.y) AS max_y, MIN(s.y) AS min_y
    FROM SensorReading s
    JOIN Robot r ON s.robot_id = r.robot_id
    GROUP BY s.robot_id
    """
    print(pd.read_sql_query(q2, conn))



    print("\n--- Task 4.1: Close Proximity Regions for 'Astro' and 'IamHuman' ---")
    q3 = """
    SELECT 
        MIN(s1.x) AS x_min,
        MAX(s1.x) AS x_max,
        MIN(s1.y) AS y_min,
        MAX(s1.y) AS y_max
    FROM SensorReading s1
    JOIN Robot r1 ON s1.robot_id = r1.robot_id
    JOIN SensorReading s2 ON s1.timestamp = s2.timestamp
    JOIN Robot r2 ON s2.robot_id = r2.robot_id
    WHERE r1.robot_name = 'Astro'
      AND r2.robot_name = 'IamHuman'
      AND ABS(s1.x - s2.x) < 1
      AND ABS(s1.y - s2.y) < 1
    """
    print(pd.read_sql_query(q3, conn))



    print("\n--- Task 4.2: Seconds 'Astro' and 'IamHuman' Are Close ---")
    q4 = """
    SELECT COUNT(*) AS seconds_close
    FROM SensorReading s1
    JOIN Robot r1 ON s1.robot_id = r1.robot_id
    JOIN SensorReading s2 ON s1.timestamp = s2.timestamp
    JOIN Robot r2 ON s2.robot_id = r2.robot_id
    WHERE r1.robot_name = 'Astro'
      AND r2.robot_name = 'IamHuman'
      AND ABS(s1.x - s2.x) < 1
      AND ABS(s1.y - s2.y) < 1
    """
    print(pd.read_sql_query(q4, conn))

    conn.close()

if __name__ == '__main__':
    run_queries()