from django.contrib import admin
from vehiculos.models import Auto

# admin.site.register(Auto)
# admin.site.register([Auto, 1, 2, 3, 4, 5])
# admin.site.register(1)
# admin.site.register(2)
# admin.site.register(3)
# admin.site.register(4)
# admin.site.register(5)

class AutoAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo']
    search_fields = ['modelo']
    list_filter = ['fecha_fabricacion']

admin.site.register(Auto, AutoAdmin)