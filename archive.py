'''
OLD CODE FOR SIMULATION from 2020
import csv
import random

NUM_SIMS = 1000
mean = 0  
std_dev = 1  
min_allowed = -3
max_allowed = 3

class StateData:
    def __init__(self, name, electoral, republican, democrat):
        self._name = name
        self._electoral = electoral
        self._republican = republican
        self._democrat = democrat
        self._num_dem_wins = 0
        self._num_rep_wins = 0
        self._num_ties = 0

def get_random_error():
    sample = random.gauss(mean, std_dev)
    return max(min_allowed, min(sample, max_allowed))

def print_state_data(states):
    for state in states:
        dem_winrate = (state._num_dem_wins / NUM_SIMS) * 100
        rep_winrate = (state._num_rep_wins / NUM_SIMS) * 100
        print(f"{state._name} Dem Winrate: {dem_winrate:.2f} Rep Winrate: {rep_winrate:.2f}")

def run_simulation(states):
    num_dem_votes = 0
    num_rep_votes = 0
    num_tied_electoral = 0

    for state in states:
        adjusted_republican = state._republican + get_random_error()
        adjusted_democrat = state._democrat + get_random_error()

        if adjusted_democrat > adjusted_republican:
            num_dem_votes += state._electoral
            state._num_dem_wins += 1
        elif adjusted_democrat < adjusted_republican:
            num_rep_votes += state._electoral
            state._num_rep_wins += 1
        else:
            num_tied_electoral += state._electoral
            state._num_ties += 1

    return num_rep_votes, num_dem_votes, num_tied_electoral

def main():
    states = []

    with open("data.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name = row[0]
            electoral = int(row[1])
            republican = float(row[2])
            democrat = float(row[3])
            states.append(StateData(name, electoral, republican, democrat))

    total_dem = 0
    total_rep = 0
    total_tied = 0

    with open("represults.txt", "w") as represults, open("demresults.txt", "w") as demresults:
        for _ in range(NUM_SIMS):
            rep, dem, tied = run_simulation(states)
            demresults.write(f"{dem}\n")
            represults.write(f"{rep}\n")

            if dem > 270:
                total_dem += 1
            elif rep > 270:
                total_rep += 1
            else:
                total_tied += 1

    print(f"Percentage of Trump wins: {(total_rep / NUM_SIMS) * 100:.2f}")
    print(f"Percentage of Kamala wins: {(total_dem / NUM_SIMS) * 100:.2f}")
    print(f"Tie percentage: {(total_tied / NUM_SIMS) * 100:.2f}")

    print_state_data(states)
'''