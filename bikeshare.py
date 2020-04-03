import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = {'monday':1
        , 'tuesday':2, 'wednesday':3, 'thursday':4, 'friday':5, 'saturday':6, 'sunday':0}
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please enter the City which you want to see \n')
    while True:
        if city.lower() not in CITY_DATA:
            city = input('please enter the city in following list \n [chicago, washigton, new york]\n') 
        else:
            city = city.lower()
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ' '
    while (month not in months) and month != 'all':
        month = input(
            "enter a valid month in 'january', 'february', 'march', 'april', 'may', 'june', 'all' :\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ' '
    while (day not in days) and day != 'all':
        day = input(
            "enter a valid day e.g. 'Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday' : \n").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    if month !='all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1 
        df = df[df['month']==month]
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == days[day]]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.strftime('%B')    
    common_month = df['month'].mode()[0]
    print('Most common month for bikeshare: ', common_month)
    
    # TO DO: display the most common day of week
    df['week'] = df['Start Time'].dt.dayofweek
    common_week = df['week'].mode()[0]
    print("Most common day of week of bikeshare: ",common_week)
    
 
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("Most common hour of bikeshare: ", common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common start station: ',common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common end statio: ',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combo'] = df['Start Station'] +' TO '+ df['End Station']
    commom_combo =df['combo'].mode()[0]
    print('Most common route bike sharers use is: ', commom_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time bike sharers travelled: ', df['Trip Duration'].sum(),'sec')
    # TO DO: display mean travel time
    print('Mean time bike sharers used bike share:',df['Trip Duration'].mean(),'sec' )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Types of Users:\n', user_types)
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('gender counts\n',gender)
    else:
        print('no gender data for this city')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        commom_yob = df['Birth Year'].mode()[0]
        print('Commom year of birth:\n', commom_yob)
    else:
        print('Birth year data is not availble for this city')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def displaysample(df):
    display =input('do you want to display 5 rows of the data frame? Enter Yes or No :\n').lower()
    count =0
    while display == 'yes':
        print(df.iloc[count:count + 5])
        display=input('do you want to display 5 more rows of the data frame? Enter Yes or No :\n')
        count+=5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        displaysample(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
