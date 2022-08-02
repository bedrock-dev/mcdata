#### BackgroundTask::PendingComparer
```cpp
/* 82008 */
struct BackgroundTask::PendingComparer
{
__int8 gap0[1];
};

```
#### BackgroundTask::PriorityComparer
```cpp
/* 82009 */
struct BackgroundTask::PriorityComparer
{
__int8 gap0[1];
};

```
#### BackgroundWorkerPerfInfo
```cpp
/* 81878 */
struct BackgroundWorkerPerfInfo
{
const BackgroundWorker *mUpdaterWorker;
std::atomic<unsigned long> mTotalRunTasks;
std::atomic<unsigned long> mTotalRunTasksTicks;
std::atomic<unsigned int> mTotalWakeUps;
std::atomic<double> mAverageTaskDuration;
std::atomic<unsigned int> mWakeUpsPerSecond;
std::chrono::_V2::system_clock::time_point mLastPerfInfoUpdate;
std::chrono::_V2::system_clock::time_point mNextPerfInfoUpdate;
};

```
#### BackwardsCompatTextureGroup
```cpp
/* 483996 */
struct BackwardsCompatTextureGroup
{
std::unordered_map<ResourceLocation,BackwardsCompatTextureInfo> mBackCompatMap;
};

```
#### BackwardsCompatTextureInfo
```cpp
/* 483458 */
struct BackwardsCompatTextureInfo
{
bool mUse;
glm::vec2 mUVSize;
glm::vec2 mUV;
glm::vec2 mBaseSize;
Core::HeapPathBuffer mBackCompatTexture;
};

```
#### BalloonDefinition
```cpp
/* 107707 */
struct BalloonDefinition
{
Vec3 mLiftForce;
};

```
#### BalloonableDefinition
```cpp
/* 302903 */
struct BalloonableDefinition
{
float mSoftDistance;
float mMaxDistance;
float mInvMass;
DefinitionTrigger mOnBalloon;
DefinitionTrigger mOnUnballoon;
};

```
#### BannerRecipes
```cpp
/* 184692 */
struct BannerRecipes
{
__int8 gap0[1];
};

```
#### BaseActorRenderContext;
```cpp
/* 88683 */
struct BaseActorRenderContext;

```
#### BaseAttributeMap
```cpp
/* 74114 */
struct BaseAttributeMap
{
std::unordered_map<unsigned int,AttributeInstance> mInstanceMap;
std::vector<AttributeInstanceHandle> mDirtyAttributes;
};

```
#### BaseGamePackSlices
```cpp
/* 13219 */
struct BaseGamePackSlices
{
std::vector<BaseGamePackSlices::BaseGameVersionPack> mBaseGameVersionPacks;
std::vector<BaseGamePackSlices::BaseGameVersionPack> mBaseGameVersionTestPacks;
};

```
#### BaseGamePackSlices::BaseGameVersionPack
```cpp
/* 9918 */
struct BaseGamePackSlices::BaseGameVersionPack
{
BaseGameVersion mBaseGameVersion;
ResourcePack *mPack;
};

```
#### BaseGamePackSlices::applyPackSlices::$407E69F49D83A976B60EB7804F48E5FB
```cpp
/* 82046 */
struct BaseGamePackSlices::applyPackSlices::$407E69F49D83A976B60EB7804F48E5FB
{
const bool shouldApplyAllSlices;
const BaseGameVersion *baseGameVersion;
};

```
#### BaseGameVersion
```cpp
/* 5692 */
struct BaseGameVersion
{
SemVersion mSemVersion;
};

```
#### BaseGameVersion::any_version_constructor
```cpp
/* 5693 */
struct BaseGameVersion::any_version_constructor
{
__int8 gap0[1];
};

```
#### BaseMobSpawner
```cpp
/* 185974 */
struct BaseMobSpawner
{
int (**_vptr$BaseMobSpawner)(void);
int mSpawnDelay;
float mSpin;
float mOSpin;
ActorDefinitionIdentifier mActorId;
SpawnDataList mSpawnPotentials;
Unique<SpawnData> mNextSpawnData;
int mMinSpawnDelay;
int mMaxSpawnDelay;
int mSpawnCount;
Unique<Mob> mDisplayEntity;
int mMaxNearbyEntities;
int mRequiredPlayerRange;
int mSpawnRange;
float mDisplayEntityWidth;
float mDisplayEntityHeight;
float mDisplayEntityScale;
};

```
#### BaseMoveToBlockGoal
```cpp
/* 122532 */
struct BaseMoveToBlockGoal
{
__int8 baseclass_0[116];
int mSearchRange;
int mSearchHeight;
int mSearchCount;
};

```
#### BaseRailBlock::Rail
```cpp
/* 222977 */
struct BaseRailBlock::Rail
{
BlockSource *mRegion;
BlockPos mPos;
bool mUsesDataBit;
std::vector<BlockPos> mConnections;
};

```
#### BasicTimer
```cpp
/* 190278 */
struct BasicTimer
{
double mTimeDelay;
double mStartTime;
std::function<double ()> mGetCurrentTimeCallback;
};

```
#### BatchedNetworkPeer::DataCallback
```cpp
/* 421260 */
struct BatchedNetworkPeer::DataCallback
{
std::string data;
Compressibility compressible;
std::function<void ()> callback;
};

```
#### BeaconBeamSection
```cpp
/* 235101 */
struct BeaconBeamSection
{
int mHeight;
Color mColor;
};

```
#### BeardKernel
```cpp
/* 40145 */
struct BeardKernel
{
const std::array<float,13824> mKernel;
};

```
#### BedHelper
```cpp
/* 88758 */
struct BedHelper
{
float mNorthDir;
float mSouthDir;
float mWestDir;
float mEastDir;
float mBedOffsetX;
float mBedOffsetZ;
float mMobOffsetWestX;
float mMobOffsetEastX;
float mMobOffsetSouthZ;
float mMobOffsetNorthZ;
};

```
#### Bedrock::Application::ThreadOwner<Core::Random>
```cpp
/* 31071 */
struct Bedrock::Application::ThreadOwner<Core::Random>
{
Core::Random mObject;
};

```
#### Bedrock::Threading::ThreadUtil
```cpp
/* 485589 */
struct Bedrock::Threading::ThreadUtil
{
__int8 gap0[1];
};

```
#### Bedrock::Threading::`anonymous namespace'::AsyncErrorCategory
```cpp
/* 484152 */
struct Bedrock::Threading::`anonymous namespace'::AsyncErrorCategory
{
__int8 baseclass_0[8];
};

```
#### BedrockEngine::CommonPlatform;
```cpp
/* 6930 */
struct BedrockEngine::CommonPlatform;

```
#### BedrockEngine::IIslandCore
```cpp
/* 5026 */
struct BedrockEngine::IIslandCore
{
int (**_vptr$IIslandCore)(void);
};

```
#### BedrockEngine::PlatformRuntimeInfo
```cpp
/* 6932 */
struct BedrockEngine::PlatformRuntimeInfo
{
int (**_vptr$PlatformRuntimeInfo)(void);
std::string mDeviceModelName;
std::string mOSVersion;
std::string mCPUType;
std::string mCPUName;
std::string mCPUFeatures;
std::string mSecureId;
std::string mSerial;
std::string mBoard;
std::string mInstallerPackageName;
std::string mRegion;
PlatformType mPlatformType;
uint64_t mCachedFreeStorageSpace_Internal;
uint64_t mCachedFreeStorageSpace_External;
uint64_t mCachedFreeStorageSpace_Cloud;
uint64_t mTotalPhysicalMemory;
uint64_t mTotalVirtualMemory;
uint64_t mUsedMemory;
size_t mPhysicalMemorySize;
uint32_t mOptimalLDBSize;
float mWidth;
float mHeight;
float mDPI;
DisplayOrientation mOrientation;
int mSignaturesHash;
bool mGraphicsTearingSupport;
bool mAllowSplitScreen;
bool mSupportsMSAA;
bool mHasFastAlphaTest;
bool mSupportsVibration;
bool mSupportsTextToSpeech;
bool mSupportsClipboard;
bool mSupportsFilePicking;
bool mAllowContentLogWrite;
bool mIsRooted;
bool mCanSelfTerminate;
bool mCanLaunchUri;
uint8_t mCoreCount;
uint8_t mThreadCount;
uint8_t mHighPerfThreadCount;
uint8_t mProcessorGrade;
uint8_t mGraphicsGrade;
uint8_t mMemoryGrade;
uint8_t mStorageGrade;
uint8_t mPowerSupplyGrade;
Core::HeapPathBuffer mAssetStoragePath;
Core::HeapPathBuffer mCurrentStoragePath;
Core::HeapPathBuffer mExternalStoragePath;
Core::HeapPathBuffer mInternalStoragePath;
Core::HeapPathBuffer mLoggingPath;
Core::HeapPathBuffer mPackagePath;
Core::HeapPathBuffer mUserDataPath;
Core::HeapPathBuffer mCacheStoragePath;
};

