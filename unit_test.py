from pytest_mock import mocker

import chall9
import pytest
import sqlite3
import builtins
import login
import mock
import itertools
from unittest.mock import patch

##################################################
# connect to the database 'inCollege.db'
conn = sqlite3.connect('inCollege.db')
c = conn.cursor()

con = sqlite3.connect('inCollege_messages.db')
cur = con.cursor()

users_table = c.execute("SELECT first_name, last_name, user_name, password FROM users").fetchall()
print(users_table)

jobs_table = c.execute("SELECT title,description,employer,location,salary,user FROM jobs").fetchall()
print(jobs_table)

messages_table = cur.execute("SELECT from_user,to_user,message,read FROM Messages").fetchall()

# clean the database
c.execute("DELETE FROM users")
c.execute("DELETE FROM jobs")
c.execute("DELETE FROM profile")
c.execute("DELETE FROM edu")
c.execute("DELETE FROM exp")
c.execute("DELETE FROM Friends")
c.execute("DELETE FROM Request")
c.execute("DELETE FROM job_applications")
c.execute("DELETE FROM saved_jobs")
cur.execute("DELETE FROM Messages")
cur.execute("DELETE FROM Courses")

conn.commit()
con.commit()
# display the database after deleting
users_table = c.execute("SELECT first_name, last_name, user_name, password FROM users").fetchall()
print(users_table)

all_jobs = c.execute("SELECT title, description, employer, location, salary FROM jobs").fetchall()

input_values = []  # declare a global variable of a list for input
print_values = []


##################################################
# functions below are used to enter inputs for the

def mock_input(s):
    print_values.append(s)
    return input_values.pop(0)


def mock_input_output_start():
    global input_values, print_values

    input_values = []
    print_values = []

    builtins.input = mock_input
    builtins.print = lambda s: print_values.append(s)


def set_keyboard_input(mocked_inputs):
    global input_values

    mock_input_output_start()
    input_values = mocked_inputs


def get_display_output():
    global print_values
    return print_values


def clear_display_output():
    global print_values
    print_values = []


######################################################
# These below functions are used for testing


# Test for job created and added to the data base
def test_create_user2():  # this function is used to test create_user function
    chall9.create_user('Kate', 'Wood', 'kate', '7896.Loki', 'Standard', '0.0')
    que = c.execute("SELECT * FROM users WHERE first_name == 'Kate'")
    rs = que.fetchall()
    print(rs)
    assert len(rs) == 1
    assert rs == [('Kate', 'Wood', 'kate', '7896.Loki', 1, 1, 1, 0, 'Standard', 0.0, None, None, None)]


def test_find_inCollege_user():  # this function is used to test the 5 limit for creating account
    set_keyboard_input(['Carlos', 'Smith', '0'])  # call function, get return value
    chall9.stack.append(chall9.home_screen)
    chall9.find_inCollege_user('Carlos', 'Smith')
    output = get_display_output()
    assert output == ["They are not yet a part of the InCollege system yet",
                      "Enter 0 to return to previous page: "]

    set_keyboard_input(['Kate', 'Wood', '0'])
    chall9.find_inCollege_user('Kate', 'Wood')
    output = get_display_output()
    assert output == ["They are a part of the InCollege system"]


def test_create_job1():
    set_keyboard_input(['Software developer', 'Researching, designing, implementing and managing software programs',
                        'ABC Inc.', 'Tampa', '$20/hour'])
    chall9.create_job('kate')
    que = c.execute("SELECT * FROM jobs WHERE title == 'Software developer'")
    rs = que.fetchall()
    assert len(rs) == 1
    print(rs)
    assert rs == [('Software developer', 'Researching, designing, implementing and managing software programs',
                   'ABC Inc.', 'Tampa', '$20/hour', 'kate')]


# Test for job created and added to the data base
def test_create_job2():
    set_keyboard_input(['Software tester',
                        'Perform automated and manual tests to ensure the software created by developers is fit for purpose',
                        'DEF Inc.', 'New York', '$15/hour'])
    chall9.create_job('john')
    que = c.execute("SELECT * FROM jobs WHERE title == 'Software tester'")
    rs = que.fetchall()
    assert len(rs) == 1
    print(rs)
    assert rs == [('Software tester',
                   'Perform automated and manual tests to ensure the software created by developers is fit for purpose',
                   'DEF Inc.', 'New York', '$15/hour', 'john')]


# Test for job post
def test_post_job():
    chall9.user = 'kate'
    job = ['Web developer', "Code, design and layout of a website according to a company's specifications",
           'GHI Inc.', 'Atlanta', '$21/hour']
    # create a job
    set_keyboard_input(job)
    chall9.create_job(chall9.user)
    que = c.execute("SELECT * FROM jobs WHERE title == 'Web developer'")
    rs = que.fetchall()
    print(rs)
    assert rs == [('Web developer', "Code, design and layout of a website according to a company's specifications",
                   'GHI Inc.', 'Atlanta', '$21/hour', 'kate')]


