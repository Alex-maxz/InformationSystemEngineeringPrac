class wideprint:
    def treeprint(tree):
        parentarr = [tree]
        parentcount = [0]
        layerarr = [tree]
        layercount = 0
        while len(layerarr) > 0:
            nextlayerarr = []
            for i in layerarr:
                print (i.data)
                nextlayerarr += i.children
            layerarr = nextlayerarr

class depthprint:
    def treeprint(tree):
        parentarr = [tree]
        parentcount = [0]

        while len(parentarr) > 0:
            if parentarr[-1].hasmore > parentcount[-1]:
                parentarr.append(parentarr[-1].children[parentcount[-1]])
                parentcount.append(0)
            else:
                print(parentarr[-1].data)
                parentarr.pop(-1)
                parentcount.pop(-1)
                if len(parentcount) == 0:
                    return
                parentcount[-1] += 1

class myTree:
    def __init__(self, data, hasmore):
        self.data = data
        self.hasmore = hasmore
        self.children = []

    def addchild(self, tree):
        self.children.append(tree)

    def addprint(self, printerclass):
        self.treeprinter = printerclass

    def printer(self):
        return self.treeprinter.treeprint(self)

localtree = myTree(10, 0)
localtree2 = myTree(12, 1)
localtree3 = myTree(11, 0)
localtree1 = myTree(5, 2)


localtree2.addchild(localtree3)

localtree1.addchild(localtree2)
localtree1.addchild(localtree)

localtree1.addprint(depthprint)

localtree1.printer()
