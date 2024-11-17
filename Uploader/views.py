from django.shortcuts import render,get_object_or_404,redirect
from .models import *


# Create your views here.
def home(request):
   
    if request.method == 'POST':
        data=request.POST
        image= request.FILES['image']
        title=data.get('title')
        cap_title=title.upper()
        description=data.get('description')
        print(image,title,description)
        print('working')
        data=user_post.objects.create(image=image,title=cap_title,description=description)
        data.save()

        return redirect('/home/')
    value=user_post.objects.all()
    context={'values':value}
    return render(request,'home.html',context)