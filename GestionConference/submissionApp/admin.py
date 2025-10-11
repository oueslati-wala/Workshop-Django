from django.contrib import admin
from .models import Submission

@admin.register(Submission)
class AdminSubmissionModel(admin.ModelAdmin):
    list_display = ("title", "status", "conference", "submission_date", "payed", "keywords","short_abstract")

    def short_abstract(self, obj):
        if len(obj.abstract) > 50:
            return obj.abstract[:50] + "..."
        return obj.abstract
    short_abstract.short_description = "Short Abstract"
    list_filter=("status","payed","conference","submission_date")
    search_fields=("title","keywords","user__username")
    list_editable=("status","keywords")
    fieldsets=(
        ("infos generales",{
            "fields":("submission_id","title","abstract","keywords")
        }),
        ("fichier et conference",{
            "fields":("paper","conference")
        }),
        ("suivi",{
            "fields":("status","payed","submission_date","user")
        })
    )
    readonly_fields=("submission_id","submission_date")