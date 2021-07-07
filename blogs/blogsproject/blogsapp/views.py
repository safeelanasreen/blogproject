from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import blogs
from.forms import ModeForm

# Create your views here.
def demo(request):
    post=blogs.objects.all()
    return render(request,"home.html",{'posts':post})
def detail(request,blogs_id):
    post1=blogs.objects.get(id=blogs_id)
    return render(request,"detail.html",{'post':post1})
def add_blogs(request):
    if request.method=='POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        s=blogs(name=name,desc=desc,img=img)
        s.save()
        print("blogs added")
    return render(request,"add_blogs.html")
def update(request,id):
    obj=blogs.objects.get(id=id)
    form=ModeForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'obj':obj})
def delete(request,id):
    if request.method=='POST':
        obj=blogs.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')
