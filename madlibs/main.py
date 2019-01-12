#!/usr/bin/env python

import jinja2
import webapp2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Note that there is no form field named 'game', so this is one value
        # you would have to pass in by the URL.
        template_vars = { 'name_of_madlib': self.request.get('madlib') }
        main_template = env.get_template('main.html')
        self.response.out.write(main_template.render(template_vars))
    def post(self):
        results_template = env.get_template('results.html')
        # The variables that are sent to results.html are those
        # that contain the input values from the main.html form with
        # names like noun1, activity, etc.
        template_variables = {
            'noun1':self.request.get("noun1"),
            'activity':self.request.get("activity"),
            'teacher':self.request.get("teacher"),
            'celebrity':self.request.get("celebrity"),
            'show':self.request.get("show"),
            'fun':self.request.get("fun"),
            "genre":self.request.get("genre"),
            "song":self.request.get("song"),
            "artist":self.request.get("artist")
        }
        self.response.out.write(results_template.render(template_variables))
    # Be sure to leave the "app=" lines that App Engine launcher created in place
    # below this code.

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
