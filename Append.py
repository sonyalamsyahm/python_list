# 1
from typing import List

students_score: list[int] = [9, 6, 5, 8, 8, 7, 7, 10, 9]
other_students_score: List[int] = [6, 7, 8, 8]
for score in other_students_score:
    students_score.append(score)


# 2
music_instruments = ["violin", "drum", "clarinet"]
indonesian_music_instruments = ["angklung", "suling"]
for music_instrument in indonesian_music_instruments:
    music_instruments.append(music_instrument)


print(students_score)
print(music_instruments)
