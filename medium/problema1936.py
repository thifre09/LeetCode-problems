from typing import List

def addRung(rungs: List[int], dist: int) -> int:
    pos = 0
    Rungsadded = 0
    i = 0
    for rung in rungs:
        if (rung - pos) <= dist:
            pos = rung
            continue
        else:
            Rungsadded += 1
            pos += dist
            rungs.insert(i,rung)
        i += 1

    return Rungsadded


print(addRung(rungs = [4,8,12,16], dist = 3))