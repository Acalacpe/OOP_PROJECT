def timeFormat(time):
    def plural(value, unit):
        return f"{value} {unit}" + ("s" if value != 1 else "")

    if time < 60:
        return plural(time, "second")
    elif time < 3600:
        minutes = time // 60
        seconds = time % 60
        return f"{plural(minutes, 'minute')} {plural(seconds, 'second')}"
    elif time < 86400:
        hours = time // 3600
        minutes = (time % 3600) // 60
        return f"{plural(hours, 'hour')} {plural(minutes, 'minute')}"
    else:
        days = time // 86400
        remaining = time % 86400
        hours = remaining // 3600
        remaining %= 3600
        minutes = remaining // 60
        seconds = remaining % 60

        result = f"{plural(days, 'day')} {plural(hours, 'hour')}"
        if minutes > 0:
            result += f" {plural(minutes, 'minute')}"
        if seconds > 0:
            result += f" {plural(seconds, 'second')}"
        return result