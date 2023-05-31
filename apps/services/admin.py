from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from apps.services.models import (
    ServiceLocation, ServiceType)


class ServiceLocationAdmin(ModelAdmin):
    model = ServiceLocation
    menu_label = 'Service Locations'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    list_display = ('name','order')
    search_fields = ('name',)


class ServiceTypeAdmin(ModelAdmin):
    model = ServiceType
    menu_label = 'Service Types'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    list_display = ('name','order')
    search_fields = ('name',)


class ServicesGroup(ModelAdminGroup):
    menu_label = 'Services'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (ServiceLocationAdmin, ServiceTypeAdmin)

modeladmin_register(ServicesGroup)