import random, math, matplotlib.pyplot as plt
import networkx as nx
  
NUM_TASKS = 6; NUM_SLOTS = 3; SLOT_CAPACITY = 2
tasks = [f"Task{i+1}" for i in range(NUM_TASKS)]
slots = [f"Slot{j+1}" for j in range(NUM_SLOTS)]

def cost(schedule):
    c = {s:0 for s in slots}
    for t,slt in schedule.items(): c[slt]+=1
    pen=sum((v-SLOT_CAPACITY)*5 for v in c.values() if v>SLOT_CAPACITY)
    var=sum((v - NUM_TASKS/NUM_SLOTS)**2 for v in c.values())
    return pen+var

def rand_sched(): return {t:random.choice(slots) for t in tasks}

def neighbor(s):
    ns=s.copy()
    ns[random.choice(tasks)] = random.choice(slots)
    return ns

def anneal(T=100, cool=0.95, stop=0.1, it=100):
    cur=rand_sched(); cc=cost(cur)
    best=cur.copy(); bc=cc; hist=[]
    while T>stop:
        for _ in range(it):
            nb=neighbor(cur); nc=cost(nb); d=nc-cc
            if d<0 or random.random()<math.exp(-d/T):
                cur,cc=nb,nc
                if nc<bc: best,bc=nb.copy(),nc
        hist.append(bc); T*=cool
    return best,bc,hist

def visualize(sched,title):
    G=nx.Graph()
    for t,s in sched.items(): G.add_edge(t,s)
    pos={t:(0,i) for i,t in enumerate(tasks)}
    pos.update({s:(2,i) for i,s in enumerate(slots)})
    plt.figure(figsize=(6,4))
    nx.draw(G,pos,with_labels=True,node_size=1500,node_color="lightblue",font_weight="bold")
    plt.title(title); plt.show()

def main():
    best,costv,h=anneal()
    print("Best schedule:")
    for t,s in best.items(): print(f"{t} → {s}")
    print("\nFinal Cost:",costv)
    visualize(best,"Final Schedule")
    plt.plot(h); plt.title("Cost Over Time"); plt.grid(); plt.show()

if __name__=="__main__": main()
