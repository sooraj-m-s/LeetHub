class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s_list = list(s)
        goal_list = list(goal)
        k = 0
        while k < len(goal_list):
            if s_list == goal_list:
                return True
            else:
                first = goal_list[0]
                temp = goal_list[1:]
                goal_list = temp
                goal_list.append(first)
            k += 1
        return False