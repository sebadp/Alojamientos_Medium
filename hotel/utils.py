# from datetime import datetime, timedelta
# from calendar import HTMLCalendar
# from .models import Booking

# class Calendar(HTMLCalendar):

#     def __init__(self, year=None, month=None):
#         self.year = year
#         self.month = month
#         super(Calendar, self).__init__()

# def formatday(self, day, bookings):
#   check_in_per_day = bookings.filter(check_in__day=day)
#   d = ''
#   for booking in check_in_per_day:
#     d += f'<li class="calendar_list"> {booking.get_html_url} </li>'
#   if day != 0:
#    return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
#   return '<td></td>'

# def formatweek(self, theweek, events):
#   week = ''
#   for d, weekday in theweek:
#     week += self.formatday(d, events)
#   return f'<tr> {week} </tr>'
# def formatmonth(self, withyear=True):
#   bookings = Booking.objects.filter(check_in__year=self.year, check_in__month=self.month)
#   cal = f'<table border="0" cellpadding="0" cellspacing="0"     class="calendar">\n'  
#   cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
#   cal += f'{self.formatweekheader()}\n'
#   for week in self.monthdays2calendar(self.year, self.month):
#     cal += f'{self.formatweek(week, bookings)}\n'  
#     return cal