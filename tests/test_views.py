from django.test import TestCase, override_settings
from django.urls import reverse

class RobotsTxtTestCase(TestCase):
    @override_settings(
        ROBOTS_SITEMAP_URL='https://example.com/sitemap.xml',
        ROBOTS_USE_SITEMAP=True,
        ROBOTS_RULES={
            '*': {
                'allow': ['/public/'],
                'disallow': ['/admin/'],
            },
        }
    )
    def test_robots_txt(self):
        response = self.client.get(reverse('robots_txt'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User-agent: *")
        self.assertContains(response, "Allow: /public/")
        self.assertContains(response, "Disallow: /admin/")
        self.assertContains(response, "Sitemap: https://example.com/sitemap.xml")