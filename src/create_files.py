import os
import sys

def create_files(folder_name):
    # Directory to hold the files
    directory = os.path.join(os.getcwd(), folder_name)

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    comment = """\
11. Container With Most Water
Solved
Medium
Topics
Companies
Hint

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

 

Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
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
