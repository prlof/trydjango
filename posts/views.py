from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def post_create(request):

    return HttpResponse("<h1>Create</h1>")

def post_detail(request):

    context = {
            "title": "Detail"
            }
    return render(request, "index.html", context)

def post_list(request):

#    if request.user.is_authenticated():
#        context = {
#                "title": "BoomFara"
#                }
#    else:
#        context = {
#                "title": "List"
#                }
    return render(request, "index.html", context)
    #return HttpResponse("<h1>List</h1>")

def post_update(request):

    return HttpResponse("<h1>Update</h1>")

def post_delete(request):

    return HttpResponse("<h1>Delete</h1>")
