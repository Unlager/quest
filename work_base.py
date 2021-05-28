import sqlite3


class withDataBase:
    def takeFromBase(self):
        conn = sqlite3.connect("data_base.db")
        cursor = conn.cursor()
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        new_datas = cursor.fetchall()
        return new_datas
        conn.close()

    def addToBase(self, data_id, data_name):
        conn = sqlite3.connect("data_base.db")
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) FROM users WHERE id = ?", (data_id,))
        data=cursor.fetchone()[0]
        if data == 0:
            cursor.execute('''INSERT INTO users(id, nickname, access) VALUES (?, ?, ?)''', (data_id, data_name, 'start'))
            conn.commit()
            conn.close()
        else:
            conn.close()
    def update_base(self, data_id):
        conn = sqlite3.connect("data_base.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET access = 'end' WHERE id = ?", (data_id,))
        conn.commit()


    def addToBaseAdmins(self, data_id, data_name, data_access):
        conn = sqlite3.connect("data_base.db")
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO users(id, nickname, access) VALUES (?, ?, ?)''', (data_id, data_name, data_access))
        conn.commit()
        conn.close()

    def deleteFromBase(self):
        conn = sqlite3.connect("data_base.db")
        cursor = conn.cursor()
        sql = "DELETE FROM users WHERE id = '447567648'"
        cursor.execute(sql)
        conn.commit()
        conn.close()

    def test(self, data_id):
        conn = sqlite3.connect("data_base.db")
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) FROM users WHERE id = ?", (data_id,))
        data=cursor.fetchone()[0]
        if data == 0:
            print("Нет пользователя")
        else:
            print("Пользователь есть")
        conn.close()
workWithBase = withDataBase()
