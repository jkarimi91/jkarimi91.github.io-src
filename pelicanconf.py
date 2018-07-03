#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

AUTHOR = u'Jay Karimi'
SITENAME = u'Jay Karimi'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = False
THEME = 'theme'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Create a dedicated page for blog listings instead of using the homepage
# i.e. root url. This allows us create a homepage.
ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLES_PATH = ['blog']
INDEX_SAVE_AS = 'blog/index.html'
INDEX_URL = '/blog'

# Used in blog listing page i.e. index.html.
DEFAULT_DATE_FORMAT = '%b %d %Y'

# Used for copyright notice.
CURRENT_YEAR = datetime.datetime.now().year

# Used for adding images to blog posts
STATIC_PATHS = ['images']
