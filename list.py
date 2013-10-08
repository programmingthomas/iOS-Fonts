sixFonts = open("ios6fonts.txt").read().split("\n")
sevenFonts = open("ios7fonts.txt").read().split("\n")

f = open("diff.txt", "w")

for newFont in sevenFonts:
    if not newFont in sixFonts:
        print(newFont);
        f.write(newFont + "\n")

f.close()