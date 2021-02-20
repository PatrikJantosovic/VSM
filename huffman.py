class node:
    def __init__(self, freq, char, children):
        self.freq = freq
        self.char = char
        self.children = children
        self.code = ''

def collect_code(node, huffman_code, result):
    huffman_code = huffman_code + str(node.code)
    for c in range(len(node.children)):
        collect_code(node.children[c],huffman_code, result)
    if len(node.children) < 1:
        pair = (node.char,huffman_code)
        result.append(pair)
        

def compute_huffman(chars, data):
    nodes = []
    empty_list = []
    for c in range(len(chars)):
        nodes.append(node(data[c], chars[c], empty_list))
    while len(nodes) > 1:
        nodes=sorted(nodes, key=lambda x: x.freq)
        child_0=nodes[0]
        child_1=nodes[1]
        child_0.code='0'
        child_1.code='1'
        children = []
        children.append(child_0)
        children.append(child_1)
        new_node=node(child_0.freq+child_1.freq,child_0.char+child_1.char,children)
        nodes.remove(child_0)
        nodes.remove(child_1)
        nodes.append(new_node)

    #ostal mi jeden node -> root a z neho traversujeme
    huffman_code = []
    collect_code(nodes[0], '', huffman_code)
    return huffman_code
    
