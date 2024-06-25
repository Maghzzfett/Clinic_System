from django.urls import path # type: ignore
from .views import HomePage,PatientsPage,SchedulesPage,AppointmentsPage,UsersPage

urlpatterns = [
    path('',HomePage.as_view(), name='home'),
     path('patients/',PatientsPage.as_view(), name='patients'),
      path('schedules/',SchedulesPage.as_view(), name='schedules'),
       path('appointments/',AppointmentsPage.as_view(), name='appointments'),
        path('users/',UsersPage.as_view(), name='users')
]