```
#### BedrockItems
```cpp
/* 180745 */
struct BedrockItems
{
__int8 gap0[1];
};

```
#### BedrockLog::LogDetails::_appendLogEntryMetadata::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 480479 */
struct BedrockLog::LogDetails::_appendLogEntryMetadata::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### BehaviorComponent
```cpp
/* 50505 */
struct BehaviorComponent
{
BehaviorTreeDefinitionPtr mTreeDefinition;
Unique<BehaviorNode> mRoot;
BehaviorData mBehaviorData;
};

```
#### BehaviorData
```cpp
/* 50510 */
struct BehaviorData
{
std::unordered_map<std::string,std::unique_ptr<BehaviorData::DataProxy>> mData;
std::vector<std::unique_ptr<BehaviorData::DataProxy>> mDataStack;
};

```
#### BehaviorDefinition
```cpp
/* 169312 */
struct BehaviorDefinition
{
int (**_vptr$BehaviorDefinition)(void);
std::string mName;
BehaviorTreeDefinitionPtr mTreeDefinition;
};

```
#### BehaviorFactory
```cpp
/* 87913 */
struct BehaviorFactory
{
std::unordered_map<std::string,std::pair<std::function<std::unique_ptr<BehaviorDefinition> ()>,std::function<std::unique_ptr<BehaviorNode> ()> >> mFactoryPairs;
};

```
#### BehaviorPackContents
```cpp
/* 5711 */
struct BehaviorPackContents
{
uint32_t mEntities;
uint32_t mLoots;
uint32_t mTrades;
uint32_t mPlugins;
};

```
#### BehaviorTreeDefinition
```cpp
/* 50508 */
struct BehaviorTreeDefinition
{
std::string mTreeName;
std::string mStringInput;
Unique<BehaviorDefinition> mRoot;
};

```
#### BehaviorTreeDefinitionPtr
```cpp
/* 50506 */
struct BehaviorTreeDefinitionPtr
{
BehaviorTreeGroup *mGroup;
BehaviorTreeDefinition *mPtr;
};

```
#### BehaviorTreeGroup
```cpp
/* 50507 */
struct BehaviorTreeGroup
{
ResourcePackManager *mResourcePackManager;
BehaviorFactory *mFactory;
BehaviorTreeGroup::BehaviorDefinitionMap mDefinitions;
std::unordered_set<BehaviorTreeDefinitionPtr *> mRegisteredPtrs;
};

```
#### Biome
```cpp
/* 9575 */
struct Biome
{
int (**_vptr$Biome)(void);
std::string mName;
int mDebugMapColor;
int mDebugMapOddColor;
float mTemperature;
float mDownfall;
float mSnowAccumulation;
float mFoliageSnow;
float mMinSnowLevel;
float mMaxSnowLevel;
float mDepth;
float mScale;
Color mWaterColor;
float mWaterTranparency;
Color mUnderWaterColor;
bool mRain;
int mId;
float mFogDist;
OceanRuinConfiguration mOceanRuinConfig;
MobList mMobs;
Unique<PerlinSimplexNoise> mTemperatureNoise;
std::unique_ptr<PerlinSimplexNoise> mFrozenTemperatureNoise;
OwnerPtr<EntityId> mEntity;
OwnerPtr<PerlinSimplexNoise> mBiomeInfoNoise;
};

```
#### BiomeArea
```cpp
/* 37040 */
struct BiomeArea
{
uint32_t mStride;
std::vector<const Biome *> mBiomes;
};

```
#### BiomeChunkData
```cpp
/* 33654 */
struct BiomeChunkData
{
unsigned __int8 biome;
};

```
#### BiomeChunkDataLegacy
```cpp
/* 252871 */
struct BiomeChunkDataLegacy
{
unsigned __int8 biome;
unsigned __int8 r;
unsigned __int8 g;
unsigned __int8 b;
};

```
#### BiomeChunkState
```cpp
/* 33754 */
struct BiomeChunkState
{
byte snowLevel;
};

```
#### BiomeComponentLoading::_buildSchema<BiomeDecorationAttributes<ListedFeatures> >::$2658D4B1BE3081384A926FB0E5D18BAF
```cpp
/* 206106 */
struct BiomeComponentLoading::_buildSchema<BiomeDecorationAttributes<ListedFeatures> >::$2658D4B1BE3081384A926FB0E5D18BAF
{
BiomeComponentLoading::BiomeSchemaNode *schemaNode;
BiomeComponentLoading::ComponentAccessor<ListedFeaturesDecorationAttributes> componentAccessor;
};

```
#### BiomeDecorationAttributes<ImplicitFeatures>
```cpp
/* 222891 */
struct BiomeDecorationAttributes<ImplicitFeatures>
{
std::vector<BiomeDecorationAttributes<ImplicitFeatures>::Element,std::allocator<BiomeDecorationAttributes<ImplicitFeatures>::Element> > mFeatures;
};

```
#### BiomeDecorationAttributes<ImplicitFeatures>::Element
```cpp
/* 222831 */
struct BiomeDecorationAttributes<ImplicitFeatures>::Element
{
ScatterParams mScatter;
WeakRef<IFeature> mFeature;
StringKey mIdentifier;
};

```
#### BiomeDecorationAttributes<ListedFeatures>
```cpp
/* 193644 */
struct BiomeDecorationAttributes<ListedFeatures>
{
std::vector<BiomeDecorationAttributes<ListedFeatures>::Element,std::allocator<BiomeDecorationAttributes<ListedFeatures>::Element> > mFeatures;
};

```
#### BiomeDecorationAttributes<ListedFeatures>::Element
```cpp
/* 192990 */
struct BiomeDecorationAttributes<ListedFeatures>::Element
{
ScatterParams mScatter;
WeakRef<IFeature> mFeature;
StringKey mIdentifier;
};

```
#### BiomeDecorationSystem::decorate::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 222934 */
struct BiomeDecorationSystem::decorate::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### BiomeHeight
```cpp
/* 191371 */
struct BiomeHeight
{
float depth;
float scale;
};

```
#### BiomeMetadata
```cpp
/* 219610 */
struct BiomeMetadata
{
std::string mName;
std::string mInherits;
Json::Value mLocalComponents;
};

```
#### BiomeRegistry::BiomeParent
```cpp
/* 217803 */
struct BiomeRegistry::BiomeParent
{
std::string parentName;
Json::Value json;
};

```
#### BiomeSource
```cpp
/* 37041 */
struct BiomeSource
{
int (**_vptr$BiomeSource)(void);
};

```
#### BiomeSourceGetBiomeCache
```cpp
/* 37221 */
struct BiomeSourceGetBiomeCache
{
std::unordered_map<BlockPos,const Biome *> mMap;
SpinLock mLock;
};

```
#### Blacklist
```cpp
/* 76901 */
struct Blacklist
{
std::vector<Blacklist::Entry> mEntries;
Bedrock::Threading::RecursiveMutex mEntriesMutex;
};

```
#### BlockActorFactory
```cpp
/* 237626 */
struct BlockActorFactory
{
__int8 gap0[1];
};

```
#### BlockBreakSensorComponent
```cpp
/* 50729 */
struct BlockBreakSensorComponent
{
float mSensorRadius;
Vec3 mSensorPos;
BlockEventDispatcherToken mListener;
std::vector<BlockListEventMap> mBlockSets;
};

```
#### BlockBreakSensorDefinition
```cpp
/* 305188 */
struct BlockBreakSensorDefinition
{
float mSensorRadius;
std::vector<BlockListEventMap> mBlockSets;
};

```
#### BlockChange
```cpp
/* 430790 */
struct BlockChange
{
int mUpdateFlags;
const Block *mOldBlock;
const Block *mNewBlock;
};

```
#### BlockComponentDescription
```cpp
/* 81010 */
struct BlockComponentDescription
{
int (**_vptr$BlockComponentDescription)(void);
};

```
#### BlockComponentFactory
```cpp
/* 13250 */
struct BlockComponentFactory
{
BlockFactoryMap mFactoryMap;
};

```
#### BlockDefinition
```cpp
/* 10157 */
struct BlockDefinition
{
SemVersion mFormatVersion;
BlockDescription mDescription;
std::vector<std::shared_ptr<BlockComponentDescription>> mDescriptions;
};

