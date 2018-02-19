print "\t\tExercise 1\n\n"

money = input("How much money do you have right now? ")
wiiprice = 30000
print "A wii console cost about", wiiprice, "pesos."
print "You can afford to buy", money/wiiprice, "wii consoles."
print "You need to have an extra", (wiiprice-(money%wiiprice)), "pesos to buy an additional wii console."
