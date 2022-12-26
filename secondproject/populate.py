import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','secondproject.settings')

import django
django.setup()

import random
from second_app.models import Userdata

from faker import Faker

fakegen = Faker()



def populate(N=5):
    for i in range(N):

        fakename = fakegen.first_name()
        fakelastname = fakegen.last_name()
        fakeemail = fakegen.email()
        userdata = Userdata.objects.get_or_create(fname=fakename,lname=fakelastname,email=fakeemail)[0]

if __name__ =='__main__':
    populate(20)