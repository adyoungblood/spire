from import_export.admin import ImportExportModelAdmin, ImportExportMixin
from django.contrib import admin
from .models import *
from resources import MemberResource, MemberAddressResource, MemberProfesionalInformationResource, MemberEducationResource
from dal import autocomplete
from spire.resources import UserResource
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class MemberEducationInline(admin.TabularInline):
	model = MemberEducation
	extra = 0


class AddressInline(admin.TabularInline):
	model = MemberAddress
	extra = 0

class ProfesionalInfoInline(admin.StackedInline):
	model = MemberProfesionalInformation
	extra = 0

class NoteInline(admin.TabularInline):
	model = MemberNote
	extra = 0


@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
	resource_class = MemberResource
	search_fields = ['user__username']
	list_display = ['user', 'get_first_name', 'get_last_name', 'membership_level', 'membership_expiration']
	autocomplete_lookup_fields = {
        'fk': ['user'],
    }
	raw_id_fields = ("user",)
	list_filter = ('membership_level',)

	inlines = [
		MemberEducationInline,
		AddressInline,
		ProfesionalInfoInline,
		NoteInline
	]

	def get_first_name(self, obj):
		return obj.user.first_name
	get_first_name.short_description = 'First Name'
	get_first_name.admin_order_field = 'user__first_name'

	def get_last_name(self, obj):
		return obj.user.last_name
	get_last_name.short_description = 'Last Name'
	get_last_name.admin_order_field = 'user__last_name'



#@admin.register(MemberNote)
#class MembersNoteAdmin(admin.ModelAdmin):
	#list_display = ['member', 'date', 'note']


@admin.register(MembershipLevel)
class MembershipLevelAdmin(admin.ModelAdmin):
	pass


#@admin.register(MemberAddress)
#class MemberAddressAdmin(ImportExportModelAdmin):
#	resource_class = MemberAddressResource

#@admin.register(MemberProfesionalInformation)
#class MemberProfesionalInformationAdmin(ImportExportModelAdmin):
#	resource_class = MemberProfesionalInformationResource


#@admin.register(MemberEducation)
#class MemberEducationAdmin(ImportExportModelAdmin):
#	resource_class = MemberEducationResource
#	list_display = ['member', 'degree', 'grad_year']


@admin.register(MemberIndustry)
class MemberIndustryAdmin(admin.ModelAdmin):
	list_display = ['industry','entered_by']


@admin.register(MemberIndustryAssociation)
class MemberIndustryAssiociationAdmin(admin.ModelAdmin):
	pass

@admin.register(MemberMembershipHistory)
class MemberMembershipHistoryAdmin(admin.ModelAdmin):
	list_display = ['member','new_level', 'previous_level', 'date']


@admin.register(MemberRegion)
class MemberRegionAdmin(admin.ModelAdmin):
	pass



@admin.register(MemberPurchaseHistory)
class MemberEventPurchaseAdmin(admin.ModelAdmin):
	list_display = ['member', 'item', 'purchase_date', 'purchase_price']



class myUserAdmin(ImportExportMixin, UserAdmin):
	resource_class = UserResource




admin.site.unregister(User)
admin.site.register(User, myUserAdmin)
