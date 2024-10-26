
{
    "_id": "rule1",
    "name": "Rule 1",
    "description": "Eligibility rule for Sales and Marketing",
    "ast": {
        "type": "operator",
        "operator": "AND",
        "left": {
            "type": "operator",
            "operator": "OR",
            "left": {
                "type": "operator",
                "operator": "AND",
                "left": {
                    "type": "operand",
                    "attribute": "age",
                    "comparator": ">",
                    "value": 30
                },
                "right": {
                    "type": "operand",
                    "attribute": "department",
                    "comparator": "==",
                    "value": "Sales"
                }
            },
            "right": {
                "type": "operator",
                "operator": "AND",
                "left": {
                    "type": "operand",
                    "attribute": "age",
                    "comparator": "<",
                    "value": 25
                },
                "right": {
                    "type": "operand",
                    "attribute": "department",
                    "comparator": "==",
                    "value": "Marketing"
                }
            }
        },
        "right": {
            "type": "operator",
            "operator": "OR",
            "left": {
                "type": "operand",
                "attribute": "salary",
                "comparator": ">",
                "value": 50000
            },
            "right": {
                "type": "operand",
                "attribute": "experience",
                "comparator": ">",
                "value": 5
            }
        }
    }
}
