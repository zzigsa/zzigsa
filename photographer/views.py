from django.shortcuts import render, get_object_of_404, redirect
from django.utils import timezone

from .models import ProductRegistration
from .models import PhotographerProfile
from .forms import UploadForm

# Create your views here.
def upload(request):
    # product = ProductRegistration()
    # product.title = request.GET['title']
    # product.summary = request.GET['summary']
    # product.detail = request.GET['detail']
    # product.pub_date = timezone.datetime.now()
    # product.save()
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    return render(request, '.html', locals())
    # return redirect('/products/' + str(product.id))


def register_photographer(request):
    photographer = PhotographerProfile()
    photographer.registration_date = timezone.datetime.now()
    photographer.name = request.GET['name']
    # photographer.profile_photo = 
    photographer.introduction = request.GET['introduction']