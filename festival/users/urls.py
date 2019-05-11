from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'users'
urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('memlist', views.memlist, name='memlist'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

