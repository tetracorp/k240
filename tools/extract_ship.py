#!/usr/bin/env python

# K240 alien ship sprite extractor
# <https://tetracorp.github.io/k240/>

import struct
import numpy as np
from PIL import Image,ImageOps

# K240 sprite extractor
path = "k240/aliens"

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

# a1data1: 61 entries of 10 bytes: 4 offset start 4 offset end 2 sprite
# records: 8 sprites x 4 small ships, 8 sprites 2 medium,
# 2 transporter and battleship, 11 missile silo launch animation

spr_names = []
for n in range(1,5):
  for n2 in range(0,8):
    spr_names.append( f"ship_small_{n}_{n2}")
for n in range(1,3):
  for n2 in range(0,8):
    spr_names.append( f"ship_med_{n+4}_{n2}" )
spr_names.append("transporter")
spr_names.append("battleship")
for n in range(0,15):
  spr_names.append(f"missile_silo_anim_{n}")

# Ignore start value, only count difference between start/end
sprite_lists = ["0"]
for alien in range(1,7):
  sprites = []
  with open(f"{path}/a{alien}data1", "rb") as f: 
    with open(f'{path}/a{alien}data2', 'rb') as f2:
      for n in range(0,61): # all files have 61 sprites
        row = f.read(10)
        (st,ed,ht) = struct.unpack('>IIH',row)
        ln = ed-st
        wd = (ln//ht)*2
        name = spr_names[n]

        data = f2.read(ln)
        mask = f2.read(ln//4)
        data = np.frombuffer(data, dtype=np.uint8)

        bitplanes = np.unpackbits(data)
        bitplanes = np.reshape(bitplanes, (4, -1, ht, wd))
        pixels = np.sum(bitplanes * (1 << np.arange(4, dtype=np.uint8)).reshape(-1, 1, 1, 1), axis=0)
        pixels = pixels.astype(np.uint8)

        for palette in [palette1,palette2]:
          palette_image = Image.new('P', (1, 1), color=0)
          palette_image.putpalette([c for rgb in palette for c in rgb])

          indexed_image = Image.fromarray(pixels[0], mode='P')
          indexed_image.putpalette(palette_image.palette)

          sprites.append(indexed_image)

    sprite_sets = [
      ( "ship_small_1", sprites[0:16] ),
      ( "ship_small_2", sprites[16:32] ),
      ( "ship_small_3", sprites[32:48] ),
      ( "ship_small_4", sprites[48:64] ),
      ( "ship_med_5", sprites[64:80] ),
      ( "ship_med_6", sprites[80:96] ),
      ( "ship_transporter", sprites[96:98] ),
      ( "ship_battleship", sprites[98:100] ),
      ( "missile_silo_anim", sprites[100:] ),
    ]

    for name,spr in sprite_sets:
      max_height = 0
      print(name)
      for frame in spr:
        if max_height < frame.size[1]:
          max_height = frame.size[1]
      frames = []
      for frame in spr:
        if frame.size[1] > 1: # ignore 1 frame dummy entries
          width = frame.size[0]
          height = frame.size[1]
          new_frame = Image.new('P',(width,max_height),0)
          new_frame.putpalette(frame.palette)
          new_frame.paste(frame, (0,max_height-height))
          # resize
          new_frame = new_frame.resize((width*2,max_height*2),resample=Image.NEAREST)
          new_frame.info
          frames.append(new_frame)
      frames[0].save(f"{ali[alien]}_{name}.gif", save_all=True,
       append_images=frames[1:], duration=200, loop=0, transparency=0, disposal=2)
