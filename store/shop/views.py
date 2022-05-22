
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Group
# from .utilities import paginator


def index(request):
    template = "shop/index.html"
    title = "Последние записи"
    item = Item.objects.all()
    items = Item.objects.all()
    keyword = request.GET.get("q", None)

    if keyword:
        item = list((Item.objects.select_related('group')
                      .filter(name__contains=keyword)))
        if item:
            title = "Found:"
            item = (Item.objects.select_related('author', 'group')
                     .filter(text__contains=keyword))
        else:
            title = "Sorry we don't have it. :C"
    # page_obj = paginator(request, item)
    context = {
        "item": item,
        "title": title,
        "items": item,
        # "page_obj": page_obj,
        "keyword": keyword
    }

    return render(request, template, context)

def group(request, slug):
    template = "shop/item_list.html"
    group = get_object_or_404(Group, slug=slug)
    item = Item.objects.filter(group=group).all()
    title = f'group of {slug}'
    # page_obj = paginator(request, item)
    context = {
        "group": group,
       # "page_obj": page_obj,
        "title": title
    }
    return render(request, template, context)

def item_detail(request, post_id):
    template = "shop/item_detail.html"
    item = get_object_or_404(Item, id=post_id)
    context = {"item": item}
    return render(request, template, context)