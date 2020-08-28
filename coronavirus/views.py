from django.shortcuts import render
from covid import Covid
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.views.generic import DetailView
import pygal
from pygal.style import Style

covid = Covid()
country = covid.get_data()

def home(request):
    # pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(country, 10)

    try:
    	countries = paginator.page(page)
    except PageNotAnInteger:
    	countries = paginator.page(1)
    except EmptyPage:
    	countries = paginator.page(paginator.num_pages)

    genereting_graphic(country)
    # pass data to dict
    context = {'countries':countries, 'top_five':country[0:5]}
    return render(request, 'home.html', context)

def genereting_graphic(country):
	hist = pygal.Bar(print_values=True, value_formatter=lambda x: '{}'.format(x))
	hist.title = "Top five of cases in the world"
	
	for c in country[0:5]:
		hist.add(c['country'], c['confirmed'])
	
	hist.render_to_file('my-svgs/top_five.svg')
	hist.render()

def country_view(request, id):
    country = covid.get_status_by_country_id(id)
    custom_style = Style(
        colors=('yellow', 'red', 'green', 'black'))

    hist = pygal.Bar(print_values=True, value_formatter=lambda x: '{}'.format(x), 
        style=custom_style)
    hist.title = 'Information about ' + country['country']

    hist.add('Confirmed', country['confirmed'])
    hist.add('Active', country['active'])
    hist.add('Recovered', country['recovered'])
    hist.add('Deaths', country['deaths'])
    
    hist.render_to_file('my-svgs/c.svg')
    hist.render()
    
    return render(request, 'country.html')


    






         

