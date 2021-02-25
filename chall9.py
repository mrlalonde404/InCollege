# Software Engineering
import setup
import string
import sqlite3
import login
from datetime import date, timedelta, datetime
import itertools

# Variable declaration
# requirements for password
password_min_length = 8
password_max_length = 12
# limits for certain things on the site
max_number_users = 10
max_number_jobs = 10
max_number_exp = 3
# used to indicate if a user is logged on & who they are
logged_in = False
# used to display new pending friend requests
user = None
friends = []
# used to display messages from messages
inbox = []
# a job title for a new job (temporary)
a_new_job = None

# holds order of pages the user visited
# insert into stack a function name when function called
# remove when exiting that function
stack = []


# displays menu options from list menu_options in an enumerated list
def display_menu(menu_options, is_home_page):
    # if not the main menu and the user can return to a previous menu present the 0th option
    if not is_home_page:
        print("\n0. To return to previous page")
    count = 1

    for option in menu_options:
        print(str(count) + '. ' + option)
        count += 1


# prompts user for selection of a valid menu item number from 0 (or 1 if home_screen) to option_size
def make_selection(option_size, is_home_screen):
    selection = input("Enter your selection: ")
    min_number = 0
    if is_home_screen:
        min_number = 1
    while not selection.isnumeric() or not (int(selection) >= min_number and int(selection) <= option_size):
        print("Invalid selection! Try again")
        selection = input("Enter your selection: ")
    return selection


# used for pages that only display a message to the user such as "Under Construction"
# or "We're here to help" but don't provide the user with anything more to do
def display_return_message():
    selection = None
    while selection != "0":
        selection = input("Enter 0 to return to previous page: ")
    stack.pop()()  # call previous function


def help_center():
    print("We're here to help")
    return "We're here to help"


def about():
    print(
        "\nIn College: Welcome to In College, the world's largest college student network with many users in many "
        "countries and territories worldwide")
    return "\nIn College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide"


def press():
    print("\nIn College Pressroom: Stay on top of the latest news, updates, and reports")
    return "\nIn College Pressroom: Stay on top of the latest news, updates, and reports"


def blog():
    print("Under Construction\n")
    return "Under Construction\n"


def careers():
    print("Under Construction\n")
    return "Under Construction\n"


def developers():
    print("Under Construction\n")
    return "Under Construction\n"


# define a function General group
def general():
    stack.append(general)
    # selections in the menu
    menu_options = ["Sign Up",
                    "Help Center",
                    "About",
                    "Press",
                    "Blog",
                    "Careers",
                    "Developers"]
    display_menu(menu_options, False)
    selection = make_selection(len(menu_options), False)
    # evaluate selection
    # return to previous page
    if selection == "0":
        stack.pop()  # remove self from stack
        stack.pop()()  # call previous function
    # go to login page
    elif selection == "1":
        login_or_register()
    # go to help center
    elif selection == "2":
        help_center()
        display_return_message()
    # go to about page
    elif selection == "3":
        about()
        display_return_message()
    # go to press page
    elif selection == "4":
        press()
        display_return_message()
    # go to blog page
    elif selection == "5":
        blog()
        display_return_message()
    # go to careers page
    elif selection == "6":
        careers()
        display_return_message()
    # go to developers page
    elif selection == "7":
        developers()
        display_return_message()


# define a function Browse InCollege
def browse_inCollege():
    print("Under Construction\n")
    return "Under Construction\n"


# define a function Business Solutions
def business_solution():
    print("Under Construction\n")
    return "Under Construction\n"


# define a function Directories
def directories():
    print("Under Construction\n")
    return "Under Construction\n"


# function for "Useful Links"
def useful_links():
    stack.append(useful_links)
    menu_options = ["General",
                    "Browse InCollege",
                    "Business Solutions",
                    "Directories"]

    display_menu(menu_options, False)
    selection = make_selection(len(menu_options), False)
    if selection == "0":
        stack.pop()  # remove self from stack
        stack.pop()()  # call previous function
    elif selection == "1":
        general()
        display_return_message()
    elif selection == "2":
        browse_inCollege()
        display_return_message()
    elif selection == "3":
        business_solution()
        display_return_message()
    elif selection == "4":
        directories()
        display_return_message()


def evaluate_off_on_controls(attribute):
    menu_options = ["Off", "On"]
    display_menu(menu_options, False)
    selection = make_selection(len(menu_options), False)
    # turn off control
    if selection == "1":
        # connect to database
        conn = sqlite3.connect("inCollege.db")
        cur = conn.cursor()
        cur.execute("UPDATE users SET " + attribute + " = 0 WHERE user_name = ? ", ([user]))
        conn.commit()
        return 1
    # turn on control
    elif selection == "2":
        # connect to database
        conn = sqlite3.connect("inCollege.db")
        cur = conn.cursor()
        cur.execute("UPDATE users SET " + attribute + " = 1 WHERE user_name = ? ", ([user]))
        conn.commit()
        return 2
    elif selection == "0":
        stack.pop()()


def logged_in_privacy_policy():
    print("We won't share your contact information with anyone without your consent")
    menu_options = ["Guest Controls"]
    display_menu(menu_options, False)
    selection = make_selection(len(menu_options), False)
    if selection == "1":
        print("Guest Controls Options")
        print("\tinCollege email")
        evaluate_off_on_controls("email")
        print("\tSMS")
        evaluate_off_on_controls("sms")
        print("\tTargeted Advertising")
        evaluate_off_on_controls("advertising")
    else:
        stack.pop()()


def copyright_notice():
    print("Copyright 2020 inCollege Inc, All rights reserved")
    return "Copyright 2020 inCollege Inc, All rights reserved"


def important_about():
    print("Our site came to be when our world was widespread in the deadly virus known as Corona\n"
          "We wanted to create a virtual space for college students everywhere.\n"
          "Where they could connect & share experiences & opportunities\n")
    return ("Our site came to be when our world was widespread in the deadly virus known as Corona\n"
            "We wanted to create a virtual space for college students everywhere.\n"
            "Where they could connect & share experiences & opportunities\n")


def accessibility():
    print("We strive to make our simple text based interface as accessible as possible\n"
          "Additional font sizes coming soon!")
    return ("We strive to make our simple text based interface as accessible as possible\n"
            "Additional font sizes coming soon!")


def user_agreement():
    print("As we provide this service to you, we ask that you be respectful of all other inCollege users\n"
          "Failure to do so can result in deletion of your posts or eventual termination of your account\n"
          "inCollege will treat you with the respect you deserve")
    return ("As we provide this service to you, we ask that you be respectful of all other inCollege users\n"
            "Failure to do so can result in deletion of your posts or eventual termination of your account\n"
            "inCollege will treat you with the respect you deserve")


