(function() {
  var questions = [];
  
  var questionCounter = 0; //Tracks question number
  var selections = []; //Array containing user choices
  var quiz = $('#quiz'); //Quiz div object
  var isSubmit = 0;
  
  // Display initial question
  //displayNext();
  
  // Build Quiz
 // buildQuiz();
 console.log("is this the first");
 $('#next').hide();
 $('#count').hide();


  // Click handler for the 'startQuiz' button
  $('#startQuiz').on('click', function (e) {
     $('#startQuiz').hide();
    $('#submitQuiz').show();



     var t = $('#time_in_mins_div').text();
     console.log('from js time_in_mins is : ' + t);
     t = t * 60;

     var test_id = $('#test_id_div').text();
     console.log("printing test_id before ajax" + test_id);

     getQuestions(test_id);


        function secondsToTime(secs)
        {
            var hours = Math.floor(secs / (60 * 60));
           
            var divisor_for_minutes = secs % (60 * 60);
            var minutes = Math.floor(divisor_for_minutes / 60);
         
            var divisor_for_seconds = divisor_for_minutes % 60;
            var seconds = Math.ceil(divisor_for_seconds);
           
            var obj = {
                "h": hours,
                "m": minutes,
                "s": seconds
            };
            return  hours  + " hours " + minutes + " minutes " + seconds + " seconds";

        }

        console.log(secondsToTime(170 * 60))

        function timer(count,str) {
          console.log("called");
              count--;
              if(count!= 0 && count < 600){
                str = str + "<div id='remain' style='display:block'>Last 10 minutes remaining</div>."
              }
              else if(count === 0){
                clearInterval(interval);
                var scoreElem = $('<p>',{id: 'timeUp'});
                scoreElem.append('Time up. Submitting the quiz Hey');
                quiz.append(scoreElem);
                $('#submitQuiz').click();
                var x = document.getElementById('submitQuiz');
                x.style.display = "none";
              }
              document.getElementById('timerCount').innerHTML=str;

          // body...
        }
            
            var interval = setInterval(function(){
              if(isSubmit === 1)
              {
                document.getElementById('timerCount').innerHTML='';
                return;
              }
            
              timer(t,secondsToTime(t--));
            }, 1000);

            timer(t,secondsToTime(t));
            $('#submitQuiz').show();
            
  });

  // Click handler for the 'next' button
  $('#next').on('click', function (e) {
    e.preventDefault();
    
    // Suspend click listener during fade animation
    if(quiz.is(':animated')) {        
      return false;
    }
    choose();
    
      questionCounter++;
      displayNext();
    
  });
  
  // Click handler for the 'prev' button
  $('#prev').on('click', function (e) {
    e.preventDefault();
    $('#next').show();
    if(quiz.is(':animated')) {
      return false;
    }


    if(questionCounter<questions.length){
    choose();
    }

    questionCounter--;
    displayNext();
  });
  
  
  // Animates buttons on hover
  $('.button').on('mouseenter', function () {
    $(this).addClass('active');
  });
  $('.button').on('mouseleave', function () {
    $(this).removeClass('active');
  });
  
  // Creates and returns the div that contains the questions and 
  // the answer selections
  function createQuestionElement(index) {
    var qElement = $('<div>', {
      id: 'question'
    });
    
    var header = $('<h2>Question ' + (index + 1) + ':</h2>');
    qElement.append(header);
    
    var question = $('<p>').append(questions[index].question);
    qElement.append(question);
    
    var radioButtons = createRadios(index);
    qElement.append(radioButtons);
    
    return qElement;
  }
  
  // Creates a list of the answer choices as radio inputs
  function createRadios(index) {
    var radioList = $('<ul>');
    var item;
    var input = '';
    for (var i = 0; i < questions[index].choices.length; i++) {
      item = $('<li>');
      input = '<input type="radio" name="answer" class="radioClass" id=' + i + ' value=' + i + ' />';
      input += '<label for=' + i + '>' + questions[index].choices[i] + '</label>';

      item.append(input);
      radioList.append(item);
    }
    return radioList;
  }
  
  // Reads the user selection and pushes the value to an array
  function choose() {
    selections[questionCounter] = +$('input[name="answer"]:checked').val();
  }
  

function getQuestions(test_id){

  console.log("getQuestions called");
  console.log("test_id is" + test_id);
  test_id = test_id.replace(/ /g,'');

            $.ajax({
            url: "/test_get_questions/",
            type: "POST",
            data: {"test_id":test_id},
            success: function(data) {
        console.log("Printing response data.");
        console.log(data);
            let parsedData = JSON.parse(data);
            questions = parsedData;
                displayNext();
            },
            error: function(data) {
                alert("Error getting questions from server");
            }
        }); 
}



function getAnswers(test_id){

  console.log("getAnswers called");
  console.log("test_id is" + test_id);
  test_id = test_id.replace(/ /g,'');

            $.ajax({
            url: "/test_get_answers/",
            type: "POST",
            data: {"test_id":test_id},
            success: function(data) {
        console.log("Printing response data.");
        console.log(data);
            let parsedData = JSON.parse(data);
            questions = parsedData;
                //displayScore();
            },
            error: function(data) {
                alert("Error getting questions from server");
            }
        }); 
}

  // Displays next requested element
  function displayNext() { 
      console.log("Printing questions");
      console.log(questions);
     
    quiz.fadeOut(function() {
      $('#question').remove();
      
      console.log("Printing questionCounter below");

      if(questionCounter < questions.length){
                $('#end_of_test_div').hide();
              console.log('in if case : ' + questionCounter);
        var nextQuestion = createQuestionElement(questionCounter);
        quiz.append(nextQuestion).fadeIn();
        if (!(isNaN(selections[questionCounter]))) {
          $('input[value='+selections[questionCounter]+']').prop('checked', true);
        }
        
        // Controls display of 'prev' button
        if(questionCounter === 1){
          $('#prev').show();
        } else if(questionCounter === 0){
          
          $('#prev').hide();
          $('#next').show();
        }
      }else {
              console.log('in else case : ' + questionCounter);
      
        console.log(questions.length-1);
        console.log('questionCounter is = questions.length-1' + questionCounter);
       
        
        $('#next').hide();
        //$('#prev').hide();
        console.log("calling myFunction");
        console.log('selections in else is : ' + selections); 
        $('#end_of_test_div').show();

      }
    });
  }

    // Click handler for the 'submitQuiz' button
  $('#submitQuiz').on('click', function (e) {
        console.log("Diff String called");
        $('#end_of_test_div').hide();
        isSubmit = 1;
        $('#timerCount').hide();
        $('#prev').hide();
        var scoreElem = displayScore();
        quiz.append(scoreElem).fadeIn();
  });



  
  // Computes score and returns a paragraph element to be displayed
  function displayScore() {
    
    $('#question').hide();

    console.log("displayScore calling");
    var score = $('<p>',{id: 'score'});
    
    console.log("selections is : " + selections);
    console.log('selections.length is : ' + selections.length);
    var numCorrect = 0;
    var numNegative = 0;

    var correctAns = 0;
    var worngAns = 0;
    var unansweredQues = 0;

    var totalMarks = $('#total_marks_div').text();



    for (var i = 0; i < selections.length; i++) {

      console.log('i is : ' + i)
      console.log('Question is : ' + questions[i].question)
      console.log('correctAnswer is : ' + questions[i].correctAnswer)
    
      console.log("User i th selection is : " + selections[i]);
      

        var ans = questions[i].choices;
        var userAns = ans[selections[i]];
        console.log(' userAns is : ' + ans[selections[i]])

      if (userAns === questions[i].correctAnswer) {
        numCorrect += questions[i].positive_marks;
        correctAns += 1;
        console.log("User Answer is correct, adding to score");
      }
      else if(userAns !== undefined)
      {
        numNegative += questions[i].negative_marks;
        worngAns += 1;
      }
      else
      {
        unansweredQues += 1;
      }
    }

    var finalScore = numCorrect - numNegative;
    score.append('Your Score :-  ' + finalScore + ' / ' + 'out of' +  
                 totalMarks + ' marks. <br> Marks for Correct Answers :- ' + numCorrect + '<br>  Marks cut for Incorrect Answers :- ' +  numNegative
                 + '<br> Correctly Answered Questions :- ' + correctAns + '<br> Incorrectly Answered Questions :- ' + worngAns
                 + '<br> Unanswered Questions :-' + unansweredQues);
    var x = document.getElementById('submitQuiz');
    x.style.display = "none";
    $('#next').hide();

    return score;
  }




})();