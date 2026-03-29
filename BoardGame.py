# Homework 3 - Board Game System
# Name: Jack Schulz
# Date:

def loadGameData(filename):
    turn = ""
    players = {}
    events = {}

    file = open(filename, "r")

    for line in file:
        line = line.strip()

        if line.startswith("Turn:"):
            turn = line.split(": ")[1]
        else:
            parts = line.split(": ")
            position = int(parts[0])
            name = parts[1]

            if name.startswith("Player"):
                players[name] = position
            else:
                events[position] = name

    file.close()
    return turn, players, events


def displayGame(turn, players, events):
    print("\nCurrent Game State")
    print("------------------")
    print("Current Turn:", turn)

    print("\nPlayer Positions:")
    for player in players:
        print(player, "is at space", players[player])

    print("\nBoard:")
    for space in range(1, 31):
        line = str(space)

        for player in players:
            if players[player] == space:
                line = line + " [" + player + "]"

        if space in events:
            line = line + " {" + events[space] + "}"

        print(line)


def movePlayer(turn, players, events):
    players[turn] = players[turn] + 1
    print("\n" + turn, "moved to space", players[turn])

    if players[turn] in events:
        print(turn, "landed on", events[players[turn]])


def switchTurn(turn):
    if turn == "Player1":
        return "Player2"
    elif turn == "Player2":
        return "Player3"
    else:
        return "Player1"


def saveGameData(filename, turn, players, events):
    file = open(filename, "w")

    file.write("Turn: " + turn + "\n")

    for player in players:
        file.write(str(players[player]) + ": " + player + "\n")

    for event in events:
        file.write(str(event) + ": " + events[event] + "\n")

    file.close()


def main():
    filename = "events.txt"

    turn, players, events = loadGameData(filename)
    displayGame(turn, players, events)

    choice = input("\nMove player? (y/n): ")

    while choice.lower() == "y":
        movePlayer(turn, players, events)
        turn = switchTurn(turn)
        saveGameData(filename, turn, players, events)

        print("\nUpdated Game State")
        print("------------------")
        displayGame(turn, players, events)

        choice = input("\nMove player? (y/n): ")

    print("\nGame ended.")


main()