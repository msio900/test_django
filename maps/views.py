from django.shortcuts import render

# Create your views here.
import folium
def home(request):
    mf = folium.Map([35.3369, 127.7306], zoom_start=10)
    mf = mf._repr_html_()
    first = 'sanghun'
    result = {'mapfolium': mf, 'f01':first}

    return render(request, template_name='maps/home.html', context=result)
