from import_export.admin import ImportExportModelAdmin, ImportExportMixin
from django.contrib import admin
from .models import *
from resources import MemberResource

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
	list_display = ['user__username', 'user__first_name', 'user__last_name', 'region','membership_level', 'membership_expiration']
	inlines = [
		MemberEducationInline,
		AddressInline,
		NoteInline,
		ProfesionalInfoInline
	]


@admin.register(MemberNote)
class MembersNoteAdmin(admin.ModelAdmin):
	list_display = ['member', 'date', 'note']


@admin.register(MembershipLevel)
class MembershipLevelAdmin(admin.ModelAdmin):
	pass



@admin.register(MemberAddress)
class MemberAddressAdmin(admin.ModelAdmin):
	pass


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
	pass



class myUserAdmin(ImportExportMixin, UserAdmin):
	resource_class = UserResource

	


admin.site.unregister(User)
admin.site.register(User, myUserAdmin)
