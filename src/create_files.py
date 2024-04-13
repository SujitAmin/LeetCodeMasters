import os
import sys

def create_files(folder_name):
    # Directory to hold the files
    directory = os.path.join(os.getcwd(), folder_name)

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Comment to be added as a block comment in each file
    comment = """\
    125. Valid Palindrome
    Solved
    Easy
    Topics
    Companies

    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
    and removing all non-alphanumeric characters, it reads the same forward and backward.
    Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

    Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

    Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

    Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
    """

    # Define file names and their corresponding content templates
    templates = {
        ".java": "/*\n{}\n*/\n\npublic class {{}} {{\n    public static void main(String[] args) {{\n        // Code goes here\n    }}\n}}".format(comment),
        ".js": "/*\n{}\n*/\n\nfunction main() {{\n    // Code goes here\n}}\nmain();".format(comment),
        ".py": "'''\n{}\n'''\n\ndef main():\n    # Code goes here\n\nif __name__ == '__main__':\n    main()".format(comment),
        ".swift": "/*\n{}\n*/\n\nimport Foundation\n\nfunc main() {{\n    // Code goes here\n}}\n\nmain()".format(comment)
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