```
#### BlockDefinitionGroup::loadResources::BlockResource
```cpp
/* 249080 */
struct BlockDefinitionGroup::loadResources::BlockResource
{
SemVersion mVersion;
BlockDescription mDescription;
Json::Value mRoot;
};

```
#### BlockEventDispatcherToken
```cpp
/* 50730 */
struct BlockEventDispatcherToken
{
ListenerHandle mHandle;
BlockEventDispatcher *mDispatcher;
};

```
#### BlockEventListener
```cpp
/* 10833 */
struct BlockEventListener
{
int (**_vptr$BlockEventListener)(void);
};

```
#### BlockFetchResult
```cpp
/* 35054 */
struct BlockFetchResult
{
std::reference_wrapper<const Block> mBlock;
BlockPos mBlockPos;
uint32_t mDistanceSquared;
};

```
#### BlockGeometry::AlignedFace
```cpp
/* 294484 */
struct BlockGeometry::AlignedFace
{
std::array<Vec3,4> verts;
std::array<Vec2,4> uvs;
size_t textureIndex;
};

```
#### BlockGeometry::Element
```cpp
/* 294425 */
struct BlockGeometry::Element
{
std::string mName;
std::string mParent;
glm::vec3 mPivot;
glm::vec3 mRotation;
std::vector<BlockGeometry::ElementBox> mBoxes;
};

```
#### BlockGeometry::ElementBox
```cpp
/* 294438 */
struct BlockGeometry::ElementBox
{
glm::vec3 mOrigin;
glm::vec3 mSize;
std::array<BlockGeometry::Face,6> mFaces;
};

```
#### BlockGeometry::Model
```cpp
/* 294412 */
struct BlockGeometry::Model
{
GameVersion mVersion;
std::string mName;
std::string mParent;
std::vector<BlockGeometry::Element> mElements;
std::unordered_map<std::string,std::string> mTextureMap;
std::vector<std::string> mTextureList;
std::vector<std::string> mTextureStack;
};

```
#### BlockGeometry::OrientedFace
```cpp
/* 294498 */
struct BlockGeometry::OrientedFace
{
std::array<Vec3,4> verts;
std::array<Vec2,4> uvs;
Vec3 norm;
size_t textureIndex;
};

```
#### BlockGeometry::Rotation;
```cpp
/* 296025 */
struct BlockGeometry::Rotation;

```
#### BlockGeometry::TessellatedModel
```cpp
/* 294467 */
struct BlockGeometry::TessellatedModel
{
std::array<AABB,4> mAABoxes;
std::array<std::vector<BlockGeometry::AlignedFace>,6> mEdgeSet;
std::array<std::vector<BlockGeometry::AlignedFace>,6> mAlignedSet;
BlockGeometry::OrientedFaceVector mOrientedSet;
std::array<BlockGeometry::TessellatedModel::Occlusion,6> mOcclusion;
std::array<BlockGeometry::TessellatedModel::Occlusion,3> mTopOcclusionRot;
std::array<BlockGeometry::TessellatedModel::Occlusion,3> mBotOcclusionRot;
std::vector<std::string> mTextureNames;
};

```
#### BlockGeometry::TessellatedModel::Occlusion
```cpp
/* 294501 */
struct BlockGeometry::TessellatedModel::Occlusion
{
std::array<unsigned char,8> blocking;
std::array<unsigned char,8> visible;
};

```
#### BlockGraphics
```cpp
/* 116684 */
struct BlockGraphics
{
int (**_vptr$BlockGraphics)(void);
IsotropicFaceData mIsotropicFaceData;
const Block *mBlock;
BlockRenderLayer mRenderLayer;
BlockShape mBlockShape;
bool mAnimatedTexture;
float mBrightnessGamma;
Color mMapColor;
bool mFancy;
bool mAllowSame;
BlockSoundType mSoundType;
AABB mVisualShape;
std::vector<TextureItem> mTextureItems;
size_t mIconTextureIndex;
std::vector<std::vector<const BlockGeometry::Model *>> mBlockModelVariants;
std::vector<std::vector<BlockGraphics::ModelItem>> mTessellatedModelParts;
};

```
#### BlockGraphics::ConstructorToken
```cpp
/* 296026 */
struct BlockGraphics::ConstructorToken
{
__int8 gap0[1];
};

```
#### BlockGraphics::ModelItem
```cpp
/* 294466 */
struct BlockGraphics::ModelItem
{
std::string name;
const BlockGeometry::TessellatedModel *model;
std::vector<unsigned long> textureIndices;
};

```
#### BlockLegacy
```cpp
/* 13199 */
struct BlockLegacy
{
int (**_vptr$BlockLegacy)(void);
std::string mDescriptionId;
std::string mRawNameId;
std::string mNamespace;
std::string mFullName;
bool mFancy;
BlockRenderLayer mRenderLayer;
bool mRenderLayerCanRenderAsOpaque;
BlockProperty mProperties;
BlockActorType mBlockEntityType;
bool mAnimatedTexture;
float mBrightnessGamma;
float mThickness;
bool mCanSlide;
bool mCanInstatick;
bool mIsInteraction;
float mGravity;
const Material *mMaterial;
Color mMapColor;
float mFriction;
bool mHeavy;
float mParticleQuantityScalar;
float mDestroySpeed;
float mExplosionResistance;
CreativeItemCategory mCreativeCategory;
bool mAllowsRunes;
bool mCanBeBrokenFromFalling;
bool mSolid;
bool mPushesOutItems;
bool mIgnoreBlockForInsideCubeRenderer;
bool mIsTrapdoor;
bool mIsDoor;
float mTranslucency;
Brightness mLightBlock;
Brightness mLightEmission;
bool mShouldRandomTick;
bool mShouldRandomTickExtraLayer;
int mFlameOdds;
int mBurnOdds;
bool mIsMobPiece;
bool mCanBeExtraBlock;
bool mCanPropagateBrightness;
NewBlockID mID;
BaseGameVersion mMinRequiredBaseGameVersion;
bool mExperimental;
bool mIsVanilla;
Unique<LootComponent> mLootComponent;
AABB mVisualShape;
unsigned int mBitsUsed;
unsigned int mTotalBitsUsed;
std::array<ItemStateInstance,105> mStates;
std::vector<std::unique_ptr<Block>> mBlockPermutations;
const Block *mDefaultState;
Bedrock::Threading::SharedMutex mLegacyDataLookupTableMutex;
std::vector<long> mLegacyDataLookupTable;
};

```
#### BlockLegacy::createBlockPermutations::$033A5A72970D0569F1B4E5782E3E5F13
```cpp
/* 223291 */
struct BlockLegacy::createBlockPermutations::$033A5A72970D0569F1B4E5782E3E5F13
{
BlockLegacy *this;
};

```
#### BlockLegacy::initFromDefinition::$033A5A72970D0569F1B4E5782E3E5F13
```cpp
/* 223292 */
struct BlockLegacy::initFromDefinition::$033A5A72970D0569F1B4E5782E3E5F13
{
BlockLegacy *this;
};

```
#### BlockListEventMap
```cpp
/* 50673 */
struct BlockListEventMap
{
std::unordered_set<const BlockLegacy *> mBlockList;
std::string mEventName;
};

```
#### BlockListSerializer
```cpp
/* 428726 */
struct BlockListSerializer
{
__int8 gap0[1];
};

```
#### BlockPalette
```cpp
/* 35009 */
struct BlockPalette
{
Bedrock::Threading::Mutex mLegacyBlockStatesConversionWarningMutex;
std::set<std::pair<int,int>> mLegacyBlockStatesConversionWarningSet;
std::map<std::string,const BlockLegacy *> mNameLookup;
std::map<CompoundTag,const Block *> mBlockFromSerId;
std::vector<const Block *> mBlockFromRuntimeId;
Level *mLevel;
};

```
#### BlockPalette::ConstructorToken
```cpp
/* 80898 */
struct BlockPalette::ConstructorToken
{
__int8 gap0[1];
};

```
#### BlockPos
```cpp
/* 5793 */
struct BlockPos
{
int x;
int y;
int z;
};

```
#### BlockReducer
```cpp
/* 456102 */
struct BlockReducer
{
int (**_vptr$BlockReducer)(void);
std::unordered_map<int,std::vector<ItemStack>> mBlockToElements;
};

```
#### BlockSelector
```cpp
/* 31936 */
struct BlockSelector
{
int (**_vptr$BlockSelector)(void);
};

```
#### BlockSerializationUtils::NbtToBlockCache
```cpp
/* 226288 */
struct BlockSerializationUtils::NbtToBlockCache
{
std::map<unsigned long,const Block *> mCache;
Bedrock::Threading::Mutex mMutex;
};

