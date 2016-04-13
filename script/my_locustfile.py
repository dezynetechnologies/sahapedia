import random

from locust import HttpLocust, TaskSet, task
from pyquery import PyQuery

class WalkPages(TaskSet):
    def on_start(self):
        # assume all users arrive at the index page
        self.index_page()


    @task(10)
    def index_page(self):
        r = self.client.get("/")
        pq = PyQuery(r.content)
        link_elements = pq("a")
        print link_elements
        self.urls_on_current_page = []
        for l in link_elements:
          if "href" in l.attrib:
            self.urls_on_current_page.append(l.attrib["href"])

    @task(30)
    def load_page(self):
        #url = random.choice(self.urls_on_current_page)
        url = self.urls_on_current_page[1]
        r = self.client.get(url)


class AwesomeUser(HttpLocust):
    task_set = WalkPages
    #host = ""

    min_wait = 1  * 1000
    max_wait = 10 * 1000
