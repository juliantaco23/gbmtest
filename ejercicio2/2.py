def calculate_points(results, scoring_system):
    points = [0] * len(results)
    for i, pos in enumerate(results):
        if pos <= len(scoring_system):  # Check if position is within the scoring system
            points[i] = scoring_system[pos - 1]  # Adjust index to start from 0
    return points

def determine_champion(points):
    max_points = max(points)
    champions = [i+1 for i, p in enumerate(points) if p == max_points]
    return champions

file_path = "./ejercicio2/test1.txt"
output_file = "./ejercicio2/output.txt"

with open(file_path, 'r') as f, open(output_file, 'w') as output:
    while True:
        # Read number of Grand Prix (G) and pilots (P)
        line = f.readline().strip()
        if line == "0 0":
            break

        G, P = map(int, line.split())

        # Read Grand Prix results
        grand_prix = []
        for _ in range(G):
            results = list(map(int, f.readline().strip().split()))
            grand_prix.append(results)

        # Read number of scoring systems (S)
        S = int(f.readline().strip())

        for _ in range(S):  # Loop for each scoring system
            # Read points for each position
            line = f.readline().strip()
            K, *points = map(int, line.split())
            scoring_system = points  # No need to use dictionary here, just store points list

            # Initialize pilot points
            pilot_points = [0] * P

            # Calculate points for each race
            for race_result in grand_prix:
                race_points = calculate_points(race_result, scoring_system)
                pilot_points = [pilot_points[pilot - 1] + points for pilot, points in zip(race_result, race_points)]

            # Find World Champion(s)
            max_points = max(pilot_points)
            champions = [i + 1 for i, points in enumerate(pilot_points) if points == max_points]
            output.write(" ".join(map(str, champions)) + "\n")

        output.write("\n")  # Print an empty line after each test case