# Test for the limitation on the number of jobs to be posted
def test_job_limit():
    set_keyboard_input(
        ['Graphic design', "Create visual communications to convey messages in an effective and aesthetically "
                           "pleasing manner", 'JKL Inc.', 'Boston', '$17/hour', 'brian'])
    chall9.create_job("Brian")

    set_keyboard_input(
        ['Graphic design', "Create visual communications to convey messages in an effective and aesthetically "
                           "pleasing manner", 'JKL Inc.', 'Boston', '$17/hour', 'brian'])
    chall9.create_job("Brian")

    set_keyboard_input(
        ['Graphic design', "Create visual communications to convey messages in an effective and aesthetically "
                           "pleasing manner", 'JKL Inc.', 'Boston', '$17/hour', 'brian'])
    chall9.create_job("Brian")

    set_keyboard_input(
        ['Graphic design', "Create visual communications to convey messages in an effective and aesthetically "
                           "pleasing manner", 'JKL Inc.', 'Boston', '$17/hour', 'brian'])
    chall9.create_job("Brian")

    set_keyboard_input(['Data analyst',
                        "interprets data and turns it into information which can offer ways to improve a business, thus affecting business decisions",
                        'MNO Inc.', 'Washington DC', '$19/hour', 'anne'])
    chall9.create_job("Anne")

    set_keyboard_input(['Accounting',
                        "Work with data",
                        'GDF Inc.', 'Ohio', '$15/hour', 'anne'])
    chall9.create_job("Anne")

    set_keyboard_input(['Financial analyst',
                        "Collect data",
                        'HDFJ Inc.', 'Tampa', '$13/hour', 'anne'])
    chall9.create_job("Anne")

    set_keyboard_input(['Graphic design',
                        "Create and design",
                        'YUI Inc.', 'Texas', '$17.5/hour', 'kate'])
    chall9.create_job("kate")

    set_keyboard_input(['Doctor',
                        "Perform surgery",
                        'Hospital A', 'Orlando', '$25/hour', 'kate'])
    chall9.create_job("kate")

    set_keyboard_input(['Nurse',
                        "Assistant doctor",
                        'Hospital B', 'Atlanta', '$20/hour', 'anne'])
    chall9.create_job("Anne")

    set_keyboard_input(['Web Design', "Plan, create and code internet sites and webpages",
                        'PQR Inc.', 'Ohio', '$22/hour'])

    chall9.create_job("abc")
    output = get_display_output()
    assert output == ['All permitted jobs have been posted, please come back later']

    jobs_table = c.execute("SELECT title,description,employer,location,salary,user FROM jobs").fetchall()
    assert len(jobs_table) == 10


def test_register():
    set_keyboard_input(['james', 'kim', 'thor', '1', '2345.Thor'])
    chall9.register_user()  # call function
    que = c.execute("SELECT * FROM users WHERE first_name == 'james'")
    rs = que.fetchall()
    print(rs)
    assert rs == [('james', 'kim', 'thor', '2345.Thor', 1, 1, 1, 0, 'Standard', 0.0, None, None, None)]


def test_login():
    set_keyboard_input(['thor', '2345.Thor', '0'])
    output = login.login()
    assert output == ('thor')

    set_keyboard_input(['Thor', '123thor', '0'])
    output = login.login()
    assert output == None


def test_connect_with_people():
    set_keyboard_input(['John', 'Doe', '0'])
    output = chall9.find_inCollege_user('John', 'Doe')
    assert output == None

    set_keyboard_input(['james', 'kim', '0'])
    chall9.find_inCollege_user('james', 'kim')
    output = get_display_output()
    assert output == ['They are a part of the InCollege system']

    set_keyboard_input(['james', 'kim', '0'])
    chall9.stack.append(chall9.home_screen)
    output = get_display_output()
    assert output == []


def test_useful_links():
    # Useful Links: General, Browse InCollege, Business Solutions, and Directories.
    # sign up function test
    # test_register()

    # help center test
    chall9.stack.append(chall9.help_center)
    output = chall9.help_center()  # output on screen displayed from the selection of the help center
    assert output == "We're here to help"  # the value that should be returned from the help center selection

    # about test
    chall9.stack.append(chall9.about)
    output = chall9.about()
    assert output == "\nIn College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide"

    # press test
    chall9.stack.append(chall9.press)
    output = chall9.press()
    assert output == "\nIn College Pressroom: Stay on top of the latest news, updates, and reports"

    # blog test
    chall9.stack.append(chall9.blog)
    output = chall9.blog()
    assert output == "Under Construction\n"

    # careers test
    chall9.stack.append(chall9.careers)
    output = chall9.careers()
    assert output == "Under Construction\n"

    # developers test
    chall9.stack.append(chall9.developers)
    output = chall9.developers()
    assert output == "Under Construction\n"

    # browse in college test
    chall9.stack.append(chall9.browse_inCollege)
    output = chall9.browse_inCollege()
    assert output == "Under Construction\n"

    # business solutions test
    chall9.stack.append(chall9.business_solution)
    output = chall9.business_solution()
    assert output == "Under Construction\n"

    # directories test
    chall9.stack.append(chall9.directories)
    output = chall9.business_solution()
    assert output == "Under Construction\n"


def test_important_links():
    # display Copyright
    output = chall9.copyright_notice()
    assert output == "Copyright 2020 inCollege Inc, All rights reserved"

    # display About
    output = chall9.important_about()
    assert output == "Our site came to be when our world was widespread in the deadly virus known as Corona\n" \
                     "We wanted to create a virtual space for college students everywhere.\n" \
                     "Where they could connect & share experiences & opportunities\n"

    # display Accessibility
    output = chall9.accessibility()
    assert output == "We strive to make our simple text based interface as accessible as possible\n" \
                     "Additional font sizes coming soon!"

    # display User Agreement
    output = chall9.user_agreement()
    assert output == "As we provide this service to you, we ask that you be respectful of all other inCollege users\n" \
                     "Failure to do so can result in deletion of your posts or eventual termination of your account\n" \
                     "inCollege will treat you with the respect you deserve"

    # display Privacy Policy
    output = chall9.privacy_policy()
    assert output == "As we provide this service to you, we ask that you be respectful of all other inCollege users\n" \
                     "Failure to do so can result in deletion of your posts or eventual termination of your account\n" \
                     "inCollege will treat you with the respect you deserve"

    # display Cookie Policy
    output = chall9.cookie_policy()
    assert output == "Cookies are yummy but not the cookies we are using\nOurs identify users to recognize if you are an existing user" \
                     "\nand help provide the ability to post and eventually apply for jobs"

    # display Copyright Policy
    output = chall9.copyright_policy()
    assert output == "We respect you as an individual & your intellectual property rights\n" \
                     "We will not violate those rights\n" \
                     "We just require that what you post is accurate, lawful, and not in violation of others' rights"

    # display Brand Policy
    output = chall9.brand_policy()
    assert output == "You are allowed to use the inCollege logo to designate a link to your inCollege profile\n" \
                     "When referring to inCollege, the name should always be written as one word exactly as shown: inCollege"

    # changing Language preference
    set_keyboard_input(['2'])
    chall9.language()
    que = c.execute("SELECT * FROM users WHERE first_name == 'james'")
    rs = que.fetchall()
    assert rs == [('james', 'kim', 'thor', '2345.Thor', 1, 1, 1, 1, 'Standard', 0.0, None, None, None)]