```
#### BlockSet
```cpp
/* 89203 */
struct BlockSet
{
float cost;
std::unordered_set<const BlockLegacy *> blocks;
};

```
#### BlockSource
```cpp
/* 13232 */
struct BlockSource
{
int (**_vptr$BlockSource)(void);
const std::thread::id mOwnerThreadID;
const bool mAllowUnpopulatedChunks;
const bool mPublicSource;
Level *mLevel;
ChunkSource *mChunkSource;
Dimension *mDimension;
const Height mMaxHeight;
std::vector<BlockFetchResult> mTempBlockFetchResult;
BlockPos mPlaceChunkPos;
BlockSource::ListenerVector mListeners;
ChunkPos mLastChunkPos;
LevelChunk *mLastChunk;
BlockTickingQueue *mRandomTickQueue;
BlockTickingQueue *mTickQueue;
const BrightnessPair mDefaultBrightness;
ActorList mTempEntityList;
BlockActorList mTempBlockEntityList;
std::vector<AABB> mTempCubeList;
};

```
#### BlockSource::fetchBlocksInBox::$74F335EC098D670C69AD7D2E598E74BF
```cpp
/* 186245 */
struct BlockSource::fetchBlocksInBox::$74F335EC098D670C69AD7D2E598E74BF
{
BlockSource *this;
const BoundingBox *box;
std::function<bool (const Block &)> *predicate;
};

```
#### BlockSource::fetchBlocksInCylinder::$BFF6684F24A24DAB087E11B4105C16CA
```cpp
/* 186244 */
struct BlockSource::fetchBlocksInCylinder::$BFF6684F24A24DAB087E11B4105C16CA
{
BlockSource *this;
const BlockPos *centerPos;
uint32_t radius;
uint32_t height;
std::function<bool (const Block &)> *predicate;
};

```
#### BlockSourceListener
```cpp
/* 34294 */
struct BlockSourceListener
{
int (**_vptr$BlockSourceListener)(void);
};

```
#### BlockTickingQueue::BlockTick
```cpp
/* 36324 */
struct BlockTickingQueue::BlockTick
{
bool mIsRemoved;
TickNextTickData mData;
};

```
#### BlockTickingQueue::HashBlockTick
```cpp
/* 186367 */
struct BlockTickingQueue::HashBlockTick
{
__int8 gap0[1];
};

```
#### BlockTickingQueue::getTickDelaysInArea::$8CF75821B5BA7DD28C0CF4A48A9CB9FA
```cpp
/* 186591 */
struct BlockTickingQueue::getTickDelaysInArea::$8CF75821B5BA7DD28C0CF4A48A9CB9FA
{
const BoundingBox *boundingBox;
std::unordered_multimap<BlockPos,TickDelayBlock> *ticks;
const BlockTickingQueue *this;
};

```
#### BlockTypeRegistry
```cpp
/* 250866 */
struct BlockTypeRegistry
{
__int8 gap0[1];
};

```
#### BlockUtils
```cpp
/* 428727 */
struct BlockUtils
{
__int8 gap0[1];
};

```
#### BlockVolume::BlockVolumeIter
```cpp
/* 35012 */
struct BlockVolume::BlockVolumeIter
{
Pos pos;
BlockPos dims;
buffer_span_mut<const Block *>::iterator blockIter;
};

```
#### Boat::Paddle
```cpp
/* 170701 */
struct Boat::Paddle
{
int mOldPressTime;
int mPressTime;
float mOldRowingTime;
float mRowingTime;
float mForce;
};

```
#### Boat::onAboveBubbleColumn::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 170702 */
struct Boat::onAboveBubbleColumn::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### BodyControlComponent
```cpp
/* 50895 */
struct BodyControlComponent
{
std::unique_ptr<BodyControl> mBodyControl;
};

```
#### BoneAnimationChannel
```cpp
/* 124546 */
struct BoneAnimationChannel
{
BoneTransformType mBoneTransformType;
std::vector<KeyFrameTransform> mKeyFrames;
};

```
#### BoneAnimationChannel::sortKeyFrames::KeyFrameCompare
```cpp
/* 124970 */
struct BoneAnimationChannel::sortKeyFrames::KeyFrameCompare
{
__int8 gap0[1];
};

```
#### BoneOrientationTransform
```cpp
/* 124454 */
struct BoneOrientationTransform
{
Vec3 mData[3];
};

```
#### BonusChestFeature::place::$FD274EF55AC88BD6B944C809A18A5641
```cpp
/* 268663 */
struct BonusChestFeature::place::$FD274EF55AC88BD6B944C809A18A5641
{
const BonusChestFeature *this;
BlockSource *region;
Random *newRandom;
};

```
#### BookAddPagePacket;
```cpp
/* 77414 */
struct BookAddPagePacket;

```
#### BookDeletePagePacket;
```cpp
/* 77415 */
struct BookDeletePagePacket;

```
#### BookSignPacket;
```cpp
/* 77416 */
struct BookSignPacket;

```
#### BookSwapPagesPacket;
```cpp
/* 77417 */
struct BookSwapPagesPacket;

```
#### BoostableComponent
```cpp
/* 51067 */
struct BoostableComponent
{
bool mIsBoosting;
int mBoostTime;
int mBoostTimeTotal;
float mFovMod;
};

```
#### BossComponent
```cpp
/* 51300 */
struct BossComponent
{
std::string mName;
bool mHealthBarVisible;
float mHealthPercent;
bool mShouldDarkenSky;
bool mCreateWorldFog;
BossBarColor mColor;
BossBarOverlay mOverlay;
int mPlayersRegistered;
int mLastHealth;
int mHudRangeSquared;
std::chrono::_V2::steady_clock::time_point mLastPlayerUpdate;
std::unordered_map<mce::UUID,int> mPlayerParty;
};

```
#### BossDefinition
```cpp
/* 310147 */
struct BossDefinition
{
std::string mName;
bool mShouldDarkenSky;
int mHudRange;
};

```
#### BossEventListener;
```cpp
/* 88023 */
struct BossEventListener;

```
#### BoundingBox
```cpp
/* 31371 */
struct BoundingBox
{
BlockPos min;
BlockPos max;
};

```
#### Bounds
```cpp
/* 37042 */
struct Bounds
{
Pos mMin;
Pos mMax;
Pos mDim;
int mArea;
int mVolume;
int mSide;
};

```
#### BreakDoorAnnotationComponent
```cpp
/* 51584 */
struct BreakDoorAnnotationComponent
{
int mBreakTicks;
Difficulty mMinDifficulty;
ActorUniqueID mTargetID;
int mBreakingTime;
std::optional<BlockPos> mObstructionPos;
size_t mLastPathIndex;
};

```
#### BreathableDefinition
```cpp
/* 107728 */
struct BreathableDefinition
{
int mTotalSupply;
int mSuffocateTime;
float mInhaleTime;
bool mBreathesAir;
bool mBreathesWater;
bool mBreathesLava;
bool mBreathesSolids;
bool mGeneratesBubbles;
std::set<const Block *> mBreathableBlocks;
std::set<const Block *> mNonBreathableBlocks;
};

```
#### BreedableComponent
```cpp
/* 51842 */
struct BreedableComponent
{
const BreedableDefinition *mStaticData;
int mLoveTimer;
int mBreedCooldown;
int mBreedCooldownTime;
bool mInheritTamed;
bool mCausesPregnancy;
ActorUniqueID mLoveCause;
};

```
#### BreedableType
```cpp
/* 319490 */
struct BreedableType
{
ActorDefinitionIdentifier mMateType;
ActorDefinitionIdentifier mBabyType;
DefinitionTrigger mOnBred;
};

```
#### BribeableDefinition
```cpp
/* 51958 */
struct BribeableDefinition
{
float mBribeCooldown;
std::set<const Item *> mBribeItems;
};

```
#### BrightnessPair
```cpp
/* 34304 */
struct BrightnessPair
{
Brightness sky;
Brightness block;
};

```
#### BubbleColumnBlock::entityInside::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 459292 */
struct BubbleColumnBlock::entityInside::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### BuildMatch
```cpp
/* 169815 */
struct BuildMatch
{
bool mMatched;
FacingID mForward;
FacingID mUp;
int mNumPatterns;
int mPatternSize;
int mSubPatternIndex;
int mRowIndex;
BlockPos mPattern;
Vec3 mObjectPos;
};

```
#### BurnsInDaylightDefinition
```cpp
/* 438582 */
struct BurnsInDaylightDefinition
{
__int8 gap0[1];
};

```
#### BurnsInDaylightFlag;
```cpp
/* 52153 */
struct BurnsInDaylightFlag;

