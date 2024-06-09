"""from django.shortcuts import render,redirect
from . forms import CustomUserCreationForm



def signup(request):
    form=CustomUserCreationForm()
    context={'form':form}
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'registration/register.html',context)

# Create your views here."""
