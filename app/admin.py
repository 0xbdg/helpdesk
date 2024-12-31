from django.contrib import admin
from .models import Ticket

# Register your models here.

admin.site.site_title = "Helpdesk"
admin.site.index_title = "Help Desk"
admin.site.site_header = "Help Desk"

class TicketConfig(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    
    readonly_fields = ["client", "problem",  "description", "date"]
    list_display = ["client", "problem", "status","date"]


admin.site.register(Ticket, TicketConfig)