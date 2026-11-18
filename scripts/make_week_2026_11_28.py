"""Posts for 28 November - 4 December 2026: useful tips with a named source
and a Velta question, not app demos (Umid, 2026-11-19). Each picture has its
own ground and layout, so the profile grid does not show one post five times:

  28 Nov  bp_521        light lavender, three big numbers        (CDC)
  29 Nov  parents_said  the brand night, speech bubbles, Velta listens
   1 Dec  move_150      warm cream, a week of seven bars         (WHO)
   4 Dec  water         pale blue, eight glasses                 (NHS)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from brand import *

INK, DIM, VIO = (22, 27, 68), (86, 80, 140), (104, 84, 214)


def wash(top, bottom, glow=None):
    """A light vertical wash with an optional soft glow (colour, x, y, radius)."""
    y = np.linspace(0, 1, H)[:, None, None]
    a = np.repeat(np.array(top, float) * (1 - y) + np.array(bottom, float) * y, W, axis=1)
    if glow:
        col, gx, gy, r = glow; yy, xx = np.mgrid[0:H, 0:W]
        k = np.clip(1 - np.hypot(xx - gx, yy - gy) / r, 0, 1)[..., None] ** 2
        a = a * (1 - k) + np.array(col, float) * k
    return Image.fromarray(a.astype(np.uint8)).convert('RGBA')


def white_card(c, box, radius=44, fill=(255, 255, 255, 235)):
    """A white card with a soft shadow, for the light grounds."""
    x0, y0, x1, y1 = box
    sh = Image.new('RGBA', c.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((x0, y0 + 14, x1, y1 + 14), radius, fill=(60, 50, 130, 60))
    c.alpha_composite(sh.filter(ImageFilter.GaussianBlur(22)))
    lay = Image.new('RGBA', c.size, (0, 0, 0, 0))
    ImageDraw.Draw(lay).rounded_rectangle(box, radius, fill=fill)
    c.alpha_composite(lay)


def foot(d, source, fill=DIM):
    ctext(d, 1196, source, font('Regular', 28), fill)
    footer_f = font('Medium', 30); t = '@mivelta.app'
    d.text(((W - d.textlength(t, font=footer_f)) / 2, H - 90), t, font=footer_f, fill=fill)


# 28 Nov — tip: blood pressure at home, 5 · 2 · 1
c = wash((240, 235, 255), (210, 200, 252), glow=((255, 255, 255), 240, 300, 640)); d = draw(c)
y = ctext(d, 110, 'Blood pressure\nat home: 5 · 2 · 1', font('Bold', 84), INK)
yy = y + 50
for n, t, s in [('5', 'minutes of quiet sitting', 'Back supported, feet flat, arm on a table'),
                ('2', 'readings each time', 'Do not talk while the cuff is working'),
                ('1', 'minute between them', 'Write both numbers down')]:
    white_card(c, (80, yy, W - 80, yy + 210)); d = draw(c)
    d.ellipse((116, yy + 31, 264, yy + 179), fill=VIO)
    f = font('Bold', 104); w = d.textlength(n, font=f); d.text((190 - w / 2, yy + 32), n, font=f, fill=WHITE)
    d.text((306, yy + 44), t, font=font('Bold', 46), fill=INK)
    d.text((306, yy + 116), s, font=font('Regular', 31), fill=DIM)
    yy += 240
ctext(d, yy + 14, 'Same time each day. Show the log to your doctor.', font('Medium', 35), INK)
foot(d, 'Source: CDC, Measuring Your Blood Pressure'); save(c, 'posts/2026-11-28/bp_521.jpg')


# 29 Nov — Velta asks: what did your parents always tell you?
def bubble(c, cx, cy, text, tail, size=44):
    """A speech bubble centred on (cx, cy); its tail points down-left or down-right."""
    f = font('Medium', size); d = draw(c); lines = text.split('\n')
    w = max(d.textlength(l, font=f) for l in lines) + 84; h = len(lines) * int(size * 1.25) + 56
    x0, y0 = int(cx - w / 2), int(cy - h / 2)
    lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    tx = x0 + (70 if tail == 'left' else w - 70); dx = -34 if tail == 'left' else 34
    ld.polygon([(tx - 30, y0 + h - 8), (tx + 30, y0 + h - 8), (tx + dx, y0 + h + 46)], fill=(255, 255, 255, 245))
    ld.rounded_rectangle((x0, y0, x0 + w, y0 + h), 46, fill=(255, 255, 255, 245))
    c.alpha_composite(lay); d = draw(c); ty = y0 + 26
    for l in lines:
        d.text((cx - d.textlength(l, font=f) / 2, ty), l, font=f, fill=INK); ty += int(size * 1.25)

c = canvas(); d = draw(c)
y = ctext(d, 110, 'What did your parents\nalways tell you?', font('Bold', 78))
bubble(c, 300, y + 150, '“Wear a hat!”', 'right')
bubble(c, 770, y + 290, '“Have you eaten?”', 'left')
bubble(c, 330, y + 440, '“Call me when\nyou get there.”', 'right')
paste(c, 'velta_listening.png', 400, W / 2 + 190, y + 640); d = draw(c)
ctext(d, 1172, 'Write yours in the comments', font('Medium', 42), SUB)
footer(d); save(c, 'posts/2026-11-29/parents_said.jpg')

# 1 Dec — fact: 150 minutes a week
c = wash((255, 243, 230), (234, 224, 255), glow=((255, 255, 255), 820, 330, 620)); d = draw(c)
y = ctext(d, 80, '150', font('Bold', 250), INK)
y = ctext(d, y - 28, 'minutes of movement a week', font('Bold', 56), INK)
y = ctext(d, y + 6, 'WHO advises adults to get at least this much', font('Regular', 34), DIM)
white_card(c, (80, y + 40, W - 80, y + 400)); d = draw(c)
bw, gap = 96, 30; x = (W - 7 * bw - 6 * gap) // 2
for i, day in enumerate('MTWTFSS'):
    d.rounded_rectangle((x, y + 150, x + bw, y + 300), 30, fill=VIO)
    f = font('Bold', 46); w = d.textlength('22', font=f); d.text((x + bw / 2 - w / 2, y + 190), '22', font=f, fill=WHITE)
    f = font('Medium', 30); w = d.textlength(day, font=f); d.text((x + bw / 2 - w / 2, y + 316), day, font=f, fill=DIM)
    x += bw + gap
ctext(d, y + 72, 'About 22 minutes a day', font('Bold', 44), INK)
paste(c, 'velta_proud.png', 330, W - 210, 1030); d = draw(c)
d.text((90, 950), 'A brisk walk counts.', font=font('Bold', 46), fill=INK)
d.text((90, 1020), 'Any amount is better\nthan none.', font=font('Regular', 38), fill=DIM, spacing=10)
foot(d, 'Source: WHO, Physical activity fact sheet'); save(c, 'posts/2026-12-01/move_150.jpg')


# 4 Dec — tip: 6 to 8 glasses of fluid
def glass(c, x, y, w, h, level, tint):
    """A drinking glass at (x, y), filled to [level] (0..1)."""
    lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); s = int(w * 0.13)
    body = [(x, y), (x + w, y), (x + w - s, y + h), (x + s, y + h)]
    d.polygon(body, fill=(255, 255, 255, 150))
    if level > 0:
        ly = y + h * (1 - level); k = (ly - y) / h
        d.polygon([(x + s * k, ly), (x + w - s * k, ly), (x + w - s, y + h), (x + s, y + h)], fill=tint)
    d.line(body + [body[0]], fill=INK + (255,), width=6, joint='curve')
    c.alpha_composite(lay)

c = wash((226, 242, 255), (198, 212, 255), glow=((255, 255, 255), 260, 380, 640)); d = draw(c)
y = ctext(d, 110, '6 to 8 glasses\nof fluid a day', font('Bold', 92), INK)
y = ctext(d, y + 14, 'Tea and coffee count too', font('Medium', 48), VIO)
gw, gh, gap = 150, 200, 52; x0 = (W - 4 * gw - 3 * gap) // 2
for i in range(8):
    gx, gy = x0 + (i % 4) * (gw + gap), y + 60 + (i // 4) * (gh + 50)
    glass(c, gx, gy, gw, gh, 0.78 if i < 6 else 0.0, (96, 150, 255, 235) if i < 6 else None)
d = draw(c)
paste(c, 'velta_thirsty.png', 300, W - 200, 1050); d = draw(c)
d.text((90, 985), 'A guide, not a rule.', font=font('Bold', 42), fill=INK)
d.text((90, 1046), 'You may need more when it is\nhot or you are active.', font=font('Regular', 34), fill=DIM, spacing=10)
foot(d, 'Source: NHS, Water, drinks and hydration'); save(c, 'posts/2026-12-04/water.jpg')
print('ok')
