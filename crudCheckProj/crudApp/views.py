from django.shortcuts import render,redirect
from .models import Details
from .forms import detailsform

# Create your views here.
def index(request):
    return render(request,'crudApp/index.html')

def create(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        obj=Details.objects.create(name=name,age=age,address=address)
        obj.save()
        return redirect('/')

def retrieve(request):
    details=Details.objects.all()
    return render(request,'crudApp/retrieve.html',{'details':details})

def edit(request,id):

    object=Details.objects.get(id=id)
    return render(request,'crudApp/edit.html',{'object':object})

def update(request,id):
    object=Details.objects.get(id=id)
    form=detailsform(request.POST,instance=object)
    if form.is_valid:
        form.save()
        object=Details.objects.all()
        return redirect('/')

def delete(request,id):
        Details.objects.get(id=id).delete()
        return redirect('/')
