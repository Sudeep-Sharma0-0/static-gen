from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.tag is None:
            return self.value
        if self.value is None:
            raise ValueError("All LeafNodes must have a value.")

        opening = f"<{self.tag}"
        if self.props is not None:
            attributes = f"{self.props_to_html()}"
            opening += f" {attributes}>"
        else:
            opening += ">"
        full_html = f"{opening}{self.value}</{self.tag}>"

        return full_html
