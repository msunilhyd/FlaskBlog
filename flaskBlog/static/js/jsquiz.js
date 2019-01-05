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

     getQuestions();
     var t =  20;

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
    $('#submitQuiz').hide();
    $('#next').show();
    if(quiz.is(':animated')) {
      return false;
    }
    choose();
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
      input = '<input type="radio" name="answer" class="radioClass" value=' + i + ' />';
      input += questions[index].choices[i];
      item.append(input);
      radioList.append(item);
    }
    return radioList;
  }
  
  // Reads the user selection and pushes the value to an array
  function choose() {
    selections[questionCounter] = +$('input[name="answer"]:checked').val();
  }
  



function getQuestions(){

  console.log("getQuestions called");

            $.ajax({
            url: "/tests/",
            type: "GET",
            data: {},
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
      
      if(questionCounter < questions.length-1){
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
        console.log(questionCounter);
        var nextQuestion = createQuestionElement(questionCounter);
        quiz.append(nextQuestion).fadeIn();
        $('#next').hide();
        //$('#prev').hide();
        $('#submitQuiz').show();
        console.log("calling myFunction");         
      }
    });
  }

    // Click handler for the 'submitQuiz' button
  $('#submitQuiz').on('click', function (e) {
        console.log("Diff String called");
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
    var numCorrect = 0;
    for (var i = 0; i < selections.length; i++) {
      console.log(questions[i].correctAnswer);
      console.log("Printing above and below selections");
      console.log(selections[i]);
      
        var ans = questions[i].choices;
        console.log("Printing ans choice below");
        console.log(ans[selections[i]]);
        var userAns = ans[selections[i]];

      if (userAns === questions[i].correctAnswer) {
        numCorrect++;
        console.log("Correct Answer");
      }
    }
    score.append('Your Score :-  ' + numCorrect + ' / ' +
                 questions.length );
    var x = document.getElementById('submitQuiz');
    x.style.display = "none";
    
    return score;
  }




})();