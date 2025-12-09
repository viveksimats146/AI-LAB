import pygame, sys, math
pygame.init()

W,H=800,600
s=pygame.display.set_mode((W,H))
FONT=pygame.font.SysFont("arial",24)
SFONT=pygame.font.SysFont("arial",18)

WHITE,BLACK,GRAY=(255,255,255),(0,0,0),(200,200,200)
COLORS={"Red":(255,80,80),"Green":(100,255,100),"Blue":(80,150,255),"Yellow":(255,255,100)}
names=list(COLORS.keys())

graph={'A':['B','C','D'],'B':['A','C','E'],'C':['A','B','D','E'],'D':['A','C','E'],'E':['B','C','D']}
pos={'A':(200,200),'B':(400,100),'C':(400,300),'D':(600,200),'E':(500,400)}
node_color={n:None for n in graph}
sel="Red"

def check():
    for n,nb in graph.items():
        for x in nb:
            if node_color[n] and node_color[n]==node_color[x]: return "Invalid!"
    return "Valid!" if all(node_color[n] for n in node_color) else "In Progress..."

def hit(p):
    for n,(x,y) in pos.items():
        if math.dist(p,(x,y))<40: return n
    return None

def draw():
    s.fill(WHITE)
    for a,nb in graph.items():
        for b in nb: pygame.draw.line(s,BLACK,pos[a],pos[b],2)
    for n,(x,y) in pos.items():
        pygame.draw.circle(s,BLACK,(x,y),40)
        pygame.draw.circle(s,node_color[n] if node_color[n] else GRAY,(x,y),35)
        s.blit(FONT.render(n,1,BLACK),(x-10,y-12))
    pygame.draw.rect(s,GRAY,(50,450,700,100),border_radius=10)
    s.blit(FONT.render("Select Color:",1,BLACK),(60,460))
    for i,c in enumerate(names):
        r=pygame.Rect(220+i*120,460,60,60)
        pygame.draw.rect(s,COLORS[c],r)
        if c==sel: pygame.draw.rect(s,BLACK,r,3)
        s.blit(SFONT.render(c,1,BLACK),(220+i*120,525))
    s.blit(FONT.render(check(),1,BLACK),(330,560))
    pygame.display.flip()

run=True
while run:
    draw()
    for e in pygame.event.get():
        if e.type==pygame.QUIT: run=False
        if e.type==pygame.MOUSEBUTTONDOWN:
            x,y=e.pos
            for i,c in enumerate(names):
                if pygame.Rect(220+i*120,460,60,60).collidepoint(x,y): sel=c
            n=hit((x,y))
            if n: node_color[n]=COLORS[sel]

pygame.quit(); sys.exit()