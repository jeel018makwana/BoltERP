from django.contrib import admin
from .models import Company
from logs.utils import log_activity

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "gst_number",
    )

    def save_model(self,request,obj,form,change):
        super().save_model(request,obj,form,change)

        if change:
            action = "UPDATE"
            description = f"Updated Company: {obj.name}"
        else:
            action = "CREATE"
            description = f"Created Company: {obj.name}"
        
        log_activity(
            user = request.user,
            action = action,
            module= "Company",
            description = description,
        )

    def delete_model(self,request,obj):
        log_activity(
            user=request.user,
            action = "DELETE",
            module="Company",
            description = f"Deleted Company: {obj.name}",
        )

        super().delete_model(request,obj)