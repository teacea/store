
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Group, Collection
from .forms  import ItemForm
# from .utilities import paginator


def index(request):
    template = "shop/index.html"
    
    item = Item.objects.all()[:5]
    items = Item.objects.all()
    keyword = request.GET.get("q", None)
    collection = get_object_or_404(Collection, slug='new')

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
        "collection": collection,
        "items": items,
        # "page_obj": page_obj,
        "keyword": keyword
    }

    return render(request, template, context)

def group(request, slug):
    template = "shop/group_list.html"
    group = get_object_or_404(Group, slug=slug)
    items = Item.objects.filter(group=group).all()

    title = f'group of {slug}'
    # page_obj = paginator(request, item)
    context = {
        "group": group,
        "items": items,
       # "page_obj": page_obj,
        "title": title
    }
    return render(request, template, context)

def item_detail(request, slug, item_id):
    template = "shop/item_detail.html"
    item = get_object_or_404(Item, id=item_id)
    form = ItemForm()
    context = {"item": item,
                "form": form
    }
    return render(request, template, context)

def col(request,slug):
    template = "shop/item_list.html" 
    collection = get_object_or_404(Collection, slug=slug)
    items = Item.objects.all()
    item = Item.objects.filter(collection=collection)
    context = {"item": item,
                "items": item,
                "collection":collection}
    return render(request, template, context)