## Schema Architecture

The `schemas/` directory contains 30 distinct modular `.schema.json` definitions mapping to the 35 translation files (with some common schemas shared):

- `schemas/ItemName.schema.json`
- `schemas/UI.schema.json`
- `schemas/Recipes.schema.json`
- `...` and many more.

## Documentation

This project contains detailed documentation to help you understand and utilize the structure:

- 📖 **[How to Use](How_To_Use.md)**: A complete guide covering IDE integration, command-line validation (using tools like `ajv` or Python), keys extraction, and various best practices.
- 🗂️ **[Categories](Categories.md)**: Complete breakdown and categorization of Project Zomboid translation files. Details what each file handles and provides key pattern explanations.
- 🔍 **[Patterns Reference](Patterns_Reference.md)**: A concise quick-lookup table for all translation key prefixes.
- 📊 **[Key Patterns Report](Key_Patterns_Report.md)**: An analytical mapping of key constraints for all translation files.

## Formatting & Contributing

This project relies on `prettier` for JSON formatting.
When making modifications or adding new descriptions to internal schemas, run the formatter to ensure consistency across files:

```bash
prettier --write "schemas/**/*.json"
```
