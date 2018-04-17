from django.contrib import admin
from import_export import resources, widgets
from import_export.admin import ImportMixin, ImportExportModelAdmin
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Category, Product
from .mail import send_password
from string import ascii_letters
from random import choice


User = get_user_model()


# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class UserResource(resources.ModelResource):

    class Meta:
        model = User
        skip_unchanged = True
        report_skipped = True
        fields = ('id', 'last_name', 'first_name', 'telephone', 'email', 'password' 'username')

    #def import_obj(self, obj, data, dry_run):
     #   passgen = lambda x: x.join(choice(ascii_letters) for i in range(10))('')
      #  for field in self.get_fields():
       #     if isinstance(field.widget, widgets.ManyToManyWidget):
        #        continue
         #   if field.column_name == 'password':
          #      data.update({'password': make_password(passgen)})
           #     send_password(field.column_name.email, field.column_name.password)
            #print(obj)

            #self.import_field(field, obj, data)


class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)


# Модель товара
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
