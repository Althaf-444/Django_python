from django.shortcuts import render , redirect
from form import Contect_form

# Create your views here.
def contect(request):
    return render(request , 'first_app/home.html')

def contect_viwe(request):
    if request.method == 'POST':
       form =  Contect_form(request.POST)
       if form.is_valid():
           form.send_email()
           return redirect('content-success')
    else :
       form = Contect_form()
       context = {'form':form}
       return render(request , 'first_app/contect.html', context)
    
def contect_success(request):
    return render(request , 'first_app/contect_success.html')
