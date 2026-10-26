class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_scores = sorted(score, reverse=True)
        rank = {}

        for i in range(len(sorted_scores)):
            if i == 0:
                rank[sorted_scores[i]] = "Gold Medal"
            elif i == 1:
                rank[sorted_scores[i]] = "Silver Medal"
            elif i == 2:
                rank[sorted_scores[i]] = "Bronze Medal"
            else:
                rank[sorted_scores[i]] = str(i + 1)

        return [rank[x] for x in score] 