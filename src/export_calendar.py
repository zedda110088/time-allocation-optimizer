import pandas as pd
from datetime import datetime, timedelta
from ics import Calendar, Event

def export_opt_to_ics(opt: pd.Series,
                      filename: str = "optimal_schedule.ics",
                      week_start=None,
                      day_start_hour: int = 8) -> str:
    """
    Export optimal weekly hours (opt) to .ics (basic version):
      - Split weekly hours evenly into 7 days
      - Schedule daytime blocks first, Sleep at night
    """
    # 1) Define the starting week (default: next Monday)
    if week_start is None:
        today = datetime.utcnow().date()
        week_start = today + timedelta(days=(7 - today.weekday()) % 7)

    # 2) Split weekly hours evenly across 7 days
    per_day = (opt / 7).to_dict()

    # 3) Order of activities: daytime first, Sleep later
    order = [a for a in ["Classes","Study_1","Study_2","Research_Project",
                         "Exercise","Study_3","Social","Sleep"]
             if a in per_day and per_day[a] > 1e-6]

    cal = Calendar()

    for d in range(7):
        # Start of the day (00:00)
        day0   = datetime.combine(week_start + timedelta(days=d), datetime.min.time())
        cursor = day0 + timedelta(hours=day_start_hour)
        sleep_hours = 0.0

        # Schedule non-sleep activities during the day
        for act in order:
            hours = float(per_day[act])
            if hours <= 0: 
                continue
            if act == "Sleep":
                sleep_hours = hours
                continue
            e = Event(name=act)
            e.begin, e.end = cursor, cursor + timedelta(hours=hours)
            cal.events.add(e)
            cursor = e.end

        # Schedule sleep at night (~23:00)
        if sleep_hours > 0:
            sleep_start = day0 + timedelta(hours=23 - max(0, sleep_hours - 1))
            e = Event(name="Sleep")
            e.begin, e.end = sleep_start, sleep_start + timedelta(hours=sleep_hours)
            cal.events.add(e)

    # 4) Write the .ics file
    with open(filename, "w") as f:
        f.writelines(cal.serialize_iter())
    print(f"ICS saved to: {filename}")

    # 5) Auto-download in Colab (fallback to manual download otherwise)
    try:
        from google.colab import files
        files.download(filename)
    except Exception:
        print("If not in Colab, manually download the file from the current working directory.")

    return filename
