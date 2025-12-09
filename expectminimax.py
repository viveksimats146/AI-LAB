import random
MAX, MIN, CHANCE = "MAX", "MIN", "CHANCE"
# Simple game tree
tree = {
    "type": MAX,
    "children": [
        { "type": CHANCE, "probs": [0.7, 0.3],
          "children": [ {"value": 5}, {"value": 1} ] },
        { "type": MIN,
          "children": [ {"value": 3}, {"value": 9} ] }
    ]
}
def expectiminimax(node):
    if "value" in node:
        return node["value"]
    t = node["type"]
    if t == MAX:
        return max(expectiminimax(c) for c in node["children"])
    if t == MIN:
        return min(expectiminimax(c) for c in node["children"])
    if t == CHANCE:
        return sum(p * expectiminimax(c)
                   for p, c in zip(node["probs"], node["children"]))
def best_action(root):
    best, idx = float("-inf"), None
    for i, c in enumerate(root["children"]):
        val = expectiminimax(c)
        print(f"Action {i} EV = {val:.3f}")
        if val > best:
            best, idx = val, i
    return idx, best
def simulate(node):
    if "value" in node:
        return node["value"]
    t = node["type"]
    if t == MAX:
        return max(simulate(c) for c in node["children"])
    if t == MIN:
        return min(simulate(c) for c in node["children"])
    if t == CHANCE:
        r, s = random.random(), 0
        for p, c in zip(node["probs"], node["children"]):
            s += p
            if r <= s:
                return simulate(c)
if __name__ == "__main__":
    a, v = best_action(tree)
    print(f"\nBest Action = {a}, Expected Utility = {v:.3f}")
    print("\nRandom simulations:")
    for _ in range(5):
        print("Outcome:", simulate(tree))
