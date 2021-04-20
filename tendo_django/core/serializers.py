from datetime import datetime, timedelta
from django.conf import settings

from rest_framework import serializers

from tendo_django.core.models import Hospital, Patient, Physician, Appointment, Diagnosis, FeedbackSurvey

class HospitalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hospital
    fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Patient
    fields = '__all__'

class PhysicianSerializer(serializers.ModelSerializer):
  class Meta:
    model = Physician
    fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Appointment
    fields = '__all__'
  
class DiagnosisSerializer(serializers.ModelSerializer):
  class Meta:
    model = Diagnosis
    fields = '__all__'

class FeedbackSurveySerializer(serializers.ModelSerializer):
  class Meta:
    model = FeedbackSurvey
    fields = '__all__'