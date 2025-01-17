
from llama_index.core.tools import FunctionTool
import os

note_file = os.path.join("data", "notes.txt")

def save_note(note):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(note_file), exist_ok=True)
    
    try:
        # Open the file safely for appending
        with open(note_file, "a") as f:
            f.write(note + "\n")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

    return "note saved"

note_engine = FunctionTool.from_defaults(
    fn= save_note,
    name= "note_saver",
    description = "this tool can save a tex based note to a file for the suer",
)