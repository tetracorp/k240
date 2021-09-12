# Images (IFF)

These are images in IFF ILBM format extracted from compressed MGL files which
appear on the disk. Thanks to <https://radishengine.github.io/denormalize/>
which was used to unpack MGL files.

Of particular note is outro3.iff, which is unused in the game perhaps due to
memory constraints.

For the images converted into png/gif format, see
[Extracted Images](https://tetracorp.github.io/k240/data/images.html).

## Files

* `hologram.iff`: Background to alien select screen.
* `lang.iff`: Language select screen.
* `outro1.iff`: Game win screen.
* `outro2.iff`: Game lose screen.
* `outro3.iff`: Game win screen for use when defeating the Swixarans. Actually
unused in the game, perhaps due to memory constraints. A screenshot in a preview
release in The One Amiga magazine shows satpic.iff used for the Swixaran win
screen instead as a stand-in. The final game just shows the regular game win
screen when defeating the Swixarans.
* `satpic.iff`: Intel screen background.
* `scitek.iff`: Sci-Tek blueprint pruchase screen background.
* `tetra.iff`: New game background screen.

The following files appear only in the CU Amiga K240 demo:

* `demo.iff`: Intro screen which only appears in the CU Amiga K240 demo.
* `demo2.iff`: Outro screen which only appears in the CU Amiga K240 demo.
* `scitek_demo.iff`: A slightly different version of scitek.mgl which in the CU
Amiga K240 demo. It's slightly brighter. The final release of the game darkens
it for improved readability.

For future reference, the method used to get raw data from the `denormalize`
tool was to upload the file, right-click the "Blob" in the inspector, store it
as a global variable (e.g. temp1) and add a download instruction like
`temp1.download ("hologram.mgl")`.


