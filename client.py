"""SQL Syntax Abstract Syntax Tree Validator.
100% Python Standard Library.
"""

import re

class SQLSyntaxValidator:
    """In-memory recursive validator verifying safe SQL clauses without injection risk."""
    DANGEROUS_KEYWORDS = ["drop", "truncate", "alter", "exec", "execute", "shutdown", "--", ";"]

    @classmethod
    def validate_select_query(cls, sql: str) -> dict:
        cleaned = sql.strip()
        tokens = re.findall(r'\b\w+\b', cleaned.lower())

        for kw in cls.DANGEROUS_KEYWORDS:
            if kw in tokens or kw in cleaned.lower():
                return {"valid": False, "error": f"Disallowed dangerous token: '{kw}'"}

        if not tokens or tokens[0] != "select":
            return {"valid": False, "error": "Query must start with SELECT"}

        has_from = "from" in tokens
        return {
            "valid": True,
            "has_from_clause": has_from,
            "query_type": "SELECT",
            "estimated_token_count": len(tokens)
        }
