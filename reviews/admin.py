from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'rating', 'created_at', 'approval_status']
    list_filter = ['is_approved', 'rating', 'created_at']
    actions = ['approve_reviews', 'unapprove_reviews']

    def approval_status(self, obj):
        return "Approved" if obj.is_approved == 1 else "Pending"
    approval_status.short_description = "Status"

    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=1)
    approve_reviews.short_description = "Approve selected reviews"

    def unapprove_reviews(self, request, queryset):
        queryset.update(is_approved=0)
    unapprove_reviews.short_description = "Unapprove selected reviews"