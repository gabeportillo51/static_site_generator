from enum import Enum
from leafnode import *

class TextType(Enum):
	NORMAL = "normal"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode:
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type =  text_type
		self.url = url

	def __eq__(self, other):
		if (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url):
			return True
		else:
			return False
	
	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
	
	def text_node_to_html_node(self):
		if self.text_type.value == "normal":
			return LEAFNODE(None, self.text, self.url)
		if self.text_type.value == "bold":
			return LEAFNODE("b", self.text)
		if self.text_type.value == "italic":
			return LEAFNODE("i", self.text)
		if self.text_type.value == "code":
			return LEAFNODE("code", self.text)
		if self.text_type.value == "link":
			return LEAFNODE("a", self.text, {"href":self.url})
		if self.text_type.value == "image":
			return LEAFNODE("img", "", {"src":self.url, "alt":self.text})
		else:
			raise Exception("incorrect text type value")

