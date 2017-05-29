import webapp2
import utils as U


form = """
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


class MainPage(webapp2.RequestHandler):

    def write_form(self, text=""): #, month="", day="", year="" ):
        self.response.write(form % { "text": U.escape_html(U.ROT13(text))}) #% { "error": error, "month": U.escape_html(month), "day": U.escape_html(day), "year": U.escape_html(year) })


    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.write_form()

    def post(self):
        texts = self.request.get("text")
        self.write_form(text=texts) #, month=user_month, year=user_year, day=user_day)


class ThanksHandler(webapp2.RequestHandler):

    def get(self):
        self.response.out.write("Thanks! thats a valid day")


app = webapp2.WSGIApplication([('/', MainPage),("/thanks",ThanksHandler)], debug=True)
