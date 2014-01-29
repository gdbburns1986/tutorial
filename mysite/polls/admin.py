from django.contrib import admin
from polls.models import Poll, Choice

#this class will allow the Chouice model
#to be displayed on the add Poll admin page
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question',               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]
    #tells django choices are edited on the Poll page
    inlines = [ChoiceInline]
    #customizing the admin change list
    list_display = ('question', 'pub_date', 'was_published_today')
    #adding a filter by published date
    list_filter = ['pub_date']
    #adding searching
    search_fields = ['question']
    #drill down by date
    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)
