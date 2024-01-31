from connection import postgres_conn

cursor = postgres_conn.cursor()

def insert_tables():

    cursor.execute(f"INSERT INTO facultet(name,create_date,discription) VALUES('sowftwere ingeneer','4-10-2000','in this facultet you will learn more about softwere ingeneering')")


    cursor.execute(f"INSERT INTO speciality(name,education_type,facultet_id) VALUES('dasturlash','kunduzgi',1)")


    cursor.execute(f"INSERT INTO \"group\"(name,student_count,facultet_id) VALUES('kelajak kasblari',24,1)")


    cursor.execute(f"INSERT INTO student(first_name,last_name,birth_date,phone_number,address,gender,group_id) VALUES('ahmad','japporov','11-11-2001','+998-99-272-23-23','toshkent shahar chilonzor 9 1 4','m',1)")


    cursor.execute(f"INSERT INTO \"user\"(first_name,last_name,birth_date,gender,salary,username,password) VALUES('bobur','aliyev','11-11-1985','m',30_000_000,'bobur123','password123')")


    cursor.execute(f"INSERT INTO control(name) VALUES('teacher')")


    cursor.execute(f"INSERT INTO user_control(user_id,control_id) VALUES(1,1)")


    cursor.execute(f"INSERT INTO subject(name,semester,create_date) VALUES('matematika',3,'2-3-2005')")


    cursor.execute(f"INSERT INTO user_subject(user_id,subject_id) VALUES(1,1)")


    cursor.execute(f"INSERT INTO user_facultet(user_id,facultet_id) VALUES(1,1)")

    cursor.execute(f"INSERT INTO subject_facultet(subject_id,facultet_id) VALUES(1,1)")


    postgres_conn.commit()
    print("INSERT 0 1")
