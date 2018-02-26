from pytrie import SortedStringTrie as Trie


class TranslationTrie(object):

    def createTrie(self, filePath):
        trie = Trie()
        # with open("/Users/nali/Downloads/final_dict.txt", 'r') as file:
        with open(filePath, 'r') as file:
            lines = file.readlines()
            flag = 0
            for line in lines:
                flag += 1
                parts = line.strip().split('\t')
                if (len(parts) > 1):
                    words = parts[1].split(';')
                    for word in words:
                        if (word != ''):
                            if (trie.get(word) == None):
                                trie[word] = set()
                                trie[word].add(parts[0])
                            else:
                                trie[word].add(parts[0])
        return trie



trie = TranslationTrie().createTrie("/Users/nali/Downloads/final_dict.txt")
print(trie.get("Education"))
print(trie.get("education"))
print(trie.longest_prefix_value("Education", default='None'))
print(trie.longest_prefix_value("education", default='None'))