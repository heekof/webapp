import cgi
import string
import re

# -----------
# User Instructions
#
# Modify the valid_month() function to verify
# whether the data a user enters is a valid
# month. If the passed in parameter 'month'
# is not a valid month, return None.
# If 'month' is a valid month, then return
# the name of the month with the first letter
# capitalized.
#

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

lowercase_month = [x.lower() for x in months]

def valid_month(month):
    if month.lower() in lowercase_month:
        return months[lowercase_month.index(month.lower())]
    else:
        return None



# print valid_month("january")
# => "January"
# print valid_month("January")
# => "January"
# print valid_month("foo")
# => None
# print valid_month("")
# => None
# -----------
# User Instructions
#
# Modify the valid_day() function to verify
# whether the string a user enters is a valid
# day. The valid_day() function takes as
# input a String, and returns either a valid
# Int or None. If the passed in String is
# not a valid day, return None.
# If it is a valid day, then return
# the day as an Int, not a String. Don't
# worry about months of different length.
# Assume a day is valid if it is a number
# between 1 and 31.
# Be careful, the input can be any string
# at all, you don't have any guarantees
# that the user will input a sensible
# day.
#
# Hint: The string function isdigit() might be helpful.

def valid_day(day):
    if day.isdigit() and ( int(day) < 32 and int(day) > 0 ):
        return int(day)



# print valid_day('0')
# => None
# print valid_day('1')
# => 1
# print valid_day('15')
# => 15
# print valid_day('500')
# => None

# -----------
# User Instructions
#
# Modify the valid_year() function to verify
# whether the string a user enters is a valid
# year. If the passed in parameter 'year'
# is not a valid year, return None.
# If 'year' is a valid year, then return
# the year as a number. Assume a year
# is valid if it is a number between 1900 and
# 2020.
#

def valid_year(year):
    if year.isdigit():
        year = int(year)
        if year <= 2020 and year >= 1900:
            return year


#print valid_year('0')
#=> None
#print valid_year('-11')
#=> None
#print valid_year('1950')
#=> 1950
#print valid_year('2000')
#=> 2000

# User Instructions
#
# Implement the function escape_html(s), which replaces
# all instances of:
# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string
# Note that your browser will probably automatically
# render your escaped text as the corresponding symbols,
# but the grading script will still correctly evaluate it.
#


def escape_html(s):
    return cgi.escape(s,quote=True)


# print escape_html('>')
# print escape_html('<')
# print escape_html('"')
# print escape_html("&")

def ROT13(s):

    alpha_lower = list(string.ascii_lowercase)
    alpha_upper = list(string.ascii_uppercase)
    punc = list(string.punctuation)

    car = []

    tag_open = False

    for c in s:
        if c == '<':
            tag_open = True
        elif c == '>':
            tag_open = False

        if c in punc or c.isdigit() or c == " " or c == "\n": # or tag_open:
            car.append(c)
        else:
            if c in alpha_lower:
                car.append(alpha_lower[(alpha_lower.index(c) + 13) % 26])
            elif c in alpha_upper:
                car.append(alpha_upper[(alpha_upper.index(c) + 13) % 26])
    return ''.join(car)



def check_username(username):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    if USER_RE.match(username):
        return True


def check_email(email):
    EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
    if EMAIL_RE.match(email):
        return True

def check_password(password1):
    PASS_RE = re.compile(r"^.{3,20}$")
    return PASS_RE.match(password1)




if __name__ == "__main__":
    print check_password("Heekof")