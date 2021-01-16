import datetime
# Calculate parking time rounded
def DtCalc(stTime, edTime):
    st=datetime.datetime.strptime(stTime, "%Y-%m-%d %H:%M")
    ed=datetime.datetime.strptime(edTime, "%Y-%m-%d %H:%M")
    rtn = ed -st
    y=round(rtn.total_seconds()/60/60)
    # Judge the parking time
    if y == 0:
        y = 1
    return y

# Return the day mark 0 for Monday, 1 for Tuesday. 6 for Sunday.
def get_week_numbeer(date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
    day = date.weekday()
    return day