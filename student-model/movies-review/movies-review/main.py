import jinja2
import webapp2

env=jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))


class MainHandler(webapp2.RequestHandler):
    def get(self):
    #make sure you have the correct html file name here
        template = env.get_template('hello.html')
        variables = {"name": self.request.get("name"), "length": self.request.get("length"), "num_reviews":int(self.request.get("num_reviews")), "stars":int(self.request.get("stars"))}
        self.response.out.write(template.render(variables))

app = webapp2.WSGIApplication([
    ('/movies', MainHandler)
], debug=True)
