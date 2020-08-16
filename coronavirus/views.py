from django.shortcuts import render
from covid import Covid
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.views.generic import DetailView
import pygal

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
    context = {'countries':countries, 'top_ten':country[0:10]}
    return render(request, 'home.html', context)


def genereting_graphic(country):
	hist = pygal.Bar(print_values=True, print_values_position='top')
	hist.title = "Top ten of cases in the world"
	
	for c in country[0:10]:
		hist.add(c['country'], c['confirmed'])
	
	hist.render_to_file('my-svgs/top_ten.svg')
	hist.render()


class ViewCountryData(DetailView):
    model = country
    template = 'country.html'

    






         

