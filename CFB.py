import pandas as pd

def categorize_teams(season_df):
    """Use a dictionary to organize the season's teams by number of wins."""
    categories = { "10 or more wins": [], "8–9 wins": [], "6–7 wins": [], "Fewer than 6 wins": [], }

    for _, row in season_df.iterrows():
        # Team looks like "Alabama (SEC)"; keep only the name, without the conference
        team = row["Team"].rsplit(" (", 1)[0]
        wins = row["Win"]

        if wins >= 10:
            categories["10 or more wins"].append((team, wins))
        elif wins >= 8:
            categories["8–9 wins"].append((team, wins))
        elif wins >= 6:
            categories["6–7 wins"].append((team, wins))
        else:
            categories["Fewer than 6 wins"].append((team, wins))

    return categories


def display_categories(categories, season):
    """Print each category and its teams (most wins first)."""
    print()
    print(f"College Football Results for {season}")
    print()
    for category, teams in categories.items():
        print(f"{category}:")
        print()
        for team, wins in sorted(teams, key=lambda t: (-t[1], t[0])):
            if wins == 1:
                label = "win"
            else:
                label = "wins"
            print(f"{team}: {wins} {label}")
        print()


def main():
    df = pd.read_csv("cfb.csv")

    while True:
        print()
        choice = input("Enter a season to analyze: ").strip()

        if not choice.isdigit():
            print("Please enter a four-digit year, such as 2019.")
            continue

        season = int(choice)
        season_df = df[df["Season"] == season]

        if season_df.empty:
            first_season = df["Season"].min()
            last_season = df["Season"].max()
            print(f"Season {season} was not found. Seasons available: {first_season} to {last_season}.")
            continue

        categories = categorize_teams(season_df)
        display_categories(categories, season)
        break


main()