from django.contrib import admin
from django.utils.html import format_html
from .models import ContactMessage, GalleryImage, MediaPost

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name_display', 'email', 'phone', 'subject', 'message_snippet', 'created_at')
    list_display_links = ('name_display', 'email')
    search_fields = ('name', 'email', 'phone', 'subject', 'message')
    list_filter = ('subject', 'created_at')
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Sender Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Inquiry & Message', {
            'fields': ('subject', 'message', 'created_at')
        }),
    )

    def name_display(self, obj):
        return obj.name if obj.name else f"(Message #{obj.id})"
    name_display.short_description = "Name"

    def message_snippet(self, obj):
        if obj.message and len(obj.message) > 50:
            return obj.message[:47] + "..."
        return obj.message or "-"
    message_snippet.short_description = "Message"

    def get_readonly_fields(self, request, obj=None):
        return ('created_at',)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('image_thumbnail', 'title', 'category', 'badge_text', 'order', 'is_active', 'created_at')
    list_display_links = ('image_thumbnail', 'title')
    list_editable = ('order', 'is_active')
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('title', 'description', 'badge_text')
    readonly_fields = ('image_preview_detail', 'created_at', 'updated_at')

    fieldsets = (
        ('Image Details', {
            'fields': ('title', 'category', 'badge_text', 'image', 'image_preview_detail')
        }),
        ('Description & Narrative', {
            'fields': ('description',)
        }),
        ('Settings & Ordering', {
            'fields': ('order', 'is_active', 'created_at', 'updated_at')
        }),
    )

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 55px; height: 42px; object-fit: cover; border-radius: 6px; border: 1px solid #ccc;" />', obj.image.url)
        return "No image"
    image_thumbnail.short_description = "Thumbnail"

    def image_preview_detail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 280px; max-height: 200px; object-fit: contain; border-radius: 8px; border: 1px solid #ccc;" />', obj.image.url)
        return "No image uploaded yet"
    image_preview_detail.short_description = "Current Image Preview"


@admin.register(MediaPost)
class MediaPostAdmin(admin.ModelAdmin):
    list_display = ('image_thumbnail', 'title', 'category', 'author_name', 'is_featured', 'order', 'is_active', 'date')
    list_display_links = ('image_thumbnail', 'title')
    list_editable = ('is_featured', 'order', 'is_active')
    list_filter = ('category', 'is_featured', 'is_active', 'date')
    search_fields = ('title', 'content', 'author_name', 'author_role')
    readonly_fields = ('image_preview_detail', 'created_at', 'updated_at')

    fieldsets = (
        ('Post Content & Headline', {
            'fields': ('title', 'category', 'content')
        }),
        ('Author & Leadership Attribution', {
            'fields': ('author_name', 'author_role')
        }),
        ('Media Visuals', {
            'fields': ('image', 'image_preview_detail')
        }),
        ('Action Links', {
            'fields': ('external_link', 'link_text')
        }),
        ('Publishing Options', {
            'fields': ('is_featured', 'order', 'is_active', 'date', 'created_at', 'updated_at')
        }),
    )

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 55px; height: 42px; object-fit: cover; border-radius: 6px; border: 1px solid #ccc;" />', obj.image.url)
        return "No image"
    image_thumbnail.short_description = "Thumbnail"

    def image_preview_detail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 280px; max-height: 200px; object-fit: contain; border-radius: 8px; border: 1px solid #ccc;" />', obj.image.url)
        return "No image uploaded yet"
    image_preview_detail.short_description = "Current Image Preview"
