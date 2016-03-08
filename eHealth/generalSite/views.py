from django.shortcuts import render

# Create your views here.
def index(request):
    context_dictionary ={}
    #context_dictionary['value']= something

    return render(request, 'generalSite/index.html',context_dictionary)