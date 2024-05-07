from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
app_name = 'universystem'

urlpatterns =[
	path('',auth_views.LoginView.as_view(),name='login'),
	path('logout/',auth_views.LogoutView.as_view(),name='logout'),
	path('student/',views.StudentProfileIndexView.as_view(), name='StudentProfileIndexView'),
	path('profile/',views.ProfileView.as_view(), name='ProfileView'),
	path('about/',views.AboutView.as_view(), name='AboutView'),
	path('lessons/<int:id>',views.LessonsDetailView.as_view(), name='LessonsDetailView'),
	path('video/<int:id>',views.VideoDetailView.as_view(), name='VideoDetailView'),
	path('addEroll/<int:id>',views.AddEnrlcourseView.as_view(), name='AddEnrlcourseView'),
	path('add/',views.AddIndexView.as_view(), name='AddIndexView'),
	path('add/text',views.AddTextIndexView.as_view(), name='AddTextIndexView'),
	path('user/registration', views.UserRegistrationView.as_view(), name='user_registration_page'),
	path('geme/', views.game, name='game'),
	path('test/', views.TestView.as_view(), name='test'),
	path('application/', views.ApplicationView.as_view(), name='ApplicationView'),
	path('submit_answers/', views.submit_answers, name="submit_answers"),
]