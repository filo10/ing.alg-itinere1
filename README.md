# ing.alg-itinere1
Algorithm engineering, midterm 1 project



### Problema  1  -  Binary  search  tree  con  lazy  deletion

Un  albero  binario  di  ricerca  con  lazy  deletion  è  composto  da  nodi  che
possono  essere  segnati  come  “eliminati”.  Siano  definite  le  seguenti
funzioni:

- **bool  delete(key  k)**:  Se  il  nodo  con  chiave  k  è  presente  nell’albero
    e  non  è  segnato  come  “eliminato”,  segna  il  nodo  come  eliminato  e
    ritorna  True.  Se  il  nodo  con  chiave  k  non  è  presente  nell’albero,  o
    è  presente  ma  è  stato  già  precedentemente  segnato  come
    eliminato,  ritorna  False.
- **insert(key  k,  value  v)**:  Inserisce  una  nuova  coppia  (k,v)  nell’albero
    binario.  Se  è  possibile  inserire  il  nodo  con  chiave  k  nella  posizione
    di  un  nodo  segnato  come  eliminato,  sostituisce  il  vecchio  nodo  con
    il  nuovo.
- **search(chiave  k)**:  Ritorna  il  nodo  con  chiave  k  se  questo  è
    presente  nell’albero  e  non  è  segnato  come  eliminato.

Basandosi  sul  codice  presentato  a  lezione  e  presente  sul  sito  del  corso,
implementare  un  dizionario  che  fa  uso  della  struttura  dati  sopra  descritta.

**Nota**:  Nella  relazione  si  discuta  in  quali  casi  è  preferibile  l’uso  della  lazy
deletion.
