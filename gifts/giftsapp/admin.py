
from django.contrib import admin

# Register your models here.
from giftsapp.models import *
admin.site.register(Profile)
admin.site.register(Agegroup)
admin.site.register(Personality)
admin.site.register(Occassion)
admin.site.register(Gifts)
admin.site.register(Gift_mapping)
admin.site.register(Gender)
admin.site.register(Quest)


