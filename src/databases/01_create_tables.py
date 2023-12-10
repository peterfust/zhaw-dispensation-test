import sqlite3

conn = sqlite3.connect("uni.db")
cur = conn.cursor()

# Creates all table for university examples...
cur.execute("DROP TABLE IF EXISTS Studenten")
conn.commit()
cur.execute("""
    CREATE TABLE Studenten(
        MatrNr INTEGER PRIMARY KEY,
        Name VARCHAR(256) NOT NULL,
        Semester INTEGER NOT NULL,
        GebDatum DATE NOT NULL
    )
""")

cur.execute("DROP TABLE IF EXISTS Professoren")
conn.commit()
cur.execute("""
    CREATE TABLE Professoren(
        PersNr INTEGER PRIMARY KEY,
        Name VARCHAR(256) NOT NULL,
        Rang CHAR(02) NOT NULL,
        Raum INTEGER NOT NULL,
        GebDatum DATE NOT NULL
    )
""")

cur.execute("DROP TABLE IF EXISTS Vorlesungen")
conn.commit()
cur.execute("""
    CREATE TABLE Vorlesungen(
        VorlNr INTEGER PRIMARY KEY,
        Titel VARCHAR(256) NOT NULL,
        SWS INTEGER NOT NULL
    )
""")

cur.execute("DROP TABLE IF EXISTS Assistenten")
conn.commit()
cur.execute("""
    CREATE TABLE Assistenten(
        PersNr INTEGER PRIMARY KEY,
        Name VARCHAR(256) NOT NULL,
        Fachgebiet VARCHAR(256) NOT NULL
    )
""")

cur.execute("DROP TABLE IF EXISTS Hoeren")
conn.commit()
cur.execute("""
    CREATE TABLE Hoeren(
        MatrNr INTEGER NOT NULL,
        VorlNr INTEGER NOT NULL,
        PRIMARY KEY (MatrNr, VorlNr),
        CONSTRAINT FK_MatrNr FOREIGN KEY (MatrNr) REFERENCES Studenten (MatrNr) ON DELETE CASCADE,
        CONSTRAINT FK_VorlNr FOREIGN KEY (VorlNr) REFERENCES Vorlesungen (VorlNr) ON DELETE CASCADE
    )
""")

cur.execute("DROP TABLE IF EXISTS Pruefen")
conn.commit()
cur.execute("""
    CREATE TABLE Pruefen(
        MatrNr INTEGER NOT NULL,
        VorlNr INTEGER NOT NULL,
        PersNr INTEGER NOT NULL,
        Note NUMERIC(2,1),
        PRIMARY KEY (MatrNr, VorlNr),
        CONSTRAINT FK_MatrNr FOREIGN KEY (MatrNr) REFERENCES Studenten (MatrNr) ON DELETE CASCADE,
        CONSTRAINT FK_VorlNr FOREIGN KEY (VorlNr) REFERENCES Vorlesungen (VorlNr),
        CONSTRAINT FK_PersNr FOREIGN KEY (PersNr) REFERENCES Professoren (PersNr)
    )
""")

cur.execute("DROP TABLE IF EXISTS Lesen")
conn.commit()
cur.execute("""
    CREATE TABLE Lesen(
        VorlNr INTEGER PRIMARY KEY ,
        PersNr INTEGER NOT NULL,
        CONSTRAINT FK_VorlNr FOREIGN KEY (VorlNr) REFERENCES Vorlesungen (VorlNr),
        CONSTRAINT FK_PersNr FOREIGN KEY (PersNr) REFERENCES Professoren (PersNr)
    )
""")

cur.execute("DROP TABLE IF EXISTS ArbeitenFuer")
conn.commit()
cur.execute("""
    CREATE TABLE ArbeitenFuer(
        PersNrP INTEGER NOT NULL,
        PersNrA INTEGER NOT NULL PRIMARY KEY ,
        CONSTRAINT FK_PersNrP FOREIGN KEY (PersNrP) REFERENCES Professoren (PersNr),
        CONSTRAINT FK_PersNrA FOREIGN KEY (PersNrA) REFERENCES Assistenten (PersNr) ON DELETE CASCADE
    )
""")

cur.execute("DROP TABLE IF EXISTS Voraussetzen")
conn.commit()
cur.execute("""
    CREATE TABLE Voraussetzen(
        Vorgaenger INTEGER NOT NULL,
        Nachfolger INTEGER NOT NULL,
        PRIMARY KEY (Vorgaenger, Nachfolger),
        CONSTRAINT FK_Vorgaenger FOREIGN KEY (Vorgaenger) REFERENCES Vorlesungen (VorlNr) ON DELETE CASCADE,
        CONSTRAINT FK_Nachfolger FOREIGN KEY (Nachfolger) REFERENCES Vorlesungen (VorlNr)
    )
""")

