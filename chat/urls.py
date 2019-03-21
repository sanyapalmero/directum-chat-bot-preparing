from django.urls import include, path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('chat/', views.ChatView.as_view(), name='chat'),
    path('faq/', views.FaqView.as_view(), name='faq')
]
