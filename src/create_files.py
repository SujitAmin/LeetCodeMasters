import os
import sys

def create_files(folder_name):
    # Directory to hold the files
    directory = os.path.join(os.getcwd(), folder_name)

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Define file names and their corresponding content templates
    templates = {
        ".java": "public class {0} {{\n    public static void main(String[] args) {{\n        // Code goes here\n    }}\n}}",
        ".js": "function main() {{\n    // Code goes here\n}}\nmain();",
        ".py": "def main():\n    # Code goes here\n\nif __name__ == '__main__':\n    main()",
        ".swift": "import Foundation\n\nfunc main() {{\n    // Code goes here\n}}\n\nmain()"
    }

    # Create files with templates
    for extension, content in templates.items():
        file_path = os.path.join(directory, "{}{}".format(folder_name, extension))
        with open(file_path, 'w') as file:
            file.write(content.format(folder_name))
        print(f"Created: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_files.py [folder_name]")
    else:
        create_files(sys.argv[1])
