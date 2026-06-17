nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_squares = [ x**2 for x in nums if x != 0]

words = ["python", "django", "api", "backend"]


word_length = {word:len(word) for word in words}

print(word_length)


scores_gen = (x for x in range(100))


print(next(scores_gen))
print(next(scores_gen))
print(next(scores_gen))
print(next(scores_gen))