f = open("Slice R.txt", "w")

for i in ["lasdjkfRlsdkjf","alsdkjflaksdjRalskdjf","laksdjflkajsdlfkjRalskdjf","l;askdjflkjasdflkjR"]:
    count = 0
    for j in i:
        if j == "R":
            f.write("="*15)
            f.write('\n')
            f.write(i[:count])
            f.write('\n')
            f.write(i[count:])
            f.write('\n')

        count = count + 1
f.write("="*15)
f.write('\n')

f.close()
