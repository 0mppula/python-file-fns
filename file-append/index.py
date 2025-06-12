import os

current_dir = os.path.dirname(__file__)
output_file = os.path.join(current_dir, "output.txt")
filename = os.path.basename(output_file)


if os.path.exists(output_file):
    with open(output_file, "r") as f:
        content = f.read(50)  # Read first 50 characters

    if content == "":
        print(f"The output file is empty.")
    else:
        print(f"Current contents of the output file \"{filename}\": \n")
        print(content)


usr_input = input(f"Enter text to append to \"{filename}\": ")

with open(output_file, "a") as f:
    f.write(usr_input)

print(f"Data appended to {filename} successfully.")
