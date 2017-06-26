from django.core import serializers
from django.http import HttpResponse
import json

from meat.models import Suburb

class DataApi:
    def suburbs(request):
        partial_suburb = request.GET.get('partial', '')
        response_list = []
        partial_suburb = partial_suburb.strip()
        if len(partial_suburb) > 0:
            suburb_list = Suburb.objects.filter(name__icontains=partial_suburb).order_by('name')[:10]
        else:
            suburb_list = Suburb.objects.all().order_by('name')[:10]
        for single_suburb in suburb_list:
            combine = single_suburb.name + ', ' + single_suburb.state + ', ' + single_suburb.postcode
            response_list.append({ "postcode": single_suburb.postcode , "display": combine , "suburb" : single_suburb.name} )
        output = json.dumps(response_list)
        return HttpResponse(output, content_type='application/json')
