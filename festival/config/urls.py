from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('bars/', include('bars.urls', namespace='bars')), 
    path('posts/', include('posts.urls', namespace='posts')),
    path('users/', include('users.urls', namespace='users')),
    path('admin/', admin.site.urls),
    path('board/',include('board.urls', namespace= 'board')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
