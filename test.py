from datetime import datetime
import sqlite3


def toDB(line):
    line = datetime.today().strftime("%H:%M:%S %d/%m") + ',' + line + '\n'
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO weather VALUES (?,?,?,?,?,?,?)", line.split(','))
    except sqlite3.OperationalError:
        c.execute("CREATE TABLE weather (Timestamp,Temp,Humidity,Press,WindSpd,WindDir,Rain)")
        c.execute("INSERT INTO weather VALUES (?,?,?,?,?,?,?)", line.split(','))
    conn.commit()
    conn.close()
