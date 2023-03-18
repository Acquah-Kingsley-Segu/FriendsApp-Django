from django.shortcuts import get_object_or_404,render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Friend


def log_user_in(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request, username=username, password=password)

  if user is not None:
    login(request, user)
    return HttpResponseRedirect(reverse('friends:index'))
  else:
    return HttpResponse({'invalid login'})

def logout(request):
  logout(request)

@login_required(login_url='login')
def index(request):
  friends = Friend.objects.all()
  context = {
    'friends': friends
  }

  return render(request, 'friends/index.html', context=context)

@login_required(login_url='login')
def create(request):
  return render(request, 'friends/create.html')

@login_required(login_url='login')
def save(request):
  if request.method == 'POST':
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    phone=request.POST['phone']
    twitter_handle=request.POST['twitter_handle']
    
    friend = Friend(first_name=first_name, last_name=last_name, email=email, phone=phone, twitter_handle=twitter_handle)
    friend.save()

    return HttpResponseRedirect(reverse('friends:show', args=(friend.id,)))
  else:
    return render(request, "friends:create")

@login_required(login_url='login')
def show(request, friend_id: int):
  friend = get_object_or_404(Friend, pk=friend_id)
  context={
    'friend': friend,
    'friend_id': friend_id
  }
  return render(request, 'friends/show.html', context=context)

@login_required(login_url='login')
def edit(request, friend_id):
  friend = get_object_or_404(Friend, pk=friend_id)
  context = {
    "friend": friend
  }

  return render(request, 'friends/edit.html', context=context)

@login_required(login_url='login')
def update(request, friend_id):
  friend = Friend.objects.get(pk=friend_id)

  if request.method == 'POST':
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    phone=request.POST['phone']
    twitter_handle=request.POST['twitter_handle']
    
    friend.first_name = first_name
    friend.last_name = last_name
    friend.email = email
    friend.phone = phone
    friend.twitter_handle = twitter_handle
    friend.save()

    return HttpResponseRedirect(reverse('friends:show', args=(friend.id,)))
  else:
    return render(request, "friends/index.html")

@login_required(login_url='login')
def delete(request, friend_id):
  friend = get_object_or_404(Friend, pk=friend_id)
  friend.delete()

  return HttpResponseRedirect(reverse('friends:index'))