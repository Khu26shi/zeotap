class ASTNode:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # e.g., 'operator' or 'operand'
        self.left = left  # Left child for operators
        self.right = right  # Right child for operators
        self.value = value  # Value for operand (e.g., age > 30)

    def evaluate(self, data):
        if self.node_type == 'operand':
            return eval(self.value, {}, data)  # Simple evaluation logic
        elif self.node_type == 'operator':
            if self.value == 'AND':
                return self.left.evaluate(data) and self.right.evaluate(data)
            elif self.value == 'OR':
                return self.left.evaluate(data) or self.right.evaluate(data)
        return False


def create_rule(rule_string):
    if "AND" in rule_string:
        parts = rule_string.split("AND")
        left = ASTNode('operand', value=parts[0].strip())
        right = ASTNode('operand', value=parts[1].strip())
        return ASTNode('operator', left=left, right=right, value="AND")
    elif "OR" in rule_string:
        parts = rule_string.split("OR")
        left = ASTNode('operand', value=parts[0].strip())
        right = ASTNode('operand', value=parts[1].strip())
        return ASTNode('operator', left=left, right=right, value="OR")
    return None


def combine_rules(rules, operator='AND'):
    if not rules:
        return None
    combined_ast = rules[0]
    for rule in rules[1:]:
        combined_ast = ASTNode('operator', left=combined_ast, right=rule, value=operator)
    return combined_ast


def evaluate_rule(ast, data):
    return ast.evaluate(data)


# Test the rule engine
if __name__ == "__main__":
    # Example rules
    rule1_ast = create_rule("age > 30 AND department == 'Sales'")
    rule2_ast = create_rule("salary > 50000 OR experience > 5")

    # Combine rules
    combined_ast = combine_rules([rule1_ast, rule2_ast], operator='AND')

    # Test data
    test_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}

    # Evaluate rule against data
    result = evaluate_rule(combined_ast, test_data)
    print("Evaluation result:", result)  # Expected True
