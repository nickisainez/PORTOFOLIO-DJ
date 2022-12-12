from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from . import views
from .views import RegisterView


urlpatterns = [
    path('crear/', views.createProject, name='crear' ),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_then_login, name='logout' ),
    path('', views.viewProjects, name='home'),
    path('proyecto/<int:project_id>', views.detailsProjects, name='detailsProjects'),
    path('aboutme/',views.aboutMe, name='aboutme'),
    path('contact/',views.contact, name='contact')
]