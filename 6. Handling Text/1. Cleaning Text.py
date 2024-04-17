# Create text
text_data = [" Interrobang. By Aishwarya Henriette ",
"Parking And Going. By Karl Gautier",
" Today Is The night. By Jarek Prakash "]
# Strip whitespaces
strip_whitespace = [string.strip() for string in text_data]
# Show text
print(strip_whitespace)

print("{:=^50}".format("split line"))

# Remove periods
remove_periods = [string.replace(".", "") for string in strip_whitespace]
# Show text
print(remove_periods)

print("{:=^50}".format("split line"))

# Create function
def capitalizer(string: str) -> str:
    return string.upper()
# Apply function
print([capitalizer(string) for string in remove_periods])

print("{:=^50}".format("split line"))

# Import library
import re
# Create function
def replace_letters_with_X(string: str) -> str:
    return re.sub(r"[a-zA-Z]", "X", string)
# Apply function
print([replace_letters_with_X(string) for string in remove_periods])