def test_logged_in_privacy_policy():
    # turn off email for user
    chall9.stack.append(chall9.logged_in_privacy_policy)
    set_keyboard_input(['1', '1', '1', '2'])
    chall9.logged_in_privacy_policy()
    que = c.execute("SELECT * FROM users WHERE first_name == 'james'")
    rs = que.fetchall()
    print(rs)
    assert rs == [('james', 'kim', 'thor', '2345.Thor', 0, 0, 1, 1, 'Standard', 0.0, None, None, None)]


# used to mock return call
def after_logged_in_menu():
    raise Exception("Used to mock return call in chall, never actually called")


def login_or_register():
    raise Exception("Used to mock return call in chall, never actually called")


# used for mock - ends loop in chall4 of having to make selection
def display_profile():
    after_menu = after_logged_in_menu()
    return f"{after_menu} returned to after_logged_in_menu"


def test_empty_profile():
    module_that_contains_function_to_be_mocked = 'unit_test'
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        clear_display_output()
        chall9.display_profile('kate')
        output = get_display_output()
        assert output == ['Kate Wood', 'No Profile Created Yet', 'No Experiences Yet', 'No Education Listed']


# used for mock - ends loop in chall4 of having to make selection
def create_profile():
    after_menu = after_logged_in_menu()
    return f"{after_menu} returned to after_logged_in_menu"


def test_create_profile_page():
    set_keyboard_input(['usf student seeking internship', 'comp sci', 'uni of south fl', 'high gpa, hard worker', '0'])
    module_that_contains_function_to_be_mocked = 'unit_test'
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        chall9.create_profile('kate')
        que = c.execute("SELECT title,major,university,info FROM profile WHERE user == 'kate'")
        rs = que.fetchall()
        assert rs == [('usf student seeking internship', 'Comp Sci', 'Uni Of South Fl', 'high gpa, hard worker')]
        set_keyboard_input(['uva grad', 'Civil Engineer', 'University of VA', 'good math skills', '0'])
        chall9.create_profile('thor')
        que = c.execute("SELECT title,major,university,info FROM profile WHERE user == 'thor'")
        rs = que.fetchall()
        assert rs == [('uva grad', 'Civil Engineer', 'University Of Va', 'good math skills')]


# used for mock - ends loop in chall4 of having to make selection
def create_education():
    after_menu = after_logged_in_menu()
    return f"{after_menu} returned to after_logged_in_menu"


def test_create_education():
    set_keyboard_input(['USF', 'bs in cs', '2017-2020'])
    module_that_contains_function_to_be_mocked = 'unit_test'
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        chall9.create_education('kate')
        que = c.execute("SELECT schoolName,degreeEarn,yearAttend  FROM edu WHERE user == 'kate'")
        rs = que.fetchall()
        assert rs == [('Usf', 'Bs In Cs', '2017-2020')]


def test_partial_profile():
    module_that_contains_function_to_be_mocked = 'unit_test'
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        clear_display_output()
        chall9.display_profile('kate')
        output = get_display_output()
        assert output == ['Kate Wood',
                          'Profile Title: usf student seeking internship\nMajor: Comp Sci\nUniversity: Uni Of South Fl\nInfo: high gpa, hard worker',
                          'No Experiences Yet',
                          'Education', 'School Name: Usf\nDegree: Bs In Cs\nYear Attended: 2017-2020', ]


def create_experience():
    after_menu = after_logged_in_menu()
    return f"{after_menu} returned to after_logged_in_menu"


def test_create_experience1():
    set_keyboard_input(
        ['Bookkeeper', 'Person who needs books kept', '2003', '2006', 'where the books are', 'kept books'])
    module_that_contains_function_to_be_mocked = 'unit_test'
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        chall9.create_experience('kate')
        que = c.execute("SELECT title,employer,startDate,endDate,location,description  FROM exp WHERE user == 'kate'")
        rs = que.fetchall()
        assert rs == [
            ('Bookkeeper', 'Person who needs books kept', '2003', '2006', 'where the books are', 'kept books')]


# test limit of 3 job experiences allowed
def test_create_experience2():
    set_keyboard_input(['Babysitter', 'parent tired of their kid', '2006', '2007', 'where the kid is',
                        'sat kids', 'Life guard', 'the living', '2012', 'present', 'earth', 'guards lives'])
    module_that_contains_function_to_be_mocked = 'unit_test'
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        chall9.create_experience('kate')
        que = c.execute("SELECT title,employer,startDate,endDate,location,description  FROM exp WHERE user == 'kate'")
        rs = que.fetchall()
        assert rs == [
            ('Bookkeeper', 'Person who needs books kept', '2003', '2006', 'where the books are', 'kept books'),
            ('Babysitter', 'parent tired of their kid', '2006', '2007', 'where the kid is', 'sat kids')]

    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        chall9.create_experience('kate')
        que = c.execute("SELECT title,employer,startDate,endDate,location,description  FROM exp WHERE user == 'kate'")
        rs = que.fetchall()
        assert rs == [
            ('Bookkeeper', 'Person who needs books kept', '2003', '2006', 'where the books are', 'kept books'),
            ('Babysitter', 'parent tired of their kid', '2006', '2007', 'where the kid is', 'sat kids'),
            ('Life guard', 'the living', '2012', 'present', 'earth', 'guards lives')]
        clear_display_output()
        chall9.create_experience('kate')
        output = get_display_output()
        assert output == (["You can only add up to 3 past jobs."])


