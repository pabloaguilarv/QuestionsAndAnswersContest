from models.base_model import BaseModel as DB

ranks = [1,2,3,4,5]

def enter_questions():
    with DB('models/contest.db') as db:
        with open('questions.txt') as file:

            for line in file:
                question = line.rstrip().split(',')
                db.execute('insert or ignore into questions (statement,category_id) values(?,?)',(question[0],question[1]))
                question_id = db.cursor.lastrowid

                for _ in range(4):
                    line = next(file,"")
                    option = line.rstrip().split(',')
                    db.execute('insert or ignore into options (option,question_id,is_correct) values(?,?,?)',(option[0],question_id,option[-1]))
                    
        db.commit()

if __name__ == '__main__':
    with DB('models/contest.db') as db:
        db.execute('''create table if not exists questions(
        id integer not null primary key autoincrement unique,
        category_id integer not null,
        statement text not null
    )''')
        db.execute('''create table if not exists options(
        id integer not null primary key autoincrement unique,
        option text not null,
        question_id integer not null,
        is_correct integer not null
    )''')

    with DB('models/players.db') as db:
        db.execute('''create table if not exists players(
    id integer not null primary key autoincrement unique,
    name text unique not null,
    max_rank integer,
    max_prize integer
    );'''
    )
    enter_questions()
