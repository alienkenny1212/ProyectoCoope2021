from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list_Socios, name='post_list_Socios'),
    path('detSocio/<int:pk>/', views.post_detail_Socios, name='post_detail_socios'),
    path('newSocio', views.post_new_Socios, name='post_new_socios'),
      path('detSocios/<int:pk>/edit/', views.post_edit_socios, name='post_edit_socios'),
]