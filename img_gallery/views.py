from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import *
from . forms import *

# Create your views here.
def img_gallery(request):
    return render(request, 'img_gallery/images.html')


def upload_image(request):
    name = request.POST.get('my_name')
    image = request.FILES.get('image_file')
    Images.objects.create(image=image, name=name)
    return redirect(display_image)


def success(request):
    return HttpResponse('Successful upload!')


def display_image(request):
    if request.method == 'GET':
        images = Images.objects.all()
        return render(request, 'img_gallery/images.html', {'images': images})


def delete_image(request, id):
    img = get_object_or_404(Images, pk=id)

    if request.method == 'POST':
        img.delete()
    return redirect(display_image)


def image_detail(request, id):
    img = get_object_or_404(Images, pk=id)

    if img:
        context = {'img': img}
        return render(request, 'img_gallery/image_detail.html', context)

