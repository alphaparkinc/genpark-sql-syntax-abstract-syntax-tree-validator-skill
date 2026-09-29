from client import SQLSyntaxValidator

query = "SELECT user_id, email FROM users WHERE active = 1"
res = SQLSyntaxValidator.validate_select_query(query)
print("Query Validation:", res)
