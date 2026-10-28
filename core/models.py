from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('leadership', 'Leadership & Guidance'),
        ('healthcare', 'Healthcare (Hridayasparsham)'),
        ('education', 'Education (Vidhya Amruthu)'),
        ('community', 'Community & Youth (Vazhikatti)'),
    ]

    title = models.CharField(max_length=200, help_text="Title or caption for the photograph")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='leadership', help_text="Category for filtering")
    image = models.ImageField(upload_to='gallery/', help_text="Upload high-resolution gallery image")
    description = models.TextField(blank=True, help_text="Short narrative or context")
    badge_text = models.CharField(max_length=60, blank=True, help_text="Badge label displayed on image (e.g. Leadership, Healthcare)")
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Show on website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def image_preview(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" style="width: 70px; height: 50px; object-fit: cover; border-radius: 6px; border: 1px solid #ddd;" />')
        return "No Image"
    image_preview.short_description = "Preview"


class MediaPost(models.Model):
    CATEGORY_CHOICES = [
        ('leadership', 'Leadership & Vision'),
        ('welfare', 'Social Welfare'),
        ('outreach', 'Community Outreach'),
        ('messages', 'Public Messages'),
        ('updates', 'Society Updates'),
        ('awareness', 'Social Awareness'),
    ]

    title = models.CharField(max_length=250, help_text="Title or headline of the post/statement")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='leadership', help_text="Topic category for filtering")
    author_name = models.CharField(max_length=150, default='Mr. Ainuddin Shah Ji', help_text="Author, speaker, or desk name")
    author_role = models.CharField(max_length=150, default='Senior Social Worker & Chief Patron', help_text="Designation or organization role")
    image = models.ImageField(upload_to='media_posts/', help_text="Photograph of Ainuddin Shah Ji or society activity")
    content = models.TextField(help_text="Verified statement, quote, or announcement text")
    external_link = models.CharField(max_length=300, blank=True, help_text="Target URL or link (e.g. /about/, /people/, /contact/)")
    link_text = models.CharField(max_length=80, default='Read More', help_text="Label on the action link (e.g. View Profile, Read Full Message)")
    is_featured = models.BooleanField(default=False, help_text="Highlight as top featured spotlight card")
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Show on website")
    date = models.DateField(default=timezone.now, help_text="Date of release or update")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Media Post"
        verbose_name_plural = "Media Posts"
        ordering = ['order', '-date', '-created_at']

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"

    def image_preview(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" style="width: 70px; height: 50px; object-fit: cover; border-radius: 6px; border: 1px solid #ddd;" />')
        return "No Image"
    image_preview.short_description = "Preview"
