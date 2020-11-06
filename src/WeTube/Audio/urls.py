from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('upload', NewAudio.as_view())),
    path('uploads', views.index, name='index'),
    path('subscriptions', views.index, name='index'),
    # path('<int:id>', AudioListen.as_view()),
    # path('comment', CommentView.as_view()),
    # path('get_audio/<file_name>', AudioFileView.as_view()),
]