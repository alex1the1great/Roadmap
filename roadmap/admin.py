from django.contrib import admin

from .models import Goal


class GoalAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'deadline']
    list_filter = ['deadline']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Goal, GoalAdmin)
