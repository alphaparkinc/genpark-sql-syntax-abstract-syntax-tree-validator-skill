# genpark-sql-syntax-abstract-syntax-tree-validator-skill

Read-only SQL grammar parser and AST injection guard preventing destructive SQL execution in database agents.

## Architecture

```mermaid
flowchart TD
    SQL[Raw Generated SQL] --> Tokenizer[Lexical Tokenizer]
    Tokenizer --> DDLFilter{Dangerous Keywords DROP/TRUNCATE?}
    DDLFilter -->|Found| Reject[Reject Query Execution]
    DDLFilter -->|Clean| Parser[Verify SELECT & FROM Structure]
    Parser --> Approved[Approved Safe Read Query]
```

## Features
- **Strict Read-Only Enforcement**: Blocks DROP, TRUNCATE, ALTER, EXEC.
- **Zero Dependencies**: 100% Python Standard Library.
