from rest_framework.test import APIRequestFactory

# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()
request = factory.post('/surveys/save_survey', 
  json.dumps({
    'appointment': None, 
    'physician_rating': 7, 
    'understanding': "yes", 
    "understanding_notes": None,
    "patient_expression": "Very sad"
    }), content_type='application/json')

assert request.status_code == 400

