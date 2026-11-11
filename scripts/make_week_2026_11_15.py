"""Posts for 15-26 November 2026, before the App Store launch.
No headline, topic or Velta pose repeated from 18 Oct - 8 Nov."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *

# 15 Nov — Velta asks: who reminds your parents? (family mode)
c = canvas(); d = draw(c)
y = ctext(d, 150, 'Who reminds\nyour parents?', font('Bold', 90))
paste(c, 'velta_open.png', 600, W / 2, y + 300); d = draw(c)
ctext(d, y + 640, 'Pills, water, a short walk', font('Medium', 44), WHITE)
ctext(d, y + 710, 'Tell Velta in the comments', font('Regular', 40), SUB)
footer(d); save(c, 'posts/2026-11-15/who_reminds.jpg')

# 17 Nov — feature: lab results in plain language
c = canvas(); d = draw(c)
y = ctext(d, 150, 'Lab results,\nin plain words', font('Bold', 90))
yy = y + 80
for t, s in [('Snap the sheet', 'One photo of your lab results'),
             ('See each value', 'Its normal range, in simple words'),
             ('Ask your doctor', 'Questions worth taking with you')]:
    card(c, 80, yy, W - 160, 200); d = draw(c)
    d.text((130, yy + 36), t, font=font('Bold', 50), fill=WHITE)
    d.text((130, yy + 112), s, font=font('Regular', 34), fill=SUB)
    yy += 235
ctext(d, yy + 30, 'Coming soon · iOS & Android', font('Medium', 40), LAV)
footer(d); save(c, 'posts/2026-11-17/lab_results.jpg')

# 19 Nov — fact: blood pressure
c = canvas(); d = draw(c)
y = ctext(d, 200, 'Almost half', font('Bold', 140))
y = ctext(d, y + 20, 'of adults with high blood pressure\ndo not know they have it', font('Medium', 50), WHITE)
y = ctext(d, y + 70, 'A simple check at home or at a pharmacy\ncan tell you. Talk to your doctor about it.', font('Regular', 36), SUB)
paste(c, 'symbol_glossy.png', 300, W / 2, y + 220); d = draw(c)
ctext(d, 1180, 'Source: WHO, Hypertension fact sheet', font('Regular', 28), LAV)
footer(d); save(c, 'posts/2026-11-19/bp_fact.jpg')

# 22 Nov — feature: family mode
c = canvas(); d = draw(c)
y = ctext(d, 150, 'Did Mum take\nher pill today?', font('Bold', 88))
paste(c, 'velta_heart.png', 520, W / 2, y + 270, soft_edge=True); d = draw(c)
yy = y + 560
for t in ['She ticks it on her phone', 'You see it on yours', 'Missed? You get a gentle note']:
    card(c, 140, yy, W - 280, 96); d = draw(c)
    ctext(d, yy + 22, t, font('Medium', 38), WHITE)
    yy += 112
footer(d); save(c, 'posts/2026-11-22/family_mode.jpg')

# 24 Nov — fact: stroke signs (NHS F.A.S.T.)
c = canvas(); d = draw(c)
y = ctext(d, 150, 'Know the signs:\nF.A.S.T.', font('Bold', 88))
yy = y + 60
for t, s in [('Face', 'Has one side dropped?'),
             ('Arms', 'Can they lift both arms?'),
             ('Speech', 'Is it slurred or strange?'),
             ('Time', 'Call emergency services at once')]:
    card(c, 80, yy, W - 160, 150); d = draw(c)
    d.text((130, yy + 24), t, font=font('Bold', 46), fill=WHITE)
    d.text((130, yy + 86), s, font=font('Regular', 34), fill=SUB)
    yy += 172
ctext(d, 1180, 'Source: NHS, Stroke symptoms', font('Regular', 28), LAV)
footer(d); save(c, 'posts/2026-11-24/fast.jpg')

# 26 Nov — countdown
c = canvas(); d = draw(c)
y = ctext(d, 170, 'Coming in\nDecember', font('Bold', 110))
paste(c, 'velta_happy.png', 560, W / 2, y + 300); d = draw(c)
ctext(d, y + 620, 'Mivelta · AI Family Health', font('Bold', 50), WHITE)
ctext(d, y + 690, 'iPhone first, then Android', font('Regular', 40), SUB)
footer(d); save(c, 'posts/2026-11-26/coming_december.jpg')
print('ok')
