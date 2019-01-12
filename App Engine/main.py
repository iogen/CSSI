#!/usr/bin/env python

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello Jeremie, how are you?')
        self.response.write(' Don\'t fall asleep!!!!')

class AboutMeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("anything I wanted")

class CountHandler(webapp2.RequestHandler):
    def get(self):
        for i in range(1, 101):
            self.response.write(i)

app = webapp2.WSGIApplication([
    ('/', MainHandler), #http://localhost:8080/
    ('/about_me', AboutMeHandler), #http://localhost:8080/aboutme
    ('/count', CountHandler), #http://localhost8080:/count
], debug=True)
