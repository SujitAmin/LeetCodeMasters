import os
import sys

def create_files(folder_name):
    # Directory to hold the files
    directory = os.path.join(os.getcwd(), folder_name)

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    comment = """\
412. Fizz Buzz
Solved
Easy
Topics
Companies

Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]

Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:
    1 <= n <= 104
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
