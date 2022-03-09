from django.contrib import admin
from django.contrib.auth.models import User
from .models import BankData


@admin.register(BankData)
class BankDataAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'iban')
    list_filter = ('first_name', 'last_name', 'iban')
    search_fields = ('first_name', 'last_name')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(first_name=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "first_name":
            kwargs["queryset"] = User.objects.filter(first_name=request.user.first_name)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
