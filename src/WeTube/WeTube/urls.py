#Django imports
from django.contrib import admin
from django.urls import include, path
#Plugin imports
from rest_framework import routers
#App imports
from . import views
from .views import userViewSet

router = routers.DefaultRouter()
router.register('users', userViewSet)
urlpatterns = [
    #path('', views.index, name='index'),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('video/', include('Video.urls')),
    path('audio/', include('Audio.urls')),
    # path('login', LoginView.as_view()),
    # path('register', RegisterView.as_view()),
    # path('logout', LogoutView.as_view())    
]

from django.conf import settings

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns