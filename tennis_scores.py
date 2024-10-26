import os

# Initialize standings dictionaries for u10 and u14
standings = {'u10': {}, 'u14': {}}

def load_standings():
    for age_group in standings:
        file_name = f"standings_{age_group}.txt"
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                for line in file:
                    player, points = line.strip().split(',')
                    standings[age_group][player] = int(points)

def save_standings():
    for age_group in standings:
        file_name = f"standings_{age_group}.txt"
        with open(file_name, 'w') as file:
            # Sort the standings by points in descending order
            sorted_standings = sorted(standings[age_group].items(), key=lambda x: x[1], reverse=True)
            for player, points in sorted_standings:
                file.write(f"{player},{points}\n")

def add_points(player, age_group, points, games_won):
    total_points = points + games_won
    if player in standings[age_group]:
        standings[age_group][player] += total_points
    else:
        standings[age_group][player] = total_points

def input_scores():
    match_type = input("Enter match type (singles, doubles, threeway): ").strip().lower()
    age_group = input("Enter age group (u10, u14): ").strip().lower()
    if age_group not in standings:
        print("Invalid age group")
        return

    if match_type == "singles":
        player1 = input("Enter name of player 1: ").strip()
        player2 = input("Enter name of player 2: ").strip()
        games1 = int(input(f"Enter games won by {player1}: "))
        games2 = int(input(f"Enter games won by {player2}: "))
        if games1 > games2:
            add_points(player1, age_group, 10, games1)
            add_points(player2, age_group, 5, games2)
        else:
            add_points(player1, age_group, 5, games1)
            add_points(player2, age_group, 10, games2)

    elif match_type == "doubles":
        team1 = input("Enter names of team 1 (comma separated): ").strip().split(',')
        team2 = input("Enter names of team 2 (comma separated): ").strip().split(',')
        games1 = int(input("Enter games won by team 1: "))
        games2 = int(input("Enter games won by team 2: "))
        if games1 > games2:
            for player in team1:
                add_points(player.strip(), age_group, 10, games1)
            for player in team2:
                add_points(player.strip(), age_group, 5, games2)
        else:
            for player in team1:
                add_points(player.strip(), age_group, 5, games1)
            for player in team2:
                add_points(player.strip(), age_group, 10, games2)

    elif match_type == "threeway":
        player1 = input("Enter name of player 1: ").strip()
        player2 = input("Enter name of player 2: ").strip()
        player3 = input("Enter name of player 3: ").strip()
        games1 = int(input(f"Enter games won by {player1}: "))
        games2 = int(input(f"Enter games won by {player2}: "))
        games3 = int(input(f"Enter games won by {player3}: "))

        max_games = max(games1, games2, games3)
        if (games1 == games2 == max_games) or (games2 == games3 == max_games) or (games1 == games3 == max_games):
            add_points(player1, age_group, 7, games1)
            add_points(player2, age_group, 7, games2)
            add_points(player3, age_group, 7, games3)
        else:
            if games1 == max_games:
                add_points(player1, age_group, 10, games1)
                add_points(player2, age_group, 5, games2)
                add_points(player3, age_group, 5, games3)
            elif games2 == max_games:
                add_points(player1, age_group, 5, games1)
                add_points(player2, age_group, 10, games2)
                add_points(player3, age_group, 5, games3)
            elif games3 == max_games:
                add_points(player1, age_group, 5, games1)
                add_points(player2, age_group, 5, games2)
                add_points(player3, age_group, 10, games3)
    else:
        print("Invalid match type")

def main():
    load_standings()
    while True:
        print("\nTennis League Standings Management")
        print("1. Input Match Scores")
        print("2. View Standings")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            input_scores()
            save_standings()
        elif choice == '2':
            for age_group in standings:
                print(f"\nStandings for {age_group}:")
                for player, points in sorted(standings[age_group].items(), key=lambda x: x[1], reverse=True):
                    print(f"{player}: {points} points")
        elif choice == '3':
            save_standings()
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
