from _typeshed import SupportsNoArgReadline


class Cancion:
    def __init__(self, nombre, artista, album):
        self.nombre = nombre
        self.artista = artista
        self.album = album
        self.previous = None
        self.next = None

class Album:
    def __init__(self,name,artist,year,genre):
        self.name = name
        self.artist = artist
        self.year = year
        self.genre = genre
        self.previous = None
        self.next = None

class Artist:
    def __init__(self,name):
        self.name = name
        self.previous = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.nombre)
            node = node.next
        nodes.append("None")
        return " --> ".join(nodes)

    def insertar(self, cancion):
        if self.head is None:
            self.head = cancion
        else:
            for current_node in self:
                pass
            current_node.next = cancion
            cancion.previous = current_node
