# -*- coding: utf-8 -*-

# Scrapy settings for myBot project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'myBot'

SPIDER_MODULES = ['myBot.spiders']
NEWSPIDER_MODULE = 'myBot.spiders'

from django.core.wsgi import get_wsgi_application

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'myBot (+http://www.yourdomain.com)'
import sys
sys.path.append('/Users/Thorri/Desktop/githubRepos/imdbScrapper/mysite')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#Added because of a model were not lodaded
#http://stackoverflow.com/questions/25537905/django-1-7-throws-django-core-exceptions-appregistrynotready-models-arent-load
application = get_wsgi_application()

ITEM_PIPELINES = {
    'myBot.pipelines.MybotPipeline': 1000,
}