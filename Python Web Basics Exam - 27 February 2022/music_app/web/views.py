from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from music_app.web.forms import ProfileCreateForm, AddAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForm
from music_app.web.models import Profile, Album


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home_page(request):
    profile = get_profile()
    albums = Album.objects.all()
    if not profile:
        return redirect('create profile')
    contex = {
        'profile': profile,
        'albums': albums
    }
    return render(request, 'home-with-profile.html', contex)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ProfileCreateForm()
    context = {
        'form': form,
        'no_profile': True
    }
    return render(request, 'home-no-profile.html', context)


class AddAlbum(generic.CreateView):
    template_name = 'add-album.html'
    form_class = AddAlbumForm
    success_url = reverse_lazy('home page')


# def album_details(request, pk):
#     album = Album.objects.filter(pk=pk).get()
#     context = {
#         'album': album
#     }
#     return render(request, 'album-details.html', context)
class AlbumDetails(generic.DetailView):
    model = Album
    template_name = 'album-details.html'


class EditAlbum(generic.UpdateView):
    model = Album
    template_name = 'edit-album.html'
    form_class = EditAlbumForm
    success_url = reverse_lazy('home page')


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    form = DeleteAlbumForm(instance=album)
    if request.method == 'POST':
        album.delete()
        return redirect('home page')

    context = {
        'form': form,
        'album': album
    }
    return render(request, 'delete-album.html', context)


def profile_details(request):
    profile = get_profile()
    all_albums = len(Album.objects.all())
    context = {
        'profile': profile,
        'all_albums': all_albums
    }
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = get_profile()
    albums = Album.objects.all()
    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=profile)
        albums.delete()
        form.save()
        return redirect('home page')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile-delete.html', context)
