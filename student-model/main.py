#!/usr/bin/env python

import jinja2
import webapp2
from google.appengine.ext import ndb

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Note that there is no form field named 'game', so this is one value
        # you would have to pass in by the URL.
        self.response.out.write("I'm done")

        student = Student(
            name = "Adina Wallis",
            university = "U. Mich"
            )
        student.put()


class Student(ndb.Model):
    name = ndb.StringProperty()
    university = ndb.StringProperty()
    birthday = ndb.DateProperty()


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
