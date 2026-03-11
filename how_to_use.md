# How to Use the Translation JSON Schema

Complete guide for using the Project Zomboid translation JSON schema.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Validate Files](#validate-files)
3. [IDE Integration](#ide-integration)
4. [Extract Keys](#extract-keys)
5. [Create New Translations](#create-new-translations)
6. [Best Practices](#best-practices)
7. [Troubleshooting](#troubleshooting)
8. [Tools & Scripts](#tools--scripts)

---

## Quick Start

### What You Have

Three reference files:

- `schemas/` - JSON Schema definitions directory
- `categories.md` - File organization and key patterns
- `how_to_use.md` - This guide

### Basic Structure

All translation files follow this pattern:

```json
{
    "unique_key_1": "Translation text 1",
    "unique_key_2": "Translation text 2",
    "Base.ItemName": "Item Display Name"
}
```

---

## Validate Files

### Method 1: Online Validator (Easiest)

1. Go to: https://www.jsonschemavalidator.net/
2. Paste the appropriate schema into the left panel (from the `schemas/` directory)
3. Paste JSON file into right panel
4. Errors appear in real-time

### Method 2: Command Line (AJV)

**Install:**

```bash
npm install -g ajv-cli
```

**Validate single file:**

```bash
ajv validate -s schemas/ItemName.schema.json -d media/lua/shared/Translate/EN/ItemName.json
```

**Validate all files:**

```bash
for file in media/lua/shared/Translate/EN/*.json; do
  ajv validate -s schemas/$(basename "$file" .json).schema.json -d "$file"
done
```

### Method 3: Python (jsonschema)

**Install:**

```bash
pip install jsonschema
```

**Validate script:**

```python
import json
from jsonschema import validate, ValidationError

with open('schemas/ItemName.schema.json') as f:
    schema = json.load(f)

with open('media/lua/shared/Translate/EN/ItemName.json') as f:
    data = json.load(f)

try:
    validate(instance=data, schema=schema)
    print("✓ Valid")
except ValidationError as e:
    print(f"✗ Invalid: {e.message}")
```

---

## IDE Integration (VS Code)

### 1. Single File Validation
Add the `$schema` property directly to a JSON file for quick local validation.

File Path: `..\media\lua\shared\Translate\EN\ItemName.json`

```json
{
    "$schema": "https://raw.githubusercontent.com/escapepz/pz_translation_json_schema/42.15.0/schemas/ItemName.schema.json",
    "Base.Apple": "Apple",
    "Base.Hammer": "Hammer"
}
```
More schema? -> [schemas/](schemas/)

### 2. Project Based Validation
Configure VS Code to automatically apply schemas to all matching files in your project without modifying the source files. 

For instance, you can map specific translation files to their schemas.

Update your `.vscode/settings.json` (or create the file and `.vscode` folder if they don't exist):

```json
{
    "json.schemas": [
        {
            "fileMatch": ["**/Translate/*/ItemName.json"],
            "url": "https://raw.githubusercontent.com/escapepz/pz_translation_json_schema/42.15.0/schemas/ItemName.schema.json",
            "name": "PZ ItemName Schema"
        },
        {
            "fileMatch": ["**/Translate/*/UI.json"],
            "url": "https://raw.githubusercontent.com/escapepz/pz_translation_json_schema/42.15.0/schemas/UI.schema.json",
            "name": "PZ UI Schema"
        }
        // ... add the rest as needed
    ]
}
```

### Benefits

- Auto-completion for keys
- Real-time validation
- Hover tooltips showing key patterns
- Error highlighting


### Other IDEs

- **JetBrains (IntelliJ, WebStorm):** Settings → Languages → JSON Schema
- **Sublime Text:** Use JSON schema plugin
- **Vim/Neovim:** Use coc.nvim or mason LSP

---

## Extract Keys

### Get All Keys from All Files

**Bash:**

```bash
grep -h "^[[:space:]]*\"" media/lua/shared/Translate/EN/*.json | \
  sed 's/.*"\([^"]*\)".*/\1/' | \
  sort | uniq > all_keys.txt
```

### Get Keys by Category

**Items only:**

```bash
jq 'keys[]' media/lua/shared/Translate/EN/ItemName.json | grep "Base\." | sort > item_keys.txt
```

**UI only:**

```bash
jq 'keys[]' media/lua/shared/Translate/EN/UI.json | grep "UI_" | sort > ui_keys.txt
```

### Get Missing Keys

Compare keys between versions/languages:

```bash
comm -23 \
  <(jq -r 'keys[]' old_version/ItemName.json | sort) \
  <(jq -r 'keys[]' new_version/ItemName.json | sort) \
  > missing_keys.txt
```

### Find Duplicates

```bash
# Check for duplicate keys within a file
jq -r 'keys[]' media/lua/shared/Translate/EN/ItemName.json | sort | uniq -d
```

---

## Create New Translations

### Adding Keys to Existing File

**Step 1:** Open the appropriate JSON file

```
media/lua/shared/Translate/EN/ItemName.json
```

**Step 2:** Add new key following the pattern:

```json
{
    "Base.Apple": "Apple",
    "Base.MyNewItem": "My New Item Name" // New key
}
```

**Step 3:** Validate the file:

```bash
ajv validate -s schemas/ItemName.schema.json -d media/lua/shared/Translate/EN/ItemName.json
```

### Creating a New Category File

**Step 1:** Create new JSON file in correct location:

```
media/lua/shared/Translate/EN/MyNewCategory.json
```

**Step 2:** Follow the key format for your category:

**For items:**

```json
{
    "Base.CustomItem1": "Custom Item 1",
    "Base.CustomItem2": "Custom Item 2"
}
```

**For UI elements:**

```json
{
    "UI_custom_menu_option1": "Custom Option 1",
    "UI_custom_menu_option2": "Custom Option 2"
}
```

**For recipes:**

```json
{
    "MakeCustomRecipe": "Make Custom Item",
    "CraftCustomTool": "Craft Custom Tool"
}
```

**Step 3:** Validate against schema

### Key Naming Convention Checklist

- ✓ Keys are **unique** within the file
- ✓ Keys follow **category pattern** (see categories.md)
- ✓ Values are **non-empty strings**
- ✓ No **special characters** except `_` and `.`
- ✓ **PascalCase** for recipe names
- ✓ **snake_case** for UI elements
- ✓ **Base.** prefix for items
- ✓ **Attributes*Type*** prefix for attributes

---

## Best Practices

### 1. Key Naming

**DO:**

```json
{
    "Base.AssaultRifle": "M16 Assault Rifle",
    "UI_mainscreen_survival": "SURVIVAL",
    "MakeBiscuits": "Prepare Biscuits"
}
```

**DON'T:**

```json
{
    "assault rifle": "M16 Assault Rifle", // Missing Base. prefix
    "ui_main_screen_survival": "SURVIVAL", // Wrong case
    "make-biscuits": "Prepare Biscuits" // Wrong separator
}
```

### 2. Value Translation

**DO:**

```json
{
    "Base.Apple": "Apple",
    "UI_mainscreen_quit": "QUIT",
    "MakeBiscuits": "Prepare Biscuits"
}
```

**DON'T:**

```json
{
    "Base.Apple": "", // Empty value
    "UI_mainscreen_quit": null, // Null value
    "MakeBiscuits": "make_biscuits" // Key as value
}
```

### 3. Consistency

**DO:**

- Use same terminology across files
- Keep formatting consistent
- Maintain capitalization patterns

**DON'T:**

- Use "Gun" in one file and "Weapon" in another
- Mix PascalCase and snake_case
- Use random capitalization

### 4. File Organization

**DO:**

- Group related translations in appropriate file
- One category per file
- Keep file sizes manageable

**DON'T:**

- Mix items and UI in one file
- Create new file for single key
- Duplicate keys across files

### 5. Version Control

```bash
# Commit structure
git add media/lua/shared/Translate/EN/*.json
git commit -m "Add French translation for items"

# Keep schema in sync
git add schemas/
git commit -m "Update schemas for new key patterns"
```

---

## Troubleshooting

### Issue: "Invalid JSON"

**Solution:** Check for:

- Missing commas between key-value pairs
- Unescaped quotes in values
- Trailing commas

**Test:**

```bash
jq empty media/lua/shared/Translate/EN/ItemName.json
```

### Issue: "Key doesn't match pattern"

**Check against categories.md:**

- Items must start with `Base.`
- UI keys must start with `UI_`
- Recipes use PascalCase
- No dashes (use `_` instead)

**Test:**

```bash
# Check key format
jq -r 'keys[]' media/lua/shared/Translate/EN/ItemName.json | head
```

### Issue: "Duplicate keys"

**Find them:**

```bash
jq -r 'keys[]' media/lua/shared/Translate/EN/ItemName.json | \
  sort | uniq -c | awk '$1 > 1 {print $2}'
```

**Remove:**

- Open file in editor
- Search for duplicate key
- Delete one instance

### Issue: Schema not working in IDE

**Solutions:**

- Restart IDE
- Check `.vscode/settings.json` syntax
- Verify schema file path is correct
- Clear IDE cache

**Verify path:**

```bash
# On Windows
ls -la .vscode/settings.json
cat .vscode/settings.json
```

---

## Tools & Scripts

### 1. Validation Script (Node.js)

**File: `validate-translations.js`**

```javascript
const fs = require("fs");
const path = require("path");
const Ajv = require("ajv");

const ajv = new Ajv();
const dir = "media/lua/shared/Translate/EN";
const files = fs.readdirSync(dir).filter((f) => f.endsWith(".json"));

files.forEach((file) => {
    const schemaPath = path.join("schemas", file.replace(".json", ".schema.json"));
    const schema = JSON.parse(fs.readFileSync(schemaPath));
    const validate = ajv.compile(schema);

    const data = JSON.parse(fs.readFileSync(path.join(dir, file)));
    const valid = validate(data);

    if (!valid) {
        console.error(`✗ ${file}: ${JSON.stringify(validate.errors)}`);
    } else {
        console.log(`✓ ${file}`);
    }
});
```

**Run:**

```bash
npm install ajv
node validate-translations.js
```

### 2. Key Extraction Script (Python)

**File: `extract-keys.py`**

```python
import json
import os
import sys
from pathlib import Path

def extract_keys(directory):
    all_keys = {}

    for file in Path(directory).glob('*.json'):
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            all_keys[file.stem] = sorted(data.keys())

    # Save to file
    with open('all_translation_keys.json', 'w', encoding='utf-8') as f:
        json.dump(all_keys, f, indent=2)

    print(f"Extracted keys from {len(all_keys)} files")

if __name__ == '__main__':
    extract_keys('media/lua/shared/Translate/EN')
```

**Run:**

```bash
python extract-keys.py
```

### 3. Find Missing Keys Script

**File: `find-missing-keys.py`**

```python
import json
from pathlib import Path

def find_missing(original, updated):
    with open(original) as f:
        orig = set(json.load(f).keys())
    with open(updated) as f:
        upd = set(json.load(f).keys())

    missing = orig - upd
    new = upd - orig

    print(f"Missing: {len(missing)}")
    print(f"New: {len(new)}")

    if missing:
        print("\nMissing keys:")
        for key in sorted(missing):
            print(f"  - {key}")

find_missing('old_ItemName.json', 'new_ItemName.json')
```

### 4. Batch Validation (Bash)

**File: `validate-all.sh`**

```bash
#!/bin/bash

SCHEMA_DIR="schemas"
DIR="media/lua/shared/Translate/EN"
ERRORS=0

for file in $DIR/*.json; do
    schema_file="$SCHEMA_DIR/$(basename "$file" .json).schema.json"
    if ! ajv validate -s "$schema_file" -d "$file" > /dev/null 2>&1; then
        echo "✗ $(basename $file)"
        ((ERRORS++))
    else
        echo "✓ $(basename $file)"
    fi
done

if [ $ERRORS -eq 0 ]; then
    echo "All files valid!"
    exit 0
else
    echo "$ERRORS file(s) failed validation"
    exit 1
fi
```

**Run:**

```bash
chmod +x validate-all.sh
./validate-all.sh
```

---

## Quick Reference

| Task                 | Command                                                          |
| -------------------- | ---------------------------------------------------------------- |
| Validate single file | `ajv validate -s schemas/ItemName.schema.json -d ItemName.json`  |
| Extract all keys     | `jq -r 'keys[]' ItemName.json \| sort`                           |
| Find duplicates      | `jq -r 'keys[]' ItemName.json \| sort \| uniq -d`                |
| Count entries        | `jq 'length' ItemName.json`                                      |
| Compare files        | `diff <(jq -r 'keys[]' file1.json) <(jq -r 'keys[]' file2.json)` |
| Format file          | `jq . ItemName.json > ItemName_formatted.json`                   |
| Check syntax         | `jq empty ItemName.json`                                         |

---

## Next Steps

1. **Set up IDE** → Follow "IDE Integration" section
2. **Validate files** → Run validation on all translation files
3. **Extract keys** → Build key index for reference
4. **Create translations** → Add new keys following patterns
5. **Test regularly** → Validate files before commit

---

## Support Resources

- **JSON Schema Documentation:** https://json-schema.org/
- **AJV Validator:** https://ajv.js.org/
- **JQ Manual:** https://stedolan.github.io/jq/
- **Project Zomboid Forums:** https://www.projectzomboid.com/
