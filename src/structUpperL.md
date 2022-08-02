#### LONG_DOUBLE_16
```cpp
/* 486702 */
struct LONG_DOUBLE_16
{
_TBYTE value;
char padding[6];
};

```
#### LabTableReactionComponent
```cpp
/* 238069 */
struct LabTableReactionComponent
{
int (**_vptr$LabTableReactionComponent)(void);
};

```
#### LargeCaveFeature
```cpp
/* 40160 */
struct LargeCaveFeature
{
int (**_vptr$LargeCaveFeature)(void);
};

```
#### LargeHellCaveFeature
```cpp
/* 36894 */
struct LargeHellCaveFeature
{
__int8 gap0[1];
};

```
#### LayerDetails::BufferAccessor<Biome *>
```cpp
/* 39874 */
struct LayerDetails::BufferAccessor<Biome *>
{
char *mStorage;
size_t mCount;
};

```
#### LayerDetails::BufferAccessor<Biome *>::TypedBits
```cpp
/* 40543 */
struct LayerDetails::BufferAccessor<Biome *>::TypedBits
{
char *mLocation;
};

```
#### LayerDetails::BufferAccessor<BiomeTemperatureCategory>
```cpp
/* 40026 */
struct LayerDetails::BufferAccessor<BiomeTemperatureCategory>
{
char *mStorage;
size_t mCount;
};

```
#### LayerDetails::BufferAccessor<BiomeTemperatureCategory>::TypedBits
```cpp
/* 40550 */
struct LayerDetails::BufferAccessor<BiomeTemperatureCategory>::TypedBits
{
char *mLocation;
};

```
#### LayerDetails::BufferAccessor<LayerValues::PreBiome>
```cpp
/* 39828 */
struct LayerDetails::BufferAccessor<LayerValues::PreBiome>
{
char *mStorage;
size_t mCount;
};

```
#### LayerDetails::BufferAccessor<LayerValues::PreBiome>::TypedBits
```cpp
/* 40539 */
struct LayerDetails::BufferAccessor<LayerValues::PreBiome>::TypedBits
{
char *mLocation;
};

```
#### LayerDetails::BufferAccessor<LayerValues::Terrain>
```cpp
/* 39752 */
struct LayerDetails::BufferAccessor<LayerValues::Terrain>
{
char *mStorage;
size_t mCount;
};

```
#### LayerDetails::BufferAccessor<LayerValues::Terrain>::TypedBits
```cpp
/* 40537 */
struct LayerDetails::BufferAccessor<LayerValues::Terrain>::TypedBits
{
char *mLocation;
};

```
#### LayerDetails::BufferAccessor<bool>
```cpp
/* 39932 */
struct LayerDetails::BufferAccessor<bool>
{
char *mStorage;
size_t mCount;
};

```
#### LayerDetails::BufferAccessor<bool>::TypedBits
```cpp
/* 40547 */
struct LayerDetails::BufferAccessor<bool>::TypedBits
{
char *mLocation;
};

```
#### LayerDetails::BufferAccessor<char>
```cpp
/* 39751 */
struct LayerDetails::BufferAccessor<char>
{
char *mStorage;
size_t mCount;
};

```
#### LayerDetails::BufferAccessor<char>::TypedBits;
```cpp
/* 40552 */
struct LayerDetails::BufferAccessor<char>::TypedBits;

```
#### LayerDetails::BufferAccessor<int>
```cpp
/* 39906 */
struct LayerDetails::BufferAccessor<int>
{
char *mStorage;
size_t mCount;
};

```
#### LayerDetails::BufferAccessor<int>::TypedBits
```cpp
/* 40545 */
struct LayerDetails::BufferAccessor<int>::TypedBits
{
char *mLocation;
};

```
#### LayerDetails::LayerBase
```cpp
/* 37190 */
struct LayerDetails::LayerBase
{
int (**_vptr$LayerBase)(void);
int64_t mSeed;
int64_t mSeedMixup;
};

```
#### LayerDetails::NeighborhoodReader<Biome *,0,0>
```cpp
/* 40546 */
struct LayerDetails::NeighborhoodReader<Biome *,0,0>
{
const LayerDetails::BufferAccessor<Biome *> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::NeighborhoodReader<Biome *,1,1>
```cpp
/* 40544 */
struct LayerDetails::NeighborhoodReader<Biome *,1,1>
{
const LayerDetails::BufferAccessor<Biome *> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::NeighborhoodReader<BiomeTemperatureCategory,1,1>
```cpp
/* 40551 */
struct LayerDetails::NeighborhoodReader<BiomeTemperatureCategory,1,1>
{
const LayerDetails::BufferAccessor<BiomeTemperatureCategory> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::NeighborhoodReader<LayerValues::PreBiome,0,0>
```cpp
/* 40542 */
struct LayerDetails::NeighborhoodReader<LayerValues::PreBiome,0,0>
{
const LayerDetails::BufferAccessor<LayerValues::PreBiome> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::NeighborhoodReader<LayerValues::PreBiome,1,1>
```cpp
/* 40541 */
struct LayerDetails::NeighborhoodReader<LayerValues::PreBiome,1,1>
{
const LayerDetails::BufferAccessor<LayerValues::PreBiome> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::NeighborhoodReader<LayerValues::Terrain,0,0>
```cpp
/* 40540 */
struct LayerDetails::NeighborhoodReader<LayerValues::Terrain,0,0>
{
const LayerDetails::BufferAccessor<LayerValues::Terrain> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::NeighborhoodReader<LayerValues::Terrain,1,1>
```cpp
/* 40538 */
struct LayerDetails::NeighborhoodReader<LayerValues::Terrain,1,1>
{
const LayerDetails::BufferAccessor<LayerValues::Terrain> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::NeighborhoodReader<bool,1,1>
```cpp
/* 40549 */
struct LayerDetails::NeighborhoodReader<bool,1,1>
{
const LayerDetails::BufferAccessor<bool> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::NeighborhoodReader<int,1,1>
```cpp
/* 40548 */
struct LayerDetails::NeighborhoodReader<int,1,1>
{
const LayerDetails::BufferAccessor<int> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::RandomProviderT<(lambda at _Minecraftpe_handheld_project_dedicated_server_______src_common_world_level_newbiome_LayerDetails_h:221:34)>
```cpp
/* 37665 */
struct LayerDetails::RandomProviderT<(lambda at _Minecraftpe_handheld_project_dedicated_server_______src_common_world_level_newbiome_LayerDetails_h:221:34)>
{
$9B9F62DABB3B3036AEF15BA6ABCB0C35 mNextRandom;
int64_t mRval;
};

```
#### LayerDetails::Storage
```cpp
/* 39750 */
struct LayerDetails::Storage
{
size_t mReadableBytes;
size_t mWriteableBytes;
std::unique_ptr<char []> mReadStorage;
std::unique_ptr<char []> mWriteStorage;
};

```
#### LayerDetails::TransferData<char>;
```cpp
/* 40553 */
struct LayerDetails::TransferData<char>;

```
#### LayerFilters::AddBiomeIsland
```cpp
/* 38482 */
struct LayerFilters::AddBiomeIsland
{
Biome *mDefaultIsland;
Biome *mSpecialIsland;
std::vector<Biome *> mShallowOceanBiomes;
};

```
#### LayerFilters::AddMushroomIsland
```cpp
/* 38027 */
struct LayerFilters::AddMushroomIsland
{
Biome *mMushroomBiome;
const BiomeRegistry *mBiomeRegistry;
};

```
#### LayerFilters::BiomeInit
```cpp
/* 37952 */
struct LayerFilters::BiomeInit
{
Biome *mFallbackBiome;
Biome *mDefaultOcean;
std::vector<std::pair<Biome *,unsigned int>> mRegularBiomes[5];
std::vector<std::pair<Biome *,unsigned int>> mSpecialBiomes[5];
};

```
#### LayerFilters::FilterBase<1,1,Biome *,Biome *>
```cpp
/* 38238 */
struct LayerFilters::FilterBase<1,1,Biome *,Biome *>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<1,1,Biome *,LayerValues::PreBiome>
```cpp
/* 37953 */
struct LayerFilters::FilterBase<1,1,Biome *,LayerValues::PreBiome>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<1,1,LayerValues::PreBiome,LayerValues::PreBiome>
```cpp
/* 37903 */
struct LayerFilters::FilterBase<1,1,LayerValues::PreBiome,LayerValues::PreBiome>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<1,1,LayerValues::PreBiome,LayerValues::Terrain>
```cpp
/* 37781 */
struct LayerFilters::FilterBase<1,1,LayerValues::PreBiome,LayerValues::Terrain>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<1,1,int,Biome *>
```cpp
/* 38111 */
struct LayerFilters::FilterBase<1,1,int,Biome *>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<3,3,Biome *,Biome *>
```cpp
/* 38028 */
struct LayerFilters::FilterBase<3,3,Biome *,Biome *>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<3,3,BiomeTemperatureCategory,BiomeTemperatureCategory>
```cpp
/* 38640 */
struct LayerFilters::FilterBase<3,3,BiomeTemperatureCategory,BiomeTemperatureCategory>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<3,3,LayerValues::PreBiome,LayerValues::PreBiome>
```cpp
/* 37833 */
struct LayerFilters::FilterBase<3,3,LayerValues::PreBiome,LayerValues::PreBiome>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<3,3,LayerValues::Terrain,LayerValues::Terrain>
```cpp
/* 37711 */
struct LayerFilters::FilterBase<3,3,LayerValues::Terrain,LayerValues::Terrain>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<3,3,bool,bool>
```cpp
/* 38214 */
struct LayerFilters::FilterBase<3,3,bool,bool>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<3,3,bool,int>
```cpp
/* 38174 */
struct LayerFilters::FilterBase<3,3,bool,int>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilteredTransformation<FilteredTransformationAttributes<LegacyPreHillsEdgeTransformation> >
```cpp
/* 38418 */
struct LayerFilters::FilteredTransformation<FilteredTransformationAttributes<LegacyPreHillsEdgeTransformation> >
{
const TagRegistry *mTagRegistry;
};

```
#### LayerFilters::FilteredTransformation<FilteredTransformationAttributes<PostShoreEdgeTransformation> >
```cpp
/* 38529 */
struct LayerFilters::FilteredTransformation<FilteredTransformationAttributes<PostShoreEdgeTransformation> >
{
const TagRegistry *mTagRegistry;
};

```
#### LayerFilters::FilteredTransformation<FilteredTransformationAttributes<PreHillsEdgeTransformation> >
```cpp
/* 38393 */
struct LayerFilters::FilteredTransformation<FilteredTransformationAttributes<PreHillsEdgeTransformation> >
{
const TagRegistry *mTagRegistry;
};

```
#### LayerFilters::PromoteCenter
```cpp
/* 38051 */
struct LayerFilters::PromoteCenter
{
Biome *mFrom;
Biome *mTo;
};

```
#### LayerFilters::RareBiomeSpot
```cpp
/* 38237 */
struct LayerFilters::RareBiomeSpot
{
uint32_t mChance;
Biome *mFromBiome;
Biome *mToBiome;
};

```
#### LayerFilters::River::operator()::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 289859 */
struct LayerFilters::River::operator()::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### LayerFilters::RiverInit
```cpp
/* 38110 */
struct LayerFilters::RiverInit
{
std::vector<Biome *> mNoRiverBiomes;
};

```
#### LayerFilters::Shore
```cpp
/* 38507 */
struct LayerFilters::Shore
{
Biome *mDefaultShore;
std::vector<Biome *> mOceanBiomes;
};

```
#### LayerFilters::`anonymous namespace'::BackCompatSorter
```cpp
/* 289812 */
struct LayerFilters::`anonymous namespace'::BackCompatSorter
{
__int8 gap0[1];
};

```
#### LayerResult<Biome *>
```cpp
/* 40554 */
struct LayerResult<Biome *>
{
std::unique_ptr<char []> mResult;
};

```
#### LayerResult<BiomeTemperatureCategory>
```cpp
/* 40678 */
struct LayerResult<BiomeTemperatureCategory>
{
std::unique_ptr<char []> mResult;
};

```
#### LayerResult<LayerValues::PreBiome>;
```cpp
/* 40614 */
struct LayerResult<LayerValues::PreBiome>;

```
#### LayerResult<LayerValues::Terrain>;
```cpp
/* 40604 */
struct LayerResult<LayerValues::Terrain>;

```
#### LayerResult<bool>
```cpp
/* 39570 */
struct LayerResult<bool>
{
std::unique_ptr<char []> mResult;
};

```
#### LayerResult<int>
```cpp
/* 40640 */
struct LayerResult<int>
{
std::unique_ptr<char []> mResult;
};

```
#### LayerValues::PreBiome
```cpp
/* 39254 */
struct LayerValues::PreBiome
{
LayerValues::Terrain mTerrain;
BiomeTemperatureCategory mTemperature;
};

```
#### LayerZooms::ZoomBase<1,LayerZooms::Alignment::Min>
```cpp
/* 37687 */
struct LayerZooms::ZoomBase<1,LayerZooms::Alignment::Min>
{
__int8 gap0[1];
};

```
#### LayerZooms::ZoomBase<2,LayerZooms::Alignment::Center>
```cpp
/* 38726 */
struct LayerZooms::ZoomBase<2,LayerZooms::Alignment::Center>
{
__int8 gap0[1];
};

```
#### Legacy::WorldConversionReport;
```cpp
/* 45326 */
struct Legacy::WorldConversionReport;

```
#### LegacyBlockPlacementProcessor
```cpp
/* 285980 */
struct LegacyBlockPlacementProcessor
{
float mChance;
Random mRandom;
bool mHasGravity;
const StructurePoolBlockRuleList *mBlockRules;
const StructurePoolBlockTagRuleList *mBlockTagRules;
};

```
#### LegacyPackIdVersion
```cpp
/* 5770 */
struct LegacyPackIdVersion
{
std::string mId;
std::string mVersion;
};

```
#### LegacyPreHillsEdgeTransformation;
```cpp
/* 13151 */
struct LegacyPreHillsEdgeTransformation;

```
#### LegacyStructureActorInfo
```cpp
/* 41836 */
struct LegacyStructureActorInfo
{
Vec3 mPos;
BlockPos mBlockPos;
CompoundTag mTag;
};

```
#### LegacyStructureBlockInfo
```cpp
/* 41823 */
struct LegacyStructureBlockInfo
{
BlockPos mPos;
const Block *mBlock;
const Block *mExtraBlock;
Unique<CompoundTag> mTag;
};

```
#### LegacyStructureBlockPalette
```cpp
/* 41787 */
struct LegacyStructureBlockPalette
{
BlockMap mMapper;
};

```
#### LegacyStructureSettings
```cpp
/* 42198 */
struct LegacyStructureSettings
{
float mIntegrity;
RandomSeed mSeed;
Projection mProjection;
Mirror_0 mMirror;
Rotation_0 mRotation;
bool mIgnoreStructureBlocks;
bool mIgnoreJigsawBlocks;
bool mWaterBelowSeaLevel;
const Block *mIgnoreBlock;
ChunkPos mChunkPos;
BoundingBox mBoundingBox;
std::unordered_map<unsigned char,unsigned char> mSwapAuxValues;
const StructurePoolBlockRuleList *mBlockRules;
const StructurePoolBlockTagRuleList *mBlockTagRules;
};

```
#### LegacyStructureTemplate
```cpp
/* 41786 */
struct LegacyStructureTemplate
{
std::string mAuthor;
BlockPos mSize;
LegacyStructureBlockPalette mPalette;
LegacyStructureBlockPalette mExtraBlockPalette;
std::vector<LegacyStructureBlockInfo> mBlockInfo;
std::vector<LegacyStructureActorInfo> mEntityInfo;
};

```
#### LegacyTradeableComponent
```cpp
/* 44847 */
struct LegacyTradeableComponent
{
bool mAddRecipeOnUpdate;
bool mResetLockedOnFirstTrade;
bool mWillingToBreed;
int mRiches;
int mTradeTier;
int mUpdateMerchantTimer;
Player *mLastPlayerTradeName;
std::unique_ptr<MerchantRecipeList> mOffers;
std::string mDisplayName;
std::vector<int> mTradeRecipeFirstTime;
};

```
#### Level::CompareLevelChunkQueuedSavingElement
```cpp
/* 88085 */
struct Level::CompareLevelChunkQueuedSavingElement
{
__int8 gap0[1];
};

```
#### LevelChunk::_createSubChunk::$31B85587540760296E2FBFD5D423D7F3
```cpp
/* 252865 */
struct LevelChunk::_createSubChunk::$31B85587540760296E2FBFD5D423D7F3
{
LevelChunk *this;
bool initSkyLight;
SubChunkInitMode initBlocks;
size_t idx;
};

```
#### LevelChunk::needsSaving::$0DAA62F87AF08124C8B5CE4526C39CCA
```cpp
/* 252868 */
struct LevelChunk::needsSaving::$0DAA62F87AF08124C8B5CE4526C39CCA
{
bool *shouldSave;
int wait;
int maxWait;
};

```
#### LevelChunk::setSaved::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 252869 */
struct LevelChunk::setSaved::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### LevelChunk::setUnsaved::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 252867 */
struct LevelChunk::setUnsaved::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### LevelChunk::tick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 252866 */
struct LevelChunk::tick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### LevelChunkBlockActorAccessToken
```cpp
/* 35033 */
struct LevelChunkBlockActorAccessToken
{
__int8 gap0[1];
};

```
#### LevelChunkBuilderData
```cpp
/* 34743 */
struct LevelChunkBuilderData
{
SpinLock mChunkGenerationGridMapSpinLock;
std::unordered_map<ChunkPos,std::shared_ptr<LevelChunkGridAreaElement<std::weak_ptr<LevelChunk> > >> mChunkGenerationGridMap;
SpinLock mChunksToAddToProcessingSpinLock;
std::vector<ChunkPos> mChunksToAddToProcessing;
SpinLock mChunksReadyForProcessingSpinLock;
std::unordered_set<ChunkPos> mChunksReadyForProcessing;
std::vector<LevelChunkBuilderData::ChunkReadyForProcessingElement> mChunkSortVector;
std::atomic<int> mChunkGenerationTasksInFlight;
SpinLock mSpawnTasksLock;
};

```
#### LevelChunkFinalDeleter
```cpp
/* 251971 */
struct LevelChunkFinalDeleter
{
__int8 gap0[1];
};

```
#### LevelChunkGarbageCollector
```cpp
/* 34651 */
struct LevelChunkGarbageCollector
{
Dimension *mDimension;
MPMCQueue<std::unique_ptr<LevelChunk,LevelChunkFinalDeleter> > mLevelChunksToDiscard;
std::atomic_size_t mPendingDeletes;
};

```
#### LevelChunkPacket::SubChunkMetadata
```cpp
/* 79949 */
struct LevelChunkPacket::SubChunkMetadata
{
uint64_t blobId;
};

```
#### LevelChunkPhase1Deleter
```cpp
/* 251902 */
struct LevelChunkPhase1Deleter
{
__int8 gap0[1];
};

```
#### LevelDataWrapper
```cpp
/* 87737 */
struct LevelDataWrapper
{
LevelData *mLevelDataFromLevel;
LevelData mLevelDataFromDisk;
};

```
#### LevelDataWrapper_0
```cpp
/* 290628 */
struct LevelDataWrapper_0
{
LevelData_0 *mLevelDataFromLevel;
LevelData_0 mLevelDataFromDisk;
};

```
#### LevelEventListener
```cpp
/* 13237 */
struct LevelEventListener
{
int (**_vptr$LevelEventListener)(void);
};

```
#### LevelSettings
```cpp
/* 5789 */
struct LevelSettings
{
RandomSeed mSeed;
GameType mGameType;
Difficulty mGameDifficulty;
bool mForceGameType;
GeneratorType mGenerator;
bool mAchievementsDisabled;
DimensionType mDimension;
int mTime;
EducationEditionOffer mEducationEditionOffer;
bool mEducationFeaturesEnabled;
bool mImmutableWorld;
float mRainLevel;
float mLightningLevel;
bool mConfirmedPlatformLockedContent;
bool mMultiplayerGameIntent;
bool mLANBroadcastIntent;
Social::GamePublishSetting mXBLBroadcastIntent;
Social::GamePublishSetting mPlatformBroadcastIntent;
bool mCommandsEnabled;
bool mTexturePacksRequired;
bool mHasLockedBehaviorPack;
bool mHasLockedResourcePack;
bool mIsFromLockedTemplate;
bool mUseMsaGamertagsOnly;
bool mOverrideSettings;
bool mBonusChestEnabled;
bool mStartWithMapEnabled;
int mServerChunkTickRange;
bool mForceExperimentalGameplay;
bool mIsFromWorldTemplate;
bool mIsWorldTemplateOptionLocked;
bool mSpawnV1Villagers;
Abilities mDefaultAbilities;
BlockPos mDefaultSpawn;
std::vector<PackInstanceId> mNewWorldBehaviorPackIdentities;
std::vector<PackInstanceId> mNewWorldResourcePackIdentities;
GameRules mGameRules;
BaseGameVersion mBaseGameVersion;
std::optional<EducationLevelSettings> mEducationLevelSettings;
};

```
#### LevelSettings_0
```cpp
/* 80857 */
struct LevelSettings_0
{
RandomSeed_0 mSeed;
GameType mGameType;
Difficulty mGameDifficulty;
bool mForceGameType;
GeneratorType mGenerator;
bool mAchievementsDisabled;
DimensionType mDimension;
int mTime;
EducationEditionOffer mEducationEditionOffer;
bool mEducationFeaturesEnabled;
bool mImmutableWorld;
float mRainLevel;
float mLightningLevel;
bool mConfirmedPlatformLockedContent;
bool mMultiplayerGameIntent;
bool mLANBroadcastIntent;
Social::GamePublishSetting mXBLBroadcastIntent;
Social::GamePublishSetting mPlatformBroadcastIntent;
bool mCommandsEnabled;
bool mTexturePacksRequired;
bool mHasLockedBehaviorPack;
bool mHasLockedResourcePack;
bool mIsFromLockedTemplate;
bool mUseMsaGamertagsOnly;
bool mOverrideSettings;
bool mBonusChestEnabled;
bool mStartWithMapEnabled;
int mServerChunkTickRange;
bool mForceExperimentalGameplay;
bool mIsFromWorldTemplate;
bool mIsWorldTemplateOptionLocked;
bool mSpawnV1Villagers;
Abilities mDefaultAbilities;
BlockPos mDefaultSpawn;
std::vector<PackInstanceId> mNewWorldBehaviorPackIdentities;
std::vector<PackInstanceId> mNewWorldResourcePackIdentities;
GameRules mGameRules;
BaseGameVersion mBaseGameVersion;
std::optional<EducationLevelSettings> mEducationLevelSettings;
};

```
#### LevelSoundEventMap
```cpp
/* 226744 */
struct LevelSoundEventMap
{
__int8 gap0[1];
};

```
#### LevelStorage
```cpp
/* 4390 */
struct LevelStorage
{
int (**_vptr$LevelStorage)(void);
};

```
#### LevelStorage::Batch
```cpp
/* 290639 */
struct LevelStorage::Batch
{
int (**_vptr$Batch)(void);
};

```
#### LevelStorageObserver
```cpp
/* 462334 */
struct LevelStorageObserver
{
std::function<void (const std::string &)> mOnSaveCallback;
};

```
#### LevelStorageSource
```cpp
/* 290483 */
struct LevelStorageSource
{
int (**_vptr$LevelStorageSource)(void);
};

```
#### LevelSummary
```cpp
/* 5806 */
struct LevelSummary
{
std::string mId;
std::string mName;
time_t mLastPlayed;
GameType mGameType;
Difficulty mGameDifficulty;
int mSeed;
int mNetworkProtocolVersion;
uint64_t mSizeOnDisk;
bool mConfirmedPlatformLockedContent;
bool mLANBroadcastIntent;
Social::GamePublishSetting mXBLBroadcastIntent;
bool mCommandsEnabled;
EducationEditionOffer mEducationEditionOffer;
GameVersion mLastLoadedGameVersion;
GameVersion mMinCompatibleClientVersion;
StorageVersion mStorageVersion;
Core::HeapPathBuffer mWorldIconPath;
Core::HeapPathBuffer mWorldIconTargetPath;
ContentIdentity mPremiumTemplateContentIdentity;
};

```
#### LinuxStackTrace
```cpp
/* 294350 */
struct LinuxStackTrace
{
__int8 gap0[1];
};

```
#### ListTagFloatAdder
```cpp
/* 61979 */
struct ListTagFloatAdder
{
Unique<ListTag> mTag;
};

```
#### ListTagIntAdder
```cpp
/* 61980 */
struct ListTagIntAdder
{
Unique<ListTag> mTag;
};

```
#### ListedFeatures;
```cpp
/* 198708 */
struct ListedFeatures;

```
#### ListenerInfo
```cpp
/* 176399 */
struct ListenerInfo
{
std::function<void (const Block &)> mCallback;
Vec3 mPosition;
float mRadiusSqr;
};

```
#### Literal
```cpp
/* 80980 */
struct Literal
{
__int8 gap0[1];
};

```
#### Llama::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124188 */
struct Llama::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### LoadedResourceData
```cpp
/* 85757 */
struct LoadedResourceData
{
int mIndex;
std::string mContent;
};

```
#### LocalConnectivitySystem
```cpp
/* 421604 */
struct LocalConnectivitySystem
{
LocalConnector *mHostConnector;
};

```
#### LocalConnector::ConnectionCallbacks
```cpp
/* 63503 */
struct LocalConnector::ConnectionCallbacks
{
int (**_vptr$ConnectionCallbacks)(void);
};

```
#### LocalConnector::LocalConnection
```cpp
/* 421438 */
struct LocalConnector::LocalConnection
{
LocalConnector *mConnector;
NetworkIdentifier mId;
};

```
#### LocalPlayer;
```cpp
/* 13198 */
struct LocalPlayer;

```
#### Localization
```cpp
/* 60176 */
struct Localization
{
bool mCommaSeperator;
const std::string mCode;
Localization::Map mStrings;
};

```
#### Lockless::WeakAtomic<SPSCQueue<BatchedNetworkPeer::DataCallback,512>::Block *>
```cpp
/* 421197 */
struct Lockless::WeakAtomic<SPSCQueue<BatchedNetworkPeer::DataCallback,512>::Block *>
{
std::atomic<SPSCQueue<BatchedNetworkPeer::DataCallback,512>::Block *> mValue;
};

```
#### LogSettingsUpdater;
```cpp
/* 3252 */
struct LogSettingsUpdater;

```
#### LookAtComponent
```cpp
/* 56822 */
struct LookAtComponent
{
bool mSetTarget;
float mSearchRadius;
bool mAllowInvulnerable;
int mCoolingTime;
};

```
#### LookAtDefinition
```cpp
/* 56877 */
struct LookAtDefinition
{
bool mSetTarget;
float mSearchRadius;
bool mAllowInvulnerable;
FloatRange mLookCooldown;
ActorFilterGroup mFilter;
DefinitionTrigger mOnLookAt;
};

```
#### LookControlComponent
```cpp
/* 56982 */
struct LookControlComponent
{
bool mHasWantedPosition;
bool mHasWantedRotation;
float mYMax;
float mXMax;
Vec3 mWantedPosition;
Vec3 mWantedRotation;
Unique<LookControl> mLookControl;
};

```
#### LoopingSoundState
```cpp
/* 86380 */
struct LoopingSoundState
{
glm::vec3 position;
float pitch;
float volume;
};

```
#### LootComponent
```cpp
/* 223099 */
struct LootComponent
{
BlockLegacy *mBlockLegacy;
std::string mLootTable;
};

```
#### LootItemCondition
```cpp
/* 104685 */
struct LootItemCondition
{
int (**_vptr$LootItemCondition)(void);
};

```
#### LootItemConditions
```cpp
/* 463986 */
struct LootItemConditions
{
__int8 gap0[1];
};

```
#### LootItemFunction
```cpp
/* 46424 */
struct LootItemFunction
{
int (**_vptr$LootItemFunction)(void);
std::vector<std::unique_ptr<LootItemCondition>> mPredicates;
};

```
#### LootItemFunctions
```cpp
/* 477577 */
struct LootItemFunctions
{
__int8 gap0[1];
};

```
#### LootPool
```cpp
/* 104643 */
struct LootPool
{
std::vector<std::unique_ptr<LootPoolEntry>> mEntries;
std::vector<std::unique_ptr<LootItemCondition>> mConditions;
Unique<LootPoolTiers> mTiers;
RandomValueBounds mRolls;
RandomValueBounds mBonusRolls;
};

```
#### LootPoolEntry
```cpp
/* 104664 */
struct LootPoolEntry
{
int (**_vptr$LootPoolEntry)(void);
int mWeight;
int mQuality;
std::vector<std::unique_ptr<LootItemCondition>> mConditions;
Unique<LootPoolEntry> mSubTable;
};

```
#### LootPoolTiers
```cpp
/* 104695 */
struct LootPoolTiers
{
int mRangeForInitialTier;
int mBonusRolls;
float mBonusRollChance;
};

```
#### LootTable
```cpp
/* 46133 */
struct LootTable
{
std::string mDir;
std::vector<std::unique_ptr<LootPool>> mPools;
};

```
#### LootTables
```cpp
/* 88306 */
struct LootTables
{
LootTableMap mLootTables;
Bedrock::Threading::Mutex mLootTableMutex;
};

```
#### LONG_DOUBLE_16
```cpp
/* 486702 */
struct LONG_DOUBLE_16
{
_TBYTE value;
char padding[6];
};

```
#### LabTableReactionComponent
```cpp
/* 238069 */
struct LabTableReactionComponent
{
int (**_vptr$LabTableReactionComponent)(void);
};

```
#### LargeCaveFeature
```cpp
/* 40160 */
struct LargeCaveFeature
{
int (**_vptr$LargeCaveFeature)(void);
};

```
#### LargeHellCaveFeature
```cpp
/* 36894 */
struct LargeHellCaveFeature
{
__int8 gap0[1];
};

```
#### LayerDetails::BufferAccessor<Biome *>
```cpp
/* 39874 */
struct LayerDetails::BufferAccessor<Biome *>
{
char *mStorage;
size_t mCount;
};

```
#### LayerDetails::BufferAccessor<Biome *>::TypedBits
```cpp
/* 40543 */
struct LayerDetails::BufferAccessor<Biome *>::TypedBits
{
char *mLocation;
};

```
#### LayerDetails::BufferAccessor<BiomeTemperatureCategory>
```cpp
/* 40026 */
struct LayerDetails::BufferAccessor<BiomeTemperatureCategory>
{
char *mStorage;
size_t mCount;
};

```
#### LayerDetails::BufferAccessor<BiomeTemperatureCategory>::TypedBits
```cpp
/* 40550 */
struct LayerDetails::BufferAccessor<BiomeTemperatureCategory>::TypedBits
{
char *mLocation;
};

```
#### LayerDetails::BufferAccessor<LayerValues::PreBiome>
```cpp
/* 39828 */
struct LayerDetails::BufferAccessor<LayerValues::PreBiome>
{
char *mStorage;
size_t mCount;
};

```
#### LayerDetails::BufferAccessor<LayerValues::PreBiome>::TypedBits
```cpp
/* 40539 */
struct LayerDetails::BufferAccessor<LayerValues::PreBiome>::TypedBits
{
char *mLocation;
};

```
#### LayerDetails::BufferAccessor<LayerValues::Terrain>
```cpp
/* 39752 */
struct LayerDetails::BufferAccessor<LayerValues::Terrain>
{
char *mStorage;
size_t mCount;
};

```
#### LayerDetails::BufferAccessor<LayerValues::Terrain>::TypedBits
```cpp
/* 40537 */
struct LayerDetails::BufferAccessor<LayerValues::Terrain>::TypedBits
{
char *mLocation;
};

```
#### LayerDetails::BufferAccessor<bool>
```cpp
/* 39932 */
struct LayerDetails::BufferAccessor<bool>
{
char *mStorage;
size_t mCount;
};

```
#### LayerDetails::BufferAccessor<bool>::TypedBits
```cpp
/* 40547 */
struct LayerDetails::BufferAccessor<bool>::TypedBits
{
char *mLocation;
};

```
#### LayerDetails::BufferAccessor<char>
```cpp
/* 39751 */
struct LayerDetails::BufferAccessor<char>
{
char *mStorage;
size_t mCount;
};

```
#### LayerDetails::BufferAccessor<char>::TypedBits;
```cpp
/* 40552 */
struct LayerDetails::BufferAccessor<char>::TypedBits;

```
#### LayerDetails::BufferAccessor<int>
```cpp
/* 39906 */
struct LayerDetails::BufferAccessor<int>
{
char *mStorage;
size_t mCount;
};

```
#### LayerDetails::BufferAccessor<int>::TypedBits
```cpp
/* 40545 */
struct LayerDetails::BufferAccessor<int>::TypedBits
{
char *mLocation;
};

```
#### LayerDetails::LayerBase
```cpp
/* 37190 */
struct LayerDetails::LayerBase
{
int (**_vptr$LayerBase)(void);
int64_t mSeed;
int64_t mSeedMixup;
};

```
#### LayerDetails::NeighborhoodReader<Biome *,0,0>
```cpp
/* 40546 */
struct LayerDetails::NeighborhoodReader<Biome *,0,0>
{
const LayerDetails::BufferAccessor<Biome *> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::NeighborhoodReader<Biome *,1,1>
```cpp
/* 40544 */
struct LayerDetails::NeighborhoodReader<Biome *,1,1>
{
const LayerDetails::BufferAccessor<Biome *> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::NeighborhoodReader<BiomeTemperatureCategory,1,1>
```cpp
/* 40551 */
struct LayerDetails::NeighborhoodReader<BiomeTemperatureCategory,1,1>
{
const LayerDetails::BufferAccessor<BiomeTemperatureCategory> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::NeighborhoodReader<LayerValues::PreBiome,0,0>
```cpp
/* 40542 */
struct LayerDetails::NeighborhoodReader<LayerValues::PreBiome,0,0>
{
const LayerDetails::BufferAccessor<LayerValues::PreBiome> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::NeighborhoodReader<LayerValues::PreBiome,1,1>
```cpp
/* 40541 */
struct LayerDetails::NeighborhoodReader<LayerValues::PreBiome,1,1>
{
const LayerDetails::BufferAccessor<LayerValues::PreBiome> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::NeighborhoodReader<LayerValues::Terrain,0,0>
```cpp
/* 40540 */
struct LayerDetails::NeighborhoodReader<LayerValues::Terrain,0,0>
{
const LayerDetails::BufferAccessor<LayerValues::Terrain> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::NeighborhoodReader<LayerValues::Terrain,1,1>
```cpp
/* 40538 */
struct LayerDetails::NeighborhoodReader<LayerValues::Terrain,1,1>
{
const LayerDetails::BufferAccessor<LayerValues::Terrain> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::NeighborhoodReader<bool,1,1>
```cpp
/* 40549 */
struct LayerDetails::NeighborhoodReader<bool,1,1>
{
const LayerDetails::BufferAccessor<bool> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::NeighborhoodReader<int,1,1>
```cpp
/* 40548 */
struct LayerDetails::NeighborhoodReader<int,1,1>
{
const LayerDetails::BufferAccessor<int> *mSourceData;
int32_t mTopLeft;
int32_t mW;
};

```
#### LayerDetails::RandomProviderT<(lambda at _Minecraftpe_handheld_project_dedicated_server_______src_common_world_level_newbiome_LayerDetails_h:221:34)>
```cpp
/* 37665 */
struct LayerDetails::RandomProviderT<(lambda at _Minecraftpe_handheld_project_dedicated_server_______src_common_world_level_newbiome_LayerDetails_h:221:34)>
{
$9B9F62DABB3B3036AEF15BA6ABCB0C35 mNextRandom;
int64_t mRval;
};

```
#### LayerDetails::Storage
```cpp
/* 39750 */
struct LayerDetails::Storage
{
size_t mReadableBytes;
size_t mWriteableBytes;
std::unique_ptr<char []> mReadStorage;
std::unique_ptr<char []> mWriteStorage;
};

```
#### LayerDetails::TransferData<char>;
```cpp
/* 40553 */
struct LayerDetails::TransferData<char>;

```
#### LayerFilters::AddBiomeIsland
```cpp
/* 38482 */
struct LayerFilters::AddBiomeIsland
{
Biome *mDefaultIsland;
Biome *mSpecialIsland;
std::vector<Biome *> mShallowOceanBiomes;
};

```
#### LayerFilters::AddMushroomIsland
```cpp
/* 38027 */
struct LayerFilters::AddMushroomIsland
{
Biome *mMushroomBiome;
const BiomeRegistry *mBiomeRegistry;
};

```
#### LayerFilters::BiomeInit
```cpp
/* 37952 */
struct LayerFilters::BiomeInit
{
Biome *mFallbackBiome;
Biome *mDefaultOcean;
std::vector<std::pair<Biome *,unsigned int>> mRegularBiomes[5];
std::vector<std::pair<Biome *,unsigned int>> mSpecialBiomes[5];
};

```
#### LayerFilters::FilterBase<1,1,Biome *,Biome *>
```cpp
/* 38238 */
struct LayerFilters::FilterBase<1,1,Biome *,Biome *>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<1,1,Biome *,LayerValues::PreBiome>
```cpp
/* 37953 */
struct LayerFilters::FilterBase<1,1,Biome *,LayerValues::PreBiome>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<1,1,LayerValues::PreBiome,LayerValues::PreBiome>
```cpp
/* 37903 */
struct LayerFilters::FilterBase<1,1,LayerValues::PreBiome,LayerValues::PreBiome>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<1,1,LayerValues::PreBiome,LayerValues::Terrain>
```cpp
/* 37781 */
struct LayerFilters::FilterBase<1,1,LayerValues::PreBiome,LayerValues::Terrain>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<1,1,int,Biome *>
```cpp
/* 38111 */
struct LayerFilters::FilterBase<1,1,int,Biome *>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<3,3,Biome *,Biome *>
```cpp
/* 38028 */
struct LayerFilters::FilterBase<3,3,Biome *,Biome *>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<3,3,BiomeTemperatureCategory,BiomeTemperatureCategory>
```cpp
/* 38640 */
struct LayerFilters::FilterBase<3,3,BiomeTemperatureCategory,BiomeTemperatureCategory>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<3,3,LayerValues::PreBiome,LayerValues::PreBiome>
```cpp
/* 37833 */
struct LayerFilters::FilterBase<3,3,LayerValues::PreBiome,LayerValues::PreBiome>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<3,3,LayerValues::Terrain,LayerValues::Terrain>
```cpp
/* 37711 */
struct LayerFilters::FilterBase<3,3,LayerValues::Terrain,LayerValues::Terrain>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<3,3,bool,bool>
```cpp
/* 38214 */
struct LayerFilters::FilterBase<3,3,bool,bool>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilterBase<3,3,bool,int>
```cpp
/* 38174 */
struct LayerFilters::FilterBase<3,3,bool,int>
{
__int8 gap0[1];
};

```
#### LayerFilters::FilteredTransformation<FilteredTransformationAttributes<LegacyPreHillsEdgeTransformation> >
```cpp
/* 38418 */
struct LayerFilters::FilteredTransformation<FilteredTransformationAttributes<LegacyPreHillsEdgeTransformation> >
{
const TagRegistry *mTagRegistry;
};

```
#### LayerFilters::FilteredTransformation<FilteredTransformationAttributes<PostShoreEdgeTransformation> >
```cpp
/* 38529 */
struct LayerFilters::FilteredTransformation<FilteredTransformationAttributes<PostShoreEdgeTransformation> >
{
const TagRegistry *mTagRegistry;
};

```
#### LayerFilters::FilteredTransformation<FilteredTransformationAttributes<PreHillsEdgeTransformation> >
```cpp
/* 38393 */
struct LayerFilters::FilteredTransformation<FilteredTransformationAttributes<PreHillsEdgeTransformation> >
{
const TagRegistry *mTagRegistry;
};

```
#### LayerFilters::PromoteCenter
```cpp
/* 38051 */
struct LayerFilters::PromoteCenter
{
Biome *mFrom;
Biome *mTo;
};

```
#### LayerFilters::RareBiomeSpot
```cpp
/* 38237 */
struct LayerFilters::RareBiomeSpot
{
uint32_t mChance;
Biome *mFromBiome;
Biome *mToBiome;
};

```
#### LayerFilters::River::operator()::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 289859 */
struct LayerFilters::River::operator()::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### LayerFilters::RiverInit
```cpp
/* 38110 */
struct LayerFilters::RiverInit
{
std::vector<Biome *> mNoRiverBiomes;
};

```
#### LayerFilters::Shore
```cpp
/* 38507 */
struct LayerFilters::Shore
{
Biome *mDefaultShore;
std::vector<Biome *> mOceanBiomes;
};

```
#### LayerFilters::`anonymous namespace'::BackCompatSorter
```cpp
/* 289812 */
struct LayerFilters::`anonymous namespace'::BackCompatSorter
{
__int8 gap0[1];
};

```
#### LayerResult<Biome *>
```cpp
/* 40554 */
struct LayerResult<Biome *>
{
std::unique_ptr<char []> mResult;
};

```
#### LayerResult<BiomeTemperatureCategory>
```cpp
/* 40678 */
struct LayerResult<BiomeTemperatureCategory>
{
std::unique_ptr<char []> mResult;
};

```
#### LayerResult<LayerValues::PreBiome>;
```cpp
/* 40614 */
struct LayerResult<LayerValues::PreBiome>;

```
#### LayerResult<LayerValues::Terrain>;
```cpp
/* 40604 */
struct LayerResult<LayerValues::Terrain>;

```
#### LayerResult<bool>
```cpp
/* 39570 */
struct LayerResult<bool>
{
std::unique_ptr<char []> mResult;
};

```
#### LayerResult<int>
```cpp
/* 40640 */
struct LayerResult<int>
{
std::unique_ptr<char []> mResult;
};

```
#### LayerValues::PreBiome
```cpp
/* 39254 */
struct LayerValues::PreBiome
{
LayerValues::Terrain mTerrain;
BiomeTemperatureCategory mTemperature;
};

```
#### LayerZooms::ZoomBase<1,LayerZooms::Alignment::Min>
```cpp
/* 37687 */
struct LayerZooms::ZoomBase<1,LayerZooms::Alignment::Min>
{
__int8 gap0[1];
};

```
#### LayerZooms::ZoomBase<2,LayerZooms::Alignment::Center>
```cpp
/* 38726 */
struct LayerZooms::ZoomBase<2,LayerZooms::Alignment::Center>
{
__int8 gap0[1];
};

```
#### Legacy::WorldConversionReport;
```cpp
/* 45326 */
struct Legacy::WorldConversionReport;

```
#### LegacyBlockPlacementProcessor
```cpp
/* 285980 */
struct LegacyBlockPlacementProcessor
{
float mChance;
Random mRandom;
bool mHasGravity;
const StructurePoolBlockRuleList *mBlockRules;
const StructurePoolBlockTagRuleList *mBlockTagRules;
};

```
#### LegacyPackIdVersion
```cpp
/* 5770 */
struct LegacyPackIdVersion
{
std::string mId;
std::string mVersion;
};

```
#### LegacyPreHillsEdgeTransformation;
```cpp
/* 13151 */
struct LegacyPreHillsEdgeTransformation;

```
#### LegacyStructureActorInfo
```cpp
/* 41836 */
struct LegacyStructureActorInfo
{
Vec3 mPos;
BlockPos mBlockPos;
CompoundTag mTag;
};

```
#### LegacyStructureBlockInfo
```cpp
/* 41823 */
struct LegacyStructureBlockInfo
{
BlockPos mPos;
const Block *mBlock;
const Block *mExtraBlock;
Unique<CompoundTag> mTag;
};

```
#### LegacyStructureBlockPalette
```cpp
/* 41787 */
struct LegacyStructureBlockPalette
{
BlockMap mMapper;
};

```
#### LegacyStructureSettings
```cpp
/* 42198 */
struct LegacyStructureSettings
{
float mIntegrity;
RandomSeed mSeed;
Projection mProjection;
Mirror_0 mMirror;
Rotation_0 mRotation;
bool mIgnoreStructureBlocks;
bool mIgnoreJigsawBlocks;
bool mWaterBelowSeaLevel;
const Block *mIgnoreBlock;
ChunkPos mChunkPos;
BoundingBox mBoundingBox;
std::unordered_map<unsigned char,unsigned char> mSwapAuxValues;
const StructurePoolBlockRuleList *mBlockRules;
const StructurePoolBlockTagRuleList *mBlockTagRules;
};

```
#### LegacyStructureTemplate
```cpp
/* 41786 */
struct LegacyStructureTemplate
{
std::string mAuthor;
BlockPos mSize;
LegacyStructureBlockPalette mPalette;
LegacyStructureBlockPalette mExtraBlockPalette;
std::vector<LegacyStructureBlockInfo> mBlockInfo;
std::vector<LegacyStructureActorInfo> mEntityInfo;
};

```
#### LegacyTradeableComponent
```cpp
/* 44847 */
struct LegacyTradeableComponent
{
bool mAddRecipeOnUpdate;
bool mResetLockedOnFirstTrade;
bool mWillingToBreed;
int mRiches;
int mTradeTier;
int mUpdateMerchantTimer;
Player *mLastPlayerTradeName;
std::unique_ptr<MerchantRecipeList> mOffers;
std::string mDisplayName;
std::vector<int> mTradeRecipeFirstTime;
};

```
#### Level::CompareLevelChunkQueuedSavingElement
```cpp
/* 88085 */
struct Level::CompareLevelChunkQueuedSavingElement
{
__int8 gap0[1];
};

```
#### LevelChunk::_createSubChunk::$31B85587540760296E2FBFD5D423D7F3
```cpp
/* 252865 */
struct LevelChunk::_createSubChunk::$31B85587540760296E2FBFD5D423D7F3
{
LevelChunk *this;
bool initSkyLight;
SubChunkInitMode initBlocks;
size_t idx;
};

```
#### LevelChunk::needsSaving::$0DAA62F87AF08124C8B5CE4526C39CCA
```cpp
/* 252868 */
struct LevelChunk::needsSaving::$0DAA62F87AF08124C8B5CE4526C39CCA
{
bool *shouldSave;
int wait;
int maxWait;
};

```
#### LevelChunk::setSaved::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 252869 */
struct LevelChunk::setSaved::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### LevelChunk::setUnsaved::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 252867 */
struct LevelChunk::setUnsaved::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### LevelChunk::tick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 252866 */
struct LevelChunk::tick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### LevelChunkBlockActorAccessToken
```cpp
/* 35033 */
struct LevelChunkBlockActorAccessToken
{
__int8 gap0[1];
};

```
#### LevelChunkBuilderData
```cpp
/* 34743 */
struct LevelChunkBuilderData
{
SpinLock mChunkGenerationGridMapSpinLock;
std::unordered_map<ChunkPos,std::shared_ptr<LevelChunkGridAreaElement<std::weak_ptr<LevelChunk> > >> mChunkGenerationGridMap;
SpinLock mChunksToAddToProcessingSpinLock;
std::vector<ChunkPos> mChunksToAddToProcessing;
SpinLock mChunksReadyForProcessingSpinLock;
std::unordered_set<ChunkPos> mChunksReadyForProcessing;
std::vector<LevelChunkBuilderData::ChunkReadyForProcessingElement> mChunkSortVector;
std::atomic<int> mChunkGenerationTasksInFlight;
SpinLock mSpawnTasksLock;
};

```
#### LevelChunkFinalDeleter
```cpp
/* 251971 */
struct LevelChunkFinalDeleter
{
__int8 gap0[1];
};

```
#### LevelChunkGarbageCollector
```cpp
/* 34651 */
struct LevelChunkGarbageCollector
{
Dimension *mDimension;
MPMCQueue<std::unique_ptr<LevelChunk,LevelChunkFinalDeleter> > mLevelChunksToDiscard;
std::atomic_size_t mPendingDeletes;
};

```
#### LevelChunkPacket::SubChunkMetadata
```cpp
/* 79949 */
struct LevelChunkPacket::SubChunkMetadata
{
uint64_t blobId;
};

```
#### LevelChunkPhase1Deleter
```cpp
/* 251902 */
struct LevelChunkPhase1Deleter
{
__int8 gap0[1];
};

```
#### LevelDataWrapper
```cpp
/* 87737 */
struct LevelDataWrapper
{
LevelData *mLevelDataFromLevel;
LevelData mLevelDataFromDisk;
};

```
#### LevelDataWrapper_0
```cpp
/* 290628 */
struct LevelDataWrapper_0
{
LevelData_0 *mLevelDataFromLevel;
LevelData_0 mLevelDataFromDisk;
};

```
#### LevelEventListener
```cpp
/* 13237 */
struct LevelEventListener
{
int (**_vptr$LevelEventListener)(void);
};

```
#### LevelSettings
```cpp
/* 5789 */
struct LevelSettings
{
RandomSeed mSeed;
GameType mGameType;
Difficulty mGameDifficulty;
bool mForceGameType;
GeneratorType mGenerator;
bool mAchievementsDisabled;
DimensionType mDimension;
int mTime;
EducationEditionOffer mEducationEditionOffer;
bool mEducationFeaturesEnabled;
bool mImmutableWorld;
float mRainLevel;
float mLightningLevel;
bool mConfirmedPlatformLockedContent;
bool mMultiplayerGameIntent;
bool mLANBroadcastIntent;
Social::GamePublishSetting mXBLBroadcastIntent;
Social::GamePublishSetting mPlatformBroadcastIntent;
bool mCommandsEnabled;
bool mTexturePacksRequired;
bool mHasLockedBehaviorPack;
bool mHasLockedResourcePack;
bool mIsFromLockedTemplate;
bool mUseMsaGamertagsOnly;
bool mOverrideSettings;
bool mBonusChestEnabled;
bool mStartWithMapEnabled;
int mServerChunkTickRange;
bool mForceExperimentalGameplay;
bool mIsFromWorldTemplate;
bool mIsWorldTemplateOptionLocked;
bool mSpawnV1Villagers;
Abilities mDefaultAbilities;
BlockPos mDefaultSpawn;
std::vector<PackInstanceId> mNewWorldBehaviorPackIdentities;
std::vector<PackInstanceId> mNewWorldResourcePackIdentities;
GameRules mGameRules;
BaseGameVersion mBaseGameVersion;
std::optional<EducationLevelSettings> mEducationLevelSettings;
};

```
#### LevelSettings_0
```cpp
/* 80857 */
struct LevelSettings_0
{
RandomSeed_0 mSeed;
GameType mGameType;
Difficulty mGameDifficulty;
bool mForceGameType;
GeneratorType mGenerator;
bool mAchievementsDisabled;
DimensionType mDimension;
int mTime;
EducationEditionOffer mEducationEditionOffer;
bool mEducationFeaturesEnabled;
bool mImmutableWorld;
float mRainLevel;
float mLightningLevel;
bool mConfirmedPlatformLockedContent;
bool mMultiplayerGameIntent;
bool mLANBroadcastIntent;
Social::GamePublishSetting mXBLBroadcastIntent;
Social::GamePublishSetting mPlatformBroadcastIntent;
bool mCommandsEnabled;
bool mTexturePacksRequired;
bool mHasLockedBehaviorPack;
bool mHasLockedResourcePack;
bool mIsFromLockedTemplate;
bool mUseMsaGamertagsOnly;
bool mOverrideSettings;
bool mBonusChestEnabled;
bool mStartWithMapEnabled;
int mServerChunkTickRange;
bool mForceExperimentalGameplay;
bool mIsFromWorldTemplate;
bool mIsWorldTemplateOptionLocked;
bool mSpawnV1Villagers;
Abilities mDefaultAbilities;
BlockPos mDefaultSpawn;
std::vector<PackInstanceId> mNewWorldBehaviorPackIdentities;
std::vector<PackInstanceId> mNewWorldResourcePackIdentities;
GameRules mGameRules;
BaseGameVersion mBaseGameVersion;
std::optional<EducationLevelSettings> mEducationLevelSettings;
};

```
#### LevelSoundEventMap
```cpp
/* 226744 */
struct LevelSoundEventMap
{
__int8 gap0[1];
};

```
#### LevelStorage
```cpp
/* 4390 */
struct LevelStorage
{
int (**_vptr$LevelStorage)(void);
};

```
#### LevelStorage::Batch
```cpp
/* 290639 */
struct LevelStorage::Batch
{
int (**_vptr$Batch)(void);
};

```
#### LevelStorageObserver
```cpp
/* 462334 */
struct LevelStorageObserver
{
std::function<void (const std::string &)> mOnSaveCallback;
};

```
#### LevelStorageSource
```cpp
/* 290483 */
struct LevelStorageSource
{
int (**_vptr$LevelStorageSource)(void);
};

```
#### LevelSummary
```cpp
/* 5806 */
struct LevelSummary
{
std::string mId;
std::string mName;
time_t mLastPlayed;
GameType mGameType;
Difficulty mGameDifficulty;
int mSeed;
int mNetworkProtocolVersion;
uint64_t mSizeOnDisk;
bool mConfirmedPlatformLockedContent;
bool mLANBroadcastIntent;
Social::GamePublishSetting mXBLBroadcastIntent;
bool mCommandsEnabled;
EducationEditionOffer mEducationEditionOffer;
GameVersion mLastLoadedGameVersion;
GameVersion mMinCompatibleClientVersion;
StorageVersion mStorageVersion;
Core::HeapPathBuffer mWorldIconPath;
Core::HeapPathBuffer mWorldIconTargetPath;
ContentIdentity mPremiumTemplateContentIdentity;
};

```
#### LinuxStackTrace
```cpp
/* 294350 */
struct LinuxStackTrace
{
__int8 gap0[1];
};

```
#### ListTagFloatAdder
```cpp
/* 61979 */
struct ListTagFloatAdder
{
Unique<ListTag> mTag;
};

```
#### ListTagIntAdder
```cpp
/* 61980 */
struct ListTagIntAdder
{
Unique<ListTag> mTag;
};

```
#### ListedFeatures;
```cpp
/* 198708 */
struct ListedFeatures;

```
#### ListenerInfo
```cpp
/* 176399 */
struct ListenerInfo
{
std::function<void (const Block &)> mCallback;
Vec3 mPosition;
float mRadiusSqr;
};

```
#### Literal
```cpp
/* 80980 */
struct Literal
{
__int8 gap0[1];
};

```
#### Llama::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124188 */
struct Llama::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### LoadedResourceData
```cpp
/* 85757 */
struct LoadedResourceData
{
int mIndex;
std::string mContent;
};

```
#### LocalConnectivitySystem
```cpp
/* 421604 */
struct LocalConnectivitySystem
{
LocalConnector *mHostConnector;
};

```
#### LocalConnector::ConnectionCallbacks
```cpp
/* 63503 */
struct LocalConnector::ConnectionCallbacks
{
int (**_vptr$ConnectionCallbacks)(void);
};

```
#### LocalConnector::LocalConnection
```cpp
/* 421438 */
struct LocalConnector::LocalConnection
{
LocalConnector *mConnector;
NetworkIdentifier mId;
};

```
#### LocalPlayer;
```cpp
/* 13198 */
struct LocalPlayer;

```
#### Localization
```cpp
/* 60176 */
struct Localization
{
bool mCommaSeperator;
const std::string mCode;
Localization::Map mStrings;
};

```
#### Lockless::WeakAtomic<SPSCQueue<BatchedNetworkPeer::DataCallback,512>::Block *>
```cpp
/* 421197 */
struct Lockless::WeakAtomic<SPSCQueue<BatchedNetworkPeer::DataCallback,512>::Block *>
{
std::atomic<SPSCQueue<BatchedNetworkPeer::DataCallback,512>::Block *> mValue;
};

```
#### LogSettingsUpdater;
```cpp
/* 3252 */
struct LogSettingsUpdater;

```
#### LookAtComponent
```cpp
/* 56822 */
struct LookAtComponent
{
bool mSetTarget;
float mSearchRadius;
bool mAllowInvulnerable;
int mCoolingTime;
};

```
#### LookAtDefinition
```cpp
/* 56877 */
struct LookAtDefinition
{
bool mSetTarget;
float mSearchRadius;
bool mAllowInvulnerable;
FloatRange mLookCooldown;
ActorFilterGroup mFilter;
DefinitionTrigger mOnLookAt;
};

```
#### LookControlComponent
```cpp
/* 56982 */
struct LookControlComponent
{
bool mHasWantedPosition;
bool mHasWantedRotation;
float mYMax;
float mXMax;
Vec3 mWantedPosition;
Vec3 mWantedRotation;
Unique<LookControl> mLookControl;
};

```
#### LoopingSoundState
```cpp
/* 86380 */
struct LoopingSoundState
{
glm::vec3 position;
float pitch;
float volume;
};

```
#### LootComponent
```cpp
/* 223099 */
struct LootComponent
{
BlockLegacy *mBlockLegacy;
std::string mLootTable;
};

```
#### LootItemCondition
```cpp
/* 104685 */
struct LootItemCondition
{
int (**_vptr$LootItemCondition)(void);
};

```
#### LootItemConditions
```cpp
/* 463986 */
struct LootItemConditions
{
__int8 gap0[1];
};

```
#### LootItemFunction
```cpp
/* 46424 */
struct LootItemFunction
{
int (**_vptr$LootItemFunction)(void);
std::vector<std::unique_ptr<LootItemCondition>> mPredicates;
};

```
#### LootItemFunctions
```cpp
/* 477577 */
struct LootItemFunctions
{
__int8 gap0[1];
};

```
#### LootPool
```cpp
/* 104643 */
struct LootPool
{
std::vector<std::unique_ptr<LootPoolEntry>> mEntries;
std::vector<std::unique_ptr<LootItemCondition>> mConditions;
Unique<LootPoolTiers> mTiers;
RandomValueBounds mRolls;
RandomValueBounds mBonusRolls;
};

```
#### LootPoolEntry
```cpp
/* 104664 */
struct LootPoolEntry
{
int (**_vptr$LootPoolEntry)(void);
int mWeight;
int mQuality;
std::vector<std::unique_ptr<LootItemCondition>> mConditions;
Unique<LootPoolEntry> mSubTable;
};

```
#### LootPoolTiers
```cpp
/* 104695 */
struct LootPoolTiers
{
int mRangeForInitialTier;
int mBonusRolls;
float mBonusRollChance;
};

```
#### LootTable
```cpp
/* 46133 */
struct LootTable
{
std::string mDir;
std::vector<std::unique_ptr<LootPool>> mPools;
};

```
#### LootTables
```cpp
/* 88306 */
struct LootTables
{
LootTableMap mLootTables;
Bedrock::Threading::Mutex mLootTableMutex;
};

```
