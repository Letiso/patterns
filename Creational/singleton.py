from sqlite3 import connect


def singleton(cls):
    data_base = cls()

    def wrapper():
        return data_base
    return wrapper


@singleton
class DataBase:
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

    def add_user(self, user):
        self.cursor.execute("""
            INSERT INTO users VALUES(?, ?, ?);
            """, user)
        self.conn.commit()

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users;")
        print('Data base contains such users as:', end=f"\n{'_' * 50}\n")

        for user in self.cursor.fetchall():
            user_id, first_name, last_name = user
            print(f'User id: {user_id}\n'
                  f'Full name: {first_name} {last_name}', end=f"\n{'_' * 50}\n")


if __name__ == '__main__':
    users_dict = {
        'Ivan Petrenko': (0, 'Ivan', 'Petrenko'),
        'Mamba Araratov': (1, 'Mamba', 'Araratov'),
        'Max Pain': (2, 'Max', 'Pain')
    }
    db_port_1 = DataBase()
    db_port_2 = DataBase()
    print(f'db_port_1 is db_port_2 - {db_port_1 is db_port_2}')

    for user_data in sorted(users_dict.values()):
        db_port_1.add_user(user_data)
    db_port_2.get_all_users()
