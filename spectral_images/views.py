from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    #return HttpResponse("Data architecture of HSI");
    return render(request, 'home.html', {'name':'Gemal'})

'''
def add(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    addition = num1+num2
    return render(request, 'result.html', {'result':addition})
'''
def add(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    addition = num1+num2
    return render(request, 'result.html', {'result':addition})