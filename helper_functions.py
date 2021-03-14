import pandas as pd


def null_count(df):
    print(df.isnull().sum().sum())


def split_dates(date_series):
    month = date_series.dt.month
    day = date_series.dt.day
    year = date_series.dt.year
    frame = {"month": month, "day": day, "year": year}
    output = pd.DataFrame(frame)
    print(output)
