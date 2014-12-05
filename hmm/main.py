from copy import deepcopy

A = {
        "adj" : {"adj" : 0.08, "adv" : 0.01, "det" : 0.01, "n" : 0.87, "v" : 0.03, "$": 0.00},
        "adv" : {"adj" : 0.11, "adv" : 0.17, "det" : 0.25, "n" : 0.12, "v" : 0.34, "$": 0.01},
        "det" : {"adj" : 0.23, "adv" : 0.01, "det" : 0.00, "n" : 0.65, "v" : 0.10, "$": 0.00},
        "n"   : {"adj" : 0.01, "adv" : 0.05, "det" : 0.02, "n" : 0.31, "v" : 0.60, "$": 0.01},
        "v"   : {"adj" : 0.09, "adv" : 0.26, "det" : 0.27, "n" : 0.12, "v" : 0.26, "$": 0.00},
        "$"   : {"adj" : 0.06, "adv" : 0.19, "det" : 0.39, "n" : 0.28, "v" : 0.08, "$": 0.00}
    }

B = {
        "adj" : {"an" : 0.00, "arrow" : 0.00, "flies" : 0.00, "like" : 0.96, "time" : 0.04},
        "adv" : {"an" : 0.00, "arrow" : 0.00, "flies" : 0.00, "like" : 0.00, "time" : 0.00},
        "det" : {"an" : 0.72, "arrow" : 0.00, "flies" : 0.00, "like" : 0.00, "time" : 0.28},
        "n"   : {"an" : 0.04, "arrow" : 0.51, "flies" : 0.25, "like" : 0.20, "time" : 0.00},
        "v"   : {"an" : 0.00, "arrow" : 0.00, "flies" : 0.03, "like" : 0.95, "time" : 0.02},
        "$"   : {"an" : 0.00, "arrow" : 0.00, "flies" : 0.00, "like" : 0.00, "time" : 0.00}
    }

s = ['time', 'flies', 'like', 'an', 'arrow']

W = {}

for POS in A:
    W[POS] = (A["$"][POS] * B[POS][s[0]], POS)

print(W)
for i in range(1, len(s)):
    NewW = deepcopy(W)
    for To in A:
        NewW[To] = max([(A[From][To] * W[From][0] * B[To][s[i]], W[From][1] + "_" + To) for From in A])
    W = NewW
    print(W)
