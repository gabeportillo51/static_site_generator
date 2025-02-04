from htmlnode import *

class PARENTNODE(HTMLNODE):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("object has no tag")
        if self.children == None:
            raise ValueError("object has no children")
        contents = ""
        for child in self.children:
            contents += child.to_html()
        if self.props != None:
            return f"<{self.tag}>{self.props_to_html()}{contents}</{self.tag}>"
        else:
            return f"<{self.tag}>{contents}</{self.tag}>"
    
    def __eq__(self, other):
        if (self.tag == other.tag) and (self.children == other.children) and (self.props == other.props):
            return True
        else:
            return False
            

