from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from website.models import Record
from .forms import SignUpForm, AddRecordForm
from .models import Record
from django import forms
# Create your views here.
def home (request):
    # templates = loader.get_template('home.html')
    # return HttpResponse(templates.render())
    # return render(request,'home.html',{})
    # if person is logged in or not 
    # this porsion is for showing the database the user that has created
    records = Record.objects.all() # grabing everything from the database and post it to the page 
     
    # //
    if request.method == 'POST':
        username = request.POST['username']  # username is the name of the input field in the html file
        password = request.POST['password'] # password is the name of the input field in the html file
    # authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
         login (request, user)
         messages.success(request, f'Welcome {username} !!')
         return redirect('home')
        else: 
         messages.success(request, f'Invalid Credentials !!')
         return redirect('home')
    else:
     return render(request,'home.html',{'records':records})
        
        
        
        
# def login_user (request):
#     pass


def logout_user (request):
    # making logout user function 
    # calling logout function which is imported 
    logout (request)
    messages.success(request, f'You have been logged out !!')
    return redirect('home')


def register_user (request):
    if request.method == 'POST':
       form = SignUpForm(request.POST)
       if form.is_valid():
           form.save()
        #    authenticate and login 
           username = form.cleaned_data.get['username']
           password = form.cleaned_data.get['password1']
        #    from the declared variables above username and password
           user = authenticate(request, username=username, password=password) 
           login (request, user)
           messages.success(request, f'Welcome {username} !!')
           return redirect('home')
    #    above is to the if filing the form 
    else: 
        form = SignUpForm()
        return render(request,'register.html',{'form':form})

    return render(request,'register.html',{'form':form})
    # passign the form to the register.html page 




def customer_record(request,pk): 
   if request.user.is_authenticated: 
       customer_record = Record.objects.get(id=pk)
       return render(request,'record.html',{'customer_record':customer_record})
   else:
        messages.success(request,"you have to log in to visit the site ")
        return redirect('home')
    
    
    
def delete_record(request,pk): 
    if request.user.is_authenticated:
        # if only can logged in user can delete the record
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"successfully deleted")
        return redirect('home')
    else:
        # else cannot delete user
        messages.success(request,"you have to logged in to delete the record")
        return redirect('home')


def add_record(request): 
        form = AddRecordForm(request.POST or None)
    
        if request.user.is_authenticated:
            if request.method == "POST":
                if form.is_valid(): 
                    add_record = form.save()
                    messages.success(request,"successfully added")
                    return redirect('home')
            # otherwise user don't want to post the form then reutrn the form means if they havenot filled the form and after adding the form also it will show the form 
            return render (request,'add_record.html',{'form':form})
        else: 
            # if user is not authenticated
            messages.success(request,"you have to logged in to add the record")   



def update_record (request,pk): 
    if request.user.is_authenticated:
        # if only can logged in user can delete the record
        update_it = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=update_it)
        if form.is_valid ():
            form.save()
            messages.success(request,"successfully updated")
            return redirect('home')
        return render (request,'update_record.html',{'form':form})
    else:
        messages.success(request,"you have to logged in to update the record") 
        
        
        
        
    