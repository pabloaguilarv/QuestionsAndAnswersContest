from base_model import BaseModel as DB

ranks = [1,2,3,4,5]

def enter_questions(quantity=25):
    with DB('models/contest.db') as db:
        for _ in range(quantity):
            question = input('Enter the question and category comma-separated: ').split(',')
            db.execute('insert into questions (statement,category_id) values(?,?)',(question[0],question[1]))
            enter_options(db.cursor.lastrowid)

def enter_options(question_id):
    with DB('contest.db') as db:
        for _ in range(4):
            option = input('Enter text and 0 or 1, 1 for the correct answer separated by a comma: ').split(',')
            db.execute('insert into options (option,is_correct,question_id) values(?,?,?)',(option[0],option[1],question_id))


if __name__ == '__main__':
    with DB('contest.db') as db:
        db.executescript('''create table if not exists questions(
        id integer not null primary key autoincrement unique,
        category_id integer not null,
        statement text not null
    );
    create table if not exists options(
        id integer not null primary key autoincrement unique,
        option text not null,
        question_id integer not null,
        is_correct integer not null
    )''')

    with DB('players.db') as db:
        db.execute('''create table if not exists players(
    id integer not null primary key autoincrement unique,
    name text unique not null,
    max_rank integer,
    max_prize integer
    );'''
    )
    enter_questions(input('Number of questions to enter(blank for 25): '))
