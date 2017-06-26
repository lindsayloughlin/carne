from django.shortcuts import render
from meat.models import Supplier

# Create your views here.


def meat_land_page(request):
    return render(request, 'meat/landing.html', {'hello': 'world'})


def supplier_detail_page(request, supplier_name):
    results = {}
    print(supplier_name)

    results['supplier_name'] = supplier_name
    object_list = Supplier.objects.filter(name=supplier_name)
    if object_list.count() == 1:
        results['supplier_model'] = object_list[0]
    else:
        results['missing'] = True

    return render(request, 'meat/supplier_detail.html', results)
