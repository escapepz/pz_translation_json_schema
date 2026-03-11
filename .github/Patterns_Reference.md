# Project Zomboid Translation JSON Patterns Reference

Complete consolidated reference for all 35 translation JSON files with exact key patterns.

---

## Quick Lookup by Prefix

| Prefix                            | File(s)                               | Pattern                                | Example                              |
| --------------------------------- | ------------------------------------- | -------------------------------------- | ------------------------------------ |
| `AEBS_`                           | DynamicRadio.json                     | `AEBS_[A-Za-z]+`                       | `AEBS_Intro`                         |
| `Attributes_Type_`                | Attributes.json                       | `Attributes_Type_[A-Za-z_]+`           | `Attributes_Type_Quality`            |
| `Base.`                           | ItemName.json, EvolvedRecipeName.json | `Base.[A-Za-z0-9_]+`                   | `Base.Apple`                         |
| `BODYPART_`                       | BodyParts.json                        | `BODYPART_[A-Z_]+`                     | `BODYPART_HEAD`                      |
| `Challenge_`                      | Challenge.json                        | `Challenge_[A-Za-z0-9\s]+_[a-z]+`      | `Challenge_YouHaveOneDay_name`       |
| `ContextMenu_`                    | ContextMenu.json                      | `ContextMenu_[A-Za-z]+`                | `ContextMenu_Destroy`                |
| `EC_`                             | Entity.json                           | `EC_[A-Za-z_]+`                        | `EC_Entity_DisplayName_Default`      |
| `Farming_`                        | Farming.json                          | `Farming_[A-Za-z]+`                    | `Farming_Carrots`                    |
| `Fluid_`                          | Fluids.json                           | `Fluid_[A-Za-z]+`                      | `Fluid_Transfer`                     |
| `GameSound_`                      | GameSound.json                        | `GameSound_[A-Za-z]+`                  | `GameSound_AlarmClockRingingLoop`    |
| `IGUI_`                           | IG_UI.json                            | `IGUI_[a-z_]+`                         | `IGUI_invpanel_Type`                 |
| `MakeUpCategory_` / `MakeUpType_` | MakeUp.json                           | `MakeUp(Category\|Type)_[A-Za-z]+`     | `MakeUpCategory_Eyes`                |
| `MapLabel_`                       | MapLabel.json                         | `MapLabel_[A-Za-z]+`                   | `MapLabel_Brandenburg`               |
| `Moodles_`                        | Moodles.json                          | `Moodles_[A-Za-z]+_lvl[0-9]+`          | `Moodles_Stress_lvl1`                |
| `MultiStageBuild_`                | MultiStageBuild.json                  | `MultiStageBuild_[A-Za-z0-9_]+_[0-9]+` | `MultiStageBuild_CreateWoodenWall_1` |
| `Print_Media_`                    | Print_Media.json                      | `Print_Media_[A-Za-z0-9_]+`            | `Print_Media_KnoxKnews_July1_title`  |
| `Print_Text_`                     | Print_Text.json                       | `Print_Text_[A-Za-z0-9_]+`             | `Print_Text_KnoxKnews_July1_title`   |
| `RD_`                             | RadioData.json                        | `RD_[a-f0-9-]+`                        | `RD_b0ee632b...`                     |
| `RecipeGroup_`                    | RecipeGroups.json                     | `RecipeGroup_[A-Za-z]+`                | `RecipeGroup_OpenBox`                |
| `RM_`                             | Recorded_Media.json                   | `RM_[A-Za-z0-9_]+` or UUID             | `RM_broadcast`                       |
| `Sandbox_`                        | Sandbox.json                          | `Sandbox_[A-Za-z]+`                    | `Sandbox_ZombieCount`                |
| `Stash_`                          | Stash.json                            | `Stash_[A-Za-z0-9_]+`                  | `Stash_LVMap1_Text1`                 |
| `SurvivalGuide_`                  | SurvivalGuide.json                    | `SurvivalGuide_entrie[0-9]+[a-z]+`     | `SurvivalGuide_entrie1title`         |
| `SurvivorSurname_`                | SurvivorNames.json                    | `SurvivorSurname_[A-Za-z]+`            | `SurvivorSurname_Simpson`            |
| `Tooltip_`                        | Tooltip.json                          | `Tooltip_[a-z_]+`                      | `Tooltip_food_Bowl`                  |
| `UI_`                             | UI.json                               | `UI_[a-z_]+`                           | `UI_mainscreen_survival`             |
| PascalCase                        | Recipes.json                          | `[A-Z][a-zA-Z0-9]*`                    | `MakeBiscuits`                       |
| Generic                           | Moveables.json, 5 Location files      | `[A-Za-z_][A-Za-z0-9_]*`               | `50s_Barstool`                       |

---

## All 35 Files Summary

**Items (1):** ItemName.json  
**Crafting (4):** Recipes.json, RecipeGroups.json, EvolvedRecipeName.json, MultiStageBuild.json  
**UI (4):** UI.json, IG_UI.json, Tooltip.json, ContextMenu.json  
**Game Mechanics (5):** Attributes.json, BodyParts.json, Farming.json, Fluids.json, Moodles.json  
**Buildings (3):** Moveables.json, MapLabel.json, Stash.json  
**Locations (5):** West Point KY.json, Rosewood KY.json, Riverside KY.json, Muldraugh KY.json, Echo Creek KY.json  
**Media (6):** RadioData.json, DynamicRadio.json, GameSound.json, Recorded_Media.json, Print_Media.json, Print_Text.json  
**Other (7):** SurvivalGuide.json, SurvivorNames.json, Sandbox.json, Challenge.json, Entity.json, MakeUp.json

---

## Pattern Categories

| Type           | Files                                                         | Examples                                            |
| -------------- | ------------------------------------------------------------- | --------------------------------------------------- |
| Module Prefix  | ItemName, EvolvedRecipeName                                   | `Base.Apple`, `CustomMod.MyItem`                    |
| UI Variants    | UI, IG_UI, Tooltip, ContextMenu                               | `UI_mainscreen_`, `IGUI_invpanel_`, `Tooltip_food_` |
| Simple Prefix  | 12 files                                                      | `Farming_`, `Fluid_`, `MapLabel_`, etc.             |
| Complex Prefix | RecipeGroups, MultiStageBuild, Moodles, Attributes            | Compound patterns with structure                    |
| Special        | Recipes (PascalCase), BodyParts (UPPERCASE), RadioData (UUID) | Unique per file                                     |
| Generic        | Moveables, 5 Location files, Recorded_Media                   | Flexible naming                                     |

---

For full details, see the [`schemas/`](schemas/) directory and [Categories.md](Categories.md)
