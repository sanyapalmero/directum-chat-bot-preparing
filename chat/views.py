from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

class IndexView(View):
    """Главная страница"""
    def get(self, request):
        template_name = 'chat/index.html'
        return render(request, template_name)


class ChatView(View):
    """Страница чата"""
    template_name = 'chat/chat.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_message = request.POST['user-message']
        if user_message == "Привет!":
            return JsonResponse({'UserMessage':user_message, 'BotMessage':'Привет :)'})
        elif user_message == "Как дела?":
            return JsonResponse({'UserMessage':user_message, 'BotMessage':'Замечательно!'})
        else:
            return JsonResponse({'UserMessage':user_message, 'BotMessage':'Непонятный для меня запрос :('})
