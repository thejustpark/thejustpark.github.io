from pathlib import Path
from html.parser import HTMLParser

root = Path(__file__).parent / 'docs'
class Check(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('src', 'href') and value and not value.startswith(('https:', 'http:', 'mailto:', '#')):
                assert (root / value.split('#')[0]).exists(), value
for page in root.glob('*.html'):
    source = page.read_text()
    Check().feed(source)
    assert source.count('</html>') == 1
    assert source.count('aria-current="page"') == 1
    assert source.count('<li>') == source.count('</li>'), page
print('PASS: four pages, local assets and links, active navigation, and list markup')
