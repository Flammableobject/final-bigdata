from django.shortcuts import render
from myapp.forms import CustomerForm
from myapp.models import Customer
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def home(request):
    context={
        'user':request.user,
        'toker':'mysecret'   
    }
    return render(request, 'home.html',context=context)

def profile(request):
    instance = get_object_or_404(Customer, user=request.user)
    form = CustomerForm(request.POST or None, instance = instance)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        context = {
              'form':form,
              'user':request.user
              }
    return render(request, 'profile.html', context)
