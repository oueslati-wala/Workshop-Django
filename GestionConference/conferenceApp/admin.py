from django.contrib import admin
from .models import Conference
from submissionApp.models import Submission
from organisation_comiteeApp.models import Committee
# Register your models here.
#admin.site.register(Conference)
#admin.site.register(Submission)
admin.site.register(Committee)
admin.site.site_title="gestion conference ai"
admin.site.site_header="gestion conference ai admin"
admin.site.index_title="welcome django app conference"

class SubmissionStackedInline(admin.StackedInline):
    model=Submission
    extra=1
    readonly_fields=("submission_id","submission_date")
    fields=("title","abstract","status","payed")

class SubmissionTabularInline(admin.TabularInline):
    model=Submission
    extra=1
    fields=("title","status","user","payed")

class ComitteeInline(admin.StackedInline):
    model=Committee
    extra=1

@admin.register(Conference)
class AdminConferenceModel(admin.ModelAdmin):
    list_display=("name","theme","location","start_date","end_date","duration")
    ordering=("start_date",)
    list_filter=("theme","location","start_date")
    search_fields=("name","descripption","location")
    date_hierarchy="start_date"
    fieldsets=(
        ("informations generales",{
            "fields":("name","theme","descripption")
        }),
        ("logistique",{
            "fields":("location","start_date","end_date")
        })
    )
    readonly_fields=("conference_id",)
    def duration(self,objet):
        if objet.start_date and objet.end_date:
            return (objet.end_date-objet.start_date).days
        return "ras"
    duration.short_description="duration (days)"
    inlines=[SubmissionStackedInline,SubmissionTabularInline,ComitteeInline]