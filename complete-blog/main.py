import jinja2
import webapp2


env=jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))


class Blogasarus(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('Blogasarus.html')
        self.response.write(template.render())

class Jeremie(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('Jeremie.html')
        self.response.write(template.render())

class Jeremie_Favorite(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('Jeremie_Favorite.html')
        self.response.write(template.render())

class Trivia(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('Trivia.html')
        self.response.write(template.render())

class Contact(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('contact.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', Blogasarus),
    ("/all_about_me", Jeremie),
    ("/favorites", Jeremie_Favorite),
    ("/trivia", Trivia),
    ("/contact", Contact)
], debug=True)
