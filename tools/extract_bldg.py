#!/usr/bin/env python

# K240 alien building sprite extractor
# <https://tetracorp.github.io/k240/>

import struct
import numpy as np
from PIL import Image,ImageOps

path = "k240/aliens"
STRINGFILE = "k240/data/gamestrings-english.txt"

palette1 = [
(0x00,0x00,0x00),
(0x66,0x66,0x66),
(0x44,0x44,0x44),
(0x22,0x22,0x22),
(0x00,0x99,0xff),
(0x00,0x33,0x88),
(0xdd,0x66,0x00),
(0xff,0xcc,0x00),
(0x77,0x00,0x00),
(0xcc,0x00,0x00),
(0x00,0x66,0x00),
(0x00,0xcc,0x00),
(0xff,0xff,0xff),
(0xcc,0xbb,0xbb),
(0x77,0x00,0x00),
(0xff,0xff,0x22),
]

# alternate palette for blinking
palette2 = palette1[:]
t = palette2.pop()
palette2.insert(-1,t)

palette = palette1

ali = ["000","kll","ore","axz","tyl","rig","swi"]

names = ["UNKNOWN"]
with open(STRINGFILE) as f:
  strs = f.read().split("\n")
  for s in strs:
    nm = s.split("\t")[-1].lower().replace(" ","_").replace("'","")
    names.append(nm)

for alien in range(1,7):
  sprites = []
  with open(f"{path}/a{alien}data3", "rb") as f:
    with open(f"{path}/a{alien}data3", "rb") as f2:
      with open(f"{path}/a{alien}data4.bin", "rb") as f3:
        f2.seek(400) # skip past index
        f3.seek(34)  # skip to building names
        for n in range(0,40): # 40 buildings
          row = f.read(10)
          (st,ed,ht) = struct.unpack('>IIH',row)
          ln = ed-st
          wd = (ln//ht)*2

          bldg = f3.read(10)
          (name_id, desc, bw,sc,bt,bh,bi,bx) = struct.unpack('>HHBBBBBB',bldg)
          name = f"{names[name_id]}"

          data = f2.read(ln)
          mask = f2.read(ln//4)
          data = np.frombuffer(data, dtype=np.uint8)

          bitplanes = np.unpackbits(data)
          bitplanes = np.reshape(bitplanes, (4, -1, ht, wd))
          pixels = np.sum(bitplanes * (1 << np.arange(4, dtype=np.uint8)).reshape(-1, 1, 1, 1), axis=0)
          pixels = pixels.astype(np.uint8)

          sprite_set = [name]
          for palette in [palette1,palette2]:
            palette_image = Image.new('P', (1, 1), color=0)
            palette_image.putpalette([c for rgb in palette for c in rgb])

            indexed_image = Image.fromarray(pixels[0], mode='P')
            indexed_image.putpalette(palette_image.palette)

            indexed_image = indexed_image.transpose(Image.FLIP_TOP_BOTTOM)
            indexed_image = indexed_image.resize((wd*2,ht*2),resample=Image.NEAREST)

            sprite_set.append(indexed_image)
          sprites.append(sprite_set)

  known_names = []
  for name,spr1,spr2 in sprites:
    name = f"{ali[alien]}_{name}"
    known_names.append(name)
    if known_names.count(name)>1: # dupes
      name = f"{name}{known_names.count(name)}"
    if spr1.size[1] > 2: # ignore dummy sprites
      print(f"{name}.gif")
      spr1.save(f"{name}.gif", save_all=True,
       append_images=[spr2], duration=200, loop=0, transparency=0, disposal=2)
