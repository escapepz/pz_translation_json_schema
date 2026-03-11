# Complete Key Pattern Analysis

All 35 translation files analyzed with actual key patterns.

## Key Patterns by File

| # | File | Key Pattern | Example |
|----|------|-------------|---------|
| 1 | [Attributes.json](media/lua/shared/Translate/EN/Attributes.json) | `Attributes_Type_{AttributeName}` | `Attributes_Type_Quality`, `Attributes_Type_Durability` |
| 2 | [BodyParts.json](media/lua/shared/Translate/EN/BodyParts.json) | `BODYPART_{PARTNAME}` | `BODYPART_HEAD`, `BODYPART_LEFT_UPPER_ARM` |
| 3 | [Challenge.json](media/lua/shared/Translate/EN/Challenge.json) | `Challenge_{ScenarioId}_{property}` | `Challenge_YouHaveOneDay_name`, `Challenge_Opening Hours_desc` |
| 4 | [ContextMenu.json](media/lua/shared/Translate/EN/ContextMenu.json) | `ContextMenu_{ActionName}` | `ContextMenu_Destroy`, `ContextMenu_Sleep` |
| 5 | [DynamicRadio.json](media/lua/shared/Translate/EN/DynamicRadio.json) | `AEBS_{PropertyName}` or generic | `AEBS_Intro`, `AEBS_temperature` |
| 6 | [Entity.json](media/lua/shared/Translate/EN/Entity.json) | `EC_{PropertyName}` | `EC_Entity_DisplayName_Default`, `EC_Energy_Electric` |
| 7 | [EvolvedRecipeName.json](media/lua/shared/Translate/EN/EvolvedRecipeName.json) | `Base.{ItemCodeName}` | `Base.CannedBologneseOpen`, `Base.Teabag2` |
| 8 | [Farming.json](media/lua/shared/Translate/EN/Farming.json) | `Farming_{CropName}` | `Farming_Carrots`, `Farming_Tomato` |
| 9 | [Fluids.json](media/lua/shared/Translate/EN/Fluids.json) | `Fluid_{ActionOrProperty}` | `Fluid_Transfer`, `Fluid_Capacity` |
| 10 | [GameSound.json](media/lua/shared/Translate/EN/GameSound.json) | `GameSound_{SoundName}` | `GameSound_AlarmClockRingingLoop`, `GameSound_BatHit` |
| 11 | [IG_UI.json](media/lua/shared/Translate/EN/IG_UI.json) | `IGUI_{panel}_{property}` | `IGUI_invpanel_Type`, `IGUI_invpage_Loot_all` |
| 12 | [ItemName.json](media/lua/shared/Translate/EN/ItemName.json) | `Base.{ItemCodeName}` | `Base.Apple`, `Base.AssaultRifle` |
| 13 | [MakeUp.json](media/lua/shared/Translate/EN/MakeUp.json) | `MakeUpCategory/Type_{Name}` | `MakeUpCategory_Eyes`, `MakeUpType_EyesFootball` |
| 14 | [MapLabel.json](media/lua/shared/Translate/EN/MapLabel.json) | `MapLabel_{LocationName}` | `MapLabel_Brandenburg`, `MapLabel_Riverside` |
| 15 | [Moodles.json](media/lua/shared/Translate/EN/Moodles.json) | `Moodles_{Type}_lvl{Level}` | `Moodles_Endurance_lvl1`, `Moodles_Stress_lvl4` |
| 16 | [Moveables.json](media/lua/shared/Translate/EN/Moveables.json) | `{FurnitureNameSnakeCase}` | `50s_Barstool`, `Aaaaah!_Painting` |
| 17 | [MultiStageBuild.json](media/lua/shared/Translate/EN/MultiStageBuild.json) | `MultiStageBuild_{Type}_{Action}` | `MultiStageBuild_CreateWoodenWall_1` |
| 18 | [Print_Media.json](media/lua/shared/Translate/EN/Print_Media.json) | `Print_Media_{MediaName}_{property}` | `Print_Media_KnoxKnews_July1_title` |
| 20 | [Print_Text.json](media/lua/shared/Translate/EN/Print_Text.json) | `Print_Text_{MediaName}_{property}` | `Print_Text_KnoxKnews_July1_title` |
| 21 | [RadioData.json](media/lua/shared/Translate/EN/RadioData.json) | `RD_{UUID}` | `RD_b0ee632b-789e-4e4f-a2b0-b09374856a62` |
| 22 | [RecipeGroups.json](media/lua/shared/Translate/EN/RecipeGroups.json) | `RecipeGroup_{GroupName}` | `RecipeGroup_OpenBox` |
| 23 | [Recipes.json](media/lua/shared/Translate/EN/Recipes.json) | `{RecipeNameInPascalCase}` | `MakeBiscuits`, `AttachBreadKnifeToSpear` |
| 24 | [Recorded_Media.json](media/lua/shared/Translate/EN/Recorded_Media.json) | `RM_{PropertyName}` or UUID | `RM_broadcast` |
| 25 | [Sandbox.json](media/lua/shared/Translate/EN/Sandbox.json) | `Sandbox_{OptionName}` | `Sandbox_PopulationOptions`, `Sandbox_ZombieCount` |
| 26 | [Stash.json](media/lua/shared/Translate/EN/Stash.json) | `Stash_{LocationCode}_{ItemKey}` | `Stash_LVMap1_Text1`, `Stash_AnnotedMap` |
| 27 | [SurvivalGuide.json](media/lua/shared/Translate/EN/SurvivalGuide.json) | `SurvivalGuide_{entryNum}{property}` | `SurvivalGuide_entrie1title`, `SurvivalGuide_entrie2txt` |
| 28 | [SurvivorNames.json](media/lua/shared/Translate/EN/SurvivorNames.json) | `SurvivorSurname_{LastName}` | `SurvivorSurname_Simpson`, `SurvivorSurname_Smith` |
| 29 | [Tooltip.json](media/lua/shared/Translate/EN/Tooltip.json) | `Tooltip_{category}_{key}` | `Tooltip_food_Bowl`, `Tooltip_item_Weight` |
| 30 | [UI.json](media/lua/shared/Translate/EN/UI.json) | `UI_{context}_{keyname}` | `UI_mainscreen_survival`, `UI_optionscreen_fullscreen` |
| 31 | [West Point, KY.json](media/lua/shared/Translate/EN/West%20Point,%20KY.json) | Generic | (Location-specific) |
| 32 | [Rosewood, KY.json](media/lua/shared/Translate/EN/Rosewood,%20KY.json) | Generic | (Location-specific) |
| 33 | [Riverside, KY.json](media/lua/shared/Translate/EN/Riverside,%20KY.json) | Generic | (Location-specific) |
| 34 | [Muldraugh, KY.json](media/lua/shared/Translate/EN/Muldraugh,%20KY.json) | Generic | (Location-specific) |
| 35 | [Echo Creek, KY.json](media/lua/shared/Translate/EN/Echo%20Creek,%20KY.json) | Generic | (Location-specific) |

