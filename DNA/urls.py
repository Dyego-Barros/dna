from django.urls import path, include
from . import views
from DNA_AUTOMATION import settings
from django.conf.urls.static import static

app_name = 'DNA'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('login/submit', views.login_submit, name='login-dashboard'),
    path('dashboard/', views.dashboard, name='dasboard'),
    path('dashboard/register/', views.register, name='register'),
    path('dashboard/register/submit', views.set_machine, name='set_machine'),
    path('dashboard/report/', views.listreport, name='report'),
    path('dashboard/report/machine_view/', views.machine_view, name='machine_view'), 
    path('dashboard/report/csv/', views.export_machine_csv, name='export_csv'),  
    path('dashboard/report/all_csv/', views.export_allMachine_csv, name='export_all_csv'), 
    path('dashboard/report/machine_view/submit', views.machine_view_submit, name='machine_view_submit'),  
    path('dashboard/delete/<int:id>', views.delete, name="delete"),
    path('logout/', views.logout_user, name='logout-user'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)