```
#### BurstReactionComponent::_onEnd::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 238333 */
struct BurstReactionComponent::_onEnd::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### BackgroundTask::PendingComparer
```cpp
/* 82008 */
struct BackgroundTask::PendingComparer
{
__int8 gap0[1];
};

```
#### BackgroundTask::PriorityComparer
```cpp
/* 82009 */
struct BackgroundTask::PriorityComparer
{
__int8 gap0[1];
};

```
#### BackgroundWorkerPerfInfo
```cpp
/* 81878 */
struct BackgroundWorkerPerfInfo
{
const BackgroundWorker *mUpdaterWorker;
std::atomic<unsigned long> mTotalRunTasks;
std::atomic<unsigned long> mTotalRunTasksTicks;
std::atomic<unsigned int> mTotalWakeUps;
std::atomic<double> mAverageTaskDuration;
std::atomic<unsigned int> mWakeUpsPerSecond;
std::chrono::_V2::system_clock::time_point mLastPerfInfoUpdate;
std::chrono::_V2::system_clock::time_point mNextPerfInfoUpdate;
};

```
#### BackwardsCompatTextureGroup
```cpp
/* 483996 */
struct BackwardsCompatTextureGroup
{
std::unordered_map<ResourceLocation,BackwardsCompatTextureInfo> mBackCompatMap;
};

```
#### BackwardsCompatTextureInfo
```cpp
/* 483458 */
struct BackwardsCompatTextureInfo
{
bool mUse;
glm::vec2 mUVSize;
glm::vec2 mUV;
glm::vec2 mBaseSize;
Core::HeapPathBuffer mBackCompatTexture;
};

```
#### BalloonDefinition
```cpp
/* 107707 */
struct BalloonDefinition
{
Vec3 mLiftForce;
};

```
#### BalloonableDefinition
```cpp
/* 302903 */
struct BalloonableDefinition
{
float mSoftDistance;
float mMaxDistance;
float mInvMass;
DefinitionTrigger mOnBalloon;
DefinitionTrigger mOnUnballoon;
};

```
#### BannerRecipes
```cpp
/* 184692 */
struct BannerRecipes
{
__int8 gap0[1];
};

```
#### BaseActorRenderContext;
```cpp
/* 88683 */
struct BaseActorRenderContext;

```
#### BaseAttributeMap
```cpp
/* 74114 */
struct BaseAttributeMap
{
std::unordered_map<unsigned int,AttributeInstance> mInstanceMap;
std::vector<AttributeInstanceHandle> mDirtyAttributes;
};

```
#### BaseGamePackSlices
```cpp
/* 13219 */
struct BaseGamePackSlices
{
std::vector<BaseGamePackSlices::BaseGameVersionPack> mBaseGameVersionPacks;
std::vector<BaseGamePackSlices::BaseGameVersionPack> mBaseGameVersionTestPacks;
};

```
#### BaseGamePackSlices::BaseGameVersionPack
```cpp
/* 9918 */
struct BaseGamePackSlices::BaseGameVersionPack
{
BaseGameVersion mBaseGameVersion;
ResourcePack *mPack;
};

```
#### BaseGamePackSlices::applyPackSlices::$407E69F49D83A976B60EB7804F48E5FB
```cpp
/* 82046 */
struct BaseGamePackSlices::applyPackSlices::$407E69F49D83A976B60EB7804F48E5FB
{
const bool shouldApplyAllSlices;
const BaseGameVersion *baseGameVersion;
};

```
#### BaseGameVersion
```cpp
/* 5692 */
struct BaseGameVersion
{
SemVersion mSemVersion;
};

```
#### BaseGameVersion::any_version_constructor
```cpp
/* 5693 */
struct BaseGameVersion::any_version_constructor
{
__int8 gap0[1];
};

```
#### BaseMobSpawner
```cpp
/* 185974 */
struct BaseMobSpawner
{
int (**_vptr$BaseMobSpawner)(void);
int mSpawnDelay;
float mSpin;
float mOSpin;
ActorDefinitionIdentifier mActorId;
SpawnDataList mSpawnPotentials;
Unique<SpawnData> mNextSpawnData;
int mMinSpawnDelay;
int mMaxSpawnDelay;
int mSpawnCount;
Unique<Mob> mDisplayEntity;
int mMaxNearbyEntities;
int mRequiredPlayerRange;
int mSpawnRange;
float mDisplayEntityWidth;
float mDisplayEntityHeight;
float mDisplayEntityScale;
};

```
#### BaseMoveToBlockGoal
```cpp
/* 122532 */
struct BaseMoveToBlockGoal
{
__int8 baseclass_0[116];
int mSearchRange;
int mSearchHeight;
int mSearchCount;
};

```
#### BaseRailBlock::Rail
```cpp
/* 222977 */
struct BaseRailBlock::Rail
{
BlockSource *mRegion;
BlockPos mPos;
bool mUsesDataBit;
std::vector<BlockPos> mConnections;
};

```
#### BasicTimer
```cpp
/* 190278 */
struct BasicTimer
{
double mTimeDelay;
double mStartTime;
std::function<double ()> mGetCurrentTimeCallback;
};

```
#### BatchedNetworkPeer::DataCallback
```cpp
/* 421260 */
struct BatchedNetworkPeer::DataCallback
{
std::string data;
Compressibility compressible;
std::function<void ()> callback;
};

```
#### BeaconBeamSection
```cpp
/* 235101 */
struct BeaconBeamSection
{
int mHeight;
Color mColor;
};

```
#### BeardKernel
```cpp
/* 40145 */
struct BeardKernel
{
const std::array<float,13824> mKernel;
};

```
#### BedHelper
```cpp
/* 88758 */
struct BedHelper
{
float mNorthDir;
float mSouthDir;
float mWestDir;
float mEastDir;
float mBedOffsetX;
float mBedOffsetZ;
float mMobOffsetWestX;
float mMobOffsetEastX;
float mMobOffsetSouthZ;
float mMobOffsetNorthZ;
};

```
#### Bedrock::Application::ThreadOwner<Core::Random>
```cpp
/* 31071 */
struct Bedrock::Application::ThreadOwner<Core::Random>
{
Core::Random mObject;
};

```
#### Bedrock::Threading::ThreadUtil
```cpp
/* 485589 */
struct Bedrock::Threading::ThreadUtil
{
__int8 gap0[1];
};

```
#### Bedrock::Threading::`anonymous namespace'::AsyncErrorCategory
```cpp
/* 484152 */
struct Bedrock::Threading::`anonymous namespace'::AsyncErrorCategory
{
__int8 baseclass_0[8];
};

```
#### BedrockEngine::CommonPlatform;
```cpp
/* 6930 */
struct BedrockEngine::CommonPlatform;

```
#### BedrockEngine::IIslandCore
```cpp
/* 5026 */
struct BedrockEngine::IIslandCore
{
int (**_vptr$IIslandCore)(void);
};

```
#### BedrockEngine::PlatformRuntimeInfo
```cpp
/* 6932 */
struct BedrockEngine::PlatformRuntimeInfo
{
int (**_vptr$PlatformRuntimeInfo)(void);
std::string mDeviceModelName;
std::string mOSVersion;
std::string mCPUType;
std::string mCPUName;
std::string mCPUFeatures;
std::string mSecureId;
std::string mSerial;
std::string mBoard;
std::string mInstallerPackageName;
std::string mRegion;
PlatformType mPlatformType;
uint64_t mCachedFreeStorageSpace_Internal;
uint64_t mCachedFreeStorageSpace_External;
uint64_t mCachedFreeStorageSpace_Cloud;
uint64_t mTotalPhysicalMemory;
uint64_t mTotalVirtualMemory;
uint64_t mUsedMemory;
size_t mPhysicalMemorySize;
uint32_t mOptimalLDBSize;
float mWidth;
float mHeight;
float mDPI;
DisplayOrientation mOrientation;
int mSignaturesHash;
bool mGraphicsTearingSupport;
bool mAllowSplitScreen;
bool mSupportsMSAA;
bool mHasFastAlphaTest;
bool mSupportsVibration;
bool mSupportsTextToSpeech;
bool mSupportsClipboard;
bool mSupportsFilePicking;
bool mAllowContentLogWrite;
bool mIsRooted;
bool mCanSelfTerminate;
bool mCanLaunchUri;
uint8_t mCoreCount;
uint8_t mThreadCount;
uint8_t mHighPerfThreadCount;
uint8_t mProcessorGrade;
uint8_t mGraphicsGrade;
uint8_t mMemoryGrade;
uint8_t mStorageGrade;
uint8_t mPowerSupplyGrade;
Core::HeapPathBuffer mAssetStoragePath;
Core::HeapPathBuffer mCurrentStoragePath;
Core::HeapPathBuffer mExternalStoragePath;
Core::HeapPathBuffer mInternalStoragePath;
Core::HeapPathBuffer mLoggingPath;
Core::HeapPathBuffer mPackagePath;
Core::HeapPathBuffer mUserDataPath;
Core::HeapPathBuffer mCacheStoragePath;
};

