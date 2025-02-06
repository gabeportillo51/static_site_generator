from htmlnode import *
from leafnode import *

class PARENTNODE(HTMLNODE):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("This parent node has no tag!")
        if self.children is None:
            raise ValueError("This parent node has no children!")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()   
        if self.props != None:
            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}>{children_html}</{self.tag}>"
                

