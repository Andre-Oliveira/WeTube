#
from django.urls import include, path
#Plugin imports
from rest_framework import routers
#
from . import views
from .views import VideoViewSet

router = routers.DefaultRouter()
router.register('videos', VideoViewSet)
urlpatterns = [
    # path('', views.index, name='index'),
    path('', include(router.urls)),
    # path('upload', NewVideo.as_view())),
    path('uploads', views.index, name='index'),
    path('subscriptions', views.index, name='index'),
    # path('<int:id>', VideoView.as_view()),
    # path('comment', CommentView.as_view()),
    # path('get_audio/<file_name>', VideoFileView.as_view()),

]