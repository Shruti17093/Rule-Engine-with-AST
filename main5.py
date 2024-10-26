def print_ast(node, level=0):
    indent = "  " * level
    if node.type == "operand":
        print(f"{indent}Operand: {node.attribute} {node.comparator} {node.value}")
    elif node.type == "operator":
        print(f"{indent}Operator: {node.operator}")
        if node.left:
            print_ast(node.left, level + 1)
        if node.right:
            print_ast(node.right, level + 1)

# Verifying the AST representation
print("Rule 1 AST:")
print_ast(rule1_ast)

print("\nRule 2 AST:")
print_ast(rule2_ast)


