# Django Robots.txt Manager
A reusable Django package to dynamically generate and manage `robots.txt`.

## Introduction
The `django_robots_txt` package allows you to dynamically generate and manage the `robots.txt` file for your Django project. It provides flexibility to define custom rules for different user-agents, include sitemaps, and easily configure settings.

## Features
- **Dynamic Generation :** Generate `robots.txt` dynamically based on your project's settings.
- **Custom Rules :** Define allow/disallow rules for specific user-agents (e.g., Googlebot, Bingbot).
- **Sitemap Support :** Easily include a sitemap URL in your `robots.txt`.
- **Highly Configurable :** Customize rules and settings via Django's `settings.py`.
- **Reusable :** Designed as a reusable Django app for easy integration into any project.


## Installation
Install the package using `pip`:

```bash
pip install django-robots-txt
```

Alternatively, if you're installing from a local source:

```bash
pip install -e /path/to/django-robots-txt
```


## Configuration
**1- Add to** `INSTALLED_APPS` **:**

Add `'django_robots_txt'` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django_robots_txt',
]
```

**2- Configure Settings :**
Configure the following settings in your `settings.py`:

```python
# Optional: Sitemap URL
ROBOTS_USE_SITEMAP = True  # Optional: Whether to include the sitemap
ROBOTS_RULES = {
    '*': {  # Default rules for all user-agents
        'allow': ['/public/', '/blog/'],
        'disallow': ['/admin/', '/private/'],
    },
    'Googlebot': {  # Custom rules for Googlebot
        'allow': ['/google-only/'],
        'disallow': ['/no-google/'],
    },
}
```
**3- Include URLs :**
Include the package's URLs in your project's `urls.py`:

from django.urls import include, path

```python
urlpatterns = [
    ...
    path('', include('django_robots_txt.urls')),
]
```
## Usage
After configuration, visit `/robots.txt` in your browser to see the dynamically generated file. For example:

```bash
User-agent: *
Allow: /public/
Allow: /blog/
Disallow: /admin/
Disallow: /private/

User-agent: Googlebot
Allow: /google-only/
Disallow: /no-google/

Sitemap: https://example.com/sitemap.xml
```

## Advanced Usage
**1- Customizing Rules**
You can define complex rules for multiple user-agents. For example:

```python
ROBOTS_RULES = {
    '*': {
        'allow': ['/public/'],
        'disallow': ['/admin/', '/private/'],
    },
    'Googlebot': {
        'allow': ['/google-only/'],
        'disallow': ['/no-google/'],
    },
    'Bingbot': {
        'disallow': ['/bing-disallowed/'],
    },
}
```
**2- Disabling Sitemap**
If you don't want to include a sitemap, set `ROBOTS_USE_SITEMAP` to `False`:

```python
ROBOTS_USE_SITEMAP = False
```

## Testing
The package includes unit tests to ensure its functionality. To run the tests:

1- Install the development dependencies:

```bash
pip install -r requirements-dev.txt
```

2- Run the tests:

```bash
python manage.py test django_robots_txt.tests
```

## Documentation

[Persian Documentation](https://uncoder.org)
