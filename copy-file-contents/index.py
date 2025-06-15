import os
from time import sleep

current_dir = os.path.dirname(__file__)
output_file = os.path.join(current_dir, "output.txt")
content_file = os.path.join(current_dir, "content.txt")

output_filename = os.path.basename(output_file)
content_filename = os.path.basename(content_file)

file_default_content = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

if os.path.exists(content_file):
    with open(content_file, "r") as f:
        content = f.read()

        with open(output_file, "w") as out_f:
            out_f.write(content)

        print(f"Data copied from {content_filename} to {output_filename} successfully.")

else:
    print(f"The content file \"{content_filename}\" does not exist.")

    print(f"Creating the content \"{content_filename}\" file with some content...")

    with open(content_file, "w") as f:
        f.write(file_default_content)

    print(f"Content written to {content_filename}.")

    sleep(3)
    print("Exiting the program.")

    exit(1)
