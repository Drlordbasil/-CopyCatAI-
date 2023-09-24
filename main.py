import os
import shutil
import subprocess


class Replicator:
    def __init__(self):
        self.program_name = "replicator.py"

    def create_copy(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        original_path = os.path.join(current_directory, self.program_name)
        copy_path = os.path.join(current_directory, f"copy_{self.program_name}")

        if original_path == copy_path:
            return "Error: Cannot create a copy of the program itself."

        shutil.copyfile(original_path, copy_path)

        return "Successfully created a copy of the program."

    def run_copy(self):
        subprocess.call(["python", f"copy_{self.program_name}"])


if __name__ == "__main__":
    replicator = Replicator()
    creation_status = replicator.create_copy()

    if creation_status.startswith("Error"):
        print(creation_status)
    else:
        replicator.run_copy()
