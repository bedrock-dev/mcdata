#### VanillaBiomeTypeAttributes
```cpp
/* 191222 */
struct VanillaBiomeTypeAttributes
{
VanillaBiomeTypes_0 mBiomeType;
};

```
#### VanillaBiomes
```cpp
/* 197945 */
struct VanillaBiomes
{
__int8 gap0[1];
};

```
#### VanillaBlockStateTransformUtils
```cpp
/* 296870 */
struct VanillaBlockStateTransformUtils
{
__int8 gap0[1];
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<CoralDirection>
```cpp
/* 461050 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<CoralDirection>
{
std::vector<std::pair<CoralDirection,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,CoralDirection>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<Direction::Type>
```cpp
/* 296872 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<Direction::Type>
{
std::vector<std::pair<Direction::Type,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,Direction::Type>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<Facing::Name>
```cpp
/* 296871 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<Facing::Name>
{
std::vector<std::pair<Facing::Name,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,Facing::Name>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<LeverDirection>
```cpp
/* 461051 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<LeverDirection>
{
std::vector<std::pair<LeverDirection,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,LeverDirection>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<PillarAxis>
```cpp
/* 461052 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<PillarAxis>
{
std::vector<std::pair<PillarAxis,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,PillarAxis>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<PortalAxis>
```cpp
/* 461046 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<PortalAxis>
{
std::vector<std::pair<PortalAxis,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,PortalAxis>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<RailDirection>
```cpp
/* 461047 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<RailDirection>
{
std::vector<std::pair<RailDirection,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,RailDirection>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<TorchFacing>
```cpp
/* 461048 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<TorchFacing>
{
std::vector<std::pair<TorchFacing,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,TorchFacing>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<WeirdoDirection>
```cpp
/* 461049 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<WeirdoDirection>
{
std::vector<std::pair<WeirdoDirection,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,WeirdoDirection>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::transformStandingRotation::$1E86A9CFC8E8AB731D791E938854EF55
```cpp
/* 461226 */
struct VanillaBlockStateTransformUtils::transformStandingRotation::$1E86A9CFC8E8AB731D791E938854EF55
{
const int halfSteps;
const int variationCount;
};

```
#### VanillaBlockUpdater
```cpp
/* 235025 */
struct VanillaBlockUpdater
{
__int8 gap0[1];
};

```
#### VanillaDimensions
```cpp
/* 255040 */
struct VanillaDimensions
{
__int8 gap0[1];
};

```
#### VanillaFeatures
```cpp
/* 31220 */
struct VanillaFeatures
{
__int8 gap0[1];
};

```
#### VanillaGameModuleServer::initializeBehaviorStack::$C1F886AF5C927D64019CD3E2F97D7EC0
```cpp
/* 13236 */
struct VanillaGameModuleServer::initializeBehaviorStack::$C1F886AF5C927D64019CD3E2F97D7EC0
{
ResourcePackRepository *repo;
ResourcePackStack *tempStack;
};

```
#### VanillaItemTiers
```cpp
/* 457257 */
struct VanillaItemTiers
{
__int8 gap0[1];
};

```
#### VanillaItems
```cpp
/* 183766 */
struct VanillaItems
{
__int8 gap0[1];
};

```
#### VanillaVillageJigsawStructureActorRules
```cpp
/* 35622 */
struct VanillaVillageJigsawStructureActorRules
{
__int8 gap0[1];
};

```
#### VanillaVillageJigsawStructureBlockRules
```cpp
/* 35879 */
struct VanillaVillageJigsawStructureBlockRules
{
__int8 gap0[1];
};

```
#### VanillaVillageJigsawStructureBlockTagRules
```cpp
/* 36063 */
struct VanillaVillageJigsawStructureBlockTagRules
{
__int8 gap0[1];
};

```
#### VanillaVillageJigsawStructureElements
```cpp
/* 36153 */
struct VanillaVillageJigsawStructureElements
{
__int8 gap0[1];
};

```
#### VanillaVillageJigsawStructures
```cpp
/* 32814 */
struct VanillaVillageJigsawStructures
{
__int8 gap0[1];
};

```
#### VariantParameterList
```cpp
/* 39406 */
struct VariantParameterList
{
VariantParameterList::Parameter parameters[7];
};

```
#### Vec2
```cpp
/* 4316 */
struct Vec2
{
float x;
float y;
};

```
#### Vec3
```cpp
/* 5796 */
struct Vec3
{
float x;
float y;
float z;
};

```
#### Vec4
```cpp
/* 102289 */
struct Vec4
{
float x;
float y;
float z;
float w;
};

