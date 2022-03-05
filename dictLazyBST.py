"""
    Briscese Filippo Maria
    0228612

    Prova Pratica - Prima Prova in Itinere
    Problema 1 - Binary search tree con lazy deletion:
    "Un albero binario di ricerca con lazy deletion e' composto da nodi che possono essere segnati come eliminati"
    Implementare:   delete(key k) --> bool
                    insert(key k, value v)
                    search(chiave k)

    Python 2.7
"""

from trees.binaryTree import BinaryTree
from trees.binaryTree import BinaryNode
from dictBinaryTree import DictBinaryTree


class LazyNode(BinaryNode):
    """
        Estensione della classe BinaryNode
        Aggiunge un attributo
        Non aggiunge metodi

        Un nodo "pigro" poteva anche non essere implementato come nuovo tipo di dato
        a patto di un saggio uso dell'attributo "info" di BinaryNode.
        Ho preferito implementarlo per un uso piu' semplice di questo tipo di nodi
        nei metodi di DictLazyBST.
    """

    def __init__(self, info):
        BinaryNode.__init__(self, info)
        self.deleted = False  # cancellato? True, False

    def __str__(self):
        return str(self.info)


class DictLazyBST(DictBinaryTree):
    """
        Estensione della classe DictBinaryTree:
        Non aggiunge alcun attributo
        Estende e sostituisce alcuni metodi

        Albero Binario di Ricerca con Lazy Deletion (vedi riga 7)
    """

    def __init__(self):
        DictBinaryTree.__init__(self)

    def delete(self, k):
        """
        Cancella un nodo in maniera "pigra":
        il nodo infatti rimarra' fisicamente al suo posto,
        ma verra' segnato come "eliminato", "cancellato".
        In caso di nodi duplicati considera sempre e solo il nodo piu' vicino alla radice.
        :param k: key; chiave del nodo da "cancellare".
        :return: bool:
                True + side effects, se il nodo e' presente nell'albero e non e' stato "cancellato" precedentemente
                False, se il nodo non e' presente oppure e' presente ma e' gia' stato "cancellato"
        """
        node = DictBinaryTree.searchNode(self, k)  # cerco il nodo
        if node is not None:  # se il nodo esiste
            if not node.deleted:  # e non e' segnato come "cancellato"
                node.deleted = True  # lo segno
                node.info.append('deleted')  # per visualizzare nella stampa il suo status
                return True
        return False

    def minKeySon(self, root):
        """
        Versione "speculare" di maxKeySon() di DictBinaryTree:
        "Permette di ottenere il nodo con chiave piu' piccola,
        partendo dal nodo root. Il nodo con chiave
        piu' piccola e' quello che si trova piu' a sinistra possibile."
        """
        if root is None:
            return None
        curr = root
        while curr.leftSon is not None:
            curr = curr.leftSon
        return curr

    def insert(self, k, v):
        """
        Inserisce una nuova coppia (k,v) nell'albero binario.
        Se e' possibile inserire il nodo nella posizione di un nodo segnato come eliminato,
        sostituisce il vecchio con il nuovo.
        :param k: key
        :param v: value
        """
        # Usando come base insert() di DictBinaryTree, il codice aggiunto e' tra le righe 103 e 123"
        pair = [k, v]
        newt = BinaryTree(LazyNode(pair))
        if self.tree.root is None:  # se l'albero e' vuoto
            self.tree.root = newt.root
        else:
            curr = self.tree.root  # nodo da analizzare
            pred = None  # nodo precedentemente analizzato
            while curr is not None:
                pred = curr
                # --> ESTENSIONE METODO ORIGINALE ######################################################################
                if curr.deleted:        # se il nodo in esame e' segnato cancellato, controlla:
                    # se il nodo e' una foglia "cancellata": (IF necessario per risolvere un problema del prossimo IF)
                    if curr.rightSon is None and curr.leftSon is None:
                        # print '- sostituendo una foglia segnata come cancellata -'
                        curr.info = pair        # sostituiscila
                        curr.deleted = False        # rimuovi segnatura
                        return
                    # controlla se il nodo e' "cancellato" e ci sono le condizioni per sostituirlo.
                    maxLeftSon = self.maxKeySon(curr.leftSon)
                    minRightSon = self.minKeySon(curr.rightSon)
                    if (k <= self.key(minRightSon)) and (k >= self.key(maxLeftSon)):
                        # PROBLEMA: e se fosse una foglia?   k <= self.key(minRightSon) = None    sara' sempre False...
                        # e quindi se una foglia e' cancellata non verra' mai rimpiazzata se possibile,
                        # l'inserimento infatti avverra' come suo figlio. (risolto con IF precedente)

                        # print '- sostituendo un nodo segnato come cancellato -'
                        curr.info = pair        # sostituisci il nodo
                        curr.deleted = False        # segna che non e' piu' cancellato
                        return
                # --> FINE ESTENSIONE ##################################################################################
                if k <= self.key(curr):  # se non entro negli if precedenti e la chiave da inserire e' < dell'attuale
                    curr = curr.leftSon  # continua a sinistra
                else:  # se e' >
                    curr = curr.rightSon  # continua a destra
            if k <= self.key(pred):
                self.tree.insertAsLeftSubTree(pred, newt)
            else:
                self.tree.insertAsRightSubTree(pred, newt)

    def search(self, k):
        """
        Ritorna il nodo con chiave k se questo e' presente nell'albero e non e' segnato come 'eliminato'.
        Nota bene: se presenti duplicati considerera' sempre e solo quello piu' vicino alla radice!
        :param k: key
        """
        node = DictBinaryTree.searchNode(self, k)  # cerco il nodo
        if node is None:  # se non esiste
            return None
        if not node.deleted:  # se non e' segnato come cancellato
            return node
        return None  # se e' segnato come cancellato


