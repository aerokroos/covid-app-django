from django.shortcuts import render
from covid import Covid
# Create your views here.
def home(request):
    covid = Covid()
    country = covid.get_data()
    
    context = {'countries':country, 'top_ten':country[0:10]}
    return render(request, 'home.html', context)

         

