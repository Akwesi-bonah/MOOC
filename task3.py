# Write your solution to exercise 3 here
def points(stats):
    # split into team and record
    parts = stats.split(":")
    team = parts[0]
    record = parts[1]

    # split record into win, loss and tie
    wins, losses, ties = record.split("-")

    # Check if  wins, losses, ties record are invalid
    for value in wins, losses, ties:
        if not value.isdigit():
            raise ValueError("All stats were not Integers")

    # Calculate the number of points.
    points = (int(wins) * 3) + int(ties)

    return points


if __name__ == "__main__":
    print(points("Heba hawks:5-6-1"))
    print(points("Brewsters:3-12-10"))
    print(points("Sleepers:0-0-0"))
    print(points("KBC:AAA-1-ll"))
    print(points("KBC:AAA-1-ll"))
    print(points("Loosisters:8-5-abb"))

