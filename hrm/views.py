from django.shortcuts import render
from hrm.models import Staff
def staffsubmit(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address= request.POST.get('address', '')
        sex= request.POST.get('sex', '')
        age= request.POST.get('age', '')
        birthday= request.POST.get('birthday', '')
        tel= request.POST.get('tel', '')
        staff=Staff()
        staff.name=name
        staff.email=email
        staff.address=address
        staff.sex=sex
        staff.age=age
        staff.birthday=birthday
        staff.tel=tel
        staff.save()
    return render(request,'staffsubmit.html')