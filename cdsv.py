import textwrap

text = "This is a long piece of text that needs to be wrapped to fit within a specific width."

# Wrap the text to a specified width (e.g., 40 characters)
wrapped_text = textwrap.wrap(text, width=40)

for line in wrapped_text:
    print(line)