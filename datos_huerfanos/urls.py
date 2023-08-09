from django.urls import path
from . import views

urlpatterns = [
    path('', views.datosh, name='datosh'),
    path('tipo_de_dato/', views.data_type, name='data_type'),
    path('tipo_de_dato/<str:data_type>/', views.get_distritos, name='get_distritos'),
    # path('tipo_de_dato/<str:data_type>', views.data_tags, name='data_tags'),
    # path('tipo_de_dato/<str:data_type>/<str:tag>/', views.view_data, name='show_data'),

]




