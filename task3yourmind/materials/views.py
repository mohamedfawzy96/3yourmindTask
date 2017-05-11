from django.shortcuts import render
from django.http import HttpResponse
from .models import Materials
from companies.models import Companies
from django.shortcuts import get_object_or_404

import random
import json

# Create your views here.


''' Generates Random for materials with out the supplier '''
def generate_data_for_materials(request):
    material_names = ['Steel','Copper','Plastic','Iron','Fabric']
    material_colors = ['Sliver', 'Yellow', 'White', 'Reddish-Yelow', 'Grey']
    material_price = [2.00, 3.00, 4.00, 2.00, 6.00]

    for i in range(0,len(material_names)):
        companies =  Companies.objects.all()
        random1 = round((random.random())*companies.count())
        company = companies[random1]
        material = Materials(name=material_names[i], color=material_colors[i], price=material_price[i], supplier=company)
        material.save()

    return HttpResponse("Done Generating")

def return_all_materials(request):
    materials = Materials.objects.all()
    return render(request, 'materials/home.html', {'materials': materials})


def home(request):
    return render(request, 'home/home.html')

def return_materials_supplier(request,id):
    material = get_object_or_404(Materials, pk=id)
    return HttpResponse(material.supplier)

