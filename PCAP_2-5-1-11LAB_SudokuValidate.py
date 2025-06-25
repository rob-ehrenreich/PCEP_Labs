#PCAP 2.5.1.11 LAB Sudoku Validation

tdata1 = """295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672"""

tdata2 = """195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671"""

gridspaces = {
    "1":([0,3],[0,3]),
    "2":([0,3],[3,6]),
    "3":([0,3],[6,9]),
    "4":([3,6],[0,3]),
    "5":([3,6],[3,6]),
    "6":([3,6],[6,9]),
    "7":([6,9],[0,3]),
    "8":([6,9],[3,6]),
    "9":([6,9],[6,9])
}

def spltstring(string):
    global rows
    global lstable
    lstable=[]
    rows=string.split("\n")
    for i in range(9):
        lstable.append(list(rows[i]))
    return rows

def spltcol(rowmatrix):
    global cols
    cols=[]
    for p in range(9):
        colbuild=""
        for q in range(9):
            colbuild+=rowmatrix[q][p]
        cols.append(colbuild)
    return cols

def spltgrid(lstable):
    global grids
    grids =[]
    for a in range(0,9,3):
        for b in range(0,9,3):
            gridbuild=""
            for c in range(a, a+3):
                for d in range(b, b+3):
                    gridbuild+=lstable[c][d]
            grids.append(gridbuild)
    return grids
                    

valchk = (1,2,3,4,5,6,7,8,9)

def rowcheck(matxin):
    for i in range(9):
        currow = tuple(sorted(map(int, matxin[i])))
        if currow != valchk:
            return "No"
    return "Yes"


def colcheck(matxin):
    for i in range(9):
        curcol = tuple(sorted(map(int, matxin[i])))
        if curcol != valchk:
            return "No"
    return "Yes"    

def gridcheck(matxin):
    for g in range(9):
        curg = tuple(sorted(map(int, matxin[g])))
        if curg != valchk:
            return "No"
    return "Yes"

def checksudoku(testdata):
    rowmatx = spltstring(testdata)
    colmatx = spltcol(rowmatx)
    gridmatx = spltgrid(lstable)
    a=rowcheck(rowmatx)
    b=colcheck(colmatx)
    c=gridcheck(gridmatx)
    if a=="Yes" and b=="Yes" and c=="Yes":
        return "Yes"
    return "No"


print("Test Data 1:",checksudoku(tdata1))
print("Test Data 2:",checksudoku(tdata2))
