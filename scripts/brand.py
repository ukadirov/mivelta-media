"""Mivelta post toolkit (Pillow). Usage example:

    from brand import *
    c = canvas()                       # 1080x1350 navy-violet gradient
    paste(c, 'velta_happy.png', 820, W/2, 560)
    d = draw(c)
    y = ctext(d, 990, "Hi, I'm Velta", font('Bold', 100))
    ctext(d, y + 5, 'Second line\\nthird line', font('Regular', 42), SUB)
    footer(d)
    save(c, 'posts/2026-10-25/post1.jpg')

Assets in ../assets: velta_happy, velta_open, velta_salad, velta_heart (has own bg),
symbol_glossy, bg_gradient, app_icon. Font: Poppins (Regular/Medium/Bold/Light).
Size 'story' = 1080x1920 for TikTok / Stories.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
A = os.path.join(ROOT, 'assets') + '/'
F = '/usr/share/fonts/truetype/google-fonts/Poppins-'
W, H = 1080, 1350
WHITE = (255, 255, 255); LAV = (205, 196, 255); SUB = (220, 226, 255)

def font(weight, size): return ImageFont.truetype(F + weight + '.ttf', size)

def canvas(size='post'):
    w, h = (1080, 1920) if size == 'story' else (W, H)
    s = max(w, h)
    g = Image.open(A + 'bg_gradient.png').convert('RGB').resize((s, s), Image.LANCZOS)
    g = g.crop(((s - w) // 2, (s - h) // 2, (s - w) // 2 + w, (s - h) // 2 + h))
    g = Image.blend(g, Image.new('RGB', (w, h), (10, 18, 60)), 0.35)
    return g.convert('RGBA')

def draw(c): return ImageDraw.Draw(c)

def paste(c, name, width, cx, cy, soft_edge=False):
    im = Image.open(A + name).convert('RGBA'); r = width / im.width
    im = im.resize((int(im.width * r), int(im.height * r)), Image.LANCZOS)
    if soft_edge:  # for images with their own background (velta_heart, app_icon)
        m = Image.new('L', im.size, 0)
        ImageDraw.Draw(m).ellipse((40, 40, im.width - 40, im.height - 40), fill=255)
        im.putalpha(m.filter(ImageFilter.GaussianBlur(60)))
    c.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))

def ctext(d, y, txt, f, fill=WHITE):
    cw = d.im.size[0]
    for line in txt.split('\n'):
        w = d.textlength(line, font=f); d.text(((cw - w) / 2, y), line, font=f, fill=fill)
        y += int(f.size * 1.25)
    return y

def card(c, x, y, w, h):
    box = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(box).rounded_rectangle((0, 0, w - 1, h - 1), radius=40,
        fill=(255, 255, 255, 34), outline=(255, 255, 255, 70), width=2)
    c.alpha_composite(box, (x, y))

def footer(d, text='@mivelta.app'):
    cw, ch = d.im.size; f = font('Medium', 30)
    d.text(((cw - d.textlength(text, font=f)) / 2, ch - 90), text, font=f, fill=(190, 200, 240))

def save(c, rel_path):
    p = os.path.join(ROOT, rel_path); os.makedirs(os.path.dirname(p), exist_ok=True)
    c.convert('RGB').save(p, quality=90); return p

def raw_url(rel_path):
    return 'https://raw.githubusercontent.com/ukadirov/mivelta-media/main/' + rel_path.lstrip('/')
