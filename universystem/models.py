from django.db import models
from django.contrib.auth.models import User
       
class Profile(models.Model):
    photo = models.ImageField(upload_to='images/profile', null=True,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True ,blank=True)
    def __str__(self):
        return self.user.username

class Lectures(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200,null=True ,blank=True)
    code = models.TextField(null=True ,blank=True)
    def __str__(self):
        return self.name

class Lectures_text(models.Model):
    lectures_id = models.ForeignKey(Lectures, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField(null=True ,blank=True)
    photo = models.ImageField(upload_to='images/lesson', blank=True)
    lectures_cod = models.TextField(null=True ,blank=True)
    def __str__(self):
        return self.title

class EnrollCource(models.Model):#Зарегистрироваться Курс
    lectures = models.ForeignKey(Lectures, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username

class QuestionOne(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
        
    class Meta:
        verbose_name = 'Тестер қосу'
        verbose_name_plural = 'Тестер қосу'

class Choice(models.Model):
    question = models.ForeignKey(QuestionOne, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Тестің жауаптарын қосу'
        verbose_name_plural = 'Тестің жауаптарын қосу'

class Application(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(null=True ,blank=True)


    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'техникалық көмек'
        verbose_name_plural = 'техникалық көмек'

class Lesson(models.Model):#Урок
    title = models.CharField(max_length=200)
    information = models.TextField()
    document = models.FileField(upload_to='pdf/document', null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    youtube = models.CharField(max_length=200)
    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    def __str__(self):
        return self.name


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    total = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    # Другие поля, которые вы хотите сохранить, например, дата и время теста

    def __str__(self):
        return f"Результат теста для {self.user.username}"