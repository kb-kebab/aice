#from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from saveoffer.models import SaveOfferView
from saveoffer.serializers import SaveOfferSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):

   serializer=SaveOfferSerializer(data=request.data)
   if serializer.is_valid():

     # isinstance= serializer.save()
      print(serializer.data)
      return Response(serializer.data)
