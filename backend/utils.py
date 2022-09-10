from lib2to3.pgen2.parse import ParseError
import string
from urllib.parse import urlparse
from secrets import choice

class URLShortener:

    def create_short_alias(self, len: int=6):
        """Create randomized sequence of ascii letters and strings of length of 'len' parameter"""
        return ''.join([choice(string.ascii_letters + string.digits) for _ in range(len)])
    
    def validate_url(self, url: str):
        validated_url = urlparse(url)
        if not "://" or 'mailto:' in url:
            raise ParseError("Not a valid URL, schema is missing")
        if not validated_url.hostname:
            raise ParseError("Not a valid URL, host name is missing")
        return f"{validated_url.scheme if validated_url.scheme else 'http'}://{validated_url.netloc}{validated_url.path}{f'?{validated_url.query}' if validated_url.query else ''}{f'#{validated_url.fragment}' if validated_url.fragment else ''}"