def test_full_profile():
    module_that_contains_function_to_be_mocked = 'unit_test'
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        clear_display_output()
        chall9.display_profile('kate')
        output = get_display_output()
        assert output == ['Kate Wood',
                          'Profile Title: usf student seeking internship\n''Major: Comp Sci\n''University: Uni Of South Fl\n''Info: high gpa, hard worker',
                          'Experience',
                          'Title: Bookkeeper\n''Employer: Person who needs books keptStart Date: 2003\n''End Date: 2006\n''Location: where the books are\n''Description: kept books',
                          'Title: Babysitter\n''Employer: parent tired of their kidStart Date: 2006\n''End Date: 2007\n''Location: where the kid is\n''Description: sat kids',
                          'Title: Life guard\n''Employer: the livingStart Date: 2012\n''End Date: present\n''Location: earth\n''Description: guards lives',
                          'Education', 'School Name: Usf\n''Degree: Bs In Cs\n''Year Attended: 2017-2020']


def student_search():
    after_menu = after_logged_in_menu()
    return f"{after_menu} returned to after_logged_in_menu"


def test_student_search(mocker):
    module_that_contains_function_to_be_mocked = 'unit_test'
    mocker.patch('chall9.display_return_message', return_value='0')
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        clear_display_output()
        user = chall9.user = 'thor'
        set_keyboard_input(['1', 'james'])
        chall9.student_search()
        output = get_display_output()
        assert output == ['\n0. To return to previous page', '1. Search by last name.', '2. Search by university.',
                          '3. Search by major.', 'Enter your selection: ', 'Enter the last name you want to search: ',
                          'No found result', ]
        clear_display_output()
        set_keyboard_input(['2', 'ucf'])
        chall9.student_search()
        output = get_display_output()
        assert output == ['\n0. To return to previous page', '1. Search by last name.', '2. Search by university.',
                          '3. Search by major.', 'Enter your selection: ', 'Enter the university you want to search: ',
                          'No result', ]
        clear_display_output()
        set_keyboard_input(['3', 'pooping'])
        chall9.student_search()
        output = get_display_output()
        assert output == ['\n0. To return to previous page', '1. Search by last name.', '2. Search by university.',
                          '3. Search by major.', 'Enter your selection: ', 'Enter the major you want to search: ',
                          'No result', ]
        clear_display_output()
        set_keyboard_input(['1', 'Wood', 'kate', '0'])
        chall9.student_search()
        output = get_display_output()
        assert output == ['\n0. To return to previous page', '1. Search by last name.', '2. Search by university.',
                          '3. Search by major.', 'Enter your selection: ', 'Enter the last name you want to search: ',
                          # 'This is the search result: ',
                          # 'Kate Wood (kate)', 'Enter the username of student you want to add friend: ',
                          # 'The request has been sent.']
                          'No found result']
        clear_display_output()
        user = chall9.user = 'kate'
        set_keyboard_input(['2', 'university of VA', 'thor'])
        chall9.student_search()
        output = get_display_output()
        assert output == ['\n0. To return to previous page', '1. Search by last name.', '2. Search by university.',
                          '3. Search by major.', 'Enter your selection: ', 'Enter the university you want to search: ',
                          'This is the search result: ',
                          'james kim (thor)', 'Enter the username of student you want to add friend: ',
                          'The request has been sent.']
        clear_display_output()
        set_keyboard_input(['3', 'civil engineer', 'thor'])
        chall9.student_search()
        output = get_display_output()
        assert output == ['\n0. To return to previous page', '1. Search by last name.', '2. Search by university.',
                          '3. Search by major.', 'Enter your selection: ', 'Enter the major you want to search: ',
                          'This is the search result: ',
                          'james kim (thor)', 'Enter the username of student you want to add friend: ',
                          'The request has been sent.']


def test_display_job():
    jobs = c.execute(
        "SELECT title, description, employer, location, salary FROM jobs WHERE title == 'Software tester'").fetchall()
    job = list(itertools.chain(*jobs))

    clear_display_output()
    chall9.display_job(job)
    output = get_display_output()
    assert output == ['Title:Software tester',
                      'Description:Perform automated and manual tests to ensure the software '
                      'created by developers is fit for purpose',
                      'Employer:DEF Inc.',
                      'Location:New York',
                      'Salary:$15/hour']


# this function uses to test the number of account limits to 10
def test_account_limit_number():
    chall9.create_user('Tony', 'Stark', 'Tony', '7896.Tony', 'Standard', '0.0')
    chall9.create_user('Nick', 'Fury', 'Nick', '7896.Nick', 'Standard', '0.0')
    chall9.create_user('Pepper', 'Potts', 'Pepper', '7896.Pepper', 'Standard', '0.0')
    chall9.create_user('Bruce', 'Banner', 'Bruce', '7896.Bruce', 'Plus', '10.0')
    chall9.create_user('Maria', 'Hill', 'Maria', '7896.Maria', 'Standard', '0.0')
    chall9.create_user('Clint', 'Barton', 'Clint', '7896.Clint', 'Plus', '10.0')
    chall9.create_user('Black', 'Widow', 'Black', '7896.Black', 'Standard', '0.0')
    chall9.create_user('Captain', 'Roger', 'Roger', '7896.Roger', 'Plus', '10.0')
    que = c.execute("SELECT * FROM users")
    rs = que.fetchall()
    print(rs)
    assert len(rs) == 10


