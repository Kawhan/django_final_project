from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('fichas',views.viewFichas, name="fichas-view"),
    path('create-fichas', views.createFichas, name="fichas_create"),
    path('<int:id_fichas>/view-ficha',views.infoFichas, name="fichas_view"),
    path('<int:id_fichas>/delete-ficha',views.deleteFicha, name="fichas_delete"),
    path('<int:id_fichas>/change-ficha',views.changeFicha, name="change_ficha"),
    path('search', views.search, name="search"),
]
