import webapp2
import utils as U


error_message = ""
form = """
<form method="post">

  What is your birthday?
  <br>
  <label>
  day
  <input type="text" name=day value="%(day)s">
  </label>
  <label>
  month
  <input type="text" name=month value="%(month)s">
  </label>
  <label>
  year
  <input type="text" name=year value="%(year)s">
  </label>
  <br>
  <br>
  <div style="color : red" > %(error)s </div>

  <input type="submit">
</form>

"""


class MainPage(webapp2.RequestHandler):

    def write_form(self, error="", month="", day="", year="" ):
        self.response.write(form % { "error": error, "month": U.escape_html(month), "day": U.escape_html(day), "year": U.escape_html(year) })

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year =     self.request.get('year')

        if not ( U.valid_day(user_day) and U.valid_month(user_month) and U.valid_year(user_year) ):
            self.write_form("That doesn't look OK !", month=user_month, year=user_year, day=user_day)
        else:
            self.redirect("/thanks")
class ThanksHandler(webapp2.RequestHandler):

    def get(self):
        self.response.out.write("Thanks! thats a valid day")


app = webapp2.WSGIApplication([('/', MainPage),("/thanks",ThanksHandler)], debug=True)
