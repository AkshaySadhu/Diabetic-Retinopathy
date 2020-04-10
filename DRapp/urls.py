from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add', views.add),
    path('insert', views.insert),
    path('search', views.search),
    path('list', views.get_all),
    path('pendingDR', views.pending),
    path('addDR/<int:id>', views.dr),
    path('addDR/<int:id>/predict', views.dr),
]
