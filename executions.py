import os

# This script was created to realize the execution tests in a more automatic way


# Define the different parameter combinations to use
params = [
    ("-v 2000 -a char", "params1"),
    ("-v 4000 -a char", "params2"),
    ("-v 6000 -a char", "params3"),
    ("-v 8000 -a char", "params4"),
    ("-v 10000 -a char", "params5"),
    ("-v 2000 -a word", "params6"),
    ("-v 4000 -a word", "params7"),
    ("-v 6000 -a word", "params8"),
    ("-v 8000 -a word", "params9"),
    ("-v 10000 -a word", "params10")
]


# Define the input file path
input_file = "../data/dataset.csv"

# Create the output folder if it doesn't exist
if not os.path.exists("../output"):
    os.mkdir("../output")

# Loop through the different parameter combinations
for param in params:
    print(param)
    # Construct the command to execute
    command = f"python langdetect.py -i {input_file} {param[0]}"

    # Run the command and capture the output
    output = os.popen(command).read()

    # Save the output to a file
    with open(f"../output/{param[1]}.txt", "w") as f:
        f.write(output)

    # Save the image to a file
    os.rename("../output/PCA.png", f"../output/PCA_{param[1]}.png")
    os.rename("../output/CM.png", f"../output/CM_{param[1]}.png")