def privacy_policy():
    print("As we provide this service to you, we ask that you be respectful of all other inCollege users\n"
          "Failure to do so can result in deletion of your posts or eventual termination of your account\n"
          "inCollege will treat you with the respect you deserve")
    return ("As we provide this service to you, we ask that you be respectful of all other inCollege users\n"
            "Failure to do so can result in deletion of your posts or eventual termination of your account\n"
            "inCollege will treat you with the respect you deserve")


def cookie_policy():
    print(
        "Cookies are yummy but not the cookies we are using\nOurs identify users to recognize if you are an existing user"
        "\nand help provide the ability to post and eventually apply for jobs")
    return (
        "Cookies are yummy but not the cookies we are using\nOurs identify users to recognize if you are an existing user"
        "\nand help provide the ability to post and eventually apply for jobs")


def copyright_policy():
    print("We respect you as an individual & your intellectual property rights\n"
          "We will not violate those rights\n"
          "We just require that what you post is accurate, lawful, and not in violation of others' rights")
    return ("We respect you as an individual & your intellectual property rights\n"
            "We will not violate those rights\n"
            "We just require that what you post is accurate, lawful, and not in violation of others' rights")


def brand_policy():
    print("You are allowed to use the inCollege logo to designate a link to your inCollege profile\n"
          "When referring to inCollege, the name should always be written as one word exactly as shown: inCollege")
    return ("You are allowed to use the inCollege logo to designate a link to your inCollege profile\n"
            "When referring to inCollege, the name should always be written as one word exactly as shown: inCollege")


def language():
    print("\tLanguage Selection")
    print("Turn Spanish on or off")
    evaluate_off_on_controls("spanish")
    return "Language"


# InCollege Important Links
def inCollege_important_links():
    stack.append(inCollege_important_links)
    menu_options = ["A Copyright Notice",
                    "About",
                    "Accessibility",
                    "User Agreement",
                    "Privacy Policy",
                    "Cookie Policy",
                    "Copyright Policy",
                    "Brand Policy"]
    # if logged on also give Languages link
    if logged_in: menu_options.append("Languages")
    display_menu(menu_options, False)
    selection = make_selection(len(menu_options), False)
    # evaluate selection
    # go back to previous page
    if selection == "0":
        stack.pop()  # remove self from stack
        stack.pop()()  # call previous function
    # display copyright page
    elif selection == "1":
        copyright_notice()
        display_return_message()
    # display about message page
    elif selection == "2":
        important_about()
        display_return_message()
    # display accessibility message page
    elif selection == "3":
        accessibility()
        display_return_message()
    # display user agreement message page
    elif selection == "4":
        user_agreement()
        display_return_message()
    elif selection == "5":
        # if user not logged in display privacy policy message only
        if not logged_in:
            privacy_policy()
            display_return_message()
        # if user is logged in give logged in privacy policy including guest controls
        else:
            # add logged_in_privacy_policy to stack since it is taking you to another page with menu options
            stack.append(logged_in_privacy_policy)
            logged_in_privacy_policy()
            # displays no message but prompts user to enter 0 to return to previous page
            display_return_message()
        # cookie policy
    elif selection == "6":
        cookie_policy()
        display_return_message()
        # copyright policy
    elif selection == "7":
        copyright_policy()
        display_return_message()
        # brand policy
    elif selection == "8":
        brand_policy()
        display_return_message()
        # language option
    elif selection == "9":
        language()
        display_return_message()


# this function will display "Under Construction"
def display_under_construction():
    print("Under Construction\n")
    return "Under Construction\n"


# This function allows you to learn 5 skills, and return to the previous menu
def learn_new_skill():
    stack.append(learn_new_skill)
    menu_options = ["Learn Python"
                    "Learn HTML",
                    "Learn to dance the tango",
                    "Learn to sing opera music",
                    "Learn to walk 5 large dogs at a time"]
    display_menu(menu_options, False)
    selection = make_selection(len(menu_options), False)
    # Learn Python
    if selection == "1":
        display_under_construction()
        display_return_message()
    # Learn HTML
    elif selection == "2":
        display_under_construction()
        display_return_message()
    # Learn to dance the tango
    elif selection == "3":
        display_under_construction()
        display_return_message()
    # Learn to sing opera music
    elif selection == "4":
        display_under_construction()
        display_return_message()
    # Learn to walk 5 large dogs at a time
    elif selection == "5":
        display_under_construction()
        display_return_message()
    # Go back to previous level
    elif selection == "0":
        stack.pop()  # remove self from stack
        stack.pop()()  # call previous function


def create_job(username=user):

    # connect to database
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()

    jobs_table = cur.execute("SELECT title,description,employer,location,salary,user FROM jobs").fetchall()
    # check if adding this job would mean more than 5 jobs in the system
    if len(jobs_table) + 1 > max_number_jobs:
        print("All permitted jobs have been posted, please come back later")
        return "All permitted jobs have been posted, please come back later"
    # if not, get job info and create the job
    else:
        # a job must contain a  title, a description, the employer, a location, and a salary
        print("Here you can post a job to the inCollege website!")
        title = input("Enter a job name: ")

        description = input("Enter a job description: ")
        employer = input("Enter the job's employer: ")
        location = input("Enter the job's location: ")
        salary = input("Enter the job's salary: ")
        cur.execute(''' INSERT INTO jobs(title,description,employer,location,salary,user)
                VALUES(?,?,?,?,?,?)''', (title, description, employer, location, salary, username))
        cur.execute('''UPDATE users set job_section_message = ? ''', (title,))
        conn.commit()
        cur.close()
        conn.close()
        print("created job: " + title)


def post_job(username=user):
    stack.append(post_job)
    # print(jobs_table)
    create_job(username)
    stack.pop()
    stack.pop()()


# Create experience for each user
def create_experience(username=user):
    # connect to database
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    # Create experience table
    cur.execute("SELECT title,employer,startDate,endDate,location,description,user FROM exp").fetchall()
    # Check the limit of the past jobs post
    cur.execute("SELECT * FROM exp WHERE user = ? ", (username,))
    rows = len(cur.fetchall())
    if rows + 1 > max_number_exp:
        print("You can only add up to 3 past jobs.")
    else:
        title = input("Enter your title: ")
        employer = input("Enter your employer: ")
        startDate = input("Enter your start date: ")
        endDate = input("Enter your end date: ")
        location = input("Enter your location: ")
        description = input("Enter the description of the job: ")
        # Add to the table
        cur.execute(''' INSERT INTO exp(title,employer,startDate,endDate,location,description,user)
                        VALUES(?,?,?,?,?,?,?)''',
                    (title, employer, startDate, endDate, location, description, username))
        conn.commit()
        cur.close()
        conn.close()


