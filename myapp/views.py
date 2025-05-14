from django.shortcuts import render
import random

fortune_list = ["You will have a great day!", "You will meet a new friend.", "Will be rich in the near future.", "You will have a fantastic career.", "You will have a great life."]

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def fortune(request):
    context = {'fortune': random.choice(fortune_list)}
    return render(request, 'myapp/fortune.html', context)