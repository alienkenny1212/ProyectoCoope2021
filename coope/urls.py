from django.urls import path
from . import views
urlpatterns = [

    path('detPersona/<int:pk>/', views.post_detail_persona, name='post_detail_persona'),
    path('newPersona', views.post_new_persona, name='post_new_persona'),
    path('Personas', views.post_list_personas, name='post_list_personas'),

    path('', views.post_list_Socios, name='post_list_Socios'),
    path('Socios', views.post_list_Socios, name='post_list_Socios'),

    path('detSocio/<int:pk>/', views.post_detail_Socios, name='post_detail_socios'),
    path('newSocio', views.post_new_Socios, name='post_new_socios'),
    path('detSocios/<int:pk>/edit/', views.post_edit_socios, name='post_edit_socios'),
    path('deleteSocios/<int:pk>/', views.post_delete_socios, name='post_delete_socios'),
]