# Create education profile for user
def create_education(username=user):
    # connect to database
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    # Create education table
    cur.execute("SELECT schoolName,degreeEarn,yearAttend,user FROM edu").fetchall()

    schoolName = input("Enter your school name: ")
    degreeEarn = input("Enter your degree: ")
    yearAttend = input("Enter the year you attended: ")
    # Add to the table
    cur.execute(''' INSERT INTO edu(schoolName,degreeEarn,yearAttend,user)
                        VALUES(?,?,?,?)''', (schoolName.title(), degreeEarn.title(), yearAttend, username))
    conn.commit()
    cur.close()
    conn.close()


# Create the profile for each user
def create_profile(username=user):
    # connect to database
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    # Create profile table
    title = input("Enter a title for your profile: ")
    maj = input("Enter your major: ")
    major = maj.title()
    uni = input("Enter your university: ")
    university = uni.title()
    info = input("Enter info for your about section: ")
    # Add to the table
    cur.execute(''' INSERT INTO profile(title,major,university,info,user)
                            VALUES(?,?,?,?,?)''', (title, major, university, info, username))
    conn.commit()
    cur.close()
    conn.close()


# User will create their profile
def user_profile():
    stack.append(user_profile)
    global user
    menu_options = ["Add profile information.",
                    "Add job experience.",
                    "Add education."]

    while logged_in:
        display_menu(menu_options, False)
        selection = make_selection(len(menu_options), False)
        if selection == "0":
            stack.pop()
            stack.pop()()
        elif selection == "1":
            print("Here you can create a personal profile for yourself!")
            create_profile(user)
        elif selection == "2":
            print("Now you can enter your experience: ")
            create_experience(user)
        elif selection == "3":
            print("Now you can enter your education: ")
            create_education(user)


# function for display profile information
def display_profile(username=user):
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    user_table = cur.execute("SELECT first_name, last_name from users WHERE user_name = ?", (username,)).fetchall()
    print(user_table[0][0] + " " + user_table[0][1])
    profile_table = cur.execute("SELECT title,major,university,info FROM profile WHERE user = ? ",
                                (username,)).fetchall()
    if not profile_table:
        print("No Profile Created Yet")
    else:
        profile_table = profile_table[0]
        print("Profile Title: " + str(profile_table[0]) + "\nMajor: " + str(profile_table[1]) + "\nUniversity: " + str(
            profile_table[2])
              + "\nInfo: " + str(profile_table[3]))

    experience_table = cur.execute("SELECT title, employer, startDate, endDate, location, description From exp Where "
                                   "user = ? ", (username,)).fetchall()
    if not experience_table:
        print("No Experiences Yet")
    else:
        print("Experience")
        for experience in experience_table:
            print("Title: " + experience[0] + "\nEmployer: " + experience[1] + "Start Date: " + experience[2]
                  + "\nEnd Date: " + experience[3] + "\nLocation: " + experience[4] + "\nDescription: " + experience[5])

    education_table = cur.execute("SELECT schoolName, degreeEarn, yearAttend FROM edu WHERE user = ? ",
                                  (username,)).fetchall()
    if not education_table:
        print("No Education Listed")
    else:
        print("Education")
        for education in education_table:
            print("School Name: " + education[0] + "\nDegree: " + education[1] + "\nYear Attended: " + education[2])
    conn.commit()
    cur.close()
    conn.close()
    # display_return_message()


# Aliaksandra, epic #5
# this function adds user to friend list when a friend request is accepted
def add_friend(friend_username, username=user):
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    cur.execute(''' INSERT INTO Friends(user,friend_username)
                    VALUES(?,?)''', (username, friend_username))
    cur.execute(''' INSERT INTO Friends(user,friend_username)
                    VALUES(?,?)''', (friend_username, username))
    conn.commit()
    cur.close()
    conn.close()
    print("You and " + friend_username + " are now friends!")


# Aliaksandra, epic #5
# deleting a friend from friend list
def delete_friend(friend_username, username=user):
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    cur.execute('''DELETE FROM Friends where user = ? and friend_username = ?''',
                (username, friend_username))
    cur.execute('''DELETE FROM Friends where user = ? and friend_username = ?''',
                (friend_username, username))
    conn.commit()
    cur.close()
    conn.close()
    print("You and " + friend_username + " are no longer friends")


# Aliaksandra, epic #5
# this function is called to reject/delete a pending friend request
def delete_pending_request(friend_username, username=user):
    global user
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    status = 'Pending'
    cur.execute('''DELETE FROM Request where user = ? and status = ?''',
                (friend_username, status))
    conn.commit()
    cur.close()
    conn.close()


# Aliaksandra, epic #5
# this function is used to get the friend list
def friend_list(username=user):
    global friends
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    # commented out, but shows the friends table
    # friend_table = cur.execute(" SELECT friend_username FROM Friends", ).fetchall()
    friend_table = cur.execute("SELECT friend_username FROM Friends WHERE user = ?", (username,)).fetchall()
    friends = [item[0] for item in friend_table]
    if len(friends) < 1:
        print("You do not have any friends")
        selection = input("Enter 0 to return to previous page: ")
        if selection == "0":
            stack.pop()
            stack.pop()()  # call previous function
    # print the friends of the current user
    print("My friends' usernames:")
    print(friends)
    conn.commit()
    cur.close()
    conn.close()


# Aliaksandra, epic #5
# this function is used to display user's friends and their profiles
def display_friends():
    global user
    stack.append(display_friends)
    friend_list(user)
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    menu_options = ["View friend's profile",
                    "Delete friend"]
    display_menu(menu_options, False)
    friend_username = None
    selection = make_selection(len(menu_options), False)
    if selection == "0":
        stack.pop()
        stack.pop()()
    # display profile
    if selection == "1":
        friend_username = input("Type friend's username to view their profile: ")
        if friend_username in friends:
            display_profile(friend_username)
    elif selection == "2":
        # delete friend
        friend_username = input("Type friend's username to delete: ")
        delete_friend(friend_username, username=user)
    if friend_username not in friends:
        print(friend_username, " is not ", user, "'s friend")
    conn.commit()
    cur.close()
    conn.close()


# Uyen, Epic #5
# This function is used to send a friend request
def send_friend_request(username=user):
    global user
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    cur.execute("SELECT user,friend_username,status FROM Request").fetchall()
    userName = input("Enter the username of student you want to add friend: ")
    if userName == user:
        print("You cannot send the friend request to yourself.")
        display_return_message()
    cur.execute("SELECT * FROM users WHERE user_name = ?", (userName,))
    students = cur.fetchall()
    found_student = False
    for student in students:
        if userName == student[2]:
            found_student = True
            request = 'Pending'
            cur.execute(''' INSERT INTO Request(user,friend_username,status)
                            VALUES(?,?,?)''', (user, userName, str(request)))
            print("The request has been sent.")
            conn.commit()
            return "sent"
            display_return_message()
    if not found_student:
        print("Invalid input. Please try again")
        display_return_message()
    cur.close()
    conn.close()


