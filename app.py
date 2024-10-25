from flask import Flask, render_template, request, jsonify
from rule_engine import create_rule, combine_rules, modify_rule, evaluate_rule
from database import init_db, get_db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_rule', methods=['POST'])
def create_rule_route():
    rule_name = request.form['rule_name']
    rule_string = request.form['rule']
    try:
        ast = create_rule(rule_string)
        # Save rule to database
        db = get_db()
        db.execute('INSERT INTO rules (name, rule_string) VALUES (?, ?)', (rule_name, rule_string))
        db.commit()
        return jsonify({'success': True, 'ast': str(ast)})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/combine_rules', methods=['POST'])
def combine_rules_route():
    rule1 = request.form['rule1']
    rule2 = request.form['rule2']
    operator = request.form['operator']
    try:
        combined_ast = combine_rules([rule1, rule2], operator)
        return jsonify({'success': True, 'ast': str(combined_ast)})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/modify_rule', methods=['POST'])
def modify_rule_route():
    rule_name = request.form['rule_name']
    modified_rule = request.form['modified_rule']
    try:
        db = get_db()
        existing_rule = db.execute('SELECT * FROM rules WHERE name = ?', (rule_name,)).fetchone()
        if not existing_rule:
            return jsonify({'success': False, 'error': 'Rule not found'})
        
        ast = modify_rule(modified_rule)
        db.execute('UPDATE rules SET rule_string = ? WHERE name = ?', (modified_rule, rule_name))
        db.commit()
        return jsonify({'success': True, 'ast': str(ast)})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_route():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        rule_name = data.get('rule_name')
        if not rule_name:
            return jsonify({"error": "Rule name is required"}), 400

        input_data = data.get('input_data', {})

        db = get_db()
        rule = db.execute('SELECT rule_string FROM rules WHERE name = ?', (rule_name,)).fetchone()

        if rule is None:
            return jsonify({"error": f"Rule '{rule_name}' not found"}), 404

        rule_string = rule['rule_string']
        result = evaluate_rule(rule_string, input_data)
        return jsonify({"result": result})

    except Exception as e:
        app.logger.error(f"Error in evaluate_rule_route: {str(e)}")
        return jsonify({"error": "An internal server error occurred"}), 500

@app.route('/get_rules')
def get_rules():
    db = get_db()
    rules = db.execute('SELECT name FROM rules').fetchall()
    return jsonify({'rules': [rule['name'] for rule in rules]})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)