cur.execute("INSERT INTO Studenten(MatrNr, Name, Semester, GebDatum) VALUES (24002, 'Xenokrates', 18, '1984-02-11')")
cur.execute("INSERT INTO Studenten(MatrNr, Name, Semester, GebDatum) VALUES (25403, 'Jonas', 12, '1988-08-09')")
cur.execute("INSERT INTO Studenten(MatrNr, Name, Semester, GebDatum) VALUES (26120, 'Fichte', 10, '1997-07-06')")
cur.execute("INSERT INTO Studenten(MatrNr, Name, Semester, GebDatum) VALUES (26830, 'Aristoxenos', 8, '1999-11-14')")
cur.execute("INSERT INTO Studenten(MatrNr, Name, Semester, GebDatum) VALUES (27550, 'Schopenhauer', 6, '1997-12-10')")
cur.execute("INSERT INTO Studenten(MatrNr, Name, Semester, GebDatum) VALUES (28106, 'Carnap', 3, '1996-05-24')")
cur.execute("INSERT INTO Studenten(MatrNr, Name, Semester, GebDatum) VALUES (29120, 'Theophrastos', 2, '1994-03-15')")
cur.execute("INSERT INTO Studenten(MatrNr, Name, Semester, GebDatum) VALUES (29555, 'Feuerbach', 2, '1995-09-28')")

cur.execute("INSERT INTO Professoren(PersNr, Name, Rang, Raum, GebDatum) VALUES (2125, 'Sokrates', 'C4', 226, '1959-04-03')")
cur.execute("INSERT INTO Professoren(PersNr, Name, Rang, Raum, GebDatum) VALUES (2126, 'Russel', 'C4', 232, '1966-07-13')")
cur.execute("INSERT INTO Professoren(PersNr, Name, Rang, Raum, GebDatum) VALUES (2127, 'Kopernikus', 'C3', 310, '1970-06-12')")
cur.execute("INSERT INTO Professoren(PersNr, Name, Rang, Raum, GebDatum) VALUES (2133, 'Popper', 'C3', 052, '1986-05-26')")
cur.execute("INSERT INTO Professoren(PersNr, Name, Rang, Raum, GebDatum) VALUES (2134, 'Augustinus', 'C3', 309, '1977-10-17')")
cur.execute("INSERT INTO Professoren(PersNr, Name, Rang, Raum, GebDatum) VALUES (2136, 'Curie', 'C4', 036, '1981-02-08')")
cur.execute("INSERT INTO Professoren(PersNr, Name, Rang, Raum, GebDatum) VALUES (2137, 'Kant', 'C4', 007, '1966-08-02')")

cur.execute("INSERT INTO Assistenten(PersNr, Name, Fachgebiet) VALUES (3002, 'Platon', 'Ideenlehre')")
cur.execute("INSERT INTO Assistenten(PersNr, Name, Fachgebiet) VALUES (3003, 'Aristoteles', 'Syllogistik')")
cur.execute("INSERT INTO Assistenten(PersNr, Name, Fachgebiet) VALUES (3004, 'Wittgenstein', 'Sprachtheorie')")
cur.execute("INSERT INTO Assistenten(PersNr, Name, Fachgebiet) VALUES (3005, 'Rhetikus', 'Planetenbewegung')")
cur.execute("INSERT INTO Assistenten(PersNr, Name, Fachgebiet) VALUES (3006, 'Newton', 'Keplersche Gesetze')")
cur.execute("INSERT INTO Assistenten(PersNr, Name, Fachgebiet) VALUES (3007, 'Spinoza', 'Gott und Natur')")

cur.execute("INSERT INTO Vorlesungen(VorlNr, Titel, SWS) VALUES (5001, 'Grundzuege', 4)")
cur.execute("INSERT INTO Vorlesungen(VorlNr, Titel, SWS) VALUES (5041, 'Ethik', 4)")
cur.execute("INSERT INTO Vorlesungen(VorlNr, Titel, SWS) VALUES (5043, 'Erkenntnistheorie', 3)")
cur.execute("INSERT INTO Vorlesungen(VorlNr, Titel, SWS) VALUES (5049, 'Maeeutik', 2)")
cur.execute("INSERT INTO Vorlesungen(VorlNr, Titel, SWS) VALUES (4052, 'Logik', 4)")
cur.execute("INSERT INTO Vorlesungen(VorlNr, Titel, SWS) VALUES (5052, 'Wissenschaftstheorie', 3)")
cur.execute("INSERT INTO Vorlesungen(VorlNr, Titel, SWS) VALUES (5216, 'Bioethik', 2)")
cur.execute("INSERT INTO Vorlesungen(VorlNr, Titel, SWS) VALUES (5259, 'Der Wiener Kreis', 2)")
cur.execute("INSERT INTO Vorlesungen(VorlNr, Titel, SWS) VALUES (5022, 'Glaube und Wissen', 2)")
cur.execute("INSERT INTO Vorlesungen(VorlNr, Titel, SWS) VALUES (4630, 'Die 3 Kritiken', 4)")

