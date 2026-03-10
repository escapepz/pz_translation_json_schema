# Translation File Categories

Complete categorization of Project Zomboid translation JSON files with actual key patterns for all 35 files.

## Overview

All translation files are located in: `media/lua/shared/Translate/EN/`

Total files: **35 JSON files**

---

## 1. Items (1 file)

**Purpose:** Game item names and descriptions

| File | Key Pattern | Example Keys |
|------|-------------|--------------|
| [ItemName.json](media/lua/shared/Translate/EN/ItemName.json) | `{ModuleName}.{ItemCodeName}` | `Base.Apple`, `Base.3030Box`, `CustomMod.MyItem` |

**Sample Keys:**
- Weapons: `Base.AssaultRifle`, `Base.Crowbar`
- Ammunition: `Base.9mmClip`, `Base.556Bullets`
- Food: `Base.Apple`, `Base.Bacon`
- Clothing: `Base.Apron_Black`, `Base.Corset`
- Tools: `Base.Hammer`, `Base.Wrench`
- Containers: `Base.Bag_Schoolbag`, `Base.Cooler`

**Size:** ~1000+ entries

---

## 2. Crafting (4 files)

**Purpose:** Recipe names, recipe groups, evolved recipes, and multi-stage building

| File | Key Pattern | Example Keys |
|------|-------------|--------------|
| [Recipes.json](media/lua/shared/Translate/EN/Recipes.json) | `{RecipeNameInPascalCase}` | `MakeBiscuits`, `AttachBreadKnifeToSpear`, `MakePizza` |
| [RecipeGroups.json](media/lua/shared/Translate/EN/RecipeGroups.json) | `RecipeGroup_{GroupName}` | `RecipeGroup_OpenBox`, `RecipeGroup_Cooking` |
| [EvolvedRecipeName.json](media/lua/shared/Translate/EN/EvolvedRecipeName.json) | `{ModuleName}.{ItemCodeName}` | `Base.CannedBologneseOpen`, `CustomMod.SpecialRecipe` |
| [MultiStageBuild.json](media/lua/shared/Translate/EN/MultiStageBuild.json) | `MultiStageBuild_{Type}_{Action}` | `MultiStageBuild_CreateWoodenWall_1` |

**Sample Keys from Recipes.json:**
- Cooking: `MakeBiscuits`, `MakePancake`, `MakePizza`
- Crafting: `MakeCrowbar`, `MakeAxe`, `MakeFishingRod`
- Disassembly: `DismantleCamera`, `DismantleTVRemote`
- Medical: `CleanBandage`, `DisinfectRag`
- Weapons: `MakePipebomb`, `MakeMolotovCocktail`

**Size:** ~1000+ entries

---

## 3. User Interface (4 files)

**Purpose:** In-game UI menu text, options, labels, tooltips, and context menu options

| File | Key Pattern | Example Keys |
|------|-------------|--------------|
| [UI.json](media/lua/shared/Translate/EN/UI.json) | `UI_{context}_{keyname}` | `UI_mainscreen_laststand`, `UI_optionscreen_fullscreen` |
| [IG_UI.json](media/lua/shared/Translate/EN/IG_UI.json) | `IGUI_{panel}_{property}` | `IGUI_invpanel_Type`, `IGUI_invpage_Loot_all` |
| [Tooltip.json](media/lua/shared/Translate/EN/Tooltip.json) | `Tooltip_{category}_{key}` | `Tooltip_food_Bowl`, `Tooltip_item_Weight` |
| [ContextMenu.json](media/lua/shared/Translate/EN/ContextMenu.json) | `ContextMenu_{ActionName}` | `ContextMenu_Destroy`, `ContextMenu_Sleep` |

**Sample Keys from UI.json:**
- Main Menu: `UI_mainscreen_survival`, `UI_mainscreen_sandbox`
- Options: `UI_optionscreen_fullscreen`, `UI_optionscreen_volume`
- Game Modes: `UI_soloscreen_sandbox`, `UI_coopscreen_title`
- Traits: `UI_trait_FastHealer`, `UI_trait_NightVision`
- Professions: `UI_prof_Carpenter`, `UI_prof_Doctor`

