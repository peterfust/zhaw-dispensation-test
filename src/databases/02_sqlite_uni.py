import sqlite3

conn = sqlite3.connect("uni.db")
cur = conn.cursor()

res = cur.execute("""
    SELECT Name, Raum 
    FROM Professoren
    WHERE Rang = "C3"
    ORDER BY PersNr DESC
""")
print(res.fetchall())

res = cur.execute("""
    SELECT * 
    FROM Vorlesungen
    WHERE SWS BETWEEN 2 AND 3
""")
print(res.fetchall())

# JOIN über 3 Tabellen via Referenztabelle
res = cur.execute("""
    SELECT s.Name
    FROM Studenten s
    JOIN Hoeren h
    ON s.MatrNr = h.MatrNr
    JOIN Vorlesungen v 
    ON v.VorlNr = h.VorlNr
    WHERE v.Titel = "Grundzuege"
""")
print(res.fetchall())

res = cur.execute("""
    SELECT SWS, count(*)
    FROM Vorlesungen
    GROUP BY SWS
""")
print(res.fetchall())

res = cur.execute("""
    SELECT Name
    FROM Professoren 
    WHERE PersNr NOT IN (SELECT PersNr FROM Lesen)
    
""")
print(res.fetchall())

res = cur.execute("""
    SELECT DISTINCT s.Name
    FROM Studenten s
    JOIN Hoeren h
    ON s.MatrNr = h.MatrNr
    JOIN Vorlesungen v 
    ON v.VorlNr = h.VorlNr
    JOIN Lesen l 
    ON v.VorlNr = l.VorlNr
    JOIN Professoren p 
    ON l.PersNr = p.PersNr
    WHERE p.Name = "Sokrates"
""")
print(res.fetchall())

res = cur.execute("""
    SELECT p.Name
    FROM Professoren p
    JOIN ArbeitenFuer a
    ON p.PersNr = a.PersNrP
    GROUP BY p.PersNr
    HAVING COUNT(*) = (SELECT MAX(t.Anzahl)
                        FROM (SELECT COUNT(PersNrP) AS Anzahl
                                FROM ArbeitenFuer
                                GROUP BY PersNrP
                             ) AS t)
""")
print(res.fetchall())

res = cur.execute("""
    SELECT DISTINCT v.Titel
    FROM Studenten s
    JOIN Hoeren h
    ON s.MatrNr = h.MatrNr
    JOIN Vorlesungen v 
    ON v.VorlNr = h.VorlNr
    WHERE s.Semester BETWEEN 1 AND 4
""")
print(res.fetchall())

res = cur.execute("""
    SELECT DISTINCT s1.Name
    FROM Studenten s1
    JOIN Hoeren h1
    ON s1.MatrNr = h1.MatrNr
    JOIN Vorlesungen v1
    ON v1.VorlNr = h1.VorlNr
    WHERE s1.Name <> "Theophrastos" AND v1.VorlNr IN (SELECT v2.VorlNr
                        FROM Vorlesungen v2 
                        JOIN Hoeren h2 
                        ON v2.VorlNr = h2.VorlNr 
                        JOIN Studenten s2 
                        ON h2.MatrNr = s2.MatrNr
                        WHERE s2.Name = "Theophrastos")
""")
print(res.fetchall())

# WHERE Spalte X in Tabelle B mehr als 3 Einträge hat
res = cur.execute("""
    SELECT s.Name, s.MatrNr
    FROM Studenten s
    JOIN Hoeren h
    ON s.MatrNr = h.MatrNr
    JOIN Vorlesungen v 
    ON v.VorlNr = h.VorlNr
    GROUP BY s.MatrNr
    HAVING COUNT(*) >= 3
""")
print(res.fetchall())

# LEFT OUTER JOIN
res = cur.execute("""
    SELECT p.Name, pr.VorlNr
    FROM Professoren p
    LEFT OUTER JOIN Pruefen pr
    ON p.PersNr = pr.PersNr
""")
print(res.fetchall())