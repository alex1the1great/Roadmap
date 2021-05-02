from django.shortcuts import render, redirect

from .models import Goal
from .forms import GoalForm


def goal_list(request):
    goals = Goal.objects.all()
    return render(request, 'roadmap/goal_list.html', {'goals': goals})


def goal_add(request):
    form = GoalForm()
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.creator = request.user
            goal.save()
            return redirect('goal_list')
    return render(request, 'roadmap/goal_add.html', {'form': form})
