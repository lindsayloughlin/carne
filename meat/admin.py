from django.contrib import admin

# Register your models here.
from meat.models import Address, Animal, Part, AltPart, AltCut, Cut, Supplier, ContactDetails, Suburb
class AddressInline(admin.StackedInline):
    model = Address

class ContactDetailsInline(admin.StackedInline):
    model= ContactDetails


class SupplierAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [ AddressInline, ContactDetailsInline ]



#admin.site.register(Question, QuestionAdmin )
#admin.site.register(MyImage, InlineImage)
#admin.site.register(HintImage)

admin.site.register(Animal)
admin.site.register(Part)
admin.site.register(Cut)
admin.site.register(AltPart)
admin.site.register(AltCut)
admin.site.register(Address)
admin.site.register(ContactDetails)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Suburb)