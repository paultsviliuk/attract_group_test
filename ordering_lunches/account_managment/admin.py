from django.contrib import admin
from .models import User, Product
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportMixin
from . import mail, utils

users=User.objects


class UserResource(resources.ModelResource):

    class Meta:
        model = User
        skip_unchanged = True
        report_skipped = False
        fields = ('id', 'name', 'surname', 'email', 'password', 'telephone')


@admin.register(User)
class UserAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = UserResource
    list_display = ['name', 'surname', 'telephone', 'email']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'shop', 'price']
