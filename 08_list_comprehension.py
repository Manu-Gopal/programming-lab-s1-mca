lst=[1,2,3,4,5,-6,-7,-8]
pstv_list=[element for element in lst if element>0]
square_of_nums=[element*element for element in lst]
print(f"positive list of numbers:{pstv_list}")
print(f"squares of element in list:{square_of_nums}")
word=input("Enter a word:")
wordlist = list(word)
vowels=['a','e','i','o','u']
vowelsFromWord = [element for element in word if element in vowels]
print(vowelsFromWord)
ordValues = [ord(element) for element in wordlist]
print(ordValues)
