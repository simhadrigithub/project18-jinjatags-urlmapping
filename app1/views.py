from django.shortcuts import render


# Create your views here.
d1={'family':'relation','members':5,'names':['murugest','drakshamma','simhadri','lavanya','chinna']}
def family(request):
    
    return render (request,'family.html',context=d1)

d2={'hobbies':['muru:watching movies','draksha:coocking foods','lavanya:learning coocking','simhadri:typing','chinna:kabadi']}
def hobbies(request):
    return render(request,'hobbies.html',context=d2)