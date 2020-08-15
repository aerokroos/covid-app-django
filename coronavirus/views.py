from django.shortcuts import render
from covid import Covid
from django.core.paginator import Paginator
from django.contrib.auth.models import User

import pygal

def home(request):
    # Get covid data
    covid = Covid()
    country = covid.get_data()

    # pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(country, 20)

    try:
    	countries = paginator.page(page)
    except PageNotAnInteger:
    	countries = paginator.page(1)
    except EmptyPage:
    	countries = paginator.page(paginator.num_pages)

    genereting_graphic(country)
    # pass data to dict
    context = {'countries':countries, 'top_ten':country[0:10]}
    return render(request, 'home.html', context)


def genereting_graphic(country):
	hist = pygal.Bar()

	hist.title = "Top ten of cases in the world"
	#hist.xlabels = [c['country'] for c in country[0:10]]
	
	for c in country[0:10]:
		hist.add(c['country'], c['confirmed'])

	hist.render_to_file('static/svg/top_ten.svg')

def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
	





         

