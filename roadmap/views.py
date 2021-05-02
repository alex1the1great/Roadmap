from django.shortcuts import render, redirect, get_object_or_404

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


def goal_edit(request, slug):
    goal = get_object_or_404(Goal, slug=slug)
    form = GoalForm(instance=goal)

    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goal_list')
    return render(request, 'roadmap/goal_edit.html', {'form': form, 'goal': goal})


def goal_delete(request, slug):
    goal = get_object_or_404(Goal, slug=slug)
    goal.delete()
    return redirect('goal_list')
