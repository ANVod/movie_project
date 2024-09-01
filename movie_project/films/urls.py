from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/', include('films.urls')),
    path('', views.home, name='home'),  # Главная страница
]
