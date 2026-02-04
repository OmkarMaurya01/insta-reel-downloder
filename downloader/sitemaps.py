from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = "daily"

    def items(self):
        return [
            'index',
            'download_video',
        ]

    def location(self, item):
        return reverse(item)
