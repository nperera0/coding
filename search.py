#
# dictionary=['pin', 'pinner', 'present']
# query='pi'
# results=['pin', 'pinner']
#

class Node(object):
    def __init__(self, value, end):
        self.value = value
        self.end = end
        self.next = {}

class Dictionary(object):
    def __init__(self):
        self.head = Node(None, False)

    def addWord(self, word):

        if word is None or word == '':
            return

        cur = self.head
        for char in word:
            if char not in cur.next:
                newNode = Node(char, False)
                cur.next[char] = newNode

            cur = cur.next[char]

        cur.end = True

    def __searchHelper(self, word, cur, results):

        if cur.end == True:
            results.append(word)

        if cur.next.keys() == []:
            return

        for key, node in cur.next.items():
            self.__searchHelper(word + node.value, cur.next[key], results)

    def search(self, query):
        if query is None or query == '':
            return None

        cur = self.head

        word  = ''
        for char in query:
            if char in cur.next:
                word += char
                cur = cur.next[char]
            else:
                return []

        results  = []
        self.__searchHelper(word, cur, results)
        return results

    def __printHelper(self, cur):

        if cur.keys() == []:
            return

        for key, node in cur.items():
            print(node.value, node.end)
            self.__printHelper(cur[key].next)

    def printDictionary(self):
        cur = self.head.next
        self.__printHelper(cur)


d = Dictionary()
d.addWord('pin')
d.addWord('pinner')
d.addWord('present')
d.printDictionary()
result = d.search('pi') # ['pin', 'pinner']
print(result)
