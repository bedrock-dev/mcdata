#### Tag
```cpp
/* 5811 */
struct Tag
{
int (**_vptr$Tag)(void);
};

```
#### TagCommand::_listTags::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 427378 */
struct TagCommand::_listTags::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### TagIDType;
```cpp
/* 40656 */
struct TagIDType;

```
#### TagMemoryChunk
```cpp
/* 61618 */
struct TagMemoryChunk
{
size_t mElements;
size_t mSize;
std::unique_ptr<unsigned char []> mBuffer;
};

```
#### TagRegistry
```cpp
/* 38394 */
struct TagRegistry
{
std::unordered_map<StringKey,unsigned int> mTagIndexMap;
std::vector<std::string> mTags;
std::vector<IndexSet> mSets;
std::vector<std::string> mTagsScratchpad;
std::vector<IDType<TagIDType>> mTagIDScratchpad;
IndexSet mIndexSetScratchpad;
TagSetID mEmptyTagSet;
};

```
#### TagSetIDType;
```cpp
/* 40657 */
struct TagSetIDType;

```
#### TagsComponent
```cpp
/* 100455 */
struct TagsComponent
{
TagSetID mTagSetID;
};

```
#### TameableComponent
```cpp
/* 54414 */
struct TameableComponent
{
float mChance;
std::set<const Item *> mTameItems;
};

```
#### TargetNearbyComponent
```cpp
/* 59369 */
struct TargetNearbyComponent
{
bool mWasSeenLastTick;
bool mWasInsideRange;
bool mWasOutsideRange;
float mPreviousDistance;
};

```
#### TaskStartInfo
```cpp
/* 63717 */
struct TaskStartInfo
{
string_span name;
std::thread::id affinity;
uint32_t priority;
int priorityBackDown;
TaskOptions options;
std::chrono::_V2::steady_clock::time_point startAtTime;
Bedrock::Threading::IAsyncResult<void>::Handle predecessor;
};

```
#### TeleportComponent
```cpp
/* 59484 */
struct TeleportComponent
{
bool mRandomTeleports;
int mMinTeleportTime;
int mMaxTeleportTime;
Vec3 mRandomTeleportCube;
float mTargetDistance;
float mTargetTeleportChance;
float mLightTeleportChance;
float mDarkTeleportChance;
int mTeleportTime;
};

```
#### Tessellator;
```cpp
/* 122537 */
struct Tessellator;

```
#### TestDedicatedServerCommands
```cpp
/* 5842 */
struct TestDedicatedServerCommands
{
__int8 gap0[1];
};

```
#### TestServerCommands
```cpp
/* 424409 */
struct TestServerCommands
{
__int8 gap0[1];
};

```
#### TextFilteringProcessor;
```cpp
/* 76902 */
struct TextFilteringProcessor;

```
#### TextObjectParser
```cpp
/* 101045 */
struct TextObjectParser
{
__int8 gap0[1];
};

```
#### TextureAtlas;
```cpp
/* 459465 */
struct TextureAtlas;

```
#### TextureAtlasItem
```cpp
/* 103920 */
struct TextureAtlasItem
{
std::string mName;
int mParsedNodeIndex;
std::vector<std::vector<TextureUVCoordinateSet>> mTextureUVs;
};

```
#### TextureItem
```cpp
/* 294387 */
struct TextureItem
{
std::string defaultName;
std::string carriedName;
TextureAtlasItem defaultItem;
TextureAtlasItem carriedItem;
};

```
#### TextureUVCoordinateSet
```cpp
/* 33516 */
struct TextureUVCoordinateSet
{
float weight;
float _u0;
float _v0;
float _u1;
float _v1;
uint16_t _texSizeW;
uint16_t _texSizeH;
ResourceLocation sourceFileLocation;
IsotropicFaceData mIsotropicFaceData;
};

```
#### TheEndBiomeSurface;
```cpp
/* 198714 */
struct TheEndBiomeSurface;

```
#### TheEndGenerator::ThreadData
```cpp
/* 289518 */
struct TheEndGenerator::ThreadData
{
std::array<long,32768> blockBuffer;
};

```
#### ThreadLocal<BackgroundWorker *>
```cpp
/* 485240 */
struct ThreadLocal<BackgroundWorker *>
{
ThreadLocal<BackgroundWorker *>::Creator mCreator;
ThreadLocal<BackgroundWorker *>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<Core::Random>
```cpp
/* 31217 */
struct ThreadLocal<Core::Random>
{
ThreadLocal<Core::Random>::Creator mCreator;
ThreadLocal<Core::Random>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<DBStorageWriteBatch>
```cpp
/* 477455 */
struct ThreadLocal<DBStorageWriteBatch>
{
ThreadLocal<DBStorageWriteBatch>::Creator mCreator;
ThreadLocal<DBStorageWriteBatch>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<EvalParams>
```cpp
/* 109090 */
struct ThreadLocal<EvalParams>
{
ThreadLocal<EvalParams>::Creator mCreator;
ThreadLocal<EvalParams>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<NetherGenerator::ThreadData>
```cpp
/* 36890 */
struct ThreadLocal<NetherGenerator::ThreadData>
{
ThreadLocal<NetherGenerator::ThreadData>::Creator mCreator;
ThreadLocal<NetherGenerator::ThreadData>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<OverworldGenerator::ThreadData>
```cpp
/* 40147 */
struct ThreadLocal<OverworldGenerator::ThreadData>
{
ThreadLocal<OverworldGenerator::ThreadData>::Creator mCreator;
ThreadLocal<OverworldGenerator::ThreadData>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<PerfTimer>
```cpp
/* 102997 */
struct ThreadLocal<PerfTimer>
{
ThreadLocal<PerfTimer>::Creator mCreator;
ThreadLocal<PerfTimer>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<Random>
```cpp
/* 31219 */
struct ThreadLocal<Random>
{
ThreadLocal<Random>::Creator mCreator;
ThreadLocal<Random>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<ResourceLoadManager::ResourceLoadTaskGroup *>
```cpp
/* 60806 */
struct ThreadLocal<ResourceLoadManager::ResourceLoadTaskGroup *>
{
ThreadLocal<ResourceLoadManager::ResourceLoadTaskGroup *>::Creator mCreator;
ThreadLocal<ResourceLoadManager::ResourceLoadTaskGroup *>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<TheEndGenerator::ThreadData>
```cpp
/* 289608 */
struct ThreadLocal<TheEndGenerator::ThreadData>
{
ThreadLocal<TheEndGenerator::ThreadData>::Creator mCreator;
ThreadLocal<TheEndGenerator::ThreadData>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<ThreadSpecificData>
```cpp
/* 3052 */
struct ThreadLocal<ThreadSpecificData>
{
ThreadLocal<ThreadSpecificData>::Creator mCreator;
ThreadLocal<ThreadSpecificData>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<bool (**)(const char *,const char *,const char *,bool,int,const char *,const char *,bool)>
```cpp
/* 480591 */
struct ThreadLocal<bool (**)(const char *,const char *,const char *,bool,int,const char *,const char *,bool)>
{
ThreadLocal<bool (**)(const char *,const char *,const char *,bool,int,const char *,const char *,bool)>::Creator mCreator;
ThreadLocal<bool (**)(const char *,const char *,const char *,bool,int,const char *,const char *,bool)>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### Tick
```cpp
/* 5810 */
struct Tick
{
uint64_t tickID;
};

```
#### TickDelayBlock
```cpp
/* 186308 */
struct TickDelayBlock
{
int mTickDelay;
const Block *mBlock;
};

```
#### TickWorldComponent
```cpp
/* 100527 */
struct TickWorldComponent
{
uint32_t mChunkRadius;
float mMaxDistToPlayers;
bool mAlwaysActive;
bool mChanged;
std::weak_ptr<ITickingArea> mTickingArea;
};

```
#### TickingAreaListBase
```cpp
/* 34631 */
struct TickingAreaListBase
{
TickingAreasList mTickingAreas;
};

```
#### TickingAreasManager
```cpp
/* 88095 */
struct TickingAreasManager
{
const DimensionMap *mDimensions;
std::unordered_map<AutomaticID<Dimension,int>,std::vector<PendingArea>> mPendingAreas;
};

```
#### TimeStamp
```cpp
/* 103885 */
struct TimeStamp
{
__int8 gap0[1];
};

```
#### Timer
```cpp
/* 86417 */
struct Timer
{
float mTicksPerSecond;
int mTicks;
float mAlpha;
float mTimeScale;
float mPassedTime;
float mFrameStepAlignmentRemainder;
float mLastTimeSeconds;
float mLastTimestep;
int mLastMs;
int mLastMsSysTime;
float mAdjustTime;
int mSteppingTick;
std::function<int ()> mGetTimeMSCallback;
};

```
#### TimerComponent
```cpp
/* 59635 */
struct TimerComponent
{
int mTime;
uint64_t mTimeStamp;
bool mHasExecuted;
bool mLooping;
int mStartTime;
bool mRandomInterval;
int mMinTime;
int mMaxTime;
DefinitionTrigger mOnTimeDown;
WeightedChoices<float> mTimeChoices;
};

```
#### TintMapColor
```cpp
/* 73857 */
struct TintMapColor
{
std::array<Color,4> colors;
};

```
#### ToolRecipes
```cpp
/* 185263 */
struct ToolRecipes
{
__int8 gap0[1];
};

```
#### TrackerStat
```cpp
/* 63726 */
struct TrackerStat
{
unsigned int sentCount;
unsigned int sentBytes;
unsigned int receivedCount;
unsigned int receivedBytes;
uint32_t sampleNum;
};

```
#### Trade
```cpp
/* 46378 */
struct Trade
{
int mMaxUses;
bool mRewardExperience;
int mWeight;
unsigned int mTraderExperience;
std::vector<std::vector<TradeItem>> mOffer;
std::vector<std::vector<TradeItem>> mReceive;
};

```
#### TradeGroup
```cpp
/* 46366 */
struct TradeGroup
{
int mNumToSelect;
std::vector<Trade> mTrades;
};

```
#### TradeItem
```cpp
/* 46403 */
struct TradeItem
{
int itemId;
int itemAux;
int count_min;
int count_max;
float price_multiplier;
std::vector<std::unique_ptr<LootItemFunction>> functions;
};

```
#### TradeResupplyComponent
```cpp
/* 106683 */
struct TradeResupplyComponent
{
bool mHasResupplied;
};

```
#### TradeTable
```cpp
/* 45372 */
struct TradeTable
{
Core::HeapPathBuffer mPath;
std::vector<TradeTier> mTiers;
};

```
#### TradeTables
```cpp
/* 48724 */
struct TradeTables
{
std::unordered_map<std::string,std::unique_ptr<TradeTable>> mTradeTables;
};

```
#### TradeTier
```cpp
/* 46353 */
struct TradeTier
{
unsigned int mExpToUnlock;
std::vector<TradeGroup> mGroups;
};

```
#### TrailSystem::BlockPositions
```cpp
/* 59928 */
struct TrailSystem::BlockPositions
{
BlockPos mBlockPos[4];
};

```
#### TransformationComponent
```cpp
/* 59948 */
struct TransformationComponent
{
int mDelayTicks;
};

```
#### TreatmentService;
```cpp
/* 5515 */
struct TreatmentService;

```
#### TripodCamera::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 170801 */
struct TripodCamera::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### TropicalFish::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124448 */
struct TropicalFish::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### TropicalFishInfo
```cpp
/* 457003 */
struct TropicalFishInfo
{
int mColor;
int mColor2;
int mVariant;
int mMarkVariant;
std::string mName;
};

```
#### TrustComponent
```cpp
/* 105989 */
struct TrustComponent
{
std::unordered_set<ActorUniqueID> mTrustedPlayerIDs;
};

```
#### TrustingComponent
```cpp
/* 54450 */
struct TrustingComponent
{
float mChance;
std::set<const Item *> mTrustItems;
};

```
#### Tag
```cpp
/* 5811 */
struct Tag
{
int (**_vptr$Tag)(void);
};

```
#### TagCommand::_listTags::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 427378 */
struct TagCommand::_listTags::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### TagIDType;
```cpp
/* 40656 */
struct TagIDType;

```
#### TagMemoryChunk
```cpp
/* 61618 */
struct TagMemoryChunk
{
size_t mElements;
size_t mSize;
std::unique_ptr<unsigned char []> mBuffer;
};

```
#### TagRegistry
```cpp
/* 38394 */
struct TagRegistry
{
std::unordered_map<StringKey,unsigned int> mTagIndexMap;
std::vector<std::string> mTags;
std::vector<IndexSet> mSets;
std::vector<std::string> mTagsScratchpad;
std::vector<IDType<TagIDType>> mTagIDScratchpad;
IndexSet mIndexSetScratchpad;
TagSetID mEmptyTagSet;
};

```
#### TagSetIDType;
```cpp
/* 40657 */
struct TagSetIDType;

```
#### TagsComponent
```cpp
/* 100455 */
struct TagsComponent
{
TagSetID mTagSetID;
};

```
#### TameableComponent
```cpp
/* 54414 */
struct TameableComponent
{
float mChance;
std::set<const Item *> mTameItems;
};

```
#### TargetNearbyComponent
```cpp
/* 59369 */
struct TargetNearbyComponent
{
bool mWasSeenLastTick;
bool mWasInsideRange;
bool mWasOutsideRange;
float mPreviousDistance;
};

```
#### TaskStartInfo
```cpp
/* 63717 */
struct TaskStartInfo
{
string_span name;
std::thread::id affinity;
uint32_t priority;
int priorityBackDown;
TaskOptions options;
std::chrono::_V2::steady_clock::time_point startAtTime;
Bedrock::Threading::IAsyncResult<void>::Handle predecessor;
};

```
#### TeleportComponent
```cpp
/* 59484 */
struct TeleportComponent
{
bool mRandomTeleports;
int mMinTeleportTime;
int mMaxTeleportTime;
Vec3 mRandomTeleportCube;
float mTargetDistance;
float mTargetTeleportChance;
float mLightTeleportChance;
float mDarkTeleportChance;
int mTeleportTime;
};

```
#### Tessellator;
```cpp
/* 122537 */
struct Tessellator;

```
#### TestDedicatedServerCommands
```cpp
/* 5842 */
struct TestDedicatedServerCommands
{
__int8 gap0[1];
};

```
#### TestServerCommands
```cpp
/* 424409 */
struct TestServerCommands
{
__int8 gap0[1];
};

```
#### TextFilteringProcessor;
```cpp
/* 76902 */
struct TextFilteringProcessor;

```
#### TextObjectParser
```cpp
/* 101045 */
struct TextObjectParser
{
__int8 gap0[1];
};

```
#### TextureAtlas;
```cpp
/* 459465 */
struct TextureAtlas;

```
#### TextureAtlasItem
```cpp
/* 103920 */
struct TextureAtlasItem
{
std::string mName;
int mParsedNodeIndex;
std::vector<std::vector<TextureUVCoordinateSet>> mTextureUVs;
};

```
#### TextureItem
```cpp
/* 294387 */
struct TextureItem
{
std::string defaultName;
std::string carriedName;
TextureAtlasItem defaultItem;
TextureAtlasItem carriedItem;
};

```
#### TextureUVCoordinateSet
```cpp
/* 33516 */
struct TextureUVCoordinateSet
{
float weight;
float _u0;
float _v0;
float _u1;
float _v1;
uint16_t _texSizeW;
uint16_t _texSizeH;
ResourceLocation sourceFileLocation;
IsotropicFaceData mIsotropicFaceData;
};

```
#### TheEndBiomeSurface;
```cpp
/* 198714 */
struct TheEndBiomeSurface;

```
#### TheEndGenerator::ThreadData
```cpp
/* 289518 */
struct TheEndGenerator::ThreadData
{
std::array<long,32768> blockBuffer;
};

```
#### ThreadLocal<BackgroundWorker *>
```cpp
/* 485240 */
struct ThreadLocal<BackgroundWorker *>
{
ThreadLocal<BackgroundWorker *>::Creator mCreator;
ThreadLocal<BackgroundWorker *>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<Core::Random>
```cpp
/* 31217 */
struct ThreadLocal<Core::Random>
{
ThreadLocal<Core::Random>::Creator mCreator;
ThreadLocal<Core::Random>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<DBStorageWriteBatch>
```cpp
/* 477455 */
struct ThreadLocal<DBStorageWriteBatch>
{
ThreadLocal<DBStorageWriteBatch>::Creator mCreator;
ThreadLocal<DBStorageWriteBatch>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<EvalParams>
```cpp
/* 109090 */
struct ThreadLocal<EvalParams>
{
ThreadLocal<EvalParams>::Creator mCreator;
ThreadLocal<EvalParams>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<NetherGenerator::ThreadData>
```cpp
/* 36890 */
struct ThreadLocal<NetherGenerator::ThreadData>
{
ThreadLocal<NetherGenerator::ThreadData>::Creator mCreator;
ThreadLocal<NetherGenerator::ThreadData>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<OverworldGenerator::ThreadData>
```cpp
/* 40147 */
struct ThreadLocal<OverworldGenerator::ThreadData>
{
ThreadLocal<OverworldGenerator::ThreadData>::Creator mCreator;
ThreadLocal<OverworldGenerator::ThreadData>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<PerfTimer>
```cpp
/* 102997 */
struct ThreadLocal<PerfTimer>
{
ThreadLocal<PerfTimer>::Creator mCreator;
ThreadLocal<PerfTimer>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<Random>
```cpp
/* 31219 */
struct ThreadLocal<Random>
{
ThreadLocal<Random>::Creator mCreator;
ThreadLocal<Random>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<ResourceLoadManager::ResourceLoadTaskGroup *>
```cpp
/* 60806 */
struct ThreadLocal<ResourceLoadManager::ResourceLoadTaskGroup *>
{
ThreadLocal<ResourceLoadManager::ResourceLoadTaskGroup *>::Creator mCreator;
ThreadLocal<ResourceLoadManager::ResourceLoadTaskGroup *>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<TheEndGenerator::ThreadData>
```cpp
/* 289608 */
struct ThreadLocal<TheEndGenerator::ThreadData>
{
ThreadLocal<TheEndGenerator::ThreadData>::Creator mCreator;
ThreadLocal<TheEndGenerator::ThreadData>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<ThreadSpecificData>
```cpp
/* 3052 */
struct ThreadLocal<ThreadSpecificData>
{
ThreadLocal<ThreadSpecificData>::Creator mCreator;
ThreadLocal<ThreadSpecificData>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### ThreadLocal<bool (**)(const char *,const char *,const char *,bool,int,const char *,const char *,bool)>
```cpp
/* 480591 */
struct ThreadLocal<bool (**)(const char *,const char *,const char *,bool,int,const char *,const char *,bool)>
{
ThreadLocal<bool (**)(const char *,const char *,const char *,bool,int,const char *,const char *,bool)>::Creator mCreator;
ThreadLocal<bool (**)(const char *,const char *,const char *,bool,int,const char *,const char *,bool)>::Pool mPool;
Bedrock::Threading::Mutex mCreatorLock;
bool mInitialized;
pthread_key_t mKey;
};

```
#### Tick
```cpp
/* 5810 */
struct Tick
{
uint64_t tickID;
};

```
#### TickDelayBlock
```cpp
/* 186308 */
struct TickDelayBlock
{
int mTickDelay;
const Block *mBlock;
};

```
#### TickWorldComponent
```cpp
/* 100527 */
struct TickWorldComponent
{
uint32_t mChunkRadius;
float mMaxDistToPlayers;
bool mAlwaysActive;
bool mChanged;
std::weak_ptr<ITickingArea> mTickingArea;
};

```
#### TickingAreaListBase
```cpp
/* 34631 */
struct TickingAreaListBase
{
TickingAreasList mTickingAreas;
};

```
#### TickingAreasManager
```cpp
/* 88095 */
struct TickingAreasManager
{
const DimensionMap *mDimensions;
std::unordered_map<AutomaticID<Dimension,int>,std::vector<PendingArea>> mPendingAreas;
};

```
#### TimeStamp
```cpp
/* 103885 */
struct TimeStamp
{
__int8 gap0[1];
};

```
#### Timer
```cpp
/* 86417 */
struct Timer
{
float mTicksPerSecond;
int mTicks;
float mAlpha;
float mTimeScale;
float mPassedTime;
float mFrameStepAlignmentRemainder;
float mLastTimeSeconds;
float mLastTimestep;
int mLastMs;
int mLastMsSysTime;
float mAdjustTime;
int mSteppingTick;
std::function<int ()> mGetTimeMSCallback;
};

```
#### TimerComponent
```cpp
/* 59635 */
struct TimerComponent
{
int mTime;
uint64_t mTimeStamp;
bool mHasExecuted;
bool mLooping;
int mStartTime;
bool mRandomInterval;
int mMinTime;
int mMaxTime;
DefinitionTrigger mOnTimeDown;
WeightedChoices<float> mTimeChoices;
};

```
#### TintMapColor
```cpp
/* 73857 */
struct TintMapColor
{
std::array<Color,4> colors;
};

```
#### ToolRecipes
```cpp
/* 185263 */
struct ToolRecipes
{
__int8 gap0[1];
};

```
#### TrackerStat
```cpp
/* 63726 */
struct TrackerStat
{
unsigned int sentCount;
unsigned int sentBytes;
unsigned int receivedCount;
unsigned int receivedBytes;
uint32_t sampleNum;
};

```
#### Trade
```cpp
/* 46378 */
struct Trade
{
int mMaxUses;
bool mRewardExperience;
int mWeight;
unsigned int mTraderExperience;
std::vector<std::vector<TradeItem>> mOffer;
std::vector<std::vector<TradeItem>> mReceive;
};

```
#### TradeGroup
```cpp
/* 46366 */
struct TradeGroup
{
int mNumToSelect;
std::vector<Trade> mTrades;
};

```
#### TradeItem
```cpp
/* 46403 */
struct TradeItem
{
int itemId;
int itemAux;
int count_min;
int count_max;
float price_multiplier;
std::vector<std::unique_ptr<LootItemFunction>> functions;
};

```
#### TradeResupplyComponent
```cpp
/* 106683 */
struct TradeResupplyComponent
{
bool mHasResupplied;
};

```
#### TradeTable
```cpp
/* 45372 */
struct TradeTable
{
Core::HeapPathBuffer mPath;
std::vector<TradeTier> mTiers;
};

```
#### TradeTables
```cpp
/* 48724 */
struct TradeTables
{
std::unordered_map<std::string,std::unique_ptr<TradeTable>> mTradeTables;
};

```
#### TradeTier
```cpp
/* 46353 */
struct TradeTier
{
unsigned int mExpToUnlock;
std::vector<TradeGroup> mGroups;
};

```
#### TrailSystem::BlockPositions
```cpp
/* 59928 */
struct TrailSystem::BlockPositions
{
BlockPos mBlockPos[4];
};

```
#### TransformationComponent
```cpp
/* 59948 */
struct TransformationComponent
{
int mDelayTicks;
};

```
#### TreatmentService;
```cpp
/* 5515 */
struct TreatmentService;

```
#### TripodCamera::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 170801 */
struct TripodCamera::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### TropicalFish::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124448 */
struct TropicalFish::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### TropicalFishInfo
```cpp
/* 457003 */
struct TropicalFishInfo
{
int mColor;
int mColor2;
int mVariant;
int mMarkVariant;
std::string mName;
};

```
#### TrustComponent
```cpp
/* 105989 */
struct TrustComponent
{
std::unordered_set<ActorUniqueID> mTrustedPlayerIDs;
};

```
#### TrustingComponent
```cpp
/* 54450 */
struct TrustingComponent
{
float mChance;
std::set<const Item *> mTrustItems;
};

```
