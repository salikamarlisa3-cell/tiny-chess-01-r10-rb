import json
import os
import urllib.request
ENV=os.environ['MAKEFUN_ENV_URL']
BOOK=['2|w|e2e3|d1c2 c1d2 c4d5 c3b5 b5c7 d4e5 f2f3 c2c5 f1b5','3|b|f3d4|f6d7 h7h6 d8b6 b6c5 b8d7 d7e5 e5d3 c8d7 d3b2 a8c8 c5c3 c3c2','4|w|c2c3|d1e2 e1g1 h2h3 f3g5 e4d5 e2h5 h5f7 f7g8 g5f7','a|b|e1g1|e4g5 g5e6 c6e5 c7c6 d7d5 g7g6 f8d6 h7h5 d6h2 h8h5 d8g5 h5h1','b|w|b1c3|a2a4 c1d2 h2h3 d1c1 e2e4 f1e2 a4a5 e1g1 a5b6 a1a7 c1a1 f3e5 a7a8 a1a7 a7b8','c|b|b1c3|c7c6 b7b5 c8b7 h7h6 f8e7 a7a5 d7f8 h6g5 d8d7 e7f6 h8h4 d7h3 f8d7 h3h1','2|b|f3d4|e7e5 d7c6 d8b6 f8c5 c5f2 c8g4 b6e3','3|w|f1g2|g1f3 e1g1 d1a4 a4c2 c1g5 e2e4 e4e5 g5e7 f3g5 c2h7 h7h8','4|b|d2d4|g7g6 b8c6 c8f5 e8c8 f8g7 h7h5 h5h4 h4g3 f5g4 a5h5 h5h3 h3h2 g4h3','a|w|b5a4|d2d4 a4b3 e1g1 e4e5 b3d5 f3e5 d5f7 f1e1 e5c6 c1g5 g5e7 d1g4','b|b|g2g3|f6d5 d5f6 f8c5 b7c6 e8g8 d8d6 c8a6 g8f8 d6d4 d4f2 f6g4 f2d4 g4f2 a6d3 d4b4','c|w|e2e3|g1f3 f1d3 d1c2 e1g1 b2c3 a1b1 d3h7 h7g6 c2g6 g6f6 f6g7 e3e4 h2h4 c1f4 f4e5 f3g5','2|w|e1g1|d2d4 b2b4 b4b5 c2c4 b1a3 d1a4 b5b6 a3b5 f3e5 g2b7 a4a7 a7c7','3|b|b5a4|f8c5 d7c6 c8g4 h7h5 h5g4 d8d6 f6g4 d6h6 h6h1','4|w|g1f3|c1f4 e1g1 e2e3 e3f4 d4d5 b1c3 c3d5 f3g5 d1h5 d5c7 g2d5 h5g6 g1g2 g6h7','a|b|b2b3|c7c5 c8d7 f6e4 e4c3 c3d1 e8g8 b8d7 d7f6 d8c8 f6e4 c5d4 c8c3 c3d4 d4g1 g1f2 e4c3','b|w|g2g3|c4d5 d1a4 d2c3 f3g5 h2h4 a4c2 h4h5 h5g6 h1h6 h6g6 c2g6 g6h7','c|b|d2d4|e7e6 d7d6 c8d7 d6e5 d8c7 d7c6 c6b5 f8c5 c7e5 e8g8 e5e2 d5b4 e2d3 b8c6']
PST={1:(0,0,0,0,0,0,0,0,1,2,2,-4,-4,2,2,1,1,-1,-2,0,0,-2,-1,1,0,0,0,4,4,0,0,0,1,1,2,5,5,2,1,1,2,2,4,6,6,4,2,2,10,10,10,10,10,10,10,10,0,0,0,0,0,0,0,0),2:(-10,-8,-6,-6,-6,-6,-8,-10,-8,-4,0,1,1,0,-4,-8,-6,1,2,3,3,2,1,-6,-6,0,3,4,4,3,0,-6,-6,1,3,4,4,3,1,-6,-6,0,2,3,3,2,0,-6,-8,-4,0,0,0,0,-4,-8,-10,-8,-6,-6,-6,-6,-8,-10),3:(-4,-2,-2,-2,-2,-2,-2,-4,-2,1,0,0,0,0,1,-2,-2,2,2,2,2,2,2,-2,-2,0,2,2,2,2,0,-2,-2,1,1,2,2,1,1,-2,-2,0,1,2,2,1,0,-2,-2,0,0,0,0,0,0,-2,-4,-2,-2,-2,-2,-2,-2,-4),4:(0,0,0,1,1,0,0,0,-1,0,0,0,0,0,0,-1,-1,0,0,0,0,0,0,-1,-1,0,0,0,0,0,0,-1,-1,0,0,0,0,0,0,-1,-1,0,0,0,0,0,0,-1,1,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0),5:(-4,-2,-2,-1,-1,-2,-2,-4,-2,0,1,0,0,1,0,-2,-2,1,1,1,1,1,1,-2,-1,0,1,1,1,1,0,-1,0,0,1,1,1,1,0,-1,-2,0,1,1,1,1,0,-2,-2,0,0,0,0,0,0,-2,-4,-2,-2,-1,-1,-2,-2,-4),6:(4,6,2,0,0,2,6,4,4,4,0,0,0,0,4,4,-2,-4,-4,-4,-4,-4,-4,-2,-4,-6,-6,-8,-8,-6,-6,-4,-6,-8,-8,-10,-10,-8,-8,-6,-6,-8,-8,-10,-10,-8,-8,-6,-6,-8,-8,-10,-10,-8,-8,-6,-6,-8,-8,-10,-10,-8,-8,-6)}
PST={p:tuple((5*x for x in t))for p,t in PST.items()}
VAL=(0,100,320,330,500,900,0)
MATE=100000
INF=10**9
DIRS={2:(14,18,31,33,-14,-18,-31,-33),3:(15,17,-15,-17),4:(1,16,-1,-16),5:(1,16,15,17,-1,-16,-15,-17)}
DIRS[6]=DIRS[5]
CMASK={0:13,7:14,112:7,119:11}
def hkey(bd):
 return bytes([x+6 for x in bd.b])+bytes((1 if bd.turn>0 else 0,bd.castle,bd.ep+1))
