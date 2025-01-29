class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return self.props

        props_html = ""
        for key, value in self.props.items():
            props_html += f"{key}=\"{value}\" "
        props_html = props_html.rstrip()
        return props_html

    def __repr__(self):
        node_info = f"HTMLNode(tag: {self.tag}, value: {
            self.value}, children: {self.children}, props: {
            self.props})"
        return node_info
