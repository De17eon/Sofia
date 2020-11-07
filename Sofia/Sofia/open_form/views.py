from django.shortcuts import render
from django.template.context_processors import csrf
from django.http import JsonResponse
from django.contrib import auth

from .models import OpenForm, OpenFormAnswer
from authsystem.models import Candidate
from authsystem.models import Company
from vacancy.models import Vacancy

#Отображает форму для ответа юзером
def create_open_form_show(request):
    
    info = {}
    info.update(csrf(request))
    
    info["id"] = 1
    info["username"] = auth.get_user(request).username
    try:
        user = Company.objects.get(user = auth.get_user(request)) 
        info["isCompany"] = user.is_company
    except:
        info["isCompany"] = False
    
    return render(request, 'create-open-form.html', info)


def create_open_form(request):
    print(request.POST)
    vacancy_id = request.POST.get('id')
    vacancy = Vacancy.objects.get(id = vacancy_id)
    num = request.POST.get('num', 0)
    text = request.POST.get('text')
    
    open_form = OpenForm(vacancy_id = vacancy, order = num, description = text)
    open_form.save()

    return JsonResponse({
        'status': 'Ok'
    })

#Отображает форму для ответа юзером
def show_open_form(request, id):
    open_form = OpenForm.objects.get(id = id)
    info = {}
    info.update(csrf(request))
    info["description"] = open_form.description
    info["id"] = id
    info["username"] = auth.get_user(request).username
    user = Company.objects.get(user = auth.get_user(request)) 
    info["isCompany"] = user.is_company
    return render(request, 'open-form.html', info)


#Отображает форму для редактирования владельцем
def edit_open_form(request, id):
    open_form = OpenForm.objects.get(id = id)
    answer_open_form = OpenFormAnswer.objects.get(open_form_id = open_form)
    info = {}
    info.update(csrf(request))
    info["description"] = open_form.description
    info["id"] = id
    info["username"] = auth.get_user(request).username
    info["answer"] = answer_open_form.text
    
    try:
        user = Company.objects.get(user = auth.get_user(request)) 
        info["isCompany"] = user.is_company
    except:
        info["isCompany"] = False
    return render(request, 'edit-open-form.html', info)

#Проверка задания от юзера работодателем
def check_open_form(request, id):
    open_form = OpenForm.objects.get(id = id)
    open_form_answer = OpenFormAnswer.objects.get(open_form_id= open_form)

    info = {}
    info.update(csrf(request))
    info["description"] = open_form.description
    info["id"] = id
    info["username"] = auth.get_user(request).username
    user = Company.objects.get(user = auth.get_user(request)) 
    info["isCompany"] = user.is_company
    info["answer"] = open_form_answer.text
    return render(request, 'check-open-form.html', info)

#Записать оценку в бд
def write_mark_to_tast(request):
    open_form = OpenForm.objects.get(id = request.POST.get('id'))
    open_form_answer = OpenFormAnswer.objects.get(open_form_id= open_form)
    open_form_answer.mark = request.POST.get('mark')
    open_form_answer.save()
    return JsonResponse({
        'status': 'Ok'
    })

#Сохранаяет изменения в описании задании
def save_form_edition(request):
    try:
        edited_text = request.POST.get('answer')
        open_form = OpenForm.objects.get(id = request.POST.get('id'))
        open_form.description = edited_text
        open_form.save()
        return JsonResponse({
            'status': 'Ok'
        })
    except:
        return JsonResponse({
            'status': 'Fail'
        }
        )
#сохраняет ответ юзера
def write_openForm_ans(request):
    try:
        files = request.FILES
        answer = request.POST.get('answer')
        form_id = request.POST.get('id')
        
        form_answer = OpenFormAnswer(
            text = answer,
            open_form_id = OpenForm.objects.get(id = form_id),
            candidate_id = Candidate.objects.get(username = "user")
        )
       
        #проверка на пустоту
        if len(files) == 0: 
            form_answer.save()
        else:
            file_ = files['file']
            form_answer.answer_file = file_
            form_answer.save()

        return JsonResponse({
            'status': 'Ok'
        })
    except:
        return JsonResponse({
            'status': 'Fail'
        })