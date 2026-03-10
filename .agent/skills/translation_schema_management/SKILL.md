---
name: translation_schema_management
description: Manage and update Project Zomboid translation JSON schemas to stay in sync with source translation files.
---

# Translation Schema Management

This skill provides a workflow for keeping the JSON schemas in this repository synchronized with the actual keys used in Project Zomboid's translation files.

## Overview

Project Zomboid translation files (`media/lua/shared/Translate/EN/*.json`) use a variety of key patterns. As the game updates, new keys or non-standard characters (spaces, special symbols) may be introduced that break existing schema patterns.

## Skills & Capabilities

- **Verify Schemas**: Cross-reference schemas against actual translation keys.
- **Pattern Recognition**: Identify new regex patterns needed to cover mismatched keys.
- **Robust Parsing**: Handle PZ's non-standard JSON (e.g., trailing commas) without modifying the source files.

## Workflow

### 1. Verify Current State
Run the verification script to identify which schemas are out of sync.

```bash
py .agent/skills/translation_schema_management/scripts/verify_translation_keys.py --schema_dir schemas --media_dir media/lua/shared/Translate/EN
```

### 2. Analyze Mismatches
Examine the output. Focus on:
- Keys that contain unexpected characters (spaces, slashes, apostrophes).
- New naming conventions (e.g., `InfoBox` suffixes).
- Module-prefixed keys (e.g., `base:Item`).

### 3. Update Schemas
Modify the `patternProperties` in the relevant `.schema.json` file. 

**Pro-tip**: Use non-greedy or character-class inclusive regex.
- Good: `^[A-Za-z0-9_\\s:\\./'!-]+$` (covers most UI/IGUI keys)
- Good: `^[A-Za-z0-9_\\(\\): -]+$` (covers most Recipe keys)

### 4. Re-verify
Run the script again to ensure zero mismatches for the updated schema.

## Guidelines

1. **Do Not Modify Translation Files**: Never fix a schema by modifying the source JSON files in `media/`. The schemas must adapt to the game data, not vice versa.
2. **Inclusive, Not Exclusive**: Schemas should be broad enough to cover valid game keys but restrictive enough to prevent typos.
3. **Preserve Metadata**: Keep the `description` and `title` fields in the schemas accurate to reflect the updated patterns.
