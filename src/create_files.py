import os
import sys

def create_files(folder_name):
    # Directory to hold the files
    directory = os.path.join(os.getcwd(), folder_name)

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    comment = """\
   242. Valid Anagram
Solved
Easy
Topics
Companies

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

    """

    # Define file names and their corresponding content templates
    templates = {
        ".java": "/*\n{0}\n*/\n\npublic class {1} {{\n    public static void main(String[] args) {{\n        // Code goes here\n    }}\n}}",
        ".js": "/*\n{0}\n*/\n\nfunction main() {{\n    // Code goes here\n}}\nmain();",
        ".py": "'''\n{0}\n'''\n\ndef main():\n    # Code goes here\n\nif __name__ == '__main__':\n    main()",
        ".swift": "/*\n{0}\n*/\n\nimport Foundation\n\nfunc main() {{\n    // Code goes here\n}}\n\nmain()"
    }

    # Create files with templates
    for extension, content in templates.items():
        file_path = os.path.join(directory, folder_name + extension)
        formatted_content = content.format(comment, folder_name)
        with open(file_path, 'w') as file:
            file.write(formatted_content)
        print(f"Created: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_files.py [folder_name]")
    else:
        create_files(sys.argv[1])
