import sqlite3

conn = sqlite3.connect("namenusa.db")
cur = conn.cursor()

res = cur.execute("""
    SELECT Name, Year
    FROM namenusaprostaat
    GROUP BY Name, Year
    HAVING SUM(Births) > 90000
    
""")
print(res.fetchall())

res = cur.execute("""
    SELECT MIN(Year)
    FROM namenusaprostaat
    WHERE Sex = 'M' AND Name = 'Keanu'
""")
print(res.fetchall())

res = cur.execute("""
    SELECT COUNT(DISTINCT Name) AS 'Anzahl_verschiedene_Namen_im_Jahr_2000'
    FROM namenusaprostaat
    WHERE Year = '2000'
""")
print(res.fetchall())

res = cur.execute("""
    SELECT SUM(Births) AS 'Anzahl'
    FROM namenusaprostaat
    WHERE Year = '1966' AND Sex = 'F'
""")
print(res.fetchall())

res = cur.execute("""
    SELECT Year, SUM(Births) AS 'AnzahlGeburten'
    FROM namenusaprostaat
    GROUP BY Year
    HAVING Year BETWEEN 1960 AND 1970
""")
print(res.fetchall())

res = cur.execute("""
    SELECT Name
    FROM namenusaprostaat
    WHERE Year >= 2000 AND Sex = 'F'
    GROUP BY Name
    ORDER BY SUM(Births) DESC LIMIT 10
""")
print(res.fetchall())

res = cur.execute("""
    SELECT COUNT(DISTINCT Name) AS 'Anzahl', Sex
    FROM namenusaprostaat
    GROUP BY Sex
""")
print(res.fetchall())

''' Command is correct but takes too long
res = cur.execute("""
    SELECT DISTINCT n1.Name
    FROM namenusaprostaat n1
    JOIN namenusaprostaat n2
    ON n1.Name = n2.Name
    WHERE n1.Sex = 'F' AND n2.Sex = 'M'
    ORDER BY n1.Name LIMIT 10
""")
print(res.fetchall())
'''

res = cur.execute("""
    SELECT DISTINCT Name
    FROM namenusaprostaat
    WHERE Sex = 'M' AND Name IN (
        SELECT Name
        FROM namenusaprostaat
        WHERE Sex = 'F')
    ORDER BY Name LIMIT 10       
""")
print(res.fetchall())

res = cur.execute("""
    SELECT SUBSTRING(Name,1,1), COUNT(Name)
    FROM namenusaprostaat
    WHERE Sex = 'F' AND (Name LIKE 'A%' OR Name LIKE 'B%' OR Name LIKE 'C%' OR Name LIKE 'X%' OR Name LIKE 'Y%' OR Name LIKE 'Z%')
    GROUP BY SUBSTRING(Name,1,1)
""")
print(res.fetchall())