## Pattern Summary

### Prefixed Patterns (File-specific)
- **AEBS_** → DynamicRadio.json
- **Attributes_Type_** → Attributes.json
- **Base.** → ItemName.json, EvolvedRecipeName.json
- **BODYPART_** → BodyParts.json
- **Challenge_** → Challenge.json
- **ContextMenu_** → ContextMenu.json
- **EC_** → Entity.json
- **Farming_** → Farming.json
- **Fluid_** → Fluids.json
- **GameSound_** → GameSound.json
- **IGUI_** → IG_UI.json
- **MakeUpCategory/Type_** → MakeUp.json
- **MapLabel_** → MapLabel.json
- **Moodles_** → Moodles.json
- **MultiStageBuild_** → MultiStageBuild.json
- **Print_Media_** → Print_Media.json
- **Print_Text_** → Print_Text.json
- **RD_** → RadioData.json
- **RecipeGroup_** → RecipeGroups.json
- **RM_** → Recorded_Media.json (also uses UUIDs or flexible/generic naming)
- **Sandbox_** → Sandbox.json
- **Stash_** → Stash.json
- **SurvivalGuide_** → SurvivalGuide.json
- **SurvivorSurname_** → SurvivorNames.json
- **Tooltip_** → Tooltip.json
- **UI_** → UI.json, IG_UI.json (with sub-prefixes)

### Generic/No Prefix Patterns
- **Recipes.json** → PascalCase (MakeBiscuits, AttachBreadKnifeToSpear)
- **Moveables.json** → Underscore-separated names (50s_Barstool, Aaaaah!_Painting)
- **Location files** → Vary by location