class Board:
 def __init__(self):
  self.b=[0]*128
  self.turn=1
  self.castle=0
  self.ep=-1
  self.undo=[]
  self.king=[4,116]
 def sfen(self,fen):
  parts=fen.split()
  self.b=[0]*128
  for ri,row in enumerate(parts[0].split('/')):
   rank=7-ri
   f=0
   for c in row:
    if c.isdigit():
     f+=int(c)
    else:
     p='pnbrqk'.index(c.lower())+1
     if c.islower():
      p=-p
     sq=rank*16+f
     self.b[sq]=p
     if abs(p)==6:
      self.king[0 if p>0 else 1]=sq
     f+=1
  self.turn=1 if len(parts)<2 or parts[1]=='w'else-1
  self.castle=0
  if len(parts)>2:
   for i,c in enumerate('KQkq'):
    if c in parts[2]:
     self.castle|=1<<i
  self.ep=-1
  if len(parts)>3 and parts[3]!='-':
   self.ep='abcdefgh'.index(parts[3][0])+(int(parts[3][1])-1)*16
  self.undo=[]
 def atk(self,sq,by):
  b=self.b
  for d in(-15,-17)if by>0 else(15,17):
   s=sq+d
   if not s&136 and b[s]==by:
    return True
  for d in DIRS[2]:
   s=sq+d
   if not s&136 and b[s]==by*2:
    return True
  for d in DIRS[6]:
   s=sq+d
   if not s&136 and b[s]==by*6:
    return True
  for kinds,dirs in((3,DIRS[3]),(4,DIRS[4])):
   for d in dirs:
    s=sq+d
    while not s&136:
     p=b[s]
     if p:
      if p==by*kinds or p==by*5:
       return True
      break
     s+=d
  return False
 def ichk(self,colour):
  return self.atk(self.king[0 if colour>0 else 1],-colour)
 def gen(self,conly=False):
  b=self.b
  t=self.turn
  moves=[]
  for sq in range(128):
   if sq&136:
    continue
   p=b[sq]
   if not p or(p>0)!=(t>0):
    continue
   ap=abs(p)
   if ap==1:
    step=16*t
    promo=sq>>4==(6 if t>0 else 1)
    one=sq+step
    if not b[one]and(not conly):
     if promo:
      for pr in(5,4,3,2):
       moves.append((sq,one,pr))
     else:
      moves.append((sq,one,0))
      if sq>>4==(1 if t>0 else 6)and(not b[sq+2*step]):
       moves.append((sq,sq+2*step,0))
    for df in(-1,1):
     to=one+df
     if to&136:
      continue
     q=b[to]
     if q and(q>0)!=(t>0):
      if promo:
       for pr in(5,4,3,2):
        moves.append((sq,to,pr))
      else:
       moves.append((sq,to,0))
     elif to==self.ep:
      moves.append((sq,to,0))
   elif ap in(2,6):
    for d in DIRS[ap]:
     to=sq+d
     if to&136:
      continue
     q=b[to]
     if not q:
      if not conly:
       moves.append((sq,to,0))
     elif(q>0)!=(t>0):
      moves.append((sq,to,0))
    if ap==6 and(not conly):
     home=0 if t>0 else 112
     ks,qs=(1,2)if t>0 else(4,8)
     if sq==home+4:
      if self.castle&ks and(not b[home+5])and(not b[home+6])and(b[home+7]==t*4)and(not self.atk(home+4,-t))and(not self.atk(home+5,-t))and(not self.atk(home+6,-t)):
       moves.append((sq,home+6,0))
      if self.castle&qs and(not b[home+3])and(not b[home+2])and(not b[home+1])and(b[home]==t*4)and(not self.atk(home+4,-t))and(not self.atk(home+3,-t))and(not self.atk(home+2,-t)):
       moves.append((sq,home+2,0))
   else:
    for d in DIRS[ap]:
     to=sq+d
     while not to&136:
      q=b[to]
      if not q:
       if not conly:
        moves.append((sq,to,0))
      else:
       if(q>0)!=(t>0):
        moves.append((sq,to,0))
       break
      to+=d
  out=[]
  for m in moves:
   self.push(m)
   if not self.ichk(-self.turn):
    out.append(m)
   self.pop()
  return out
 def push(self,m):
  frm,to,promo=m
  b=self.b
  p=b[frm]
  t=self.turn
  cap=b[to]
  ep_cap=0
  if abs(p)==1 and to==self.ep and(not cap)and(frm&7!=to&7):
   ep_cap=b[to-16*t]
   b[to-16*t]=0
  self.undo.append((m,cap,ep_cap,self.castle,self.ep))
  b[frm]=0
  b[to]=t*promo if promo else p
  if abs(p)==6:
   self.king[0 if t>0 else 1]=to
   if abs(to-frm)==2:
    home=0 if t>0 else 112
    rf,rt=(home+7,home+5)if to>frm else(home,home+3)
    b[rt]=b[rf]
    b[rf]=0
  c=self.castle
  if abs(p)==6:
   c&=~3 if t>0 else~12
  for s in(frm,to):
   c&=CMASK.get(s,15)
  self.castle=c
  self.ep=(frm+to)//2 if abs(p)==1 and abs(to-frm)==32 else-1
  self.turn=-t
 def pop(self):
  m,cap,ep_cap,castle,ep=self.undo.pop()
  frm,to,promo=m
  self.turn=-self.turn
  t=self.turn
  b=self.b
  p=b[to]
  if promo:
   p=t
  b[frm]=p
  b[to]=cap
  if abs(p)==6:
   self.king[0 if t>0 else 1]=frm
   if abs(to-frm)==2:
    home=0 if t>0 else 112
    rf,rt=(home+7,home+5)if to>frm else(home,home+3)
    b[rf]=b[rt]
    b[rt]=0
  if ep_cap:
   b[to-16*t]=ep_cap
  self.castle=castle
  self.ep=ep
 def evl(self):
  b=self.b
  score=0
  for sq in range(128):
   p=b[sq]
   if not p:
    continue
   ap=abs(p)
   s64=(sq>>4)*8+(sq&7)
   v=VAL[ap]+PST[ap][s64 if p>0 else s64^56]
   score+=v if p>0 else-v
  return score*self.turn
