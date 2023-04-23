import sqlite3


class DbAdvanced:

    def __init__(self):
        self.conn = sqlite3.connect('tg_data_adv_ru.db')
        self.cur = self.conn.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS tg_data_adv_ru(
           tg_data_id INTEGER PRIMARY KEY,
           MESSAGE_ID INTEGER,
           SENDER CHAR(255),
           CHAT_TITLE CHAR(255),
           DATE INTEGER,
           MESSAGE TEXT,
           ADV_MESSAGE TEXT
           );
        """)
        self.conn.commit()

    def db_cleaning(self):
        self.cur.execute("""DELETE FROM tg_data_adv_ru;""")
        self.conn.commit()

    def insert_into_db(self, new_line):
        self.cur.execute("INSERT INTO tg_data_adv_ru VALUES(NULL, ?, ?, ?, ?, ?, ?);", new_line)
        self.conn.commit()

    def last_date(self):
        self.cur.execute("SELECT MAX(DATE) from tg_data_adv_ru;")
        last_date = self.cur.fetchone()
        return last_date[0]

    def read_db(self, begin, end):
        self.conn = sqlite3.connect('tg_data_adv_ru.db')
        self.cur = self.conn.cursor()
        result = []

        try:

            self.cur.execute("SELECT * from tg_data_adv_ru WHERE DATE BETWEEN ? AND ?", (begin, end))
            records = self.cur.fetchall()
            # print(len(records))
            # print(records[0])

            for row in records:
                result.append(
                    {"MESSAGE_ID": row[1], "SENDER": row[2], "CHAT_TITLE": row[3], "DATE": row[4], "MESSAGE": row[5],
                     "ADV_MESSAGE": row[6]})

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

        finally:
            if self.conn:
                self.conn.close()
                return result
