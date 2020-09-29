from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

# Create your views here.
from .models import Todo

def index_view(request):
    #return HttpResponse(" Welcome to index page")
    todo_items = Todo.objects.all().order_by("-added_date")

    context = {"todo_items" :todo_items}
    return render(request, 'to_do_list_app/index.html',context)


def add_data_view(request):
    current_date_object = timezone.now()
    text_object = request.POST["content"]
    add_data_object = Todo.objects.create(added_date= current_date_object, text= text_object)
    print(add_data_object)
    print(add_data_object.id)
    count_object = Todo.objects.all().count()
    print(count_object)


    #return render(request, 'to_do_list_app/index.html', )
    return HttpResponseRedirect(reverse('to_do_list_app:index_view'))



def delete_data_view(request,delete_item_id):
    obj = Todo.objects.get(id=delete_item_id).delete()
    """if request.method == "post":
        obj.delete()"""
    return HttpResponseRedirect(reverse("to_do_list_app:index_view"))

def update_data_view(request, update_item_id):
    obj = Todo.objects.get(id=update_item_id)
    print(obj)
    context = {"obj" : obj}

    return render(request,"to_do_list_app/update.html",context)








"""def delete_data_view(request, id):
    Todo.objects.get(id=id).delete()


    return HttpResponseRedirect(reverse('to_do_list_app:index_view'))"""



"""def delete_data_view(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect(reverse('to_do_list_app:index_view'), args=("todo_id.id"))
"""
""" todo_id = Todo.objects.get(id=todo_id)
    print(todo_id)
    print(todo_id.id)
    todo_id.delete()
    context = {"todo_id":todo_id}

    return render(request, 'to_do_list_app/delete.html',context)"""


