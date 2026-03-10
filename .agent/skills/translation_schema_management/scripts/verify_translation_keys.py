import os
import json
import re
import argparse

# py .agent/skills/translation_schema_management/scripts/verify_translation_keys.py --schema_dir schemas --media_dir media/lua/shared/Translate/EN

def clean_json_content(content):
    """Remove trailing commas and handle BOM."""
    # Remove BOM if present
    if content.startswith('\ufeff'):
        content = content[1:]
    # Remove trailing commas
    content = re.sub(r',\s*([\]}])', r'\1', content)
    return content

def verify_schemas(schema_dir, media_dir):
    results = {}
    
    for schema_file in os.listdir(schema_dir):
        if not schema_file.endswith(".schema.json"):
            continue
        
        base_name = schema_file.replace(".schema.json", "")
        data_file = os.path.join(media_dir, base_name + ".json")
        if not os.path.exists(data_file):
            continue
            
        with open(os.path.join(schema_dir, schema_file), 'r', encoding='utf-8') as f:
            try:
                schema = json.load(f)
            except Exception as e:
                print(f"Error loading schema {schema_file}: {e}")
                continue
                
        pattern_props = schema.get("patternProperties", {})
        # Filter out the meta-keys like $
        patterns = [re.compile(p) for p in pattern_props.keys() if not p.startswith("^\\$")]
        
        with open(data_file, 'r', encoding='utf-8-sig') as f:
            try:
                content = clean_json_content(f.read())
                data = json.loads(content)
            except Exception as e:
                print(f"Error loading translation file {data_file}: {e}")
                continue
                
        mismatches = []
        for key in data.keys():
            if key.startswith("$"):
                continue
            if not any(p.match(key) for p in patterns):
                mismatches.append(key)
                
        if mismatches:
            results[base_name] = {
                "patterns": list(pattern_props.keys()),
                "mismatches": mismatches
            }
            
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify PZ Translation Schemas")
    parser.add_argument("--schema_dir", default="schemas", help="Directory containing .schema.json files")
    parser.add_argument("--media_dir", default="media/lua/shared/Translate/EN", help="Directory containing .json translation files")
    
    args = parser.parse_args()
    
    mismatches = verify_schemas(args.schema_dir, args.media_dir)
    
    if not mismatches:
        print("All schemas are up to date.")
    else:
        for file, info in mismatches.items():
            print(f"--- {file} ---")
            print(f"Current Patterns: {info['patterns']}")
            print(f"Mismatched Keys (total {len(info['mismatches'])}):")
            for m in sorted(info['mismatches'])[:10]:
                print(f"  {m}")
            if len(info['mismatches']) > 10:
                print("  ...")
