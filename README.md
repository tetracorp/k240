# Exploring K240

_A Commodore Amiga game disassembly project_

This project analyzes a disassembled code of the 1994 Commodore Amiga game
_K240_ in order to understand how it functions. The project's findings are
primarily documented at the website here: https://tetracorp.github.io/k240/

This project also documents the history of the game's development and release,
and other related trivia.

## Files

`playk240.68k.asm` is a heavily annotated dissassembly of the main game
executable, in 68000 assembly language. `playk240.cnf` is a config file which
can be used with the disassembler program _IRA_ v2.09+ to generate this file
from a v2.000 executable only.

You can re-assemble this code with vasm like so:

    vasmm68k_mot -no-opt -Fhunkexe -nosym -o playk240 playk240.asm

You still require the other original game files to play. An authorized free
download of K240 can be found [here](http://gremlinworld.emuunlim.com/amiga.htm).

The other files are mainly decompressed data files, and tools which aren't
needed any more but were useful in analysis and are included here for
completeness.

The directory `src/` contains some earlier versions of the disassembly which
disassembled the v1.886 executable. These may not reassemble cleanly, though the
only significant version difference in v2.000 is the fleet bug fix.

Further information can be found at the [project website](https://tetracorp.github.io/k240/).

## Related links

- [Exploring the Dungeons of Avalon](https://tetracorp.github.io/dungeons-of-avalon/),
  a similar project analyzing the _Dungeons of Avalon_ RPG series.
- [Tetracorp homepage](https://tetracorp.github.io/)
