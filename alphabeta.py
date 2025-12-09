import math, copy

E='.'; P='P'; A='A'; N=8

def board():
    b=[[E]*N for _ in range(N)]
    for r in range(3):
        for c in range(N):
            if (r+c)%2: b[r][c]=A
    for r in range(5,8):
        for c in range(N):
            if (r+c)%2: b[r][c]=P
    return b

def show(b):
    print("  "+" ".join(map(str,range(N))))
    for i,r in enumerate(b): print(i," ".join(r))
    print()

def moves(b,p):
    M=[]
    dirs=[(-1,-1),(-1,1)] if p==P else [(1,-1),(1,1)]
    for r in range(N):
        for c in range(N):
            if b[r][c]==p:
                for dr,dc in dirs:
                    r2,c2=r+dr,c+dc
                    if 0<=r2<N and 0<=c2<N:
                        if b[r2][c2]==E: M.append(((r,c),(r2,c2)))
                        elif b[r2][c2]!=p:
                            r3,c3=r2+dr,c2+dc
                            if 0<=r3<N and 0<=c3<N and b[r3][c3]==E:
                                M.append(((r,c),(r3,c3)))
    return M

def move(b,m):
    nb=copy.deepcopy(b)
    (r1,c1),(r2,c2)=m
    nb[r1][c1]=E; nb[r2][c2]=b[r1][c1]
    if abs(r1-r2)==2: nb[(r1+r2)//2][(c1+c2)//2]=E
    return nb

def score(b):
    return sum(r.count(A) for r in b)-sum(r.count(P) for r in b)

def over(b):
    return not moves(b,P) or not moves(b,A)

def minimax(b,d,a,beta,maxp):
    if d==0 or over(b): return score(b),b
    best=-math.inf if maxp else math.inf
    bestb=b
    for m in moves(b,A if maxp else P):
        v,_=minimax(move(b,m),d-1,a,beta,not maxp)
        if maxp:
            if v>best: best,bestb=v,move(b,m)
            a=max(a,v); 
        else:
            if v<best: best,bestb=v,move(b,m)
            beta=min(beta,v)
        if beta<=a: break
    return best,bestb

def play():
    b=board(); show(b)
    while not over(b):
        ms=moves(b,P)
        print("Moves:",list(enumerate(ms)))
        b=move(b,ms[int(input("Pick: "))])
        _,b=minimax(b,3,-1e9,1e9,True); show(b)
    print("Game Over")

play()
