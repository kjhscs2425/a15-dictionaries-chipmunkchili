text = """
Everyone counts.
Everyone has access to great learning.
Every person's unique talents are valued equally.
Everyone takes responsibility for themselves and their community."""

# Make a dictionary where the keys are characters and the values are the number of times that character appears in the `text` print the dicitonary

counter = {}

text_lower = text.lower()

for character in text_lower:
    if character == "\n" or character == " " or character == "." or character == "'":
            text_lower.replace(character, "")
    elif character in counter:
        counter[character] += 1
    else:
        counter[character] = 1
        
print(counter)