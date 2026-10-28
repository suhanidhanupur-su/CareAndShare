import os, sys, shutil
sys.path.insert(0, r'C:\Users\suhani\Desktop\CareAndShare\CareAndShare')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CareAndShare.settings')
import django
django.setup()

from core.models import GalleryImage, MediaPost
from django.conf import settings

media_gallery_dir = os.path.join(settings.MEDIA_ROOT, 'gallery')
media_posts_dir = os.path.join(settings.MEDIA_ROOT, 'media_posts')
os.makedirs(media_gallery_dir, exist_ok=True)
os.makedirs(media_posts_dir, exist_ok=True)

static_img_dir = os.path.join(settings.STATICFILES_DIRS[0], 'images')

# Copy images to media directory if not already there
img_mappings = {
    'ainuddin_shah.jpg': 'ainuddin_shah.jpg',
    'slide-ainuddin.jpg': 'slide-ainuddin.jpg',
    'slide-ainuddin-2.jpg': 'slide-ainuddin-2.jpg',
    'hridayasparsham-1.jpg': 'hridayasparsham-1.jpg',
    'vazhikatti-1.jpg': 'vazhikatti-1.jpg',
    'vidhyamrutham-1.jpg': 'vidhyamrutham-1.jpg',
    'banner-inner.jpg': 'banner-inner.jpg',
    'logo.png': 'logo.png',
}

for src_name, dst_name in img_mappings.items():
    src_path = os.path.join(static_img_dir, src_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, os.path.join(media_gallery_dir, dst_name))
        shutil.copy2(src_path, os.path.join(media_posts_dir, dst_name))

print("Media folders prepared and initial files copied.")

# 1. Populate Gallery Images if empty
if GalleryImage.objects.count() == 0:
    gallery_data = [
        {
            'title': 'Mr. Ainuddin Shah Ji - Senior Social Worker',
            'category': 'leadership',
            'badge_text': 'Leadership',
            'image': 'gallery/ainuddin_shah.jpg',
            'description': 'Respected Ainuddin Shah Ji guiding social welfare and community outreach initiatives in Sardhana.',
            'order': 1
        },
        {
            'title': 'Moving Step by Step - Community Welfare',
            'category': 'community',
            'badge_text': 'Community Outreach',
            'image': 'gallery/slide-ainuddin.jpg',
            'description': 'We strive to share the burden of the less fortunate through the efforts of those with surplus resources.',
            'order': 2
        },
        {
            'title': 'Leadership in Action',
            'category': 'leadership',
            'badge_text': 'Leadership',
            'image': 'gallery/slide-ainuddin-2.jpg',
            'description': 'Inspiring volunteers and organizing local relief drives for underprivileged families.',
            'order': 3
        },
        {
            'title': 'Hridayasparsham (Pro Heart) Initiative',
            'category': 'healthcare',
            'badge_text': 'Healthcare',
            'image': 'gallery/hridayasparsham-1.jpg',
            'description': 'Flagship paediatric cardiology programme delivering life-saving heart surgeries to vulnerable children.',
            'order': 4
        },
        {
            'title': 'Vazhikatti - Youth Guidance Campaign',
            'category': 'community',
            'badge_text': 'Youth Campaign',
            'image': 'gallery/vazhikatti-1.jpg',
            'description': 'Intensive youth awareness drive combating substance abuse and guiding young citizens toward meaningful goals.',
            'order': 5
        },
        {
            'title': 'Vidhya Amruthu - Educational Aid',
            'category': 'education',
            'badge_text': 'Education',
            'image': 'gallery/vidhyamrutham-1.jpg',
            'description': 'Educational venture providing learning kits, textbooks, and merit scholarships for deserving students.',
            'order': 6
        },
        {
            'title': 'Community Relief & Welfare',
            'category': 'community',
            'badge_text': 'Welfare Camp',
            'image': 'gallery/banner-inner.jpg',
            'description': 'Grassroots relief, volunteer aid distribution, and community support programs.',
            'order': 7
        },
        {
            'title': 'Emblem of Care & Share Society',
            'category': 'education',
            'badge_text': 'Our Emblem',
            'image': 'gallery/logo.png',
            'description': 'Symbolizing protective care, learning, and human dignity: Together We Care, Together We Share.',
            'order': 8
        },
    ]
    for item in gallery_data:
        GalleryImage.objects.create(**item)
    print(f"Populated {len(gallery_data)} Gallery images in DB.")
