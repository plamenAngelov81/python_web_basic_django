from django.urls import path, include

from car_collection_app.web.views import index, profile_details, profile_edit, profile_delete, profile_create, \
    car_create, car_details, car_edit, car_delete, catalogue

urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
        path('create/', profile_create, name='profile create')
    ])),
    path('car/create/', car_create, name='car create'),
    path('car/<int:pk>/', include([
        path('details/', car_details, name='car details'),
        path('delete/', car_delete, name='car delete'),
        path('edit/', car_edit, name='car edit'),
    ]))
]
