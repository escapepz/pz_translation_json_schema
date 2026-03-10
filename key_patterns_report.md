# Complete Key Pattern Analysis

All 35 translation files analyzed with actual key patterns.

## Key Patterns by File

| # | File | Key Pattern | Example |
|----|------|-------------|---------|
| 1 | [ItemName.json](media/lua/shared/Translate/EN/ItemName.json) | `Base.{ItemCodeName}` | `Base.Apple`, `Base.AssaultRifle` |
| 2 | [Recipes.json](media/lua/shared/Translate/EN/Recipes.json) | `{RecipeNameInPascalCase}` | `MakeBiscuits`, `AttachBreadKnifeToSpear` |
| 3 | [RecipeGroups.json](media/lua/shared/Translate/EN/RecipeGroups.json) | `RecipeGroup_{GroupName}` | `RecipeGroup_OpenBox` |
| 4 | [EvolvedRecipeName.json](media/lua/shared/Translate/EN/EvolvedRecipeName.json) | `Base.{ItemCodeName}` | `Base.CannedBologneseOpen`, `Base.Teabag2` |
| 5 | [MultiStageBuild.json](media/lua/shared/Translate/EN/MultiStageBuild.json) | `MultiStageBuild_{Type}_{Action}` | `MultiStageBuild_CreateWoodenWall_1` |
| 6 | [UI.json](media/lua/shared/Translate/EN/UI.json) | `UI_{context}_{keyname}` | `UI_mainscreen_survival`, `UI_optionscreen_fullscreen` |
| 7 | [IG_UI.json](media/lua/shared/Translate/EN/IG_UI.json) | `IGUI_{panel}_{property}` | `IGUI_invpanel_Type`, `IGUI_invpage_Loot_all` |
| 8 | [Tooltip.json](media/lua/shared/Translate/EN/Tooltip.json) | `Tooltip_{category}_{key}` | `Tooltip_food_Bowl`, `Tooltip_item_Weight` |
| 9 | [ContextMenu.json](media/lua/shared/Translate/EN/ContextMenu.json) | `ContextMenu_{ActionName}` | `ContextMenu_Destroy`, `ContextMenu_Sleep` |
| 10 | [Attributes.json](media/lua/shared/Translate/EN/Attributes.json) | `Attributes_Type_{AttributeName}` | `Attributes_Type_Quality`, `Attributes_Type_Durability` |
| 11 | [BodyParts.json](media/lua/shared/Translate/EN/BodyParts.json) | `BODYPART_{PARTNAME}` | `BODYPART_HEAD`, `BODYPART_LEFT_UPPER_ARM` |
| 12 | [Farming.json](media/lua/shared/Translate/EN/Farming.json) | `Farming_{CropName}` | `Farming_Carrots`, `Farming_Tomato` |
| 13 | [Fluids.json](media/lua/shared/Translate/EN/Fluids.json) | `Fluid_{ActionOrProperty}` | `Fluid_Transfer`, `Fluid_Capacity` |
| 14 | [Moodles.json](media/lua/shared/Translate/EN/Moodles.json) | `Moodles_{Type}_lvl{Level}` | `Moodles_Endurance_lvl1`, `Moodles_Stress_lvl4` |
| 15 | [Moveables.json](media/lua/shared/Translate/EN/Moveables.json) | `{FurnitureNameSnakeCase}` | `50s_Barstool`, `Aaaaah!_Painting` |
| 16 | [MapLabel.json](media/lua/shared/Translate/EN/MapLabel.json) | `MapLabel_{LocationName}` | `MapLabel_Brandenburg`, `MapLabel_Riverside` |
| 17 | [Stash.json](media/lua/shared/Translate/EN/Stash.json) | `Stash_{LocationCode}_{ItemKey}` | `Stash_LVMap1_Text1`, `Stash_AnnotedMap` |
| 18 | [RadioData.json](media/lua/shared/Translate/EN/RadioData.json) | `RD_{UUID}` | `RD_b0ee632b-789e-4e4f-a2b0-b09374856a62` |
| 19 | [DynamicRadio.json](media/lua/shared/Translate/EN/DynamicRadio.json) | `AEBS_{PropertyName}` or generic | `AEBS_Intro`, `AEBS_temperature` |
| 20 | [GameSound.json](media/lua/shared/Translate/EN/GameSound.json) | `GameSound_{SoundName}` | `GameSound_AlarmClockRingingLoop`, `GameSound_BatHit` |
| 21 | [Recorded_Media.json](media/lua/shared/Translate/EN/Recorded_Media.json) | Generic | (Not sampled) |
| 22 | [Print_Media.json](media/lua/shared/Translate/EN/Print_Media.json) | `Print_Media_{MediaName}_{property}` | `Print_Media_KnoxKnews_July1_title` |
| 23 | [Print_Text.json](media/lua/shared/Translate/EN/Print_Text.json) | `Print_Text_{MediaName}_{property}` | `Print_Text_KnoxKnews_July1_title` |
| 24 | [SurvivalGuide.json](media/lua/shared/Translate/EN/SurvivalGuide.json) | `SurvivalGuide_{entryNum}{property}` | `SurvivalGuide_entrie1title`, `SurvivalGuide_entrie2txt` |
| 25 | [SurvivorNames.json](media/lua/shared/Translate/EN/SurvivorNames.json) | `SurvivorSurname_{LastName}` | `SurvivorSurname_Simpson`, `SurvivorSurname_Smith` |
| 26 | [Sandbox.json](media/lua/shared/Translate/EN/Sandbox.json) | `Sandbox_{OptionName}` | `Sandbox_PopulationOptions`, `Sandbox_ZombieCount` |
| 27 | [Challenge.json](media/lua/shared/Translate/EN/Challenge.json) | `Challenge_{ScenarioId}_{property}` | `Challenge_YouHaveOneDay_name`, `Challenge_Opening Hours_desc` |
| 28 | [Entity.json](media/lua/shared/Translate/EN/Entity.json) | `EC_{PropertyName}` | `EC_Entity_DisplayName_Default`, `EC_Energy_Electric` |
| 29 | [MakeUp.json](media/lua/shared/Translate/EN/MakeUp.json) | `MakeUpCategory/Type_{Name}` | `MakeUpCategory_Eyes`, `MakeUpType_EyesFootball` |
| 30 | [West Point, KY.json](media/lua/shared/Translate/EN/West%20Point,%20KY.json) | Generic | (Location-specific) |
| 31 | [Rosewood, KY.json](media/lua/shared/Translate/EN/Rosewood,%20KY.json) | Generic | (Location-specific) |
| 32 | [Riverside, KY.json](media/lua/shared/Translate/EN/Riverside,%20KY.json) | Generic | (Location-specific) |
| 33 | [Muldraugh, KY.json](media/lua/shared/Translate/EN/Muldraugh,%20KY.json) | Generic | (Location-specific) |
| 34 | [Echo Creek, KY.json](media/lua/shared/Translate/EN/Echo%20Creek,%20KY.json) | Generic | (Location-specific) |

