from rest_framework import generics
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import SaveOfferView
from .serializers import SaveOfferSerializer


class OfferDetailAPIView(generics.RetrieveAPIView):
    queryset = SaveOfferView.objects.all()
    serializer_class = SaveOfferSerializer

Offer_Detail = OfferDetailAPIView.as_view()


@csrf_exempt 
def save_offer(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        
        content = payload.get('content')

        if content is not None:
            save_offer = SaveOfferView(content=content)
            save_offer.save()
            return JsonResponse({'status': 'success'})
        
    return JsonResponse({'status': 'error', 'message': 'Invalid request or missing content'})