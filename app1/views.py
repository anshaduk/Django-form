from django.shortcuts import render
from .forms import student

# Create your views here.
def addFunc(req):
    if req.method=='POST':
        form=student(req.POST)
        if form.is_valid():
            form.save()
    else:
        form=student()
    return render(req,'add.html',{'form':form})
