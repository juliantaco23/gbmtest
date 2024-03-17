def min_jumps(x):
    steps = 0
    while steps * (steps + 1) < 2 * x:
        steps += 1
    if steps * (steps + 1) // 2 == x + 1:
        steps += 1
    return steps

def process_input(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        # Read the number of test cases
        t = int(f_in.readline().strip())
        
        # Process each test case
        for _ in range(t):
            x = int(f_in.readline().strip())
            result = min_jumps(x)
            f_out.write(f"{result}\n")

process_input("./ejercicio3/tests.txt", "./ejercicio3/output.txt")
