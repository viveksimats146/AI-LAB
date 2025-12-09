facts = [
    "vertebrate(duck)",
    "flying(duck)",
    "mammal(cat)"
]

rules = [
    ("vertebrate(A)", ["mammal(A)"]),
    ("animal(A)", ["vertebrate(A)"]),
    ("bird(A)", ["vertebrate(A)", "flying(A)"])
]

def unify(t, f):
    if "(" not in t: 
        return {} if t == f else None
    p1, a1 = t.split("("); a1 = a1[:-1]
    p2, a2 = f.split("("); a2 = a2[:-1]
    if p1 != p2: return None
    if a1.isupper(): return {a1: a2}
    return {} if a1 == a2 else None

def backward_chain(goal, facts, rules, visited=None):
    if visited is None: visited = set()
    if goal in visited: return False
    visited.add(goal)

    for f in facts:
        if unify(goal, f) is not None:
            return True

    for head, body in rules:
        sub = unify(head, goal)
        if sub:
            new_goals = []
            for b in body:
                p, a = b.split("("); a = a[:-1]
                if a in sub: a = sub[a]
                new_goals.append(f"{p}({a})")
            if all(backward_chain(g, facts, rules, visited.copy()) for g in new_goals):
                return True
    return False

while True:
    q = input("Enter goal: ")
    print("TRUE\n" if backward_chain(q, facts, rules) else "FALSE\n")
    if input("More? (y/n): ") != "y": break
