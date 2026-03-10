# Project Zomboid Translation JSON Schema

A comprehensive set of JSON Schemas for validating, writing, and assisting in the creation of translation files for Project Zomboid (and its mods). This collection covers all translation files found in Project Zomboid's `media/lua/shared/Translate/` directory.

## Features

- **Validation:** Ensures translation files have valid structures and prevents missing commas/braces, avoiding unexpected loading errors in-game.
- **Auto-completion & Tooltips:** Brings intelligence, descriptive pattern rules, and real-time error checking directly to IDEs.
- **Pattern Enforcement:** Automatically enforces correct translation key patterns and valid naming conventions across different types of JSON structures (e.g., `Base.{ItemCodeName}`, `UI_{context}_{keyname}`).

## Documentation

This project contains detailed documentation to help you understand and utilize the structure:

- 📖 **[How to Use](how_to_use.md)**: A complete guide covering IDE integration, command-line validation (using tools like `ajv` or Python), keys extraction, and various best practices.
- 🗂️ **[Categories](categories.md)**: Complete breakdown and categorization of Project Zomboid translation files. Details what each file handles and provides key pattern explanations.
- 🔍 **[Patterns Reference](patterns_reference.md)**: A concise quick-lookup table for all translation key prefixes.
- 📊 **[Key Patterns Report](key_patterns_report.md)**: An analytical mapping of key constraints for all translation files.

## Schema Architecture

The `schemas/` directory contains 30 distinct modular `.schema.json` definitions mapping to the 35 translation files (with some common schemas shared):

- `schemas/ItemName.schema.json`
- `schemas/UI.schema.json`
- `schemas/Recipes.schema.json`
- `...` and many more.

## Quick IDE Setup (VS Code)

To take full advantage of these JSON schemas in VS Code, configure your workspace mapping settings via `.vscode/settings.json`.

For instance, you can map specific translation files to their schemas:

```json
{
    "json.schemas": [
        {
            "fileMatch": ["**/Translate/*/ItemName.json"],
            "url": "./pz_translation_json_schema/schemas/ItemName.schema.json",
            "name": "PZ ItemName Schema"
        },
        {
            "fileMatch": ["**/Translate/*/UI.json"],
            "url": "./pz_translation_json_schema/schemas/UI.schema.json",
            "name": "PZ UI Schema"
        }
        // ... add the rest as needed
    ]
}
```

*For more details on integrating with JetBrains products or validating via the CLI, refer to the [How to Use](how_to_use.md) guide.*

## Formatting & Contributing

This project relies on `prettier` for JSON formatting. 
When making modifications or adding new descriptions to internal schemas, run the formatter to ensure consistency across files:

```bash
prettier --write "schemas/**/*.json"
```
