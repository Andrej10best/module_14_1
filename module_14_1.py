import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT not null,
email TEXT not null,
age INTEGER,
balance INTEGER not null
)
''')
'''Добавляю 10 записей'''
for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) '
                   'VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', i * 10, 1000)
                   )
'''Меняю баланс в каждой второй строке'''
cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 != 0', (500,))

'''Удаляю каждую третью строку'''
for i in range(1, 11):
    if (i - 1) % 3 == 0:
        cursor.execute(f'DELETE FROM Users WHERE id = {i}')

'''Вывожу в консоль всех пользователей, возраст которых не равен 60'''
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

connection.commit()
connection.close()
