var interviewCntTags = [], interviewCnt = 0;

function interviewAddTags(question, text = "") {
    //var divTags = document.getElementById('tags[' + question + ']');
    var divTags = $('div#tags\\[' + question + '\\]');
    console.log($('div#tags[' + question + ']'), 'tags[' + question + ']');
    var name = 'tags[' + question + ']';
    divTags.append("<input name='" + name + "' placeholder = 'Введите быстрый ответ' value='" + text + "' class='center-input--answer'>");
    //divTags.innerHTML += "<input name='" + name + "' placeholder = 'Введите быстрый ответ' value='" + text + "'>";
    interviewCntTags[question]++;

}

function addQuestion(name = "", tags = []) {
    interviewCntTags.push(0);
    //form_ = document.forms.interviewQuestions;
    form_ = $('form#interviewQuestions');

    strHtml = "";
    strHtml += "<div id='interview_question'>";

    strHtml += "<input name='interview_question[" + interviewCnt + "]' placeholder = 'Введите вопрос' class='center-input--question'><br>";


    strHtml += "<div id='tags[" + interviewCnt + "]' class='quick_answer'></div>";
    strHtml += "<input name='addTags[" + interviewCnt + "]' type='button' onclick='interviewAddTags(" + interviewCnt + ")' \
                    value='Добавить быстрый ответ' class='center-input btn btn-lg btn-secondary'><br><br>";
    strHtml += "</div>";
    //form_.innerHTML += strHtml;
    form_.append(strHtml);

    for (var i = 0; i < tags.length; i++) {
        interviewAddTags(interviewCnt, tags[i]);
    }
                    
    interviewCnt++;
}

document.addEventListener("DOMContentLoaded", () => {
    var btnAddQuestion = document.getElementById("interview-add_question");
    if (btnAddQuestion != null) {
        btnAddQuestion.onclick = () => {
            addQuestion();
        }
    }
    var btnSaveForm = document.getElementById('interview-save_question');
    if (btnSaveForm != null) {
        btnSaveForm.onclick = () => {
            var fd = new FormData(interviewQuestions);
            $.ajax({
                type: "POST",
                url: 'interview/new/ajax/',
                data: fd,
                contentType: false,
                processData: false
            }).done(function (result) {
                alert(result['answer']);
                if (result['status'] == 'ok') {
                    console.log($("[name='idInterview']"));
                    console.log(result['id']);
                    $("[name='idInterview']").val(result['id']);
                }
            });
        }
    }

    var btnSaveForm = document.getElementById('interview-save_answer');
    if (btnSaveForm != null) {
        btnSaveForm.onclick = () => {
            var fd = new FormData(interviewAnswer);
            $.ajax({
                type: "POST",
                url: 'interview/answer/ajax/',
                data: fd,
                contentType: false,
                processData: false
            }).done(function (result) {
                alert(result);
            });
        }
    }
    
})

$(document).ready(function() {
// CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});


function interviewAnswerAddTag(id, text){
    let textArea = document.getElementsByName('answer[' + id + ']')[0];
    if (textArea) {
        textArea.innerHTML += text;
    }
}