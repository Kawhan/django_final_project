from . import views
from django.urls import path


urlpatterns = [
    path('view-missoes', views.viewMissoes, name='view_missoes'),
    path('missoes-create', views.missoesCreate, name='create_missoes'),
    path('<int:missao_id>/missoes-edit', views.missoesEdit, name='missoes_edit'),
    path('<int:missao_id>/delete-missao', views.missoesDelete, name='missoes_delete')
]