# Uyen, Epic #5
# This function is used to generate pending request
def generate_pending_request(username=user):
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    status = 'Pending'
    cur.execute("SELECT * FROM Request WHERE  user = ? and status = ?", (user, status))
    rows = cur.fetchall()
    cur.close()
    conn.close()

    if not rows:
        print("No pending request")
        selection = input("Enter 0 to return to previous page: ")
        if selection == "0":
            stack.pop()()
    else:
        print("These are all pending requests: ")
        for student in rows:
            print(student[0])


# Uyen, Epic #5
# This function is used to search for students by their last name
def search_by_last(last):
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE last_name = ?", (last,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    if not rows:
        print("No found result")
        return False
    else:
        print("This is the search result: ")
        for student in rows:
            print(student[0] + " " + student[1] + " (" + student[2] + ")")
    return True


# Uyen, Epic #5
# This function is used to search for students by their university
def search_by_uni(uni):
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM profile WHERE university = ?", (uni,))
    rows = cur.fetchall()

    if not rows:
        print("No result")
        return False
    else:
        print("This is the search result: ")
        for item in rows:
            user = item[4]
            users_table = cur.execute("SELECT * FROM users WHERE user_name = ?", (user,)).fetchall()
            for student in users_table:
                print(student[0] + " " + student[1] + " (" + student[2] + ")")
            conn.commit()
            cur.close()
            conn.close()
        return "Found"


# Uyen, Epic #5
# This function is used to search for students by their major
def search_by_major(maj):
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM profile WHERE major = ?", (maj,))
    rows = cur.fetchall()

    if not rows:
        print("No result")
        return False
    else:
        print("This is the search result: ")
        for item in rows:
            user = item[4]
            users_table = cur.execute("SELECT * FROM users WHERE user_name = ?", (user,)).fetchall()
            for student in users_table:
                print(student[0] + " " + student[1] + " (" + student[2] + ")")
            conn.commit()
            cur.close()
            conn.close()
        return "Found"


# Uyen, Epic #5
# This function is used to search for students
def student_search():
    stack.append(student_search)
    global user
    menu_options = ["Search by last name.",
                    "Search by university.",
                    "Search by major."]
    display_menu(menu_options, False)
    selection = make_selection(len(menu_options), False)
    if selection == "0":
        stack.pop()
        stack.pop()()
    elif selection == "1":
        lastName = input("Enter the last name you want to search: ").lower()
        if search_by_last(lastName):
            send_friend_request(user)
    elif selection == "2":
        uni = input("Enter the university you want to search: ")
        if search_by_uni(uni.title()):
            send_friend_request(user)
    elif selection == "3":
        major = input("Enter the major you want to search: ")
        if search_by_major(major.title()):
            send_friend_request(user)


# Aliaksandra, epic #5
# This function gives an option to accept or reject new friend requests
def pending_request_message():
    global user
    menu_options = ["Accept",
                    "Reject"]
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    status = 'Pending'
    cur.execute('''SELECT * FROM Request WHERE friend_username = ? and status = ?''', (user, status))
    rows = cur.fetchall()
    cur.close()
    conn.close()

    if not rows:
        return
    if rows:
        print("You have pending friend requests: ")
        for student in rows:
            print(student[0])

    display_menu(menu_options, False)
    selection = make_selection(len(menu_options), False)
    if selection == "0":
        stack.pop()
    elif selection == "1":
        friend_username = input("Enter username you want to accept as a friend: ")
        add_friend(friend_username, username=user)
        delete_pending_request(friend_username, username=user)

    elif selection == "2":
        friend_username = input("Enter username you want to reject as a friend: ")
        delete_pending_request(friend_username, username=user)
        print("You rejected a friend request from " + friend_username)


# Michael, epic #6
def print_job(job):
    # given a job as a parameter, prints the details of a job
    print("Title:" + job[0])
    print("Description:" + job[1])
    print("Employer:" + job[2])
    print("Location:" + job[3])
    print("Salary:" + job[4])


# Michael, epic #6
def apply_for_job(job):
    global user
    current_date = date.today().isoformat()
    # check if existing application already exists, if one is found, user can't apply
    # submit application to job
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    # get the job titles and
    # check the table of job applications for the user name and this specific job's title
    all_jobs = cur.execute("SELECT * FROM job_applications WHERE job_title = ?", (job[0],)).fetchall()
    found = False
    for job in all_jobs:
        if job[1] == user:
            found = True
            break
    if not found:
        conn = sqlite3.connect("inCollege.db")
        cur = conn.cursor()
        grad_date = input("Enter your expected graduation date (mm/dd/yyyy): ")
        job_start_date = input("Enter a date that you can start working (mm/dd/yyyy): ")
        reason = input("Write a paragraph  explaining why you think that you would be a good fit for this job: ")
        cur.execute(''' INSERT INTO job_applications(job_title, applicant, grad_date, job_start_date, reason, apply_day)
                        VALUES(?,?,?,?,?,?)''', (job[0], user, grad_date, job_start_date, reason, current_date))
        cur.execute(''' UPDATE users set last_day_apply_for_job = ? WHERE user_name = ? ''', (current_date, user) )
        conn.commit()
        cur.close()
        conn.close()
        print("Thank you for applying!")
        selection = input("Enter 0 to return to previous page: ")
        if selection == "0":
            stack.pop()
        # for testing if the applying for the job worked or not
        return "Applied"
    else:
        print("You've already applied to this job before!")
        return "You've already applied to this job before!"

# Sofia : Epic #8 -  fixing to fix job_menu function 
def all_jobs(requires_selection):
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    all_jobs = cur.execute("SELECT * FROM jobs").fetchall()
    jobs_applied_for = cur.execute("SELECT * FROM job_applications").fetchall()
    cur.close()
    conn.close()

    print("All posted jobs: ")
    for i in range(len(all_jobs)):
        found = False
        # try to find an application that has the current user listed on it
        for applied in jobs_applied_for:
            if applied[0] == all_jobs[i][0] and applied[1] == user:
                found = True
        # if found, print that the user has already applied for it next to the job, otherwise just print the job title
        if found:
            print(str(i+1) + ".", all_jobs[i][0], "\tApplied for already")
        else:
            print(str(i+1) + ".", all_jobs[i][0])

    # let the users select the job and prints it to the screen with the previously created print_job func.
    if requires_selection: 
        select = int(make_selection(len(all_jobs), True))
        return all_jobs[select -1]
    else: display_return_message()

