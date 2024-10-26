# tennisproject
# Project that takes user input to create and manage the standings of a tennis league. 
# The standings for two age groups (u10 and u14) are stored in a dictionary named standings 
# Each age group has a corresponding dictionary where the player names serve as keys and their points are stored as values
# The load_standings function reads standings from two separate files (standings_u10.txt and standings_u14.txt) 
# It checks if the files exist and, if so, loads the player names and points into the standings dictionary.
# The save_standings function writes the updated standings back to the files, ensuring that they are sorted by points in descending order. 
# Each player’s name and points are stored in a comma-separated format.
# The add_points function updates a player’s points, adding their earned points and the number of games won in the match.
# The input_scores prompts the user to input match details, 
# including the match type (singles, doubles, or threeway), age group, player names, and the number of games won. 
# Points are awarded based on match outcomes:
# Singles: The winner receives 10 points, and the loser gets 5.
# Doubles: The logic mirrors singles, but points are distributed to each player in a team.
# Threeway: This type involves three players, with special handling if there’s a tie for the most games won.
# The main function provides a simple menu interface, where users can choose between:
# Inputting Match Scores: Calls input_scores to enter new match data, and then saves the standings.
# Viewing Standings: Displays the current standings for both age groups, sorted by points.
# Exiting: Saves the standings and exits the program.
