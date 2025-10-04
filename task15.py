words=list(input().split())
words.sort(key=lambda a: len(a))
print(words)