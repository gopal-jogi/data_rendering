from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='this my thing assumption'
    d={ 'a':data}
    return render(request,'data_render.html',context=d)

def login(request):
    
    d={ 'b':'akshay', 'c':'jogi'}
    return render(request,'login.html',context=d)