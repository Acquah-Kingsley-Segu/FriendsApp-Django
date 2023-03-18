from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def login_user(request):
  # check if user actually made a post request by filling in the form 
  if request.method == 'POST':
    #getting user form entries
    username = request.POST['username']
    password = request.POST['password']

    #authenticate user
    user = authenticate(request, username=username, password=password)

    #check if user exist
    if user is not None:
      #login user in if they exist in our database
      login(request, user)
      #redirect to home page
      messages.success(request, ("You logged in succesfully"))
      return redirect('friends:index')
    else:
      #create an error message
      messages.warning(request, ("You do not have an account. Sign Up"))
      return redirect('registration:login')

  else: #display if user just visited the site
    return render(request, 'registration/login.html', {})

def logout_user(request):
  logout(request)
  messages.success(request, "You logged out succesfully")
  return redirect('registration:login')

def signup_user(request):
  if request.method == 'POST':
    #get data from form
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    #instantiate user
    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
    #save user
    user.save()

    messages.success(request, "You successfully signed up")
    return redirect('login')
  else:
    return render(request, 'registration/signup.html', {})