import os

current_dir = os.path.dirname(__file__)
content_file = os.path.join(current_dir, "content.txt")

content_filename = os.path.basename(content_file)

if os.path.exists(content_file):
    with open(content_file, "r") as f:
        content = f.read()

        print(f"Data read from {content_filename} successfully.")
        print(content)

else:
    print(f"The content file \"{content_filename}\" does not exist.")
    print("Exiting the program.")
    exit(1)
