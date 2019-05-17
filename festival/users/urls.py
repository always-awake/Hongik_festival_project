from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'users'
urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('<int:user_id>/', views.userpage, name='userpage'),
    path('<int:user_id>/likes/', views.like_user, name='like_user'),
    path('mypage/', views.mypage, name='mypage'),
    path('<int:user_id>/mypage_update/',views.mypage_update,name="mypage_update"), #test 중
    path('<int:user_id>/mypage_update_func/',views.mypage_update_func,name="mypage_update_func"),#테스트중
    path('signup/', views.signup, name='signup'),
    path('login/direct/', views.direct_login, name='direct_login'),
    path('login/indirect/', views.indirect_login, name='indirect_login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_id>/letters/', views.letter_post, name='letter_post'),
    path('letters/<str:type>/', views.letter_list, name='letter_list'),
    path('<int:letter_id>/letters/detail/', views.letter_detail, name='letter_detail'), 
    path('<int:letter_id>/letters/delete/', views.letter_to_delete, name='letter_delete'),
    path('privacy', views.privacy, name='privacy'),
    path('report/', views.report, name='report'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

