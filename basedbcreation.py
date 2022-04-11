import sqlite3 as sql
import hmac
import hashlib

db_connection = sql.connect('contest.db')
db_cursor = db_connection.cursor()

ranks = [1,2,3,4,5]

db_cursor.executescript('''create table if not exists players(
    id integer not null primary key autoincrement unique,
    name text unique not null,
    full_contests_won integer,
    highest_rank integer,
    prizes_won integer,
    last_prize_won text,
    last_rank_achieved integer
);
    create table if not exists rank_1(
        id integer not null primary key autoincrement unique,
        question text,
        option_a text,
        option_b text,
        option_c text,
        option_d text,
        correct_answer text
);
    
    create table if not exists rank_2(
        id integer not null primary key autoincrement unique,
        question text,
        option_a text,
        option_b text,
        option_c text,
        option_d text,
        correct_answer text
);
    
    create table if not exists rank_3(
        id integer not null primary key autoincrement unique,
        question text,
        option_a text,
        option_b text,
        option_c text,
        option_d text,
        correct_answer text
);
    
    create table if not exists rank_4(
        id integer not null primary key autoincrement unique,
        question text,
        option_a text,
        option_b text,
        option_c text,
        option_d text,
        correct_answer text
);
    
    create table if not exists rank_5(
        id integer not null primary key autoincrement unique,
        question text,
        option_a text,
        option_b text,
        option_c text,
        option_d text,
        correct_answer text
)''')

for rank in ranks:
    question_quantity = int(input(f'How many questions for rank {rank}?'))

    print(f'Provide the information for the questions in rank {rank}.')

    for _ in range(question_quantity):
        question = input('Question:')
        option_a = input('Option A:')
        option_b = input('Option B:')
        option_c = input('Option C:')
        option_d = input('Option D:')
        correct_answer = input('Correct answer (A,B,C,D):')

        #secret_answer = hmac.new('ijdf74'.encode('utf-8'),correct_answer.encode('utf-8'),hashlib.sha256).hexdigest()

        db_cursor.execute('insert or ignore into rank_'+str(rank)+''' 
        (question,option_a,option_b,option_c,option_d,correct_answer) values(?,?,?,?,?,?)''',
        (question,option_a,option_b,option_c,option_d,correct_answer)
        )

db_connection.commit()
db_connection.close()