#!/usr/bin/python

import random

from locust import HttpLocust, TaskSet, task
from pyquery import PyQuery

class RandomSitemapWalk(TaskSet):
    def on_start(self):
        self.sitemap_links = []
        self.sitemap_links.append('/?q=aboutus')
        self.sitemap_links.append('/?q=funding-partner')
        self.sitemap_links.append('/?q=contribute')
        self.sitemap_links.append('?q=community/all')
        self.sitemap_links.append('/?q=project')
        self.sitemap_links.append('/?q=project-page/oral-history')
        self.sitemap_links.append('/?q=project-page/heritage-education')
        self.sitemap_links.append('/?q=project-page/world-heritage-sites-india')
        self.sitemap_links.append('/?q=ajanta-caves')
        self.sitemap_links.append('/?q=living-legacies-film-chola-temples-thanjavur-and-kumbhakonam')

    @task(10)
    def load_page(self):
        url = random.choice(self.sitemap_links)
        r = self.client.get(url)

class AwesomeUser(HttpLocust):
    task_set = RandomSitemapWalk
    min_wait = 1  * 1000
    max_wait = 10 * 1000
