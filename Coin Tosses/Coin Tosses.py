def coinTosses():
    countH = 0
    countT = 0

    for i in range (1,5001,1):

        import random
        hot = random.randrange(1,101)
        if hot % 2 == 0:
            countH += 1
            print ("Attempt # " + str(i) + " Throwing a coin... It's a head! ... Got " + str(countH) + " head(s) so far and " + str(countT) + " tails(s) so far")
        if hot % 2 == 1:
            countT += 1
            print ("Attempt #" + str(i) + " Throwing a coin... It's a tail! ... Got " + str(countH) + " head(s) so far and " + str(countT) + " tails(s) so far")

coinTosses()














