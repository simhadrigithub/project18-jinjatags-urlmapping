from django.shortcuts import render

# Create your views here.
d1={'schools':['zphs schools','mandal schools','private schools','govnt schools']}
def schools(request):
    return render(request,'schools.html',context=d1)

d2={'colleges':['govn college','private college','university college','ambedkar college','svu university college','jntu college']}
def colleges(request):
    return render(request,'colleges.html',context=d2)

d3={'a':20,'b':40,'c':50}
def highest(request):
    return render(request,'highest-value.html',context=d3)


