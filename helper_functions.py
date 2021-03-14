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

class CustomDF(pd.DataFrame):
    def __init__(self, filename):
        super().__init__(pd.read_csv(filename))

    # print('Class Instantiated')

    def nullcount(self):
        print('This code is getting run')
        return self.isnull().sum().sum()

    def split_dates(self):
        month = self.dt.month
        day = self.dt.day
        year = self.dt.year
        frame = {"month": month, "day": day, "year": year}
        output = self.DataFrame(frame)
        return output

if __name__ == '__main__':

    # instantiating object for the purpose of testing nullcount method in class CustomDF
    print('Running First line')
    # import file
    df_forest = CustomDF('ForestCover.csv')
    print('First line of code executed')
    # new_df_obj = New_DataFrame(df_new)
    # null_counted = new_df_obj.nullcount()
    print('DF: ', df_forest)
    #test method
    nullcounts = df_forest.nullcount()

    #instantiating another object for the purpose of testing split_dates method in class CustomDF
    #import file
    df_dates = CustomDF('Dates.csv')
    # test method
    df_dates_changed = df_dates.split_dates()
    print('The new df with changed dates is:', df_dates_changed)

