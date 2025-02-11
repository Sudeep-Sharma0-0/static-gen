from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, props=props, children=children)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent Node must have a tag!")
        if len(self.children) < 1:
            raise ValueError("Parent Node must have children!")

        opening = f"<{self.tag}"
        if self.props is not None:
            attributes = f"{self.props_to_html()}"
            opening += f" {attributes}>"
        else:
            opening += ">"

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        full_html = f"{opening}{children_html}</{self.tag}>"

        return full_html
