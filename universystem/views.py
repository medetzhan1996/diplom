import errno
import sys
from multiprocessing import context
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic.base import TemplateResponseMixin,View
from .forms import UserRegistrationForm, ProfileForm, LecturesForm, LecturesTextForm,ApplicationForm
from .models import User, Profile,Lectures,Lectures_text,EnrollCource,QuestionOne,Choice,Lesson,TestResult
from django.http import JsonResponse
from django.contrib import messages


class UserRegistrationView(TemplateResponseMixin, View):
    template_name = 'registration/registration.html'

    def get(self,request):
        registration_form = UserRegistrationForm()
        #profile_form = ProfileForm()
        return self.render_to_response({'registration_form': registration_form})

    def post(self, request):
        registration_form = UserRegistrationForm(request.POST)
        #profile_form = ProfileForm(request.POST, files=request.FILES)
        if registration_form.is_valid():
            new_user = registration_form.save(commit=False)
        # Set the chosen password
            new_user.set_password(
            registration_form.cleaned_data['password'])
        # Save the User object
            new_user.save()
            # profile = profile_form.save(commit = False)
            # profile.user = new_user
            # profile.save()
            return redirect('universystem:login')
        return self.render_to_response({'registration_form': registration_form, 'profile_form': profile_form})

class ProfileView(TemplateResponseMixin,View):
    template_name = 'ProfileView.html'
    def get(self,request):
        user_id = request.user  # Предположим, что у вас есть аутентифицированный пользователь
        test_results = TestResult.objects.filter(user=user_id)
        lectures = Lectures.objects.all()
        video = Lesson.objects.all()
        lesson = EnrollCource.objects.filter(user= request.user)
        return self.render_to_response({'lectures': lectures, 'lesson': lesson,'video':video,'test_results':test_results})


class AboutView(TemplateResponseMixin,View):
    template_name = 'AboutView.html'
    def get(self,request):
        lectures = Lectures.objects.all()
        video = Lesson.objects.all()
        return self.render_to_response({'lectures': lectures,'video':video})

class StudentProfileIndexView(TemplateResponseMixin,View):
    template_name = 'home.html'
    def get(self,request):
        lectures = Lectures.objects.all()
        video = Lesson.objects.all()

        return self.render_to_response({'lectures': lectures,'video':video})

class LessonsDetailView(TemplateResponseMixin,View):
    template_name = 'detail.html'
    def get(self,request, id):
        lectures = Lectures.objects.all()
        lecturesone = Lectures.objects.get(id=id)
        video = Lesson.objects.all()
        lectures_text = Lectures_text.objects.filter(lectures_id=id)

        return self.render_to_response({'lectures': lectures, 'lecturesone':lecturesone,
         'lectures_text':lectures_text,'video':video})

    def post(self,request, id):
        lectures = Lectures.objects.all()
        lecturesone = Lectures.objects.get(id=id)
        video = Lesson.objects.all()
        lectures_text = Lectures_text.objects.filter(lectures_id=id)
        
        if request.method == "POST":
            codeareadata = request.POST['codearea']

            try:

                original_stdout = sys.stdout
                sys.stdout = open('file.txt', 'w') 

                exec(codeareadata)  

                sys.stdout.close()

                sys.stdout = original_stdout 


                output = open('file.txt', 'r').read()

            except Exception as e:
                sys.stdout = original_stdout
                output = e
                
        return self.render_to_response({'lectures': lectures, 'lecturesone':lecturesone, 
         'lectures_text':lectures_text,'code': codeareadata , 'output': output,'video':video})


class VideoDetailView(TemplateResponseMixin, View):
    template_name = 'video-detail.html'

    def get(self, request, id):
        lectures = Lectures.objects.all()
        video = Lesson.objects.all()
        related_videos = Lesson.objects.filter(id=id)
        return self.render_to_response({'video': video,'lectures':lectures,'related_videos':related_videos})


class AddEnrlcourseView(View):

    def post(self,request,id):
        courses_obj = EnrollCource(lectures_id=request.POST['lessonid'], user =request.user)
        courses_obj.save()
        return redirect('universystem:LessonsDetailView',id)

class AddIndexView(TemplateResponseMixin,View):
    template_name = 'test.html'
    def get(self,request):
        lectures_form = LecturesForm()
        lectures = Lectures.objects.all()
        video = Lesson.objects.all()
        return self.render_to_response({'lectures_form':lectures_form,'lectures':lectures,'video':video})

    def post(self,request):
        video = Lesson.objects.all()
        lectures_form = LecturesForm(data=request.POST)
        if lectures_form.is_valid():#тексеру
            lectures_formadd = lectures_form.save(commit=False)
            lectures_formadd.save()
            return redirect('universystem:AddIndexView')
        return self.render_to_response({'lectures_form': lectures_form,'video':video})

class AddTextIndexView(TemplateResponseMixin,View):
    template_name = 'addtext.html'
    def get(self,request):
        lectures_text = LecturesTextForm()
        lectures = Lectures_text.objects.all()
        video = Lesson.objects.all()
        return self.render_to_response({'lectures_text':lectures_text,'lectures':lectures,'video':video})

    def post(self,request):
        lectures_text = LecturesTextForm(data=request.POST)
        if lectures_text.is_valid():#тексеру
            lectures_formadd = lectures_text.save(commit=False)
            lectures_formadd.save()
            return redirect('universystem:AddTextIndexView')
        return self.render_to_response({'lectures_text': lectures_text,'lectures':lectures})

def game(request):
    return render(request, 'index.html')

class TestView(TemplateResponseMixin,View):
    template_name = 'test.html'
    def get(self,request):
        video = Lesson.objects.all()
        questions = QuestionOne.objects.all()
        return self.render_to_response({'questions': questions,'video':video})


def submit_answers(request):
     # Получаем POST-данные
    data = request.POST
    
    # Инициализируем переменные
    score = 0
    total = 0
    results = {}
    
    # Перебираем все отправленные ответы
    for key, value in data.items():
        # Если имя поля не является идентификатором вопроса, то пропускаем
        if not key.isdigit():
            continue
        
        # Получаем выбранный вариант ответа
        choice = Choice.objects.get(id=value)
        
        # Если выбранный вариант ответа является правильным, увеличиваем счетчик
        if choice.is_correct:
            score += 1
        
        # Увеличиваем общий счетчик вопросов
        total += 1
        
        # Сохраняем результат для данного вопроса
        results[int(key)] = choice.is_correct
    
    # Формируем результаты
    results = {
        'score': score,
        'total': total,
        'results': results
    }
    test_result = TestResult.objects.create(
        user=request.user,  # Предположим, что у вас есть аутентифицированный пользователь
        score=score,
        total=total,
        # Другие поля, которые вы хотите сохранить
    )
    # Возвращаем результаты в виде JSON-ответа
    return JsonResponse(results)

class ApplicationView(TemplateResponseMixin,View):
    template_name = 'application.html'
    def get(self,request):
        comment_form = ApplicationForm()
        return self.render_to_response({'comment_form':comment_form})

    def post(self,request):
        comment_form = ApplicationForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            messages.info(request, "Техникалық көмек сәтті жіберілді")
            return redirect('universystem:StudentProfileIndexView')
        return self.render_to_response({ 'comment_form':comment_form})
