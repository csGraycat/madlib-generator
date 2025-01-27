#  madlib generator
#  read a story from a file; replace some words in the story with user input
with open('text1.txt') as f:
    text = f.readline()

vowels = ['e', 'u', 'i', 'o', 'a']
words_count = 0
new_text = []
i = 0
is_article = False

for word in text.split():

    if word == "a" and ("<" and ">" in text.split()[i + 1]):  # check for article "a"
        i += 1
        is_article = True
        continue

    if "<" and ">" in word:  # replace the word in brackets
        a = 1
        b = word.index(">")
        descriptor = word[a:b].replace("_", " ")
        user_input = input(descriptor + ": ")
        words_count += 1
        word = word.replace(word[:b+1], user_input)

    if is_article:  # put the correct article
        if word[0] in vowels:
            new_text.append('an')
        else:
            new_text.append('a')
        is_article = False
    new_text.append(word)
    i += 1

print(" ".join(new_text))

print("Words replaced:", words_count)
