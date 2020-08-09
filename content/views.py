from django.shortcuts import render
from django.views import View
from collections import OrderedDict
import requests
from .fusioncharts import FusionCharts
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
        chart_data = list()
        datasource = OrderedDict()
        for language in language_set:
            language_dict = dict()
            count = language_list.count(language)
            language_dict["label"] = language
            language_dict["value"] = str(count)
            chart_data.append(language_dict)

        datasource["data"] = chart_data
        chartConfig = OrderedDict()
        chartConfig["caption"] = "Languages used by user"
        chartConfig["showpercentvalues"] = '1'
        chartConfig["decimals"] = '1'
        chartConfig["plottooltext"] = "$label"
        chartConfig["theme"] = "fusion"
        datasource["chart"] = chartConfig
        language_chart = FusionCharts("doughnut2d", "myFirstChart", "100%",
                                      "400", "myFirstchart-container", "json", datasource)
        print(datasource)
        context = {
            'data': data,
            'follower_list': follower_list,
            'output': language_chart.render(),
        }
        return render(request, self.template_name, context=context)
