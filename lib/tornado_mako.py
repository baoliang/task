import os
import settings
import mako
import tornado

from mako.template import Template
from mako.lookup import TemplateLookup
mako.runtime.UNDEFINED = ''
 
from mako.exceptions import TemplateLookupException
 
from tornado.web import RequestHandler
 
class LyRequestHandler(RequestHandler):
 
    lookup = TemplateLookup(["./template"])
 
    def render(self, template_name, **kwargs):
        """ Redefine the render """
 
        t = self.lookup.get_template(template_name)
 
        args = dict(
            handler=self,
            request=self.request,
            current_user=self.current_user,
            locale=self.locale,
            _=self.locale.translate,
            static_url=self.static_url,
            xsrf_form_html=self.xsrf_form_html,
            reverse_url=self.application.reverse_url,
            LANGUAGES=settings.LANGUAGES,
            STATIC_URL=settings.STATIC_URL,
            THEME_URL=settings.THEME_URL
        )
 
        args.update(kwargs)
 
        html = t.render(**args)
        self.finish(html)