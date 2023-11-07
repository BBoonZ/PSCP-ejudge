"""[Super Recommended] Reachability"""
import json
def main(node, start):
    """Wtf how i do it wat!!??? rlly??"""
    total = node[start] + list(start)
    for i in range(26):
        loop = total.copy()
        for i in loop:
            total += node[i]
        total = sorted(list(set(total)))
    print(total)
    #break
main(json.loads(input().replace("'", '"')), input())
