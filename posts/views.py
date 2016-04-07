from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse

# Create your views here.

from .models import Post
def post_create(request):

    return HttpResponse("<h1>Create</h1>")

def post_detail(request):

    #instance = Post.objects.get(id=66)
    instance = get_object_or_404(Post, title = "Hi")
    context = {
            "title": "Detail"
            }
    return render(request, "index.html", context)

def post_list(request):

    queryset = Post.objects.all()
    context = {
            "object_list" : queryset,
            "title" : "List"
            }

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
