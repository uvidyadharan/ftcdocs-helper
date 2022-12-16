#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sphinx.errors import ExtensionError


def add_cb_javascript(app, pagename, templatename, context, doctree):
    if not app.config.googleanalytics_enabled:
        return

    metatags = context.get('metatags', '')
    metatags += """
    <!-- Start of HubSpot Embed Code MKT -->
    <script type="text/javascript" id="hs-script-loader" async defer src="//js.hs-scripts.com/1747660.js"></script>
    <!-- End of HubSpot Embed Code MKT -->
    """
    context['metatags'] = metatags

def setup(app):
    app.add_config_value('cookiebanner_enabled', True, 'html')
    app.connect('html-page-context', add_cb_javascript)

