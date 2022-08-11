import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello You! Let\'s explore some US bikeshare data!')
<<<<<<< HEAD
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
=======
    # TO DO: get user input for city (chicago, new york city, washington). 
>>>>>>> refactoring
    while True:
        city_list = ['chicago', 'new york city','washington']
        city = str(input("\n \nPlease type the name of the city you want to analyse! \nPlease write it correctly like 'Chicago', 'New york city' or 'Washington': \nYour input: ")).lower()
        if city in city_list:
          print("\n --> Thanks, now we got: {}.".format(city.title()))
          break
        else:
            print("\n --> {} is not valid!\nPlease try it once more. Look at the right writing!".format(city.title()))
            
     
    
     # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month_list = ['january','february','march','april','may','june','all']
        month = str(input("\nWhich month would you like to analyse? \n'january','february','march','april','may','june' or 'all'\nYour input: ")).lower()
        if month == 'all':
            print("\n --> Now you see the data for all month for data we have!")
            break
        elif month in month_list:
            print("\n --> Now you see the data for {}!".format(month.title()))
            break
        else: 
           print("\n --> {} is not valid!\nPlease try it once more. Look at the right writing".format(month))
   
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
        'saturday', 'sunday', 'all']
        day = str(input("\nWhich day you wanna explore?\n'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday' or 'all'?\n Your input: ".lower()))
        if day == 'all':
            print("\n --> Now you see the data for all days!")
            break
        elif day in day_list:
            print("\n --> Now you see the data for {}!".format(day.title()))
            break
        else:
            print("\n --> {} is not valid!\nPlease try it once more. Look at the right writing".format(day))

    print('-'*60)
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
    print("\n Loading data...")
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month_list = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month_list.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
   
#returns all selections as dataframe (df)
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print('-'*40)
    
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("\nThe most frequent month is: {}.\n(Month: 1:January 2:February 3:March 4:April 5:May 6:June)".format(popular_month))
    print('-'*20)
    
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("\nThe most frequent day is: {}".format(popular_day))
    print('-'*20)

    # TO DO: display the most common start hour
    # Create an hour culomn
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("\nThe most frequent hour is: {}:00hrs".format(popular_hour))
    print('-'*20)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print('-'*40)

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("\nThe most commonly used start station is: {}.".format(popular_start_station))
    print('-'*20)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("\nThe most commonly used end station is: {}.".format(popular_end_station))
    print('-'*20)

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['Start Station']+" "+"to"+" "+df['End Station']
    popular_route = df['route'].mode()[0]
    print("\nThe most commonly used route is: {}.".format(popular_route))
    print('-'*20)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
        


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print('-'*40)
          
    # TO DO: display total travel time
    trip_sum =df['Trip Duration'].sum()
    print("\n The total trip duration in this dataset is: {:,.2f}secounds.\n That means:\n {:,.2f} minute(s) or \n {:,.2f} hour(s) or \n {:,.2f} day(s)".format(trip_sum, trip_sum/60, trip_sum/60/60, trip_sum/60/60/24))
    print('-'*20)
          
    # TO DO: display mean travel time
    avg_duration = df['Trip Duration'].mean()
    print("\n The average trip duration is: {:,.2f} minutes.".format(avg_duration/60))
    print('-'*20)
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print('-'*20)
          
    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print("\n There are \n{}.".format(user_count))
    print('-'*20)
    
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("\nThe count of each gender are: \n{}.".format(gender))
        print('-'*20)
    except:
        print("\nThere ist no gender data in this dataset.")      
    print('-'*20)
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode()[0])
        print("\nThe earlies year of birth: {}.\nThe recent year of birth {}. \nThe most common year of birth: {}.".format(earliest, recent, common))
        print('-'*20)
    except:
        print("\nThere ist no birth year data in this dataset.")
        print('-'*20)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    # TO DO: get user input for raw data (yes or no, yes then 5 rows)
    ''' Ask user if he want to see more raw data (in 5 row blocks)
        Input: yes or no, if yes ask for more 5 rows'''
    while True:
        choice_list = ['yes','no']
        choice = str(input("\nWould you see more raw data in blocks of 5 entries? \nyes or no\nYour input: ")).lower()
        if choice in choice_list:
            if choice == 'yes':
                begin = 0
                end = 5
                dataframe = df.iloc[begin:end,:9]
                print(dataframe)
            break
        else:
           print("\n --> {} is not valid!\nPlease try it once more.")
    if choice == 'yes':
        while True:
            choice_2 = str(input("\nWould you see even more raw data in blocks of 5 entries? \nyes or no\nYour input: ")).lower()
            if choice in choice_list:
                if choice_2 == 'yes':
                    begin += 5
                    end += 5
                    dataframe = df.iloc[begin:end,:9]
                    print(dataframe)
                else:
                    break
            else:
                print("\n --> {} is not valid!\nPlease try it once more.")
    
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
