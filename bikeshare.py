import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }
city = ''
month_index = {'All':0, 'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'None':7}
day_index = {'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'}
month = 0
day = 0
filter_data = 0
filters = {'Month', 'Day', 'All'} 
    
# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
def get_city():
    while True:
      city = str(input('\n Would you like to view data for Washington, New York or Chicago?\n'))
      selected_file = ''
      if city.lower() not in ('washington', 'new york', 'chicago'):
        print ('Oops! It seems like you\'ve chosen an invalid city. Please try again')
      elif city.lower() == 'washington': 
          selected_file = 'Washington'
          #return 'washington.csv'
          break
      elif city.lower() == 'chicago':
          selected_file = 'Chicago'
          break
      elif city.lower()== 'new york':
          selected_file = 'New York City'
          break
        
    return selected_file

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    
   
    # MONTH INPUT
    # get user input for month (all, january, february, ... , june)
    filter_data = str(input('\nWould you like to view data by month or day? Type all for no filter\n'.title()))
    
    while True:
        if filter_data in filters:
            break
        else:
            print('Oops! looks like you\'re input is invalid. Please try again.')
            filter_data = input()
            
    if filter_data == 'all':
        month = 'all'
        day = 'all'
    elif filter_data == 'Month':
        day = 'all'
        month = str(input('\n Please choose between the months January, Febuary, March, April, May, June. \n'.title()))
        while True:
            if month in month_index:
                break
            else:
                print('\nOops! you\'re input is invalid. Please choose a month between January and June\n')
                month = input()
# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)              
    else:
        month = 'all'
        day = str(input('\nWould yo like to view data for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?\n'.title()))
        while True:
            if day in day_index:
                break
            else:
                print('\nOops! that input is invalid. Please try again.')
                day = input()


    


    print('-'*40)
    #print(selected_file, month, day, filter_data)
    return month, day, filter_data


def load_data(selected_file, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    
    df = pd.read_csv(CITY_DATA[selected_file], parse_dates = ['Start Time', 'End Time'])
    df['Trip'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    return df
        
    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y-%m-%d %H:%M:%S')  
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day


    if data_filter == 'Month':
        #df_filtered = df[df.month == month]
        df_filtered = df.filter(items=['Month'])
        return df_filtered
    elif data_filter == 'Day':
        df_filtered = df[df.day == day]
        return df_filtered
    else:
        return df
   
def get_most_popularMonth(df):
    print('\nCalculating The Most Common Month of Travel...\n')
    start_time = time.time()
    
    months_worded = ["January", "February", "March", "April", "May", "June"]
    pop_month_index = int(df['start_time'].dt.month.mode())
    pop_month_worded = months_worded[pop_month_index - 1]
    print('Most Popular Month is {}'.format(pop_month_worded))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    # TO DO: display the most common day of week
def get_most_popular_day(df):
    print('\nCalculating The Most Common Day of Travel...\n')
    start_time = time.time()
    
    day_worded = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saterday", "Sunday"]
    pop_day_index = int(df['start_time'].dt.dayofweek.mode())
    pop_day_worded = day_worded[pop_day_index]
    print('Most Popular Day is {}'.format(pop_day_worded))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: display the most common start hour
def get_most_popular_hour(df):
    print('\nCalculating The Most Common Hour of Travel...\n')
    start_time = time.time()

    pop_hour = int(df['start_time'].dt.hour.mode())
    print('Most Popular Hour is {}H00'.format(pop_hour))    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    #print('\nCalculating The Most Popular Stations and Trip...\n')
    #start_time = time.time()

    # TO DO: display most commonly used start station
def get_most_popular_station_stats(df):
    print('\nCalculating The Most Commonly used Station...\n')
    start_time = time.time()
    pop_start_station = df['start_station'].mode().to_string(index = False)
    print("Most Popular Start Station is {}".format(pop_start_station))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    # TO DO: display most commonly used end station
def get_most_popular_end_station(df):
    print('\nCalculating The Most Commonly used End Station...\n')
    start_time = time.time()
    
    pop_end_station = df['end_station'].mode().to_string(index = False)
    print("Most Popular End Station is {}".format(pop_end_station))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    # TO DO: display most frequent combination of start station and end station trip
def get_most_popular_trip(df):
    print('\nCalculating The Most Common Trip...\n')
    start_time = time.time()
    
    popular_trip = df['trip'].mode().to_string(index = False)
    print("Most Popular Trip is {}".format(popular_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    #print('\nCalculating Trip Duration...\n')
    #start_time = time.time()

    # TO DO: display total travel time
def get_total_travel_time(df):
    print('\nCalculating Total Travel Time...\n')
    start_time = time.time()
    
    total_travel_time = df['trip_duration'].sum()
    print('Total travel time is {}'.format(total_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    # TO DO: display mean travel time
def get_average_travel_time(df):
    print('\nCalculating Average Travel Time...\n')
    start_time = time.time()
    
    average_travel_time = round(df['trip_duration'].mean())
    print('Average travel time is {}'.format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#def user_stats(df):
    """Displays statistics on bikeshare users."""

   # print('\nCalculating User Stats...\n')
   # start_time = time.time()

    # TO DO: Display counts of user types
def get_counts_of_user_type(df):
    print('\nCalculating User Types...\n')
    start_time = time.time()
    
    customers = df.query('user_type == "Customer"').user_type.count()
    subscribers = df.query('user_type == "Subscriber"').user_type.count()
    print('Total number of customers are {} and total number of subscribers are {}.'.format(customers, subscribers))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    # TO DO: Display counts of gender
def get_counts_of_gender(df):
    print('\nCalculating Number of Female and Male Users...\n')
    
    #selected_file = ('New York', 'Chicago', 'Washington')
    
    #start_time = time.time()
    while True:
        if city.lower() == 'New York':
            female_count = df.query('gender == "Female"').gender.count()
            male_count = df.query('gender == "Male"').gender.count()
            print('There are {} female users and {} male users.'.format(female_count, male_count))
        elif city.lower() == 'Chicago':
            female_count = df.query('gender == "Female"').gender.count()
            male_count = df.query('gender == "Male"').gender.count()
            print('There are {} female users and {} male users.'.format(female_count, male_count))
        else:
            print("There is no gender data available for this city.")
            break
            
     
        #city == 'Washington'
       # gender = 0
   # return get_counts_of_gender(df)
    
        

    
    

       
    #while True:
       # if city == 'new_york_city.csv' or city == 'chicago.csv': 
      #      print('\nCalculating Sum of Males and Females...\n')
      #  elif city == 'washington.csv':
       #     print ('\n There is no info for gender for Washington\n')
    
     # if female_count == df.query('gender == "Female"') or male_count == df.query('gender == "Male"'):
      #  print('There are {} female users and {} male users.'.format(female_count, male_count))
    #  else:
      #  print("There is no gender data available for this city.")
   
    
        
    start_time = time.time()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    # TO DO: Display earliest, most recent, and most common year of birth
def get_years_of_birth(df):
    print('\nCalculating Oldest and Youngest User and Most Common Birth Year ...\n')
    start_time = time.time()
    
    if city.lower() == 'New York':
        earliest_birth_year = int(df['birth_year'].min())
        latest_birth_year = int(df['birth_year'].max())
        most_common_birth_year = int(df['birth_year'].mode())
        print('The oldest bike users are born in {}, the youngest users are born in {}, and the most common year of birth is {}.'.format(earliest_birth_year, latest_birth_year,  most_common_birth_year))
    elif city.lower() == 'Chicago':
        earliest_birth_year = int(df['birth_year'].min())
        latest_birth_year = int(df['birth_year'].max())
        most_common_birth_year = int(df['birth_year'].mode())
        print('The oldest bike users are born in {}, the youngest users are born in {}, and the most common year of birth is {}.'.format(earliest_birth_year, latest_birth_year,  most_common_birth_year))
    else:
        print("There is no birth data available for this city.")
    #break
        
        
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    q = input('\n Would you like to see the raw data for your chosen city?\n')
    i = 0 
    while True:
        if q != 'yes':
            break
          
        elif q == 'yes':
            i += 5 
            print(df.iloc[i:i+5])
            break
         
    return df.sample(5)


def main():
    while True:
        selected_file = get_city()
        month, day, filter_data = get_filters()
        df = load_data(selected_file, month, day)
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        
        get_most_popularMonth(df)
        get_most_popular_day(df)
        
        get_most_popular_hour(df)
        get_most_popular_station_stats(df)
        get_most_popular_end_station(df)
        get_most_popular_trip(df)
        get_total_travel_time(df)
        get_average_travel_time(df)
        get_counts_of_user_type(df)
        #if city == 'new_york_city.csv' or city == 'chicago.csv': 
          #  print('\nCalculating Sum of Males and Females...\n')
       # elif city == 'washington.csv':
        #    print ('\n There is no info for gender for Washington\n')
        get_counts_of_gender(df)
        get_years_of_birth(df)
        raw_data(df)

        #time_stats(df)
        #station_stats(df)
        #trip_duration_stats(df)
       # user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        else:
            main()
            break
            


if __name__ == "__main__":
    main()