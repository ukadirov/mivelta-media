from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os; U=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','assets')+'/'
F='/usr/share/fonts/truetype/google-fonts/Poppins-'
W,H=1080,1350
def font(w,s): return ImageFont.truetype(F+w+'.ttf',s)
def bg():
    g=Image.open(U+'bg_gradient.png').convert('RGB').resize((H,H),Image.LANCZOS)
    g=g.crop(((H-W)//2,0,(H-W)//2+W,H))
    # darken a bit for text contrast
    ov=Image.new('RGB',(W,H),(10,18,60)); g=Image.blend(g,ov,0.35)
    return g.convert('RGBA')
def paste(c,path,width,cx,cy):
    im=Image.open(U+path).convert('RGBA'); r=width/im.width
    im=im.resize((int(im.width*r),int(im.height*r)),Image.LANCZOS)
    c.alpha_composite(im,(int(cx-im.width/2),int(cy-im.height/2)))
def ctext(d,y,txt,f,fill=(255,255,255)):
    for line in txt.split('\n'):
        w=d.textlength(line,font=f); d.text(((W-w)/2,y),line,font=f,fill=fill); y+=int(f.size*1.25)
    return y
LAV=(205,196,255); SUB=(220,226,255)
def footer(d):
    f=font('Medium',30); t='@mivelta.app'; d.text(((W-d.textlength(t,font=f))/2,H-90),t,font=f,fill=(190,200,240))
out=[]
# 1a
c=bg(); paste(c,'symbol_glossy.png',620,W/2,500); d=ImageDraw.Draw(c)
y=ctext(d,860,'Meet Mivelta',font('Bold',104)); ctext(d,y+10,'AI Family Health',font('Regular',48),LAV); footer(d); out.append(('post1_1',c))
# 1b
c=bg(); d=ImageDraw.Draw(c)
y=ctext(d,170,"Your family's health,\nin one place",font('Bold',78))
paste(c,'velta_open.png',780,W/2,y+340); d=ImageDraw.Draw(c)
ctext(d,y+650,'For you, your parents\nand your kids',font('Regular',46),SUB); footer(d); out.append(('post1_2',c))
# 1c
c=bg(); d=ImageDraw.Draw(c)
y=ctext(d,150,'What Mivelta does',font('Bold',76))
rows=[('Medicines','Reminders on time, for every family member'),('Lab results','Explained in plain words'),('Daily diary','Blood pressure, sugar, sleep, weight')]
yy=y+80
for t,s in rows:
    box=Image.new('RGBA',(W-160,210),(255,255,255,0)); bd=ImageDraw.Draw(box)
    bd.rounded_rectangle((0,0,W-161,209),radius=40,fill=(255,255,255,34),outline=(255,255,255,70),width=2)
    c.alpha_composite(box,(80,yy)); d=ImageDraw.Draw(c)
    d.text((130,yy+38),t,font=font('Bold',54),fill=(255,255,255))
    d.text((130,yy+118),s,font=font('Regular',36),fill=SUB)
    yy+=250
ctext(d,yy+40,'Coming soon · iOS & Android',font('Medium',44),LAV); footer(d); out.append(('post1_3',c))
# 2
c=bg(); paste(c,'velta_happy.png',820,W/2,560); d=ImageDraw.Draw(c)
y=ctext(d,990,"Hi, I'm Velta",font('Bold',100))
ctext(d,y+5,'I live inside Mivelta and help\nyour family stay on track',font('Regular',42),SUB); footer(d); out.append(('post2',c))
# 3
c=bg(); d=ImageDraw.Draw(c)
y=ctext(d,140,'Did mom take her\nmedicine today?',font('Bold',82))
im=Image.open(U+'velta_heart.png').convert('RGBA').resize((760,760),Image.LANCZOS)
m=Image.new('L',(760,760),0); ImageDraw.Draw(m).ellipse((40,40,720,720),fill=255); m=m.filter(ImageFilter.GaussianBlur(60))
im.putalpha(m); c.alpha_composite(im,(int(W/2-380),y)); d=ImageDraw.Draw(c)
ctext(d,y+740,'Family mode sends you a gentle\nalert if a dose is missed',font('Regular',42),SUB); footer(d); out.append(('post3',c))
for n,c in out: c.convert('RGB').save(n+'.jpg',quality=92)
sheet=Image.new('RGB',(5*360,450),'white')
for i,(n,c) in enumerate(out): sheet.paste(c.convert('RGB').resize((360,450)),(i*360,0))
sheet.save('sheet.png')