# this function use to test the friend list
def test_friend_list():
    chall9.add_friend('Tony', 'Pepper')
    chall9.friend_list('Tony')
    assert ["My friends' usernames:Pepper"]

    chall9.friend_list('Pepper')
    assert ["My friends' usernames:Tony"]

    chall9.add_friend('Bruce', 'Black')
    chall9.add_friend('Bruce', 'Tony')
    chall9.friend_list('Bruce')
    list_friends = chall9.friends
    assert len(list_friends) == 2
    assert list_friends == ['Black', 'Tony']


# this function is used to test the display_friends()
def test_display_friends1():
    chall9.user = 'Pepper'
    chall9.friends.append('Tony')
    set_keyboard_input(['1', 'Tony'])
    # chall6.stack.append(chall6.after_logged_in_menu)
    chall9.display_friends()
    output = get_display_output()

    assert output == ["My friends' usernames:",
                      ['Tony'],
                      '\n0. To return to previous page',
                      "1. View friend's profile",
                      '2. Delete friend',
                      'Enter your selection: ',
                      "Type friend's username to view their profile: ",
                      'Tony Stark',
                      'No Profile Created Yet',
                      'No Experiences Yet',
                      'No Education Listed']


def test_display_friends2():
    chall9.friends.pop()
    chall9.user = 'Pepper'
    set_keyboard_input(['2', 'Tony'])

    chall9.display_friends()
    output = get_display_output()
    assert output == ["My friends' usernames:",
                      ['Tony'],
                      '\n0. To return to previous page',
                      "1. View friend's profile",
                      '2. Delete friend',
                      'Enter your selection: ',
                      "Type friend's username to delete: ",
                      'You and Tony are no longer friends']


def test_apply_for_job():
    module_that_contains_function_to_be_mocked = 'unit_test'
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        clear_display_output()
        user = 'kate'
        set_keyboard_input(['05/05/2021', '08/05/2021', 'I have all the skills the job needed.', '0'])
        output = chall9.apply_for_job(['Software tester'])
        # output = get_display_output()
        assert output == 'Applied'


def test_jobs_user_applied_for(mocker):
    chall9.user = 'Pepper'
    module_that_contains_function_to_be_mocked = 'unit_test'
    mocker.patch('chall9.display_return_message', return_value='0')
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        set_keyboard_input(['0'])
        chall9.jobs_user_applied_for(chall9.user)
        output = get_display_output()
        assert output == ['These are the jobs you have applied for: ', 'Software tester']


def test_jobs_not_applied_for(mocker):
    chall9.user = 'Pepper'
    module_that_contains_function_to_be_mocked = 'unit_test'
    mocker.patch('chall9.display_return_message', return_value='0')
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        set_keyboard_input(['0'])
        chall9.jobs_not_applied_for(chall9.user)
        output = get_display_output()
        assert output == ['These are the jobs you can apply for: ',
                          'Software developer',
                          'Web developer',
                          'Graphic design',
                          'Graphic design',
                          'Graphic design',
                          'Graphic design',
                          'Data analyst',
                          'Accounting',
                          'Financial analyst']


def test_save_job():
    job = ["Nurse"]
    clear_display_output()
    chall9.save_job(job, "Pepper")
    output = get_display_output()
    assert output == ["Job post has been saved"]

    clear_display_output()
    chall9.saved_jobs_list("Pepper")
    output = get_display_output()
    assert output == ['These are the jobs you saved: ', 'Nurse', 'Do you want to delete a saved job? (Y/N) ']


def test_delete_saved_job():
    chall9.user = 'Pepper'
    clear_display_output()
    set_keyboard_input(["Nurse"])
    chall9.delete_saved_job()
    output = get_display_output()
    assert output == ['Which job do you want to delete? ', 'Job post has been deleted']


def test_applied_jobs_message():
    clear_display_output()
    chall9.user = 'Pepper'
    chall9.applied_jobs_message()
    output = get_display_output()
    assert output == ['\nYou have currently applied for 1 jobs']


def test_delete_job(mocker):
    module_that_contains_function_to_be_mocked = 'unit_test'
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        clear_display_output()
        user = 'john'
        chall9.delete_job(["Software tester", "", "", "", "", user], user)
        output = get_display_output()
        assert output == ['Job post has been deleted']
        # assert output == ['You cannot delete the job post you have not created']


def test_send_friend_request(mocker):
    module_that_contains_function_to_be_mocked = 'unit_test'
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        user = 'kate'
        set_keyboard_input(['thor'])
        chall9.send_friend_request(username=user)
        output = chall9.stack.append(chall9.display_return_message)
        assert output is None


def test_requests_after_login():
    module_that_contains_function_to_be_mocked = 'unit_test'
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        chall9.user = 'thor'
        set_keyboard_input(['1', 'kate'])
        chall9.pending_request_message()
        output = get_display_output()
        assert output == ['You have pending friend requests: ',
                          'kate',
                          'kate',
                          'Pepper',
                          '\n0. To return to previous page',
                          '1. Accept',
                          '2. Reject',
                          'Enter your selection: ',
                          'Enter username you want to accept as a friend: ',
                          'You and kate are now friends!']
        que = c.execute("SELECT *  FROM Friends ")
        rs = que.fetchall()
        # check they are both friends with each other
        assert rs == [
            ('Black', 'Bruce'),
            ('Bruce', 'Black'),
            ('Tony', 'Bruce'),
            ('Bruce', 'Tony'),
            ('thor', 'kate'),
            ('kate', 'thor')]


def test_send_message():
    clear_display_output()
    chall9.user = 'kate'
    set_keyboard_input(["Hi, how are you?"])
    chall9.send_message('Pepper')
    output = get_display_output()
    assert output == ['Enter your message: ', 'Message sent to Pepper!']