# Michael, epic #6
# Aliaksandra, epic #6
# this function displays jobs menu to apply, save, delete jobs
def jobs_menu():
    stack.append(jobs_menu)
    global user

    applied_jobs_message()
    # Sofia : Epic #8
    check_job_section_message()

    menu_options = ["View all posted jobs",
                    "Display a job description",
                    "Apply for a job",
                    "Delete a job post",
                    "Save a job",
                    "Jobs you have applied for",
                    "Jobs you have not applied for",
                    "Saved jobs"]
    display_menu(menu_options, False)
    selection = make_selection(len(menu_options), False)
    if selection == "0":
        stack.pop()
        stack.pop()()
    elif selection == "1":
        all_jobs(False)
    elif selection == "2":
        # display job description
        display_job(all_jobs(True))
        
    elif selection == "3":
        # apply for a job
        apply_for_job(all_jobs(True))
        
    elif selection == "4":
        # delete a job post
        delete_job(all_jobs(True))
        
    elif selection == "5":
        # save a job post to apply later
        save_job(all_jobs(True))
        
    elif selection == "6":
        # list of jobs user applied for
        jobs_user_applied_for()
        
    elif selection == "7":
        # list of jobs not applied for
        jobs_not_applied_for()
        
    elif selection == "8":
        # list of saved jobs
        saved_jobs_list()
        


# Aliaksandra, epic #6
# this function displays list of jobs user applied for
def jobs_user_applied_for(username=user):
    global user
    applied = False
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    cur.execute('''SELECT * FROM job_applications WHERE applicant = ?''', (username,))
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    if not rows:
        print("You have not applied for any jobs yet.")
        display_return_message()
    if rows:
        print("These are the jobs you have applied for: ")
        applied = True
        for job_title in rows:
            print(job_title[0])
        display_return_message()


# Aliaksandra, epic #6
# this function displays list of jobs user hasn't applied for
def jobs_not_applied_for(username=user):
    global user
    applied = False
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    cur.execute(
        '''SELECT * FROM jobs WHERE title NOT IN (SELECT job_title FROM job_applications WHERE applicant = ?)''',
        (username,))
    rows = cur.fetchall()
    cur.close()
    conn.close()

    if not rows:
        print("There are currently no jobs to apply for.")
        display_return_message()
    if rows:
        print("These are the jobs you can apply for: ")
        applied = True
        for job_title in rows:
            print(job_title[0])
        display_return_message()


# Aliaksandra, epic #6
# this function displays a list of saved jobs
def saved_jobs_list(username=user):
    global user
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    cur.execute('''SELECT * FROM saved_jobs WHERE user = ?''', (user,))
    rows = cur.fetchall()
    cur.close()
    conn.close()

    if not rows:
        print("You do not have any jobs saved")
        display_return_message()
    if rows:
        print("These are the jobs you saved: ")
        for job in rows:
            print(job[0])
        selection = input("Do you want to delete a saved job? (Y/N) ")
        if selection.upper() == "Y":
            delete_saved_job()
        elif selection.upper() == "N":
            display_return_message()


# Aliaksandra, epic #6
# this function allows to delete the job the user saved
def delete_saved_job():
    global user
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    cur.execute('''SELECT * FROM saved_jobs WHERE user = ?''', (user,))
    rows = cur.fetchall()
    job_to_delete = input("Which job do you want to delete? ")
    cur.execute('''DELETE FROM saved_jobs where job_title = ? AND user = ?''', (job_to_delete, user))
    print("Job post has been deleted")
    conn.commit()
    cur.close()
    conn.close()


# Aliaksandra, epic #6
# this function allows to save a job to apply for later
def save_job(job, username=user):
    global user
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    cur.execute('''INSERT INTO saved_jobs(job_title, user) VALUES(?,?)''', (job[0], user))
    print("Job post has been saved")
    conn.commit()
    cur.close()
    conn.close()


# Aliaksandra, epic #6
# this function allows to delete the job the user posted
def delete_job(job, username=user):
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    posted_jobs = cur.execute('''SELECT * FROM jobs WHERE title = ? and user = ?''', (job[0], user,)).fetchall()
    found = False
    if job[5] == username:
        found = True
    if found:
        cur.execute('''DELETE FROM jobs WHERE title = ? AND user = ?''', (job[0], user))
        conn.commit()
        # Sofia : Epic #8 delete job -- send message to all applicants
        applicants = cur.execute('''SELECT applicant FROM job_applications WHERE job_title = ? ''' , (job[0],)).fetchall()
        deleted_message = "\nA job that you applied for has been deleted: " + job[0]
        for applicant in applicants:
            current_job_section_message = cur.execute("SELECT job_section_message FROM users WHERE user_name = ? " ,( [user])).fetchone()[0]
            if current_job_section_message is not None:
                to_post = current_job_section_message + deleted_message
            cur.execute("UPDATE users SET job_section_message = ? WHERE user_name = ? ", (deleted_message, applicant[0])  )
            conn.commit()
        cur.execute('''DELETE FROM job_applications WHERE job_title = ?''', (job[0],))
        conn.commit()
        cur.execute('''DELETE FROM saved_jobs WHERE job_title = ?''', (job[0],))
        print("Job post has been deleted")
        conn.commit()
        cur.close()
        conn.close()
    if not found:
        print("You cannot delete the job post you have not created")


# Aliaksandra, epic #6
# this function displays job post details
def display_job(job):
    global user
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    print_job(job)
    conn.commit()
    cur.close()
    conn.close()


# Michael : Epic #7
# modified by Sofia to split into two functions : find_message_recipient & send_message so send_message can be reused
def find_message_recipient(isPlusUser):
    # get friends of this user
    global user
    global friends

    friends_names = []
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    friend_table = cur.execute("SELECT friend_username FROM Friends WHERE user = ?", (user,)).fetchall()
    users = cur.execute("SELECT first_name, last_name, user_name FROM users").fetchall()
    # get a list of usernames from the list of tuples called users
    usernames = [item[2] for item in users]
    # this is getting the friends usernames and storing them in friends
    friends = [(item[0]) for item in friend_table]
    # close connections
    cur.close()
    conn.close()

    # if they are a plus user
    if isPlusUser:
        if len(users) > 1:
            # print available users
            print("Everyone you can send a message to:")
            for u in users:
                #  print everyone that isn't the current user
                if u[2] != user:
                    print(f"Name: {u[0]} {u[1]}")
                    print(f"Username: {u[2]}")
        else:
            print("There are no other users of inCollege to send a message to")
            return
        # send the message
        conn = sqlite3.connect("inCollege_messages.db")
        cur = conn.cursor()

        t = input("Enter the username of the person you want to send to: ")

        if t == user:
            print("You can't send a message to yourself, try sending a message to someone else.")
            return
        elif t not in usernames:
            print("User isn't in the system, can't send a message.")
            return
        send_message(t)
        # close connections
        cur.close()
        conn.close()

    else:  # if they are a standard user
        # print the users friends, their names and usernames
        print("You can send a message to any of your friends:")
        for f in friends:
            for u in users:
                if u[2] == f:
                    print(f"Name: {u[0]} {u[1]}")
                    print(f"Username: {u[2]}")
        # send the message
        conn = sqlite3.connect("inCollege_messages.db")
        cur = conn.cursor()

        t = input("Enter the username of the person you want to send to: ")

        if t == user:
            print("You can't send a message to yourself, try sending a message to someone else.\n")
        else:  # t is not the user
            if t not in friends:  # t needs to be a friend
                if t not in usernames:  # t needs to be in the list of usernames and a friend
                    print("User isn't in the system, can't send a message.")
                else:
                    print("I'm sorry, you are not friends with that person")
            else:  # otherwise t is a friend and their username is in the system, send the message
                send_message(t)

        # close connections
        cur.close()
        conn.close()


