from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Service, PortfolioItem, Testimonial, SocialLink
from django.contrib import admin
from .models import ContactFeedback

admin.site.register(Service)
admin.site.register(PortfolioItem)
admin.site.register(Testimonial)
admin.site.register(SocialLink)



@admin.register(ContactFeedback)
class ContactFeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('submitted_at',)