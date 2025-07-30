class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_set, negative_set = set(positive_feedback), set(negative_feedback)
        scores = []

        for i in range(len(report)):
            words = report[i].split()
            score = 0
            for word in words:
                if word in positive_set:
                    score += 3
                elif word in negative_set:
                    score -=1
            scores.append((score, student_id[i]))
        
        scores.sort(key=lambda x: (-x[0], x[1]))
        return [i[1] for i in scores[:k]]