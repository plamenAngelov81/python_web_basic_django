from django.shortcuts import render, redirect

from retake_exam_21_12_2022.web.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, \
    ProfileEditForm, DeleteProfileForm
from retake_exam_21_12_2022.web.models import Profile, Plant


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home_page(request):
    user = get_profile()

    context = {
        'user': user
    }
    return render(request, 'home-page.html', context)


def profile_create(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileCreateForm()
    context = {
        'form': form
    }
    return render(request, 'create-profile.html', context)


def catalogue(request):
    user = get_profile()
    plants = Plant.objects.all()

    context = {
        'user': user,
        'plants': plants
    }
    return render(request, 'catalogue.html', context)


def plant_create(request):
    if request.method == 'POST':
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = PlantCreateForm()
    context = {
        'form': form
    }
    return render(request, 'create-plant.html', context)


def plant_details(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    context = {
        'plant': plant
    }
    return render(request, 'plant-details.html', context)


def plant_edit(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == "POST":
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = PlantEditForm(instance=plant)
    context = {
        'plant': plant,
        'form': form
    }
    return render(request, 'edit-plant.html', context)


def plant_delete(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    form = PlantDeleteForm(instance=plant)
    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant
    }
    return render(request, 'delete-plant.html', context)


def profile_details(request):
    user = get_profile()
    plants = Plant.objects.all()
    stars = len(plants)
    context = {
        'user': user,
        'stars': stars
    }
    return render(request, 'profile-details.html', context)


def profile_edit(request):
    user = get_profile()
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileEditForm(instance=user)
    context = {
        'form': form,
        'user': user
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    user = get_profile()
    plants = Plant.objects.all()

    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=user)
        plants.delete()
        form.save()
        return redirect('home page')
    else:
        form = DeleteProfileForm(instance=user)

    context = {
        'form': form,
        'profile': user,
    }
    return render(request, 'delete-profile.html', context)


