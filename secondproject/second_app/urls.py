from django.conf.urls import url
from second_app import views

urlpatterns = [
    url(r'^data\/',views.presentdata,name='data'),
    url(r'^form\/',views.formpagereq,name='formdata')
]