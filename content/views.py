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

        repos_url = data['repos_url']
        repo_data = requests.get(repos_url).json()
        repo_list = [repo for repo in repo_data]
        language_list = [repo["language"]
                         for repo in repo_list if repo["language"]]
        language_set = list(set(language_list))
        language_dict = dict()
        for language in language_set:
            count = language_list.count(language)
            language_dict[language] = count

        context = {
            'data': data,
            'follower_list': follower_list
        }
        return render(request, self.template_name, context=context)


# def Home(request):
#     return render(request, 'content/home.html')