# Michael : Epic #7 -- function split by Sofia
def send_message(to_user):
    global user

    conn = sqlite3.connect("inCollege_messages.db")
    cur = conn.cursor()

    mess = input("Enter your message: ")
    cur.execute("INSERT INTO Messages(from_user, to_user, message, read) VALUES(?,?,?,0)", (user, to_user, mess))
    conn.commit()
    print(f"Message sent to {to_user}!")

    # close connections
    cur.close()
    conn.close()


# Sofia : Epic #7
def read_message(unread_messages):
    global user

    conn = sqlite3.connect("inCollege_messages.db")
    cur = conn.cursor()

    print("\nChoose new message to open")
    menu_options = [row[0] for row in unread_messages]
    display_menu(menu_options, True)
    selection = make_selection(len(menu_options), True)
    # to correspond to index in unread_messages
    selection = int(selection) - 1

    message = unread_messages[selection][1]
    from_user = unread_messages[selection][0]
    print("\nMessage from " + from_user + ":")
    print(message)
    print("\n")

    while selection != 'y' and selection != 'n':
        selection = input("Would you like to delete this message y/n ? : ")
    # delete message
    if selection == 'y':
        cur.execute("DELETE FROM Messages WHERE to_user = ? and from_user = ? and message = ? ",
                    ([user, from_user, message]))
        conn.commit()
    # mark as read and keep 
    else:
        # mark message as read
        cur.execute("UPDATE Messages SET  read = 1 WHERE to_user = ? and from_user = ? and message = ? ",
                    ([user, from_user, message]))
        conn.commit()

    print("\n")
    selection = "temp"
    while selection != 'y' and selection != 'n':
        selection = input("Would you like to respond to this message y/n ? : ")
    # send message 
    if selection == 'y':
        send_message(from_user)
    # close connections
    cur.close()
    conn.close()


# Sofia : Epic #7
def check_messages():
    global user

    conn = sqlite3.connect("inCollege_messages.db")
    cur = conn.cursor()

    read_messages = cur.execute("SELECT from_user, message FROM Messages WHERE to_user = ? and read = 1",
                                (user,)).fetchall()
    unread_messages = cur.execute("SELECT from_user, message FROM Messages WHERE to_user = ? and read = 0",
                                  (user,)).fetchall()

    if len(unread_messages) > 0:
        print("\nNew messages: \n")
        for row in unread_messages:
            print("Message from " + row[0])
    if len(read_messages) > 0:
        print("\nRead messages still in inbox")
        for row in read_messages:
            print("Message from " + row[0])

    if len(unread_messages) > 0:
        read_message(unread_messages)
        # close connections
        cur.close()
        conn.close()

    # Michael : Epic #7


def messages_menu():
    # stack.append(messages_menu)
    global user

    # check if the user is a standard user or a Plus user
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    account_type = cur.execute("SELECT account_type FROM users WHERE user_name = ?", (user,)).fetchone()[0]
    if account_type == "Plus":
        isPlusUser = True
    else:
        isPlusUser = False
    cur.close()
    conn.close()

    # display the messages menu options and select from them
    menu_options = ["Send a message",
                    "Check messages"]
    display_menu(menu_options, False)
    selection = make_selection(len(menu_options), False)
    # evaluate selection
    if selection == "0":
        stack.pop()  # remove self from stack
        stack.pop()()  # call previous function
    if selection == "1":
        find_message_recipient(isPlusUser)
    elif selection == "2":
        check_messages()


# Sofia : Epic #8
def check_login_message():
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()

    global user

    login_message = cur.execute("SELECT login_message FROM users WHERE user_name = ? " , (user,)).fetchone()[0]
    if login_message is not None:
        print(login_message)

        cur.execute("UPDATE users SET login_message = '' WHERE user_name = ? ", (user,))
        conn.commit()
    
    cur.close()
    conn.close()


# Sofia : Epic #7
def check_new_messages():
    conn = sqlite3.connect("inCollege_messages.db")
    cur = conn.cursor()

    global user

    new_messages = cur.execute("SELECT from_user, message FROM Messages WHERE to_user = ? and read = 0",
                               (user,)).fetchall()

    if len(new_messages) > 0:
        print("\nYou have " + str(len(new_messages)) + " new messages")
        open_message = input("Enter 1 to check your messages: ")
        if open_message == "1":
            check_messages()

    # close connections
    cur.close()
    conn.close()


# Kaiyuan : Epic #8
def apply_for_jobs_message():
    global user
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    past_7_day = date.today() - timedelta(days=7)

    apply_day = cur.execute("SELECT last_day_apply_for_job FROM users WHERE user_name = ?", (user,)).fetchone()[0]

    if apply_day is None:
        print(
            "Remember – you are going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")
    else:
        apply_date = datetime.strptime(apply_day, '%Y-%m-%d').date()
        if past_7_day > apply_date:
            print(
            "Remember – you are going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")

    cur.close()
    conn.close()


# Kaiyuan : Epic #8
def new_messages():
    conn = sqlite3.connect("inCollege_messages.db")
    cur = conn.cursor()
    global user
    new_messages = cur.execute("SELECT from_user, message FROM Messages WHERE to_user = ? and read = 0",
                               (user,)).fetchall()

    if len(new_messages) > 0:
        print("You have messages waiting for you")
    cur.close()
    conn.close()


# Kaiyuan : Epic #8
def create_profile_message():
    global user
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    title = cur.execute("SELECT title FROM profile WHERE user = ?", (user,)).fetchall()
    if len(title) == 0:
        print("Do not forget to create a profile")
    cur.close()
    conn.close()


# Kaiyuan : Epic #8
def applied_jobs_message():
    global user
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    apply_job = cur.execute("SELECT job_title FROM job_applications WHERE applicant = ?", (user,)).fetchall()
    apply_jobs = list(itertools.chain(*apply_job))
    print("\nYou have currently applied for " + str(len(apply_jobs)) + " jobs")
    cur.close()
    conn.close()


# Sofia : Epic #8
def check_job_section_message():
    global user
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    # check for any job section messages 
    message = cur.execute("SELECT job_section_message FROM users WHERE user_name = ?", ([user])).fetchone()
    # display message
    if message[0] is not None:
        print(str(message[0]))
        print("A new job " + str(message[0]) + " has been posted.")

    # clear message since it has been displayed to user & is no longer new
    empty = None
    cur.execute("UPDATE users SET job_section_message = ?  WHERE user_name = ? ",(empty, user))
    conn.commit()
    cur.close()
    conn.close()


