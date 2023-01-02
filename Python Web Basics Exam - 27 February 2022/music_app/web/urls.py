from django.urls import path, include

from music_app.web.views import home_page, AddAlbum, AlbumDetails, EditAlbum, delete_album, profile_details, \
    profile_delete, create_profile

urlpatterns = [
    path('', home_page, name='home page'),
    path('album/', include([
        path('add/', AddAlbum.as_view(), name='add album'),
        path('details/<int:pk>/', AlbumDetails.as_view(), name='album details'),
        path('edit/<int:pk>/', EditAlbum.as_view(), name='edit album'),
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ])),
    path('profile/', include([
        path('details/', profile_details, name='profile details'),
        path('delete/', profile_delete, name='profile delete'),
        path('create/', create_profile, name='create profile')
    ]))
]
