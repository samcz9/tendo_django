from tendo_django.core.models import FeedbackSurvey, Appointment
from tendo_django.core.serializers import FeedbackSurveySerializer
from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response
from rest_framework.decorators import action


class FeedbackSurveyViewSet(viewsets.ModelViewSet):
    """ Retreives Lists and Updates Feedback Surveys """
    queryset = FeedbackSurvey.objects.all()
    serializer_class = FeedbackSurveySerializer

    @action(detail=False, methods=['post'])
    def save_survey(self, request, *args, **kwargs):
      data = request.data
      user = request.user
      if not data["appointment_id"]:
        return Reponse(400)
      appointment = Appointment.objects.get(id=data["appointment_id"])
      survey = FeedbackSurvey.objects.create(
        appointment=appointment,
        physician_rating=data["physician_rating"],
        understanding=data["understanding"],
        understanding_notes=data["understanding_notes"],
        patient_expression=data["patient_expression"]
      )
      return Response(200)

    