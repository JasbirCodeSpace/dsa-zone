from django.contrib import admin
from account.models import User

@admin.register(User)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_student', 'is_curator')
