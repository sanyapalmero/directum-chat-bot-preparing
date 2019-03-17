from django.shortcuts import render
from django.views import View


class IndexView(View):
    """Главная страница"""
    def get(self, request):
        template_name = 'chat/index.html'
        return render(request, template_name)


class ChatView(View):
    """Страница чата"""
    def get(self, request):
        template_name = 'chat/chat.html'
        return render(request, template_name)
