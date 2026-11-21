"""The life-style look, from 21 November 2026 (see life.py):

  21 Nov  pill_box        kitchen table, the medicines list on the phone
  22 Nov  did_mum         the phone at home, family mode (replaces family_mode.jpg)
  26 Nov  only_reason     a quote card (replaces coming_december.jpg)
  29 Nov  call_me         a quote on a light ground, Velta listens (replaces parents_said.jpg)
   1 Dec  walk_together   a walk in the park (replaces move_150.jpg)
  and photo covers for the two reels already published (15 and 18 Nov).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from life import *

# 21 Nov
c = frame(on_screen('kitchen_11.webp', 'meds.png')[0], shift=0.0); shade(c, top=0.9, start=0.4)
words(c, 70, 70, 'Medicine reminders', 'The pill box\ngot a helper'); mark(c); save(c, 'posts/2026-11-21/pill_box.jpg')

# 22 Nov
c = frame(on_screen('hand_home_11.webp', 'mum.png')[0]); shade(c, bottom=0.92, start=0.42)
words(c, 70, 1010, 'Family mode', 'Did Mum take\nher pills today?'); mark(c); save(c, 'posts/2026-11-22/did_mum.jpg')

# 26 Nov
c = Image.new('RGBA', (W, H), NIGHT + (255,)); d = draw(c); star(d, 80, 150, GOLD); y = 270
for line, col in [('“Did you take', WHITE), ('your pills?”', WHITE), ('should not be', WHITE), ('the only reason', GOLD), ('you call Mum.', WHITE)]:
    d.text((80, y), line, font=font('Bold', 92), fill=col); y += 112
d.text((80, y + 50), 'Let the list do the asking.\nYou talk about everything else.', font=font('Regular', 42), fill=LAV, spacing=14)
mark(c); save(c, 'posts/2026-11-26/only_reason.jpg')

# 26 Nov, second choice: not about pills (the week already has four posts on medicines)
c = Image.new('RGBA', (W, H), NIGHT + (255,)); d = draw(c); star(d, 80, 150, GOLD); y = 290
for line, col in [('You look after', WHITE), ('everyone.', WHITE), ('Who looks', GOLD), ('after you?', GOLD)]:
    d.text((80, y), line, font=font('Bold', 104), fill=col); y += 128
d.text((80, y + 50), 'A question for every caregiver.\nAnswer it kindly.', font=font('Regular', 42), fill=LAV, spacing=14)
mark(c); save(c, 'posts/2026-11-26/who_looks_after_you.jpg')

# 29 Nov
c = Image.new('RGBA', (W, H), (238, 233, 255, 255)); d = draw(c); star(d, 80, 130, VIO); y = 240
for line, col in [('“Call me when', INK), ('you get there.”', VIO)]:
    d.text((80, y), line, font=font('Bold', 100), fill=col); y += 122
d.text((80, y + 40), 'What did your parents\nalways tell you?', font=font('Medium', 50), fill=INK, spacing=14)
paste(c, 'velta_listening.png', 460, W - 300, 1010); mark(c, INK); save(c, 'posts/2026-11-29/call_me.jpg')

# 1 Dec
c = frame(plain('walk_11.webp')); shade(c, bottom=0.9, start=0.4)
words(c, 70, 1010, '150 minutes a week · WHO', '22 minutes a day.\nBetter together.'); mark(c); save(c, 'posts/2026-12-01/walk_together.jpg')

# covers for the published reels, 1080x1920; the words sit inside the middle 3:4 that a profile grid shows
R = (1080, 1920)
p, q = on_screen('hand_train_11.webp', 'today.png'); c = frame(p, R, centre=q[:, 0].mean()); shade(c, bottom=0.94, start=0.42)
words(c, 70, 1262, 'One-minute tour', "Your family's health,\nin one app"); mark(c, y=1590); save(c, 'posts/2026-11-15/cover_tour_photo.jpg')
p, q = on_screen('hand_home_3.webp', 'lab_result.png'); c = frame(p, R, centre=q[:, 0].mean()); shade(c, bottom=0.94, start=0.42)
words(c, 70, 1262, 'Lab results', 'A lab sheet,\nin plain words'); mark(c, y=1590); save(c, 'posts/2026-11-17/cover_labs_photo.jpg')
p, q = on_screen('kitchen_3.webp', 'diary_bp.png'); c = frame(p, R, centre=q[:, 0].mean() + 60); shade(c, top=0.94, start=0.42)
words(c, 70, 300, 'Health diary', 'Blood pressure,\nas one clear chart'); mark(c, y=1590); save(c, 'posts/2026-11-19/cover_charts_photo.jpg')
print('ok')
