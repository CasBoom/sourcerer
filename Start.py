class Start:
    def __init__(self):
        self.title = """   
..............._____..___...__.__..____......__....___..____.....___..____..................
............../.___/./...\\.|..|..||....\\..../..]../.._]|....\\.../.._]|....\\.................
.............(...\\_.|.....||..|..||..D..)../../../..[_.|..D..)./..[_.|..D..)................
..............\\__..||..O..||..|..||..../../../..|...._]|..../.|...._]|..../.................
............../..\\.||.....||..:..||....\\./...\\_.|...[_.|....\\.|...[_.|....\\.................
..............\\....||.....||.....||.....\\\\.....||.....||.....\\|.....||.....\\................
...............\\___|.\\___/..\\__,_||__|\\_|.\\____||_____||__|\\_||_____||__|\\_|................
............................................................................................"""
        self.image = """
............................................................................................
............................................VVVVVVVVVVVVVVV:................................
............................................FFFFFFVVVVVVVVV:................................
............................................IIFFFFFFVVVFV**.................................
...................................VVVVVVVVVVVVVVVVVVVVV....................................
...................................VVFFFFFFFFFFFVVVVVVVV....................................
...................................IIIIIIIIIIIIIIFFFVVVV....................................
...............................IIFVVVVVVVVVVVVVVVVIIIFVV....................................
...............................MMIVVVVVVFFVVVVVVVVIMMIFV....................................
...............................MMIVVFFFFFFFFFFFVVFMMMIFV....................................
...............................MMII*::::::*VMFFFFFMMMMIV....................................
...............................MM**:.......*VVFIIIMNNMIV....................................
...............................NM.............IMIMN$NNMI....................................
............................MMMII.......*MMIIIMMIIIMNMMFVVV.................................
............................MNV.:.....VVINNMMMMMMIIINNMMMFV.................................
...........................*NN*......:N$$NNNMMMMMMMMN$NMMII*::..............................
........................*VVVVI*::....*N$N$$NNNNNMMMNNNNMMIVV**..............................
.......................*VVV*VVVIM:::::::VMIFFVVVVVVVVVVVVVVV**:.............................
...........***:........*FFFVVVVFM*::::::*****VMVVV****FMFVVVV*..............................
..........:**:............*VVVFFMVVV*******V*VNIVVVVVVMMIFFVV:..............................
..........VV***::::::..........:::*********MIFVVVVVVVV:::::::..............*VVV**...........
..........VVVVVVVVVVV*:.............................................::::...:IFVVV...........
............VVVVVVVVVVV**********::::...............VVV*******::::::*MFVVVVVFFVVV...........
.............::**VVVVVVVVVVVVVV*VVVVVVVVVVVV********IMIFVVVVVVVVVVVVFMIFVVV*................
.....................VVVVVVVVVVVVVVVVV***VVVVV***VVVIMIFVVVVVVVVVVVVFMIFVVV:................
........................::**VVVVVVVVVVV*VVVVVVVVVVVVVVVVVVVVVVVVVVVV........................
.............................................:**VVV.........................................
............................................................................................"""

        
    def render(self):
        print(self.image+self.title)