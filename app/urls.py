from django.urls import path
from . import views


urlpatterns = [
    path('',views.LoginView.as_view(), name='login'),
    path('home',views.HomeView.as_view(), name='home'),
    path('logout',views.logoutview, name='logout'),
    path('profile',views.ProfileView.as_view(), name='profile'),
    path('courses',views.shortCourseListView, name='courses'),
    path('addcourses',views.CreateCourseView.as_view(), name='addcourses'),
    path('delete/<int:id>',views.deleteCourseView, name='delete'),
    
]
