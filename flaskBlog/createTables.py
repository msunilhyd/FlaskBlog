
  q = (db.session.query(Test, UserTest)
    .filter(Test.id == UserTest.test_id)
    .filter(UserTest.user_id == user_id)
    .all())
  print('printing the left join of test and user_test')
  print(q)
  print('len of q is : ')
  print(len(q))
  tests = Test.query.order_by(Test.date_posted.desc())
  print('len of tests is : ')
  print(tests.count())

  print('type of q is : ')
  print(type(q))
  
  print('type of tests is : ')
  print(type(tests))

  for test in tests:
    print('Hey')
    print(test)

  for test in q:
    print('Hello')
    print(test)

  q = (db.session.query(Test.id, UserTest.test_id)
    .outerjoin(UserTest, Test.id == UserTest.test_id)
    .filter(UserTest.user_id == user_id))


  for test in q:
    print('Ayyo Rama')
    print(test)

  cur = mysql.connect().cursor()
  cur.execute('''select test.id, user_test.user_id, user_test.test_id, user_test.user_score from test left join user_test on test.id = user_test.test_id and user_test.user_id=1;
''')
  rv = cur.fetchall()
  for emp in rv:
    for test in tests:
      if test.id == emp[2]:
        print('Chekkey')
        print(emp[0])
        print(emp[1])
        print(emp[2])
        print(emp[3])
        test.user_score = emp[3]
      else:
        test.user_score = None
      print(test.user_score)

  for test in tests:
    if test.user_score is not None:


Steps for deployment to Linode :

ssh root@139.162.34.166 


instructions for a test:

1. Click on the radio button out of the 4 options to answer a question.
2. To de-select an answer, click on the answered radio button.
3. You will see 'Reached the end of the test', after the last question of the test.
4.Time is indication in the top right corner for the test.
5.Test will auto submit once, time is up.
6.All the Best.



update test set instructions = '1. Click on the radio button out of the 4 options to answer a question. <br />2. To de-select an answer, click on the answered radio button.<br /> 3. You will see ''Reached the end of the test'', after the last question of the test.</br> 4.Time is indication in the top right corner for the test.</br> 5.Test will auto submit once, time is up. 6.All the Best.' where id = 9;


update test set instructions = '1. Click on the radio button out of the 4 options to answer a question. 2. To de-select an answer, click on the answered radio button. 3. You will see ''Reached the end of the test'', after the last question of the test. 4.Time is indication in the top right corner for the test. 5.Test will auto submit once, time is up. 6.All the Best.' where id = 9;

    CREATE TABLE user
(
  userid int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(20) NOT NULL,
  email VARCHAR(40) NOT NULL UNIQUE,
  image_file VARCHAR(20) NOT NULL DEFAULT 'default.jpg',
  password VARCHAR(60) NOT NULL 
);


GRANT ALL PRIVILEGES ON kumardb.* TO 'kumaruser'@'localhost';


    CREATE TABLE friends
(
  friendId int(7) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  friendName VARCHAR(20) NOT NULL
);



    insert into friends(friendName) values('Yavvan');
    insert into friends(friendName) values('Jujju');


    CREATE TABLE questions
(
  questionid int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  question VARCHAR(300) NOT NULL,
  a VARCHAR(100) NOT NULL,
  b VARCHAR(100) NOT NULL,
  c VARCHAR(100) NOT NULL,
  d VARCHAR(100) NOT NULL, 
  ans  VARCHAR(20) NOT NULL
);

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

if you get this erro :  
  ERROR [alembic.env] Target database is not up to date.

  run:
  python manage.py db stamp heads



update user set is_admin = 1 where username = 'msunilhyd';

update user set is_admin = 1 where username = 'bob';



ALTER TABLE user ADD COLUMN is_admin INT DEFAULT 0;


ALTER TABLE test
MODIFY COLUMN test_name varchar(100);

ALTER TABLE test
MODIFY COLUMN category varchar(100);


ALTER TABLE user
MODIFY COLUMN username varchar(100);

ALTER TABLE user
MODIFY COLUMN email varchar(100);

ALTER TABLE user
MODIFY COLUMN password varchar(100);





ALTER TABLE questions MODIFY COLUMN question VARCHAR(1000);


    insert into questions(question,a,b,c,d,ans)
     values('question : Who is the king of the jungle', 'a:lion', 'b:sunil','c:tiger','d:deer', 'correctAnswer : a');
    insert into questions(question,a,b,c,d,ans)
     values('question : Which is the most populous city in the world',
      'a:Delhi', 'b:Tokyo','c:Mumbai','d:Hyderabad', 'correctAnswer : b');


    insert into questions(question,a,b,c,d,ans)
     values('Who is the king of the jungle', 'lion', 'sunil','tiger','deer', 'a');
    insert into questions(question,a,b,c,d,ans)
     values('Which is the most populous city in the world',
      'Delhi', 'Tokyo','Mumbai','Hyderabad', 'b');


    insert into questions(question,a,b,c,d,ans)
     values('Who is the Coolest Front end Developer', 'Sunil', 'Zakir','Ravi','Me', 'Zakir');

     insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'Sudheer');

          insert into questions(question,a,b,c,d,ans)
     values('My name is ?', 'Linus', 'Sunil','Yashkp','Sudheer', 'Linus');


          insert into questions(question,a,b,c,d,ans)
     values('Collest HeadPhone', 'AlTech Lansing', 'Sony','Apple','Bose', 'Sony');

          insert into questions(question,a,b,c,d,ans)
     values('Greatest Investors', 'Bill Gates', 'Accel Partners','Yahoo','Warren Buffet', 'Warren Buffet');

          insert into questions(question,a,b,c,d,ans)
     values('Best programmer you have ever met', 'Varsh', 'Ranga','Tomar','Azhar', 'Tomar');

          insert into questions(question,a,b,c,d,ans)
     values('Who is the Greatest Leader in the world', 'Matrin Luther Jr', 'Dr. B.R.Ambedkar',
      'Nelson Mandela','KCR', 'Dr. B.R.Ambedkar');

          insert into questions(question,a,b,c,d,ans)
     values('Coolest Music Director', 'Harris Jayaraj', 'Anirudh','A.R.Rahman','Deva', 'Anirudh');

        200 line question  insert into questions(question,a,b,c,d,ans)
     values('And there were people who talk of Philosophyforgetting the main thing, that the practice is more important than the talking, and they never realise that the hypocrisy is the matte that makes the difference for the whole practical world of importance and nevertheless the Tigers in the dwindling population is a big concern for the animal lovers and the governments and there of for the PETA. Hail Karl Marx', 'Pilla Raa', 'Dil Bhar','Newyork Nagaram','Kothaga', 'c');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');

          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');


          insert into questions(question,a,b,c,d,ans)
     values('Best Fifa Player', 'Linus', 'Sunil','Yashkp','Sudheer', 'd');