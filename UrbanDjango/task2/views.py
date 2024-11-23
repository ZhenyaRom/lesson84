from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def responsible1(request):
    return render(request, 'sample2.html')


class Responsible2(TemplateView):
    template_name = 'sample1.html'
