def add_time(start, duration, start_day = None):
    start_time, meridiem = start.split()
    start_hrs, start_mins = (int(num) for num in start_time.split(':'))
    dur_hrs, dur_mins = (int(num) for num in duration.split(':'))
    
    tot_mins = start_mins + dur_mins
    end_mins = str(tot_mins % 60).zfill(2)
    spillover_hrs = tot_mins // 60
    
    tot_hrs = start_hrs + dur_hrs + (12 if meridiem == 'PM' else 0) + spillover_hrs
    end_hrs = tot_hrs % 24
    end_meridiem = (' AM' if end_hrs // 12 == 0 else ' PM')
    end_hrs = end_hrs % 12
    if end_hrs == 0: end_hrs = 12
    end_hrs = str(end_hrs)
    spillover_days = tot_hrs // 24

    end_days = ''
    if start_day is not None:
        week_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
        end_day = week_days[(week_days.index(start_day.capitalize()) + spillover_days) % 7]
        end_days += ', ' + end_day
    if spillover_days == 1:
        end_days += ' (next day)'
    elif spillover_days > 1:
        end_days += (' (' + str(spillover_days) + ' days later)')

    new_time = end_hrs + ':' + end_mins + end_meridiem + end_days
    return new_time