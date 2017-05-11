from django.shortcuts import render
from .models import Companies
from django.http import HttpResponse


def generate_data_for_companies(request):
    companies_names = ['CompanyA','CompanyB','CompanyC','CompanyD','CompanyE']
    companies_locations = ['Cairo', 'Berlin', 'Poland', 'London', 'Silicon Valley']

    for i in range(0,len(companies_names)):
        company = Companies(name=companies_names[i], location=companies_locations[i])
        company.save()
        print(company)

    return HttpResponse("Done Generating")