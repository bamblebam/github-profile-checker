from django.shortcuts import render
from django.views import View
import requests
# Create your views here.


class Home(View):
    template_name = 'content/home.html'
    url = 'https://api.github.com/users/{}'

    def get(self, request):
        data = requests.get(self.url.format('bamblebam')).json()
        context = {
            'data': data,
        }
        return render(request, self.template_name, context=context)


# def Home(request):
#     return render(request, 'content/home.html')