```
#### Village
```cpp
/* 52684 */
struct Village
{
mce::UUID mUniqueID;
Dimension *mDimension;
Village::UnclaimedPOIList mUnclaimedPOIStacks;
Village::ClaimedPOIList mClaimedPOIs;
std::array<std::unordered_map<ActorUniqueID,Tick>,4> mDwellers;
AABB mBounds;
AABB mStaticRaidBounds;
byte mVillageVersion;
Tick mGameTick;
Tick mSaveTick;
Tick mRingTick;
Tick mNoBreedTimer;
int64_t mVillageHeroTimer;
int mInitializationTimer;
std::unordered_map<ActorUniqueID,int> mPlayerStanding;
Village::DwellerMap mAggressors;
bool mVillageInitialized;
const Util::HashString mNitwitFamily;
const Util::HashString mVillagePrefix;
std::unique_ptr<Raid> mRaid;
std::unordered_set<ActorUniqueID> mSoundTheAlarmPlayerList;
};

```
#### VillageLegacy;
```cpp
/* 88767 */
struct VillageLegacy;

```
#### VillageManager
```cpp
/* 34809 */
struct VillageManager
{
Dimension *mDimension;
std::vector<BlockPos> mFindPOIQueries;
std::vector<std::shared_ptr<POIInstance>> mUnclusteredPOIs;
VillageManager::VillageMap mVillages;
std::array<std::unordered_map<BlockPos,std::shared_ptr<POIInstance>>,3> mClusteredPOIs;
VillageManager::POIBlueprintMap mPOIBlueprints;
Tick mTickCount;
WanderingTraderScheduler mWanderingTraderScheduler;
bool mFinishedQueryScan;
int mCurrentXScan;
int mCurrentYScan;
int mCurrentZScan;
};

```
#### Village_0
```cpp
/* 122663 */
struct Village_0
{
mce::UUID mUniqueID;
Dimension *mDimension;
Village::UnclaimedPOIList mUnclaimedPOIStacks;
Village::ClaimedPOIList mClaimedPOIs;
std::array<std::unordered_map<ActorUniqueID,Tick>,4> mDwellers;
AABB mBounds;
AABB mStaticRaidBounds;
byte_0 mVillageVersion;
Tick mGameTick;
Tick mSaveTick;
Tick mRingTick;
Tick mNoBreedTimer;
int64_t mVillageHeroTimer;
int mInitializationTimer;
std::unordered_map<ActorUniqueID,int> mPlayerStanding;
Village::DwellerMap mAggressors;
bool mVillageInitialized;
const Util::HashString mNitwitFamily;
const Util::HashString mVillagePrefix;
std::unique_ptr<Raid> mRaid;
std::unordered_set<ActorUniqueID> mSoundTheAlarmPlayerList;
};

```
#### VillagerV2::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 171082 */
struct VillagerV2::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### VanillaBiomeTypeAttributes
```cpp
/* 191222 */
struct VanillaBiomeTypeAttributes
{
VanillaBiomeTypes_0 mBiomeType;
};

```
#### VanillaBiomes
```cpp
/* 197945 */
struct VanillaBiomes
{
__int8 gap0[1];
};