```
#### BedrockItems
```cpp
/* 180745 */
struct BedrockItems
{
__int8 gap0[1];
};

```
#### BedrockLog::LogDetails::_appendLogEntryMetadata::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 480479 */
struct BedrockLog::LogDetails::_appendLogEntryMetadata::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### BehaviorComponent
```cpp
/* 50505 */
struct BehaviorComponent
{
BehaviorTreeDefinitionPtr mTreeDefinition;
Unique<BehaviorNode> mRoot;
BehaviorData mBehaviorData;
};

```
#### BehaviorData
```cpp
/* 50510 */
struct BehaviorData
{
std::unordered_map<std::string,std::unique_ptr<BehaviorData::DataProxy>> mData;
std::vector<std::unique_ptr<BehaviorData::DataProxy>> mDataStack;
};

```
#### BehaviorDefinition
```cpp
/* 169312 */
struct BehaviorDefinition
{
int (**_vptr$BehaviorDefinition)(void);
std::string mName;
BehaviorTreeDefinitionPtr mTreeDefinition;
};

```
#### BehaviorFactory
```cpp
/* 87913 */
struct BehaviorFactory
{
std::unordered_map<std::string,std::pair<std::function<std::unique_ptr<BehaviorDefinition> ()>,std::function<std::unique_ptr<BehaviorNode> ()> >> mFactoryPairs;
};

```
#### BehaviorPackContents
```cpp
/* 5711 */
struct BehaviorPackContents
{
uint32_t mEntities;
uint32_t mLoots;
uint32_t mTrades;
uint32_t mPlugins;
};

```
#### BehaviorTreeDefinition
```cpp
/* 50508 */
struct BehaviorTreeDefinition
{
std::string mTreeName;
std::string mStringInput;
Unique<BehaviorDefinition> mRoot;
};

```
#### BehaviorTreeDefinitionPtr
```cpp
/* 50506 */
struct BehaviorTreeDefinitionPtr
{
BehaviorTreeGroup *mGroup;
BehaviorTreeDefinition *mPtr;
};

```
#### BehaviorTreeGroup
```cpp
/* 50507 */
struct BehaviorTreeGroup
{
ResourcePackManager *mResourcePackManager;
BehaviorFactory *mFactory;
BehaviorTreeGroup::BehaviorDefinitionMap mDefinitions;
std::unordered_set<BehaviorTreeDefinitionPtr *> mRegisteredPtrs;
};

```
#### Biome
```cpp
/* 9575 */
struct Biome
{
int (**_vptr$Biome)(void);
std::string mName;
int mDebugMapColor;
int mDebugMapOddColor;
float mTemperature;
float mDownfall;
float mSnowAccumulation;
float mFoliageSnow;
float mMinSnowLevel;
float mMaxSnowLevel;
float mDepth;
float mScale;
Color mWaterColor;
float mWaterTranparency;
Color mUnderWaterColor;
bool mRain;
int mId;
float mFogDist;
OceanRuinConfiguration mOceanRuinConfig;
MobList mMobs;
Unique<PerlinSimplexNoise> mTemperatureNoise;
std::unique_ptr<PerlinSimplexNoise> mFrozenTemperatureNoise;
OwnerPtr<EntityId> mEntity;
OwnerPtr<PerlinSimplexNoise> mBiomeInfoNoise;
};

```
#### BiomeArea
```cpp
/* 37040 */
struct BiomeArea
{
uint32_t mStride;
std::vector<const Biome *> mBiomes;
};

```
#### BiomeChunkData
```cpp
/* 33654 */
struct BiomeChunkData
{
unsigned __int8 biome;
};

```
#### BiomeChunkDataLegacy
```cpp
/* 252871 */
struct BiomeChunkDataLegacy
{
unsigned __int8 biome;
unsigned __int8 r;
unsigned __int8 g;
unsigned __int8 b;
};

```
#### BiomeChunkState
```cpp
/* 33754 */
struct BiomeChunkState
{
byte snowLevel;
};

```
#### BiomeComponentLoading::_buildSchema<BiomeDecorationAttributes<ListedFeatures> >::$2658D4B1BE3081384A926FB0E5D18BAF
```cpp
/* 206106 */
struct BiomeComponentLoading::_buildSchema<BiomeDecorationAttributes<ListedFeatures> >::$2658D4B1BE3081384A926FB0E5D18BAF
{
BiomeComponentLoading::BiomeSchemaNode *schemaNode;
BiomeComponentLoading::ComponentAccessor<ListedFeaturesDecorationAttributes> componentAccessor;
};

```
#### BiomeDecorationAttributes<ImplicitFeatures>
```cpp
/* 222891 */
struct BiomeDecorationAttributes<ImplicitFeatures>
{
std::vector<BiomeDecorationAttributes<ImplicitFeatures>::Element,std::allocator<BiomeDecorationAttributes<ImplicitFeatures>::Element> > mFeatures;
};

```
#### BiomeDecorationAttributes<ImplicitFeatures>::Element
```cpp
/* 222831 */
struct BiomeDecorationAttributes<ImplicitFeatures>::Element
{
ScatterParams mScatter;
WeakRef<IFeature> mFeature;
StringKey mIdentifier;
};

```
#### BiomeDecorationAttributes<ListedFeatures>
```cpp
/* 193644 */
struct BiomeDecorationAttributes<ListedFeatures>
{
std::vector<BiomeDecorationAttributes<ListedFeatures>::Element,std::allocator<BiomeDecorationAttributes<ListedFeatures>::Element> > mFeatures;
};

```
#### BiomeDecorationAttributes<ListedFeatures>::Element
```cpp
/* 192990 */
struct BiomeDecorationAttributes<ListedFeatures>::Element
{
ScatterParams mScatter;
WeakRef<IFeature> mFeature;
StringKey mIdentifier;
};

```
#### BiomeDecorationSystem::decorate::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 222934 */
struct BiomeDecorationSystem::decorate::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### BiomeHeight
```cpp
/* 191371 */
struct BiomeHeight
{
float depth;
float scale;
};

```
#### BiomeMetadata
```cpp
/* 219610 */
struct BiomeMetadata
{
std::string mName;
std::string mInherits;
Json::Value mLocalComponents;
};

```
#### BiomeRegistry::BiomeParent
```cpp
/* 217803 */
struct BiomeRegistry::BiomeParent
{
std::string parentName;
Json::Value json;
};

```
#### BiomeSource
```cpp
/* 37041 */
struct BiomeSource
{
int (**_vptr$BiomeSource)(void);
};

```
#### BiomeSourceGetBiomeCache
```cpp
/* 37221 */
struct BiomeSourceGetBiomeCache
{
std::unordered_map<BlockPos,const Biome *> mMap;
SpinLock mLock;
};

```
#### Blacklist
```cpp
/* 76901 */
struct Blacklist
{
std::vector<Blacklist::Entry> mEntries;
Bedrock::Threading::RecursiveMutex mEntriesMutex;
};

```
#### BlockActorFactory
```cpp
/* 237626 */
struct BlockActorFactory
{
__int8 gap0[1];
};

```
#### BlockBreakSensorComponent
```cpp
/* 50729 */
struct BlockBreakSensorComponent
{
float mSensorRadius;
Vec3 mSensorPos;
BlockEventDispatcherToken mListener;
std::vector<BlockListEventMap> mBlockSets;
};

```
#### BlockBreakSensorDefinition
```cpp
/* 305188 */
struct BlockBreakSensorDefinition
{
float mSensorRadius;
std::vector<BlockListEventMap> mBlockSets;
};

```
#### BlockChange
```cpp
/* 430790 */
struct BlockChange
{
int mUpdateFlags;
const Block *mOldBlock;
const Block *mNewBlock;
};

```
#### BlockComponentDescription
```cpp
/* 81010 */
struct BlockComponentDescription
{
int (**_vptr$BlockComponentDescription)(void);
};

```
#### BlockComponentFactory
```cpp
/* 13250 */
struct BlockComponentFactory
{
BlockFactoryMap mFactoryMap;
};

```
#### BlockDefinition
```cpp
/* 10157 */
struct BlockDefinition
{
SemVersion mFormatVersion;
BlockDescription mDescription;
std::vector<std::shared_ptr<BlockComponentDescription>> mDescriptions;
};

