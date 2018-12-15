
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
  question VARCHAR(100) NOT NULL,
  a VARCHAR(100) NOT NULL,
  b VARCHAR(100) NOT NULL,
  c VARCHAR(100) NOT NULL,
  d VARCHAR(100) NOT NULL, 
  ans  VARCHAR(20) NOT NULL
);


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