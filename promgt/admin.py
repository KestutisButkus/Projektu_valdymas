from django.contrib import admin
from .models import Client, Employee, Project, Task, Invoice
from tinymce.widgets import TinyMCE
from django.db import models

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'company', 'email', 'phone')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position')
    search_fields = ('first_name', 'last_name', 'position')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'client', 'manager')
    list_filter = ('start_date', 'end_date', 'client', 'manager')
    search_fields = ('name', 'client__first_name', 'client__last_name', 'manager__username')
    fields = ('name', 'start_date', 'end_date', 'client', 'employees', 'manager', 'photo', 'description')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('date_issued', 'amount')
    list_filter = ('date_issued',)
    search_fields = ('date_issued', 'amount')

admin.site.register(Client, ClientAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Invoice, InvoiceAdmin)
