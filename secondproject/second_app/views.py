from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from second_app.models import Userdata
from second_app.forms import myForm
def index(request):
    mydict = {'helpme':'help is on the way '}
    return render(request,r'help\help.html',mydict)

def presentdata(request):
    userdata_objects= Userdata.objects.order_by('fname')
    data_dict = {'dataproj':userdata_objects}
    return render(request,r'presentdata\presentdata.html',data_dict)

def formpagereq(request):
    f = myForm(request.POST)
    if f.is_valid():
        f.save()
    return render(request,'forms/forms.html',{'form':f})