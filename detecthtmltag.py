# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def solve():
    n = int(input())
    html_content = ""
    for _ in range(n):
        html_content += input() + "\n"

    # Remove HTML comments
    html_without_comments = re.sub(r"", "", html_content, flags=re.DOTALL)

    # Find all tags
    tags = re.findall(r"<([a-zA-Z0-9]+)([^>]*)>", html_without_comments)

    for tag_name, attributes_str in tags:
        print(tag_name, end="")
        attributes = re.findall(r'([a-zA-Z0-9-]+)="([^"]*)"', attributes_str)
        if attributes:
            print("-> ", end="")
            attribute_parts = []
            for attr, value in attributes:
                attribute_parts.append(f"{attr} > {value}")
            print("-> ".join(attribute_parts))
        else:
            print()

if __name__ == "__main__":
    solve()