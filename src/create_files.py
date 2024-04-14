import os
import sys

def create_files(folder_name):
    # Directory to hold the files
    directory = os.path.join(os.getcwd(), folder_name)

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    comment = """\
1578. Minimum Time to Make Rope Colorful
Solved
Medium
Topics
Companies
Hint

Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.

 

Example 1:

Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.

Example 2:

Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.

Example 3:

Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2
Explanation: Bob will remove the balloons at indices 0 and 4. Each balloons takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.

Constraints:
    n == colors.length == neededTime.length
    1 <= n <= 105
    1 <= neededTime[i] <= 104
    colors contains only lowercase English letters.
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
