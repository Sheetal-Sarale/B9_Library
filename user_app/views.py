from django.shortcuts import render,HttpResponse,redirect
from.forms import NewUserForm       # username, passw1,passw2, email\
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
# Create your views here.



def user_signup(request):
    if request.method == "POST":
        data = request.POST
        # print(data)
        form = NewUserForm(data)
        if form.is_valid():
           user = form.save()                # user entry in auth user table
           print(user)
           messages.success(request, f"user:'{user.username}'registered successfully. you can login here.")
           return redirect("user_login")
        else: 
           messages.error(request, "unsuccessful signup invalid information")


    elif request.method == "GET":
     form = NewUserForm()
     return render(request=request, template_name="register.html", context={"signup_form":form})
    

def user_login(request):
   if request.method == "POST":
    #   form = AuthenticationForm(request, data=request.POST)  
    #   if form.is_valid():
    #      user_name = form.cleaned_data.get("username") 
    #      password = form.cleaned_data.get("password")
      user_name = request.POST.get("username")
      password = request.POST.get("password")
      user = authenticate(username=user_name, password=password)  # verify auth user   return user object
      if user:
            login(request,user)       # to maintain session     django session table entry
            messages.success(request, "logged in successfully" )
            return redirect("home_page")
      else:
            messages.error(request, "invalid username and password")  
            return redirect("user_login")   

   elif request.method == "GET":
      return render(request, "login.html",{"login_form": AuthenticationForm})
      
   
def user_logout(request):
     logout(request) 
     return redirect("user_login")