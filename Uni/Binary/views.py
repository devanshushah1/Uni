from django.shortcuts import render, redirect
from . import CheckAdjacent
from .forms import NumberForm, UserNameForm, DataQueryForm
import requests
from .models import *
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
    response2 = requests.get('https://api.github.com/users/' + username + '/followers')
    name_list = []
    follower_list = []
    username_dict = GitQuery.objects.all().values('username')
    username_list = []
    for k in username_dict:
        username_list.append(k['username'])

    if response:
        user_data = response.json()
        for i in user_data:
            name_list.append(i['name'])
        repo_count = len(name_list)
        if username in username_list:
            obj = GitQuery.objects.get(username=username)
            obj.repo_count = repo_count
            obj.save()
    if response2:
        folo_data = response2.json()
        for i in folo_data:
            follower_list.append(i['login'])
        folo_count = len(follower_list)
        if username in username_list:
            pass

        else:
            GitQuery.objects.create(username=username, repo_count=repo_count, folo_count=folo_count)
    error = 'User Not Found'

    context = {'names': name_list, 'error': error, 'followers': follower_list}
    return render(request, 'Binary/queryresult.html', context)


def dataquery(request):
    form = DataQueryForm()
    result = None
    if request.method == 'POST':
        form = DataQueryForm(request.POST)
        if form.is_valid():
            repo_count = form.cleaned_data['repo_count']
            result = GitQuery.objects.filter(repo_count=repo_count)
            for obj in result:
                obj.count += 1
                obj.save()

    context = {'form': form, 'result': result}
    return render(request, 'Binary/dataquery.html', context)


def Top3(request):
    ans = GitQuery.objects.order_by('-count')[:3]
    context = {'ans': ans}
    return render(request, 'Binary/top3.html', context)
