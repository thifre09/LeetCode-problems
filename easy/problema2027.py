from typing import List

def minMovesToSeat(seats: List[int], students: List[int]) -> int:
    diferenca = 0
    movimentos = 0
    for i in range(len(seats)):
        diferenca = 0
        seat = min(seats)
        student = min(students)
        diferenca += abs(seat-student)
        movimentos += diferenca
        seats.remove(seat)
        students.remove(student)
    return movimentos

print(minMovesToSeat(seats = [2,2,6,6], students = [1,3,2,6]))