```
#### BlockDefinitionGroup::loadResources::BlockResource
```cpp
/* 249080 */
struct BlockDefinitionGroup::loadResources::BlockResource
{
SemVersion mVersion;
BlockDescription mDescription;
Json::Value mRoot;
};

```
#### BlockEventDispatcherToken
```cpp
/* 50730 */
struct BlockEventDispatcherToken
{
ListenerHandle mHandle;
BlockEventDispatcher *mDispatcher;
};

```
#### BlockEventListener
```cpp
/* 10833 */
struct BlockEventListener
{
int (**_vptr$BlockEventListener)(void);
};

```
#### BlockFetchResult
```cpp
/* 35054 */
struct BlockFetchResult
{
std::reference_wrapper<const Block> mBlock;
BlockPos mBlockPos;
uint32_t mDistanceSquared;
};

```
#### BlockGeometry::AlignedFace
```cpp
/* 294484 */
struct BlockGeometry::AlignedFace
{
std::array<Vec3,4> verts;
std::array<Vec2,4> uvs;
size_t textureIndex;
};

```
#### BlockGeometry::Element
```cpp
/* 294425 */
struct BlockGeometry::Element
{
std::string mName;
std::string mParent;
glm::vec3 mPivot;
glm::vec3 mRotation;
std::vector<BlockGeometry::ElementBox> mBoxes;
};

```
#### BlockGeometry::ElementBox
```cpp
/* 294438 */
struct BlockGeometry::ElementBox
{
glm::vec3 mOrigin;
glm::vec3 mSize;
std::array<BlockGeometry::Face,6> mFaces;
};

```
#### BlockGeometry::Model
```cpp
/* 294412 */
struct BlockGeometry::Model
{
GameVersion mVersion;
std::string mName;
std::string mParent;
std::vector<BlockGeometry::Element> mElements;
std::unordered_map<std::string,std::string> mTextureMap;
std::vector<std::string> mTextureList;
std::vector<std::string> mTextureStack;
};

```
#### BlockGeometry::OrientedFace
```cpp
/* 294498 */
struct BlockGeometry::OrientedFace
{
std::array<Vec3,4> verts;
std::array<Vec2,4> uvs;
Vec3 norm;
size_t textureIndex;
};

```
#### BlockGeometry::Rotation;
```cpp
/* 296025 */
struct BlockGeometry::Rotation;

```
#### BlockGeometry::TessellatedModel
```cpp
/* 294467 */
struct BlockGeometry::TessellatedModel
{
std::array<AABB,4> mAABoxes;
std::array<std::vector<BlockGeometry::AlignedFace>,6> mEdgeSet;
std::array<std::vector<BlockGeometry::AlignedFace>,6> mAlignedSet;
BlockGeometry::OrientedFaceVector mOrientedSet;
std::array<BlockGeometry::TessellatedModel::Occlusion,6> mOcclusion;
std::array<BlockGeometry::TessellatedModel::Occlusion,3> mTopOcclusionRot;
std::array<BlockGeometry::TessellatedModel::Occlusion,3> mBotOcclusionRot;
std::vector<std::string> mTextureNames;
};

```
#### BlockGeometry::TessellatedModel::Occlusion
```cpp
/* 294501 */
struct BlockGeometry::TessellatedModel::Occlusion
{
std::array<unsigned char,8> blocking;
std::array<unsigned char,8> visible;
};

```
#### BlockGraphics
```cpp
/* 116684 */
struct BlockGraphics
{
int (**_vptr$BlockGraphics)(void);
IsotropicFaceData mIsotropicFaceData;
const Block *mBlock;
BlockRenderLayer mRenderLayer;
BlockShape mBlockShape;
bool mAnimatedTexture;
float mBrightnessGamma;
Color mMapColor;
bool mFancy;
bool mAllowSame;
BlockSoundType mSoundType;
AABB mVisualShape;
std::vector<TextureItem> mTextureItems;
size_t mIconTextureIndex;
std::vector<std::vector<const BlockGeometry::Model *>> mBlockModelVariants;
std::vector<std::vector<BlockGraphics::ModelItem>> mTessellatedModelParts;
};

```
#### BlockGraphics::ConstructorToken
```cpp
/* 296026 */
struct BlockGraphics::ConstructorToken
{
__int8 gap0[1];
};

```
#### BlockGraphics::ModelItem
```cpp
/* 294466 */
struct BlockGraphics::ModelItem
{
std::string name;
const BlockGeometry::TessellatedModel *model;
std::vector<unsigned long> textureIndices;
};

```
#### BlockLegacy
```cpp
/* 13199 */
struct BlockLegacy
{
int (**_vptr$BlockLegacy)(void);
std::string mDescriptionId;
std::string mRawNameId;
std::string mNamespace;
std::string mFullName;
bool mFancy;
BlockRenderLayer mRenderLayer;
bool mRenderLayerCanRenderAsOpaque;
BlockProperty mProperties;
BlockActorType mBlockEntityType;
bool mAnimatedTexture;
float mBrightnessGamma;
float mThickness;
bool mCanSlide;
bool mCanInstatick;
bool mIsInteraction;
float mGravity;
const Material *mMaterial;
Color mMapColor;
float mFriction;
bool mHeavy;
float mParticleQuantityScalar;
float mDestroySpeed;
float mExplosionResistance;
CreativeItemCategory mCreativeCategory;
bool mAllowsRunes;
bool mCanBeBrokenFromFalling;
bool mSolid;
bool mPushesOutItems;
bool mIgnoreBlockForInsideCubeRenderer;
bool mIsTrapdoor;
bool mIsDoor;
float mTranslucency;
Brightness mLightBlock;
Brightness mLightEmission;
bool mShouldRandomTick;
bool mShouldRandomTickExtraLayer;
int mFlameOdds;
int mBurnOdds;
bool mIsMobPiece;
bool mCanBeExtraBlock;
bool mCanPropagateBrightness;
NewBlockID mID;
BaseGameVersion mMinRequiredBaseGameVersion;
bool mExperimental;
bool mIsVanilla;
Unique<LootComponent> mLootComponent;
AABB mVisualShape;
unsigned int mBitsUsed;
unsigned int mTotalBitsUsed;
std::array<ItemStateInstance,105> mStates;
std::vector<std::unique_ptr<Block>> mBlockPermutations;
const Block *mDefaultState;
Bedrock::Threading::SharedMutex mLegacyDataLookupTableMutex;
std::vector<long> mLegacyDataLookupTable;
};

```
#### BlockLegacy::createBlockPermutations::$033A5A72970D0569F1B4E5782E3E5F13
```cpp
/* 223291 */
struct BlockLegacy::createBlockPermutations::$033A5A72970D0569F1B4E5782E3E5F13
{
BlockLegacy *this;
};

```
#### BlockLegacy::initFromDefinition::$033A5A72970D0569F1B4E5782E3E5F13
```cpp
/* 223292 */
struct BlockLegacy::initFromDefinition::$033A5A72970D0569F1B4E5782E3E5F13
{
BlockLegacy *this;
};

```
#### BlockListEventMap
```cpp
/* 50673 */
struct BlockListEventMap
{
std::unordered_set<const BlockLegacy *> mBlockList;
std::string mEventName;
};

```
#### BlockListSerializer
```cpp
/* 428726 */
struct BlockListSerializer
{
__int8 gap0[1];
};

```
#### BlockPalette
```cpp
/* 35009 */
struct BlockPalette
{
Bedrock::Threading::Mutex mLegacyBlockStatesConversionWarningMutex;
std::set<std::pair<int,int>> mLegacyBlockStatesConversionWarningSet;
std::map<std::string,const BlockLegacy *> mNameLookup;
std::map<CompoundTag,const Block *> mBlockFromSerId;
std::vector<const Block *> mBlockFromRuntimeId;
Level *mLevel;
};

```
#### BlockPalette::ConstructorToken
```cpp
/* 80898 */
struct BlockPalette::ConstructorToken
{
__int8 gap0[1];
};

```
#### BlockPos
```cpp
/* 5793 */
struct BlockPos
{
int x;
int y;
int z;
};

```
#### BlockReducer
```cpp
/* 456102 */
struct BlockReducer
{
int (**_vptr$BlockReducer)(void);
std::unordered_map<int,std::vector<ItemStack>> mBlockToElements;
};

```
#### BlockSelector
```cpp
/* 31936 */
struct BlockSelector
{
int (**_vptr$BlockSelector)(void);
};

```
#### BlockSerializationUtils::NbtToBlockCache
```cpp
/* 226288 */
struct BlockSerializationUtils::NbtToBlockCache
{
std::map<unsigned long,const Block *> mCache;
Bedrock::Threading::Mutex mMutex;
};

```
#### BlockSet
```cpp
/* 89203 */
struct BlockSet
{
float cost;
std::unordered_set<const BlockLegacy *> blocks;
};

