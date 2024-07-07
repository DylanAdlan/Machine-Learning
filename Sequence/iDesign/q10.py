sentence = input().split()

words = {}
for word in sentence:
    if word in words:
        words[word] +=1
    else:
        words[word] = 1

print(words)