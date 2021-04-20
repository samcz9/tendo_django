from django.contrib import admin
from tendo_django.core.models import Hospital, Patient, Physician, Appointment, Diagnosis, FeedbackSurvey

class HospitalAdmin(admin.ModelAdmin):
  list_display = ('name',)

class PatientAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name')

class PhysicianAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name')

class AppointmentAdmin(admin.ModelAdmin):
  list_display = ('patient', 'physician', 'time_start')

class DiagnosisAdmin(admin.ModelAdmin):
  list_display = ('name',)

class FeedbackSurveyAdmin(admin.ModelAdmin):
  list_display = ('appointment',)

admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Physician, PhysicianAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Diagnosis, DiagnosisAdmin)
admin.site.register(FeedbackSurvey, FeedbackSurveyAdmin)