def test_find_message_recipent():
    clear_display_output()
    chall9.user = 'kate'
    set_keyboard_input(['Pepper', 'How are you?'])
    chall9.find_message_recipient(True)
    output = get_display_output()
    assert output == ['Everyone you can send a message to:',
                      'Name: james kim',
                      'Username: thor',
                      'Name: Tony Stark',
                      'Username: Tony',
                      'Name: Nick Fury',
                      'Username: Nick',
                      'Name: Pepper Potts',
                      'Username: Pepper',
                      'Name: Bruce Banner',
                      'Username: Bruce',
                      'Name: Maria Hill',
                      'Username: Maria',
                      'Name: Clint Barton',
                      'Username: Clint',
                      'Name: Black Widow',
                      'Username: Black',
                      'Name: Captain Roger',
                      'Username: Roger',
                      'Enter the username of the person you want to send to: ',
                      'Enter your message: ',
                      'Message sent to Pepper!']

    clear_display_output()
    chall9.user = 'kate'
    set_keyboard_input(['kate', 'How are you?'])
    chall9.find_message_recipient(True)
    output = get_display_output()
    assert output == ['Everyone you can send a message to:',
                      'Name: james kim',
                      'Username: thor',
                      'Name: Tony Stark',
                      'Username: Tony',
                      'Name: Nick Fury',
                      'Username: Nick',
                      'Name: Pepper Potts',
                      'Username: Pepper',
                      'Name: Bruce Banner',
                      'Username: Bruce',
                      'Name: Maria Hill',
                      'Username: Maria',
                      'Name: Clint Barton',
                      'Username: Clint',
                      'Name: Black Widow',
                      'Username: Black',
                      'Name: Captain Roger',
                      'Username: Roger',
                      'Enter the username of the person you want to send to: ',
                      "You can't send a message to yourself, try sending a message to someone else."]

    clear_display_output()
    chall9.user = 'kate'
    set_keyboard_input(['uyen', 'How are you?'])
    chall9.find_message_recipient(True)
    output = get_display_output()
    assert output == ['Everyone you can send a message to:',
                      'Name: james kim',
                      'Username: thor',
                      'Name: Tony Stark',
                      'Username: Tony',
                      'Name: Nick Fury',
                      'Username: Nick',
                      'Name: Pepper Potts',
                      'Username: Pepper',
                      'Name: Bruce Banner',
                      'Username: Bruce',
                      'Name: Maria Hill',
                      'Username: Maria',
                      'Name: Clint Barton',
                      'Username: Clint',
                      'Name: Black Widow',
                      'Username: Black',
                      'Name: Captain Roger',
                      'Username: Roger',
                      'Enter the username of the person you want to send to: ',
                      "User isn't in the system, can't send a message."]

    clear_display_output()
    chall9.user = 'kate'
    set_keyboard_input(['Pepper', 'How are you?'])
    chall9.find_message_recipient(False)
    output = get_display_output()
    assert output == ['You can send a message to any of your friends:',
                      'Name: james kim',
                      'Username: thor',
                      'Enter the username of the person you want to send to: ',
                      "I'm sorry, you are not friends with that person"]

    clear_display_output()
    chall9.user = 'Tony'
    set_keyboard_input(['Bruce', 'How are you?'])
    chall9.find_message_recipient(False)
    output = get_display_output()
    assert output == ['You can send a message to any of your friends:',
                      'Name: Bruce Banner',
                      'Username: Bruce',
                      'Enter the username of the person you want to send to: ',
                      'Enter your message: ',
                      'Message sent to Bruce!']


def test_read_message(mocker):
    module_that_contains_function_to_be_mocked = 'unit_test'
    mocker.patch('chall9.display_return_message', return_value='0')
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        user = 'Pepper'
        unread_messages = cur.execute("SELECT from_user, message FROM Messages WHERE to_user = ? and read = 0",
                                      (user,)).fetchall()

        set_keyboard_input(['1', '1', 'n', 'n'])
        chall9.read_message(unread_messages)
        output = get_display_output()
        assert output == ['\nChoose new message to open',
                          '1. kate',
                          '2. kate',
                          'Enter your selection: ',
                          '\nMessage from kate:',
                          'Hi, how are you?',
                          '\n',
                          'Would you like to delete this message y/n ? : ',
                          'Would you like to delete this message y/n ? : ',
                          '\n',
                          'Would you like to respond to this message y/n ? : ']


def test_check_messages():
    clear_display_output()
    chall9.user = 'Pepper'
    set_keyboard_input(['2', '1', 'n', 'n'])
    chall9.check_messages()
    output = get_display_output()
    assert output == ['\nNew messages: \n',
                      'Message from kate',
                      'Message from kate',
                      '\nChoose new message to open',
                      '1. kate',
                      '2. kate',
                      'Enter your selection: ',
                      '\nMessage from kate:',
                      'How are you?',
                      '\n',
                      'Would you like to delete this message y/n ? : ',
                      'Would you like to delete this message y/n ? : ',
                      '\n',
                      'Would you like to respond to this message y/n ? : ']


def test_check_new_messages():
    clear_display_output()
    chall9.user = 'Pepper'
    set_keyboard_input(['1', '1', 'n', 'n'])
    chall9.check_new_messages()
    output = get_display_output()
    assert output == ['\nYou have 1 new messages',
                      'Enter 1 to check your messages: ',
                      '\nNew messages: \n',
                      'Message from kate',
                      '\nRead messages still in inbox',
                      'Message from kate',
                      '\nChoose new message to open',
                      '1. kate',
                      'Enter your selection: ',
                      '\nMessage from kate:',
                      'Hi, how are you?',
                      '\n',
                      'Would you like to delete this message y/n ? : ',
                      '\n',
                      'Would you like to respond to this message y/n ? : ']


def test_check_login_message():
    clear_display_output()
    chall9.user = 'kate'
    chall9.check_login_message()
    output = chall9.stack.append(chall9.display_return_message)
    assert output is None