**Size:** ~1000+ entries

---

## 4. Game Mechanics (5 files)

**Purpose:** Core gameplay attributes, body parts, farming, fluids, and status effects

| File | Key Pattern | Example Keys |
|------|-------------|--------------|
| [Attributes.json](media/lua/shared/Translate/EN/Attributes.json) | `Attributes_Type_{AttributeName}` | `Attributes_Type_Quality`, `Attributes_Type_Durability` |
| [BodyParts.json](media/lua/shared/Translate/EN/BodyParts.json) | `BODYPART_{PARTNAME}` | `BODYPART_HEAD`, `BODYPART_LEFT_UPPER_ARM` |
| [Farming.json](media/lua/shared/Translate/EN/Farming.json) | `Farming_{CropName}` | `Farming_Carrots`, `Farming_Tomato` |
| [Fluids.json](media/lua/shared/Translate/EN/Fluids.json) | `Fluid_{ActionOrProperty}` | `Fluid_Transfer`, `Fluid_Capacity` |
| [Moodles.json](media/lua/shared/Translate/EN/Moodles.json) | `Moodles_{Type}_lvl{Level}` | `Moodles_Endurance_lvl1`, `Moodles_Stress_lvl4` |

**Sample Keys:**
- Attributes: `Attributes_Type_Quality`, `Attributes_Type_WoodType`, `Attributes_Type_MetalType`
- Body Parts: `BODYPART_HEAD`, `BODYPART_NECK`, `BODYPART_TORSO`, `BODYPART_LEFT_ARM`, `BODYPART_RIGHT_HAND`, `BODYPART_LEGS`, `BODYPART_FEET`
- Farming: `Farming_Corn`, `Farming_Wheat`, `Farming_Carrots`, `Farming_Cabbage`, `Farming_Potatoes`
- Fluids: `Fluid_Water`, `Fluid_Blood`, `Fluid_Gasoline`, `Fluid_Bleach`
- Moodles: `Moodles_Hungry_lvl1`, `Moodles_Tired_lvl2`, `Moodles_Panicked_lvl3`, `Moodles_Stressed_lvl4`, `Moodles_Sick_lvl1`

**Size:** Small (50-200 entries each)

---

## 5. Buildings & Locations (8 files)

### A. Building Elements (3 files)

| File | Key Pattern | Example Keys |
|------|-------------|--------------|
| [Moveables.json](media/lua/shared/Translate/EN/Moveables.json) | `{FurnitureNameSnakeCase}` | `50s_Barstool`, `Aaaaah!_Painting` |
| [MapLabel.json](media/lua/shared/Translate/EN/MapLabel.json) | `MapLabel_{LocationName}` | `MapLabel_Brandenburg`, `MapLabel_Riverside` |
| [Stash.json](media/lua/shared/Translate/EN/Stash.json) | `Stash_{LocationCode}_{ItemKey}` | `Stash_LVMap1_Text1`, `Stash_AnnotedMap` |

### B. Map Locations (5 files)

| File | Location | Key Pattern |
|------|----------|------------|
| [West Point, KY.json](media/lua/shared/Translate/EN/West%20Point,%20KY.json) | West Point | Generic (location-specific POI names) |
| [Rosewood, KY.json](media/lua/shared/Translate/EN/Rosewood,%20KY.json) | Rosewood | Generic (location-specific POI names) |
| [Riverside, KY.json](media/lua/shared/Translate/EN/Riverside,%20KY.json) | Riverside | Generic (location-specific POI names) |
| [Muldraugh, KY.json](media/lua/shared/Translate/EN/Muldraugh,%20KY.json) | Muldraugh | Generic (location-specific POI names) |
| [Echo Creek, KY.json](media/lua/shared/Translate/EN/Echo%20Creek,%20KY.json) | Echo Creek | Generic (location-specific POI names) |

**Purpose:** Location-specific POI names, building descriptions, and map labels

**Size:** ~100-500 entries per map

---

## 6. Media & Communication (6 files)

