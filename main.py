import csv, sqlite3

if __name__ == '__main__':
    con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    curs = con.cursor()
    cur.execute("CREATE TABLE polaczenia (from_subscriber,to_subscriber,datetime,duration,celltower);")

    with open("polaczenia_duze.csv", "r") as fin:
        reader = csv.reader(fin, delimiter = ";")
        next(reader, None)
        rows = [x for x in reader]
        curs.executemany("INSERT INTO polaczenia (from_subscriber, to_subscriber, datetime, duration , celltower) VALUES (?, ?, ?, ?, ?)", rows,)

    sql_con
    cursor = sql_con.cursor()
    cursor.execute("SELECT sum(duration) from polaczenia")
    final = cursor.fetchone()[0]

print(str(final))