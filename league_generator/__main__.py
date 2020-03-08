from random import shuffle
import copy

from league_generator.check_matches import check_matches
from league_generator.courts import COURTS
from league_generator.gen_cvs import gen_csv

TOTAL_TEAMS = 28  + 1
fn = "games28.csv"
check = (TOTAL_TEAMS - 1) / 2



def make_set(ms=[], _vs=[], _team_crt=[]):
    tries = 0
    m = []
    teams = list(range(1, TOTAL_TEAMS))
    courts = list(range(1, TOTAL_TEAMS, 2))
    #     print(f" CRT {len(_team_crt)}")
    while teams:
        shuffle(teams)
        t1 = teams.pop()

        shuffle(teams)
        t2 = teams.pop()

        shuffle(courts)
        c1 = courts.pop()


        g = [t1, t2, (COURTS[c1], COURTS[c1 + 1])]

        if [t1, t2] not in _vs or [t2, t1] not in _vs:

            if [t1, (COURTS[c1], COURTS[c1 + 1])] not in _team_crt \
                and [t2, (COURTS[c1], COURTS[c1 + 1])] not in _team_crt:
                print(f"Dupe Court {g} \n\n {_team_crt}  \n - - - - ")

                m.append(g)

                _vs.append([t1, t2])
                _vs.append([t2, t1])

                _team_crt.append([t1, (COURTS[c1], COURTS[c1 + 1])])
                _team_crt.append([t2, (COURTS[c1], COURTS[c1 + 1])])



        else:
            tries = tries + 1
            if tries > 1000:
                break

            teams.append(t1)
            teams.append(t2)
            courts.append(c1)

            if len(teams) == 2:
                break
    return m, _vs, _team_crt


if __name__ == "__main__":

    total = []
    vs = []
    tc = []
    for x in range(1, 8):
        print(f"Week {x}")
        m1 = None
        while True:
            m1, vs1, tc1 = make_set(_vs=copy.deepcopy(vs), _team_crt=copy.deepcopy(tc))
            print(f"\tm1: {len(m1)} {len(vs1)} {len(tc1)} ")

            if len(m1) == check:
                total.append(m1)
                break

        m2 = None
        while True:
            m2, vs2, tc2 = make_set(ms=m1, _vs=copy.deepcopy(vs1), _team_crt=copy.deepcopy(tc1))
            print(f"\tm2: {len(m2)}  {len(vs2)} {len(tc2)} ")

            if len(m2) == check:
                total.append(m2)
                break

        while True:
            m3, vs3, tc3 = make_set(ms=m1 + m2, _vs=copy.deepcopy(vs2), _team_crt=copy.deepcopy(tc2))
            print(f"\tm3: {len(m3)} {len(vs3)} {len(tc3)} ")
            if len(m3) == check:
                total.append(m3)
                break

        print(len(m1), len(m2), len(m3), len(vs), len(tc3))

        vs = copy.deepcopy(vs3)
        tc = []

    print(len(total))


    gen_csv(total, TOTAL_TEAMS, fn=fn)

    check_matches(fn=fn)
