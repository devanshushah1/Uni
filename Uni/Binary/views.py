from django.shortcuts import render, redirect
from . import CheckAdjacent
from .forms import NumberForm, UserNameForm
import requests
# Create your views here.
# from .CheckAdjacent import CheckAdjacent


def HomePage(request):
    return render(request, 'Binary/index.html')


def BinaryCheck(request):
    form = NumberForm()

    if request.method == "POST":
        form = NumberForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            return Solution(request, num1, num2)
    context = {'form': form}
    return render(request, 'Binary/binarycheck.html', context)


def Solution(request, num1, num2):
    answer = CheckAdjacent.CheckAdjacent(num1, num2)
    context = {'answer': answer}
    return render(request, 'Binary/solution.html', context)


def ApiQuery(request):
    form = UserNameForm()

    if request.method == 'POST':
        form = UserNameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            return QueryResult(request, username)

    context = {'form': form}
    return render(request, 'Binary/ApiQuery.html', context)


def QueryResult(request, username):
    response = requests.get('https://api.github.com/users/' + username + '/repos')
    user_data = response.json()
    name_list = []
    for i in user_data:
        name_list.append(i['name'])
    context = {'names': name_list}

    return render(request, 'Binary/queryresult.html', context)
