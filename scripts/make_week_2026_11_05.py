"""Posts for 5, 7 and 8 November 2026. Checked against earlier posts:
no headline, topic or Velta pose repeated from 18-29 October."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *

# 5 Nov — Velta + sleep (diary feature), new topic
c = canvas(); d = draw(c)
y = ctext(d, 150, 'How many hours\ndid you sleep?', font('Bold', 84))
paste(c, 'velta_happy.png', 640, W / 2, y + 320); d = draw(c)
ctext(d, y + 660, 'Most adults need 7 to 9 hours', font('Medium', 44), WHITE)
ctext(d, y + 730, 'Tell Velta in the comments', font('Regular', 40), SUB)
ctext(d, 1180, 'Source: NHS', font('Regular', 28), LAV)
footer(d); save(c, 'posts/2026-11-05/sleep_question.jpg')

# 7 Nov — fact (carousel of 2), text only
c = canvas(); d = draw(c)
y = ctext(d, 330, 'About 1 in 2', font('Bold', 150))
y = ctext(d, y + 20, 'people with a long-term condition\ndo not take their medicines\nas prescribed', font('Medium', 50), WHITE)
ctext(d, y + 60, 'Forgetting, busy days, doubts about a dose', font('Regular', 36), SUB)
ctext(d, 1180, 'Source: WHO, Adherence to long-term therapies', font('Regular', 28), LAV)
footer(d); save(c, 'posts/2026-11-07/fact_1.jpg')

c = canvas(); d = draw(c)
y = ctext(d, 150, 'Small habits help', font('Bold', 84))
rows = [('Same time, every day', 'Tie the dose to a meal or brushing teeth'),
        ('A reminder', 'On the phone, not only in your head'),
        ('Ask, don\'t guess', 'Unsure about a dose? Ask your doctor')]
yy = y + 70
for t, s in rows:
    card(c, 80, yy, W - 160, 210); d = draw(c)
    d.text((130, yy + 38), t, font=font('Bold', 50), fill=WHITE)
    d.text((130, yy + 118), s, font=font('Regular', 34), fill=SUB)
    yy += 250
ctext(d, yy + 30, 'Mivelta · coming soon', font('Medium', 42), LAV)
footer(d); save(c, 'posts/2026-11-07/fact_2.jpg')

# 8 Nov — complaint feature (not shown before)
c = canvas(); d = draw(c)
y = ctext(d, 150, 'Headache for\ntwo days?', font('Bold', 90))
paste(c, 'symbol_glossy.png', 380, W / 2, y + 210); d = draw(c)
yy = y + 430
for t in ['Write what you feel', 'See what you can do at home', 'Know when to see a doctor']:
    card(c, 140, yy, W - 280, 100); d = draw(c)
    ctext(d, yy + 24, t, font('Medium', 40), WHITE)
    yy += 118
ctext(d, yy + 20, 'Coming soon · iOS & Android', font('Medium', 38), LAV)
footer(d); save(c, 'posts/2026-11-08/complaint.jpg')
print('ok')
