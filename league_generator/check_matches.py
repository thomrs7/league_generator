

def check_matches(fn ="test.csv"):
    import pandas as pd

    vsc = {}

    df = pd.read_csv(fn)
    for row in df.iterrows():
        r = row[1]
        for row1 in df.iterrows():

            r1 = row1[1]
            if r.Week == r1.Week and (r.Match1 == r1.Match1 or r.Match2 == r1.Match2 or r.Match3 == r1.Match3):
                if r['Team#'] != r1['Team#']:
                    #                 print(f"WK{r.Week} A{r['Team#']} B{r1['Team#']}")
                    if r['Team#'] in vsc:
                        vsc[r['Team#']].append(r1['Team#'])
                    else:
                        vsc[r['Team#']] = [r1['Team#']]

    for v in vsc:
        print(v, len(set(vsc[v])), vsc[v])

    print()
    dc = []
    for row in df.iterrows():
        r = row[1]
        i = row[0]
        if r.Match1 == r.Match2 or r.Match2 == r.Match3 or r.Match1 == r.Match3:
            dc.append(r)
        else:
            #         print(f"{i} pass")
            pass

    print(len(dc))

    for d in dc:
        print(d)
        print()

if __name__ == "__main__":
    check_matches()