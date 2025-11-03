import os

def list_current_directory():
    """Prints all files and directories in the current working directory."""
    print("Contents of the current directory:")
    try:
        # os.listdir('.') returns a list of names in the directory named '.'
        contents = os.listdir('.')
        for item in contents:
            print(f"- {item}")
    except Exception as e:
        print(f"Error listing directory contents: {e}")

if __name__ == "__main__":
    list_current_directory()
