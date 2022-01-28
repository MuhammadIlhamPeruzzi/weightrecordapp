from django.shortcuts import render, redirect  
from weight.forms import WeightForm  
from weight.models import WeightRecord

# Create your views here.  
def create(request):  
    if request.method == "POST":  
        form = WeightForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/list')  
            except:  
                pass
    else:  
        form = WeightForm()  
    return render(request,'create.html',{'form':form})

def list(request):  
    weightRecords = WeightRecord.objects.all()  
    return render(request,"list.html",{'weightRecords':weightRecords})

def edit(request, id):  
    weightRecord = WeightRecord.objects.get(id=id)
    return render(request,'edit.html', {'weightRecord':weightRecord})

def update(request, id):  
    weightRecord = WeightRecord.objects.get(id=id) 
    form = WeightForm(request.POST, instance = weightRecord)

    if form.is_valid():  
        form.save()  
        return redirect("/list")

    return render(request, 'edit.html', {'employee': employee})

def delete(request, id):  
    weightRecord = WeightRecord.objects.get(id=id)
    weightRecord.delete()  
    return redirect("/list")
