# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        self.handler = handler
        self.children = {}
    
    def __repr__(self):
        return str(self.children)

# A RouteTrie stores our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)

     
    def insert(self, path_parts, handler):
        # Assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for part in path_parts:
            if part not in current_node.children:
                current_node.children[part] = RouteTrieNode(None)
            current_node = current_node.children[part]
        current_node.handler = handler
        

    def find(self, path_parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match 
        if len(path_parts) == 0:
            return self.root.handler
        current_node = self.root
        for part in path_parts:
            if part not in current_node.children:
                return 'not found handler' 
            current_node =  current_node = current_node.children[part]
        return current_node.handler


# The Router class wraps the RouteTrie class 
class Router:
    def __init__(self, handler):
        # Create a new RouteTrie for holding our routes
        self.route_trie = RouteTrie(handler)
        self.route_trie.root.handler = handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        pathes = self.split_path(path)
        self.route_trie.insert(pathes , handler)     

    def lookup(self,path):
       # lookup path (by parts) and return the associated handler
        path_parts = self.split_path(path)
        return  self.route_trie.find(path_parts)

    def split_path(self, path):
        if path == "/":
            return []
        path_parts = path.split('/')
        return path_parts

if __name__ == "__main__":
    
    # Test 
    router1 = Router("root handler") 
    router1.add_handler("/home/about", "about handler")  # add a route

    print("#"*60)
    print("Test")
    print(router1.lookup("/")) # should print 'root handler'
    print(router1.lookup("/home")) # should print 'not found handler' or None if you did not implement one
    print(router1.lookup("/home/about")) # should print 'about handler'
    print(router1.lookup("/home/about/")) # should print not found handler does not handle trailing slashes
    print(router1.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

