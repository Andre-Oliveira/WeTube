from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    # path('video/', include('Video.urls')),
    path('', views.index, name='index'),
    # path('', HomeView.as_view()),
    path('admin/', admin.site.urls),
    path('video/', include('Video.urls')),
    path('audio/', include('Audio.urls')),
    # path('login', LoginView.as_view()),
    # path('register', RegisterView.as_view()),
    # path('logout', LogoutView.as_view())    
]

from django.conf import settings
from django.urls import include, path

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns