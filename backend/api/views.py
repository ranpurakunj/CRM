import json
# from django.http import JsonResponse
from django.forms.models import model_to_dict

from Profile.models import Profile
from Profile.serializers import ProfileSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view




@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer=ProfileSerializer(data= request.data)
    if serializer.is_valid():
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not a good data"}, status=404)