# Kaiyuan : Epic #9
def business_analysis():
    stack.append(business_analysis)
    menu_options = ["How to use In College learning",
                    "Train the trainer",
                    "Gamification of learning",
                    "Not seeing what you’re looking for? Sign in to see all 7,609 results."]
    display_menu(menu_options, False)
    selection = make_selection(len(menu_options), False)
    if selection == '0':
        stack.pop()
        stack.pop()()
    elif selection == '1' or selection == '2' or selection == '3' or selection == '4':
        login_to_database()


# Kaiyuan : Epic #9
def training_and_education():
    stack.append(training_and_education)
    menu_options = ["Short-term training",
                    "Long-term training",
                    "Practice",
                    "Pay for training"]
    display_menu(menu_options, False)
    selection = make_selection(len(menu_options), False)
    if selection == '0':
        stack.pop()
        stack.pop()() # call previous function
    elif selection == '1':
        print("Under construction")
    elif selection == '2':
        print("Under construction")
    elif selection == '3':
        print("Under construction")
    elif selection == '4':
        print("Under construction")


# Kaiyuan : Epic #9
def training():
    stack.append(training)
    menu_options = ["Training and Education",
                    "IT Help Desk",
                    "Business Analysis and Strategy",
                    "Security"]
    display_menu(menu_options, False)
    selection = make_selection(len(menu_options), False)
    if selection == '0':
        stack.pop()
        stack.pop()()
    elif selection == '1':
        training_and_education()
    elif selection == '2' or selection == '4':
        print("Coming Soon!")
    elif selection == '3':
        business_analysis()


# Uyen: Epic #9
def learning():
    stack.append(learning)
    global user
    conn = sqlite3.connect("inCollege_messages.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM Courses WHERE user = ?", (user,))
    rows = cur.fetchall()

    print("Courses that you have taken: ")
    for i in rows:
        print("- " + i[0])

    menu_options = ["How to use In College learning",
                    "Train the trainer",
                    "Gamification of learning",
                    "Understanding the Architectural Design Process",
                    "Project Management Simplified"]
    display_menu(menu_options, False)
    selection = make_selection(len(menu_options), False)
    if selection == '0':
        stack.pop()
        stack.pop()()
    elif selection == '1':
        course_taken("How to use In College learning")
        display_return_message()
    elif selection == '2':
        course_taken("Train the trainer")
        display_return_message()
    elif selection == '3':
        course_taken("Gamification of learning")
        display_return_message()
    elif selection == '4':
        course_taken("Understanding the Architectural Design Process")
        display_return_message()
    elif selection == "5":
        course_taken("Project Management Simplified")
        display_return_message()

    conn.commit()
    cur.close()
    conn.close()

# Uyen: Epic #9
def course_taken(course_name):
    global user
    conn = sqlite3.connect("inCollege_messages.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM Courses WHERE user = ? and course = ?", (user,course_name))
    rows = cur.fetchall()
    if not rows:
        print("You have now completed this training")
        cur.execute(''' INSERT INTO Courses(course, user)
                    VALUES(?,?)''',
                    (course_name, user))
    elif rows:
        select = input("You have already taken this course, do you want to take it again? "
              "Type Y for Yes, N for No: ")
        if select == "Y":
            print("You have now completed this training")
            display_return_message()
        elif select == "N":
            print("Course Cancelled")
            display_return_message()

    conn.commit()
    cur.close()
    conn.close()

def after_logged_in_menu():
    stack.append(after_logged_in_menu)
    # print(stack)
    global user
    # Kaiyuan : Epic #8
    # check if user has new messages
    new_messages()

    # checking for new friend requests to accept/reject
    pending_request_message()
    # Sofia : Epic #7
    # check if user has new unread messages
    check_new_messages()
    # Kaiyuan : Epic #8
    # check if user has applied for a job
    apply_for_jobs_message()

    # Kaiyuan : Epic #8
    # check if user has no profile
    create_profile_message()

    # Sofia : Epic #8
    check_login_message()

    menu_options = ["Create your profile",
                    "Job menu",
                    "Find someone you know",
                    "Learn a new skill",
                    "Post a job",
                    "Useful Links",
                    "InCollege Important Links",
                    "View my profile",
                    "Show my network",
                    "Pending friend request",
                    "Messages",
                    "InCollege Learning"]
    while logged_in:
        display_menu(menu_options, False)
        selection = make_selection(len(menu_options), False)
        # evaluate selection
        if selection == "0":
            stack.pop()  # remove self from stack
            stack.pop()()  # call previous function
        elif selection == "1":
            user_profile()
            return 1
        elif selection == "2":
            jobs_menu()
            return 2
        elif selection == "3":
            student_search()
            display_return_message()
            return 3
        elif selection == "4":
            learn_new_skill()
            return 4
        elif selection == "5":
            post_job(user)
            return 5
        elif selection == "6":
            useful_links()
            return 6
        elif selection == "7":
            inCollege_important_links()
            return 7
        elif selection == "8":
            display_profile(user)
            display_return_message()
            return 8
        elif selection == "9":
            display_friends()
            display_return_message()
            return 9
        elif selection == "10":
            generate_pending_request()
            display_return_message()
            return 10
        elif selection == "11":
            messages_menu()
            display_return_message()
            return 11
        elif selection == "12":
            learning()
            display_return_message()
            return 12


def inform_other_users_of_new_user(user_name, first, last):
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()

    all_users = cur.execute("SELECT user_name FROM users WHERE user_name != ? ", ([user_name]))
    for account in all_users:
        new_user_message = "\n" + first + " " + last + " has joined inCollege"
        current_message = cur.execute("SELECT login_message FROM users where user_name = ? " , ([account[0]])).fetchone()[0]
        if current_message is not None:
            new_user_message = current_message + new_user_message
        cur.execute("UPDATE users SET login_message = ? WHERE user_name = ?", (new_user_message, account[0]))
   
    conn.commit()
    cur.close()
    conn.close()


def create_user(first, last, reg_user, reg_password, account_type, billing_rate):
    # add user to database
    # connect to database
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    # create user, default values for email, sms, advertising are 1 indicating True - these options are on
    # default value for spanish is 0 indicating False, default language is english
    cur.execute(''' INSERT INTO users(first_name, last_name, user_name, password, email, sms, advertising, spanish, account_type, billing_rate)
            VALUES(?,?,?,?,?,?,?,?,?,?)''',
                (first, last, reg_user, reg_password, 1, 1, 1, 0, account_type, billing_rate))
    conn.commit()
    cur.close()
    conn.close()
    print("created user " + reg_user)
    # Sofia : Epic #8
    inform_other_users_of_new_user(reg_user, first, last)


