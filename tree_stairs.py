

# def append_sons(n, current_sum, tree):
#         if current_sum == n:
#             global distinct_steps
#             distinct_steps += 1
#             return
#         if tree["sum"] + 1 <= n:
#             node_sum = tree["sum"] + 1
#             tree["sons"].append({"label": f"{tree['label']} + 1", "sum": node_sum, "sons":[]})
#             append_sons(n, node_sum, tree["sons"][-1])

#         if tree["sum"] + 2 <= n:
#             node_sum = tree["sum"] + 2
#             tree["sons"].append({"label": f"{tree['label']} + 2", "sum": node_sum, "sons":[]})
#             append_sons(n, node_sum, tree["sons"][-1])
        
#         return distinct_steps


# distinct_steps = 0
# root = {"label":"0", "sum": 0, "sons": []}
# n = 10
# print(append_sons(n=n, current_sum=root["sum"], tree=root))
# print(root)
n=3
def steps_stairs(n=n):
    if n == 1:
        return 1

    one_step_back = 1
    two_step_back = 1


    for i in range(2, n+1):
        total = one_step_back + two_step_back
        two_step_back = one_step_back
        one_step_back = total
        print(f"1sb:  {one_step_back},  2sb: {two_step_back}, total:  {total}")


    return total

steps_stairs(n=n)
