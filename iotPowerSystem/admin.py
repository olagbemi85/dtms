from django.contrib import admin
from .models import Data, Station, Region, AreaOffice, Company, Level, Position




class dataPowerAdmin(admin.ModelAdmin):
	list_display=('voltage_r', 'voltage_y', 'voltage_b', 'currents_r', 'currents_y', 'currents_b', 'power_r', 'power_y', 'power_b', 'temp', 'station_code', 'days','hourly')
admin.site.register(Data, dataPowerAdmin)


#@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    #list_display = ('station_name')
    list_display = ['station_name','company','regional_office','code','location','max_power', 'area_office','state','local_gov_area','latitude','longtitudes']    
admin.site.register(Station, StationAdmin)    


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']
    #list_editable =  ['name']


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']
    #list_editable =  ['name']


@admin.register(AreaOffice)
class AreaOfficeAdmin(admin.ModelAdmin):
    list_display =['name','region']
    list_editable = ['region']
    list_display_links = ("name", )
 
 
@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['name']
    #list_editable =  ['name']
    

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name']
    #list_editable =  ['name']         