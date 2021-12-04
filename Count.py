from typing import List

# count of items in list
students_score: List[float] = [9.0, 8.8, 7.0, 9.5, 8.5, 8.5, 10.0, 9.5, 7.5, 7.8, 9.0, 9.0]
score_nine = students_score.count(9.0)
print("total student with nine score: ", score_nine)
