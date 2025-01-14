
def __init__(self, type, operator=None, left=None, right=None, attribute=None, comparator=None, value=None):
        """
        Represents a node in the AST.

        :param type: String indicating the node type ("operator" or "operand").
        :param operator: String for logical operators ("AND" or "OR") if the node type is "operator".
        :param left: Reference to the left child Node (applicable for "operator" nodes).
        :param right: Reference to the right child Node (applicable for "operator" nodes).
        :param attribute: String representing the attribute name (e.g., "age", "department") for operand nodes.
        :param comparator: String representing the comparison operator (e.g., ">", "==") for operand nodes.
        :param value: The value to be compared against the attribute for operand nodes.
        """
        self.type = type
        self.operator = operator      # Only for "operator" nodes ("AND"/"OR")
        self.left = left              # Reference to the left child node (for operators)
        self.right = right            # Reference to the right child node (for operators)
        self.attribute = attribute    # Only for "operand" nodes (e.g., "age")
        self.comparator = comparator  # Comparison operator (e.g., ">", "<", "==")
        self.value = value            # The value for comparison (e.g., 30, "Sales")
