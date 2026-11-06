class Solution:
    def judgeCircle(self, moves: str) -> bool:
        up = moves.count('U')
        down = moves.count('D')
        left = moves.count('L')
        right = moves.count('R')

        return up == down and left == right