class BST:
    def __init__(self, value):
        self.value = value;
    tempStorage = None
    lN = None
    rN = None

    def minVal(self):
        if self.lN is not None:
            return self.lN.minVal()
        else:
            return self.value

    def maxVal(self):
        if self.rN is not None:
            return self.rN.maxVal()
        else:
            return self.value

    def insert(self, value):
        if self.value == None:
            self.value = value
        else:
            if value < self.value:
                if self.lN == None:
                    self.lN = BST(value);
                else:
                    self.lN.insert(value)
            elif value > self.value:
                if self.rN == None:
                    self.rN = BST(value);
                else:
                    self.rN.insert(value)

    def printOutTree(self):
        self.tempStorage = str(str(self.value) + "   ")
        if(self.lN is not None):
            self.tempStorage += str(self.lN.printOutTree())
        if(self.rN is not None):
            self.tempStorage += str(self.rN.printOutTree())
        return str(self.tempStorage)

    def searchTree(self, value):
        if self.value == value:
            return value
        else:
            if self.lN is not None and self.value > value:
                temp = self.lN.searchTree(value)
                if temp == value:
                    return value
                else:
                        return None
            if self.rN is not None and self.value < value:
                temp = self.rN.searchTree(value)
                if temp == value:
                    return value
                else:
                    return None

    def deleteNode(self, value):
        print("checking node " + str(self.value))
        #Check Left Node
        ###########Checking With No Child Nodes##########
        if self.lN is not None and self.lN.isLastNode() and self.lN.value == value:
            print("Found the damn node: " + str(self.value))
            self.lN = None
            return True
        ###########Checking With 1 Child Node##########
        elif self.lN is not None and self.lN.hasOneNode() and self.lN.value == value:
            print("Found the damn node: " + str(self.value))
            self.tempStorage = self.lN
            self.lN = self.lN.lN
            self.tempStorage = None
            return True
        ##########Checking With 2 Child Nodes##########
        elif self.lN is not None and self.lN.hasTwoNodes() and self.lN.value == value:
            print("Found the damn node: " + str(self.value))
            self.lN.goDownAndDelete(self)

        #Checks Right Node
        ##########Checking With No Child Nodes##########
        if self.rN is not None and self.rN.isLastNode() and self.rN.value == value:
            print("Found the damn node: " + str(self.value))
            self.rN = None
            return True
        ##########Checking With 1 Child Node##########
        elif self.rN is not None and self.rN.hasOneNode() and self.rN.value == value:
            print("Found the damn node: " + str(self.value))
            self.tempStorage = self.rN
            self.rN = self.rN.rN
            self.tempStorage = None
            return True
        ##########Checking With 2 Child Nodes##########

        elif self.rN is not None and self.rN.hasTwoNodes() and self.rN.value == value:
            print("Found the damn node: " + str(self.rN.value))
            self.rN.goDownAndDelete(self.rN)







        ##########Call On Delete Function on children Nodes##########
        if self.lN is not None:
            if self.lN.deleteNode(value):
                return True
        if self.rN is not None:
            if self.rN.deleteNode(value):
                return True
        else:
            return False

    def goDownAndDelete(self, node):
        if self.lN.lN is None:
            print("Switching: " + str(self.lN.value) + "  For: " + str(node.value))
            node.value = self.lN.value
            self.lN = None
            return True
        elif self.lN.lN is not None:
            return self.lN.goDownAndDelete(node)
        else:
            return False

    def hasTwoNodes(self):
        if self.lN is not None and self.rN is not None:
            return True
        else:
            return False


    def hasOneNode(self):
        if self.lN is None and self.rN is not None:
            return True
        elif self.lN is not None and self.rN is None:
            return True
        else:
            return False

    def isLastNode(self):
        if self.lN is None and self.rN is None:
            return True
        else:
            return False

searchTree = BST(10)
searchTree.insert(5)
searchTree.insert(4)
searchTree.insert(2)
searchTree.insert(6)
# Higher Numbers
searchTree.insert(15)
searchTree.insert(13)
searchTree.insert(19)
searchTree.insert(21)
searchTree.insert(18)
print(searchTree.printOutTree())
searchTree.deleteNode(19)
print("--------------------")
print(searchTree.printOutTree())