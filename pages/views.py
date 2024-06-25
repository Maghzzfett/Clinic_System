from django.views.generic import TemplateView # type: ignore

# Create your views here.

class HomePage(TemplateView):
    template_name= 'home.html'

class PatientsPage(TemplateView):
    template_name= 'patients.html'

class SchedulesPage(TemplateView):
    template_name='schedules.html'

class AppointmentsPage(TemplateView):
    template_name='appointments.html'

class UsersPage(TemplateView):
    template_name='users.html'