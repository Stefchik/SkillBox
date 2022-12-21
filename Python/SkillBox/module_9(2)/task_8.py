text = open("text.txt", "r").read().lower()
sym_dict = {}
sym_count = 0

for sym in text:
    if ord('a') <= ord(sym) <= ord('z'):
        x = sym_dict.get(sym, 0)
        sym_dict[sym] = x + 1
        sym_count += 1

lout = [(k, "{:5.3f}".format(sym_dict[k] / sym_count)) for k in sym_dict.keys()]
lout.sort(key=lambda x: x[0])
lout.sort(key=lambda x: x[1], reverse=True)
sout = "\n".join([i[0] + " " + i[1] for i in lout])
open("analysis.txt", "w").write(sout)
