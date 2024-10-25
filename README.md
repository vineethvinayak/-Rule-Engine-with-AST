# Rule Engine with AST

The Rule Engine with AST project is a web-based application that allows users to create, combine, modify, and evaluate rules using Abstract Syntax Trees (ASTs). It provides a flexible and powerful way to define and process complex logical rules.


# Features:

- Create Rules: Users can create new rules by providing a rule name and rule string
- Combine Rules: Users can combine two existing rules using logical operators (AND, OR).
- Modify Rules (BONUS): Users can modify existing rules by providing the rule name and the modified rule string.
- Evaluate Rules: Users can evaluate rules against input data to determine if the rule conditions are met.
- Rule Management (BONUS): The system maintains a list of created rules for easy access and evaluation.
- Error Handling (BONUS): - Each section includes error handling to display meaningful messages to the user if something goes wrong (e.g., invalid input, server errors). 



# Tech Stack:

**Client:** HTML5, CSS, JavaScript 

**Server:** Python v3.12, Flask 2.0.1, SQLite

# Directory Structure:
![Screenshot 2024-10-25 091753](https://github.com/user-attachments/assets/f267ab60-5733-4080-bc66-aa80dcb4b405)

# Installation:


- Clone the repository

```bash
  git clone https://github.com/vineethvinayak/Rule-Engine-with-AST.git
  cd Rule-Engine-with-AST
```
- Create and activate a Virtual Envirnoment

```bash
   python -m venv venv
   venv\Scripts\activate #On Linux, use `source venv/bin/activate`
```
- Install the required dependencies

```bash
   pip install -r requirements.txt
```
- Initialize the database

```bash
   python
>>> from database import init_db
>>> init_db()
>>> exit()
```
- Run the Flask Application

```bash
   python app.py
```
- Open a web browser and navigate to http://127.0.0.1:5000/ to use the application
    
# Rules and Input
## Rules:
### - General Conditions for Rule String Acceptance: 
i. The rule string must follow a specific syntax using supported Logical Operators   such as: AND, OR and Supported Comparison Symbols such as: Equal to: =, Greater than: >, Less than: <, Greater than or equal to: >= and Less than or equal to: <=.

ii.	Parentheses must be balanced.

iii. Variable names in the rule should be valid (e.g., alphanumeric, no spaces).

iv. Operators (AND, OR) should be used correctly.

v. Comparison operators (>, <, >=, <=, =) should be used with appropriate operands.

### - Rule Naming Convention:

i. Valid: Alphanumeric characters, underscores, no spaces (e.g., "age_check", "income_rule_2023")

ii. Invalid: Names with spaces or special characters (e.g., "age check", "income-rule")

iii. Each new rule created should have a unique name.

## Input(with examples):

#### - Create Rule: The Create Rule feature allows users to define new rules in the system.
Valid Input example:

rule name: rule88

rule string:((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)

#### - Combine Rules: - This feature allows users to combine two existing rules using logical operators
Valid Input example:

rule 1: ((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing'))

Operator: AND

rule 2: (salary > 50000 OR experience > 5)

#### - Evaluate Rule : - This feature allows users to test rules against specific input data.
Valid Input example:

rule name: rule88

JSON Data for true: {"age": 35, "department": "Sales", "salary": 60000, "experience": 3} 

JSON Data for false: {"age": 25, "department": "Sales", "salary": 60000, "experience": 3} 

#### - Modify Rule (BONUS): - This feature enables users to update existing rules.
Valid Input example:

rule name: rule88

rule string: ((age > 40 AND department = 'Sales') AND (salary > 50000 OR experience > 5)

# Security Considerations (BONUS):
  - Input validation to prevent injection attacks. 
  - Secure handling of user-provided data, especially in rule evaluation.

# Performance Considerations (BONUS): 
   - Efficient AST traversal for large or complex rules.

# Conclusion:
In conclusion, the Rule Engine with AST project has successfully achieved its goals by implementing a 
powerful and flexible system that combines rule engine capabilities with Abstract Syntax Tree (AST) parsing 
in a web-based application. The project provides an intuitive interface for creating, combining, modifying, 
and evaluating complex rules while leveraging modern web technologies like Flask and SQLAlchemy. The 
seamless integration of AST parsing enhances the efficiency and structure of rule representation, while 
dynamic rule evaluation against varied input data showcases its practical application. 

The project's robust backend logic is effectively complemented by a user-friendly frontend, offering a 
valuable tool for managing intricate rule-based scenarios. It stands as a solid foundation for future 
developments, whether through additional rule types, enhanced parsing, or broader integrations. Overall, 
the Rule Engine with AST project demonstrates a successful fusion of advanced programming techniques 
with real-world usability, addressing both technical challenges and user requirements in rule-based decision
making processes.


