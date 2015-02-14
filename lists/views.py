from django.shortcuts import render, redirect

from lists.models import Item

# Create your views here.

def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST.get('item_text', '')
        Item.objects.create(text=new_item_text)
        return redirect('/lists/the-unique-list-id/')

    items = Item.objects.all()
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