## Pattern Summary

### Prefixed Patterns (File-specific)
- **UI_** → UI.json, IG_UI.json (with sub-prefixes)
- **Base.** → ItemName.json, EvolvedRecipeName.json
- **Tooltip_** → Tooltip.json
- **MapLabel_** → MapLabel.json
- **Stash_** → Stash.json
- **RD_** → RadioData.json
- **AEBS_** → DynamicRadio.json
- **GameSound_** → GameSound.json
- **Attributes_Type_** → Attributes.json
- **BODYPART_** → BodyParts.json
- **Farming_** → Farming.json
- **Fluid_** → Fluids.json
- **Moodles_** → Moodles.json
- **ContextMenu_** → ContextMenu.json
- **RecipeGroup_** → RecipeGroups.json
- **MultiStageBuild_** → MultiStageBuild.json
- **Print_Media_** → Print_Media.json
- **Print_Text_** → Print_Text.json
- **SurvivalGuide_** → SurvivalGuide.json
- **SurvivorSurname_** → SurvivorNames.json
- **Sandbox_** → Sandbox.json
- **Challenge_** → Challenge.json
- **EC_** → Entity.json
- **MakeUpCategory/Type_** → MakeUp.json
- **IGUI_** → IG_UI.json

### Generic/No Prefix Patterns
- **Recipes.json** → PascalCase (MakeBiscuits, AttachBreadKnifeToSpear)
- **Moveables.json** → Underscore-separated names (50s_Barstool, Aaaaah!_Painting)
- **Location files** → Vary by location
- **Recorded_Media.json** → Unknown (not sampled)

