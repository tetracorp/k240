#!/usr/bin/env python
#
# extract K240 manual protection strings

codeTable = [
  [0x11,0x17,0x18,0x34,0x28,0x20,0x20,0x20,0x20,0x20, 0x000b ,0x0001 ,0x0004],
  [0x34,0x13,0x37,0x15,0x14,0x13,0x20,0x20,0x20,0x20, 0x000b ,0x0005 ,0x0002],
  [0x21,0x37,0x23,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x000b ,0x0008 ,0x0002],
  [0x21,0x36,0x19,0x17,0x15,0x20,0x20,0x20,0x20,0x20, 0x000b ,0x000a ,0x0006],
  [0x38,0x21,0x16,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x000b ,0x000c ,0x0003],
  [0x23,0x18,0x22,0x34,0x19,0x35,0x13,0x14,0x20,0x20, 0x000b ,0x000d ,0x0007],
  [0x36,0x14,0x19,0x12,0x22,0x13,0x20,0x20,0x20,0x20, 0x000c ,0x0001 ,0x0003],
  [0x36,0x17,0x18,0x29,0x23,0x18,0x37,0x25,0x20,0x20, 0x000c ,0x0003 ,0x0002],
  [0x22,0x13,0x29,0x13,0x34,0x15,0x20,0x20,0x20,0x20, 0x000c ,0x0005 ,0x0005],
  [0x15,0x18,0x38,0x13,0x20,0x20,0x20,0x20,0x20,0x20, 0x000c ,0x0007 ,0x0004],
  [0x37,0x19,0x15,0x18,0x34,0x13,0x20,0x20,0x20,0x20, 0x000c ,0x0009 ,0x0001],
  [0x23,0x21,0x16,0x22,0x20,0x20,0x20,0x20,0x20,0x20, 0x000d ,0x0002 ,0x0008],
  [0x13,0x33,0x18,0x15,0x20,0x20,0x20,0x20,0x20,0x20, 0x000d ,0x0004 ,0x0001],
  [0x22,0x19,0x29,0x21,0x14,0x20,0x20,0x20,0x20,0x20, 0x000d ,0x0005 ,0x0009],
  [0x34,0x19,0x37,0x15,0x14,0x19,0x29,0x20,0x20,0x20, 0x000d ,0x0007 ,0x0005],
  [0x21,0x22,0x15,0x13,0x14,0x19,0x18,0x23,0x20,0x20, 0x000e ,0x0002 ,0x0005],
  [0x38,0x21,0x37,0x17,0x21,0x29,0x20,0x20,0x20,0x20, 0x000e ,0x0004 ,0x0005],
  [0x37,0x13,0x13,0x23,0x20,0x20,0x20,0x20,0x20,0x20, 0x000e ,0x0007 ,0x0005],
  [0x34,0x19,0x37,0x15,0x14,0x19,0x29,0x20,0x20,0x20, 0x0011 ,0x0001 ,0x0004],
  [0x22,0x17,0x38,0x38,0x21,0x14,0x16,0x20,0x20,0x20, 0x0011 ,0x0003 ,0x0003],
  [0x25,0x18,0x35,0x13,0x37,0x20,0x20,0x20,0x20,0x20, 0x0011 ,0x0005 ,0x0004],
  [0x23,0x18,0x22,0x1a,0x29,0x21,0x16,0x20,0x20,0x20, 0x0011 ,0x0006 ,0x0006],
  [0x29,0x21,0x14,0x25,0x13,0x14,0x20,0x20,0x20,0x20, 0x0012 ,0x0002 ,0x0007],
  [0x23,0x13,0x15,0x21,0x18,0x29,0x22,0x20,0x20,0x20, 0x0012 ,0x0003 ,0x0001],
  [0x19,0x14,0x13,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x0012 ,0x0004 ,0x000a],
  [0x22,0x13,0x13,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x0012 ,0x0006 ,0x0007],
  [0x23,0x13,0x15,0x21,0x18,0x29,0x22,0x20,0x20,0x20, 0x0017 ,0x0002 ,0x0005],
  [0x13,0x11,0x17,0x21,0x29,0x22,0x20,0x20,0x20,0x20, 0x0017 ,0x0004 ,0x0009],
  [0x21,0x14,0x38,0x19,0x17,0x14,0x20,0x20,0x20,0x20, 0x0017 ,0x0006 ,0x0004],
  [0x36,0x17,0x18,0x29,0x23,0x20,0x20,0x20,0x20,0x20, 0x0017 ,0x0008 ,0x0002],
  [0x34,0x19,0x22,0x15,0x20,0x20,0x20,0x20,0x20,0x20, 0x0017 ,0x000a ,0x0002],
  [0x36,0x19,0x15,0x15,0x19,0x38,0x20,0x20,0x20,0x20, 0x0018 ,0x0001 ,0x0010],
  [0x18,0x37,0x22,0x15,0x21,0x29,0x29,0x20,0x20,0x20, 0x0018 ,0x0005 ,0x0006],
  [0x36,0x29,0x17,0x13,0x1a,0x14,0x18,0x37,0x15,0x20, 0x0018 ,0x0006 ,0x000a],
  [0x18,0x34,0x19,0x37,0x22,0x20,0x20,0x20,0x20,0x20, 0x0018 ,0x0008 ,0x0005],
  [0x16,0x19,0x17,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x0018 ,0x000a ,0x000a],
  [0x36,0x17,0x15,0x15,0x19,0x37,0x20,0x20,0x20,0x20, 0x001a ,0x0003 ,0x0006],
  [0x22,0x1a,0x21,0x34,0x13,0x20,0x20,0x20,0x20,0x20, 0x001a ,0x0004 ,0x0002],
  [0x38,0x19,0x17,0x22,0x13,0x20,0x20,0x20,0x20,0x20, 0x001b ,0x0001 ,0x0009],
  [0x23,0x13,0x22,0x13,0x29,0x13,0x34,0x15,0x20,0x20, 0x001b ,0x0002 ,0x0005],
  [0x14,0x18,0x25,0x26,0x15,0x20,0x20,0x20,0x20,0x20, 0x001b ,0x0004 ,0x0004],
  [0x22,0x18,0x37,0x34,0x13,0x20,0x20,0x20,0x20,0x20, 0x0020 ,0x0001 ,0x0006],
  [0x21,0x37,0x37,0x17,0x21,0x29,0x29,0x16,0x20,0x20, 0x0020 ,0x0003 ,0x0001],
  [0x13,0x37,0x13,0x38,0x16,0x20,0x20,0x20,0x20,0x20, 0x0020 ,0x000c ,0x000f],
  [0x13,0x37,0x13,0x38,0x16,0x20,0x20,0x20,0x20,0x20, 0x0024 ,0x0007 ,0x0006],
  [0x36,0x13,0x24,0x19,0x14,0x13,0x20,0x20,0x20,0x20, 0x0024 ,0x000a ,0x0005],
  [0x21,0x34,0x34,0x13,0x22,0x22,0x18,0x37,0x25,0x20, 0x0029 ,0x0004 ,0x0003],
  [0x34,0x21,0x37,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x0029 ,0x000c ,0x000c],
  [0x26,0x19,0x12,0x13,0x35,0x13,0x14,0x20,0x20,0x20, 0x002e ,0x0003 ,0x0005],
  [0x23,0x21,0x15,0x21,0x36,0x21,0x22,0x13,0x20,0x20, 0x002e ,0x0005 ,0x0006],
  [0x1a,0x13,0x14,0x17,0x22,0x13,0x20,0x20,0x20,0x20, 0x002e ,0x0007 ,0x0006],
  [0x21,0x35,0x21,0x18,0x29,0x21,0x36,0x29,0x13,0x20, 0x002e ,0x0009 ,0x0004],
  [0x36,0x13,0x25,0x18,0x37,0x20,0x20,0x20,0x20,0x20, 0x0030 ,0x0004 ,0x0003],
  [0x38,0x21,0x22,0x22,0x20,0x20,0x20,0x20,0x20,0x20, 0x0030 ,0x0008 ,0x0006],
  [0x19,0x37,0x34,0x13,0x20,0x20,0x20,0x20,0x20,0x20, 0x0030 ,0x000c ,0x0007],
  [0x22,0x34,0x19,0x17,0x15,0x22,0x20,0x20,0x20,0x20, 0x0030 ,0x0011 ,0x0003],
  [0x19,0x15,0x26,0x13,0x14,0x20,0x20,0x20,0x20,0x20, 0x0030 ,0x0015 ,0x0007],
  [0x16,0x13,0x21,0x14,0x20,0x20,0x20,0x20,0x20,0x20, 0x0034 ,0x0005 ,0x0009],
  [0x37,0x13,0x12,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x0034 ,0x000a ,0x0005],
  [0x26,0x18,0x25,0x26,0x29,0x16,0x20,0x20,0x20,0x20, 0x0034 ,0x000f ,0x0004],
  [0x21,0x29,0x18,0x13,0x37,0x22,0x20,0x20,0x20,0x20, 0x0034 ,0x0014 ,0x0009],
  [0x14,0x13,0x22,0x17,0x29,0x15,0x20,0x20,0x20,0x20, 0x0035 ,0x0001 ,0x0005],
  [0x18,0x38,0x1a,0x13,0x14,0x18,0x21,0x29,0x20,0x20, 0x0035 ,0x0004 ,0x0003],
  [0x19,0x14,0x13,0x22,0x20,0x20,0x20,0x20,0x20,0x20, 0x0035 ,0x0007 ,0x0003],
  [0x15,0x26,0x13,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x0035 ,0x0009 ,0x0005],
  [0x12,0x18,0x37,0x23,0x19,0x12,0x20,0x20,0x20,0x20, 0x0039 ,0x0002 ,0x0004],
  [0x21,0x14,0x14,0x18,0x35,0x13,0x22,0x20,0x20,0x20, 0x0039 ,0x0003 ,0x0001],
  [0x17,0x1a,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x003b ,0x0001 ,0x0009],
  [0x37,0x19,0x36,0x29,0x13,0x20,0x20,0x20,0x20,0x20, 0x003b ,0x0003 ,0x0002],
  [0x36,0x17,0x18,0x29,0x23,0x18,0x37,0x25,0x20,0x20, 0x003b ,0x0005 ,0x0004],
  [0x21,0x22,0x15,0x13,0x14,0x19,0x18,0x23,0x20,0x20, 0x003c ,0x0001 ,0x0008],
  [0x34,0x19,0x37,0x15,0x21,0x18,0x37,0x22,0x20,0x20, 0x003c ,0x0003 ,0x0009],
  [0x23,0x14,0x21,0x25,0x20,0x20,0x20,0x20,0x20,0x20, 0x003c ,0x0006 ,0x0005],
  [0x34,0x17,0x14,0x14,0x13,0x37,0x15,0x20,0x20,0x20, 0x003c ,0x0009 ,0x0008],
  [0x35,0x18,0x14,0x17,0x22,0x20,0x20,0x20,0x20,0x20, 0x0048 ,0x0001 ,0x0003],
  [0x22,0x17,0x34,0x26,0x20,0x20,0x20,0x20,0x20,0x20, 0x0048 ,0x0004 ,0x0007],
  [0x22,0x1a,0x21,0x34,0x13,0x20,0x20,0x20,0x20,0x20, 0x0060 ,0x0004 ,0x0002],
  [0x38,0x19,0x14,0x13,0x20,0x20,0x20,0x20,0x20,0x20, 0x0060 ,0x0009 ,0x0008],
  [0x36,0x17,0x18,0x29,0x23,0x20,0x20,0x20,0x20,0x20, 0x0060 ,0x000b ,0x0002],
  [0x38,0x18,0x22,0x22,0x18,0x29,0x13,0x20,0x20,0x20, 0x0060 ,0x000e ,0x0004],
  [0x36,0x17,0x14,0x37,0x18,0x37,0x25,0x20,0x20,0x20, 0x0067 ,0x0001 ,0x0003],
  [0x21,0x37,0x23,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x0067 ,0x0004 ,0x0002],
  [0x1a,0x21,0x37,0x13,0x29,0x22,0x20,0x20,0x20,0x20, 0x0067 ,0x0008 ,0x0002],
  [0x25,0x21,0x29,0x21,0x33,0x16,0x20,0x20,0x20,0x20, 0x0068 ,0x0002 ,0x0006],
  [0x26,0x21,0x35,0x13,0x20,0x20,0x20,0x20,0x20,0x20, 0x0068 ,0x0003 ,0x0003],
  [0x15,0x19,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x0068 ,0x0005 ,0x0004],
  [0x22,0x1a,0x21,0x34,0x13,0x20,0x20,0x20,0x20,0x20, 0x0069 ,0x0003 ,0x0005],
  [0x1a,0x29,0x21,0x37,0x13,0x15,0x22,0x20,0x20,0x20, 0x0069 ,0x0005 ,0x0001],
  [0x15,0x26,0x14,0x13,0x21,0x15,0x20,0x20,0x20,0x20, 0x0069 ,0x0008 ,0x0005],
  [0x34,0x21,0x1a,0x13,0x29,0x29,0x21,0x20,0x20,0x20, 0x006a ,0x0002 ,0x0002],
  [0x15,0x26,0x21,0x15,0x20,0x20,0x20,0x20,0x20,0x20, 0x006a ,0x0005 ,0x0003],
  [0x29,0x18,0x25,0x26,0x15,0x20,0x20,0x20,0x20,0x20, 0x006a ,0x000a ,0x0004],
  [0x37,0x13,0x35,0x13,0x14,0x20,0x20,0x20,0x20,0x20, 0x006b ,0x0002 ,0x0008],
  [0x1a,0x21,0x14,0x21,0x23,0x13,0x20,0x20,0x20,0x20, 0x006b ,0x0003 ,0x0003],
  [0x16,0x19,0x17,0x14,0x20,0x20,0x20,0x20,0x20,0x20, 0x006b ,0x0005 ,0x0007],
  [0x36,0x21,0x15,0x15,0x13,0x14,0x18,0x13,0x22,0x20, 0x006f ,0x0002 ,0x0002],
  [0x36,0x13,0x22,0x15,0x20,0x20,0x20,0x20,0x20,0x20, 0x006f ,0x0003 ,0x0005],
  [0x34,0x21,0x14,0x14,0x16,0x20,0x20,0x20,0x20,0x20, 0x006f ,0x0005 ,0x0005],
  [0x26,0x13,0x21,0x14,0x15,0x20,0x20,0x20,0x20,0x20, 0x0070 ,0x0002 ,0x0004],
  [0x29,0x18,0x24,0x13,0x20,0x20,0x20,0x20,0x20,0x20, 0x0070 ,0x0005 ,0x0003],
  [0x34,0x19,0x37,0x22,0x13,0x18,0x29,0x22,0x20,0x20, 0x00b1 ,0x0001 ,0x0003],
  [0x35,0x19,0x15,0x14,0x13,0x20,0x20,0x20,0x20,0x20, 0x00b1 ,0x0002 ,0x0001],
  [0x36,0x19,0x17,0x15,0x19,0x37,0x20,0x20,0x20,0x20, 0x00b2 ,0x0004 ,0x0008],
  [0x15,0x19,0x17,0x34,0x26,0x13,0x20,0x20,0x20,0x20, 0x00b2 ,0x0005 ,0x0004],
  [0x17,0x15,0x18,0x29,0x18,0x22,0x13,0x14,0x20,0x20, 0x00b3 ,0x0001 ,0x0004],
  [0x22,0x17,0x14,0x1a,0x29,0x17,0x22,0x20,0x20,0x20, 0x00b3 ,0x0003 ,0x0004],
  [0x22,0x13,0x14,0x19,0x37,0x15,0x20,0x20,0x20,0x20, 0x00b3 ,0x0004 ,0x0003],
  [0x13,0x37,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x00b3 ,0x000c ,0x0003],
  [0x17,0x37,0x13,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x00b4 ,0x0004 ,0x0005],
  [0x1a,0x29,0x17,0x22,0x20,0x20,0x20,0x20,0x20,0x20, 0x00b4 ,0x0005 ,0x0005],
  [0x36,0x17,0x23,0x25,0x13,0x15,0x20,0x20,0x20,0x20, 0x00b4 ,0x0006 ,0x0004],
  [0x37,0x19,0x15,0x14,0x13,0x20,0x20,0x20,0x20,0x20, 0x00b4 ,0x000d ,0x0002],
  [0x34,0x13,0x15,0x15,0x13,0x20,0x20,0x20,0x20,0x20, 0x00b4 ,0x0013 ,0x0003],
  [0x23,0x14,0x19,0x18,0x15,0x13,0x20,0x20,0x20,0x20, 0x00b5 ,0x0003 ,0x0007],
  [0x35,0x19,0x17,0x22,0x20,0x20,0x20,0x20,0x20,0x20, 0x00b5 ,0x0006 ,0x0001],
  [0x34,0x17,0x36,0x13,0x20,0x20,0x20,0x20,0x20,0x20, 0x00b5 ,0x000a ,0x0005],
  [0x19,0x36,0x27,0x13,0x34,0x15,0x18,0x24,0x20,0x20, 0x00b6 ,0x0001 ,0x0002],
  [0x19,0x14,0x23,0x14,0x13,0x20,0x20,0x20,0x20,0x20, 0x00b6 ,0x0004 ,0x0004],
  [0x34,0x19,0x29,0x19,0x37,0x18,0x13,0x22,0x20,0x20, 0x00b6 ,0x0003 ,0x0006],
  [0x35,0x19,0x17,0x22,0x20,0x20,0x20,0x20,0x20,0x20, 0x00b7 ,0x0001 ,0x0004],
  [0x23,0x13,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x00b7 ,0x0003 ,0x0005],
  [0x35,0x19,0x15,0x14,0x13,0x20,0x20,0x20,0x20,0x20, 0x00b8 ,0x0001 ,0x0007],
  [0x22,0x13,0x34,0x15,0x18,0x19,0x37,0x20,0x20,0x20, 0x00b8 ,0x0003 ,0x0004],
  [0x22,0x19,0x37,0x15,0x20,0x20,0x20,0x20,0x20,0x20, 0x00b8 ,0x0009 ,0x0003],
  [0x34,0x19,0x17,0x29,0x13,0x17,0x14,0x22,0x20,0x20, 0x00b8 ,0x000a ,0x0002],
  [0x35,0x13,0x37,0x23,0x17,0x20,0x20,0x20,0x20,0x20, 0x00ba ,0x0001 ,0x0002],
  [0x15,0x14,0x19,0x1a,0x20,0x20,0x20,0x20,0x20,0x20, 0x00ba ,0x0003 ,0x0006],
  [0x34,0x26,0x18,0x24,0x24,0x14,0x13,0x20,0x20,0x20, 0x00ba ,0x0008 ,0x0001],
  [0x15,0x19,0x17,0x27,0x19,0x17,0x14,0x22,0x20,0x20, 0x00ba ,0x000c ,0x0006],
  [0x35,0x18,0x25,0x17,0x13,0x17,0x14,0x20,0x20,0x20, 0x00ba ,0x0016 ,0x0006],
  [0x13,0x29,0x29,0x13,0x20,0x20,0x20,0x20,0x20,0x20, 0x00ba ,0x001b ,0x0003],
  [0x23,0x13,0x22,0x22,0x17,0x22,0x20,0x20,0x20,0x20, 0x00bc ,0x0003 ,0x0001],
  [0x29,0x13,0x22,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x00bc ,0x0008 ,0x0003],
  [0x36,0x19,0x17,0x15,0x19,0x37,0x20,0x20,0x20,0x20, 0x00bd ,0x0004 ,0x0003],
  [0x1a,0x19,0x17,0x14,0x20,0x20,0x20,0x20,0x20,0x20, 0x00bd ,0x0006 ,0x0001],
  [0x1a,0x19,0x18,0x37,0x15,0x20,0x20,0x20,0x20,0x20, 0x00bd ,0x000a ,0x0006],
  [0x35,0x19,0x17,0x22,0x20,0x20,0x20,0x20,0x20,0x20, 0x00be ,0x0001 ,0x0005],
  [0x23,0x19,0x37,0x37,0x13,0x14,0x20,0x20,0x20,0x20, 0x00be ,0x0005 ,0x0002],
  [0x19,0x14,0x23,0x14,0x13,0x22,0x20,0x20,0x20,0x20, 0x00be ,0x0008 ,0x0005],
  [0x1a,0x17,0x18,0x22,0x20,0x20,0x20,0x20,0x20,0x20, 0x00bf ,0x0002 ,0x0002],
  [0x19,0x14,0x23,0x14,0x13,0x20,0x20,0x20,0x20,0x20, 0x00c0 ,0x0001 ,0x0002],
  [0x23,0x19,0x34,0x28,0x22,0x20,0x20,0x20,0x20,0x20, 0x00c0 ,0x0003 ,0x0001],
  [0x22,0x19,0x37,0x15,0x20,0x20,0x20,0x20,0x20,0x20, 0x00c0 ,0x0004 ,0x0004],
  [0x19,0x14,0x36,0x18,0x15,0x13,0x20,0x20,0x20,0x20, 0x00c0 ,0x0008 ,0x0007],
  [0x1a,0x13,0x17,0x35,0x13,0x37,0x15,0x20,0x20,0x20, 0x00c0 ,0x000a ,0x0002],
  [0x24,0x19,0x14,0x38,0x13,0x20,0x20,0x20,0x20,0x20, 0x00c3 ,0x0001 ,0x0003],
  [0x24,0x29,0x19,0x15,0x15,0x13,0x20,0x20,0x20,0x20, 0x00c3 ,0x0002 ,0x0003],
  [0x22,0x13,0x34,0x15,0x13,0x17,0x14,0x20,0x20,0x20, 0x00c4 ,0x0002 ,0x0006],
  [0x23,0x19,0x37,0x37,0x13,0x14,0x20,0x20,0x20,0x20, 0x00c4 ,0x0005 ,0x0003],
  [0x17,0x37,0x13,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x00c4 ,0x0006 ,0x0005],
  [0x35,0x19,0x17,0x22,0x20,0x20,0x20,0x20,0x20,0x20, 0x00c6 ,0x0001 ,0x0005],
  [0x22,0x19,0x37,0x15,0x20,0x20,0x20,0x20,0x20,0x20, 0x00c6 ,0x0003 ,0x0004],
  [0x13,0x33,0x13,0x38,0x1a,0x29,0x13,0x20,0x20,0x20, 0x00c6 ,0x0006 ,0x0004],
  [0x23,0x19,0x37,0x37,0x13,0x20,0x20,0x20,0x20,0x20, 0x00c6 ,0x0007 ,0x0002],
  [0x35,0x19,0x15,0x14,0x13,0x20,0x20,0x20,0x20,0x20, 0x00c7 ,0x0001 ,0x0003],
  [0x14,0x13,0x22,0x15,0x13,0x37,0x15,0x20,0x20,0x20, 0x00c7 ,0x0003 ,0x0004],
  [0x13,0x37,0x34,0x19,0x14,0x13,0x20,0x20,0x20,0x20, 0x00c7 ,0x0005 ,0x0007],
  [0x29,0x19,0x18,0x37,0x20,0x20,0x20,0x20,0x20,0x20, 0x00c7 ,0x0006 ,0x0003],
  [0x35,0x19,0x17,0x22,0x20,0x20,0x20,0x20,0x20,0x20, 0x00c9 ,0x0001 ,0x0001],
  [0x24,0x19,0x37,0x34,0x15,0x18,0x19,0x37,0x20,0x20, 0x00c9 ,0x0007 ,0x0004],
  [0x35,0x19,0x15,0x14,0x13,0x20,0x20,0x20,0x20,0x20, 0x00c9 ,0x000f ,0x0001],
  [0x36,0x29,0x13,0x17,0x20,0x20,0x20,0x20,0x20,0x20, 0x00ca ,0x0001 ,0x0007],
  [0x36,0x19,0x17,0x15,0x19,0x37,0x20,0x20,0x20,0x20, 0x00ca ,0x0002 ,0x000b],
  [0x34,0x13,0x15,0x15,0x13,0x20,0x20,0x20,0x20,0x20, 0x00ca ,0x0006 ,0x0009],
  [0x14,0x13,0x1a,0x19,0x14,0x15,0x22,0x20,0x20,0x20, 0x00cc ,0x0003 ,0x0001],
  [0x23,0x13,0x22,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x00cc ,0x0007 ,0x0003],
  [0x22,0x13,0x14,0x15,0x20,0x20,0x20,0x20,0x20,0x20, 0x00cc ,0x000c ,0x0009],
  [0x37,0x19,0x17,0x35,0x13,0x29,0x20,0x20,0x20,0x20, 0x00cc ,0x0015 ,0x0001],
  [0x1a,0x19,0x17,0x14,0x20,0x20,0x20,0x20,0x20,0x20, 0x00cc ,0x001a ,0x0002],
  [0x19,0x17,0x35,0x14,0x18,0x15,0x20,0x20,0x20,0x20, 0x00ce ,0x0002 ,0x0005],
  [0x34,0x29,0x18,0x13,0x37,0x15,0x20,0x20,0x20,0x20, 0x00ce ,0x000c ,0x0009],
  [0x18,0x37,0x15,0x13,0x14,0x35,0x18,0x37,0x15,0x20, 0x00ce ,0x000d ,0x0002],
  [0x35,0x19,0x15,0x14,0x13,0x20,0x20,0x20,0x20,0x20, 0x00cf ,0x0001 ,0x0004],
  [0x1a,0x14,0x13,0x37,0x37,0x13,0x37,0x15,0x20,0x20, 0x00cf ,0x0002 ,0x0005],
  [0x34,0x13,0x15,0x15,0x13,0x20,0x20,0x20,0x20,0x20, 0x00cf ,0x0003 ,0x0002],
  [0x15,0x14,0x19,0x17,0x35,0x13,0x20,0x20,0x20,0x20, 0x00d1 ,0x0001 ,0x0002],
  [0x17,0x15,0x18,0x29,0x18,0x22,0x13,0x37,0x15,0x20, 0x00d1 ,0x0002 ,0x0006],
  [0x22,0x17,0x14,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x00d1 ,0x0005 ,0x0003],
  [0x14,0x13,0x37,0x23,0x14,0x13,0x20,0x20,0x20,0x20, 0x00d2 ,0x0003 ,0x0001],
  [0x22,0x17,0x14,0x1a,0x29,0x17,0x22,0x20,0x20,0x20, 0x00d2 ,0x0003 ,0x0004],
  [0x34,0x13,0x15,0x15,0x13,0x20,0x20,0x20,0x20,0x20, 0x00d2 ,0x0005 ,0x0004],
  [0x35,0x19,0x17,0x22,0x20,0x20,0x20,0x20,0x20,0x20, 0x00d3 ,0x0001 ,0x0003],
  [0x29,0x18,0x22,0x15,0x13,0x20,0x20,0x20,0x20,0x20, 0x00d3 ,0x0002 ,0x0006],
  [0x14,0x18,0x13,0x37,0x20,0x20,0x20,0x20,0x20,0x20, 0x00d3 ,0x0004 ,0x0004],
  [0x35,0x13,0x14,0x22,0x20,0x20,0x20,0x20,0x20,0x20, 0x00d3 ,0x0010 ,0x0002],
  [0x1a,0x13,0x17,0x15,0x20,0x20,0x20,0x20,0x20,0x20, 0x00d8 ,0x0001 ,0x0006],
  [0x23,0x21,0x37,0x22,0x20,0x20,0x20,0x20,0x20,0x20, 0x00d8 ,0x0003 ,0x0002],
  [0x36,0x19,0x17,0x34,0x29,0x18,0x13,0x14,0x22,0x20, 0x00d8 ,0x0005 ,0x0003],
  [0x34,0x19,0x29,0x19,0x37,0x18,0x13,0x20,0x20,0x20, 0x00da ,0x0001 ,0x0004],
  [0x1a,0x29,0x17,0x22,0x20,0x20,0x20,0x20,0x20,0x20, 0x00da ,0x0002 ,0x0001],
  [0x34,0x19,0x37,0x15,0x14,0x13,0x20,0x20,0x20,0x20, 0x00dc ,0x0002 ,0x0005],
  [0x22,0x13,0x34,0x15,0x18,0x19,0x37,0x20,0x20,0x20, 0x00de ,0x0002 ,0x0001],
  [0x35,0x19,0x17,0x22,0x20,0x20,0x20,0x20,0x20,0x20, 0x00de ,0x0005 ,0x0003],
  [0x34,0x19,0x37,0x22,0x15,0x14,0x17,0x18,0x14,0x13, 0x00de ,0x0007 ,0x0002],
  [0x17,0x22,0x18,0x37,0x13,0x20,0x20,0x20,0x20,0x20, 0x00de ,0x0009 ,0x0002],
  [0x15,0x16,0x1a,0x13,0x20,0x20,0x20,0x20,0x20,0x20, 0x00df ,0x0001 ,0x0005],
  [0x22,0x17,0x18,0x35,0x18,0x22,0x20,0x20,0x20,0x20, 0x00df ,0x0002 ,0x0002],
  [0x17,0x37,0x13,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x00e0 ,0x0002 ,0x0003],
  [0x15,0x19,0x17,0x15,0x13,0x22,0x20,0x20,0x20,0x20, 0x00e0 ,0x0003 ,0x0003],
  [0x1a,0x13,0x17,0x35,0x13,0x37,0x15,0x20,0x20,0x20, 0x00e0 ,0x0005 ,0x0005],
  [0x12,0x18,0x14,0x23,0x20,0x20,0x20,0x20,0x20,0x20, 0x0079 ,0x0001 ,0x0003],
  [0x15,0x21,0x22,0x15,0x13,0x20,0x20,0x20,0x20,0x20, 0x0079 ,0x0002 ,0x0001],
  [0x37,0x18,0x34,0x26,0x15,0x20,0x20,0x20,0x20,0x20, 0x007a ,0x0004 ,0x000a],
  [0x36,0x13,0x24,0x18,0x37,0x23,0x13,0x15,0x20,0x20, 0x007a ,0x0007 ,0x0004],
  [0x23,0x13,0x37,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x007a ,0x000b ,0x0007],
  [0x17,0x37,0x15,0x13,0x37,0x20,0x20,0x20,0x20,0x20, 0x007a ,0x000e ,0x0001],
  [0x23,0x13,0x14,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x007a ,0x000f ,0x0001],
  [0x38,0x21,0x34,0x26,0x13,0x37,0x20,0x20,0x20,0x20, 0x007d ,0x0003 ,0x0007],
  [0x12,0x18,0x14,0x23,0x20,0x20,0x20,0x20,0x20,0x20, 0x007d ,0x0006 ,0x0002],
  [0x15,0x21,0x25,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x007e ,0x0002 ,0x0004],
  [0x35,0x19,0x14,0x14,0x21,0x15,0x20,0x20,0x20,0x20, 0x007e ,0x0004 ,0x0003],
  [0x34,0x1a,0x17,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x007e ,0x0008 ,0x0003],
  [0x17,0x37,0x23,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x007f ,0x0001 ,0x0004],
  [0x12,0x13,0x14,0x23,0x13,0x37,0x20,0x20,0x20,0x20, 0x007f ,0x0003 ,0x0002],
  [0x18,0x38,0x1a,0x13,0x14,0x18,0x21,0x29,0x13,0x20, 0x0081 ,0x0001 ,0x0001],
  [0x13,0x18,0x37,0x13,0x37,0x20,0x20,0x20,0x20,0x20, 0x0081 ,0x0004 ,0x0005],
  [0x28,0x14,0x13,0x18,0x22,0x15,0x20,0x20,0x20,0x20, 0x0081 ,0x0007 ,0x0004],
  [0x28,0x29,0x13,0x18,0x37,0x13,0x14,0x20,0x20,0x20, 0x0081 ,0x0011 ,0x0002],
  [0x23,0x13,0x22,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x0082 ,0x0001 ,0x0004],
  [0x22,0x34,0x26,0x18,0x24,0x24,0x13,0x20,0x20,0x20, 0x0083 ,0x0001 ,0x0003],
  [0x18,0x26,0x37,0x13,0x37,0x20,0x20,0x20,0x20,0x20, 0x0084 ,0x0002 ,0x0003],
  [0x23,0x14,0x13,0x18,0x20,0x20,0x20,0x20,0x20,0x20, 0x0084 ,0x0003 ,0x0003],
  [0x25,0x13,0x26,0x13,0x37,0x20,0x20,0x20,0x20,0x20, 0x0085 ,0x0001 ,0x0002],
  [0x14,0x13,0x1a,0x21,0x14,0x18,0x13,0x14,0x15,0x20, 0x0086 ,0x0003 ,0x0002],
  [0x21,0x37,0x25,0x14,0x18,0x24,0x24,0x20,0x20,0x20, 0x0086 ,0x0006 ,0x0002],
  [0x28,0x37,0x19,0x1a,0x24,0x20,0x20,0x20,0x20,0x20, 0x0086 ,0x0009 ,0x0001],
  [0x37,0x17,0x37,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x0087 ,0x0001 ,0x0003],
  [0x13,0x18,0x37,0x13,0x37,0x20,0x20,0x20,0x20,0x20, 0x0087 ,0x0005 ,0x0001],
  [0x12,0x17,0x14,0x23,0x13,0x20,0x20,0x20,0x20,0x20, 0x0087 ,0x000b ,0x0002],
  [0x26,0x21,0x37,0x25,0x21,0x14,0x22,0x20,0x20,0x20, 0x0088 ,0x0002 ,0x0005],
  [0x19,0x23,0x13,0x14,0x20,0x20,0x20,0x20,0x20,0x20, 0x0088 ,0x0004 ,0x0003],
  [0x22,0x34,0x26,0x18,0x24,0x24,0x13,0x20,0x20,0x20, 0x0088 ,0x0009 ,0x0002],
  [0x19,0x23,0x13,0x14,0x20,0x20,0x20,0x20,0x20,0x20, 0x0089 ,0x0001 ,0x0002],
  [0x23,0x13,0x38,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x008a ,0x0002 ,0x0008],
  [0x12,0x18,0x14,0x23,0x20,0x20,0x20,0x20,0x20,0x20, 0x008a ,0x000a ,0x0001],
  [0x13,0x18,0x37,0x13,0x37,0x20,0x20,0x20,0x20,0x20, 0x008a ,0x000b ,0x0001],
  [0x23,0x18,0x13,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x008a ,0x0010 ,0x0007],
  [0x35,0x13,0x14,0x24,0x19,0x29,0x25,0x13,0x37,0x20, 0x008b ,0x0002 ,0x0001],
  [0x23,0x21,0x37,0x37,0x20,0x20,0x20,0x20,0x20,0x20, 0x008b ,0x0005 ,0x0004],
  [0x12,0x18,0x14,0x23,0x20,0x20,0x20,0x20,0x20,0x20, 0x008b ,0x000b ,0x0004],
  [0x22,0x13,0x37,0x28,0x13,0x37,0x20,0x20,0x20,0x20, 0x008b ,0x0011 ,0x0001],
  [0x13,0x18,0x37,0x13,0x38,0x20,0x20,0x20,0x20,0x20, 0x008c ,0x0002 ,0x0003],
  [0x12,0x13,0x14,0x23,0x13,0x37,0x20,0x20,0x20,0x20, 0x008d ,0x0002 ,0x0002],
  [0x25,0x13,0x36,0x14,0x21,0x34,0x26,0x15,0x20,0x20, 0x008d ,0x0008 ,0x0009],
  [0x36,0x14,0x21,0x17,0x34,0x26,0x13,0x37,0x20,0x20, 0x008d ,0x000a ,0x0001],
  [0x23,0x21,0x14,0x21,0x17,0x24,0x26,0x18,0x37,0x20, 0x008e ,0x0003 ,0x0003],
  [0x22,0x18,0x13,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x008e ,0x0006 ,0x0002],
  [0x13,0x14,0x26,0x21,0x29,0x15,0x13,0x37,0x20,0x20, 0x008e ,0x000b ,0x0004],
  [0x13,0x18,0x37,0x38,0x21,0x29,0x20,0x20,0x20,0x20, 0x008e ,0x0012 ,0x0003],
  [0x22,0x21,0x15,0x13,0x29,0x29,0x18,0x15,0x20,0x20, 0x008f ,0x0001 ,0x0007],
  [0x34,0x26,0x21,0x37,0x34,0x13,0x20,0x20,0x20,0x20, 0x008f ,0x0002 ,0x0002],
  [0x21,0x22,0x15,0x13,0x14,0x19,0x18,0x23,0x13,0x37, 0x008f ,0x0005 ,0x0001],
  [0x21,0x37,0x23,0x13,0x14,0x13,0x20,0x20,0x20,0x20, 0x0091 ,0x0001 ,0x0001],
  [0x21,0x17,0x24,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x0092 ,0x0002 ,0x0003],
  [0x25,0x29,0x13,0x18,0x34,0x26,0x13,0x20,0x20,0x20, 0x0092 ,0x0004 ,0x0002],
  [0x21,0x37,0x28,0x29,0x18,0x34,0x28,0x13,0x37,0x20, 0x0092 ,0x0009 ,0x0001],
  [0x36,0x13,0x24,0x13,0x26,0x29,0x20,0x20,0x20,0x20, 0x0092 ,0x0012 ,0x0002],
  [0x23,0x14,0x18,0x37,0x25,0x13,0x37,0x23,0x20,0x20, 0x0093 ,0x0002 ,0x0001],
  [0x17,0x37,0x15,0x13,0x14,0x13,0x37,0x20,0x20,0x20, 0x0093 ,0x0004 ,0x0002],
  [0x12,0x19,0x29,0x29,0x13,0x37,0x20,0x20,0x20,0x20, 0x0094 ,0x0001 ,0x0003],
  [0x25,0x13,0x29,0x23,0x20,0x20,0x20,0x20,0x20,0x20, 0x0094 ,0x0004 ,0x0002],
  [0x36,0x13,0x25,0x18,0x37,0x37,0x20,0x20,0x20,0x20, 0x0094 ,0x000c ,0x0002],
  [0x37,0x21,0x26,0x14,0x17,0x37,0x25,0x20,0x20,0x20, 0x0094 ,0x000e ,0x000a],
  [0x36,0x13,0x25,0x18,0x37,0x37,0x13,0x37,0x20,0x20, 0x0095 ,0x0001 ,0x0001],
  [0x26,0x18,0x13,0x14,0x20,0x20,0x20,0x20,0x20,0x20, 0x0095 ,0x0003 ,0x0001],
  [0x21,0x29,0x18,0x13,0x37,0x22,0x20,0x20,0x20,0x20, 0x0095 ,0x0004 ,0x0001],
  [0x15,0x21,0x28,0x15,0x18,0x28,0x13,0x37,0x20,0x20, 0x0095 ,0x000a ,0x0008],
  [0x23,0x21,0x22,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x0096 ,0x0001 ,0x0001],
  [0x12,0x13,0x29,0x15,0x13,0x37,0x20,0x20,0x20,0x20, 0x0096 ,0x0008 ,0x0003],
  [0x22,0x13,0x18,0x37,0x13,0x38,0x20,0x20,0x20,0x20, 0x0096 ,0x000f ,0x0002],
  [0x29,0x19,0x34,0x26,0x20,0x20,0x20,0x20,0x20,0x20, 0x0096 ,0x0014 ,0x0003],
  [0x36,0x13,0x15,0x21,0x20,0x20,0x20,0x20,0x20,0x20, 0x0096 ,0x0017 ,0x0001],
  [0x28,0x13,0x18,0x37,0x13,0x14,0x20,0x20,0x20,0x20, 0x0097 ,0x0001 ,0x0002],
  [0x17,0x37,0x23,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x0097 ,0x0007 ,0x0002],
  [0x26,0x21,0x15,0x15,0x13,0x20,0x20,0x20,0x20,0x20, 0x0097 ,0x000b ,0x0007],
  [0x18,0x26,0x14,0x13,0x20,0x20,0x20,0x20,0x20,0x20, 0x0099 ,0x0002 ,0x0004],
  [0x22,0x34,0x26,0x18,0x24,0x24,0x13,0x20,0x20,0x20, 0x009b ,0x0001 ,0x0001],
  [0x22,0x15,0x13,0x26,0x15,0x20,0x20,0x20,0x20,0x20, 0x009b ,0x0002 ,0x0001],
  [0x21,0x37,0x29,0x21,0x25,0x13,0x20,0x20,0x20,0x20, 0x009d ,0x0001 ,0x0003],
  [0x22,0x18,0x37,0x23,0x20,0x20,0x20,0x20,0x20,0x20, 0x009d ,0x0003 ,0x0002],
  [0x36,0x18,0x29,0x23,0x13,0x15,0x20,0x20,0x20,0x20, 0x009e ,0x0002 ,0x0007],
  [0x35,0x18,0x13,0x14,0x13,0x34,0x28,0x20,0x20,0x20, 0x009e ,0x0004 ,0x0006],
  [0x22,0x18,0x37,0x23,0x20,0x20,0x20,0x20,0x20,0x20, 0x009f ,0x0002 ,0x0002],
  [0x17,0x37,0x23,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x00a1 ,0x0001 ,0x0002],
  [0x35,0x13,0x14,0x38,0x13,0x18,0x23,0x13,0x37,0x20, 0x00a1 ,0x0002 ,0x0003],
  [0x22,0x18,0x13,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x00a1 ,0x0003 ,0x0002],
  [0x37,0x13,0x17,0x13,0x20,0x20,0x20,0x20,0x20,0x20, 0x00a1 ,0x0005 ,0x0003],
  [0x12,0x18,0x14,0x23,0x20,0x20,0x20,0x20,0x20,0x20, 0x00a2 ,0x0001 ,0x0003],
  [0x12,0x13,0x18,0x15,0x13,0x14,0x13,0x20,0x20,0x20, 0x00a2 ,0x0004 ,0x0004],
  [0x23,0x18,0x13,0x22,0x13,0x22,0x20,0x20,0x20,0x20, 0x00a4 ,0x0001 ,0x0008],
  [0x24,0x18,0x37,0x23,0x13,0x37,0x20,0x20,0x20,0x20, 0x00a4 ,0x0001 ,0x000a],
  [0x21,0x29,0x29,0x13,0x14,0x20,0x20,0x20,0x20,0x20, 0x00a5 ,0x0001 ,0x0005],
  [0x12,0x13,0x37,0x37,0x20,0x20,0x20,0x20,0x20,0x20, 0x00a5 ,0x0003 ,0x0002],
  [0x36,0x21,0x17,0x20,0x20,0x20,0x20,0x20,0x20,0x20, 0x00a8 ,0x0001 ,0x0001],
  [0x22,0x13,0x26,0x14,0x20,0x20,0x20,0x20,0x20,0x20, 0x00aa ,0x0001 ,0x0002],
  [0x37,0x21,0x34,0x26,0x20,0x20,0x20,0x20,0x20,0x20, 0x00aa ,0x0002 ,0x0004],
  [0x37,0x18,0x34,0x26,0x15,0x20,0x20,0x20,0x20,0x20, 0x00aa ,0x0004 ,0x0006],
  [0x25,0x13,0x22,0x15,0x21,0x38,0x15,0x13,0x37,0x20, 0x00aa ,0x0006 ,0x000b],
  [0x28,0x19,0x29,0x19,0x37,0x18,0x13,0x20,0x20,0x20, 0x00aa ,0x0007 ,0x0001],
  [0x35,0x18,0x14,0x17,0x22,0x20,0x20,0x20,0x20,0x20, 0x00aa ,0x0008 ,0x0008],
]

