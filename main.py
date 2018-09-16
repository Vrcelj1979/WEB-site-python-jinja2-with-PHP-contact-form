import os
import jinja2
import webapp2



template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("main.html")

class O_namaHandler(BaseHandler):
    def get(self):
        return self.render_template("O_nama.html")

class CenovnikHandler(BaseHandler):
    def get(self):
        return self.render_template("Cenovnik.html")

class KonsultacijeHandler(BaseHandler):
    def get(self):
        return self.render_template("Konsultacije.html")

class LokacijeHandler(BaseHandler):
    def get(self):
        return self.render_template("Lokacije.html")

class Priprema_za_ispitHandler(BaseHandler):
    def get(self):
        return self.render_template("Priprema_za_ispit.html")

class Statisticka_analiza_podatakaHandler(BaseHandler):
    def get(self):
        return self.render_template("Statisticka_analiza_podataka.html")

class Ucenje_na_daljinuHandler(BaseHandler):
    def get(self):
        return self.render_template("Ucenje_na_daljinu.html")

class kurseviHandler(BaseHandler):
    def get(self):
        return self.render_template("kursevi.html")

class contactHandler(BaseHandler):
    def get(self):
        return self.render_template("index.php")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/O_nama', O_namaHandler),
    webapp2.Route('/Cenovnik', CenovnikHandler),
    webapp2.Route('/Konsultacije', KonsultacijeHandler),
    webapp2.Route('/Lokacije', LokacijeHandler),
    webapp2.Route('/Priprema_za_ispit', Priprema_za_ispitHandler),
    webapp2.Route('/Statisticka_analiza_podataka', Statisticka_analiza_podatakaHandler),
    webapp2.Route('/Ucenje_na_daljinu', Ucenje_na_daljinuHandler),
    webapp2.Route('/kursevi', kurseviHandler),
    webapp2.Route('/index.php', contactHandler),
], debug=True)
