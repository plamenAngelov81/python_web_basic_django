from django.shortcuts import render, redirect

from car_collection_app.web.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, \
    ProfileEditForm, DeleteProfileForm
from car_collection_app.web.models import Profile, Car


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def index(request):
    user = get_profile()
    context = {
        'user': user
    }
    return render(request, 'index.html', context)


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
    return render(request, 'profile-create.html', context)


def catalogue(request):
    user = get_profile()
    cars = Car.objects.all()
    total_cars = len(cars)
    context = {
        'cars': cars,
        'total_cars': total_cars,
        'user': user
    }
    return render(request, 'catalogue.html', context)


def car_create(request):
    if request.method == 'POST':
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarCreateForm()
    context = {
        'form': form
    }
    return render(request, 'car-create.html', context)


def car_details(request, pk):
    car = Car.objects.filter(pk=pk).get()
    context = {
        'car': car
    }
    return render(request, 'car-details.html', context)


def car_edit(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == "POST":
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarEditForm(instance=car)
    context = {
        'car': car,
        'form': form
    }
    return render(request, 'car-edit.html', context)


def car_delete(request, pk):
    car = Car.objects.filter(pk=pk).get()
    form = CarDeleteForm(instance=car)
    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': car
    }

    return render(request, 'car-delete.html', context)


def profile_details(request):
    user = get_profile()
    cars = Car.objects.all()
    total_car_price = 0
    for car in cars:
        total_car_price += car.price
    context = {
        'user': user,
        'total_car_price': total_car_price
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
    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    user = get_profile()
    cars = Car.objects.all()
    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=user)
        cars.delete()
        form.save()
        return redirect('index')
    else:
        form = DeleteProfileForm(instance=user)
    context = {
        'form': form,
        'profile': user,
    }
    return render(request, 'profile-delete.html', context)