```
#### BlockSource
```cpp
/* 13232 */
struct BlockSource
{
int (**_vptr$BlockSource)(void);
const std::thread::id mOwnerThreadID;
const bool mAllowUnpopulatedChunks;
const bool mPublicSource;
Level *mLevel;
ChunkSource *mChunkSource;
Dimension *mDimension;
const Height mMaxHeight;
std::vector<BlockFetchResult> mTempBlockFetchResult;
BlockPos mPlaceChunkPos;
BlockSource::ListenerVector mListeners;
ChunkPos mLastChunkPos;
LevelChunk *mLastChunk;
BlockTickingQueue *mRandomTickQueue;
BlockTickingQueue *mTickQueue;
const BrightnessPair mDefaultBrightness;
ActorList mTempEntityList;
BlockActorList mTempBlockEntityList;
std::vector<AABB> mTempCubeList;
};

```
#### BlockSource::fetchBlocksInBox::$74F335EC098D670C69AD7D2E598E74BF
```cpp
/* 186245 */
struct BlockSource::fetchBlocksInBox::$74F335EC098D670C69AD7D2E598E74BF
{
BlockSource *this;
const BoundingBox *box;
std::function<bool (const Block &)> *predicate;
};

```
#### BlockSource::fetchBlocksInCylinder::$BFF6684F24A24DAB087E11B4105C16CA
```cpp
/* 186244 */
struct BlockSource::fetchBlocksInCylinder::$BFF6684F24A24DAB087E11B4105C16CA
{
BlockSource *this;
const BlockPos *centerPos;
uint32_t radius;
uint32_t height;
std::function<bool (const Block &)> *predicate;
};

```
#### BlockSourceListener
```cpp
/* 34294 */
struct BlockSourceListener
{
int (**_vptr$BlockSourceListener)(void);
};

```
#### BlockTickingQueue::BlockTick
```cpp
/* 36324 */
struct BlockTickingQueue::BlockTick
{
bool mIsRemoved;
TickNextTickData mData;
};

```
#### BlockTickingQueue::HashBlockTick
```cpp
/* 186367 */
struct BlockTickingQueue::HashBlockTick
{
__int8 gap0[1];
};

```
#### BlockTickingQueue::getTickDelaysInArea::$8CF75821B5BA7DD28C0CF4A48A9CB9FA
```cpp
/* 186591 */
struct BlockTickingQueue::getTickDelaysInArea::$8CF75821B5BA7DD28C0CF4A48A9CB9FA
{
const BoundingBox *boundingBox;
std::unordered_multimap<BlockPos,TickDelayBlock> *ticks;
const BlockTickingQueue *this;
};

```
#### BlockTypeRegistry
```cpp
/* 250866 */
struct BlockTypeRegistry
{
__int8 gap0[1];
};

```
#### BlockUtils
```cpp
/* 428727 */
struct BlockUtils
{
__int8 gap0[1];
};

```
#### BlockVolume::BlockVolumeIter
```cpp
/* 35012 */
struct BlockVolume::BlockVolumeIter
{
Pos pos;
BlockPos dims;
buffer_span_mut<const Block *>::iterator blockIter;
};

```
#### Boat::Paddle
```cpp
/* 170701 */
struct Boat::Paddle
{
int mOldPressTime;
int mPressTime;
float mOldRowingTime;
float mRowingTime;
float mForce;
};

```
#### Boat::onAboveBubbleColumn::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 170702 */
struct Boat::onAboveBubbleColumn::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### BodyControlComponent
```cpp
/* 50895 */
struct BodyControlComponent
{
std::unique_ptr<BodyControl> mBodyControl;
};

```
#### BoneAnimationChannel
```cpp
/* 124546 */
struct BoneAnimationChannel
{
BoneTransformType mBoneTransformType;
std::vector<KeyFrameTransform> mKeyFrames;
};

```
#### BoneAnimationChannel::sortKeyFrames::KeyFrameCompare
```cpp
/* 124970 */
struct BoneAnimationChannel::sortKeyFrames::KeyFrameCompare
{
__int8 gap0[1];
};

```
#### BoneOrientationTransform
```cpp
/* 124454 */
struct BoneOrientationTransform
{
Vec3 mData[3];
};

```
#### BonusChestFeature::place::$FD274EF55AC88BD6B944C809A18A5641
```cpp
/* 268663 */
struct BonusChestFeature::place::$FD274EF55AC88BD6B944C809A18A5641
{
const BonusChestFeature *this;
BlockSource *region;
Random *newRandom;
};

```
#### BookAddPagePacket;
```cpp
/* 77414 */
struct BookAddPagePacket;

```
#### BookDeletePagePacket;
```cpp
/* 77415 */
struct BookDeletePagePacket;

```
#### BookSignPacket;
```cpp
/* 77416 */
struct BookSignPacket;

```
#### BookSwapPagesPacket;
```cpp
/* 77417 */
struct BookSwapPagesPacket;

```
#### BoostableComponent
```cpp
/* 51067 */
struct BoostableComponent
{
bool mIsBoosting;
int mBoostTime;
int mBoostTimeTotal;
float mFovMod;
};

```
#### BossComponent
```cpp
/* 51300 */
struct BossComponent
{
std::string mName;
bool mHealthBarVisible;
float mHealthPercent;
bool mShouldDarkenSky;
bool mCreateWorldFog;
BossBarColor mColor;
BossBarOverlay mOverlay;
int mPlayersRegistered;
int mLastHealth;
int mHudRangeSquared;
std::chrono::_V2::steady_clock::time_point mLastPlayerUpdate;
std::unordered_map<mce::UUID,int> mPlayerParty;
};

```
#### BossDefinition
```cpp
/* 310147 */
struct BossDefinition
{
std::string mName;
bool mShouldDarkenSky;
int mHudRange;
};

```
#### BossEventListener;
```cpp
/* 88023 */
struct BossEventListener;

```
#### BoundingBox
```cpp
/* 31371 */
struct BoundingBox
{
BlockPos min;
BlockPos max;
};

```
#### Bounds
```cpp
/* 37042 */
struct Bounds
{
Pos mMin;
Pos mMax;
Pos mDim;
int mArea;
int mVolume;
int mSide;
};

```
#### BreakDoorAnnotationComponent
```cpp
/* 51584 */
struct BreakDoorAnnotationComponent
{
int mBreakTicks;
Difficulty mMinDifficulty;
ActorUniqueID mTargetID;
int mBreakingTime;
std::optional<BlockPos> mObstructionPos;
size_t mLastPathIndex;
};

```
#### BreathableDefinition
```cpp
/* 107728 */
struct BreathableDefinition
{
int mTotalSupply;
int mSuffocateTime;
float mInhaleTime;
bool mBreathesAir;
bool mBreathesWater;
bool mBreathesLava;
bool mBreathesSolids;
bool mGeneratesBubbles;
std::set<const Block *> mBreathableBlocks;
std::set<const Block *> mNonBreathableBlocks;
};

```
#### BreedableComponent
```cpp
/* 51842 */
struct BreedableComponent
{
const BreedableDefinition *mStaticData;
int mLoveTimer;
int mBreedCooldown;
int mBreedCooldownTime;
bool mInheritTamed;
bool mCausesPregnancy;
ActorUniqueID mLoveCause;
};

```
#### BreedableType
```cpp
/* 319490 */
struct BreedableType
{
ActorDefinitionIdentifier mMateType;
ActorDefinitionIdentifier mBabyType;
DefinitionTrigger mOnBred;
};

```
#### BribeableDefinition
```cpp
/* 51958 */
struct BribeableDefinition
{
float mBribeCooldown;
std::set<const Item *> mBribeItems;
};

```
#### BrightnessPair
```cpp
/* 34304 */
struct BrightnessPair
{
Brightness sky;
Brightness block;
};

```
#### BubbleColumnBlock::entityInside::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 459292 */
struct BubbleColumnBlock::entityInside::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### BuildMatch
```cpp
/* 169815 */
struct BuildMatch
{
bool mMatched;
FacingID mForward;
FacingID mUp;
int mNumPatterns;
int mPatternSize;
int mSubPatternIndex;
int mRowIndex;
BlockPos mPattern;
Vec3 mObjectPos;
};

```
#### BurnsInDaylightDefinition
```cpp
/* 438582 */
struct BurnsInDaylightDefinition
{
__int8 gap0[1];
};

```
#### BurnsInDaylightFlag;
```cpp
/* 52153 */
struct BurnsInDaylightFlag;

```
#### BurstReactionComponent::_onEnd::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 238333 */
struct BurstReactionComponent::_onEnd::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
