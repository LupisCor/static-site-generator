class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # string
        self.value = value # string
        self.childen = children # list
        self.props = props # dict
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        k = self.props.keys()
        output = ""
        for key in k:
            output = output + f' {key}="{self.props[key]}"'
        return output

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.childen}, {self.props})"