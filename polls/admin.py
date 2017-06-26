from django.contrib import admin

from meat.models import Animal, Part, Cut, AltPart, AltCut, Address, ContactDetails, Supplier
from .models import Question, Choice, HintImage


# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class InlineImage(admin.TabularInline):
    model = HintImage

class QuestionAdmin(admin.ModelAdmin):

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None, {'fields' : ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [InlineImage, ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin )
#admin.site.register(MyImage, InlineImage)
admin.site.register(HintImage)