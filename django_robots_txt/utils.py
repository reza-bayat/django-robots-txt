from django.conf import settings

def generate_robots_content():
    sitemap_url = getattr(settings, 'ROBOTS_SITEMAP_URL', '/sitemap.xml')
    use_sitemap = getattr(settings, 'ROBOTS_USE_SITEMAP', True)
    rules = getattr(settings, 'ROBOTS_RULES', {})

    lines = []

    for robot, rule in rules.items():
        lines.append(f"User-agent: {robot}")
        if 'allow' in rule:
            for path in rule['allow']:
                lines.append(f"Allow: {path}")
        if 'disallow' in rule:
            for path in rule['disallow']:
                lines.append(f"Disallow: {path}")
        lines.append("") 

    if use_sitemap:
        lines.append(f"Sitemap: {sitemap_url}")

    return "\n".join(lines)