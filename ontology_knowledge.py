# -----------------------------
# Ontology Triples
# -----------------------------
triples=[
    ("Dog","subClassOf","Animal"),
    ("Cat","subClassOf","Animal"),
    ("Animal","subClassOf","LivingBeing"),
    ("Poodle","subClassOf","Dog"),
    ("PersianCat","subClassOf","Cat")
]
# -----------------------------
# Build Knowledge Graph
# -----------------------------
kg={}
for sub,rel,sup in triples:
    if rel=="subClassOf":
        kg.setdefault(sup,set()).add(sub)
        kg.setdefault(sub,set())
# -----------------------------
# Find all subclasses (direct+indirect)
# -----------------------------
def find_all_subclasses(cls,kg):
    res=set()
    def dfs(c):
        for s in kg.get(c,[]):
            if s not in res:
                res.add(s)
                dfs(s)
    dfs(cls)
    return res
# -----------------------------
# Find all superclasses
# -----------------------------
def find_all_superclasses(cls,kg):
    rev={}
    for p,subs in kg.items():
        for s in subs:
            rev.setdefault(s,set()).add(p)
    res=set()
    def dfs(c):
        for p in rev.get(c,[]):
            if p not in res:
                res.add(p)
                dfs(p)
    dfs(cls)
    return res
# -----------------------------
# Check if subclass
# -----------------------------
def is_subclass(sub,sup,kg):
    return sup in find_all_superclasses(sub,kg)
# -----------------------------
# Demo Queries
# -----------------------------
print("Knowledge Graph (Superclass -> Subclasses):")
for k,v in kg.items():
    print(f"{k} -> {v}")
query_cls="Animal"
print(f"\nAll subclasses of {query_cls}: {find_all_subclasses(query_cls,kg)}")
a,b="Poodle","Animal"
print(f"\nIs {a} a subclass of {b}? {'Yes' if is_subclass(a,b,kg) else 'No'}")
a,b="Cat","Dog"
print(f"Is {a} a subclass of {b}? {'Yes' if is_subclass(a,b,kg) else 'No'}")