**Purpose:** Radio, TV, audio, and recorded media content

| File | Key Pattern | Example Keys |
|------|-------------|--------------|
| [RadioData.json](media/lua/shared/Translate/EN/RadioData.json) | `RD_{UUID}` | `RD_b0ee632b-789e-4e4f-a2b0-b09374856a62` |
| [DynamicRadio.json](media/lua/shared/Translate/EN/DynamicRadio.json) | `AEBS_{PropertyName}` or Generic | `AEBS_Intro`, `AEBS_temperature` |
| [GameSound.json](media/lua/shared/Translate/EN/GameSound.json) | `GameSound_{SoundName}` | `GameSound_AlarmClockRingingLoop`, `GameSound_BatHit` |
| [Recorded_Media.json](media/lua/shared/Translate/EN/Recorded_Media.json) | `RM_{PropertyName}` | `RM_broadcast`, `RM_recording` |
| [Print_Text.json](media/lua/shared/Translate/EN/Print_Text.json) | `Print_Text_{MediaName}_{property}` | `Print_Text_KnoxKnews_July1_title` |
| [Print_Media.json](media/lua/shared/Translate/EN/Print_Media.json) | `Print_Media_{MediaName}_{property}` | `Print_Media_KnoxKnews_July1_title` |

**Sample Content:**
- Radio broadcasts and announcements
- Music tracks and jingles
- Sound effect labels
- Book titles and content
- Magazine articles

**Size:** ~100-500 entries

---

## 7. Gameplay Features (4 files)

**Purpose:** Survival guide, survivor names, sandbox options, challenges

| File | Key Pattern | Example Keys |
|------|-------------|--------------|
| [SurvivalGuide.json](media/lua/shared/Translate/EN/SurvivalGuide.json) | `SurvivalGuide_entrie{num}{property}` | `SurvivalGuide_entrie1title`, `SurvivalGuide_entrie2txt` |
| [SurvivorNames.json](media/lua/shared/Translate/EN/SurvivorNames.json) | `SurvivorSurname_{LastName}` | `SurvivorSurname_Simpson`, `SurvivorSurname_Smith` |
| [Sandbox.json](media/lua/shared/Translate/EN/Sandbox.json) | `Sandbox_{OptionName}` | `Sandbox_PopulationOptions`, `Sandbox_ZombieCount` |
| [Challenge.json](media/lua/shared/Translate/EN/Challenge.json) | `Challenge_{ScenarioId}_{property}` | `Challenge_YouHaveOneDay_name`, `Challenge_Opening Hours_desc` |

**Size:** Variable (50-1000+ entries)

---

## 8. Miscellaneous (2 files)

| File | Key Pattern | Example Keys |
|------|-------------|--------------|
| [Entity.json](media/lua/shared/Translate/EN/Entity.json) | `EC_{PropertyName}` | `EC_Entity_DisplayName_Default`, `EC_Energy_Electric` |
| [MakeUp.json](media/lua/shared/Translate/EN/MakeUp.json) | `MakeUp(Category\|Type)_{Name}` | `MakeUpCategory_Eyes`, `MakeUpType_EyesFootball` |

---

## Key Format Summary

### Module Item Format
```
{ModuleName}.{ItemCodeName}
```
- Used in: `ItemName.json`, `EvolvedRecipeName.json`
- Examples: `Base.Apple`, `Base.Hammer`, `Base.3030Box`, `CustomMod.MyItem`
- Module names: Any registered module (Base, custom mods, etc.)

### Recipe Format
```
{RecipeNameInPascalCase}
```
- Used in: `Recipes.json`
- Examples: `MakeBiscuits`, `AttachBreadKnifeToSpear`, `DismantleCamera`

### UI Format
```
UI_{context}_{keyname}
```
- Used in: `UI.json`, `Tooltip.json`
- Examples: `UI_mainscreen_survival`, `UI_optionscreen_fullscreen`, `Tooltip_food_Bowl`

### In-Game UI Format
```
IGUI_{panel}_{property}
```
- Used in: `IG_UI.json`
- Examples: `IGUI_invpanel_Type`, `IGUI_invpage_Loot_all`

