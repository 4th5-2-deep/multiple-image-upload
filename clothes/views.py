from django.shortcuts import render, redirect
from .forms import MultipleImageForm
from .models import Clothes


def index(request):
    clothes_list = Clothes.objects.all()
    context = {
        'clothes_list': clothes_list,
    }
    return render(request, 'clothes/index.html', context)


def new(request):
    if request.method == 'POST':
        form = MultipleImageForm(request.POST, request.FILES)
        if form.is_valid():
            category_id = request.POST.get('category')
            images = request.FILES.getlist('images')
            for image in images:
                Clothes.objects.create(category_id=category_id, image=image)
            return redirect('clothes:index')
    else:
        form = MultipleImageForm()    
    context = {
        'form': form, 
    }
    return render(request, 'clothes/new.html', context)