```
#### VanillaBlockStateTransformUtils
```cpp
/* 296870 */
struct VanillaBlockStateTransformUtils
{
__int8 gap0[1];
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<CoralDirection>
```cpp
/* 461050 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<CoralDirection>
{
std::vector<std::pair<CoralDirection,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,CoralDirection>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<Direction::Type>
```cpp
/* 296872 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<Direction::Type>
{
std::vector<std::pair<Direction::Type,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,Direction::Type>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<Facing::Name>
```cpp
/* 296871 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<Facing::Name>
{
std::vector<std::pair<Facing::Name,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,Facing::Name>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<LeverDirection>
```cpp
/* 461051 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<LeverDirection>
{
std::vector<std::pair<LeverDirection,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,LeverDirection>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<PillarAxis>
```cpp
/* 461052 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<PillarAxis>
{
std::vector<std::pair<PillarAxis,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,PillarAxis>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<PortalAxis>
```cpp
/* 461046 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<PortalAxis>
{
std::vector<std::pair<PortalAxis,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,PortalAxis>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<RailDirection>
```cpp
/* 461047 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<RailDirection>
{
std::vector<std::pair<RailDirection,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,RailDirection>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<TorchFacing>
```cpp
/* 461048 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<TorchFacing>
{
std::vector<std::pair<TorchFacing,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,TorchFacing>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::CommonDirectionMapping<WeirdoDirection>
```cpp
/* 461049 */
struct VanillaBlockStateTransformUtils::CommonDirectionMapping<WeirdoDirection>
{
std::vector<std::pair<WeirdoDirection,CommonDirection>> mToRight;
std::vector<std::pair<CommonDirection,WeirdoDirection>> mToLeft;
};

```
#### VanillaBlockStateTransformUtils::transformStandingRotation::$1E86A9CFC8E8AB731D791E938854EF55
```cpp
/* 461226 */
struct VanillaBlockStateTransformUtils::transformStandingRotation::$1E86A9CFC8E8AB731D791E938854EF55
{
const int halfSteps;
const int variationCount;
};

```
#### VanillaBlockUpdater
```cpp
/* 235025 */
struct VanillaBlockUpdater
{
__int8 gap0[1];
};

```
#### VanillaDimensions
```cpp
/* 255040 */
struct VanillaDimensions
{
__int8 gap0[1];
};

```
#### VanillaFeatures
```cpp
/* 31220 */
struct VanillaFeatures
{
__int8 gap0[1];
};

```
#### VanillaGameModuleServer::initializeBehaviorStack::$C1F886AF5C927D64019CD3E2F97D7EC0
```cpp
/* 13236 */
struct VanillaGameModuleServer::initializeBehaviorStack::$C1F886AF5C927D64019CD3E2F97D7EC0
{
ResourcePackRepository *repo;
ResourcePackStack *tempStack;
};

```
#### VanillaItemTiers
```cpp
/* 457257 */
struct VanillaItemTiers
{
__int8 gap0[1];
};

```
#### VanillaItems
```cpp
/* 183766 */
struct VanillaItems
{
__int8 gap0[1];
};

```
#### VanillaVillageJigsawStructureActorRules
```cpp
/* 35622 */
struct VanillaVillageJigsawStructureActorRules
{
__int8 gap0[1];
};

```
#### VanillaVillageJigsawStructureBlockRules
```cpp
/* 35879 */
struct VanillaVillageJigsawStructureBlockRules
{
__int8 gap0[1];
};

```
#### VanillaVillageJigsawStructureBlockTagRules
```cpp
/* 36063 */
struct VanillaVillageJigsawStructureBlockTagRules
{
__int8 gap0[1];
};

```
#### VanillaVillageJigsawStructureElements
```cpp
/* 36153 */
struct VanillaVillageJigsawStructureElements
{
__int8 gap0[1];
};

```
#### VanillaVillageJigsawStructures
```cpp
/* 32814 */
struct VanillaVillageJigsawStructures
{
__int8 gap0[1];
};

```
#### VariantParameterList
```cpp
/* 39406 */
struct VariantParameterList
{
VariantParameterList::Parameter parameters[7];
};

```
#### Vec2
```cpp
/* 4316 */
struct Vec2
{
float x;
float y;
};

```
#### Vec3
```cpp
/* 5796 */
struct Vec3
{
float x;
float y;
float z;
};

```
#### Vec4
```cpp
/* 102289 */
struct Vec4
{
float x;
float y;
float z;
float w;
};

```
#### Village
```cpp
/* 52684 */
struct Village
{
mce::UUID mUniqueID;
Dimension *mDimension;
Village::UnclaimedPOIList mUnclaimedPOIStacks;
Village::ClaimedPOIList mClaimedPOIs;
std::array<std::unordered_map<ActorUniqueID,Tick>,4> mDwellers;
AABB mBounds;
AABB mStaticRaidBounds;
byte mVillageVersion;
Tick mGameTick;
Tick mSaveTick;
Tick mRingTick;
Tick mNoBreedTimer;
int64_t mVillageHeroTimer;
int mInitializationTimer;
std::unordered_map<ActorUniqueID,int> mPlayerStanding;
Village::DwellerMap mAggressors;
bool mVillageInitialized;
const Util::HashString mNitwitFamily;
const Util::HashString mVillagePrefix;
std::unique_ptr<Raid> mRaid;
std::unordered_set<ActorUniqueID> mSoundTheAlarmPlayerList;
};

```
#### VillageLegacy;
```cpp
/* 88767 */
struct VillageLegacy;

```
#### VillageManager
```cpp
/* 34809 */
struct VillageManager
{
Dimension *mDimension;
std::vector<BlockPos> mFindPOIQueries;
std::vector<std::shared_ptr<POIInstance>> mUnclusteredPOIs;
VillageManager::VillageMap mVillages;
std::array<std::unordered_map<BlockPos,std::shared_ptr<POIInstance>>,3> mClusteredPOIs;
VillageManager::POIBlueprintMap mPOIBlueprints;
Tick mTickCount;
WanderingTraderScheduler mWanderingTraderScheduler;
bool mFinishedQueryScan;
int mCurrentXScan;
int mCurrentYScan;
int mCurrentZScan;
};

```
#### Village_0
```cpp
/* 122663 */
struct Village_0
{
mce::UUID mUniqueID;
Dimension *mDimension;
Village::UnclaimedPOIList mUnclaimedPOIStacks;
Village::ClaimedPOIList mClaimedPOIs;
std::array<std::unordered_map<ActorUniqueID,Tick>,4> mDwellers;
AABB mBounds;
AABB mStaticRaidBounds;
byte_0 mVillageVersion;
Tick mGameTick;
Tick mSaveTick;
Tick mRingTick;
Tick mNoBreedTimer;
int64_t mVillageHeroTimer;
int mInitializationTimer;
std::unordered_map<ActorUniqueID,int> mPlayerStanding;
Village::DwellerMap mAggressors;
bool mVillageInitialized;
const Util::HashString mNitwitFamily;
const Util::HashString mVillagePrefix;
std::unique_ptr<Raid> mRaid;
std::unordered_set<ActorUniqueID> mSoundTheAlarmPlayerList;
};

```
#### VillagerV2::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 171082 */
struct VillagerV2::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
