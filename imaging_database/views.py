from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    categories = Category.objects.all()

    context = {}
    context['categories'] = categories

    return render(request, 'index.html', context)

def categoryPage(request, pk):
    category = Category.objects.get(id=pk)
    images = spectralImage.objects.filter(category=category)
    # .order_by('-date_created')[:6]
    for x in images:
        x.shortDescription = x.description[:130]

    context = {}
    context['images'] = images
    context['category'] = category

    return render(request, 'category.html', context)

# def imageDetailPage(request, slug1, slug2):

#     category = Category.objects.get(slug=slug1)
#     image = spectralImage.objects.get(slug=slug2)

#     context = {}
#     context['category'] = category
#     context['image'] = image
#     return render(request, 'image.html', context)

def spectralPage(request):
    category = Category.objects.filter()
    # image = spectralImage.objects.get()
    # mask = Mask.objects.all()
    # tissuetype = Tissue_class.objects.all()
    hspectral = spectralImage.objects.filter()

    context={}
    context['category'] =  category
    # context['image'] = image
    # context['mask'] = mask
    # context['tissuetype'] = tissuetype
    context['hspectral'] = hspectral
    return render(request, 'spectral.html', context)

def searchPage(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        # patient_search = Patient.objects.filter(gender__contains=searched)
        rgb_search = spectralImage.objects.filter(Q(description__icontains=searched) | Q(uniqueId__icontains=searched))
        return render(request, 'search.html', {'searched':searched, 'rgb_search': rgb_search})
    else:
        return render(request, 'search.html', {})


def searchPage2(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        # patient_search = Patient.objects.filter(gender__contains=searched)
        rgb_search = Tissue_class.objects.filter(class_type__icontains=searched)
        return render(request, 'search2.html', {'searched':searched, 'rgb_search': rgb_search})
    else:
        return render(request, 'search2.html', {})


def testPage(request, pk):
    spectral_image = spectralImage.objects.filter(id=pk).first()
    masked = Mask.objects.filter(spectral_image = spectral_image)
    context={}
    context['spectral_image'] =  spectral_image
    context['masked'] =  masked
    return render(request, 'test.html', context)

