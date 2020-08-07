from django.shortcuts import render
from django.views import View
# Create your views here.


class Home(View):
    template_name = 'content/home.html'

    def get(self, request):
        return render(request, self.template_name)

# def Home(request):
#     return render(request, 'content/home.html')
