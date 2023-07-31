from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
d1={'occupation':['murugesh:contractor','drakshamma:house wife','simhadri:studying mca','chinna:studying 10th','lavanya:her also coocking food in house']}
def family1(request):
    return render(request,'family1.html',context=d1)
def nature(request):
    return HttpResponse("hello beautiful  nature")