cur.execute("INSERT INTO Hoeren(MatrNr, VorlNr) VALUES (26120, 5001)")
cur.execute("INSERT INTO Hoeren(MatrNr, VorlNr) VALUES (27550, 5001)")
cur.execute("INSERT INTO Hoeren(MatrNr, VorlNr) VALUES (27550, 4052)")
cur.execute("INSERT INTO Hoeren(MatrNr, VorlNr) VALUES (28106, 5041)")
cur.execute("INSERT INTO Hoeren(MatrNr, VorlNr) VALUES (28106, 5052)")
cur.execute("INSERT INTO Hoeren(MatrNr, VorlNr) VALUES (28106, 5216)")
cur.execute("INSERT INTO Hoeren(MatrNr, VorlNr) VALUES (28106, 5259)")
cur.execute("INSERT INTO Hoeren(MatrNr, VorlNr) VALUES (29120, 5001)")
cur.execute("INSERT INTO Hoeren(MatrNr, VorlNr) VALUES (29120, 5041)")
cur.execute("INSERT INTO Hoeren(MatrNr, VorlNr) VALUES (29120, 5049)")
cur.execute("INSERT INTO Hoeren(MatrNr, VorlNr) VALUES (29555, 5022)")
cur.execute("INSERT INTO Hoeren(MatrNr, VorlNr) VALUES (25403, 5022)")
cur.execute("INSERT INTO Hoeren(MatrNr, VorlNr) VALUES (29555, 5001)")

cur.execute("INSERT INTO Voraussetzen(Vorgaenger, Nachfolger) VALUES (5001, 5041)")
cur.execute("INSERT INTO Voraussetzen(Vorgaenger, Nachfolger) VALUES (5001, 5043)")
cur.execute("INSERT INTO Voraussetzen(Vorgaenger, Nachfolger) VALUES (5001, 5049)")
cur.execute("INSERT INTO Voraussetzen(Vorgaenger, Nachfolger) VALUES (5041, 5216)")
cur.execute("INSERT INTO Voraussetzen(Vorgaenger, Nachfolger) VALUES (5043, 5052)")
cur.execute("INSERT INTO Voraussetzen(Vorgaenger, Nachfolger) VALUES (5041, 5052)")
cur.execute("INSERT INTO Voraussetzen(Vorgaenger, Nachfolger) VALUES (5052, 5259)")

cur.execute("INSERT INTO ArbeitenFuer(PersNrA,PersNrP) VALUES (3002, 2125)")
cur.execute("INSERT INTO ArbeitenFuer(PersNrA,PersNrP) VALUES (3003, 2125)")
cur.execute("INSERT INTO ArbeitenFuer(PersNrA,PersNrP) VALUES (3004, 2126)")
cur.execute("INSERT INTO ArbeitenFuer(PersNrA,PersNrP) VALUES (3005, 2127)")
cur.execute("INSERT INTO ArbeitenFuer(PersNrA,PersNrP) VALUES (3006, 2127)")
cur.execute("INSERT INTO ArbeitenFuer(PersNrA,PersNrP) VALUES (3007, 2134)")

cur.execute("INSERT INTO Pruefen(MatrNr, VorlNr, PersNr, Note) VALUES (28106, 5001, 2126, 1.0)")
cur.execute("INSERT INTO Pruefen(MatrNr, VorlNr, PersNr, Note) VALUES (25403, 5041, 2125, 2.0)")
cur.execute("INSERT INTO Pruefen(MatrNr, VorlNr, PersNr, Note) VALUES (27550, 4630, 2137, 2.0)")

cur.execute("INSERT INTO Lesen(PersNr,VorlNr) VALUES (2125, 4052);")
cur.execute("INSERT INTO Lesen(PersNr,VorlNr) VALUES (2137, 4630);")
cur.execute("INSERT INTO Lesen(PersNr,VorlNr) VALUES (2137, 5001);")
cur.execute("INSERT INTO Lesen(PersNr,VorlNr) VALUES (2134, 5022);")
cur.execute("INSERT INTO Lesen(PersNr,VorlNr) VALUES (2125, 5041);")
cur.execute("INSERT INTO Lesen(PersNr,VorlNr) VALUES (2126, 5043);")
cur.execute("INSERT INTO Lesen(PersNr,VorlNr) VALUES (2125, 5049);")
cur.execute("INSERT INTO Lesen(PersNr,VorlNr) VALUES (2126, 5052);")
cur.execute("INSERT INTO Lesen(PersNr,VorlNr) VALUES (2126, 5216);")
cur.execute("INSERT INTO Lesen(PersNr,VorlNr) VALUES (2133, 5259);")

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()


conn = sqlite3.connect("namenusa.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS namenusaprostaat")
conn.commit()

cur.execute("""
    CREATE TABLE namenusaprostaat(
        State CHAR(2) NOT NULL,
        Sex CHAR(1) NOT NULL CHECK ( Sex IN ('F', 'M') ),
        Year INTEGER NOT NULL, 
        Name VARCHAR(256) NOT NULL, 
        Births INTEGER NOT NULL,
        CONSTRAINT NamenUSAProStaatKey UNIQUE(State,Name,Sex,Year)
    )
""")

with open('namenusa-insert-1.sql', 'r') as file:
    sql_script = file.read()

cur.executescript(sql_script)
conn.commit()

with open('namenusa-insert-2.sql', 'r') as file:
    sql_script = file.read()

cur.executescript(sql_script)
conn.commit()

cur.close()
conn.close()