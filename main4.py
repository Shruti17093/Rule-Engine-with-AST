def evaluate_rule(ast, data):
    if ast.type == "operand":
        # Evaluate the condition based on the data
        attribute_value = data.get(ast.attribute)
        if ast.comparator == ">":
            return attribute_value > ast.value
        elif ast.comparator == "<":
            return attribute_value < ast.value
        elif ast.comparator == "==":
            return attribute_value == ast.value
        # Add other comparison operations as needed
    
    elif ast.type == "operator":
        left_result = evaluate_rule(ast.left, data)
        right_result = evaluate_rule(ast.right, data)
        if ast.operator == "AND":
            return left_result and right_result
        elif ast.operator == "OR":
            return left_result or right_result

    return False

