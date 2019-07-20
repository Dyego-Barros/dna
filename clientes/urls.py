from django.urls import path, include
from . import views
from DNA_AUTOMATION import settings
from django.conf.urls.static import static

app_name= 'clientes'

urlpatterns = [
    path('register_Client/', views.register_client, name="client"),
    path('register_Client/submit', views.register_client_submit, name="client_submit"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)