amiga_scancodes = {
  0x45 : "ESCAPE",
  0x50 : "F1",
  0x51 : "F2",
  0x52 : "F3",
  0x53 : "F4",
  0x54 : "F5",
  0x55 : "F6",
  0x56 : "F7",
  0x57 : "F8",
  0x58 : "F9",
  0x59 : "F10",
  0x01 : "1",
  0x02 : "2",
  0x03 : "3",
  0x04 : "4",
  0x05 : "5",
  0x06 : "6",
  0x07 : "7",
  0x08 : "8",
  0x09 : "9",
  0x0A : "0",
  0x42 : "TAB",
  0x44 : "ENTER",
  0x41 : "BACKSPACE",
  0x40 : "SPACE",
  0x20 : "A",
  0x35 : "B",
  0x33 : "C",
  0x22 : "D",
  0x12 : "E",
  0x23 : "F",
  0x24 : "G",
  0x25 : "H",
  0x17 : "I",
  0x26 : "J",
  0x27 : "K",
  0x28 : "L",
  0x37 : "M",
  0x36 : "N",
  0x18 : "O",
  0x19 : "P",
  0x10 : "Q",
  0x13 : "R",
  0x21 : "S",
  0x14 : "T",
  0x16 : "U",
  0x34 : "V",
  0x11 : "W",
  0x32 : "X",
  0x15 : "Y",
  0x31 : "Z",
  0x0B : "MINUS",
  0x0C : "EQUALS",
  0x1A : "LEFTBRACKET",
  0x1B : "RIGHTBRACKET",
  0x0D : "BACKSLASH",
  0x29 : "SEMICOLON",
  0x2A : "SINGLEQUOTE",
  0x38 : "COMMA",
  0x39 : "PERIOD",
  0x3A : "SLASH",
  0x00 : "GRAVE",
  0x30 : "LTGT",
  0x1D : "NUMPAD_1",
  0x1E : "NUMPAD_2",
  0x1F : " ", #"NUMPAD_3"
  0x2D : "NUMPAD_4",
  0x2E : "NUMPAD_5",
  0x2F : "NUMPAD_6",
  0x3D : "NUMPAD_7",
  0x3E : "NUMPAD_8",
  0x3F : "NUMPAD_9",
  0x0F : "NUMPAD_0",
  0x5A : "NUMPAD_LPAREN",
  0x5B : "NUMPAD_RPAREN",
  0x5C : "NUMPAD_DIVIDE",
  0x5D : "NUMPAD_MULTIPLY",
  0x4A : "NUMPAD_MINUS",
  0x5E : "NUMPAD_PLUS",
  0x3C : "NUMPAD_PERIOD",
  0x43 : "NUMPAD_ENTER",
  0x47 : "INSERT",
  0x46 : "DELETE",
  0x5F : "HELP",
  0x4C : "CURSOR_UP",
  0x4D : "CURSOR_DOWN",
  0x4F : "CURSOR_LEFT",
  0x4E : "CURSOR_RIGHT",
  0x63 : "LEFT_CTRL",
  0x60 : "LEFT_SHIFT",
  0x64 : "LEFT_ALT",
  0x66 : "LEFT_SUPER",
  0x67 : "RIGHT_SUPER",
  0x65 : "RIGHT_ALT",
  0x61 : "RIGHT_SHIFT",
  0x62 : "CAPSLOCK",
  0x4B : "F11",
  0x6F : "F12",
  0x70 : "HOME",
  0x71 : "END",
  0x48 : "PAGEUP",
  0x49 : "PAGEDOWN",
  0x6E : "PAUSE",
  0xFF : "NUMLOCK",
  0xFF : "RIGHT_CTRL",
}

for row in codeTable:
  s = "".join(amiga_scancodes[x-1] for x in row[0:10])
  page = row[10]
  line = row[11]
  word = row[12]
  print (f"| {page:3} | {line:2} | {word:2} | {s:10} |")