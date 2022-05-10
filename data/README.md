# Data

This directory contains various data from the game.

- `buildings-offsets.txt`: Building IDs.
- `gamestrings-english.txt`: Game strings extracted from english.mgl correctly
  by reading offsets from the file. A peculiarity in string 102: it contains two
  strings, "AREA EXP." and "--- NONE ---" separated by a null byte (denoted by
  a slash instead in this file here). If you display 102, you get "AREA EXP."
  and then the string ends because of the null byte. A separate function in the
  code specifically reads the second half by skipping to a 10-byte offset. This
  means the first part of string 102 has to be of identical length in all three
  languages. My guess is it was done to abbreviate Area Explosive so it would
  fit in the missile launch window.
- `gamestrings-french.txt`: Same, but French.
- `gamestrings-german.txt`: Same, but German.
- `gamestrings.v1.886.txt`: Old version of game strings extracted from memory, ignore this.
- `images_iff/`: Images in IFF ILBM format, extracted from .MGL files.
- `speech/`: Voice samples in raw format, extracted from .MGL files.
