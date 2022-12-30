from django.urls import path, include

from retake_exam_21_12_2022.web.views import home_page, catalogue, profile_create, profile_details, profile_edit, \
    profile_delete, plant_create, plant_details, plant_edit, plant_delete

urlpatterns = [
    path('', home_page, name='home page'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', profile_create, name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ])),
    path('create/', plant_create, name='plant create'),
    path('details/<int:pk>/', plant_details, name='plant details'),
    path('edit/<int:pk>/', plant_edit, name='plant edit'),
    path('delete/<int:pk>/', plant_delete, name='plant delete')
]