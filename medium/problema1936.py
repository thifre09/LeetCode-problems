from typing import List

def addRung(rungs: List[int], dist: int) -> int:
    pos = 0
    Rungsadded = 0
    for rung in rungs:
        if (rung - pos) <= dist:
            pos = rung
            continue
        else:
            while (rung - pos) > dist:
                Rungsadded += 1
                pos += dist
            pos = rung

    return Rungsadded


print(addRung(rungs = [4,8,12,16], dist = 3))