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

## First-Time Setup Instructions

### Quick Setup

```bash
# 1. Clone the repository
git clone https://github.com/escapepz/pz_translation_json_schema.git
cd pz_translation_json_schema

# 2. Install Python (3.9+ recommended)
# The verification script uses only standard library modules [1](#3-0)

# 3. Install Node.js (for prettier formatting)
# Download from https://nodejs.org or use version manager

# 4. (Optional) Install pre-commit for development
pip install pre-commit
```

### Verify Installation

Test the setup by running the verification script:

```bash
python .agent/skills/translation_schema_management/scripts/verify_translation_keys.py
```

This uses default paths:

- `--schema_dir schemas`
- `--media_dir media/lua/shared/Translate/EN`

### Optional Development Setup

For ongoing development, set up pre-commit hooks:

```bash
pre-commit install
```

### Project Structure

The project contains:

- `schemas/` - 30 JSON schema files
- `media/lua/shared/Translate/EN/` - 42 translation files
- `.agent/skills/translation_schema_management/` - verification scripts
- Documentation files (README.md, Categories.md, etc.)

### Notes

- No Python package manager files (requirements.txt, pyproject.toml) exist in the project
- The verification script handles non-standard JSON (trailing commas) automatically
- Prettier is used for consistent JSON formatting across schema files