def test_apply_for_jobs_message():
    clear_display_output()
    chall9.user = 'Clint'
    chall9.apply_for_jobs_message()
    output = get_display_output()
    assert output == ['Remember – you are going to want to have a job when you graduate. ' +
                      'Make sure that you start to apply for jobs today!']


def test_new_messages():
    clear_display_output()
    chall9.user = 'kate'
    set_keyboard_input(["Hi, how are you?"])
    chall9.send_message('Pepper')

    clear_display_output()
    chall9.user = 'Pepper'
    chall9.new_messages()
    output = get_display_output()
    assert output == ['You have messages waiting for you']


def test_create_profile_message():
    clear_display_output()
    chall9.user = 'Maria'
    chall9.create_profile_message()
    output = get_display_output()
    assert output == ['Do not forget to create a profile']


def test_inform_other_users_of_new_user(mocker):
    module_that_contains_function_to_be_mocked = 'unit_test'
    mocker.patch('chall9.display_return_message', return_value='0')
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        clear_display_output()
        chall9.create_user('Don', 'Potts', 'Pepper', '7896.Pepper', 'Standard', '0.0')

        clear_display_output()
        que = c.execute("SELECT login_message FROM users WHERE user_name == 'kate'")
        rs = que.fetchall()
        assert len(rs) == 1
        print(rs)
        assert rs == [('\n' + 'Don' + ' ' + 'Potts' + ' has joined inCollege',)]


def test_check_job_section_message():
    set_keyboard_input(['Financial analyst',
                        "Collect data",
                        'HDFJ Inc.', 'Tampa', '$13/hour', 'anne'])
    chall9.create_job("Anne")

    clear_display_output()
    chall9.user = 'kate'
    chall9.check_job_section_message()
    output = get_display_output()
    assert output == ['Financial analyst', 'A new job ' + 'Financial analyst' + ' has been posted.']


def test_delete_job_message(mocker):
    module_that_contains_function_to_be_mocked = 'unit_test'
    mocker.patch('chall9.display_return_message', return_value='0')
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        clear_display_output()
        user = 'john'
        chall9.delete_job('Software tester', user)

        clear_display_output()
        que = c.execute("SELECT job_section_message FROM users WHERE user_name = 'Pepper'")
        rs = que.fetchone()
        # assert len(rs) == 2
        # print(rs)
        assert rs == ('\nA job that you applied for has been deleted: Software tester',)


def learning():
    after_menu = after_logged_in_menu()
    return f"{after_menu} returned to after_logged_in_menu"


# test inCollege Learning page has correct options
def test_InCollegeLearning(mocker):
    module_that_contains_function_to_be_mocked = 'unit_test'
    mocker.patch('chall9.make_selection', return_value=0)
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        clear_display_output()
        chall9.learning()
        output = get_display_output()
        assert output == ['Courses that you have taken: ',
                          '\n0. To return to previous page',
                          '1. How to use In College learning',
                          '2. Train the trainer',
                          '3. Gamification of learning',
                          '4. Understanding the Architectural Design Process',
                          '5. Project Management Simplified']

    # test notification of completion of learning


def test_course_completion_messages(mocker):
    chall9.user = "Bruce"
    module_that_contains_function_to_be_mocked = 'unit_test'
    mocker.patch('chall9.display_return_message', return_value='0')
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        clear_display_output()
        set_keyboard_input(['1'])
        chall9.learning()
        output = get_display_output()
        assert output == ['Courses that you have taken: ',
                          '\n'
                          '0. To return to previous page',
                          '1. How to use In College learning',
                          '2. Train the trainer',
                          '3. Gamification of learning',
                          '4. Understanding the Architectural Design Process',
                          '5. Project Management Simplified',
                          'Enter your selection: ',
                          "You have now completed this training"]


# test course indicates completion
def test_indication_of_completion(mocker):
    chall9.user = "Bruce"
    module_that_contains_function_to_be_mocked = 'unit_test'
    mocker.patch('chall9.make_selection', return_value=0)
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        clear_display_output()
        chall9.learning()
        output = get_display_output()
        assert output == ['Courses that you have taken: ',
                          '- How to use In College learning',
                          '\n0. To return to previous page',
                          '1. How to use In College learning',
                          '2. Train the trainer',
                          '3. Gamification of learning',
                          '4. Understanding the Architectural Design Process',
                          '5. Project Management Simplified']

    # test retake functionality


def test_retake_course(mocker):
    chall9.user = "Bruce"
    module_that_contains_function_to_be_mocked = 'unit_test'
    mocker.patch('chall9.display_return_message', return_value='0')
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        clear_display_output()
        set_keyboard_input(['1', 'Y'])
        chall9.learning()
        output = get_display_output()
        assert output == ['Courses that you have taken: ',
                          '- How to use In College learning',
                          '\n'
                          '0. To return to previous page',
                          '1. How to use In College learning',
                          '2. Train the trainer',
                          '3. Gamification of learning',
                          '4. Understanding the Architectural Design Process',
                          '5. Project Management Simplified',
                          'Enter your selection: ',
                          "You have already taken this course, do you want to take it again? Type Y for Yes, N for No: ",
                          "You have now completed this training"]


# test retake functionality
def test_course_cancellation(mocker):
    chall9.user = "Bruce"
    module_that_contains_function_to_be_mocked = 'unit_test'
    mocker.patch('chall9.display_return_message', return_value='0')
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        clear_display_output()
        set_keyboard_input(['1', 'N'])
        chall9.learning()
        output = get_display_output()
        assert output == ['Courses that you have taken: ',
                          '- How to use In College learning',
                          '\n'
                          '0. To return to previous page',
                          '1. How to use In College learning',
                          '2. Train the trainer',
                          '3. Gamification of learning',
                          '4. Understanding the Architectural Design Process',
                          '5. Project Management Simplified',
                          'Enter your selection: ',
                          "You have already taken this course, do you want to take it again? Type Y for Yes, N for No: ",
                          "Course Cancelled"]


