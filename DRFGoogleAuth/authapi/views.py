# authapi/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import requests

@api_view(['POST'])
@permission_classes([AllowAny])
def google_authenticate(request):
    google_token = request.data.get('google_token')

    if not google_token:
        return Response({'error': 'Google token is required.'}, status=400)

    # Verify the Google token with Google's API
    google_response = requests.get(f'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token={google_token}')
    google_data = google_response.json()

    if 'error_description' in google_data:
        return Response({'error': 'Invalid Google token.'}, status=400)

    # Extract user information
    user_info = {
        'user_id': google_data['sub'],
        'email': google_data['email'],
        'name': google_data['name'],
        # Add other user info fields you need
    }

    return Response(user_info)