def has_special(reg_password):
    special_chars = string.punctuation
    booleans = list(map(lambda char: char in special_chars, reg_password))
    if any(booleans):
        return True
    else:
        return False


def find_inCollege_user(first, last):
    # find accounts with the corresponding first & last names
    # connect to database
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE first_name = ? and last_name = ?", (first, last))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    if not rows:
        print("They are not yet a part of the InCollege system yet")
        selection = input("Enter 0 to return to previous page: ")
        if selection == "0":
            stack.pop()()  # call previous function
    else:
        print("They are a part of the InCollege system")
        return "Exists"


def register_user():
    registering = True
    # connect to database
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    # get all users registered already
    users_table = cur.execute("SELECT first_name, last_name, user_name, password FROM users").fetchall()
    # print(users_table)
    cur.close()
    conn.close()
    # check if adding this user would mean more than 5 users in the system
    if len(users_table) + 1 > max_number_users:
        # return "All permitted accounts have been created, please come back later"
        print("All permitted accounts have been created, please come back later")
        # if registering didn't work, take them back to the register or login screen
        stack.pop()()  # return to previous function
    # if not, get user info
    else:
        result = 0
        while registering:
            # make lower case & strip white spaces - store all user's names uniformly
            first = input("Enter first name: ").lower().strip()
            last = input("Enter last name: ").lower().strip()
            reg_user = input("Enter a username: ")

            # display the options for the account types
            print("1. Standard account")
            print("2. Plus Account")
            selection = make_selection(2, False)

            account_type = "Standard"
            billing_rate = 0.0
            # get account details for database based off of selection
            if selection == "1":
                pass
            # Login to account
            elif selection == "2":
                account_type = "Plus"
                billing_rate = 10.0

            # check if user is already is in the table or not
            if len(users_table) == 0:
                result = 0
            else:
                # check if user already exists in the users table
                for i in range(len(users_table)):
                    if users_table[i][0] == reg_user:
                        # user_name matched to one already in the table
                        result = 1
                    else:
                        # user not found
                        result = 0
            if result == 0:
                making_password = True
                print("Password must be at least 8 characters long, but no more than 12. "
                      "Must include 1 capital letter, 1 digit, and 1 non-alpha character")
                while making_password:
                    reg_password = input("Enter a password: ")
                    # check password for necessary strength requirements
                    if (8 <= len(reg_password) <= 12
                            and any(letter.isupper() for letter in reg_password)
                            and any(letter.isdigit() for letter in reg_password)
                            and has_special(reg_password)):
                        create_user(first, last, reg_user, reg_password, account_type, billing_rate)
                        global logged_in
                        logged_in = True
                        global user
                        user = reg_user
                        registering = False
                        return "Registered"
                    elif len(reg_password) < 8:
                        print("Password is too short. Try again.")
                    elif len(reg_password) > 12:
                        print("Password is too long. Try again.")
                    elif not any(letter.isupper() for letter in reg_password):
                        print("Password does not contain an uppercase. Try again.")
                    elif not any(letter.isdigit() for letter in reg_password):
                        print("Password does not contain a digit. Try again.")
                    elif not has_special(reg_password):
                        print("Password does not contain a non-alpha character. Try again.")
            else:
                print("That username is already taken! Try again.")
                continue


def login_to_database():
    # find all usernames & passwords registered
    # connect to database
    conn = sqlite3.connect("inCollege.db")
    cur = conn.cursor()
    users_table = cur.execute("SELECT user_name, password FROM users").fetchall()
    cur.close()
    conn.close()
    print(users_table)
    global user
    user = login.login()
    if user is not None:
        global logged_in
        logged_in = True
        after_logged_in_menu()
    stack.pop()()


def login_or_register():
    stack.append(login_or_register)
    # select whether to register from an account or to login into inCollege
    menu_options = ["Register for an inCollege account",
                    "Login to your account",
                    "Useful Links",
                    "InCollege Important Links",
                    "Training"]#Epic 9: kaiyuan
    display_menu(menu_options, False)
    selection = make_selection(len(menu_options), False)
    # register for account
    if selection == "1":
        if register_user() == "Registered":
            after_logged_in_menu()
    # Login to account
    elif selection == "2":
        login_to_database()
    # go to useful links
    elif selection == "3":
        useful_links()
    # go to inCollege important links
    elif selection == "4":
        inCollege_important_links()
    elif selection == "0":
        stack.pop()  # remove self from stack
        stack.pop()()  # call previous function
    elif selection == '5':
        training()


def connect_with_people():
    print("Get ready to connect!")
    print("First let's gather some info. on the person you are looking go")
    first = input("First name: ")
    last = input("Last name: ")
    # convert first & last to all lower case & remove white spaces for comparison
    if find_inCollege_user(first.lower().strip(), last.lower().strip()) == "Exists":
        # If a contact is found in the InCollege system, they will be asked to join InCollege and presented
        # with an option to either log in or sign up and join their friends
        print("Would you like to join inCollege and connect with " + first.capitalize() + " " + last.capitalize() + "?")
        menu_options = ["Register or login"]
        display_menu(menu_options, False)
        selection = make_selection(len(menu_options), False)
        if selection == "1":
            login_or_register()
        elif selection == "0":
            stack.pop()()  # call previous function


def in_college_video():
    stack.append(in_college_video)
    print("Video is now playing")
    go_home = input("Enter 0 to return to the previous page: ")
    if go_home == "0":
        stack.pop()  # remove inCollegeVideo
        stack.pop()()  # go to previous page


def home_screen():
    stack.append(home_screen)
    # show success story on home page front
    print(
        "My college success story began in my Senior year when I took Dr. Andersen's Software Engineering Class. \n"
        "I learned the vast intricacies of Python, Jira, Agile, and Git: the foundational elements of what it is \n"
        "needed to become a computer science professional. This class allowed me to market myself in ways UCF grads \n"
        "could only dream of. Now I'm on InCollege to explain how I did it!")
    # select whether to register from an account or to login into inCollege
    menu_options = ["Start InCollege Video",
                    "Connect with people",
                    "Login or register",
                    "Useful Links",
                    "InCollege Important Links"]
    display_menu(menu_options, True)
    selection = make_selection(len(menu_options), True)
    # evaluate selection
    # go to college video
    if selection == "1":
        in_college_video()
        return "1"
    # connect with other people based on first and last name
    elif selection == "2":
        connect_with_people()
        return "2"
    # go to the login or register menu
    elif selection == "3":
        login_or_register()
        return "3"
    # go to useful links
    elif selection == "4":
        useful_links()
        return "4"
    # go to inCollege important links
    elif selection == "5":
        inCollege_important_links()
        return "5"


# Start of program
def main():
    global logged_in
    logged_in = False
    home_screen()


if __name__ == "__main__":
    main()