### Prefixed Format (Category Specific)
```
{PREFIX}_{RestOfKey}
```
- Used in: Most game mechanic and feature files
- Examples:
  - `MapLabel_Brandenburg` (MapLabel format)
  - `Stash_LVMap1_Text1` (Stash format)
  - `Farming_Carrots` (Farming format)
  - `ContextMenu_Destroy` (ContextMenu format)
  - `Challenge_YouHaveOneDay_name` (Challenge format)

### Generic Format
```
{KeyNameInCamelOrSnakeCase}
```
- Used in: Location files, some media files
- Flexible naming convention (varies by file content)

---

## File Statistics

| Category | Files | Total Entries |
|----------|-------|--------------|
| Items | 1 | 1000+ |
| Crafting | 4 | 1000+ |
| UI | 4 | 1000+ |
| Game Mechanics | 5 | 200-500 |
| Buildings & Locations | 8 | 500-2000 |
| Media | 6 | 300-1000 |
| Gameplay | 4 | 200-1000 |
| Miscellaneous | 2 | 100-500 |
| **TOTAL** | **35** | **5000+** |

---

## Complete File Mapping

### All 35 Files by Pattern Type

**Module Prefix (`{ModuleName}.`):**
- ItemName.json
- EvolvedRecipeName.json
(Any registered module, not just Base)

**UI Prefix (`UI_` or `IGUI_` or `Tooltip_`):**
- UI.json
- IG_UI.json
- Tooltip.json

**Map/Location Prefix:**
- MapLabel.json
- Stash.json
- West Point, KY.json
- Rosewood, KY.json
- Riverside, KY.json
- Muldraugh, KY.json
- Echo Creek, KY.json

**Prefixed Patterns (File-Specific):**
- ContextMenu.json (`ContextMenu_`)
- Attributes.json (`Attributes_Type_`)
- BodyParts.json (`BODYPART_`)
- Farming.json (`Farming_`)
- Fluids.json (`Fluid_`)
- Moodles.json (`Moodles_`)
- RecipeGroups.json (`RecipeGroup_`)
- MultiStageBuild.json (`MultiStageBuild_`)
- RadioData.json (`RD_`)
- DynamicRadio.json (`AEBS_` or generic)
- GameSound.json (`GameSound_`)
- Recorded_Media.json (`RM_`)
- Print_Media.json (`Print_Media_`)
- Print_Text.json (`Print_Text_`)
- SurvivalGuide.json (`SurvivalGuide_entrie`)
- SurvivorNames.json (`SurvivorSurname_`)
- Sandbox.json (`Sandbox_`)
- Challenge.json (`Challenge_`)
- Entity.json (`EC_`)
- MakeUp.json (`MakeUpCategory_` or `MakeUpType_`)

**PascalCase (No Prefix):**
- Recipes.json

**Flexible/Generic:**
- Moveables.json

---

## Common Translation Patterns

### Quantity-based Naming
```json
"Base.3030Box": "Box of .30-30 Rounds",
"Base.3030Bullets": ".30-30 Round",
"Base.3030Carton": "Carton of .30-30 Rounds"
```

### Variant Naming
```json
"Base.Apron_Black": "Apron",
"Base.Apron_Leather": "Leather Apron",
"Base.Apron_Hide": "Hide Apron"
```

### Quality Levels
```json
"BrickWall(Good)": "Brick Wall (Craftsman)",
"BrickWall(Poor)": "Brick Wall (Basic)",
"BrickWall": "Brick Wall (Craftsman)"
```

### State Variants
```json
"Base.ClayBowl": "Bowl",
"Base.ClayBowlUnfired": "Clay Bowl (Unfired)",
"Base.ClayBrickUnfired": "Clay Brick (Unfired)"
```

---

## Notes

- All keys must be unique within their file
- Values are human-readable English strings
- Some files contain 1000+ entries
- Keys follow consistent naming patterns by category
- Map location files contain location-specific content
- Location files (KY.json) use flexible generic patterns for POI names
- Total of 35 translation files covering all game systems
