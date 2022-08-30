text = "data.txt"
f = open(text, "r")

with open("converted.txt", "w") as ff:
    for line in f:
        s = line.split(":")
        try:
            ff.write("%.2f" % (int(s[0]) + float(s[1]) / 60.0) + "\n")
        except:
            break

print("done")
