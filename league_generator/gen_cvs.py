
# THIS IS OLD UNSED
def gen_csv(total, TOTAL_TEAMS, fn = "test.csv"):
    wks = []

    t = total[0:3]
    for t in zip(*[iter(total)] * 3):
        l = {}
        for team in list(range(1, TOTAL_TEAMS)):
            #         print(team)
            l[team] = []
            for g in t:
                for match in g:
                    if team in match:
                        l[team].append(match)
        wks.append(l)

    def court(x):
        for g in x:
            if (type(g) is tuple):
                court = g
        return court

    x = ""
    y = 0
    with open(fn, 'w') as file:
        file.write("Week,Team#,Match1,Match2,Match3\n")
        print("Week,Team#,Match1,Match2,Match3\n")
        for y in [0, 1, 2, 3, 4, 5, 6]:
            t = wks[y]
            for k in t.keys():
                try:

                    msg = f"{y+1}, {k:<5}, {court(t[k][0])[0]}&{court(t[k][0])[1]} , {court(t[k][1])[0]}&{court(t[k][1])[1]} , {court(t[k][2])[0]}&{court(t[k][2])[1]} "
                    #                     print(msg)
                    file.write(f"{msg} \n")
                except Exception as err:
                    print("!!!!! " + err, t[k])
