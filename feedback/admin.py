from django.contrib import admin
from .models import OfferModel, ProblemModel


@admin.register(OfferModel)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(ProblemModel)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
#     search_fields = ('username', 'email')
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#     ordering = ('username',)
#
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#