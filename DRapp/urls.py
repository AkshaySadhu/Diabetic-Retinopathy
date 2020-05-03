from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.prelogin),
    path('home/', views.home),
    path('add', views.add),
    path('insert', views.insert),
    path('search', views.search),
    path('list', views.get_all),
    path('addDR/<int:id>', views.dr),
    path('addDR/<int:id>/predict', views.dr),
    path('login', views.loggingin),
    path('logout', views.user_logout)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
