import os

current_dir = os.path.dirname(__file__)
output_file = os.path.join(current_dir, "output.txt")
filename = os.path.basename(output_file)

usr_input = input("Enter some text to write to a file: ")

with open(output_file, "w") as f:
    f.write(usr_input)

print(f"Data written to {filename} successfully.")
