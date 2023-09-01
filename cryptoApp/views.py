from django.shortcuts import render, HttpResponse
from .models import ItemRegist, ContentTable, blogTable
from .custom_templates import get_specific_link

# Create your views here.



def content(request):
    querySet = blogTable.objects.all()


    context = {
        'queries' : querySet
    }

    return render(request, 'homepage.html', context)


def linkContent(request):
    get_specific_link(blogTable, '')


    


