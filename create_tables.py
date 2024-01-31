from connection import postgres_conn
cursor = postgres_conn.cursor()

def create_tables():

    cursor.execute("""CREATE TABLE facultet(
                   facultet_id SERIAL NOT NULL PRIMARY KEY,
                   name VARCHAR(60) NOT NULL,
                   create_date DATE NOT NULL,
                   discription TEXT,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")

    cursor.execute("""CREATE TABLE speciality(
                   speciality_id SERIAL NOT NULL PRIMARY KEY,
                   name VARCHAR(50) NOT NULL,
                   education_type VARCHAR(10) NOT NULL,
                   facultet_id INT NOT NULL REFERENCES facultet(facultet_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE "group"(
                   group_id SERIAL NOT NULL PRIMARY KEY,
                   name VARCHAR(50) NOT NULL,
                   student_count INT NOT NULL,
                   facultet_id INT NOT NULL REFERENCES facultet(facultet_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE student(
                   student_id SERIAL NOT NULL PRIMARY KEY,
                   first_name VARCHAR(20) NOT NULL,
                   last_name VARCHAR(20) NOT NULL,
                   birth_date DATE NOT NULL,
                   phone_number VARCHAR(20) NOT NULL,
                   address TEXT,
                   gender VARCHAR(1) NOT NULL,
                   group_id INT NOT NULL REFERENCES "group"(group_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    cursor.execute("""CREATE TABLE "user"(
                   user_id SERIAL NOT NULL PRIMARY KEY,
                   first_name VARCHAR(20) NOT NULL,
                   last_name VARCHAR(20) NOT NULL,
                   birth_date DATE NOT NULL,
                   gender VARCHAR(1) NOT NULL,
                   salary NUMERIC(10,2) NOT NULL,
                   username VARCHAR(20) NOT NULL,
                   password VARCHAR(20) NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")
    

    cursor.execute("""CREATE TABLE control(
                   control_id SERIAL NOT NULL PRIMARY KEY,
                   name VARCHAR(60) NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE user_control(
                   user_id INT NOT NULL REFERENCES "user"(user_id),
                   control_id INT NOT NULL REFERENCES control(control_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE subject(
                   subject_id SERIAL NOT NULL PRIMARY KEY,
                   name VARCHAR(60) NOT NULL,
                   semester INT NOT NULL,
                   create_date DATE NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    cursor.execute("""CREATE TABLE user_subject(
                   user_id INT NOT NULL REFERENCES "user"(user_id),
                   subject_id INT NOT NULL REFERENCES subject(subject_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE user_facultet(
                   user_id INT NOT NULL REFERENCES "user"(user_id),
                   facultet_id INT NOT NULL REFERENCES facultet(facultet_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    cursor.execute("""CREATE TABLE subject_facultet(
                   subject_id INT NOT NULL REFERENCES "subject"(subject_id),
                   facultet_id INT NOT NULL REFERENCES facultet(facultet_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    postgres_conn.commit()
    print("CREATE TABLE")

