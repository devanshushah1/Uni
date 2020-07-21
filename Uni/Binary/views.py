from django.shortcuts import render, redirect
from . import CheckAdjacent
from .forms import NumberForm
# Create your views here.
# from .CheckAdjacent import CheckAdjacent


def HomePage(request):
    form = NumberForm()

    if request.method == "POST":
        form = NumberForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            return Solution(request, num1, num2)
    context = {'form': form}
    return render(request, 'Binary/index.html', context)


def Solution(request, num1, num2):
    answer = CheckAdjacent.CheckAdjacent(num1, num2)
    context = {'answer': answer}
    return render(request, 'Binary/solution.html', context)
