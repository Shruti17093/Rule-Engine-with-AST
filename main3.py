def create_rule(rule_string):
    # Parse the rule string to construct the AST
    # This could involve tokenizing the string and converting it into an AST
    # For simplicity, we will mock this implementation
    
    # Example hardcoded AST creation for the rule string
    age_condition = Node(type="operand", attribute="age", comparator=">", value=30)
    department_condition = Node(type="operand", attribute="department", comparator="==", value="Sales")
    and_node = Node(type="operator", operator="AND", left=age_condition, right=department_condition)
    
    return and_node
