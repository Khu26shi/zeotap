from flask import Flask, request, render_template, jsonify
from rule_engine import create_rule, combine_rules, evaluate_rule, ASTNode  # Import your rule engine

app = Flask(__name__)

# In-memory storage for rules
rules_store = []

@app.route('/')
def index():
    return render_template('index.html')  # Load the homepage with the form

@app.route('/create_rule', methods=['POST'])
def create_rule_route():
    rule_string = request.form.get('rule')
    try:
        # Create an AST from the rule string
        rule_ast = create_rule(rule_string)
        rules_store.append(rule_ast)  # Add to the list of stored rules
        return jsonify({"message": "Rule created successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/combine_rules', methods=['POST'])
def combine_rules_route():
    try:
        combined_ast = combine_rules(rules_store)  # Combine all stored rules
        return jsonify({"message": "Rules combined successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_route():
    try:
        # Get user input data from the form
        user_data = request.json
        combined_ast = combine_rules(rules_store)  # Use the combined rules AST
        result = evaluate_rule(combined_ast, user_data)
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
