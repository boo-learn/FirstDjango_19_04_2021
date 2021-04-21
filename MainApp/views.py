from django.shortcuts import render, HttpResponse

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 3, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 4, "name": "Картофель фри", "quantity": 0},
    {"id": 5, "name": "Кепка", "quantity": 124},
]


# Create your views here.
def main(request):
    return render(request, 'index.html')


def item(request, id):
    context = {}
    for item in items:
        if item["id"] == id:
            context["item"] = item
            return render(request, 'item.html', context)

    return HttpResponse(f"Товар с id={id} не найден")


def items_list(request):
    context = {
        "items": items
    }
    return render(request, 'items_list.html', context)
