# importing the required modules
import sqlite3

# setting up the connection with database
conn = sqlite3.connect('inCollege.db')
print("Successfully connected to the database")

# defining the cursor
cursor = conn.cursor()

# creating user profile table
users_table = cursor.execute(""" CREATE TABLE IF NOT EXISTS users(
    first_name TEXT,
    last_name TEXT,
    user_name TEXT,
    password CHAR(12),
    email INT,
    sms INT,
    advertising INT,
    spanish INT,
    account_type TEXT,
    billing_rate FLOAT,
    last_day_apply_for_job date,
    job_section_message TEXT,
    login_message TEXT
    
);
""")
# only to be executed one time so the table can be expanded without ruining rest of table
# cursor.execute("ALTER TABLE users ADD account_type TEXT")
# cursor.execute("ALTER TABLE users ADD billing_rate FLOAT")

users_table = cursor.fetchall()
# print(users_table)
for i in users_table:
    print(i)

# creating jobs table
jobs_table = cursor.execute(""" CREATE TABLE IF NOT EXISTS jobs(
    title TEXT,
    description TEXT,
    employer TEXT,
    location TEXT,
    salary TEXT,
    user TEXT
);
""")

jobs_table = cursor.fetchall()
for i in jobs_table:
    print(i)

# creating jobs_applications table
job_applications_table = cursor.execute(""" CREATE TABLE IF NOT EXISTS job_applications(
    job_title TEXT,
    applicant TEXT,
    grad_date TEXT,
    job_start_date TEXT,
    reason TEXT,
    apply_day date
);
""")

job_applications_table = cursor.fetchall()
for i in job_applications_table:
    print(i)


# creating saved_jobs table
saved_jobs_table = cursor.execute(""" CREATE TABLE IF NOT EXISTS saved_jobs(
    job_title TEXT,
    user TEXT
);
""")

saved_jobs_table = cursor.fetchall()
for i in saved_jobs_table:
    print(i)


# create profile table
profile_table = cursor.execute(""" CREATE TABLE IF NOT EXISTS profile(
    title TEXT,
    major TEXT,
    university TEXT,
    info TEXT,
    user TEXT
);
""")
profile_table = cursor.fetchall()
for i in profile_table:
    print(i)

# create experience table
exp_table = cursor.execute(""" CREATE TABLE IF NOT EXISTS exp(
    title TEXT,
    employer TEXT,
    startDate TEXT,
    endDate TEXT,
    location TEXT,
    description TEXT,
    user TEXT
);
""")
exp_table = cursor.fetchall()
for i in exp_table:
    print(i)

# create education table
edu_table = cursor.execute(""" CREATE TABLE IF NOT EXISTS edu(
    schoolName TEXT,
    degreeEarn TEXT,
    yearAttend TEXT,
    user TEXT
);
""")
edu_table = cursor.fetchall()
for i in edu_table:
    print(i)


# create friend table
friend_table = cursor.execute(""" CREATE TABLE IF NOT EXISTS Friends(
    user TEXT,
    friend_username TEXT 
);
""")
friend_table = cursor.fetchall()
for i in friend_table:
    print(i)

# create friend request table
request_table = cursor.execute(""" CREATE TABLE IF NOT EXISTS Request(
    user TEXT,
    friend_username TEXT,
    status TEXT
);
""")
request_table = cursor.fetchall()
for i in request_table:
    print(i)

cursor.close()
conn.commit()

# closing the connection
conn.close()

# Michael epic #7
# second database for messages
# setting up the connection with database
conn = sqlite3.connect('inCollege_messages.db')
print("Successfully connected to the database")

# defining the cursor
cursor = conn.cursor()

# create messages table
messages_table = cursor.execute(""" CREATE TABLE IF NOT EXISTS Messages(
    from_user TEXT,
    to_user TEXT,
    message TEXT,
    read INT
);
""")
messages_table = cursor.fetchall()
for i in messages_table:
    print(i)

# create course table
courses_table = cursor.execute(""" CREATE TABLE IF NOT EXISTS Courses(
    course TEXT,
    user TEXT
);
""")
courses_table = cursor.fetchall()
for i in courses_table:
    print(i)

cursor.close()
conn.commit()

# closing the connection
conn.close()
