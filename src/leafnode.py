from htmlnode import *

class LEAFNODE(HTMLNODE):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("This leaf node has no value!")
        if self.tag == None:
            return self.value
        else:
            if self.props != None:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
                

        