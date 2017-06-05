import webapp2
import utils as U
import jinja2
import os
import sys

sys.path.insert(1, '/home/jaafar/google-cloud-sdk/platform/google_appengine')
sys.path.insert(1, '/home/jaafar/google-cloud-sdk/platform/google_appengine/lib/yaml/lib')
sys.path.insert(1, 'lib')

#if 'google' in sys.modules:
#   del sys.modules['google']

from google.appengine.ext import db




print db.__doc__

"""
A template library is a library for building complicated strings !

A database is a program that stores and retrieves large amounts of structured data

"""



template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)
#
#
#

form = """
<form method="get">

  <b> Sign up </b>
  <br>
  <label> Username
  <input type="text" name="username" value="%(username)s" >
  </label>

  <div style="color : red" >  %(username_error)s  </div>

  <label>
  Password
  <input type="password" name="password" >

  </label>

   <div style="color : red" >  %(password_error)s </div>

  <label>
  Verify Password
  <input type="password" name="password2" >
  </label>


  <label>
  Email (optional)
  <input type="text" name="email" value="%(email)s" >
  </label>

  <div style="color : red" >  %(email_error)s  </div>



  <input type="submit">
</form>

"""

form13 = """
<form method="post">

  Type some text
  <br>
  <label>
  <textarea name="text" rows="20" cols="50" >%(text)s
  </textarea>
  </label>
  <br>
  <br>

  <input type="submit">
</form>

"""


hidden_html="""
<input type="hidden" name="food" value="%s">

"""

shopping = """

<br><br>
<h2> shopping list </h2>
<ul>
%s
</ul>
"""

class Handler(webapp2.RequestHandler):


    def render_str(self, template, **params):
         t = jinja_env.get_template(template)
         return t.render(params)

    def render(self, template, **kw):
         self.write(self.render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class MainPage(Handler):


    def get(self):
        self.write("Home page")


class FizzBuzzHandler(Handler):


    def get(self):
        n = self.request.get("n")
        if n:
            n = int(n)
            self.render("fizzbuzz.html", n=n)
        else:
            self.render("fizzbuzz.html", n=0)



class Rot13Handler(webapp2.RequestHandler):
    def write_form(self, text=""): #, month="", day="", year="" ):
        self.response.write(form13 % { "text": U.escape_html(U.ROT13(text))}) #% { "error": error, "month": U.escape_html(month), "day": U.escape_html(day), "year": U.escape_html(year) })


    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.write_form()

    def post(self):
        texts = self.request.get("text")
        self.write_form(text=texts)

class SignupHandler(webapp2.RequestHandler):

    def write_form(self, username="", email="", email_error="", password_error="", username_error=""): #, month="", day="", year="" ):
        self.response.write(form % { "username": U.escape_html(username), "email":U.escape_html(email), "email_error": email_error, "username_error": username_error, "password_error": password_error })


    def get(self):

        self.response.headers['Content-Type'] = 'text/html'
        self.write_form()


    def post(self):

        username = self.request.get("username")
        password = self.request.get("password")
        password2 = self.request.get("password2")
        email = self.request.get("email")

        if not U.check_username(username):
            self.write_form(username_error="Username invalid", username=username)
        elif (password != password2) or (not U.check_password(password)):
            self.write_form(password_error='Passwords do not match !')
        elif email:
            if not U.check_email(email):
                self.write_form(email_error='email incorrect', email=email)
            else:
                self.redirect("/welcome")
        else:
            self.redirect("/welcome")


class ThanksHandler(webapp2.RequestHandler):

    def get(self):
        self.response.out.write("Thanks!")


class WelcomeHandler(webapp2.RequestHandler):

    def get(self):
        self.response.out.write("Welcome!")

class AsciiHandler(Handler):
    def get(self):
        self.render_front()

    def render_front(self, title="", art="", error=""):
        arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC ")
        self.render("front.html", title=title, art=art, error=error, arts=arts)

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        if title and art:
            #self.write("THANKS !")
            a = Art(title=title, art=art)
            a.put()
            self.redirect("/ascii")
        else:
            error = "we need both a title and some artwork !"
            self.render_front(title, art, error)

class Art(db.Model):
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)


class BlogHandler(Handler):
    pass

app = webapp2.WSGIApplication([('/', MainPage),('/blog',BlogHandler),("/ascii",AsciiHandler),("/fizzbuzz",FizzBuzzHandler),("/rot13",Rot13Handler),("/signup",SignupHandler),("/thanks",ThanksHandler),("/welcome",WelcomeHandler)], debug=True)
