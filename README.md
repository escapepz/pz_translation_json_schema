# Project Zomboid Translation JSON Schema

[![Version](https://img.shields.io/badge/version-1.0.2-blue.svg)](https://github.com/escapepz/pz_translation_json_schema)
[![Project Zomboid](https://img.shields.io/badge/Project%20Zomboid-42.16.0-orange.svg)](https://projectzomboid.com/)
[![zread](https://img.shields.io/badge/Ask_Zread-_.svg?style=flat&color=00b0aa&labelColor=000000&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTQuOTYxNTYgMS42MDAxSDIuMjQxNTZDMS44ODgxIDEuNjAwMSAxLjYwMTU2IDEuODg2NjQgMS42MDE1NiAyLjI0MDFWNC45NjAxQzEuNjAxNTYgNS4zMTM1NiAxLjg4ODEgNS42MDAxIDIuMjQxNTYgNS42MDAxSDQuOTYxNTZDNS4zMTUwMiA1LjYwMDEgNS42MDE1NiA1LjMxMzU2IDUuNjAxNTYgNC45NjAxVjIuMjQwMUM1LjYwMTU2IDEuODg2NjQgNS4zMTUwMiAxLjYwMDEgNC45NjE1NiAxLjYwMDFaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik00Ljk2MTU2IDEwLjM5OTlIMi4yNDE1NkMxLjg4ODEgMTAuMzk5OSAxLjYwMTU2IDEwLjY4NjQgMS42MDE1NiAxMS4wMzk5VjEzLjc1OTlDMS42MDE1NiAxNC4xMTM0IDEuODg4MSAxNC4zOTk5IDIuMjQxNTYgMTQuMzk5OUg0Ljk2MTU2QzUuMzE1MDIgMTQuMzk5OSA1LjYwMTU2IDE0LjExMzQgNS42MDE1NiAxMy43NTk5VjExLjAzOTlDNS42MDE1NiAxMC42ODY0IDUuMzE1MDIgMTAuMzk5OSA0Ljk2MTU2IDEwLjM5OTlaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik0xMy43NTg0IDEuNjAwMUgxMS4wMzg0QzEwLjY4NSAxLjYwMDEgMTAuMzk4NCAxLjg4NjY0IDEwLjM5ODQgMi4yNDAxVjQuOTYwMUMxMC4zOTg0IDUuMzEzNTYgMTAuNjg1IDUuNjAwMSAxMS4wMzg0IDUuNjAwMUgxMy43NTg0QzE0LjExMTkgNS42MDAxIDE0LjM5ODQgNS4zMTM1NiAxNC4zOTg0IDQuOTYwMVYyLjI0MDFDMTQuMzk4NCAxLjg4NjY0IDE0LjExMTkgMS42MDAxIDEzLjc1ODQgMS42MDAxWiIgZmlsbD0iI2ZmZiIvPgo8cGF0aCBkPSJNNCAxMkwxMiA0TDQgMTJaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik00IDEyTDEyIDQiIHN0cm9rZT0iI2ZmZiIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgo8L3N2Zz4K&logoColor=ffffff)](https://zread.ai/escapepz/pz_translation_json_schema)
[![DeepWiki](https://img.shields.io/badge/DeepWiki-_.svg?style=flat&color=6a0dad&labelColor=000000&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI%2BPHBhdGggZD0iTTEyIDJMMiA3bDEwIDUgMTAtNS0xMC01eiIvPjxwYXRoIGQ9Ik0yIDE3bDEwIDUgMTAtNXBNMiAxMmwxMCA1IDEwLTUiLz48L3N2Zz4%3D&logoColor=ffffff)](https://deepwiki.com/escapepz/pz_translation_json_schema)
[![Verify Translation Schemas](https://github.com/escapepz/pz_translation_json_schema/actions/workflows/verify-schemas.yml/badge.svg)](https://github.com/escapepz/pz_translation_json_schema/actions/workflows/verify-schemas.yml)

A comprehensive set of JSON Schemas for validating, writing, and assisting in the creation of translation files for Project Zomboid (and its mods). This collection covers all translation files found in Project Zomboid's `media/lua/shared/Translate/` directory.

~~📌 **Note:** This project provides the core schema definitions for [pz-translation-data](https://github.com/SirDoggyJvla/pz-translation-data). Updates here are manually integrated into the data repository to ensure standard compliance.~~ No, that guy is against using any AI to help with data. I don't want to waste time explaining it to strangers with a different mindset.

> [!NOTE]
> The `media/lua/shared/Translate/EN` directory contains data from the vanilla files of Project Zomboid. All rights reserved by **The Indie Stone**.

## Features

- **Validation:** Ensures translation files have valid structures and prevents missing commas/braces, avoiding unexpected loading errors in-game.
- **Auto-completion & Tooltips:** Brings intelligence, descriptive pattern rules, and real-time error checking directly to IDEs.
- **Pattern Enforcement:** Automatically enforces correct translation key patterns and valid naming conventions across different types of JSON structures (e.g., `Base.{ItemCodeName}`, `UI_{context}_{keyname}`).

## Quick IDE Setup (VS Code)

> 💡 **Tip:** If the schema fails to load, you may need to add GitHub to your **[Trusted Domains](.github/Troubleshooting_Trusted_Domains.md)**.

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

_For more details on integrating with JetBrains products or validating via the CLI, refer to the [How to Use](.github/How_To_Use.md) guide._

## Schema Architecture

The `schemas/` directory contains 30 distinct modular `.schema.json` definitions mapping to the 35 translation files (with some common schemas shared):

- `schemas/ItemName.schema.json`
- `schemas/UI.schema.json`
- `schemas/Recipes.schema.json`
- `...` and many more.

## Documentation

This project contains detailed documentation to help you understand and utilize the structure:

- 📖 **[How to Use](.github/How_To_Use.md)**: A complete guide covering IDE integration, command-line validation (using tools like `ajv` or Python), keys extraction, and various best practices.
- 🛠️ **[Trusted Domains](.github/Troubleshooting_Trusted_Domains.md)**: Troubleshooting guide for configuring `json.schemaDownload.trustedDomains` in VS Code.
- 🗂️ **[Categories](.github/Categories.md)**: Complete breakdown and categorization of Project Zomboid translation files. Details what each file handles and provides key pattern explanations.
- 🔍 **[Patterns Reference](.github/Patterns_Reference.md)**: A concise quick-lookup table for all translation key prefixes.
- 📊 **[Key Patterns Report](.github/Key_Patterns_Report.md)**: An analytical mapping of key constraints for all translation files.

## Formatting & Contributing

This project relies on `prettier` for JSON formatting.
When making modifications or adding new descriptions to internal schemas, run the formatter to ensure consistency across files:

```bash
npx prettier --write "schemas/**/*.json"
```