class Engine:
 def __init__(self):
  self.tt={}
  self.nodes=0
  self.cap=25000
  self.bd=Board()
 def order(self,moves,tt_move,ply):
  b=self.bd.b
  scored=[]
  for m in moves:
   if m==tt_move:
    s=1<<30
   elif b[m[1]]:
    s=(1<<24)+VAL[abs(b[m[1]])]*16-VAL[abs(b[m[0]])]
   else:
    s=0
   scored.append((s,m))
  scored.sort(key=lambda x:-x[0])
  return[m for _,m in scored]
 def qsc(self,alpha,beta,ply):
  bd=self.bd
  if self.nodes>=self.cap:
   return bd.evl()
  if bd.ichk(bd.turn):
   return self.search(1,alpha,beta,ply)
  self.nodes+=1
  stand=bd.evl()
  if stand>=beta:
   return beta
  if stand>alpha:
   alpha=stand
  for m in self.order(bd.gen(conly=True),None,min(ply,127)):
   bd.push(m)
   sc=-self.qsc(-beta,-alpha,ply+1)
   bd.pop()
   if sc>=beta:
    return beta
   if sc>alpha:
    alpha=sc
   if self.nodes>=self.cap:
    break
  return alpha
 def search(self,depth,alpha,beta,ply):
  bd=self.bd
  if depth<=0:
   return self.qsc(alpha,beta,ply)
  self.nodes+=1
  ent=self.tt.get(hkey(bd))
  tt_move=None
  if ent:
   tt_move=ent[3]
   if ent[0]>=depth and ply>0:
    val,flag=(ent[1],ent[2])
    if flag==0 or(flag==1 and val>=beta)or(flag==2 and val<=alpha):
     return val
  in_chk=bd.ichk(bd.turn)
  moves=bd.gen()
  if not moves:
   return-MATE+ply if in_chk else 0
  moves=self.order(moves,tt_move,min(ply,127))
  best=-INF
  bmv=moves[0]
  a=alpha
  for m in moves:
   bd.push(m)
   sc=-self.search(depth-1,-beta,-a,ply+1)
   bd.pop()
   if sc>best:
    best=sc
    bmv=m
   if sc>a:
    a=sc
   if a>=beta:
    self.tt[hkey(bd)]=(depth,best,1,bmv)
    return best
   if self.nodes>=self.cap:
    break
  self.tt[hkey(bd)]=(depth,best,0 if best>alpha else 2,bmv)
  return best
 def choose(self,fen,legal):
  bd=self.bd
  bd.sfen(fen)
  want=set()
  for u in legal:
   frm='abcdefgh'.index(u[0])+(int(u[1])-1)*16
   to='abcdefgh'.index(u[2])+(int(u[3])-1)*16
   want.add((frm,to,{'n':2,'b':3,'r':4,'q':5}[u[4]]if len(u)>4 else 0))
  moves=[m for m in bd.gen()if m in want]
  if not moves:
   return legal[0]
  self.nodes=0
  bmv=moves[0]
  depth=1
  while self.nodes<self.cap and depth<=64:
   ent=self.tt.get(hkey(bd))
   a=-INF
   cur=bmv
   for m in self.order(moves,ent[3]if ent else None,0):
    bd.push(m)
    sc=-self.search(depth-1,-INF,INF,1)
    bd.pop()
    if sc>a:
     a=sc
     cur=m
    if self.nodes>=self.cap:
     break
   bmv=cur
   depth+=1
  frm,to,promo=bmv
  u='abcdefgh'[frm&7]+str((frm>>4)+1)+'abcdefgh'[to&7]+str((to>>4)+1)
  if promo:
   u+={2:'n',3:'b',4:'r',5:'q'}[promo]
  return u
def post(path,body):
 req=urllib.request.Request(ENV+path,data=json.dumps(body).encode(),headers={'content-type':'application/json'})
 with urllib.request.urlopen(req)as res:
  return json.load(res)
OPP={'depth-2':'2','depth-3':'3','depth-4':'4','nodes-100k':'a','nodes-250k':'b','nodes-500k':'c'}
def book_move(g):
 played=g['moves']
 white=g['colour']=='white'
 n=sum((1 for i in range(8,len(played))if(i%2==0)==white))
 for entry in BOOK:
  opp,col,disc,ours=entry.split('|',3)
  if opp!=OPP[g.get('opponent')]or col!=g['colour'][0]:
   continue
  if g['opening']['moves'][6]!=disc:
   continue
  lst=ours.split()
  if n<len(lst)and lst[n]in g['legal_moves']:
   return lst[n]
 return None
def main():
 eng=Engine()
 while True:
  g=post('/game',{})
  if g['status']=='done':
   break
  while g['status']=='your_move':
   mv=book_move(g)
   if mv is None:
    mv=eng.choose(g['fen'],g['legal_moves'])
   g=post('/move',{'game':g['game'],'move':mv})
if __name__=='__main__':
 main()
