# Index(['Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year'], dtype='object')

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
DAY_DATA = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

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
    while True:
        city = input("Which city do you want to explore? (Chicago, New York City, Washington)").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city. Please choose from Chicago, New York City, or Washington.")
    print("We are accessing the data for {}!".format(city.title()))

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month do you want to look into? (All, January, February, ... , June)").lower()
        if month in MONTH_DATA:
            break
        else:
            print("Invalid month. Please choose from All, January, February, March, April, May, or June.")
    if month == 'all':
        print("We are looking at all months!")
    else:
        print("We are looking at {}!".format(month.title()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day of the week do you want to look into? (All, Monday, Tuesday, ... Sunday)").lower()
        if day in DAY_DATA:
            break
        else:
            print("Invalid day of the week. Please choose from All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday.")
    if day == 'all':
        print("We are looking at all days of the week!")
    else:
        print("We are looking at {}!".format(day.title()))


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


    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    
    print('Most popular month:', popular_month)    	

    # TO DO: display the most common day of week.
    popular_dow = df['day_of_week'].mode()[0]
    
    print('Most popular day of the week:', popular_dow) 

    # TO DO: display the most common start hour
    # group by hour, count and sort by count. Display top 1
    ## extract hour from the Start Time column to create an hour column
    df['start_hour'] = df['Start Time'].dt.hour

    ## find the most popular hour
    popular_sh = df['start_hour'].mode()[0]
    
    print('Most popular start hour:', popular_sh)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # 'Start Station', 'End Station'
    # TO DO: display most commonly used start station
    popular_station1 = df['Start Station'].mode()[0]
    
    print('Most common start station:', popular_station1)  

    # TO DO: display most commonly used end station
    popular_station2 = df['End Station'].mode()[0]
    
    print('Most common end station:', popular_station2) 

    # TO DO: display most frequent combination of start station and end station trip
    df['Route'] = df['Start Station'] + ' - ' + df['End Station']
    popular_route = df['Route'].mode()[0]
    
    print('Most popular route:', popular_route) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Duration Seconds'] = (df['End Time'] - df['Start Time']).dt.total_seconds()
    df['Duration'] = df['Duration Seconds']
    print('Total travel time:', df['Duration'].sum())
    

    # TO DO: display mean travel time
    print('Mean travel time:', df['Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df:
        customers = len(df[df['User Type'] == 'Customer'])
        subscribers = len(df[df['User Type'] == 'Subscriber'])
        print('There have been ', customers, ' rentals by customers and ', subscribers, ' rentals by subscribers.')
    else:
        print('No user type information available.')

    # TO DO: Display counts of gender
    if 'Gender' in df:
        male_users = len(df[df['Gender'] == 'Male'])
        female_users = len(df[df['Gender'] == 'Female'])
        print('There have been ', female_users, ' female users and ', male_users, ' male users.')
    else:
        print('No gender information available.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        latest_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()
        print('Earliest birth year of any user: ', earliest_birth_year)
        print('Most recent birth year of any user: ', latest_birth_year)
        print('Most common birth year of all users: ', most_common_birth_year)
    else:
        print('No year of birth information available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Displays raw data, five rows per input."""
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
