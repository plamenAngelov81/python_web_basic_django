from django.contrib import admin

from my_games_app.web.models import Profile, Game


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class GamesAdmin(admin.ModelAdmin):
    pass
