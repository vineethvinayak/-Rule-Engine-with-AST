from ast_node import Node
import re
import json

def create_rule(rule_string):
    return parse_rule(rule_string)

def combine_rules(rules, operator):
    if len(rules) < 2:
        raise ValueError("At least two rules are required for combination")
    
    combined_ast = parse_rule(rules[0])
    for rule in rules[1:]:
        right_ast = parse_rule(rule)
        combined_ast = Node("operator", operator, combined_ast, right_ast)
    
    return combined_ast

def modify_rule(rule_string):
    return parse_rule(rule_string)

def evaluate_rule(rule_string, data):
    ast = parse_rule(rule_string)
    return evaluate_ast(ast, data)

def parse_rule(rule_string):
    tokens = tokenize(rule_string)
    return parse_expression(tokens)

def tokenize(rule_string):
    return re.findall(r'\(|\)|\w+|>=|<=|>|<|=|AND|OR', rule_string)

def parse_expression(tokens):
    if len(tokens) == 0:
        return None
    
    if tokens[0] == '(':
        depth = 1
        for i, token in enumerate(tokens[1:], 1):
            if token == '(':
                depth += 1
            elif token == ')':
                depth -= 1
                if depth == 0:
                    left = parse_expression(tokens[1:i])
                    if i + 1 < len(tokens) and tokens[i+1] in ['AND', 'OR']:
                        operator = tokens[i+1]
                        right = parse_expression(tokens[i+2:])
                        return Node("operator", operator, left, right)
                    return left
    
    if len(tokens) >= 3 and tokens[1] in ['>', '<', '>=', '<=', '=']:
        return Node("operand", ' '.join(tokens[:3]))
    
    if len(tokens) >= 2 and tokens[0] in ['AND', 'OR']:
        operator = tokens[0]
        right = parse_expression(tokens[1:])
        return Node("operator", operator, None, right)
    
    raise ValueError(f"Invalid rule syntax: {' '.join(tokens)}")

def evaluate_ast(ast, data):
    if ast.type == "operator":
        if ast.value == "AND":
            return evaluate_ast(ast.left, data) and evaluate_ast(ast.right, data)
        elif ast.value == "OR":
            return evaluate_ast(ast.left, data) or evaluate_ast(ast.right, data)
    elif ast.type == "operand":
        attribute, operator, value = ast.value.split()
        if attribute not in data:
            return False
        
        data_value = data[attribute]
        if operator == '=':
            return str(data_value) == value
        elif operator == '>':
            return float(data_value) > float(value)
        elif operator == '<':
            return float(data_value) < float(value)
        elif operator == '>=':
            return float(data_value) >= float(value)
        elif operator == '<=':
            return float(data_value) <= float(value)
    
    return False