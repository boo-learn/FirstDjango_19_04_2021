from django.shortcuts import render, HttpResponse, Http404
from MainApp.models import Item


# Create your views here.
def main(request):
    return render(request, 'index.html')


def item(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404
    context = {
        "item": item
    }
    return render(request, 'item.html', context)


def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, 'items_list.html', context)
