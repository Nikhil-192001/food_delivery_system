from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pricing
from .serializers import PricingSerializer

@api_view(['GET'])
def delivery_cost(request):
    if request.method == 'GET':
        zone = request.data.get('zone')
        organization_id = request.data.get('organization_id')
        total_distance = float(request.data.get('total_distance', 0))
        item_type = request.data.get('item_type')
        print('zone: ',zone,'organization_id: ',organization_id,'total_distance: ',total_distance,'item_type: ',item_type)

        try:
            pricing = Pricing.objects.get(organization_id=organization_id, item__type=item_type, zone=zone)
        except Pricing.DoesNotExist:
            return Response({'error': 'Pricing not found'}, status=404)

        base_distance = pricing.base_distance_in_km
        km_price = pricing.km_price
        fix_price = pricing.fix_price
        total_price = fix_price
        print(base_distance,km_price,fix_price,total_price,)

        if total_distance > base_distance:
             total_price += km_price * (total_distance - base_distance)

        return Response({'total_price': total_price})
