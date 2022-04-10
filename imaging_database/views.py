from django.shortcuts import render
from django.db.models import Q
from django.http import StreamingHttpResponse
from .models import *
# Create your views here.
def index(request):
    categories = Category.objects.all()

    context = {}
    context['categories'] = categories

    return render(request, 'index.html', context)

def categoryPage(request, slug):
    category = Category.objects.get(slug=slug)
    images = spectralImage.objects.filter(category=category).order_by('-date_created')[:6]
    for x in images:
        x.shortDescription = x.description[:130]

    context = {}
    context['images'] = images
    context['category'] = category

    return render(request, 'category.html', context)

def imageDetailPage(request, slug1, slug2):

    category = Category.objects.get(slug=slug1)
    image = spectralImage.objects.get(slug=slug2)

    context = {}
    context['category'] = category
    context['image'] = image
    return render(request, 'image.html', context)

def spectralPage(request, slug3, slug4, slug5):
    category = Category.objects.get(slug=slug3)
    image = spectralImage.objects.get(slug=slug4)
    mask = Mask.objects.all()
    tissuetype = Tissue_class.objects.all()
    # hspectral = spectralImage.objects.get(slug=slug5)

    context={}
    context['category'] =  category
    context['image'] = image
    context['mask'] = mask
    context['tissuetype'] = tissuetype
    # context['hspectral'] = hspectral
    return render(request, 'spectral.html', context)

def searchPage(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        # patient_search = Patient.objects.filter(gender__contains=searched)
        tissue_search = Tissue_class.objects.filter(class_type__icontains=searched)
        return render(request, 'search.html', {'searched':searched, 'tissue_search': tissue_search})
    else:
        return render(request, 'search.html', {})







# def download(request,path):
# 	file_path=os.path.join(settings.MEDIA_ROOT,path)
# 	if os.path.exists(file_path):
# 		with open(file_path,'rb')as fh:
# 			response=HttpResponse(fh.read(),content_type="application/adminupload")
# 			response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
# 			return response

# 	raise Http404			





