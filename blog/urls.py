from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.all_posts, name='posts'),
    path('posts/<int:post_id>/', views.post_detail, name='detail'),
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]
