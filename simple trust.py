import random
# -------------------------
# Service Provider
# -------------------------
class Provider:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality
        self.feedback = []
        self.trust = 0
        self.reputation = 0
    def receive_feedback(self, rating):
        self.feedback.append(rating)
        self.trust = sum(self.feedback)/len(self.feedback)
# -------------------------
# Client
# -------------------------
class Client:
    def __init__(self, name):
        self.name = name
    def interact(self, provider):
        rating = 1 if random.random()<provider.quality else -1
        provider.receive_feedback(rating)
        return rating
# -------------------------
# Initialize Providers & Clients
# -------------------------
providers=[Provider("P1",0.9),Provider("P2",0.6),Provider("P3",0.3)]
clients=[Client(f"C{i}") for i in range(1,6)]
# -------------------------
# Interactions
# -------------------------
for c in clients:
    for p in providers:
        r=c.interact(p)
        print(f"{c.name} rated {p.name}: {r}")
# -------------------------
# Compute Reputation
# -------------------------
total_trust=sum(p.trust for p in providers)
for p in providers:
    p.reputation=p.trust/total_trust if total_trust!=0 else 0
# -------------------------
# Select Best Provider
# -------------------------
best=max(providers,key=lambda x:x.reputation)
# -------------------------
# Print Results
# -------------------------
print("\nProvider Trust & Reputation:")
for p in providers:
    print(f"{p.name}: Trust={p.trust:.2f}, Reputation={p.reputation:.2f}")
print(f"\nBest Provider selected: {best.name}")
