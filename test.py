import difflib

with open("f1.txt", "r") as f:
    s1 = f.readlines()

with open("f2.txt", "r") as f:
    s2 = f.readlines()
print(s2[0].rstrip())
d = difflib.Differ()
diff = d.compare(s1, s2)
print("\n".join(diff))
