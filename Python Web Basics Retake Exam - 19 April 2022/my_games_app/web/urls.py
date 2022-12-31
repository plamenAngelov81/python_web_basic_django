from django.urls import path, include

from my_games_app.web.views import home_page, Dashboard, CreateProfile, edit_profile, details_profile, \
    delete_profile, CreateGame, DetailsGame, EditGame, delete_game

urlpatterns = [
    path('', home_page, name='home-page'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('profile/', include([
        path('create/', CreateProfile.as_view(), name='create-profile'),
        path('edit/', edit_profile, name='edit-profile'),
        path('details/', details_profile, name='details-profile'),
        path('delete', delete_profile, name='delete-profile'),
    ])),
    path('game/', include([
        path('create/', CreateGame.as_view(), name='create-game'),
        path('details/<int:pk>/', DetailsGame.as_view(), name='details-game'),
        path('edit/<int:pk>/', EditGame.as_view(), name='edit-game'),
        path('delete/<int:pk>/', delete_game, name='delete-game'),
    ]))
]
