import webapp2
import json
import urllib2
import urllib
import jinja2
from google.appengine.api import users


env=jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))


class Account(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('account.html')
        self.response.write()



class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">  Sign in or register <style> <div class="g-signin2" data-onsuccess="onSignIn"></div> </style>  </a>.' %
                users.create_login_url('/'))

        self.response.write('<html><body>%s</body></html>' % greeting)




app = webapp2.WSGIApplication([
    ('/', Account)
], debug=True)
