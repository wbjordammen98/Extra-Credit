# Problem 2

# Open in file of World Sereis winners.
infile = open("WorldSeriesWinners.txt","r")

# Prints each team name individually.
teams = infile.readline()
team_name = teams.rstrip('\n')

# Set variable for starting year of the World Series.
starting_year = 1903

# Create an empty dictionary for the number of WS wins for the team.
num_ws_won_dict = {}

# Create an empty dictionary for the years of each WS.
ws_year_dict = {}

# Add the progressively increasing year as the key and the respective team as the value. 
ws_year_dict[starting_year] = team_name

# Counter variable to keep track of each WS win per team.
num_ws_won_dict[team_name] = 1

# 
while teams != "":

    if starting_year != 1903 and starting_year != 1993:

        if team_name in num_ws_won_dict:
            num_ws_won_dict[team_name] += 1
        else:
            num_ws_won_dict[team_name] = 1

        teams = infile.readline()
        team_name = teams.rstrip()

        starting_year += 1

        ws_year_dict[starting_year] = team_name
        
    else:
        starting_year += 1
        

infile.close()

print("NOTE: The World Series was not played in the years of 1904 and 1994, so PLEASE DON'T enter either of those years.")
user_requested_year = input("Enter a year in the range of 1903 to 2009 to find out the World Series champion for that year: ")

if user_requested_year >= '1903' and user_requested_year <= '2009':

    team = ws_year_dict[int(user_requested_year)]

    print("The team that won the World Series in " + user_requested_year + " is the " + team + ".")
    print("The " + team + " have won the World Series " + str(num_ws_won_dict[team]) + " times.")

else:
    print("Invalid year. CHOOSE FROM THE RANGE *(1903-2009)*")

    