# Sofia and Michael Epic #9
def test_training_option_menu(mocker):
    clear_display_output()
    module_that_contains_function_to_be_mocked = 'unit_test'
    mocker.patch('chall9.training_and_education', return_value='0')
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        clear_display_output()
        set_keyboard_input(['5','1'])
        chall9.login_or_register()
        output = get_display_output()
        # also shows the options for if you selected the training and education option to show its options too
        assert output == ['\n0. To return to previous page', '1. Register for an inCollege account',
                          '2. Login to your account', '3. Useful Links', '4. InCollege Important Links',
                          '5. Training','Enter your selection: ','\n0. To return to previous page',
                          '1. Training and Education','2. IT Help Desk', '3. Business Analysis and Strategy',
                          '4. Security', 'Enter your selection: ']


# Michael Epic #9
def test_submenus_tu_it_sec(mocker):
    clear_display_output()
    module_that_contains_function_to_be_mocked = 'unit_test'
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        # check their menu options results for the under construction output
        # all 4 go to the same place so only need to check for one
        clear_display_output()
        set_keyboard_input(['1', '1'])
        chall9.training()
        output = get_display_output()
        assert output == ['\n0. To return to previous page',
                          '1. Training and Education',
                          '2. IT Help Desk',
                          '3. Business Analysis and Strategy',
                          '4. Security', 'Enter your selection: ',
                          '\n0. To return to previous page',
                          '1. Short-term training',
                          '2. Long-term training',
                          '3. Practice',
                          '4. Pay for training',
                          'Enter your selection: ',
                          'Under construction']

        # check it help desk and security both redirect to coming soon, only have to test one
        clear_display_output()
        set_keyboard_input(['2'])
        chall9.training()
        output = get_display_output()
        assert output == ['\n0. To return to previous page',
                          '1. Training and Education',
                          '2. IT Help Desk',
                          '3. Business Analysis and Strategy',
                          '4. Security',
                          'Enter your selection: ',
                          'Coming Soon!']


# Michael Epic #9
def test_business_analysis_and_strategy_1(mocker):
    clear_display_output()
    module_that_contains_function_to_be_mocked = 'unit_test'
    mocker.patch('chall9.login_to_database', return_value='0')
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        clear_display_output()
        set_keyboard_input(['3', '1'])
        chall9.training()
        output = get_display_output()
        # test for the options appearing correctly
        assert output == ['\n0. To return to previous page',
                          '1. Training and Education',
                          '2. IT Help Desk',
                          '3. Business Analysis and Strategy',
                          '4. Security',
                          'Enter your selection: ',
                          '\n0. To return to previous page',
                          '1. How to use In College learning',
                          '2. Train the trainer',
                          '3. Gamification of learning',
                          '4. Not seeing what you’re looking for? Sign in to see all 7,609 results.',
                          'Enter your selection: ']



# Michael Epic #9
def test_business_analysis_and_strategy_2(mocker):
    conn.close()
    clear_display_output()
    module_that_contains_function_to_be_mocked = 'unit_test'
    mocker.patch('chall9.jobs_menu', return_value='0')
    mock_target = f"{module_that_contains_function_to_be_mocked}.after_logged_in_menu"
    with mock.patch(mock_target, return_value="pretend after_logged_in"):
        # all 4 of these options route to the same place so only have to check 1
        clear_display_output()
        set_keyboard_input(['3', '1', 'kate', '7896.Loki', '2', '2'])
        chall9.training()
        output = get_display_output()

        # output should be sign-in page
        assert output == ['\n0. To return to previous page',
                          '1. Training and Education',
                          '2. IT Help Desk',
                          '3. Business Analysis and Strategy',
                          '4. Security',
                          'Enter your selection: ',
                          '\n0. To return to previous page',
                          '1. How to use In College learning',
                          '2. Train the trainer',
                          '3. Gamification of learning',
                          '4. Not seeing what you’re looking for? Sign in to see all 7,609 results.',
                          'Enter your selection: ',
                          [('kate', '7896.Loki'),
                           ('thor', '2345.Thor'),
                           ('Tony', '7896.Tony'),
                           ('Nick', '7896.Nick'),
                           ('Pepper', '7896.Pepper'),
                           ('Bruce', '7896.Bruce'),
                           ('Maria', '7896.Maria'),
                           ('Clint', '7896.Clint'),
                           ('Black', '7896.Black'),
                           ('Roger', '7896.Roger'),
                           ('Pepper', '7896.Pepper')],
                          'Enter your user name: ',
                          'Input your password: ',
                          'You have successfully logged in!',
                          'Remember – you are going to want to have a job when you graduate. Make sure '
                          'that you start to apply for jobs today!',
                          '\nDon Potts has joined inCollege',
                          '\n0. To return to previous page',
                          '1. Create your profile',
                          '2. Job menu',
                          '3. Find someone you know',
                          '4. Learn a new skill',
                          '5. Post a job',
                          '6. Useful Links',
                          '7. InCollege Important Links',
                          '8. View my profile',
                          '9. Show my network',
                          '10. Pending friend request',
                          '11. Messages',
                          '12. InCollege Learning',
                          'Enter your selection: ',
                          'Remember – you are going to want to have a job when you graduate. Make sure '
                          'that you start to apply for jobs today!',
                          '',
                          '\n0. To return to previous page',
                          '1. Create your profile',
                          '2. Job menu',
                          '3. Find someone you know',
                          '4. Learn a new skill',
                          '5. Post a job',
                          '6. Useful Links',
                          '7. InCollege Important Links',
                          '8. View my profile',
                          '9. Show my network',
                          '10. Pending friend request', '11. Messages',
                          '12. InCollege Learning',
                          'Enter your selection: ']
