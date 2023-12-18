import re
import pandas as pd

def preprocess(data):
    pattern = '\d{1,2}\/\d{1,2}\/\d{2},\s\d{1,2}:\d{2}\s(?:am|pm)'
    messages = re.split(pattern, data)
    msg = messages[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': msg, 'message_date': dates})
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p')
    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    m = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            m.append(entry[2])
        else:
            users.append('group_notification')
            m.append(entry[0])
    df['user'] = users
    df['message'] = m
    df.drop(columns=['user_message'], inplace=True)

    df['year'] = df['date'].dt.year
    df['only_date'] = df['date'].dt.date
    df['day_name'] = df['date'].dt.day_name()
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.date
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df

