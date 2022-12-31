from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from my_games_app.web.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, ProfileEditForm, \
    DeleteProfileForm
from my_games_app.web.models import Profile, Game


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


class CreateProfile(generic.CreateView):
    form_class = CreateProfileForm
    template_name = 'create-profile.html'
    success_url = reverse_lazy('home-page')


class Dashboard(generic.TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = Game.objects.all()
        return context


class CreateGame(generic.CreateView):
    form_class = CreateGameForm
    template_name = 'create-game.html'
    success_url = reverse_lazy('dashboard')


class DetailsGame(generic.DetailView):
    model = Game
    template_name = 'details-game.html'


class EditGame(generic.UpdateView):
    model = Game
    template_name = 'edit-game.html'
    form_class = EditGameForm
    success_url = reverse_lazy('dashboard')


def delete_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    form = DeleteGameForm(instance=game)
    if request.method == 'POST':
        game.delete()
        return redirect('dashboard')

    context = {
        'form': form,
        'game': game
    }
    return render(request, 'delete-game.html', context)


def details_profile(request):
    user = get_profile()
    games = Game.objects.all()
    total_games = len(games)
    average_rating = 0
    if total_games > 0:
        average_rating = sum(game.rating for game in games) / total_games
    context = {
        'user': user,
        'total_games': total_games,
        'average_rating': average_rating
    }
    return render(request, 'details-profile.html', context)


def edit_profile(request):
    user = get_profile()
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('details-profile')
    else:
        form = ProfileEditForm(instance=user)
    context = {
        'form': form
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    user = get_profile()
    games = Game.objects.all()
    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=user)
        games.delete()
        form.save()
        return redirect('home-page')
    else:
        form = DeleteProfileForm(instance=user)
    context = {
        'form': form,
        'profile': user,
    }
    return render(request, 'delete-profile.html', context)
