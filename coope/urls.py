from django.urls import path
from . import views
urlpatterns = [

    path('', views.menu_principal, name='menu_principal'),

#PERSONAS
    path('Personas', views.post_list_personas, name='post_list_personas'),
    path('detPersona/<int:pk>/', views.post_detail_persona, name='post_detail_persona'),
    path('newPersona', views.post_new_persona, name='post_new_persona'),
    path('detPersona/<int:pk>/edit/', views.post_edit_persona, name='post_edit_persona'),
    path('deletePersona/<int:pk>/', views.post_delete_persona, name='post_delete_persona'),

#SOCIOS
    path('Socios', views.post_list_Socios, name='post_list_Socios'),
    path('detSocio/<int:pk>/', views.post_detail_Socios, name='post_detail_socios'),
    path('newSocio', views.post_new_Socios, name='post_new_socios'),
    path('detSocios/<int:pk>/edit/', views.post_edit_socios, name='post_edit_socios'),
    path('deleteSocios/<int:pk>/', views.post_delete_socios, name='post_delete_socios'),

#NO TOCAR NADA DE AQUÍ PARA ARRIBA

#EMPLEADOS
    path('Empleados', views.post_list_empleado, name='post_list_empleado'),
    path('detEmpleado/<int:pk>/', views.post_detail_empleado, name='post_detail_empleado'),
    path('newEmpleado', views.post_new_empleado, name='post_new_empleado'),
    path('detEmpleados/<int:pk>/edit/', views.post_edit_empleado, name='post_edit_empleado'),
    path('deleteEmpleados/<int:pk>/', views.post_delete_empleado, name='post_delete_empleado'),


#TECNICOS
    path('Tecnicos', views.post_list_tecnico, name='post_list_tecnico'),
    path('detTecnico/<int:pk>/', views.post_detail_tecnico, name='post_detail_tecnico'),
    path('newTecnico', views.post_new_tecnico, name='post_new_tecnico'),
    path('detTecnicos/<int:pk>/edit/', views.post_edit_tecnico, name='post_edit_tecnico'),
    path('deleteTecnicos/<int:pk>/', views.post_delete_tecnico, name='post_delete_tecnico'),
#INSPECTORES
path('Inspector', views.post_list_Inspector, name='post_list_Inspector'),
    path('detInspector/<int:pk>/', views.post_detail_Inspector, name='post_detail_Inspector'),
    path('newInspector', views.post_new_Inspector, name='post_new_Inspector'),
    path('detInspector/<int:pk>/edit/', views.post_edit_Inspector, name='post_edit_Inspector'),
    path('deleteInspector/<int:pk>/', views.post_delete_Inspector, name='post_delete_Inspector'),
]