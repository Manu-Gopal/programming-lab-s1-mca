def character_freq():
    freq={}
    str=input("enter the string ")
    for i in str:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    print(freq)
character_freq()
