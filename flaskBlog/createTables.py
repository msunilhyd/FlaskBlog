

Steps for deployment to Linode :

ssh root@139.162.34.166 



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