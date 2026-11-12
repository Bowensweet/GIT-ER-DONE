import pandas as pd

def categorize_teams(season_df):
    """Use a dictionary to organize the season's teams by number of wins."""
    categories = { "10 or more wins": [], "8-9 wins": [],"6-7 wins": [],"Fewer than 6 wins": [], }

    for _, row in season_df.iterrows():
        team = row["Team"]
        wins = row["Win"]

        if wins >= 10:
            categories["10 or more wins"].append((team, wins))
        elif wins >= 8:
            categories["8-9 wins"].append((team, wins))
        elif wins >= 6:
            categories["6-7 wins"].append((team, wins))
        else:
            categories["Fewer than 6 wins"].append((team, wins))

    return categories


def display_categories(categories, season):
    """Print each category and its teams (most wins first)."""
    print(f"      {season} Season Results      ")
    print()
    for category, teams in categories.items():
        print(f"{category} ({len(teams)} teams)")
        print()
        if not teams:
            print("  (no teams)")
            continue
        for team, wins in sorted(teams, key=lambda t: (-t[1], t[0])):
            print(f"  {team}: {wins} wins")


def main():
   
    df = pd.read_csv("cfb.csv")  
    first_season = df["Season"].min()
    last_season = df["Season"].max()
    print("College Football Season Explorer")
    print(f"Seasons available: {first_season} to {last_season}")

    while True:
        choice = input("Which season would you like to analyze? (or 'q' to quit): ").strip()

        if choice.lower() == "q":
            print("Goodbye!")
            break

        if not choice.isdigit():
            print("Please enter a four-digit year, such as 2019.")
            continue

        season = int(choice)
        season_df = df[df["Season"] == season]

        if season_df.empty:
            print(f"Season {season} was not found in the data.")
            continue

        categories = categorize_teams(season_df)
        display_categories(categories, season)


main()