import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("queries.db")  # Update path if necessary
cursor = connection.cursor()

# Example query to fetch all data
cursor.execute("""
WITH QCount AS (
    SELECT query_name, COUNT(*) as total FROM Queries GROUP BY query_name
)
SELECT
    q.query_name,
    ROUND(AVG(q.rating * 1.0 / q.position), 2) AS quality,
    ROUND(COALESCE(SUM(CASE WHEN q.rating < 3 THEN 1 ELSE 0 END) * 100.00 / qc.total, 0), 2) as poor_query_percentage
FROM Queries q
LEFT JOIN QCount qc ON qc.query_name=q.query_name
WHERE q.query_name IS NOT NULL
GROUP BY q.query_name, qc.total
""")
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(row)

# Close the connection
connection.close()