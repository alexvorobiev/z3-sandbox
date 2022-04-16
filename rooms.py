from z3 import *

# room capacities
rooms = [3, 4, 4]

# peoples' choices
people = [[0, 2, 4], [0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]

# talks' repeats
meetings = [2, 1, 1, 2, 2]

# time slots
nTimes = 3

sol = Solver()

# True if person p is in room r at time slot t meeting m iteration i

vars1 = [f"r{r}_t{t}_p{p}_m{m}_{i}" for r in range(len(rooms)) for t in range(nTimes) for p in range(len(people)) for m in people[p] for i in range(meetings[m])]

# True if person p is in meeting m iteration i
p_m = [Bool(f"p{p}_m{m}_{i}") for p in range(len(people)) for m in people[p] for i in range(meetings[m])]

# True if meeting m iteration i is in room r at time t
m_r_t = [Bool(f"m{m}_{i}_r{r}_t{t}") for m in range(len(meetings)) for i in range(meetings[m]) for r in range(len(rooms)) for t in range(nTimes)]


def m_r_t_idx(m, i, r, t):
    idx = 0
    for mi in range(m):
        idx += meetings[mi] * (len(rooms) * nTimes)

    # idx += len(rooms) * t
    return (idx + i * (len(rooms) * nTimes) + r * nTimes + t)

# only works if the person wants that meeting
def p_m_idx(p, m, i):
    idx = 0
    for pe in range(p):
        for mi in people[pe]:
            idx += meetings[mi]

    it = iter(people[p])
    while (mi := next(it, None)) is not None and (m != mi):
        idx += meetings[mi]

    return idx + i

# iteration of the same meeting can't be at the same time
# a person can have only one iteration of a meeting
# a person can't be in different rooms at the same time
# room capacity constraint