if __name__ == "__main__":
    diz = DictLazyBST()

    print("insert(13,nodo0)")
    diz.insert(13, 'nodo0')
    diz.tree.stampa()
    print ''

    print("insert(7,nodo1)")
    diz.insert(7, 'nodo1')
    diz.tree.stampa()
    print ''

    print("insert(19,nodo2)")
    diz.insert(19, 'nodo2')
    diz.tree.stampa()
    print ''

    print("insert(4,nodo3)")
    diz.insert(4, 'nodo3')
    diz.tree.stampa()
    print ''

    print("insert(11, nodo4)")
    diz.insert(11, 'nodo4')
    diz.tree.stampa()
    print ''

    print("insert(10, nodo5)")
    diz.insert(10, 'nodo5')
    diz.tree.stampa()
    print ''

    print("insert(15, nodo6)")
    diz.insert(15, 'nodo6')
    diz.tree.stampa()
    print ''

    print("insert(14, nodo7)")
    diz.insert(14, 'nodo7')
    diz.tree.stampa()
    print ''

    print("insert(17, nodo8)")
    diz.insert(17, 'nodo8')
    diz.tree.stampa()
    print ''

    print("insert(23, nodo9)")
    diz.insert(23, 'nodo9')
    diz.tree.stampa()
    print ''

    print("insert(21, nodo10)")
    diz.insert(21, 'nodo10')
    diz.tree.stampa()
    print ''

    print("insert(26, nodo11)")
    diz.insert(26, 'nodo11')
    diz.tree.stampa()
    print ''

    print("insert(30, nodo12)")
    diz.insert(30, 'nodo12')
    diz.tree.stampa()
    print ''

    print("search(3) = " + str(diz.search(3)) + "\n")
    cerca0 = diz.search(19)
    print("search(19) = " + str(cerca0))      # qui cerca di stampare un elem. nodo, che non e' "stringabile"...
    # print('Il nodo che volevi stampare: ' + str(cerca0.info) + "\n")
    cerca1 = diz.search(4)
    print("search(4) = " + str(cerca1))
    # print('Il nodo che volevi stampare: ' + str(cerca1.info) + "\n")
    print("search(300) = " + str(diz.search(300)) + "\n")

    print("delete(19)")
    diz.delete(19)
    diz.tree.stampa()
    print ''

    print("search(19) = " + str(diz.search(19)))
    print ''

    print("insert(22, nodo13)")
    diz.insert(22, 'nodo13')
    diz.tree.stampa()
    print ''

    print("insert(18, nodo14)")
    diz.insert(18, 'nodo14')
    diz.tree.stampa()
    print ''

# le foglie sono ancora "rotte" se faccio insert e sono cancellate?

    print("delete(30)")
    diz.delete(30)
    diz.tree.stampa()
    print ''

    print("search(30) = " + str(diz.search(30)))
    print ''

    print("insert(32, nodo20)")
    diz.insert(32, 'nodo20')
    diz.tree.stampa()
    print ''
