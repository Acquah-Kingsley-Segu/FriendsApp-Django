from django.shortcuts import get_object_or_404,render

from .models import Friend

def index(request):
  friends = Friend.objects.all()
  context = {
    'friends': friends
  }

  return render(request, 'friends/index.html', context=context)

def show(request, friend_id: int):
  friend = get_object_or_404(Friend, pk=friend_id)
  context={
    'friend': friend,
    'friend_id': friend_id
  }
  return render(request, 'friends/show.html', context=context)

