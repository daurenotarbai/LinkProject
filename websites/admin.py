from django.contrib import admin
from .models import *

class LinkModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LinkModel._meta.fields]
admin.site.register(LinkModel,LinkModelAdmin)

class CategoryLinkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CategoryLink._meta.fields]
admin.site.register(CategoryLink,CategoryLinkAdmin)


class LinksInWishlistAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LinksInWishlist._meta.fields]
admin.site.register(LinksInWishlist,LinksInWishlistAdmin)

class VisitedHistoryModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in VisitedHistoryModel._meta.fields]
admin.site.register(VisitedHistoryModel,VisitedHistoryModelAdmin)