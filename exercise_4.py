print ("\t\tExercise 4\n\n");

sum = 0

file_text = open("DNA.txt").read()

for x in file_text:
    if x == 'C' or x == 'G':
        sum = sum + 1
y = len(file_text)
print "There are", sum, "C's and G's in the overall", len(file_text), "DNA amounting to", 100.00*sum/y, "% of the DNA."
