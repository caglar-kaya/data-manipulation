import re

# For this example, we will work with the Data Science Wikipedia article. First, please inspect the text below.

with open("Part A - Regular Expressions/data/practice.txt", "r") as file:
    wikipedia_article = file.read()

print(wikipedia_article)

# Your task is to filter out every heading (i.e., Foundations, Relationship to statistics etc.) using a regular expression.
# To do so, please complement the below function, which should return a list of strings that contains the different headings as elements.

def answer():
    with open("Part A - Regular Expressions/data/practice.txt", "r") as file:
        wikipedia_article = file.read()
        headings = re.findall(r'=+\s(.*?)\s=+', wikipedia_article)
    return headings

assert type(answer()) == type([]), "Please return a list!"
assert type(answer()[0]) == type(str()), "The returned list should contain strings as elements!"
assert len(answer()) == 10, "Your results seem to be incomplete!"
assert "Foundations" in answer(), "Your results seem to be incomplete!"
assert "Modern usage" in answer(), "Your results seem to be incomplete!"

print('Everything looks okay :)')