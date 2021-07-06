import logging
import urllib

import requests
from requests_html import HTML
from requests_html import HTMLSession


class GScrapper:
    google_domains = ('https://www.google.',
                      'https://google.',
                      'https://webcache.googleusercontent.',
                      'http://webcache.googleusercontent.',
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".IsZvec"

    def __init__(self, engine=None):
        self.engine = engine or 'https://www.google.com.ua'
        self.search_url = f'{self.engine}/search?q='
        self.logger = logging.getLogger(self.__class__.__name__)

    def _get_search_url(self, query):
        return self.search_url + query

    def _get_source(self, search_url):

        try:
            session = HTMLSession()
            response = session.get(search_url)
            return response
        except requests.exceptions.RequestException as e:
            self.logger.error(e)

    def _get_results(self, query):
        query = urllib.parse.quote_plus(query)
        search_url = self._get_search_url(query)
        return self._get_source(search_url)

    def _parse_response(self, response) -> list:
        output = []
        results = response.html.find(self.css_identifier_result)
        for result in results:
            output.append({
                'title': result.find(self.css_identifier_title, first=True).text,
                'link': result.find(self.css_identifier_link, first=True).attrs['href'],
                'text': result.find(self.css_identifier_text, first=True).text
            })
        return output

    def get_search_results(self, query) -> list:
        response = self._get_results(query)
        return self._parse_response(response)
