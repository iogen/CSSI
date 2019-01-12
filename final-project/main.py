import jinja2
import webapp2


env=jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))


class Music(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('music.html')
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/Music', Music),

], debug=True)
