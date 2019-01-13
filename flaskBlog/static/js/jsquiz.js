

function selectradio(event){
   console.log(event);
      var $radio = $(event.target)       // if this was previously checked
      if ($radio.data('waschecked') == true)
      {
          $radio.prop('checked', false);
          $radio.data('waschecked', false);
      }
      else{
          $radio.data('waschecked', true);        // remove was checked from other radio
     }
     // $radio.siblings('input[name="rad"]').data('waschecked', false);
     $radio.closest("ul").find('input').each(function (index,elem){
       if(elem != event.target){
         $(elem).data('waschecked', false);
       }
     });

}
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
    if(questionCounter<questions.length){
    choose();
    }    
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
      input = '<input type="radio" name="answer" class="radioClass" id=' + i + ' value=' + i + ' onclick="selectradio(event)" />';
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
    if(questionCounter<questions.length){
    choose();
    }

       var test_id = $('#test_id_div').text();
        getAnswers(test_id);

  });

var questionsAns;
 
function getAnswers(test_id){

  console.log("getAnswers called");
  console.log("test_id is" + test_id);
  test_id = test_id.replace(/ /g,'');

            $.ajax({
            url: "/test_get_answers/",
            type: "POST",
            data: {"test_id":test_id},
            success: function(data) {
        console.log("Printing Answers data.");
        console.log(data);
            let parsedData = JSON.parse(data);
            questionsAns = parsedData;
            var scoreElem = displayScore(questionsAns);
            quiz.append(scoreElem).fadeIn();
            },
            error: function(data) {
                alert("Error getting questions from server");
            }
        }); 
}



    var positive_score = 0;
    var negative_score = 0;

    var no_of_correct_ans_ques = 0;
    var no_of_wrong_ans_ques = 0;
    var no_of_not_ans_ques = 0;


  // Computes score and returns a paragraph element to be displayed
  function displayScore(questionsAns) {
    
    $('#question').hide();

    var score = $('<p>',{id: 'score'});


    var totalMarks = $('#total_marks_div').text();

    console.log('printing questionsAns from displayScore' + questionsAns);

    console.log('printing length of questions : ' + questionsAns.length);


    console.log('printing selections : ' + selections);

    console.log('selections.length is : ' + selections.length);

    for (var i = 0; i < selections.length; i++) {

      console.log('i is : ' + i);

        var ans = questions[i].choices;
        var userAns = ans[selections[i]];
        console.log(' userAns is : ' + userAns);
        console.log(' correctAnswer is : ' + questionsAns[i].correctAnswer);

      if (userAns === questionsAns[i].correctAnswer) {
        positive_score += questionsAns[i].positive_marks;
        no_of_correct_ans_ques += 1;
        console.log('positive_score is : ' + positive_score);
        console.log("User Answer is correct, adding to score");
      }
      else if(userAns !== undefined)
      {
        negative_score += questionsAns[i].negative_marks;
        no_of_wrong_ans_ques += 1;
      }
      else
      {
        console.log('no_of_not_ans_ques below');
        console.log(ans[selections[i]]);
        no_of_not_ans_ques += 1;
      }
    }


    if(i < questionsAns.length-1)
    {
        no_of_not_ans_ques += questionsAns.length - i ;
    }

    var finalScore = positive_score - negative_score;
    score.append('Your Score :-  ' + finalScore + ' / ' + 'out of' +  
                 totalMarks + ' marks. <br> Marks for Correct Answers :- ' + positive_score + '<br>  Marks cut for Incorrect Answers :- ' +  negative_score
                 + '<br> Correctly Answered Questions :- ' + no_of_correct_ans_ques + '<br> Incorrectly Answered Questions :- ' + no_of_wrong_ans_ques
                 + '<br> Unanswered Questions :- ' + no_of_not_ans_ques);
    var x = document.getElementById('submitQuiz');
    x.style.display = "none";
    $('#next').hide();

    updateUserScore(finalScore, positive_score, negative_score, no_of_correct_ans_ques, no_of_wrong_ans_ques, no_of_not_ans_ques);
    return score;
  }  


function updateUserScore( finalScore, positive_score, negative_score, no_of_correct_ans_ques, no_of_wrong_ans_ques, no_of_not_ans_ques){

  console.log("updateUserScore called");
  var test_id = $('#test_id_div').text();
  console.log("test_id is" + test_id);
  test_id = test_id.replace(/ /g,'');
  var user_id = $('#user_id_div').text();
  user_id = user_id.replace(/ /g,'');



            $.ajax({
            url: "/test_update_user_score/",
            type: "POST",
            data: {"test_id":test_id, "user_id":user_id, "user_score":finalScore,
             "positive_score":positive_score, "negative_score":negative_score, "correct_answers":no_of_correct_ans_ques,
            "wrong_answers":no_of_wrong_ans_ques, 
             "no_answers":no_of_not_ans_ques},
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


})();
