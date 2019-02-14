from django.shortcuts import render, redirect 
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    all_items = List.objects.all().order_by('date')

    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been successfully added to your TODO list!'))
        else:
            messages.success(request, ('Oops! You can\'t add a blank item to your TODO list.'))
        
    return render(request, 'home.html', {'all_items': all_items})

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.isCompleted = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.isCompleted = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Your activity has been successfully edited!'))
        else:
            messages.success(request, form.errors)
        
        return redirect("home")
    
    else:
        all_items = List.objects.all().order_by('date')
        messages.success(request, ('EDITING A RECORD'))
        return render(request, 'edit.html', {'all_items': all_items, 'edit_item_id': list_id})

def delete(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        item.delete()
        messages.success(request, ('Item has been successfully deleted from your TODO list.'))
        return redirect('home')
    else:
        all_items = List.objects.all().order_by('date')
        messages.success(request, ('DELETING A RECORD'))
        return render(request, 'delete.html', {'all_items': all_items, 'delete_item_id': list_id})
