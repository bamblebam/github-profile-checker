from django.shortcuts import render
from django.views import View
import requests
# Create your views here.


class Home(View):
    template_name = 'content/home.html'
    url = 'https://api.github.com/users/{}'

    def get(self, request):
        data = requests.get(self.url.format('bamblebam')).json()
        follower_url = data['followers_url']
        follower_data = requests.get(follower_url).json()
        follower_list = [follower for follower in follower_data]
        print(follower_list[0])
        context = {
            'data': data,
            'follower_list': follower_list
        }
        return render(request, self.template_name, context=context)


# def Home(request):
#     return render(request, 'content/home.html')