else:
    print(f"GalleryImage already has {GalleryImage.objects.count()} items.")

# 2. Populate Media Posts if empty
if MediaPost.objects.count() == 0:
    media_data = [
        {
            'title': '"IT IS NOW OR NEVER !" — An Open Appeal for Compassion & Sharing',
            'category': 'messages',
            'author_name': 'Mr. Ainuddin Shah Ji',
            'author_role': 'Senior Social Worker & Chief Patron',
            'image': 'media_posts/slide-ainuddin.jpg',
            'content': 'We strongly believe that every individual deserves an opportunity to live a healthy, dignified, and fulfilling life. We are all bound by our duty to society and to our fellow citizens. We should commit ourselves to helping the less fortunate and the needy by sharing our resources with those who are deprived. This is the right time to come forward and support this noble cause of care and share.',
            'external_link': '/people/',
            'link_text': 'Read Full Leadership Message',
            'is_featured': True,
            'order': 0,
        },
        {
            'title': 'Serving Humanity is Our Highest Moral Duty',
            'category': 'leadership',
            'author_name': 'Mr. Ainuddin Shah Ji',
            'author_role': 'Senior Social Worker',
            'image': 'media_posts/ainuddin_shah.jpg',
            'content': 'Through Care & Share Society Sardhana, we have resolved to reach the poorest and most vulnerable, ensuring that lack of resources never denies a child an education or a patient life-saving healthcare.',
            'external_link': '/about/',
            'link_text': 'View Leadership Profile',
            'order': 1,
        },
        {
            'title': 'Sharing is Absolute Caring — Core Philosophy',
            'category': 'welfare',
            'author_name': 'Care & Share Society',
            'author_role': 'Sardhana • Non-Profit',
            'image': 'media_posts/slide-ainuddin.jpg',
            'content': 'Care & Share Society, Sardhana is dedicated to serving humanity under Ainuddin Shah Ji\'s guidance. Through care, sharing, compassion, and collective responsibility, we aim to create meaningful change.',
            'external_link': '/about/',
            'link_text': 'Read Foundation Creed',
            'order': 2,
        },
        {
            'title': 'Moving Step by Step — Reaching Deprived Families',
            'category': 'outreach',
            'author_name': 'Community Outreach',
            'author_role': 'Care & Share Sardhana',
            'image': 'media_posts/slide-ainuddin-2.jpg',
            'content': 'We strive to share the burden of the less fortunate, through the efforts of those who have more than enough resources. Grassroots volunteers actively mobilize aid and community support across Sardhana.',
            'external_link': '/gallery/',
            'link_text': 'View Society Gallery',
            'order': 3,
        },
        {
            'title': 'Every Contribution Brings Hope to Families in Need',
            'category': 'messages',
            'author_name': 'Mr. Ainuddin Shah Ji',
            'author_role': 'Senior Social Worker',
            'image': 'media_posts/ainuddin_shah.jpg',
            'content': 'Every contribution and helping hand of yours will be fully utilized to uplift communities and bring hope to families in need. Looking forward to your compassionate support and participation.',
            'external_link': '/people/',
            'link_text': 'Read Full Message',
            'order': 4,
        },
        {
            'title': 'Care & Share Society Sardhana — Guiding Leadership',
            'category': 'updates',
            'author_name': 'Society Administration',
            'author_role': 'Care & Share Sardhana',
            'image': 'media_posts/slide-ainuddin.jpg',
            'content': 'Dedicated to community welfare under the leadership of respected Senior Social Worker Ainuddin Shah Ji, upholding transparency, mutual support, and dignity for every individual.',
            'external_link': '/people/',
            'link_text': 'Meet People Behind',
            'order': 5,
        },
        {
            'title': 'Equal Opportunity to Live a Healthy & Dignified Life',
            'category': 'awareness',
            'author_name': 'Mr. Ainuddin Shah Ji',
            'author_role': 'Senior Social Worker',
            'image': 'media_posts/slide-ainuddin-2.jpg',
            'content': 'We strongly believe that every individual deserves an opportunity to live a healthy, dignified, and fulfilling life. We are all bound by our duty to society and to our fellow citizens.',
            'external_link': '/contact/',
            'link_text': 'Connect With Us',
            'order': 6,
        },
    ]
    for post in media_data:
        MediaPost.objects.create(**post)
    print(f"Populated {len(media_data)} Media posts in DB.")
else:
    print(f"MediaPost already has {MediaPost.objects.count()} items.")
