from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'users'
urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('mypage/', views.mypage, name='mypage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('letters/<int:user_id>/', views.letter_post, name='letter_post'),
    path('letters/to/', views.letter_to_list, name='letter_to_list'),
    path('letters/from/', views.letter_from_list, name='letter_from_list'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

