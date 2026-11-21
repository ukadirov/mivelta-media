"""Life-style posts (2026-11-20): a photo from daily life with the real app
on the phone's screen, a few words, the name. Umid chose this look after
the profile had become one navy card fifteen times.

The photos in assets/photos are generated (FLUX.1 Krea) with the phone's
screen a flat bright green; `on_screen` finds that green and puts a real
screenshot from assets/screens there, in perspective, under the photo's
own light and behind any finger that covers the glass. Posts made this
way are marked as AI-generated when they are scheduled.

Needs numpy and scipy next to Pillow."""
import numpy as np
from scipy import ndimage
from brand import *

P, SC = A + 'photos/', A + 'screens/'
INK, VIO, GOLD = (22, 27, 68), (104, 84, 214), (255, 205, 120)
NIGHT = (30, 26, 92)


def on_screen(photo, shot, scale=2):
    """The photo (enlarged [scale] times) with [shot] on its green screen,
    and the screen's four corners."""
    p = Image.open(P + photo).convert('RGB'); p = p.resize((p.width * scale, p.height * scale), Image.LANCZOS)
    a = np.asarray(p).astype(float); r, g, b = a[..., 0], a[..., 1], a[..., 2]
    green = (g > 110) & (g > r * 1.35) & (g > b * 1.35)
    lab, n = ndimage.label(green); m = lab == 1 + int(np.argmax(ndimage.sum(green, lab, range(1, n + 1))))
    ys, xs = np.nonzero(m)   # the corners: the extremes along the two diagonals
    quad = np.array([(xs[i], ys[i]) for i in (np.argmin(xs + ys), np.argmax(xs - ys), np.argmax(xs + ys), np.argmin(xs - ys))], float)
    c = quad.mean(0); quad = c + (quad - c) * 1.035            # past the rounded corners
    s = Image.open(SC + shot).convert('RGB'); w, h = s.size; rows, rhs = [], []
    # The phone in the photo is not as tall as the one the screenshot was taken on: show the top of
    # the screen at its true proportions, never squeezed to fit.
    side = lambda i, j: float(np.hypot(*(quad[i] - quad[j])))
    ratio = (side(0, 1) + side(3, 2)) / (side(0, 3) + side(1, 2))
    if w / h < ratio:
        h = int(w / ratio); s = s.crop((0, 0, w, h))
    else:
        nw = int(h * ratio); s = s.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h)); w = nw
    for (x, y), (u, v) in zip(quad, [(0, 0), (w, 0), (w, h), (0, h)]):
        rows += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; rhs += [u, v]
    warped = s.transform(p.size, Image.PERSPECTIVE, tuple(np.linalg.solve(np.array(rows), np.array(rhs))), Image.BICUBIC)
    light = Image.fromarray(np.clip(np.where(m, g / np.median(g[m]), 1.0) * 200, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(10 * scale))
    k = np.clip(np.asarray(light).astype(float) / 200, 0.78, 1.12)[..., None]
    lit = Image.fromarray(np.clip(np.asarray(warped).astype(float) * k, 0, 255).astype(np.uint8))
    mask = Image.fromarray((ndimage.binary_dilation(m, iterations=2 * scale) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2 * scale))
    p.paste(lit, (0, 0), mask)
    return p, quad


def plain(photo, scale=2):
    p = Image.open(P + photo).convert('RGB'); return p.resize((p.width * scale, p.height * scale), Image.LANCZOS)


def frame(im, size=(W, H), shift=0.5, centre=None):
    """Crop a photo to the post's shape. [shift] 0..1 slides the crop along
    the spare side; [centre] (an x) keeps that point in the middle instead."""
    w, h = im.size; tw, th = size
    if w / h > tw / th:
        nw = int(h * tw / th); x = int((w - nw) * shift) if centre is None else int(min(max(centre - nw / 2, 0), w - nw))
        im = im.crop((x, 0, x + nw, h))
    else:
        nh = int(w * th / tw); y = int((h - nh) * shift); im = im.crop((0, y, w, y + nh))
    return im.resize(size, Image.LANCZOS).convert('RGBA')


def shade(c, top=0.0, bottom=0.0, start=0.45):
    """Darken the top and/or the bottom of a photo for the words."""
    w, h = c.size; y = np.arange(h)[:, None] / h
    a = np.maximum(np.clip((start - y) / start, 0, 1) * top, np.clip((y - (1 - start)) / start, 0, 1) * bottom)
    lay = np.zeros((h, w, 4), np.uint8); lay[..., :3] = (10, 14, 44); lay[..., 3] = (a * 255).astype(np.uint8).repeat(w, axis=1)
    c.alpha_composite(Image.fromarray(lay))


def words(c, x, y, small, big, size=78, sub=None):
    """A small gold line, the big white lines under it, an optional line below."""
    d = draw(c); d.text((x, y), small, font=font('Medium', 34), fill=GOLD); y += 54
    for line in big.split('\n'):
        d.text((x, y), line, font=font('Bold', size), fill=WHITE); y += int(size * 1.16)
    if sub:
        d.text((x, y + 6), sub, font=font('Medium', 36), fill=(225, 228, 255))
    return y


def mark(c, fill=WHITE, y=None):
    d = draw(c); w, h = c.size; f = font('Bold', 40); t = 'Mivelta'
    d.text((w - 70 - d.textlength(t, font=f), (h - 96) if y is None else y), t, font=f, fill=fill)


def star(d, x, y, fill):
    d.text((x, y), '✦', font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 64), fill=fill)
