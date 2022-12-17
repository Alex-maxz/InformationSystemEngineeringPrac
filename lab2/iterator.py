import numpy as np

class myTree:
    def __init__(self, data, hasmore):
        self.data = data
        self.hasmore = hasmore
        self.children = []

    def addchild(self, tree):
        self.children.append(tree)


def treegen():
    generator = np.random.default_rng()
    
    data = generator.integers(high= 100, low= 0)
    childNumber = generator.integers(low = 0, high = 3)

    localTree = myTree(data, childNumber)

    for i in range(childNumber):
        localTree.children.append(treegen())

    return localTree

def depthfirst(tree):
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

def widthfirst(tree):
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
        
        

class Iterator:

    def getDepth(tree):
        return depthIterator(tree)

    def getBreadth(tree):
        return breadthIterator(tree)

    '''
    def __init__(self, tree, type = "depth"):
        if type == "depth":
            self.func = depthIterator
        if type == "width":
            self.func = widthIterator

        self.getcount()

    def getcount(self, tree):
        parentarr = [tree]
        parentcount = [0]
        self.amount = 0

        if parentarr[-1].hasmore > parentcount[-1]:
            parentarr.append(parentarr[-1].children[parentcount[-1]])
            parentcount.append(0)
        else:
            #print(parentarr[-1].data)
            self.amount += 1
            parentarr.pop(-1)
            parentcount.pop(-1)
            if len(parentcount) == 0:
                return
            parentcount[-1] += 1
    '''


class depthIterator:

    def __init__(self, tree):
        self.parentarr = [tree]
        self.parentcount = [0]
        self.current_element_number = 0

    def count(self, tree):
        parentarr = [tree]
        parentcount = [0]
        self.amount = 0

        if parentarr[-1].hasmore > parentcount[-1]:
            parentarr.append(parentarr[-1].children[parentcount[-1]])
            parentcount.append(0)
        else:
            #print(parentarr[-1].data)
            self.amount += 1
            parentarr.pop(-1)
            parentcount.pop(-1)
            if len(parentcount) == 0:
                return
            parentcount[-1] += 1

    def getNext(self):

        if self.parentarr[-1].hasmore > self.parentcount[-1]:
            self.parentarr.append(self.parentarr[-1].children[self.parentcount[-1]])
            self.parentcount.append(0)
        else:
            self.current_element = self.parentarr[-1].data
            #print(self.parentarr[-1].data)
            self.parentarr.pop(-1)
            self.parentcount.pop(-1)
            if len(self.parentcount) == 0:
                return
            self.parentcount[-1] += 1
        self.current_element_number += 1
        return self.current_element

    def hasmore(self):
        if self.current_element_number < self.amount:
            return True
        else:
            return False

            

class breadthIterator:
    def __init__(self, tree):
        self.parentarr = [tree]
        self.parentcount = [0]
        self.layerarr = [tree]
        self.current_element_number = 0
        self.layeriterator = 0

    def count(self, tree):
        parentarr = [tree]
        parentcount = [0]
        self.amount = 0

        if parentarr[-1].hasmore > parentcount[-1]:
            parentarr.append(parentarr[-1].children[parentcount[-1]])
            parentcount.append(0)
        else:
            #print(parentarr[-1].data)
            self.amount += 1
            parentarr.pop(-1)
            parentcount.pop(-1)
            if len(parentcount) == 0:
                return
            parentcount[-1] += 1

    def getNext(self):
        if len(self.layerarr) > 0:
            nextlayerarr = []
            print(self.layerarr[self.layeriterator].data)
            self.layeriterator += 1
            if self.layeriterator == len(self.layerarr):
                for i in self.layerarr:
                    nextlayerarr += i.children
                self.layeriterator = 0
                self.layerarr = nextlayerarr
    

    def hasmore(self):
        if self.current_element_number < self.amount:
            return True
        else:
            return False





localtree = myTree(10, 0)
localtree2 = myTree(12, 1)
localtree3 = myTree(11, 0)
localtree1 = myTree(5, 2)


localtree2.addchild(localtree3)

localtree1.addchild(localtree2)
localtree1.addchild(localtree)


iterator = Iterator.getBreadth(localtree1)

iterator.getNext()
iterator.getNext()
iterator.getNext()




