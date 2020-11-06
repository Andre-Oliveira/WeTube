from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('upload', NewVideo.as_view())),
    path('uploads', views.index, name='index'),
    path('subscriptions', views.index, name='index'),
    # path('<int:id>', VideoView.as_view()),
    # path('comment', CommentView.as_view()),
    # path('get_audio/<file_name>', VideoFileView.as_view()),

]