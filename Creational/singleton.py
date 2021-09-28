from sqlite3 import connect


def singleton(cls):
    instance = cls()

    def wrapper():
        return instance
    return wrapper


@singleton
class UsersDataBase:
    def __init__(self):
        self.conn = connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
            user_id         INT PRIMARY KEY,
            first_name      TEXT,
            last_name       TEXT);
        """)
        self.conn.commit()

    def add_user(self, user: tuple):
        self.cursor.execute("""
            INSERT INTO users VALUES(?, ?, ?);
            """, user)
        self.conn.commit()

    def getUser(self, user_id: int):
        self.cursor.execute("SELECT * FROM users WHERE user_id = ?;", (user_id, ))
        print('\nRequested user:', end=f"\n{'_' * 50}\n")
        user_id, first_name, last_name = self.cursor.fetchone()
        print(f'User id: {user_id}\n'
                f'Full name: {first_name} {last_name}', end=f"\n{'_' * 50}\n")

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users;")
        print('\nData base contains such users as:', end=f"\n{'_' * 50}\n")

        for user in self.cursor.fetchall():
            user_id, first_name, last_name = user
            print(f'User id: {user_id}\n'
                  f'Full name: {first_name} {last_name}', end=f"\n{'_' * 50}\n")


if __name__ == '__main__':
    from random import randrange

    users_dict = {
        'Ivan Petrenko': (0, 'Ivan', 'Petrenko'),
        'Mamba Bumba': (1, 'Mamba', 'Bumba'),
        'Max Pain': (2, 'Max', 'Pain')
    }
    db_port_1 = UsersDataBase()
    db_port_2 = UsersDataBase()
    print(f'db_port_1 is db_port_2 - {db_port_1 is db_port_2}')

    for user_data in sorted(users_dict.values()):
        db_port_1.add_user(user_data)
    db_port_2.get_all_users()
    db_port_1.getUser(randrange(len(users_dict)))
