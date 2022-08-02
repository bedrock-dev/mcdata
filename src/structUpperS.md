#### SHPortalRoom::postProcess::$A4BF091F36AB25C4BAD93320DD623D59
```cpp
/* 31937 */
struct SHPortalRoom::postProcess::$A4BF091F36AB25C4BAD93320DD623D59
{
const Block **endPortalEye;
const Block **endPortalNoEye;
};

```
#### SPSCQueue<BatchedNetworkPeer::DataCallback,512>
```cpp
/* 421255 */
struct SPSCQueue<BatchedNetworkPeer::DataCallback,512>
{
Lockless::WeakAtomic<SPSCQueue<BatchedNetworkPeer::DataCallback,512>::Block *> mFrontBlock;
char mCachelineFiller[56];
Lockless::WeakAtomic<SPSCQueue<BatchedNetworkPeer::DataCallback,512>::Block *> mTailBlock;
size_t mLargestBlockSize;
};

```
#### SPSCQueue<BatchedNetworkPeer::DataCallback,512>::Block
```cpp
/* 421196 */
struct SPSCQueue<BatchedNetworkPeer::DataCallback,512>::Block
{
Lockless::WeakAtomic<unsigned long> front;
size_t localTail;
char cachelineFiller0[48];
Lockless::WeakAtomic<unsigned long> tail;
size_t localFront;
char cachelineFiller1[48];
Lockless::WeakAtomic<SPSCQueue<BatchedNetworkPeer::DataCallback,512>::Block *> next;
char *data;
const size_t sizeMask;
char *rawThis;
};

```
#### SaveTransactionManager
```cpp
/* 3012 */
struct SaveTransactionManager
{
SaveTransactionManager::ShowIconFunction mShowIconFunction;
};

```
#### SavedData
```cpp
/* 34295 */
struct SavedData
{
int (**_vptr$SavedData)(void);
bool mDirty;
std::string mId;
};

```
#### SavedDataStorage
```cpp
/* 87726 */
struct SavedDataStorage
{
int (**_vptr$SavedDataStorage)(void);
LevelStorage *levelStorage;
std::unordered_map<std::string,SavedData *> savedDatas;
};

```
#### ScaffoldingClimberDefinition
```cpp
/* 412552 */
struct ScaffoldingClimberDefinition
{
__int8 gap0[1];
};

```
#### ScaleByAgeComponent
```cpp
/* 58652 */
struct ScaleByAgeComponent
{
float mStartScale;
float mEndScale;
};

```
#### ScaleByAgeDefinition
```cpp
/* 107549 */
struct ScaleByAgeDefinition
{
float mStartScale;
float mEndScale;
};

```
#### ScatterParams
```cpp
/* 192991 */
struct ScatterParams
{
ScatterParams::CoordinateRange mX;
ScatterParams::CoordinateRange mZ;
ScatterParams::CoordinateRange mHeight;
ScatterParams::CoordinateEvaluationOrder mEvalOrder;
ScatterParams::ChanceInformation mScatterChance;
ExpressionNode mIterations;
};

```
#### ScatterParams::ChanceInformation
```cpp
/* 192995 */
struct ScatterParams::ChanceInformation
{
ExpressionNode mChancePercent;
int mNumerator;
int mDenominator;
};

```
#### ScatterParams::CoordinateRange
```cpp
/* 192992 */
struct ScatterParams::CoordinateRange
{
ExpressionNode mMinOrSingleValue;
ExpressionNode mMax;
uint32_t mGridStepCount;
ScatterParams::RandomDistributionType mDistribution;
};

```
#### ScatterParams::ScatteredPositions
```cpp
/* 198707 */
struct ScatterParams::ScatteredPositions
{
RenderParams *mMolangParams;
Random *mRandom;
const ScatterParams *mScatterParams;
BlockPos mOrigin;
uint32_t mIterations;
};

```
#### ScatterParams::_getPos::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 457571 */
struct ScatterParams::_getPos::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### ScatterParams::initMolangParams::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 457570 */
struct ScatterParams::initMolangParams::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SceneFactory;
```cpp
/* 81128 */
struct SceneFactory;

```
#### SceneStack;
```cpp
/* 81127 */
struct SceneStack;

```
#### Scheduler
```cpp
/* 4391 */
struct Scheduler
{
uint32_t mTotalFrames;
uint32_t mStarvedFrames;
uint32_t mPromotionFrames;
uint32_t mTargetFPS;
uint32_t mEffectiveFPS;
uint32_t mFramesOverBound;
double mAverageCallbackDuration;
double mTotalCoroutineDuration;
size_t mTotalRunCoroutines;
double mCoroutineTimeLimit;
std::unique_ptr<WorkerPool> mCoroutinePool;
std::chrono::time_point<std::chrono::_V2::system_clock,std::chrono::duration<long,std::ratio<1,1000000000> > > mNextStarveCheckTime;
std::thread::id mThreadID;
};

```
#### Scheduler::ScopedChangeScheduler
```cpp
/* 484341 */
struct Scheduler::ScopedChangeScheduler
{
BackgroundWorker *mParent;
};

```
#### SchedulerComponent
```cpp
/* 58798 */
struct SchedulerComponent
{
int mCurrentEventIndex;
};

```
#### SchedulerDefinition
```cpp
/* 58854 */
struct SchedulerDefinition
{
std::vector<DefinitionTrigger> mTriggerDefs;
unsigned int mMinDelayTicks;
unsigned int mMaxDelayTicks;
};

```
#### ScopedAutoreleasePool
```cpp
/* 87060 */
struct ScopedAutoreleasePool
{
__int8 gap0[1];
};

```
#### ScopedProfileTag
```cpp
/* 103054 */
struct ScopedProfileTag
{
__int8 gap0[1];
};

```
#### ScoreInfo
```cpp
/* 80247 */
struct ScoreInfo
{
const Objective *mObjective;
bool mValid;
int mValue;
};

```
#### ScoreInfoRef
```cpp
/* 80248 */
struct ScoreInfoRef
{
const Objective *mObjective;
bool mValid;
int *mValue;
};

```
#### ScorePacketInfo
```cpp
/* 70049 */
struct ScorePacketInfo
{
ScoreboardId mScoreboardId;
std::string mObjectiveName;
int mScoreValue;
IdentityDefinition::Type mIdentityType;
PlayerScoreboardId mPlayerId;
ActorUniqueID mEntityId;
std::string mFakePlayerName;
};

```
#### Scoreboard
```cpp
/* 80249 */
struct Scoreboard
{
int (**_vptr$Scoreboard)(void);
CommandSoftEnumRegistry mRegistry;
std::unordered_map<std::string,DisplayObjective> mDisplayObjectives;
IdentityDictionary mIdentityDict;
std::unordered_map<ScoreboardId,ScoreboardIdentityRef> mIdentityRefs;
bool mShouldUpdateUI;
std::unordered_map<std::string,std::unique_ptr<Objective>> mObjectives;
std::unordered_map<std::string,std::unique_ptr<ObjectiveCriteria>> mCriteria;
};

```
#### ScoreboardCommand::InitProxy
```cpp
/* 426836 */
struct ScoreboardCommand::InitProxy
{
Scoreboard *mScoreboard;
};

```
#### ScoreboardCommand::SetScoreOutput
```cpp
/* 426837 */
struct ScoreboardCommand::SetScoreOutput
{
int mSuccessCount;
int mFirstNewScore;
std::string mFirstSuccess;
};

```
#### ScoreboardId
```cpp
/* 70050 */
struct ScoreboardId
{
int64_t mRawID;
IdentityDefinition *mIdentityDef;
};

```
#### ScoreboardIdentityPacketInfo
```cpp
/* 70103 */
struct ScoreboardIdentityPacketInfo
{
ScoreboardId mScoreboardId;
PlayerScoreboardId mPlayerId;
};

```
#### ScoreboardIdentityRef
```cpp
/* 80250 */
struct ScoreboardIdentityRef
{
uint32_t mObjectiveReferences;
ScoreboardId mScoreboardId;
};

```
#### ScreenshotOptions
```cpp
/* 35042 */
struct ScreenshotOptions
{
bool mCropToRatio;
int mWidthRatio;
int mHeightRatio;
uint32_t mMaxWidth;
uint32_t mMaxHeight;
bool mRestrictScreenshotSize;
bool mApplySquareFrame;
Core::HeapPathBuffer mRequestedFileName;
Core::HeapPathBuffer mRequestedFilePath;
Core::HeapPathBuffer mRequestedExtension;
bool mReplaceImage;
bool mUseScreenshotsFolder;
bool mHideUI;
bool mLogRequest;
bool mWriteScreenshotToFile;
bool mIsSavegameScreenshot;
Core::HeapPathBuffer mOutFileName;
Core::HeapPathBuffer mOutFileDir;
Core::HeapPathBuffer mOutExtension;
};

```
#### ScriptApi::EMPTYObjectHandle
```cpp
/* 95649 */
struct ScriptApi::EMPTYObjectHandle
{
__int8 gap0[1];
};

```
#### ScriptApi::EventTracking
```cpp
/* 95734 */
struct ScriptApi::EventTracking
{
ScriptApi::ScriptObjectHandle mFunctionObject;
};

```
#### ScriptApi::JavaScriptErrorHandler;
```cpp
/* 95279 */
struct ScriptApi::JavaScriptErrorHandler;

```
#### ScriptApi::ScriptCallbackInterface
```cpp
/* 99153 */
struct ScriptApi::ScriptCallbackInterface
{
int (**_vptr$ScriptCallbackInterface)(void);
};

```
#### ScriptApi::ScriptFramework
```cpp
/* 99152 */
struct ScriptApi::ScriptFramework
{
int (**_vptr$ScriptFramework)(void);
std::unique_ptr<ScriptApi::ScriptLanguageInterface> mLanguageInterface;
std::vector<ScriptApi::ScriptSystemInfo> mScriptSystems;
std::unique_ptr<ScriptApi::ScriptReport> mScriptReportQueue;
};

```
#### ScriptApi::ScriptLanguageInterface
```cpp
/* 97714 */
struct ScriptApi::ScriptLanguageInterface
{
int (**_vptr$ScriptLanguageInterface)(void);
};

```
#### ScriptApi::ScriptReport
```cpp
/* 99141 */
struct ScriptApi::ScriptReport
{
std::vector<std::shared_ptr<ScriptApi::ScriptReportItem>> mReportItems;
};

```
#### ScriptApi::ScriptReportItem
```cpp
/* 95269 */
struct ScriptApi::ScriptReportItem
{
std::string mMessage;
ScriptApi::ScriptReportItemType mType;
std::unique_ptr<ScriptApi::JavaScriptErrorHandler> mErrorHandler;
};

```
#### ScriptApi::ScriptVersionInfo
```cpp
/* 99227 */
struct ScriptApi::ScriptVersionInfo
{
int32_t mMajorVersion;
int32_t mMinVerssion;
};

```
#### ScriptApi::WORKAROUNDS::tempActorComponent
```cpp
/* 423896 */
struct ScriptApi::WORKAROUNDS::tempActorComponent
{
ActorUniqueID mID;
};

```
#### ScriptApi::WORKAROUNDS::tempLevelComponent
```cpp
/* 424122 */
struct ScriptApi::WORKAROUNDS::tempLevelComponent
{
__int8 gap0[1];
};

```
#### ScriptBinderComponent
```cpp
/* 96379 */
struct ScriptBinderComponent
{
int (**_vptr$ScriptBinderComponent)(void);
};

```
#### ScriptBinderTemplate
```cpp
/* 95815 */
struct ScriptBinderTemplate
{
int (**_vptr$ScriptBinderTemplate)(void);
};

```
#### ScriptBinderTemplateController
```cpp
/* 98718 */
struct ScriptBinderTemplateController
{
std::unordered_map<std::string,std::unique_ptr<ScriptBinderTemplate>> mTemplates;
};

```
#### ScriptCommandCallbackData
```cpp
/* 95647 */
struct ScriptCommandCallbackData
{
ScriptApi::ScriptObjectHandle mFunction;
std::string mCommand;
bool mCallbackReceived;
Json::Value mData;
};

```
#### ScriptCommandFactory
```cpp
/* 475676 */
struct ScriptCommandFactory
{
__int8 gap0[1];
};

```
#### ScriptEngine::ScriptQueueData
```cpp
/* 99171 */
struct ScriptEngine::ScriptQueueData
{
Core::HeapPathBuffer mScriptPath;
std::string mScriptName;
std::string mScriptContent;
std::string mPackID;
std::string mPackVersion;
uint64_t mScriptHash;
};

```
#### ScriptEngineWithContext<ScriptServerContext>::createEntity::$C3475C4D5343D48D4C7832305B127EAE
```cpp
/* 99880 */
struct ScriptEngineWithContext<ScriptServerContext>::createEntity::$C3475C4D5343D48D4C7832305B127EAE
{
ScriptEngineWithContext<ScriptServerContext> *this;
ScriptApi::ScriptObjectHandle *entityHandle;
const std::string *templateName;
const ScriptApi::ScriptVersionInfo *info;
};

```
#### ScriptEventData
```cpp
/* 96208 */
struct ScriptEventData
{
int (**_vptr$ScriptEventData)(void);
std::string mEventName;
};

```
#### ScriptEventListener
```cpp
/* 97518 */
struct ScriptEventListener
{
int (**_vptr$ScriptEventListener)(void);
};

```
#### ScriptObjectBinder
```cpp
/* 96427 */
struct ScriptObjectBinder
{
const std::string mTypeIdentifier;
unsigned int mComponentsInUse;
std::vector<std::unique_ptr<ScriptBinderComponent>> mComponents;
};

```
#### ScriptOnlyComponents<ScriptServerContext>
```cpp
/* 99148 */
struct ScriptOnlyComponents<ScriptServerContext>
{
std::map<std::string,Json::Value> mScriptOnlyComponentDefs;
};

```
#### ScriptOnlyComponents<ScriptServerContext>::ScriptOnly
```cpp
/* 97603 */
struct ScriptOnlyComponents<ScriptServerContext>::ScriptOnly
{
std::map<std::string,Json::Value> mLookup;
};

```
#### ScriptOnlyEventsData<ScriptServerContext>
```cpp
/* 99149 */
struct ScriptOnlyEventsData<ScriptServerContext>
{
std::map<std::string,Json::Value> mScriptOnlyEventsData;
};

```
#### ScriptQueries
```cpp
/* 99151 */
struct ScriptQueries
{
entt::DefaultRegistry mRegistryView;
};

```
#### ScriptQueryComponent
```cpp
/* 423826 */
struct ScriptQueryComponent
{
std::unordered_set<std::string> mFilters;
ScriptQueryComponent::ViewType mType;
std::string mSpatialTag;
std::string mCoordinateTags[3];
};

```
#### ScriptServerContext
```cpp
/* 99139 */
struct ScriptServerContext
{
Level *mLevel;
Minecraft *mMinecraft;
PacketSender *mPacketSender;
entt::DefaultRegistry *mRegistry;
ScriptApi::ScriptReport *mScriptReport;
};

```
#### ScriptTemplateFactory<ScriptServerContext>
```cpp
/* 99142 */
struct ScriptTemplateFactory<ScriptServerContext>
{
ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::Entity> mEntities;
ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::Entity> mItemEntities;
ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::Component> mComponents;
ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::ReceivedEvent> mReceivedEvents;
ScriptTemplateFactory<ScriptServerContext>::HashedEntries mScriptEventDatas;
ScriptTemplateFactory<ScriptServerContext>::Entry<ScriptTemplateFactory<ScriptServerContext>::ReceivedEvent> mBroadcastEvent;
};

```
#### ScriptTemplateFactory<ScriptServerContext>::Component
```cpp
/* 95456 */
struct ScriptTemplateFactory<ScriptServerContext>::Component
{
int (**_vptr$Component)(void);
};

```
#### ScriptTemplateFactory<ScriptServerContext>::Entity
```cpp
/* 95381 */
struct ScriptTemplateFactory<ScriptServerContext>::Entity
{
int (**_vptr$Entity)(void);
};

```
#### ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::Component>
```cpp
/* 99144 */
struct ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::Component>
{
std::unordered_map<unsigned long,std::shared_ptr<ScriptTemplateFactory<ScriptServerContext>::Component>> mTemplates;
};

```
#### ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::Entity>
```cpp
/* 99143 */
struct ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::Entity>
{
std::unordered_map<unsigned long,std::shared_ptr<ScriptTemplateFactory<ScriptServerContext>::Entity>> mTemplates;
};

```
#### ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::ReceivedEvent>
```cpp
/* 99145 */
struct ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::ReceivedEvent>
{
std::unordered_map<unsigned long,std::shared_ptr<ScriptTemplateFactory<ScriptServerContext>::ReceivedEvent>> mTemplates;
};

```
#### ScriptTemplateFactory<ScriptServerContext>::HashedEntries
```cpp
/* 99146 */
struct ScriptTemplateFactory<ScriptServerContext>::HashedEntries
{
std::unordered_set<unsigned long> mHashes;
};

```
#### ScriptTemplateFactory<ScriptServerContext>::ReceivedEvent
```cpp
/* 95540 */
struct ScriptTemplateFactory<ScriptServerContext>::ReceivedEvent
{
int (**_vptr$ReceivedEvent)(void);
};

```
#### SearchRequestTelemetry;
```cpp
/* 45324 */
struct SearchRequestTelemetry;

```
#### Seasons
```cpp
/* 34400 */
struct Seasons
{
Dimension *mDimension;
PerlinSimplexNoise mSnowNoise;
};

```
#### SeatDescription
```cpp
/* 55146 */
struct SeatDescription
{
Vec3 mPosition;
int mMinSeatCount;
int mMaxSeatCount;
float mSeatRotation;
bool mLockRiderRotation;
float mLockRiderRotationDegrees;
};

```
#### SecureStorage
```cpp
/* 479501 */
struct SecureStorage
{
int (**_vptr$SecureStorage)(void);
};

```
#### SelectorIterator<Actor>
```cpp
/* 90959 */
struct SelectorIterator<Actor>
{
CommandResultVector mTargets;
std::vector<Actor *>::iterator mIndex;
};

```
#### SelectorIterator<Player>
```cpp
/* 33510 */
struct SelectorIterator<Player>
{
CommandResultVector mTargets;
std::vector<Actor *>::iterator mIndex;
};

```
#### SemVersion::any_version_constructor
```cpp
/* 5623 */
struct SemVersion::any_version_constructor
{
__int8 gap0[1];
};

```
#### SendEventData
```cpp
/* 88826 */
struct SendEventData
{
float minActivationRange;
float maxActivationRange;
int cooldownTime;
int castDuration;
float weight;
bool doCastingAnimation;
int particleColor;
ActorFilterGroup targetFilter;
LevelSoundEvent startSound;
std::vector<SendEventStage> stages;
};

```
#### SensingComponent
```cpp
/* 58948 */
struct SensingComponent
{
SensingComponent::ActorSet mSeen;
SensingComponent::ActorSet mUnseen;
};

```
#### SerializedPersonaPieceHandle
```cpp
/* 74272 */
struct SerializedPersonaPieceHandle
{
std::string mPieceId;
persona::PieceType mPieceType;
mce::UUID mPackId;
bool mIsDefaultPiece;
std::string mProductId;
};

```
#### SerializedSkin
```cpp
/* 74239 */
struct SerializedSkin
{
std::string mId;
std::string fullId;
std::string mResourcePatch;
std::string mDefaultGeometryName;
mce::Image mSkinImage;
mce::Image mCapeImage;
std::vector<AnimatedImageData> mSkinAnimatedImages;
Json::Value mGeometryData;
Json::Value mGeometryDataMutable;
std::string mAnimationData;
std::string mCapeId;
bool mIsPremium;
bool mIsPersona;
bool mIsPersonaCapeOnClassicSkin;
TrustedSkinFlag mIsTrustedSkin;
std::vector<SerializedPersonaPieceHandle> mPersonaPieces;
std::string mArmSize;
std::unordered_map<persona::PieceType,TintMapColor> mPieceTintColors;
Color mSkinColor;
};

```
#### SerializedSkin_0
```cpp
/* 173180 */
struct SerializedSkin_0
{
std::string mId;
std::string fullId;
std::string mResourcePatch;
std::string mDefaultGeometryName;
mce::Image_0 mSkinImage;
mce::Image_0 mCapeImage;
std::vector<AnimatedImageData>_0 mSkinAnimatedImages;
Json::Value mGeometryData;
Json::Value mGeometryDataMutable;
std::string mAnimationData;
std::string mCapeId;
bool mIsPremium;
bool mIsPersona;
bool mIsPersonaCapeOnClassicSkin;
TrustedSkinFlag mIsTrustedSkin;
std::vector<SerializedPersonaPieceHandle> mPersonaPieces;
std::string mArmSize;
std::unordered_map<persona::PieceType,TintMapColor> mPieceTintColors;
Color mSkinColor;
};

```
#### ServerCommunicationInterface
```cpp
/* 4257 */
struct ServerCommunicationInterface
{
std::unique_ptr<RakNet::TCPInterface> mTCPConnection;
RakNet::SystemAddress mHostAddress;
};

```
#### ServerInstance::initializeServer::$1AF53268373D8F94D8C5F1843C50C698
```cpp
/* 87054 */
struct ServerInstance::initializeServer::$1AF53268373D8F94D8C5F1843C50C698
{
std::unordered_map<PackIdVersion,std::string> *packIdToContentKey;
ResourcePackRepository *resourcePackRepository;
};

```
#### ServerLocator
```cpp
/* 63710 */
struct ServerLocator
{
int (**_vptr$ServerLocator)(void);
};

```
#### ServerMetrics
```cpp
/* 8550 */
struct ServerMetrics
{
int (**_vptr$ServerMetrics)(void);
};

```
#### ServerMetricsImpl::DataTransferred
```cpp
/* 8105 */
struct ServerMetricsImpl::DataTransferred
{
uint64_t totalBytesReceived;
uint64_t totalBytesSent;
};

```
#### ServerNetworkHandler::Client
```cpp
/* 73788 */
struct ServerNetworkHandler::Client
{
std::unique_ptr<ConnectionRequest> mPrimaryRequest;
std::unordered_map<unsigned char,std::unique_ptr<SubClientConnectionRequest>> mSubClientRequests;
};

```
#### ServerNetworkHandler::_getActiveAndInProgressPlayerCount::$0EBB06E09BB4D485483DF06B22BB4AE5
```cpp
/* 77491 */
struct ServerNetworkHandler::_getActiveAndInProgressPlayerCount::$0EBB06E09BB4D485483DF06B22BB4AE5
{
const ServerNetworkHandler *this;
mce::UUID *excludePlayer;
int *numPlayers;
};

```
#### ServerNetworkHandler::_onClientAuthenticated::$40782884DF021EB8A0B68AECF65B4504
```cpp
/* 77489 */
struct ServerNetworkHandler::_onClientAuthenticated::$40782884DF021EB8A0B68AECF65B4504
{
ServerNetworkHandler *this;
};

```
#### ServerNetworkHandler::handle::$3CDCE61CA261A057C80CC046802E365C
```cpp
/* 77437 */
struct ServerNetworkHandler::handle::$3CDCE61CA261A057C80CC046802E365C
{
ServerNetworkHandler *this;
const NetworkIdentifier *source;
std::set<std::string> *downloading;
};

```
#### ServerNetworkHandler::handle::$ED428D87CD11B947B517AB43C0D6E540
```cpp
/* 76956 */
struct ServerNetworkHandler::handle::$ED428D87CD11B947B517AB43C0D6E540
{
ServerNetworkHandler *this;
const NetworkIdentifier source;
};

```
#### ServerPlayer::NearbyActor
```cpp
/* 89356 */
struct ServerPlayer::NearbyActor
{
bool isAutonomous;
ServerPlayer::NearbyActor::State state;
Actor *tempActor;
};

```
#### ServerPlayer::recoverR5LostInventoryAndXP::$566869B8F3A3697DD8479CC05753D205
```cpp
/* 90647 */
struct ServerPlayer::recoverR5LostInventoryAndXP::$566869B8F3A3697DD8479CC05753D205
{
std::vector<BlockPos> chestPositions;
};

```
#### ServerScoreboard::unit_test_ctor_t
```cpp
/* 294173 */
struct ServerScoreboard::unit_test_ctor_t
{
__int8 gap0[1];
};

```
#### ServiceLocator<AppConfigs>
```cpp
/* 5585 */
struct ServiceLocator<AppConfigs>
{
__int8 gap0[1];
};

```
#### ServiceLocator<AppPlatform>
```cpp
/* 5584 */
struct ServiceLocator<AppPlatform>
{
__int8 gap0[1];
};

```
#### ServiceLocator<ContentLog>
```cpp
/* 5586 */
struct ServiceLocator<ContentLog>
{
__int8 gap0[1];
};

```
#### ServiceLocator<Core::LoadTimeProfiler>
```cpp
/* 480120 */
struct ServiceLocator<Core::LoadTimeProfiler>
{
__int8 gap0[1];
};

```
#### ServiceLocator<EducationOptions>
```cpp
/* 81171 */
struct ServiceLocator<EducationOptions>
{
__int8 gap0[1];
};

```
#### ServiceLocator<FeatureToggles>
```cpp
/* 77439 */
struct ServiceLocator<FeatureToggles>
{
__int8 gap0[1];
};

```
#### ServiceLocator<IMinecraftEventing>
```cpp
/* 45361 */
struct ServiceLocator<IMinecraftEventing>
{
__int8 gap0[1];
};

```
#### ServiceLocator<NetworkDebugManager>
```cpp
/* 64308 */
struct ServiceLocator<NetworkDebugManager>
{
__int8 gap0[1];
};

```
#### ServiceLocator<PackManifest::CapabilityRegistry>
```cpp
/* 82679 */
struct ServiceLocator<PackManifest::CapabilityRegistry>
{
__int8 gap0[1];
};

```
#### ServiceLocator<ServerInstance>
```cpp
/* 87055 */
struct ServiceLocator<ServerInstance>
{
__int8 gap0[1];
};

```
#### ServiceOverrider<bool (*)(const char *,const char *,const char *,bool,int,const char *,const char *,bool)>
```cpp
/* 480590 */
struct ServiceOverrider<bool (*)(const char *,const char *,const char *,bool,int,const char *,const char *,bool)>
{
ThreadLocal<bool (**)(const char *,const char *,const char *,bool,int,const char *,const char *,bool)> mService;
bool (**mDefaultService)(const char *, const char *, const char *, bool, int, const char *, const char *, bool);
};

```
#### SharePtrRefTraits<PerlinSimplexNoise>
```cpp
/* 191523 */
struct SharePtrRefTraits<PerlinSimplexNoise>
{
__int8 gap0[1];
};

```
#### Shareable
```cpp
/* 417212 */
struct Shareable
{
int itemId;
int itemAux;
int wantAmount;
int surplusAmount;
int maxAmount;
int craftIntoItem;
int craftIntoItemAux;
int itemPriority;
};

```
#### ShareableDefinition
```cpp
/* 116674 */
struct ShareableDefinition
{
std::vector<Shareable> mItems;
bool mShareAllItems;
int mAllItemWantAmount;
int mAllItemSurplusAmount;
int mAllItemMaxAmount;
};

```
#### SharedAmplifiers
```cpp
/* 174643 */
struct SharedAmplifiers
{
__int8 gap0[1];
};

```
#### SharedAttributes
```cpp
/* 174606 */
struct SharedAttributes
{
__int8 gap0[1];
};

```
#### SharedBuffs
```cpp
/* 174644 */
struct SharedBuffs
{
__int8 gap0[1];
};

```
#### SharedCounter<ActivatorRailBlock>
```cpp
/* 251389 */
struct SharedCounter<ActivatorRailBlock>
{
ActivatorRailBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<AirBlock>
```cpp
/* 250879 */
struct SharedCounter<AirBlock>
{
AirBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<AirBlockItem>
```cpp
/* 180756 */
struct SharedCounter<AirBlockItem>
{
AirBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<AnvilBlock>
```cpp
/* 251440 */
struct SharedCounter<AnvilBlock>
{
AnvilBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ArmorItem>
```cpp
/* 183817 */
struct SharedCounter<ArmorItem>
{
ArmorItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ArmorStandItem>
```cpp
/* 183950 */
struct SharedCounter<ArmorStandItem>
{
ArmorStandItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ArrowItem>
```cpp
/* 183797 */
struct SharedCounter<ArrowItem>
{
ArrowItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<AuxDataBlockItem>
```cpp
/* 184012 */
struct SharedCounter<AuxDataBlockItem>
{
AuxDataBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BalloonItem>
```cpp
/* 183996 */
struct SharedCounter<BalloonItem>
{
BalloonItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BambooBlock>
```cpp
/* 251696 */
struct SharedCounter<BambooBlock>
{
BambooBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BambooBlockItem>
```cpp
/* 184057 */
struct SharedCounter<BambooBlockItem>
{
BambooBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BambooSapling>
```cpp
/* 251700 */
struct SharedCounter<BambooSapling>
{
BambooSapling *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BannerBlock>
```cpp
/* 251511 */
struct SharedCounter<BannerBlock>
{
BannerBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BannerItem>
```cpp
/* 183965 */
struct SharedCounter<BannerItem>
{
BannerItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BannerPatternItem>
```cpp
/* 183973 */
struct SharedCounter<BannerPatternItem>
{
BannerPatternItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BarrelBlock>
```cpp
/* 251731 */
struct SharedCounter<BarrelBlock>
{
BarrelBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BarrierBlock>
```cpp
/* 251688 */
struct SharedCounter<BarrierBlock>
{
BarrierBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BeaconBlock>
```cpp
/* 251412 */
struct SharedCounter<BeaconBlock>
{
BeaconBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BedBlock>
```cpp
/* 251128 */
struct SharedCounter<BedBlock>
{
BedBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BedItem>
```cpp
/* 183876 */
struct SharedCounter<BedItem>
{
BedItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BedrockBlock>
```cpp
/* 251076 */
struct SharedCounter<BedrockBlock>
{
BedrockBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BeehiveBlock>
```cpp
/* 251774 */
struct SharedCounter<BeehiveBlock>
{
BeehiveBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BeetrootBlock>
```cpp
/* 251591 */
struct SharedCounter<BeetrootBlock>
{
BeetrootBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BellBlock>
```cpp
/* 251739 */
struct SharedCounter<BellBlock>
{
BellBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BellBlockItem>
```cpp
/* 184065 */
struct SharedCounter<BellBlockItem>
{
BellBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BlastFurnaceBlock>
```cpp
/* 251719 */
struct SharedCounter<BlastFurnaceBlock>
{
BlastFurnaceBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BlockItem>
```cpp
/* 182765 */
struct SharedCounter<BlockItem>
{
BlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BlockLegacy>
```cpp
/* 13208 */
struct SharedCounter<BlockLegacy>
{
BlockLegacy *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BlockPlanterItem>
```cpp
/* 183809 */
struct SharedCounter<BlockPlanterItem>
{
BlockPlanterItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BlueIceBlock>
```cpp
/* 251619 */
struct SharedCounter<BlueIceBlock>
{
BlueIceBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BoatItem>
```cpp
/* 183851 */
struct SharedCounter<BoatItem>
{
BoatItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BookshelfBlock>
```cpp
/* 251181 */
struct SharedCounter<BookshelfBlock>
{
BookshelfBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BottleItem>
```cpp
/* 183894 */
struct SharedCounter<BottleItem>
{
BottleItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BowItem>
```cpp
/* 183793 */
struct SharedCounter<BowItem>
{
BowItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BrewingStandBlock>
```cpp
/* 251362 */
struct SharedCounter<BrewingStandBlock>
{
BrewingStandBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BubbleColumnBlock>
```cpp
/* 251680 */
struct SharedCounter<BubbleColumnBlock>
{
BubbleColumnBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BucketItem>
```cpp
/* 183835 */
struct SharedCounter<BucketItem>
{
BucketItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CactusBlock>
```cpp
/* 251267 */
struct SharedCounter<CactusBlock>
{
CactusBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CakeBlock>
```cpp
/* 251302 */
struct SharedCounter<CakeBlock>
{
CakeBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CameraBlock>
```cpp
/* 251583 */
struct SharedCounter<CameraBlock>
{
CameraBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CameraItem>
```cpp
/* 183979 */
struct SharedCounter<CameraItem>
{
CameraItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CampfireBlock>
```cpp
/* 251751 */
struct SharedCounter<CampfireBlock>
{
CampfireBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CarrotBlock>
```cpp
/* 251424 */
struct SharedCounter<CarrotBlock>
{
CarrotBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CarrotOnAStickItem>
```cpp
/* 183928 */
struct SharedCounter<CarrotOnAStickItem>
{
CarrotOnAStickItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CartographyTableBlock>
```cpp
/* 251727 */
struct SharedCounter<CartographyTableBlock>
{
CartographyTableBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CauldronBlock>
```cpp
/* 251366 */
struct SharedCounter<CauldronBlock>
{
CauldronBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ChemicalHeatBlock>
```cpp
/* 251633 */
struct SharedCounter<ChemicalHeatBlock>
{
ChemicalHeatBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ChemistryAuxDataBlockItem>
```cpp
/* 184069 */
struct SharedCounter<ChemistryAuxDataBlockItem>
{
ChemistryAuxDataBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ChemistryItem>
```cpp
/* 183990 */
struct SharedCounter<ChemistryItem>
{
ChemistryItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ChemistryTableBlock>
```cpp
/* 251626 */
struct SharedCounter<ChemistryTableBlock>
{
ChemistryTableBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ChestBlock>
```cpp
/* 251200 */
struct SharedCounter<ChestBlock>
{
ChestBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ChorusFlowerBlock>
```cpp
/* 251527 */
struct SharedCounter<ChorusFlowerBlock>
{
ChorusFlowerBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ChorusPlantBlock>
```cpp
/* 251575 */
struct SharedCounter<ChorusPlantBlock>
{
ChorusPlantBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ClayBlock>
```cpp
/* 251271 */
struct SharedCounter<ClayBlock>
{
ClayBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ClockItem>
```cpp
/* 183870 */
struct SharedCounter<ClockItem>
{
ClockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ClothBlock>
```cpp
/* 251158 */
struct SharedCounter<ClothBlock>
{
ClothBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ClothBlockItem>
```cpp
/* 184016 */
struct SharedCounter<ClothBlockItem>
{
ClothBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CoalItem>
```cpp
/* 183801 */
struct SharedCounter<CoalItem>
{
CoalItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CocoaBlock>
```cpp
/* 251393 */
struct SharedCounter<CocoaBlock>
{
CocoaBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ColoredBlock>
```cpp
/* 251471 */
struct SharedCounter<ColoredBlock>
{
ColoredBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ColoredTorchBlock>
```cpp
/* 251637 */
struct SharedCounter<ColoredTorchBlock>
{
ColoredTorchBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CommandBlock>
```cpp
/* 251409 */
struct SharedCounter<CommandBlock>
{
CommandBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ComparatorBlock>
```cpp
/* 251448 */
struct SharedCounter<ComparatorBlock>
{
ComparatorBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CompassItem>
```cpp
/* 183863 */
struct SharedCounter<CompassItem>
{
CompassItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ComposterBlock>
```cpp
/* 251763 */
struct SharedCounter<ComposterBlock>
{
ComposterBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CompoundItem>
```cpp
/* 183983 */
struct SharedCounter<CompoundItem>
{
CompoundItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ConcreteBlock>
```cpp
/* 251567 */
struct SharedCounter<ConcreteBlock>
{
ConcreteBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ConcretePowderBlock>
```cpp
/* 251571 */
struct SharedCounter<ConcretePowderBlock>
{
ConcretePowderBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ConduitBlock>
```cpp
/* 251676 */
struct SharedCounter<ConduitBlock>
{
ConduitBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<Coral>
```cpp
/* 251644 */
struct SharedCounter<Coral>
{
Coral *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CoralBlock>
```cpp
/* 251648 */
struct SharedCounter<CoralBlock>
{
CoralBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CoralFan>
```cpp
/* 251652 */
struct SharedCounter<CoralFan>
{
CoralFan *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CoralFanBlockItem>
```cpp
/* 184025 */
struct SharedCounter<CoralFanBlockItem>
{
CoralFanBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CoralFanHang>
```cpp
/* 251656 */
struct SharedCounter<CoralFanHang>
{
CoralFanHang *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CropBlock>
```cpp
/* 251211 */
struct SharedCounter<CropBlock>
{
CropBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CrossbowItem>
```cpp
/* 183969 */
struct SharedCounter<CrossbowItem>
{
CrossbowItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DaylightDetectorBlock>
```cpp
/* 251452 */
struct SharedCounter<DaylightDetectorBlock>
{
DaylightDetectorBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DeadBush>
```cpp
/* 251150 */
struct SharedCounter<DeadBush>
{
DeadBush *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DetectorRailBlock>
```cpp
/* 251135 */
struct SharedCounter<DetectorRailBlock>
{
DetectorRailBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DirtBlock>
```cpp
/* 251064 */
struct SharedCounter<DirtBlock>
{
DirtBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DispenserBlock>
```cpp
/* 251116 */
struct SharedCounter<DispenserBlock>
{
DispenserBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DoorBlock>
```cpp
/* 251226 */
struct SharedCounter<DoorBlock>
{
DoorBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DoorItem>
```cpp
/* 183831 */
struct SharedCounter<DoorItem>
{
DoorItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DoublePlantBlock>
```cpp
/* 251507 */
struct SharedCounter<DoublePlantBlock>
{
DoublePlantBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DragonEggBlock>
```cpp
/* 251377 */
struct SharedCounter<DragonEggBlock>
{
DragonEggBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DriedKelpBlock>
```cpp
/* 251664 */
struct SharedCounter<DriedKelpBlock>
{
DriedKelpBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DropperBlock>
```cpp
/* 251385 */
struct SharedCounter<DropperBlock>
{
DropperBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DyePowderItem>
```cpp
/* 183873 */
struct SharedCounter<DyePowderItem>
{
DyePowderItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EggItem>
```cpp
/* 183859 */
struct SharedCounter<EggItem>
{
EggItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ElementBlock>
```cpp
/* 251641 */
struct SharedCounter<ElementBlock>
{
ElementBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ElementBlockItem>
```cpp
/* 184073 */
struct SharedCounter<ElementBlockItem>
{
ElementBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EmptyMapItem>
```cpp
/* 183921 */
struct SharedCounter<EmptyMapItem>
{
EmptyMapItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EnchantedBookItem>
```cpp
/* 183855 */
struct SharedCounter<EnchantedBookItem>
{
EnchantedBookItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EnchantingTableBlock>
```cpp
/* 251358 */
struct SharedCounter<EnchantingTableBlock>
{
EnchantingTableBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EndCrystalItem>
```cpp
/* 183954 */
struct SharedCounter<EndCrystalItem>
{
EndCrystalItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EndGatewayBlock>
```cpp
/* 251543 */
struct SharedCounter<EndGatewayBlock>
{
EndGatewayBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EndPortalBlock>
```cpp
/* 251369 */
struct SharedCounter<EndPortalBlock>
{
EndPortalBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EndPortalFrameBlock>
```cpp
/* 251373 */
struct SharedCounter<EndPortalFrameBlock>
{
EndPortalFrameBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EndRodBlock>
```cpp
/* 251539 */
struct SharedCounter<EndRodBlock>
{
EndRodBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EnderChestBlock>
```cpp
/* 251397 */
struct SharedCounter<EnderChestBlock>
{
EnderChestBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EnderEyeItem>
```cpp
/* 183898 */
struct SharedCounter<EnderEyeItem>
{
EnderEyeItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EnderpearlItem>
```cpp
/* 183887 */
struct SharedCounter<EnderpearlItem>
{
EnderpearlItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ExperiencePotionItem>
```cpp
/* 183905 */
struct SharedCounter<ExperiencePotionItem>
{
ExperiencePotionItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FarmBlock>
```cpp
/* 251215 */
struct SharedCounter<FarmBlock>
{
FarmBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FenceBlock>
```cpp
/* 251283 */
struct SharedCounter<FenceBlock>
{
FenceBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FenceGateBlock>
```cpp
/* 251342 */
struct SharedCounter<FenceGateBlock>
{
FenceGateBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FireBlock>
```cpp
/* 251623 */
struct SharedCounter<FireBlock>
{
FireBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FireChargeItem>
```cpp
/* 183909 */
struct SharedCounter<FireChargeItem>
{
FireChargeItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FireworkChargeItem>
```cpp
/* 183935 */
struct SharedCounter<FireworkChargeItem>
{
FireworkChargeItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FireworksItem>
```cpp
/* 183932 */
struct SharedCounter<FireworksItem>
{
FireworksItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FishingRodItem>
```cpp
/* 183866 */
struct SharedCounter<FishingRodItem>
{
FishingRodItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FlintAndSteelItem>
```cpp
/* 183789 */
struct SharedCounter<FlintAndSteelItem>
{
FlintAndSteelItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FlowerBlock>
```cpp
/* 251162 */
struct SharedCounter<FlowerBlock>
{
FlowerBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FlowerPotBlock>
```cpp
/* 251420 */
struct SharedCounter<FlowerPotBlock>
{
FlowerPotBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FrostedIceBlock>
```cpp
/* 251535 */
struct SharedCounter<FrostedIceBlock>
{
FrostedIceBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FurnaceBlock>
```cpp
/* 251218 */
struct SharedCounter<FurnaceBlock>
{
FurnaceBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<GlassBlock>
```cpp
/* 251112 */
struct SharedCounter<GlassBlock>
{
GlassBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<GlazedTerracottaBlock>
```cpp
/* 251563 */
struct SharedCounter<GlazedTerracottaBlock>
{
GlazedTerracottaBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<GlowStickItem>
```cpp
/* 184008 */
struct SharedCounter<GlowStickItem>
{
GlowStickItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<GrassBlock>
```cpp
/* 251060 */
struct SharedCounter<GrassBlock>
{
GrassBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<GrassPathBlock>
```cpp
/* 251519 */
struct SharedCounter<GrassPathBlock>
{
GrassPathBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<GravelBlock>
```cpp
/* 251092 */
struct SharedCounter<GravelBlock>
{
GravelBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<GrindstoneBlock>
```cpp
/* 251715 */
struct SharedCounter<GrindstoneBlock>
{
GrindstoneBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HangingActorItem>
```cpp
/* 183823 */
struct SharedCounter<HangingActorItem>
{
HangingActorItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HatchetItem>
```cpp
/* 183785 */
struct SharedCounter<HatchetItem>
{
HatchetItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HayBlockBlock>
```cpp
/* 251499 */
struct SharedCounter<HayBlockBlock>
{
HayBlockBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HoeItem>
```cpp
/* 183813 */
struct SharedCounter<HoeItem>
{
HoeItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HoneyBlock>
```cpp
/* 251777 */
struct SharedCounter<HoneyBlock>
{
HoneyBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HoneycombBlock>
```cpp
/* 251781 */
struct SharedCounter<HoneycombBlock>
{
HoneycombBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HopperBlock>
```cpp
/* 251459 */
struct SharedCounter<HopperBlock>
{
HopperBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HorseArmorItem>
```cpp
/* 183938 */
struct SharedCounter<HorseArmorItem>
{
HorseArmorItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HugeMushroomBlock>
```cpp
/* 251323 */
struct SharedCounter<HugeMushroomBlock>
{
HugeMushroomBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<IceBlock>
```cpp
/* 251259 */
struct SharedCounter<IceBlock>
{
IceBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<IceBombItem>
```cpp
/* 183986 */
struct SharedCounter<IceBombItem>
{
IceBombItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<InvisibleBlock>
```cpp
/* 251308 */
struct SharedCounter<InvisibleBlock>
{
InvisibleBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<Item>
```cpp
/* 13202 */
struct SharedCounter<Item>
{
Item *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ItemFrameBlock>
```cpp
/* 251523 */
struct SharedCounter<ItemFrameBlock>
{
ItemFrameBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<JigsawBlock>
```cpp
/* 251755 */
struct SharedCounter<JigsawBlock>
{
JigsawBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<JukeboxBlock>
```cpp
/* 251279 */
struct SharedCounter<JukeboxBlock>
{
JukeboxBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<KelpBlock>
```cpp
/* 251660 */
struct SharedCounter<KelpBlock>
{
KelpBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LadderBlock>
```cpp
/* 251229 */
struct SharedCounter<LadderBlock>
{
LadderBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LanternBlock>
```cpp
/* 251747 */
struct SharedCounter<LanternBlock>
{
LanternBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LeadItem>
```cpp
/* 183947 */
struct SharedCounter<LeadItem>
{
LeadItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LeafBlockItem>
```cpp
/* 184037 */
struct SharedCounter<LeafBlockItem>
{
LeafBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LecternBlock>
```cpp
/* 251712 */
struct SharedCounter<LecternBlock>
{
LecternBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LeverBlock>
```cpp
/* 251237 */
struct SharedCounter<LeverBlock>
{
LeverBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LightBlock>
```cpp
/* 251766 */
struct SharedCounter<LightBlock>
{
LightBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LightGemBlock>
```cpp
/* 251295 */
struct SharedCounter<LightGemBlock>
{
LightGemBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LingeringPotionItem>
```cpp
/* 183961 */
struct SharedCounter<LingeringPotionItem>
{
LingeringPotionItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LiquidBlockDynamic>
```cpp
/* 251080 */
struct SharedCounter<LiquidBlockDynamic>
{
LiquidBlockDynamic *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LiquidBlockStatic>
```cpp
/* 251084 */
struct SharedCounter<LiquidBlockStatic>
{
LiquidBlockStatic *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LoomBlock>
```cpp
/* 251735 */
struct SharedCounter<LoomBlock>
{
LoomBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MagmaBlock>
```cpp
/* 251547 */
struct SharedCounter<MagmaBlock>
{
MagmaBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MapItem>
```cpp
/* 183880 */
struct SharedCounter<MapItem>
{
MapItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MedicineItem>
```cpp
/* 184000 */
struct SharedCounter<MedicineItem>
{
MedicineItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MelonBlock>
```cpp
/* 251330 */
struct SharedCounter<MelonBlock>
{
MelonBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MetalBlock>
```cpp
/* 251169 */
struct SharedCounter<MetalBlock>
{
MetalBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MinecartItem>
```cpp
/* 183839 */
struct SharedCounter<MinecartItem>
{
MinecartItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MobPlacerItem>
```cpp
/* 183902 */
struct SharedCounter<MobPlacerItem>
{
MobPlacerItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MobSpawnerBlock>
```cpp
/* 251193 */
struct SharedCounter<MobSpawnerBlock>
{
MobSpawnerBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MonsterEggBlock>
```cpp
/* 251316 */
struct SharedCounter<MonsterEggBlock>
{
MonsterEggBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MovingBlock>
```cpp
/* 251603 */
struct SharedCounter<MovingBlock>
{
MovingBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MushroomBlock>
```cpp
/* 251165 */
struct SharedCounter<MushroomBlock>
{
MushroomBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MyceliumBlock>
```cpp
/* 251346 */
struct SharedCounter<MyceliumBlock>
{
MyceliumBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<NetherReactorBlock>
```cpp
/* 251599 */
struct SharedCounter<NetherReactorBlock>
{
NetherReactorBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<NetherWartBlock>
```cpp
/* 251354 */
struct SharedCounter<NetherWartBlock>
{
NetherWartBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<NewLeafBlock>
```cpp
/* 251479 */
struct SharedCounter<NewLeafBlock>
{
NewLeafBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<NewLogBlock>
```cpp
/* 251483 */
struct SharedCounter<NewLogBlock>
{
NewLogBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<NoteBlock>
```cpp
/* 251124 */
struct SharedCounter<NoteBlock>
{
NoteBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ObserverBlock>
```cpp
/* 251607 */
struct SharedCounter<ObserverBlock>
{
ObserverBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ObsidianBlock>
```cpp
/* 251185 */
struct SharedCounter<ObsidianBlock>
{
ObsidianBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<OldLeafBlock>
```cpp
/* 251104 */
struct SharedCounter<OldLeafBlock>
{
OldLeafBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<OldLogBlock>
```cpp
/* 251100 */
struct SharedCounter<OldLogBlock>
{
OldLogBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<OreBlock>
```cpp
/* 251096 */
struct SharedCounter<OreBlock>
{
OreBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PickaxeItem>
```cpp
/* 183781 */
struct SharedCounter<PickaxeItem>
{
PickaxeItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PistonArmBlock>
```cpp
/* 251154 */
struct SharedCounter<PistonArmBlock>
{
PistonArmBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PistonBlock>
```cpp
/* 251139 */
struct SharedCounter<PistonBlock>
{
PistonBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PlanksBlock>
```cpp
/* 251068 */
struct SharedCounter<PlanksBlock>
{
PlanksBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PodzolBlock>
```cpp
/* 251587 */
struct SharedCounter<PodzolBlock>
{
PodzolBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PortalBlock>
```cpp
/* 251299 */
struct SharedCounter<PortalBlock>
{
PortalBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PotatoBlock>
```cpp
/* 251428 */
struct SharedCounter<PotatoBlock>
{
PotatoBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PotionItem>
```cpp
/* 183891 */
struct SharedCounter<PotionItem>
{
PotionItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PoweredRailBlock>
```cpp
/* 251131 */
struct SharedCounter<PoweredRailBlock>
{
PoweredRailBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PressurePlateBlock>
```cpp
/* 251241 */
struct SharedCounter<PressurePlateBlock>
{
PressurePlateBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PrismarineBlock>
```cpp
/* 251491 */
struct SharedCounter<PrismarineBlock>
{
PrismarineBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PumpkinBlock>
```cpp
/* 251287 */
struct SharedCounter<PumpkinBlock>
{
PumpkinBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<QuartzBlockBlock>
```cpp
/* 251463 */
struct SharedCounter<QuartzBlockBlock>
{
QuartzBlockBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RailBlock>
```cpp
/* 251233 */
struct SharedCounter<RailBlock>
{
RailBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RapidFertilizerItem>
```cpp
/* 183993 */
struct SharedCounter<RapidFertilizerItem>
{
RapidFertilizerItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RecordItem>
```cpp
/* 183941 */
struct SharedCounter<RecordItem>
{
RecordItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RedStoneDustItem>
```cpp
/* 183843 */
struct SharedCounter<RedStoneDustItem>
{
RedStoneDustItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RedStoneOreBlock>
```cpp
/* 251244 */
struct SharedCounter<RedStoneOreBlock>
{
RedStoneOreBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RedStoneWireBlock>
```cpp
/* 251203 */
struct SharedCounter<RedStoneWireBlock>
{
RedStoneWireBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RedstoneBlock>
```cpp
/* 251455 */
struct SharedCounter<RedstoneBlock>
{
RedstoneBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RedstoneLampBlock>
```cpp
/* 251381 */
struct SharedCounter<RedstoneLampBlock>
{
RedstoneLampBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RedstoneTorchBlock>
```cpp
/* 251248 */
struct SharedCounter<RedstoneTorchBlock>
{
RedstoneTorchBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ReedBlock>
```cpp
/* 251275 */
struct SharedCounter<ReedBlock>
{
ReedBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RepeaterBlock>
```cpp
/* 251305 */
struct SharedCounter<RepeaterBlock>
{
RepeaterBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RotatedPillarBlock>
```cpp
/* 251551 */
struct SharedCounter<RotatedPillarBlock>
{
RotatedPillarBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SandBlock>
```cpp
/* 251088 */
struct SharedCounter<SandBlock>
{
SandBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SandStoneBlock>
```cpp
/* 251120 */
struct SharedCounter<SandStoneBlock>
{
SandStoneBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<Sapling>
```cpp
/* 251072 */
struct SharedCounter<Sapling>
{
Sapling *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SaplingBlockItem>
```cpp
/* 184033 */
struct SharedCounter<SaplingBlockItem>
{
SaplingBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ScaffoldingBlock>
```cpp
/* 251692 */
struct SharedCounter<ScaffoldingBlock>
{
ScaffoldingBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ScaffoldingBlockItem>
```cpp
/* 184061 */
struct SharedCounter<ScaffoldingBlockItem>
{
ScaffoldingBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SeaGrass>
```cpp
/* 251668 */
struct SharedCounter<SeaGrass>
{
SeaGrass *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SeaLanternBlock>
```cpp
/* 251495 */
struct SharedCounter<SeaLanternBlock>
{
SeaLanternBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SeaPickle>
```cpp
/* 251672 */
struct SharedCounter<SeaPickle>
{
SeaPickle *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SeaPickleBlockItem>
```cpp
/* 184029 */
struct SharedCounter<SeaPickleBlockItem>
{
SeaPickleBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ShearsItem>
```cpp
/* 183883 */
struct SharedCounter<ShearsItem>
{
ShearsItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ShieldItem>
```cpp
/* 183820 */
struct SharedCounter<ShieldItem>
{
ShieldItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ShovelItem>
```cpp
/* 183777 */
struct SharedCounter<ShovelItem>
{
ShovelItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ShulkerBoxBlock>
```cpp
/* 251559 */
struct SharedCounter<ShulkerBoxBlock>
{
ShulkerBoxBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ShulkerBoxBlockItem>
```cpp
/* 184053 */
struct SharedCounter<ShulkerBoxBlockItem>
{
ShulkerBoxBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SignBlock>
```cpp
/* 251222 */
struct SharedCounter<SignBlock>
{
SignBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SignItem>
```cpp
/* 183827 */
struct SharedCounter<SignItem>
{
SignItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SkullBlock>
```cpp
/* 251436 */
struct SharedCounter<SkullBlock>
{
SkullBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SkullItem>
```cpp
/* 183924 */
struct SharedCounter<SkullItem>
{
SkullItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SlimeBlock>
```cpp
/* 251487 */
struct SharedCounter<SlimeBlock>
{
SlimeBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SmokerBlock>
```cpp
/* 251723 */
struct SharedCounter<SmokerBlock>
{
SmokerBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SnowBlock>
```cpp
/* 251263 */
struct SharedCounter<SnowBlock>
{
SnowBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SnowballItem>
```cpp
/* 183847 */
struct SharedCounter<SnowballItem>
{
SnowballItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SoulSandBlock>
```cpp
/* 251291 */
struct SharedCounter<SoulSandBlock>
{
SoulSandBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SparklerItem>
```cpp
/* 184004 */
struct SharedCounter<SparklerItem>
{
SparklerItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SplashPotionItem>
```cpp
/* 183958 */
struct SharedCounter<SplashPotionItem>
{
SplashPotionItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SpongeBlock>
```cpp
/* 251108 */
struct SharedCounter<SpongeBlock>
{
SpongeBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StainedGlassBlock>
```cpp
/* 251579 */
struct SharedCounter<StainedGlassBlock>
{
StainedGlassBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StainedGlassPaneBlock>
```cpp
/* 251475 */
struct SharedCounter<StainedGlassPaneBlock>
{
StainedGlassPaneBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StairBlock>
```cpp
/* 251197 */
struct SharedCounter<StairBlock>
{
StairBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StemBlock>
```cpp
/* 251334 */
struct SharedCounter<StemBlock>
{
StemBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StoneBlock>
```cpp
/* 251056 */
struct SharedCounter<StoneBlock>
{
StoneBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StoneBrickBlock>
```cpp
/* 251319 */
struct SharedCounter<StoneBrickBlock>
{
StoneBrickBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StoneButtonBlock>
```cpp
/* 251252 */
struct SharedCounter<StoneButtonBlock>
{
StoneButtonBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StoneSlabBlock2>
```cpp
/* 251515 */
struct SharedCounter<StoneSlabBlock2>
{
StoneSlabBlock2 *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StoneSlabBlock3>
```cpp
/* 251704 */
struct SharedCounter<StoneSlabBlock3>
{
StoneSlabBlock3 *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StoneSlabBlock4>
```cpp
/* 251708 */
struct SharedCounter<StoneSlabBlock4>
{
StoneSlabBlock4 *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StoneSlabBlock>
```cpp
/* 251173 */
struct SharedCounter<StoneSlabBlock>
{
StoneSlabBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StoneSlabBlockItem>
```cpp
/* 184020 */
struct SharedCounter<StoneSlabBlockItem>
{
StoneSlabBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StonecutterBlock>
```cpp
/* 251595 */
struct SharedCounter<StonecutterBlock>
{
StonecutterBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StrippedLogBlock>
```cpp
/* 251615 */
struct SharedCounter<StrippedLogBlock>
{
StrippedLogBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StructureBlock>
```cpp
/* 251611 */
struct SharedCounter<StructureBlock>
{
StructureBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StructureVoid>
```cpp
/* 251555 */
struct SharedCounter<StructureVoid>
{
StructureVoid *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SuspiciousStewItem>
```cpp
/* 183976 */
struct SharedCounter<SuspiciousStewItem>
{
SuspiciousStewItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SweetBerryBushBlock>
```cpp
/* 251743 */
struct SharedCounter<SweetBerryBushBlock>
{
SweetBerryBushBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TallGrass>
```cpp
/* 251146 */
struct SharedCounter<TallGrass>
{
TallGrass *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ThinFenceBlock>
```cpp
/* 251326 */
struct SharedCounter<ThinFenceBlock>
{
ThinFenceBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TntBlock>
```cpp
/* 251177 */
struct SharedCounter<TntBlock>
{
TntBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TopSnowBlock>
```cpp
/* 251256 */
struct SharedCounter<TopSnowBlock>
{
TopSnowBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TopSnowBlockItem>
```cpp
/* 184049 */
struct SharedCounter<TopSnowBlockItem>
{
TopSnowBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TorchBlock>
```cpp
/* 251189 */
struct SharedCounter<TorchBlock>
{
TorchBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TrapDoorBlock>
```cpp
/* 251312 */
struct SharedCounter<TrapDoorBlock>
{
TrapDoorBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TridentItem>
```cpp
/* 183944 */
struct SharedCounter<TridentItem>
{
TridentItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TripWireBlock>
```cpp
/* 251405 */
struct SharedCounter<TripWireBlock>
{
TripWireBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TripWireHookBlock>
```cpp
/* 251401 */
struct SharedCounter<TripWireHookBlock>
{
TripWireHookBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TurtleEggBlock>
```cpp
/* 251684 */
struct SharedCounter<TurtleEggBlock>
{
TurtleEggBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<UnderwaterTorchBlock>
```cpp
/* 251629 */
struct SharedCounter<UnderwaterTorchBlock>
{
UnderwaterTorchBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<UndyedShulkerBoxBlock>
```cpp
/* 251531 */
struct SharedCounter<UndyedShulkerBoxBlock>
{
UndyedShulkerBoxBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<VineBlock>
```cpp
/* 251338 */
struct SharedCounter<VineBlock>
{
VineBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WallBlock>
```cpp
/* 251416 */
struct SharedCounter<WallBlock>
{
WallBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WaterLilyBlockItem>
```cpp
/* 184045 */
struct SharedCounter<WaterLilyBlockItem>
{
WaterLilyBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WaterlilyBlock>
```cpp
/* 251350 */
struct SharedCounter<WaterlilyBlock>
{
WaterlilyBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WeaponItem>
```cpp
/* 183805 */
struct SharedCounter<WeaponItem>
{
WeaponItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WebBlock>
```cpp
/* 251142 */
struct SharedCounter<WebBlock>
{
WebBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WeightedPressurePlateBlock>
```cpp
/* 251444 */
struct SharedCounter<WeightedPressurePlateBlock>
{
WeightedPressurePlateBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WitherRoseBlock>
```cpp
/* 251770 */
struct SharedCounter<WitherRoseBlock>
{
WitherRoseBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WoodBlock>
```cpp
/* 251759 */
struct SharedCounter<WoodBlock>
{
WoodBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WoodButtonBlock>
```cpp
/* 251432 */
struct SharedCounter<WoodButtonBlock>
{
WoodButtonBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WoodSlabBlock>
```cpp
/* 251467 */
struct SharedCounter<WoodSlabBlock>
{
WoodSlabBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WoodSlabBlockItem>
```cpp
/* 184041 */
struct SharedCounter<WoodSlabBlockItem>
{
WoodSlabBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WoolCarpetBlock>
```cpp
/* 251503 */
struct SharedCounter<WoolCarpetBlock>
{
WoolCarpetBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WorkbenchBlock>
```cpp
/* 251207 */
struct SharedCounter<WorkbenchBlock>
{
WorkbenchBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WritableBookItem>
```cpp
/* 183913 */
struct SharedCounter<WritableBookItem>
{
WritableBookItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WrittenBookItem>
```cpp
/* 183917 */
struct SharedCounter<WrittenBookItem>
{
WrittenBookItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedModifiers
```cpp
/* 174645 */
struct SharedModifiers
{
__int8 gap0[1];
};

```
#### SharedPtr<ActivatorRailBlock>
```cpp
/* 251388 */
struct SharedPtr<ActivatorRailBlock>
{
SharedCounter<ActivatorRailBlock> *pc;
};

```
#### SharedPtr<AirBlock>
```cpp
/* 250878 */
struct SharedPtr<AirBlock>
{
SharedCounter<AirBlock> *pc;
};

```
#### SharedPtr<AirBlockItem>
```cpp
/* 180755 */
struct SharedPtr<AirBlockItem>
{
SharedCounter<AirBlockItem> *pc;
};

```
#### SharedPtr<AnvilBlock>
```cpp
/* 251439 */
struct SharedPtr<AnvilBlock>
{
SharedCounter<AnvilBlock> *pc;
};

```
#### SharedPtr<ArmorItem>
```cpp
/* 183816 */
struct SharedPtr<ArmorItem>
{
SharedCounter<ArmorItem> *pc;
};

```
#### SharedPtr<ArmorStandItem>
```cpp
/* 183949 */
struct SharedPtr<ArmorStandItem>
{
SharedCounter<ArmorStandItem> *pc;
};

```
#### SharedPtr<ArrowItem>
```cpp
/* 183796 */
struct SharedPtr<ArrowItem>
{
SharedCounter<ArrowItem> *pc;
};

```
#### SharedPtr<AuxDataBlockItem>
```cpp
/* 184011 */
struct SharedPtr<AuxDataBlockItem>
{
SharedCounter<AuxDataBlockItem> *pc;
};

```
#### SharedPtr<BalloonItem>
```cpp
/* 183995 */
struct SharedPtr<BalloonItem>
{
SharedCounter<BalloonItem> *pc;
};

```
#### SharedPtr<BambooBlock>
```cpp
/* 251695 */
struct SharedPtr<BambooBlock>
{
SharedCounter<BambooBlock> *pc;
};

```
#### SharedPtr<BambooBlockItem>
```cpp
/* 184056 */
struct SharedPtr<BambooBlockItem>
{
SharedCounter<BambooBlockItem> *pc;
};

```
#### SharedPtr<BambooSapling>
```cpp
/* 251699 */
struct SharedPtr<BambooSapling>
{
SharedCounter<BambooSapling> *pc;
};

```
#### SharedPtr<BannerBlock>
```cpp
/* 251510 */
struct SharedPtr<BannerBlock>
{
SharedCounter<BannerBlock> *pc;
};

```
#### SharedPtr<BannerItem>
```cpp
/* 183964 */
struct SharedPtr<BannerItem>
{
SharedCounter<BannerItem> *pc;
};

```
#### SharedPtr<BannerPatternItem>
```cpp
/* 183972 */
struct SharedPtr<BannerPatternItem>
{
SharedCounter<BannerPatternItem> *pc;
};

```
#### SharedPtr<BarrelBlock>
```cpp
/* 251730 */
struct SharedPtr<BarrelBlock>
{
SharedCounter<BarrelBlock> *pc;
};

```
#### SharedPtr<BarrierBlock>
```cpp
/* 251687 */
struct SharedPtr<BarrierBlock>
{
SharedCounter<BarrierBlock> *pc;
};

```
#### SharedPtr<BeaconBlock>
```cpp
/* 251411 */
struct SharedPtr<BeaconBlock>
{
SharedCounter<BeaconBlock> *pc;
};

```
#### SharedPtr<BedBlock>
```cpp
/* 251127 */
struct SharedPtr<BedBlock>
{
SharedCounter<BedBlock> *pc;
};

```
#### SharedPtr<BedItem>
```cpp
/* 183875 */
struct SharedPtr<BedItem>
{
SharedCounter<BedItem> *pc;
};

```
#### SharedPtr<BedrockBlock>
```cpp
/* 251075 */
struct SharedPtr<BedrockBlock>
{
SharedCounter<BedrockBlock> *pc;
};

```
#### SharedPtr<BeehiveBlock>
```cpp
/* 251773 */
struct SharedPtr<BeehiveBlock>
{
SharedCounter<BeehiveBlock> *pc;
};

```
#### SharedPtr<BeetrootBlock>
```cpp
/* 251590 */
struct SharedPtr<BeetrootBlock>
{
SharedCounter<BeetrootBlock> *pc;
};

```
#### SharedPtr<BellBlock>
```cpp
/* 251738 */
struct SharedPtr<BellBlock>
{
SharedCounter<BellBlock> *pc;
};

```
#### SharedPtr<BellBlockItem>
```cpp
/* 184064 */
struct SharedPtr<BellBlockItem>
{
SharedCounter<BellBlockItem> *pc;
};

```
#### SharedPtr<BlastFurnaceBlock>
```cpp
/* 251718 */
struct SharedPtr<BlastFurnaceBlock>
{
SharedCounter<BlastFurnaceBlock> *pc;
};

```
#### SharedPtr<BlockItem>
```cpp
/* 182764 */
struct SharedPtr<BlockItem>
{
SharedCounter<BlockItem> *pc;
};

```
#### SharedPtr<BlockLegacy>
```cpp
/* 13209 */
struct SharedPtr<BlockLegacy>
{
SharedCounter<BlockLegacy> *pc;
};

```
#### SharedPtr<BlockPlanterItem>
```cpp
/* 183808 */
struct SharedPtr<BlockPlanterItem>
{
SharedCounter<BlockPlanterItem> *pc;
};

```
#### SharedPtr<BlueIceBlock>
```cpp
/* 251618 */
struct SharedPtr<BlueIceBlock>
{
SharedCounter<BlueIceBlock> *pc;
};

```
#### SharedPtr<BoatItem>
```cpp
/* 183850 */
struct SharedPtr<BoatItem>
{
SharedCounter<BoatItem> *pc;
};

```
#### SharedPtr<BookshelfBlock>
```cpp
/* 251180 */
struct SharedPtr<BookshelfBlock>
{
SharedCounter<BookshelfBlock> *pc;
};

```
#### SharedPtr<BottleItem>
```cpp
/* 183893 */
struct SharedPtr<BottleItem>
{
SharedCounter<BottleItem> *pc;
};

```
#### SharedPtr<BowItem>
```cpp
/* 183792 */
struct SharedPtr<BowItem>
{
SharedCounter<BowItem> *pc;
};

```
#### SharedPtr<BrewingStandBlock>
```cpp
/* 251361 */
struct SharedPtr<BrewingStandBlock>
{
SharedCounter<BrewingStandBlock> *pc;
};

```
#### SharedPtr<BubbleColumnBlock>
```cpp
/* 251679 */
struct SharedPtr<BubbleColumnBlock>
{
SharedCounter<BubbleColumnBlock> *pc;
};

```
#### SharedPtr<BucketItem>
```cpp
/* 183834 */
struct SharedPtr<BucketItem>
{
SharedCounter<BucketItem> *pc;
};

```
#### SharedPtr<CactusBlock>
```cpp
/* 251266 */
struct SharedPtr<CactusBlock>
{
SharedCounter<CactusBlock> *pc;
};

```
#### SharedPtr<CakeBlock>
```cpp
/* 251301 */
struct SharedPtr<CakeBlock>
{
SharedCounter<CakeBlock> *pc;
};

```
#### SharedPtr<CameraBlock>
```cpp
/* 251582 */
struct SharedPtr<CameraBlock>
{
SharedCounter<CameraBlock> *pc;
};

```
#### SharedPtr<CameraItem>
```cpp
/* 183978 */
struct SharedPtr<CameraItem>
{
SharedCounter<CameraItem> *pc;
};

```
#### SharedPtr<CampfireBlock>
```cpp
/* 251750 */
struct SharedPtr<CampfireBlock>
{
SharedCounter<CampfireBlock> *pc;
};

```
#### SharedPtr<CarrotBlock>
```cpp
/* 251423 */
struct SharedPtr<CarrotBlock>
{
SharedCounter<CarrotBlock> *pc;
};

```
#### SharedPtr<CarrotOnAStickItem>
```cpp
/* 183927 */
struct SharedPtr<CarrotOnAStickItem>
{
SharedCounter<CarrotOnAStickItem> *pc;
};

```
#### SharedPtr<CartographyTableBlock>
```cpp
/* 251726 */
struct SharedPtr<CartographyTableBlock>
{
SharedCounter<CartographyTableBlock> *pc;
};

```
#### SharedPtr<CauldronBlock>
```cpp
/* 251365 */
struct SharedPtr<CauldronBlock>
{
SharedCounter<CauldronBlock> *pc;
};

```
#### SharedPtr<ChemicalHeatBlock>
```cpp
/* 251632 */
struct SharedPtr<ChemicalHeatBlock>
{
SharedCounter<ChemicalHeatBlock> *pc;
};

```
#### SharedPtr<ChemistryAuxDataBlockItem>
```cpp
/* 184068 */
struct SharedPtr<ChemistryAuxDataBlockItem>
{
SharedCounter<ChemistryAuxDataBlockItem> *pc;
};

```
#### SharedPtr<ChemistryItem>
```cpp
/* 183989 */
struct SharedPtr<ChemistryItem>
{
SharedCounter<ChemistryItem> *pc;
};

```
#### SharedPtr<ChemistryTableBlock>
```cpp
/* 251625 */
struct SharedPtr<ChemistryTableBlock>
{
SharedCounter<ChemistryTableBlock> *pc;
};

```
#### SharedPtr<ChestBlock>
```cpp
/* 251199 */
struct SharedPtr<ChestBlock>
{
SharedCounter<ChestBlock> *pc;
};

```
#### SharedPtr<ChorusFlowerBlock>
```cpp
/* 251526 */
struct SharedPtr<ChorusFlowerBlock>
{
SharedCounter<ChorusFlowerBlock> *pc;
};

```
#### SharedPtr<ChorusPlantBlock>
```cpp
/* 251574 */
struct SharedPtr<ChorusPlantBlock>
{
SharedCounter<ChorusPlantBlock> *pc;
};

```
#### SharedPtr<ClayBlock>
```cpp
/* 251270 */
struct SharedPtr<ClayBlock>
{
SharedCounter<ClayBlock> *pc;
};

```
#### SharedPtr<ClockItem>
```cpp
/* 183869 */
struct SharedPtr<ClockItem>
{
SharedCounter<ClockItem> *pc;
};

```
#### SharedPtr<ClothBlock>
```cpp
/* 251157 */
struct SharedPtr<ClothBlock>
{
SharedCounter<ClothBlock> *pc;
};

```
#### SharedPtr<ClothBlockItem>
```cpp
/* 184015 */
struct SharedPtr<ClothBlockItem>
{
SharedCounter<ClothBlockItem> *pc;
};

```
#### SharedPtr<CoalItem>
```cpp
/* 183800 */
struct SharedPtr<CoalItem>
{
SharedCounter<CoalItem> *pc;
};

```
#### SharedPtr<CocoaBlock>
```cpp
/* 251392 */
struct SharedPtr<CocoaBlock>
{
SharedCounter<CocoaBlock> *pc;
};

```
#### SharedPtr<ColoredBlock>
```cpp
/* 251470 */
struct SharedPtr<ColoredBlock>
{
SharedCounter<ColoredBlock> *pc;
};

```
#### SharedPtr<ColoredTorchBlock>
```cpp
/* 251636 */
struct SharedPtr<ColoredTorchBlock>
{
SharedCounter<ColoredTorchBlock> *pc;
};

```
#### SharedPtr<CommandBlock>
```cpp
/* 251408 */
struct SharedPtr<CommandBlock>
{
SharedCounter<CommandBlock> *pc;
};

```
#### SharedPtr<ComparatorBlock>
```cpp
/* 251447 */
struct SharedPtr<ComparatorBlock>
{
SharedCounter<ComparatorBlock> *pc;
};

```
#### SharedPtr<CompassItem>
```cpp
/* 183862 */
struct SharedPtr<CompassItem>
{
SharedCounter<CompassItem> *pc;
};

```
#### SharedPtr<ComposterBlock>
```cpp
/* 251762 */
struct SharedPtr<ComposterBlock>
{
SharedCounter<ComposterBlock> *pc;
};

```
#### SharedPtr<CompoundItem>
```cpp
/* 183982 */
struct SharedPtr<CompoundItem>
{
SharedCounter<CompoundItem> *pc;
};

```
#### SharedPtr<ConcreteBlock>
```cpp
/* 251566 */
struct SharedPtr<ConcreteBlock>
{
SharedCounter<ConcreteBlock> *pc;
};

```
#### SharedPtr<ConcretePowderBlock>
```cpp
/* 251570 */
struct SharedPtr<ConcretePowderBlock>
{
SharedCounter<ConcretePowderBlock> *pc;
};

```
#### SharedPtr<ConduitBlock>
```cpp
/* 251675 */
struct SharedPtr<ConduitBlock>
{
SharedCounter<ConduitBlock> *pc;
};

```
#### SharedPtr<Coral>
```cpp
/* 251643 */
struct SharedPtr<Coral>
{
SharedCounter<Coral> *pc;
};

```
#### SharedPtr<CoralBlock>
```cpp
/* 251647 */
struct SharedPtr<CoralBlock>
{
SharedCounter<CoralBlock> *pc;
};

```
#### SharedPtr<CoralFan>
```cpp
/* 251651 */
struct SharedPtr<CoralFan>
{
SharedCounter<CoralFan> *pc;
};

```
#### SharedPtr<CoralFanBlockItem>
```cpp
/* 184024 */
struct SharedPtr<CoralFanBlockItem>
{
SharedCounter<CoralFanBlockItem> *pc;
};

```
#### SharedPtr<CoralFanHang>
```cpp
/* 251655 */
struct SharedPtr<CoralFanHang>
{
SharedCounter<CoralFanHang> *pc;
};

```
#### SharedPtr<CropBlock>
```cpp
/* 251210 */
struct SharedPtr<CropBlock>
{
SharedCounter<CropBlock> *pc;
};

```
#### SharedPtr<CrossbowItem>
```cpp
/* 183968 */
struct SharedPtr<CrossbowItem>
{
SharedCounter<CrossbowItem> *pc;
};

```
#### SharedPtr<DaylightDetectorBlock>
```cpp
/* 251451 */
struct SharedPtr<DaylightDetectorBlock>
{
SharedCounter<DaylightDetectorBlock> *pc;
};

```
#### SharedPtr<DeadBush>
```cpp
/* 251149 */
struct SharedPtr<DeadBush>
{
SharedCounter<DeadBush> *pc;
};

```
#### SharedPtr<DetectorRailBlock>
```cpp
/* 251134 */
struct SharedPtr<DetectorRailBlock>
{
SharedCounter<DetectorRailBlock> *pc;
};

```
#### SharedPtr<DirtBlock>
```cpp
/* 251063 */
struct SharedPtr<DirtBlock>
{
SharedCounter<DirtBlock> *pc;
};

```
#### SharedPtr<DispenserBlock>
```cpp
/* 251115 */
struct SharedPtr<DispenserBlock>
{
SharedCounter<DispenserBlock> *pc;
};

```
#### SharedPtr<DoorBlock>
```cpp
/* 251225 */
struct SharedPtr<DoorBlock>
{
SharedCounter<DoorBlock> *pc;
};

```
#### SharedPtr<DoorItem>
```cpp
/* 183830 */
struct SharedPtr<DoorItem>
{
SharedCounter<DoorItem> *pc;
};

```
#### SharedPtr<DoublePlantBlock>
```cpp
/* 251506 */
struct SharedPtr<DoublePlantBlock>
{
SharedCounter<DoublePlantBlock> *pc;
};

```
#### SharedPtr<DragonEggBlock>
```cpp
/* 251376 */
struct SharedPtr<DragonEggBlock>
{
SharedCounter<DragonEggBlock> *pc;
};

```
#### SharedPtr<DriedKelpBlock>
```cpp
/* 251663 */
struct SharedPtr<DriedKelpBlock>
{
SharedCounter<DriedKelpBlock> *pc;
};

```
#### SharedPtr<DropperBlock>
```cpp
/* 251384 */
struct SharedPtr<DropperBlock>
{
SharedCounter<DropperBlock> *pc;
};

```
#### SharedPtr<DyePowderItem>
```cpp
/* 183872 */
struct SharedPtr<DyePowderItem>
{
SharedCounter<DyePowderItem> *pc;
};

```
#### SharedPtr<EggItem>
```cpp
/* 183858 */
struct SharedPtr<EggItem>
{
SharedCounter<EggItem> *pc;
};

```
#### SharedPtr<ElementBlock>
```cpp
/* 251640 */
struct SharedPtr<ElementBlock>
{
SharedCounter<ElementBlock> *pc;
};

```
#### SharedPtr<ElementBlockItem>
```cpp
/* 184072 */
struct SharedPtr<ElementBlockItem>
{
SharedCounter<ElementBlockItem> *pc;
};

```
#### SharedPtr<EmptyMapItem>
```cpp
/* 183920 */
struct SharedPtr<EmptyMapItem>
{
SharedCounter<EmptyMapItem> *pc;
};

```
#### SharedPtr<EnchantedBookItem>
```cpp
/* 183854 */
struct SharedPtr<EnchantedBookItem>
{
SharedCounter<EnchantedBookItem> *pc;
};

```
#### SharedPtr<EnchantingTableBlock>
```cpp
/* 251357 */
struct SharedPtr<EnchantingTableBlock>
{
SharedCounter<EnchantingTableBlock> *pc;
};

```
#### SharedPtr<EndCrystalItem>
```cpp
/* 183953 */
struct SharedPtr<EndCrystalItem>
{
SharedCounter<EndCrystalItem> *pc;
};

```
#### SharedPtr<EndGatewayBlock>
```cpp
/* 251542 */
struct SharedPtr<EndGatewayBlock>
{
SharedCounter<EndGatewayBlock> *pc;
};

```
#### SharedPtr<EndPortalBlock>
```cpp
/* 251368 */
struct SharedPtr<EndPortalBlock>
{
SharedCounter<EndPortalBlock> *pc;
};

```
#### SharedPtr<EndPortalFrameBlock>
```cpp
/* 251372 */
struct SharedPtr<EndPortalFrameBlock>
{
SharedCounter<EndPortalFrameBlock> *pc;
};

```
#### SharedPtr<EndRodBlock>
```cpp
/* 251538 */
struct SharedPtr<EndRodBlock>
{
SharedCounter<EndRodBlock> *pc;
};

```
#### SharedPtr<EnderChestBlock>
```cpp
/* 251396 */
struct SharedPtr<EnderChestBlock>
{
SharedCounter<EnderChestBlock> *pc;
};

```
#### SharedPtr<EnderEyeItem>
```cpp
/* 183897 */
struct SharedPtr<EnderEyeItem>
{
SharedCounter<EnderEyeItem> *pc;
};

```
#### SharedPtr<EnderpearlItem>
```cpp
/* 183886 */
struct SharedPtr<EnderpearlItem>
{
SharedCounter<EnderpearlItem> *pc;
};

```
#### SharedPtr<ExperiencePotionItem>
```cpp
/* 183904 */
struct SharedPtr<ExperiencePotionItem>
{
SharedCounter<ExperiencePotionItem> *pc;
};

```
#### SharedPtr<FarmBlock>
```cpp
/* 251214 */
struct SharedPtr<FarmBlock>
{
SharedCounter<FarmBlock> *pc;
};

```
#### SharedPtr<FenceBlock>
```cpp
/* 251282 */
struct SharedPtr<FenceBlock>
{
SharedCounter<FenceBlock> *pc;
};

```
#### SharedPtr<FenceGateBlock>
```cpp
/* 251341 */
struct SharedPtr<FenceGateBlock>
{
SharedCounter<FenceGateBlock> *pc;
};

```
#### SharedPtr<FireBlock>
```cpp
/* 251622 */
struct SharedPtr<FireBlock>
{
SharedCounter<FireBlock> *pc;
};

```
#### SharedPtr<FireChargeItem>
```cpp
/* 183908 */
struct SharedPtr<FireChargeItem>
{
SharedCounter<FireChargeItem> *pc;
};

```
#### SharedPtr<FireworkChargeItem>
```cpp
/* 183934 */
struct SharedPtr<FireworkChargeItem>
{
SharedCounter<FireworkChargeItem> *pc;
};

```
#### SharedPtr<FireworksItem>
```cpp
/* 183931 */
struct SharedPtr<FireworksItem>
{
SharedCounter<FireworksItem> *pc;
};

```
#### SharedPtr<FishingRodItem>
```cpp
/* 183865 */
struct SharedPtr<FishingRodItem>
{
SharedCounter<FishingRodItem> *pc;
};

```
#### SharedPtr<FlintAndSteelItem>
```cpp
/* 183788 */
struct SharedPtr<FlintAndSteelItem>
{
SharedCounter<FlintAndSteelItem> *pc;
};

```
#### SharedPtr<FlowerBlock>
```cpp
/* 251161 */
struct SharedPtr<FlowerBlock>
{
SharedCounter<FlowerBlock> *pc;
};

```
#### SharedPtr<FlowerPotBlock>
```cpp
/* 251419 */
struct SharedPtr<FlowerPotBlock>
{
SharedCounter<FlowerPotBlock> *pc;
};

```
#### SharedPtr<FrostedIceBlock>
```cpp
/* 251534 */
struct SharedPtr<FrostedIceBlock>
{
SharedCounter<FrostedIceBlock> *pc;
};

```
#### SharedPtr<FurnaceBlock>
```cpp
/* 251217 */
struct SharedPtr<FurnaceBlock>
{
SharedCounter<FurnaceBlock> *pc;
};

```
#### SharedPtr<GlassBlock>
```cpp
/* 251111 */
struct SharedPtr<GlassBlock>
{
SharedCounter<GlassBlock> *pc;
};

```
#### SharedPtr<GlazedTerracottaBlock>
```cpp
/* 251562 */
struct SharedPtr<GlazedTerracottaBlock>
{
SharedCounter<GlazedTerracottaBlock> *pc;
};

```
#### SharedPtr<GlowStickItem>
```cpp
/* 184007 */
struct SharedPtr<GlowStickItem>
{
SharedCounter<GlowStickItem> *pc;
};

```
#### SharedPtr<GrassBlock>
```cpp
/* 251059 */
struct SharedPtr<GrassBlock>
{
SharedCounter<GrassBlock> *pc;
};

```
#### SharedPtr<GrassPathBlock>
```cpp
/* 251518 */
struct SharedPtr<GrassPathBlock>
{
SharedCounter<GrassPathBlock> *pc;
};

```
#### SharedPtr<GravelBlock>
```cpp
/* 251091 */
struct SharedPtr<GravelBlock>
{
SharedCounter<GravelBlock> *pc;
};

```
#### SharedPtr<GrindstoneBlock>
```cpp
/* 251714 */
struct SharedPtr<GrindstoneBlock>
{
SharedCounter<GrindstoneBlock> *pc;
};

```
#### SharedPtr<HangingActorItem>
```cpp
/* 183822 */
struct SharedPtr<HangingActorItem>
{
SharedCounter<HangingActorItem> *pc;
};

```
#### SharedPtr<HatchetItem>
```cpp
/* 183784 */
struct SharedPtr<HatchetItem>
{
SharedCounter<HatchetItem> *pc;
};

```
#### SharedPtr<HayBlockBlock>
```cpp
/* 251498 */
struct SharedPtr<HayBlockBlock>
{
SharedCounter<HayBlockBlock> *pc;
};

```
#### SharedPtr<HoeItem>
```cpp
/* 183812 */
struct SharedPtr<HoeItem>
{
SharedCounter<HoeItem> *pc;
};

```
#### SharedPtr<HoneyBlock>
```cpp
/* 251776 */
struct SharedPtr<HoneyBlock>
{
SharedCounter<HoneyBlock> *pc;
};

```
#### SharedPtr<HoneycombBlock>
```cpp
/* 251780 */
struct SharedPtr<HoneycombBlock>
{
SharedCounter<HoneycombBlock> *pc;
};

```
#### SharedPtr<HopperBlock>
```cpp
/* 251458 */
struct SharedPtr<HopperBlock>
{
SharedCounter<HopperBlock> *pc;
};

```
#### SharedPtr<HorseArmorItem>
```cpp
/* 183937 */
struct SharedPtr<HorseArmorItem>
{
SharedCounter<HorseArmorItem> *pc;
};

```
#### SharedPtr<HugeMushroomBlock>
```cpp
/* 251322 */
struct SharedPtr<HugeMushroomBlock>
{
SharedCounter<HugeMushroomBlock> *pc;
};

```
#### SharedPtr<IceBlock>
```cpp
/* 251258 */
struct SharedPtr<IceBlock>
{
SharedCounter<IceBlock> *pc;
};

```
#### SharedPtr<IceBombItem>
```cpp
/* 183985 */
struct SharedPtr<IceBombItem>
{
SharedCounter<IceBombItem> *pc;
};

```
#### SharedPtr<InvisibleBlock>
```cpp
/* 251307 */
struct SharedPtr<InvisibleBlock>
{
SharedCounter<InvisibleBlock> *pc;
};

```
#### SharedPtr<Item>
```cpp
/* 13205 */
struct SharedPtr<Item>
{
SharedCounter<Item> *pc;
};

```
#### SharedPtr<ItemFrameBlock>
```cpp
/* 251522 */
struct SharedPtr<ItemFrameBlock>
{
SharedCounter<ItemFrameBlock> *pc;
};

```
#### SharedPtr<JigsawBlock>
```cpp
/* 251754 */
struct SharedPtr<JigsawBlock>
{
SharedCounter<JigsawBlock> *pc;
};

```
#### SharedPtr<JukeboxBlock>
```cpp
/* 251278 */
struct SharedPtr<JukeboxBlock>
{
SharedCounter<JukeboxBlock> *pc;
};

```
#### SharedPtr<KelpBlock>
```cpp
/* 251659 */
struct SharedPtr<KelpBlock>
{
SharedCounter<KelpBlock> *pc;
};

```
#### SharedPtr<LadderBlock>
```cpp
/* 251228 */
struct SharedPtr<LadderBlock>
{
SharedCounter<LadderBlock> *pc;
};

```
#### SharedPtr<LanternBlock>
```cpp
/* 251746 */
struct SharedPtr<LanternBlock>
{
SharedCounter<LanternBlock> *pc;
};

```
#### SharedPtr<LeadItem>
```cpp
/* 183946 */
struct SharedPtr<LeadItem>
{
SharedCounter<LeadItem> *pc;
};

```
#### SharedPtr<LeafBlockItem>
```cpp
/* 184036 */
struct SharedPtr<LeafBlockItem>
{
SharedCounter<LeafBlockItem> *pc;
};

```
#### SharedPtr<LecternBlock>
```cpp
/* 251711 */
struct SharedPtr<LecternBlock>
{
SharedCounter<LecternBlock> *pc;
};

```
#### SharedPtr<LeverBlock>
```cpp
/* 251236 */
struct SharedPtr<LeverBlock>
{
SharedCounter<LeverBlock> *pc;
};

```
#### SharedPtr<LightBlock>
```cpp
/* 251765 */
struct SharedPtr<LightBlock>
{
SharedCounter<LightBlock> *pc;
};

```
#### SharedPtr<LightGemBlock>
```cpp
/* 251294 */
struct SharedPtr<LightGemBlock>
{
SharedCounter<LightGemBlock> *pc;
};

```
#### SharedPtr<LingeringPotionItem>
```cpp
/* 183960 */
struct SharedPtr<LingeringPotionItem>
{
SharedCounter<LingeringPotionItem> *pc;
};

```
#### SharedPtr<LiquidBlockDynamic>
```cpp
/* 251079 */
struct SharedPtr<LiquidBlockDynamic>
{
SharedCounter<LiquidBlockDynamic> *pc;
};

```
#### SharedPtr<LiquidBlockStatic>
```cpp
/* 251083 */
struct SharedPtr<LiquidBlockStatic>
{
SharedCounter<LiquidBlockStatic> *pc;
};

```
#### SharedPtr<LoomBlock>
```cpp
/* 251734 */
struct SharedPtr<LoomBlock>
{
SharedCounter<LoomBlock> *pc;
};

```
#### SharedPtr<MagmaBlock>
```cpp
/* 251546 */
struct SharedPtr<MagmaBlock>
{
SharedCounter<MagmaBlock> *pc;
};

```
#### SharedPtr<MapItem>
```cpp
/* 183879 */
struct SharedPtr<MapItem>
{
SharedCounter<MapItem> *pc;
};

```
#### SharedPtr<MedicineItem>
```cpp
/* 183999 */
struct SharedPtr<MedicineItem>
{
SharedCounter<MedicineItem> *pc;
};

```
#### SharedPtr<MelonBlock>
```cpp
/* 251329 */
struct SharedPtr<MelonBlock>
{
SharedCounter<MelonBlock> *pc;
};

```
#### SharedPtr<MetalBlock>
```cpp
/* 251168 */
struct SharedPtr<MetalBlock>
{
SharedCounter<MetalBlock> *pc;
};

```
#### SharedPtr<MinecartItem>
```cpp
/* 183838 */
struct SharedPtr<MinecartItem>
{
SharedCounter<MinecartItem> *pc;
};

```
#### SharedPtr<MobPlacerItem>
```cpp
/* 183901 */
struct SharedPtr<MobPlacerItem>
{
SharedCounter<MobPlacerItem> *pc;
};

```
#### SharedPtr<MobSpawnerBlock>
```cpp
/* 251192 */
struct SharedPtr<MobSpawnerBlock>
{
SharedCounter<MobSpawnerBlock> *pc;
};

```
#### SharedPtr<MonsterEggBlock>
```cpp
/* 251315 */
struct SharedPtr<MonsterEggBlock>
{
SharedCounter<MonsterEggBlock> *pc;
};

```
#### SharedPtr<MovingBlock>
```cpp
/* 251602 */
struct SharedPtr<MovingBlock>
{
SharedCounter<MovingBlock> *pc;
};

```
#### SharedPtr<MushroomBlock>
```cpp
/* 251164 */
struct SharedPtr<MushroomBlock>
{
SharedCounter<MushroomBlock> *pc;
};

```
#### SharedPtr<MyceliumBlock>
```cpp
/* 251345 */
struct SharedPtr<MyceliumBlock>
{
SharedCounter<MyceliumBlock> *pc;
};

```
#### SharedPtr<NetherReactorBlock>
```cpp
/* 251598 */
struct SharedPtr<NetherReactorBlock>
{
SharedCounter<NetherReactorBlock> *pc;
};

```
#### SharedPtr<NetherWartBlock>
```cpp
/* 251353 */
struct SharedPtr<NetherWartBlock>
{
SharedCounter<NetherWartBlock> *pc;
};

```
#### SharedPtr<NewLeafBlock>
```cpp
/* 251478 */
struct SharedPtr<NewLeafBlock>
{
SharedCounter<NewLeafBlock> *pc;
};

```
#### SharedPtr<NewLogBlock>
```cpp
/* 251482 */
struct SharedPtr<NewLogBlock>
{
SharedCounter<NewLogBlock> *pc;
};

```
#### SharedPtr<NoteBlock>
```cpp
/* 251123 */
struct SharedPtr<NoteBlock>
{
SharedCounter<NoteBlock> *pc;
};

```
#### SharedPtr<ObserverBlock>
```cpp
/* 251606 */
struct SharedPtr<ObserverBlock>
{
SharedCounter<ObserverBlock> *pc;
};

```
#### SharedPtr<ObsidianBlock>
```cpp
/* 251184 */
struct SharedPtr<ObsidianBlock>
{
SharedCounter<ObsidianBlock> *pc;
};

```
#### SharedPtr<OldLeafBlock>
```cpp
/* 251103 */
struct SharedPtr<OldLeafBlock>
{
SharedCounter<OldLeafBlock> *pc;
};

```
#### SharedPtr<OldLogBlock>
```cpp
/* 251099 */
struct SharedPtr<OldLogBlock>
{
SharedCounter<OldLogBlock> *pc;
};

```
#### SharedPtr<OreBlock>
```cpp
/* 251095 */
struct SharedPtr<OreBlock>
{
SharedCounter<OreBlock> *pc;
};

```
#### SharedPtr<PickaxeItem>
```cpp
/* 183780 */
struct SharedPtr<PickaxeItem>
{
SharedCounter<PickaxeItem> *pc;
};

```
#### SharedPtr<PistonArmBlock>
```cpp
/* 251153 */
struct SharedPtr<PistonArmBlock>
{
SharedCounter<PistonArmBlock> *pc;
};

```
#### SharedPtr<PistonBlock>
```cpp
/* 251138 */
struct SharedPtr<PistonBlock>
{
SharedCounter<PistonBlock> *pc;
};

```
#### SharedPtr<PlanksBlock>
```cpp
/* 251067 */
struct SharedPtr<PlanksBlock>
{
SharedCounter<PlanksBlock> *pc;
};

```
#### SharedPtr<PodzolBlock>
```cpp
/* 251586 */
struct SharedPtr<PodzolBlock>
{
SharedCounter<PodzolBlock> *pc;
};

```
#### SharedPtr<PortalBlock>
```cpp
/* 251298 */
struct SharedPtr<PortalBlock>
{
SharedCounter<PortalBlock> *pc;
};

```
#### SharedPtr<PotatoBlock>
```cpp
/* 251427 */
struct SharedPtr<PotatoBlock>
{
SharedCounter<PotatoBlock> *pc;
};

```
#### SharedPtr<PotionItem>
```cpp
/* 183890 */
struct SharedPtr<PotionItem>
{
SharedCounter<PotionItem> *pc;
};

```
#### SharedPtr<PoweredRailBlock>
```cpp
/* 251130 */
struct SharedPtr<PoweredRailBlock>
{
SharedCounter<PoweredRailBlock> *pc;
};

```
#### SharedPtr<PressurePlateBlock>
```cpp
/* 251240 */
struct SharedPtr<PressurePlateBlock>
{
SharedCounter<PressurePlateBlock> *pc;
};

```
#### SharedPtr<PrismarineBlock>
```cpp
/* 251490 */
struct SharedPtr<PrismarineBlock>
{
SharedCounter<PrismarineBlock> *pc;
};

```
#### SharedPtr<PumpkinBlock>
```cpp
/* 251286 */
struct SharedPtr<PumpkinBlock>
{
SharedCounter<PumpkinBlock> *pc;
};

```
#### SharedPtr<QuartzBlockBlock>
```cpp
/* 251462 */
struct SharedPtr<QuartzBlockBlock>
{
SharedCounter<QuartzBlockBlock> *pc;
};

```
#### SharedPtr<RailBlock>
```cpp
/* 251232 */
struct SharedPtr<RailBlock>
{
SharedCounter<RailBlock> *pc;
};

```
#### SharedPtr<RapidFertilizerItem>
```cpp
/* 183992 */
struct SharedPtr<RapidFertilizerItem>
{
SharedCounter<RapidFertilizerItem> *pc;
};

```
#### SharedPtr<RecordItem>
```cpp
/* 183940 */
struct SharedPtr<RecordItem>
{
SharedCounter<RecordItem> *pc;
};

```
#### SharedPtr<RedStoneDustItem>
```cpp
/* 183842 */
struct SharedPtr<RedStoneDustItem>
{
SharedCounter<RedStoneDustItem> *pc;
};

```
#### SharedPtr<RedStoneOreBlock>
```cpp
/* 251243 */
struct SharedPtr<RedStoneOreBlock>
{
SharedCounter<RedStoneOreBlock> *pc;
};

```
#### SharedPtr<RedStoneWireBlock>
```cpp
/* 251202 */
struct SharedPtr<RedStoneWireBlock>
{
SharedCounter<RedStoneWireBlock> *pc;
};

```
#### SharedPtr<RedstoneBlock>
```cpp
/* 251454 */
struct SharedPtr<RedstoneBlock>
{
SharedCounter<RedstoneBlock> *pc;
};

```
#### SharedPtr<RedstoneLampBlock>
```cpp
/* 251380 */
struct SharedPtr<RedstoneLampBlock>
{
SharedCounter<RedstoneLampBlock> *pc;
};

```
#### SharedPtr<RedstoneTorchBlock>
```cpp
/* 251247 */
struct SharedPtr<RedstoneTorchBlock>
{
SharedCounter<RedstoneTorchBlock> *pc;
};

```
#### SharedPtr<ReedBlock>
```cpp
/* 251274 */
struct SharedPtr<ReedBlock>
{
SharedCounter<ReedBlock> *pc;
};

```
#### SharedPtr<RepeaterBlock>
```cpp
/* 251304 */
struct SharedPtr<RepeaterBlock>
{
SharedCounter<RepeaterBlock> *pc;
};

```
#### SharedPtr<RotatedPillarBlock>
```cpp
/* 251550 */
struct SharedPtr<RotatedPillarBlock>
{
SharedCounter<RotatedPillarBlock> *pc;
};

```
#### SharedPtr<SandBlock>
```cpp
/* 251087 */
struct SharedPtr<SandBlock>
{
SharedCounter<SandBlock> *pc;
};

```
#### SharedPtr<SandStoneBlock>
```cpp
/* 251119 */
struct SharedPtr<SandStoneBlock>
{
SharedCounter<SandStoneBlock> *pc;
};

```
#### SharedPtr<Sapling>
```cpp
/* 251071 */
struct SharedPtr<Sapling>
{
SharedCounter<Sapling> *pc;
};

```
#### SharedPtr<SaplingBlockItem>
```cpp
/* 184032 */
struct SharedPtr<SaplingBlockItem>
{
SharedCounter<SaplingBlockItem> *pc;
};

```
#### SharedPtr<ScaffoldingBlock>
```cpp
/* 251691 */
struct SharedPtr<ScaffoldingBlock>
{
SharedCounter<ScaffoldingBlock> *pc;
};

```
#### SharedPtr<ScaffoldingBlockItem>
```cpp
/* 184060 */
struct SharedPtr<ScaffoldingBlockItem>
{
SharedCounter<ScaffoldingBlockItem> *pc;
};

```
#### SharedPtr<SeaGrass>
```cpp
/* 251667 */
struct SharedPtr<SeaGrass>
{
SharedCounter<SeaGrass> *pc;
};

```
#### SharedPtr<SeaLanternBlock>
```cpp
/* 251494 */
struct SharedPtr<SeaLanternBlock>
{
SharedCounter<SeaLanternBlock> *pc;
};

```
#### SharedPtr<SeaPickle>
```cpp
/* 251671 */
struct SharedPtr<SeaPickle>
{
SharedCounter<SeaPickle> *pc;
};

```
#### SharedPtr<SeaPickleBlockItem>
```cpp
/* 184028 */
struct SharedPtr<SeaPickleBlockItem>
{
SharedCounter<SeaPickleBlockItem> *pc;
};

```
#### SharedPtr<ShearsItem>
```cpp
/* 183882 */
struct SharedPtr<ShearsItem>
{
SharedCounter<ShearsItem> *pc;
};

```
#### SharedPtr<ShieldItem>
```cpp
/* 183819 */
struct SharedPtr<ShieldItem>
{
SharedCounter<ShieldItem> *pc;
};

```
#### SharedPtr<ShovelItem>
```cpp
/* 183776 */
struct SharedPtr<ShovelItem>
{
SharedCounter<ShovelItem> *pc;
};

```
#### SharedPtr<ShulkerBoxBlock>
```cpp
/* 251558 */
struct SharedPtr<ShulkerBoxBlock>
{
SharedCounter<ShulkerBoxBlock> *pc;
};

```
#### SharedPtr<ShulkerBoxBlockItem>
```cpp
/* 184052 */
struct SharedPtr<ShulkerBoxBlockItem>
{
SharedCounter<ShulkerBoxBlockItem> *pc;
};

```
#### SharedPtr<SignBlock>
```cpp
/* 251221 */
struct SharedPtr<SignBlock>
{
SharedCounter<SignBlock> *pc;
};

```
#### SharedPtr<SignItem>
```cpp
/* 183826 */
struct SharedPtr<SignItem>
{
SharedCounter<SignItem> *pc;
};

```
#### SharedPtr<SkullBlock>
```cpp
/* 251435 */
struct SharedPtr<SkullBlock>
{
SharedCounter<SkullBlock> *pc;
};

```
#### SharedPtr<SkullItem>
```cpp
/* 183923 */
struct SharedPtr<SkullItem>
{
SharedCounter<SkullItem> *pc;
};

```
#### SharedPtr<SlimeBlock>
```cpp
/* 251486 */
struct SharedPtr<SlimeBlock>
{
SharedCounter<SlimeBlock> *pc;
};

```
#### SharedPtr<SmokerBlock>
```cpp
/* 251722 */
struct SharedPtr<SmokerBlock>
{
SharedCounter<SmokerBlock> *pc;
};

```
#### SharedPtr<SnowBlock>
```cpp
/* 251262 */
struct SharedPtr<SnowBlock>
{
SharedCounter<SnowBlock> *pc;
};

```
#### SharedPtr<SnowballItem>
```cpp
/* 183846 */
struct SharedPtr<SnowballItem>
{
SharedCounter<SnowballItem> *pc;
};

```
#### SharedPtr<SoulSandBlock>
```cpp
/* 251290 */
struct SharedPtr<SoulSandBlock>
{
SharedCounter<SoulSandBlock> *pc;
};

```
#### SharedPtr<SparklerItem>
```cpp
/* 184003 */
struct SharedPtr<SparklerItem>
{
SharedCounter<SparklerItem> *pc;
};

```
#### SharedPtr<SplashPotionItem>
```cpp
/* 183957 */
struct SharedPtr<SplashPotionItem>
{
SharedCounter<SplashPotionItem> *pc;
};

```
#### SharedPtr<SpongeBlock>
```cpp
/* 251107 */
struct SharedPtr<SpongeBlock>
{
SharedCounter<SpongeBlock> *pc;
};

```
#### SharedPtr<StainedGlassBlock>
```cpp
/* 251578 */
struct SharedPtr<StainedGlassBlock>
{
SharedCounter<StainedGlassBlock> *pc;
};

```
#### SharedPtr<StainedGlassPaneBlock>
```cpp
/* 251474 */
struct SharedPtr<StainedGlassPaneBlock>
{
SharedCounter<StainedGlassPaneBlock> *pc;
};

```
#### SharedPtr<StairBlock>
```cpp
/* 251196 */
struct SharedPtr<StairBlock>
{
SharedCounter<StairBlock> *pc;
};

```
#### SharedPtr<StemBlock>
```cpp
/* 251333 */
struct SharedPtr<StemBlock>
{
SharedCounter<StemBlock> *pc;
};

```
#### SharedPtr<StoneBlock>
```cpp
/* 251055 */
struct SharedPtr<StoneBlock>
{
SharedCounter<StoneBlock> *pc;
};

```
#### SharedPtr<StoneBrickBlock>
```cpp
/* 251318 */
struct SharedPtr<StoneBrickBlock>
{
SharedCounter<StoneBrickBlock> *pc;
};

```
#### SharedPtr<StoneButtonBlock>
```cpp
/* 251251 */
struct SharedPtr<StoneButtonBlock>
{
SharedCounter<StoneButtonBlock> *pc;
};

```
#### SharedPtr<StoneSlabBlock2>
```cpp
/* 251514 */
struct SharedPtr<StoneSlabBlock2>
{
SharedCounter<StoneSlabBlock2> *pc;
};

```
#### SharedPtr<StoneSlabBlock3>
```cpp
/* 251703 */
struct SharedPtr<StoneSlabBlock3>
{
SharedCounter<StoneSlabBlock3> *pc;
};

```
#### SharedPtr<StoneSlabBlock4>
```cpp
/* 251707 */
struct SharedPtr<StoneSlabBlock4>
{
SharedCounter<StoneSlabBlock4> *pc;
};

```
#### SharedPtr<StoneSlabBlock>
```cpp
/* 251172 */
struct SharedPtr<StoneSlabBlock>
{
SharedCounter<StoneSlabBlock> *pc;
};

```
#### SharedPtr<StoneSlabBlockItem>
```cpp
/* 184019 */
struct SharedPtr<StoneSlabBlockItem>
{
SharedCounter<StoneSlabBlockItem> *pc;
};

```
#### SharedPtr<StonecutterBlock>
```cpp
/* 251594 */
struct SharedPtr<StonecutterBlock>
{
SharedCounter<StonecutterBlock> *pc;
};

```
#### SharedPtr<StrippedLogBlock>
```cpp
/* 251614 */
struct SharedPtr<StrippedLogBlock>
{
SharedCounter<StrippedLogBlock> *pc;
};

```
#### SharedPtr<StructureBlock>
```cpp
/* 251610 */
struct SharedPtr<StructureBlock>
{
SharedCounter<StructureBlock> *pc;
};

```
#### SharedPtr<StructureVoid>
```cpp
/* 251554 */
struct SharedPtr<StructureVoid>
{
SharedCounter<StructureVoid> *pc;
};

```
#### SharedPtr<SuspiciousStewItem>
```cpp
/* 183975 */
struct SharedPtr<SuspiciousStewItem>
{
SharedCounter<SuspiciousStewItem> *pc;
};

```
#### SharedPtr<SweetBerryBushBlock>
```cpp
/* 251742 */
struct SharedPtr<SweetBerryBushBlock>
{
SharedCounter<SweetBerryBushBlock> *pc;
};

```
#### SharedPtr<TallGrass>
```cpp
/* 251145 */
struct SharedPtr<TallGrass>
{
SharedCounter<TallGrass> *pc;
};

```
#### SharedPtr<ThinFenceBlock>
```cpp
/* 251325 */
struct SharedPtr<ThinFenceBlock>
{
SharedCounter<ThinFenceBlock> *pc;
};

```
#### SharedPtr<TntBlock>
```cpp
/* 251176 */
struct SharedPtr<TntBlock>
{
SharedCounter<TntBlock> *pc;
};

```
#### SharedPtr<TopSnowBlock>
```cpp
/* 251255 */
struct SharedPtr<TopSnowBlock>
{
SharedCounter<TopSnowBlock> *pc;
};

```
#### SharedPtr<TopSnowBlockItem>
```cpp
/* 184048 */
struct SharedPtr<TopSnowBlockItem>
{
SharedCounter<TopSnowBlockItem> *pc;
};

```
#### SharedPtr<TorchBlock>
```cpp
/* 251188 */
struct SharedPtr<TorchBlock>
{
SharedCounter<TorchBlock> *pc;
};

```
#### SharedPtr<TrapDoorBlock>
```cpp
/* 251311 */
struct SharedPtr<TrapDoorBlock>
{
SharedCounter<TrapDoorBlock> *pc;
};

```
#### SharedPtr<TridentItem>
```cpp
/* 183943 */
struct SharedPtr<TridentItem>
{
SharedCounter<TridentItem> *pc;
};

```
#### SharedPtr<TripWireBlock>
```cpp
/* 251404 */
struct SharedPtr<TripWireBlock>
{
SharedCounter<TripWireBlock> *pc;
};

```
#### SharedPtr<TripWireHookBlock>
```cpp
/* 251400 */
struct SharedPtr<TripWireHookBlock>
{
SharedCounter<TripWireHookBlock> *pc;
};

```
#### SharedPtr<TurtleEggBlock>
```cpp
/* 251683 */
struct SharedPtr<TurtleEggBlock>
{
SharedCounter<TurtleEggBlock> *pc;
};

```
#### SharedPtr<UnderwaterTorchBlock>
```cpp
/* 251628 */
struct SharedPtr<UnderwaterTorchBlock>
{
SharedCounter<UnderwaterTorchBlock> *pc;
};

```
#### SharedPtr<UndyedShulkerBoxBlock>
```cpp
/* 251530 */
struct SharedPtr<UndyedShulkerBoxBlock>
{
SharedCounter<UndyedShulkerBoxBlock> *pc;
};

```
#### SharedPtr<VineBlock>
```cpp
/* 251337 */
struct SharedPtr<VineBlock>
{
SharedCounter<VineBlock> *pc;
};

```
#### SharedPtr<WallBlock>
```cpp
/* 251415 */
struct SharedPtr<WallBlock>
{
SharedCounter<WallBlock> *pc;
};

```
#### SharedPtr<WaterLilyBlockItem>
```cpp
/* 184044 */
struct SharedPtr<WaterLilyBlockItem>
{
SharedCounter<WaterLilyBlockItem> *pc;
};

```
#### SharedPtr<WaterlilyBlock>
```cpp
/* 251349 */
struct SharedPtr<WaterlilyBlock>
{
SharedCounter<WaterlilyBlock> *pc;
};

```
#### SharedPtr<WeaponItem>
```cpp
/* 183804 */
struct SharedPtr<WeaponItem>
{
SharedCounter<WeaponItem> *pc;
};

```
#### SharedPtr<WebBlock>
```cpp
/* 251141 */
struct SharedPtr<WebBlock>
{
SharedCounter<WebBlock> *pc;
};

```
#### SharedPtr<WeightedPressurePlateBlock>
```cpp
/* 251443 */
struct SharedPtr<WeightedPressurePlateBlock>
{
SharedCounter<WeightedPressurePlateBlock> *pc;
};

```
#### SharedPtr<WitherRoseBlock>
```cpp
/* 251769 */
struct SharedPtr<WitherRoseBlock>
{
SharedCounter<WitherRoseBlock> *pc;
};

```
#### SharedPtr<WoodBlock>
```cpp
/* 251758 */
struct SharedPtr<WoodBlock>
{
SharedCounter<WoodBlock> *pc;
};

```
#### SharedPtr<WoodButtonBlock>
```cpp
/* 251431 */
struct SharedPtr<WoodButtonBlock>
{
SharedCounter<WoodButtonBlock> *pc;
};

```
#### SharedPtr<WoodSlabBlock>
```cpp
/* 251466 */
struct SharedPtr<WoodSlabBlock>
{
SharedCounter<WoodSlabBlock> *pc;
};

```
#### SharedPtr<WoodSlabBlockItem>
```cpp
/* 184040 */
struct SharedPtr<WoodSlabBlockItem>
{
SharedCounter<WoodSlabBlockItem> *pc;
};

```
#### SharedPtr<WoolCarpetBlock>
```cpp
/* 251502 */
struct SharedPtr<WoolCarpetBlock>
{
SharedCounter<WoolCarpetBlock> *pc;
};

```
#### SharedPtr<WorkbenchBlock>
```cpp
/* 251206 */
struct SharedPtr<WorkbenchBlock>
{
SharedCounter<WorkbenchBlock> *pc;
};

```
#### SharedPtr<WritableBookItem>
```cpp
/* 183912 */
struct SharedPtr<WritableBookItem>
{
SharedCounter<WritableBookItem> *pc;
};

```
#### SharedPtr<WrittenBookItem>
```cpp
/* 183916 */
struct SharedPtr<WrittenBookItem>
{
SharedCounter<WrittenBookItem> *pc;
};

```
#### ShieldItemUtils
```cpp
/* 183434 */
struct ShieldItemUtils
{
__int8 gap0[1];
};

```
#### ShoreTransformation;
```cpp
/* 198717 */
struct ShoreTransformation;

```
#### Shulker::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 171018 */
struct Shulker::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Silverfish::spawnAnim::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 171020 */
struct Silverfish::spawnAnim::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SimpleContainer
```cpp
/* 89261 */
struct SimpleContainer
{
__int8 baseclass_0[244];
int mSize;
std::vector<ItemStack> mItems;
};

```
#### SimplexNoise
```cpp
/* 34414 */
struct SimplexNoise
{
Vec3 mOrigin;
int mNoiseMap[512];
};

```
#### SkinAdjustments
```cpp
/* 88757 */
struct SkinAdjustments
{
unsigned int mAnimOverrideBitmask;
};

```
#### SkinData
```cpp
/* 44370 */
struct SkinData
{
std::optional<int> mVariant;
std::optional<int> mMarkVariant;
};

```
#### SkinHash
```cpp
/* 171257 */
struct SkinHash
{
size_t geoLength;
uint64_t shaData[8];
};

```
#### SkinInfoData
```cpp
/* 173189 */
struct SkinInfoData
{
int (**_vptr$SkinInfoData)(void);
std::string mDefaultMeshName;
bool mIsAlphaTest;
bool mIsDirty;
SerializedSkin mSkin;
};

```
#### SlabBlockItem::_useOn::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 227140 */
struct SlabBlockItem::_useOn::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SlotDescriptor
```cpp
/* 100018 */
struct SlotDescriptor
{
int mSlot;
std::vector<ItemInstance> mAcceptedItems;
const Item *mItem;
std::string mInteractText;
DefinitionTrigger mOnEquip;
DefinitionTrigger mOnUnequip;
};

```
#### SlotDropChance
```cpp
/* 89150 */
struct SlotDropChance
{
EquipmentSlot mSlot;
float mDropChance;
};

```
#### SmallSet<Actor *>
```cpp
/* 88055 */
struct SmallSet<Actor *>
{
std::vector<Actor *> c;
};

```
#### SmallSet<ActorUniqueID>
```cpp
/* 238400 */
struct SmallSet<ActorUniqueID>
{
std::vector<ActorUniqueID> c;
};

```
#### SmallSet<DBChunkStorage *>
```cpp
/* 462662 */
struct SmallSet<DBChunkStorage *>
{
std::vector<DBChunkStorage *> c;
};

```
#### SmallSet<WorkerPool *>
```cpp
/* 81991 */
struct SmallSet<WorkerPool *>
{
std::vector<WorkerPool *> c;
};

```
#### SnapshotFilenameAndLength
```cpp
/* 6450 */
struct SnapshotFilenameAndLength
{
std::string filename;
uint64_t filesize;
};

```
#### Social::Events::IEventListener;
```cpp
/* 42828 */
struct Social::Events::IEventListener;

```
#### Social::Events::Measurement
```cpp
/* 43074 */
struct Social::Events::Measurement
{
std::string mName;
Json::Value mValue;
int mValueDivisorForAverage;
Social::Events::Measurement::AggregationType mType;
};

```
#### Social::Events::Property
```cpp
/* 42921 */
struct Social::Events::Property
{
std::string mName;
Json::Value mValue;
};

```
#### Social::GameConnectionInfo
```cpp
/* 63698 */
struct Social::GameConnectionInfo
{
Social::ConnectionType mType;
std::string mHostIpAddress;
std::string mUnresolvedUrl;
int mPort;
std::string mRakNetGUID;
ThirdPartyInfo mThirdPartyServerInfo;
};

```
#### Social::IUserManager;
```cpp
/* 44956 */
struct Social::IUserManager;

```
#### Social::MultiplayerService;
```cpp
/* 479541 */
struct Social::MultiplayerService;

```
#### Social::User;
```cpp
/* 44200 */
struct Social::User;

```
#### Social::UserPicturePath
```cpp
/* 44126 */
struct Social::UserPicturePath
{
std::shared_ptr<ResourceLocation> mLocation;
};

```
#### Social::XboxLiveUser;
```cpp
/* 45093 */
struct Social::XboxLiveUser;

```
#### SortItemInstanceIdAux
```cpp
/* 75857 */
struct SortItemInstanceIdAux
{
__int8 gap0[1];
};

```
#### SoundItem;
```cpp
/* 87050 */
struct SoundItem;

```
#### SoundPlayer;
```cpp
/* 86997 */
struct SoundPlayer;

```
#### SparklerItem::ColorInfo
```cpp
/* 457256 */
struct SparklerItem::ColorInfo
{
ItemColor mDyeId;
CompoundType mColorCompound;
int mVariantIndex;
int mRGB;
};

```
#### SpatialActorNetworkData
```cpp
/* 77504 */
struct SpatialActorNetworkData
{
Actor *mEntity;
bool mHasInitializedLastSent;
bool mAutoSend;
MoveActorAbsoluteData mLastSentMoveData;
MoveActorAbsoluteData mLastReceivedMoveData;
};

```
#### SpawnActorComponent
```cpp
/* 59118 */
struct SpawnActorComponent
{
std::vector<SpawnActorEntry> mSpawnEntries;
};

```
#### SpawnActorParameters
```cpp
/* 59072 */
struct SpawnActorParameters
{
bool mSpawnsItemStack;
int mSpawnTimeMin;
int mSpawnTimeMax;
int mSpawnTimer;
LevelSoundEvent mSpawnSound;
const Item *mItem;
std::string mEntityDefinition;
std::string mSpawnMethod;
ActorFilterGroup mFilters;
bool mSingleUse;
bool mShouldLeash;
int mNumToSpawn;
};

```
#### SpawnConditions
```cpp
/* 37046 */
struct SpawnConditions
{
bool isOnSurface;
bool isInWater;
bool isInLava;
bool isUnderground;
uint64_t delayEndWorldAge;
int rawBrightness;
BlockPos pos;
};

```
#### SpawnGroupData
```cpp
/* 190808 */
struct SpawnGroupData
{
std::string mIdentifier;
std::vector<MobSpawnRules> mSpawnRules;
};

```
#### SpecificEnchantFunction::EnchantInfo
```cpp
/* 291647 */
struct SpecificEnchantFunction::EnchantInfo
{
Enchant::Type enchantment;
int level;
};

```
#### SpikeFeature::EndSpike
```cpp
/* 255156 */
struct SpikeFeature::EndSpike
{
const int mCenterX;
const int mCenterZ;
const int mRadius;
const int mHeight;
const bool mGuarded;
const AABB mTopBoundingBox;
};

```
#### SpongeBlock::_spawnAbsorbParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 460015 */
struct SpongeBlock::_spawnAbsorbParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Squid::aiStep::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124436 */
struct Squid::aiStep::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Squid::spawnInkParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124435 */
struct Squid::spawnInkParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Squid::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124437 */
struct Squid::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### StackResultStorageEntity
```cpp
/* 13182 */
struct StackResultStorageEntity
{
std::optional<EntityContext> mContext;
};

```
#### StackResultStorageFeature
```cpp
/* 31083 */
struct StackResultStorageFeature
{
std::optional<std::reference_wrapper<FeatureRegistry> > mRegistry;
size_t mIndex;
};

```
#### StackResultStorageSharePtr<EntityRegistry>
```cpp
/* 13165 */
struct StackResultStorageSharePtr<EntityRegistry>
{
std::shared_ptr<EntityRegistry> mValue;
};

```
#### StackResultStorageSharePtr<PerlinSimplexNoise>
```cpp
/* 191531 */
struct StackResultStorageSharePtr<PerlinSimplexNoise>
{
std::shared_ptr<PerlinSimplexNoise> mValue;
};

```
#### StackStats
```cpp
/* 45335 */
struct StackStats
{
PackType mStackType;
uint32_t mPackCount;
double mParseTime;
};

```
#### StackedGraphBars::ColorKey
```cpp
/* 421771 */
struct StackedGraphBars::ColorKey
{
char colorTag;
std::string name;
};

```
#### StartGamePacket::write::$5498B64B1945F9BCA5158804213C50F5
```cpp
/* 80901 */
struct StartGamePacket::write::$5498B64B1945F9BCA5158804213C50F5
{
std::unique_ptr<ListTag> *blockPaletteList;
};

```
#### StateAnimationVariable
```cpp
/* 125167 */
struct StateAnimationVariable
{
HashedString mVariableName;
ExpressionNode mInput;
std::vector<AnimationValueCurveKeyFrame> mKeyFrames;
};

```
#### StateVectorComponent
```cpp
/* 45380 */
struct StateVectorComponent
{
Vec3 mPos;
Vec3 mPosPrev;
Vec3 mPosDelta;
};

```
#### Stopwatch
```cpp
/* 85830 */
struct Stopwatch
{
int (**_vptr$Stopwatch)(void);
double _st;
double _tt;
double _last;
double _max;
int _count;
int _printcounter;
};

```
#### StoreSearchTelemetryData;
```cpp
/* 45340 */
struct StoreSearchTelemetryData;

```
#### StrongholdFeature::StrongholdResult
```cpp
/* 42641 */
struct StrongholdFeature::StrongholdResult
{
bool success;
ChunkPos location;
};

```
#### StructureBlockPalette
```cpp
/* 77486 */
struct StructureBlockPalette
{
std::vector<std::unique_ptr<CompoundTag>> mStructurePaletteIdToSerializationId;
std::unordered_map<unsigned long,StructureBlockPalette::BlockPositionData> mBlockPositionData;
};

```
#### StructureBlockPalette::BlockPositionData
```cpp
/* 74447 */
struct StructureBlockPalette::BlockPositionData
{
std::unique_ptr<CompoundTag> mBlockEntityData;
std::vector<StructureBlockPalette::TickingQueueData> mTickData;
};

```
#### StructureBlockPalette::TickingQueueData
```cpp
/* 74460 */
struct StructureBlockPalette::TickingQueueData
{
int mTickDelay;
};

```
#### StructureEditorData
```cpp
/* 45347 */
struct StructureEditorData
{
std::string mStructureName;
std::string mDataField;
bool mIncludePlayers;
bool mShowBoundingBox;
StructureRedstoneSaveMode mRedstoneSaveMode;
StructureBlockType mType;
StructureSettings mSettings;
};

```
#### StructureEditorData_0
```cpp
/* 80908 */
struct StructureEditorData_0
{
std::string mStructureName;
std::string mDataField;
bool mIncludePlayers;
bool mShowBoundingBox;
StructureRedstoneSaveMode mRedstoneSaveMode;
StructureBlockType mType;
StructureSettings_0 mSettings;
};

```
#### StructureEditorData_1
```cpp
/* 238479 */
struct StructureEditorData_1
{
std::string mStructureName;
std::string mDataField;
bool mIncludePlayers;
bool mShowBoundingBox;
StructureRedstoneSaveMode mRedstoneSaveMode;
StructureBlockType mType;
StructureSettings_1 mSettings;
};

```
#### StructureFeature::findFarAwayStructures::StructureInfo
```cpp
/* 287709 */
struct StructureFeature::findFarAwayStructures::StructureInfo
{
ChunkPos min;
ChunkPos max;
ChunkPos id;
};

```
#### StructureHelpers
```cpp
/* 287770 */
struct StructureHelpers
{
__int8 gap0[1];
};

```
#### StructureIntegrityProcessor
```cpp
/* 288382 */
struct StructureIntegrityProcessor
{
float mIntegrity;
RandomSeed mStartSeed;
};

```
#### StructureIntegrityProcessor_0
```cpp
/* 462024 */
struct StructureIntegrityProcessor_0
{
float mIntegrity;
RandomSeed_0 mStartSeed;
};

```
#### StructureManager
```cpp
/* 32815 */
struct StructureManager
{
SharedMutex mRepositoryMutex;
std::unordered_map<std::string,std::unique_ptr<LegacyStructureTemplate>> mLegacyStructureRepository;
std::unordered_map<std::string,std::unique_ptr<StructureTemplate>> mStructureRepository;
LevelStorage *mLevelStorage;
ResourcePackManager *mPackManager;
};

```
#### StructurePiece
```cpp
/* 31308 */
struct StructurePiece
{
int (**_vptr$StructurePiece)(void);
BoundingBox mBoundingBox;
int mOrientation;
int mGenDepth;
};

```
#### StructurePoolActorRule
```cpp
/* 35465 */
struct StructurePoolActorRule
{
const Unique<IStructurePoolActorPredicate> mSourcePredicate;
const std::string mResultActor;
};

```
#### StructurePoolBlockRule
```cpp
/* 35649 */
struct StructurePoolBlockRule
{
const Unique<IStructurePoolBlockPredicate> mSourcePredicate;
const Unique<IStructurePoolBlockPredicate> mTargetPredicate;
const Block *mResultBlock;
};

```
#### StructurePoolBlockTagRule
```cpp
/* 35906 */
struct StructurePoolBlockTagRule
{
const Unique<IStructurePoolBlockTagPredicate> mSourcePredicate;
const std::string mResultKey;
const std::string mResultValue;
};

```
#### StructurePoolElement
```cpp
/* 31953 */
struct StructurePoolElement
{
int (**_vptr$StructurePoolElement)(void);
std::once_flag mTemplateOnceFlag;
std::optional<StructurePoolElement::LazyTemplate> mTemplate;
std::string mLocation;
StructureManager *mManager;
bool mValid;
Projection mProjection;
const StructurePoolBlockRuleList *mBlockRules;
const StructurePoolBlockTagRuleList *mBlockTagRules;
const StructurePoolActorRuleList *mActorRules;
};

```
#### StructurePoolElement::LazyTemplate
```cpp
/* 289311 */
struct StructurePoolElement::LazyTemplate
{
LegacyStructureTemplate *mStructure;
std::vector<JigsawBlockInfo> mJigsawMarkers;
};

```
#### StructureStart
```cpp
/* 38732 */
struct StructureStart
{
int (**_vptr$StructureStart)(void);
BoundingBox boundingBox;
int chunkX;
int chunkZ;
PieceList pieces;
};

```
#### StructureTelemetryClientData
```cpp
/* 45349 */
struct StructureTelemetryClientData
{
uint32_t mSizeEditCount;
uint32_t mOffsetEditCount;
uint32_t mRotationEditCount;
uint32_t mMirrorEditCount;
};

```
#### StructureTelemetryServerData
```cpp
/* 77485 */
struct StructureTelemetryServerData
{
bool mHasBeenActivatedByRedstone;
bool mHasLoadedIntoUnloadedChunks;
BlockPos mLastOffsetWhenLoadingIntoUnloadedChunks;
};

```
#### StructureTemplate
```cpp
/* 41934 */
struct StructureTemplate
{
std::string mName;
StructureTemplateData mStructureTemplateData;
};

```
#### StructureTemplate::_fillBlockInfo::$2FA47CEBC638377704193C5643AD3DC1
```cpp
/* 288378 */
struct StructureTemplate::_fillBlockInfo::$2FA47CEBC638377704193C5643AD3DC1
{
std::map<const Block *,int> *blockToIndex;
StructureBlockPalette *structureBlockPalette;
const Block *voidBlock;
};

```
#### StructureTemplateData
```cpp
/* 74503 */
struct StructureTemplateData
{
int (**_vptr$StructureTemplateData)(void);
int mFormatVersion;
BlockPos mSize;
BlockPos mStructureWorldOrigin;
std::vector<int> mBlockIndices;
std::vector<int> mExtraBlockIndices;
std::unordered_map<std::string,StructureBlockPalette> mPalettes;
std::vector<std::unique_ptr<CompoundTag>> mEntityData;
};

```
#### StructureTemplateFeature::BoundingBox2D
```cpp
/* 280104 */
struct StructureTemplateFeature::BoundingBox2D
{
Vec2 min;
Vec2 max;
};

```
#### StructureTemplatePool
```cpp
/* 32001 */
struct StructureTemplatePool
{
std::string mName;
std::vector<const StructurePoolElement *> mTemplates;
std::string mFallback;
};

```
#### SubChunk
```cpp
/* 35007 */
struct SubChunk
{
DirtyTicksCounter mDirtyTicksCounter;
std::unique_ptr<SubChunkBrightnessStorage> mLight;
std::unique_ptr<SubChunkBlockStorage> mBlocks[2];
SubChunkBlockStorage *mBlocksReadPtr[2];
SpinLock *mWriteLock;
};

```
#### SubChunkBlockPos
```cpp
/* 34732 */
struct SubChunkBlockPos
{
SubChunkBlockPos::$F507DBCC95B5F1F0349D6A6FBF2E560F _anon_0;
};

```
#### SubChunkBlockPos::$F507DBCC95B5F1F0349D6A6FBF2E560F::$E23C018BDD51DA9542B42FDC09D6AA49
```cpp
/* 34734 */
struct SubChunkBlockPos::$F507DBCC95B5F1F0349D6A6FBF2E560F::$E23C018BDD51DA9542B42FDC09D6AA49
{
uint8_t x;
uint8_t y;
uint8_t z;
};

```
#### SubChunkBlockStorage
```cpp
/* 33596 */
struct SubChunkBlockStorage
{
int (**_vptr$SubChunkBlockStorage)(void);
};

```
#### SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 253613 */
struct SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$242ED9D411BD064A57C4553B835CD0FE
```cpp
/* 253619 */
struct SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$242ED9D411BD064A57C4553B835CD0FE
{
const std::bitset<2> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$633D66453D3F5664A26EE59CDFD22959
```cpp
/* 253620 */
struct SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$633D66453D3F5664A26EE59CDFD22959
{
const std::bitset<2> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
```cpp
/* 253621 */
struct SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
{
uint16_t *max;
std::vector<unsigned short> *outOfBoundSlots;
size_t *idx;
};

```
#### SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
```cpp
/* 253617 */
struct SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
{
const BoundingBox *box;
};

```
#### SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
```cpp
/* 253616 */
struct SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
{
uint32_t height;
uint32_t radius;
const BlockPos *pos;
};

```
#### SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::findUsedIndices::$89D4AD7C0CE71E5C121270538A6F6D8C
```cpp
/* 253618 */
struct SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::findUsedIndices::$89D4AD7C0CE71E5C121270538A6F6D8C
{
std::bitset<2> *existing;
};

```
#### SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::makePrunedCopy::$5C37BA6189407DC409FF9D08D5F65A9E
```cpp
/* 253615 */
struct SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::makePrunedCopy::$5C37BA6189407DC409FF9D08D5F65A9E
{
std::array<unsigned long,2> *remappingLookup;
};

```
#### SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 253670 */
struct SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$6F135F9B09AF7761430A35C180173A8C
```cpp
/* 253675 */
struct SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$6F135F9B09AF7761430A35C180173A8C
{
const std::bitset<4096> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$290B4DE2DB2BE431220A17F6F7E7C4F0
```cpp
/* 253676 */
struct SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$290B4DE2DB2BE431220A17F6F7E7C4F0
{
const std::bitset<4096> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
```cpp
/* 253677 */
struct SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
{
uint16_t *max;
std::vector<unsigned short> *outOfBoundSlots;
size_t *idx;
};

```
#### SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
```cpp
/* 253673 */
struct SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
{
const BoundingBox *box;
};

```
#### SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
```cpp
/* 253672 */
struct SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
{
uint32_t height;
uint32_t radius;
const BlockPos *pos;
};

```
#### SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::findUsedIndices::$6336BD0E2483FB0EFB3F76DC3EBC5309
```cpp
/* 253674 */
struct SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::findUsedIndices::$6336BD0E2483FB0EFB3F76DC3EBC5309
{
std::bitset<4096> *existing;
};

```
#### SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::makePrunedCopy::$2185D287A3144BABD0B238662BD24236
```cpp
/* 253671 */
struct SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::makePrunedCopy::$2185D287A3144BABD0B238662BD24236
{
std::array<unsigned long,4096> *remappingLookup;
};

```
#### SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 253622 */
struct SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$66FA6D0B33FF0D79D1FAEF5E715B6A50
```cpp
/* 253627 */
struct SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$66FA6D0B33FF0D79D1FAEF5E715B6A50
{
const std::bitset<4> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$5D469001403E80B2A426E4718973955B
```cpp
/* 253628 */
struct SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$5D469001403E80B2A426E4718973955B
{
const std::bitset<4> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
```cpp
/* 253629 */
struct SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
{
uint16_t *max;
std::vector<unsigned short> *outOfBoundSlots;
size_t *idx;
};

```
#### SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
```cpp
/* 253625 */
struct SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
{
const BoundingBox *box;
};

```
#### SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
```cpp
/* 253624 */
struct SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
{
uint32_t height;
uint32_t radius;
const BlockPos *pos;
};

```
#### SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::findUsedIndices::$D3A89A71AD77E1A6A761C588139D92F8
```cpp
/* 253626 */
struct SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::findUsedIndices::$D3A89A71AD77E1A6A761C588139D92F8
{
std::bitset<4> *existing;
};

```
#### SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::makePrunedCopy::$97D49D667F65B59D64A1CF6C21EF1D86
```cpp
/* 253623 */
struct SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::makePrunedCopy::$97D49D667F65B59D64A1CF6C21EF1D86
{
std::array<unsigned long,4> *remappingLookup;
};

```
#### SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 253630 */
struct SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$C26F408D3D152A4098209C2CE9387EF2
```cpp
/* 253635 */
struct SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$C26F408D3D152A4098209C2CE9387EF2
{
const std::bitset<8> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$09FE199C713A938B3B17002F6F47058A
```cpp
/* 253636 */
struct SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$09FE199C713A938B3B17002F6F47058A
{
const std::bitset<8> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
```cpp
/* 253637 */
struct SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
{
uint16_t *max;
std::vector<unsigned short> *outOfBoundSlots;
size_t *idx;
};

```
#### SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
```cpp
/* 253633 */
struct SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
{
const BoundingBox *box;
};

```
#### SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
```cpp
/* 253632 */
struct SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
{
uint32_t height;
uint32_t radius;
const BlockPos *pos;
};

```
#### SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::findUsedIndices::$5D1D4294B57C53DD4C7D10D4AE89381A
```cpp
/* 253634 */
struct SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::findUsedIndices::$5D1D4294B57C53DD4C7D10D4AE89381A
{
std::bitset<8> *existing;
};

```
#### SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::makePrunedCopy::$9D7F1A052824D1DF666118F69FC3070A
```cpp
/* 253631 */
struct SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::makePrunedCopy::$9D7F1A052824D1DF666118F69FC3070A
{
std::array<unsigned long,8> *remappingLookup;
};

```
#### SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 253638 */
struct SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$4917742FCBCB7D234EAD1B5E3DA1DE4E
```cpp
/* 253643 */
struct SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$4917742FCBCB7D234EAD1B5E3DA1DE4E
{
const std::bitset<16> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$28E5234A30BDDE39C7BEB7FA929ADF5A
```cpp
/* 253644 */
struct SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$28E5234A30BDDE39C7BEB7FA929ADF5A
{
const std::bitset<16> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
```cpp
/* 253645 */
struct SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
{
uint16_t *max;
std::vector<unsigned short> *outOfBoundSlots;
size_t *idx;
};

```
#### SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
```cpp
/* 253641 */
struct SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
{
const BoundingBox *box;
};

```
#### SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
```cpp
/* 253640 */
struct SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
{
uint32_t height;
uint32_t radius;
const BlockPos *pos;
};

```
#### SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::findUsedIndices::$900FAD5FCE8D58777B797CA0B7FA2138
```cpp
/* 253642 */
struct SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::findUsedIndices::$900FAD5FCE8D58777B797CA0B7FA2138
{
std::bitset<16> *existing;
};

```
#### SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::makePrunedCopy::$05DA6B700FA0222B559606B9A00A1F7D
```cpp
/* 253639 */
struct SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::makePrunedCopy::$05DA6B700FA0222B559606B9A00A1F7D
{
std::array<unsigned long,16> *remappingLookup;
};

```
#### SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 253646 */
struct SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$AAA3ED88E6F951360D315A860A822F3A
```cpp
/* 253651 */
struct SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$AAA3ED88E6F951360D315A860A822F3A
{
const std::bitset<32> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$ED58595EF437FEAFABE4C940374EA69A
```cpp
/* 253652 */
struct SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$ED58595EF437FEAFABE4C940374EA69A
{
const std::bitset<32> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
```cpp
/* 253653 */
struct SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
{
uint16_t *max;
std::vector<unsigned short> *outOfBoundSlots;
size_t *idx;
};

```
#### SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
```cpp
/* 253649 */
struct SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
{
const BoundingBox *box;
};

```
#### SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
```cpp
/* 253648 */
struct SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
{
uint32_t height;
uint32_t radius;
const BlockPos *pos;
};

```
#### SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::findUsedIndices::$C463AA8D3B7416B6EACBAB570E768265
```cpp
/* 253650 */
struct SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::findUsedIndices::$C463AA8D3B7416B6EACBAB570E768265
{
std::bitset<32> *existing;
};

```
#### SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::makePrunedCopy::$CC93A48B8F76E12549E857D7142C04AB
```cpp
/* 253647 */
struct SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::makePrunedCopy::$CC93A48B8F76E12549E857D7142C04AB
{
std::array<unsigned long,32> *remappingLookup;
};

```
#### SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 253654 */
struct SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$B5E2A92EF98D0403FD7DBC5576FA3DFE
```cpp
/* 253659 */
struct SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$B5E2A92EF98D0403FD7DBC5576FA3DFE
{
const std::bitset<64> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$704CDF7438A6CF9DB4A498AA560B0A22
```cpp
/* 253660 */
struct SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$704CDF7438A6CF9DB4A498AA560B0A22
{
const std::bitset<64> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
```cpp
/* 253661 */
struct SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
{
uint16_t *max;
std::vector<unsigned short> *outOfBoundSlots;
size_t *idx;
};

```
#### SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
```cpp
/* 253657 */
struct SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
{
const BoundingBox *box;
};

```
#### SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
```cpp
/* 253656 */
struct SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
{
uint32_t height;
uint32_t radius;
const BlockPos *pos;
};

```
#### SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::findUsedIndices::$2990B7D608F6D64D2C15233EADEB07CB
```cpp
/* 253658 */
struct SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::findUsedIndices::$2990B7D608F6D64D2C15233EADEB07CB
{
std::bitset<64> *existing;
};

```
#### SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::makePrunedCopy::$B8D88B99E42BC318262126A78F11A7E5
```cpp
/* 253655 */
struct SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::makePrunedCopy::$B8D88B99E42BC318262126A78F11A7E5
{
std::array<unsigned long,64> *remappingLookup;
};

```
#### SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 253662 */
struct SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$1AEE232A0E96F160F80275F43A812658
```cpp
/* 253667 */
struct SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$1AEE232A0E96F160F80275F43A812658
{
const std::bitset<256> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$40981709DD800CB46A7EC240DF9DEAFC
```cpp
/* 253668 */
struct SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$40981709DD800CB46A7EC240DF9DEAFC
{
const std::bitset<256> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
```cpp
/* 253669 */
struct SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
{
uint16_t *max;
std::vector<unsigned short> *outOfBoundSlots;
size_t *idx;
};

```
#### SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
```cpp
/* 253665 */
struct SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
{
const BoundingBox *box;
};

```
#### SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
```cpp
/* 253664 */
struct SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
{
uint32_t height;
uint32_t radius;
const BlockPos *pos;
};

```
#### SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::findUsedIndices::$34AB7F28A08EB8CC59CD205CAB614B75
```cpp
/* 253666 */
struct SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::findUsedIndices::$34AB7F28A08EB8CC59CD205CAB614B75
{
std::bitset<256> *existing;
};

```
#### SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::makePrunedCopy::$3817DFAD228892A6745DC344E6C4662F
```cpp
/* 253663 */
struct SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::makePrunedCopy::$3817DFAD228892A6745DC344E6C4662F
{
std::array<unsigned long,256> *remappingLookup;
};

```
#### SubChunkBrightnessStorage
```cpp
/* 33558 */
struct SubChunkBrightnessStorage
{
std::array<SubChunkBrightnessStorage::LightPair,4096> mLight;
};

```
#### SubChunkBrightnessStorage::LightPair
```cpp
/* 33561 */
struct SubChunkBrightnessStorage::LightPair
{
SubChunkBrightnessStorage::LightPair::$C82CAE701F9C96804622E94D041F6011 _anon_0;
};

```
#### SubChunkBrightnessStorage::LightPair::$C82CAE701F9C96804622E94D041F6011::$FEA8D14758525B4BCA5C0100E71C9EA7
```cpp
/* 33563 */
struct SubChunkBrightnessStorage::LightPair::$C82CAE701F9C96804622E94D041F6011::$FEA8D14758525B4BCA5C0100E71C9EA7
{
unsigned __int8 blockLight : 4;
unsigned __int8 skyLight : 4;
};

```
#### SubChunkLightIndex
```cpp
/* 252527 */
struct SubChunkLightIndex
{
SubChunkLightIndex::$D642419CEF3A4ECC892D938F72F5EEEF _anon_0;
};

```
#### SubChunkLightIndex::$D642419CEF3A4ECC892D938F72F5EEEF::$1B14A3B4ACC00D53AE1F0B03F21ED5AD
```cpp
/* 252530 */
struct SubChunkLightIndex::$D642419CEF3A4ECC892D938F72F5EEEF::$1B14A3B4ACC00D53AE1F0B03F21ED5AD
{
unsigned __int32 mToDoIndex : 18;
unsigned __int32 mPad2 : 14;
};

```
#### SubChunkLightIndex::$D642419CEF3A4ECC892D938F72F5EEEF::$C5E0CE72C99D254AFB51B3E72BF5B343
```cpp
/* 252529 */
struct SubChunkLightIndex::$D642419CEF3A4ECC892D938F72F5EEEF::$C5E0CE72C99D254AFB51B3E72BF5B343
{
unsigned __int32 mSubChunkBlockY : 4;
unsigned __int32 mChunkIndexY : 2;
unsigned __int32 mSubChunkBlockZ : 4;
unsigned __int32 mChunkIndexZ : 2;
unsigned __int32 mSubChunkBlockX : 4;
unsigned __int32 mChunkIndexX : 2;
unsigned __int32 mPad : 8;
};

```
#### SubChunkRelighter
```cpp
/* 252862 */
struct SubChunkRelighter
{
bool mNeedToResetToDoBits;
std::bitset<196608> mToDo;
std::array<unsigned char,4096> mOldAbsorption;
std::vector<SubChunkLightIndex> mAdditiveBlocksToProcess[2][16];
std::vector<SubChunkLightIndex> mEdgeBlocksToProcess[16];
std::vector<SubChunkLightIndex> mBlocksToProcess[16];
std::vector<SubChunkLightIndex> mAbsorptionBlocksToProcess;
std::vector<SubtractiveLightInfo> mSubtractiveBlocks[2];
SubChunk *mSubChunkPtrArray[3][4][4];
bool mSubChunkPtrArrayValid[3][4][4];
bool mSubChunkTouched[3][4][4];
ChunkPos mCenterChunkPos;
size_t mCenterSubChunkIndex;
BlockSource *mSource;
bool mOriginalLighting;
SubChunkRelighter::LightPair mDefaultLightPair;
const Block *mDefaultBlock;
};

```
#### SubChunkStorageFormat::$4A48E9E2C062D44B94D66378C25E9D86
```cpp
/* 253612 */
struct SubChunkStorageFormat::$4A48E9E2C062D44B94D66378C25E9D86
{
__int8 network : 1;
__int8 type : 7;
};

```
#### SubClientConnectionRequest
```cpp
/* 73929 */
struct SubClientConnectionRequest
{
Unique<UnverifiedCertificate> mCertificateData;
Unique<Certificate> mCertificate;
Unique<WebToken> mRawToken;
};

```
#### SubpackInfoCollection
```cpp
/* 5712 */
struct SubpackInfoCollection
{
std::vector<SubpackInfo> mSubpackInfo;
};

```
#### SubtractiveLightInfo
```cpp
/* 252566 */
struct SubtractiveLightInfo
{
SubtractiveLightInfo::$6B0E6A960ECE12370BB5BB4D4B3FBF4C _anon_0;
};

```
#### SubtreeDefinition::load::$2A59718DDDE9B252D2E2D9E1042A23A6
```cpp
/* 454213 */
struct SubtreeDefinition::load::$2A59718DDDE9B252D2E2D9E1042A23A6
{
SubtreeDefinition *this;
};

```
#### SurfaceBuilderComponent
```cpp
/* 190841 */
struct SurfaceBuilderComponent
{
ISurfaceBuilder *mSurfaceBuilder;
};

```
#### SurfaceBuilderRegistry
```cpp
/* 88421 */
struct SurfaceBuilderRegistry
{
std::vector<SurfaceBuilderRegistry::Element> mSurfaceBuilders;
};

```
#### SurfaceBuilderRegistry::Element
```cpp
/* 88434 */
struct SurfaceBuilderRegistry::Element
{
std::unique_ptr<ISurfaceBuilder> mBuilder;
SurfaceBuilderRegistry::ScoringFunc mScoringFunc;
};

```
#### SurfaceMaterialAdjustmentAttributes
```cpp
/* 193919 */
struct SurfaceMaterialAdjustmentAttributes
{
std::vector<SurfaceMaterialAdjustmentAttributes::Element> mAdjustments;
};

```
#### SurfaceMaterialAdjustmentAttributes::Element
```cpp
/* 193031 */
struct SurfaceMaterialAdjustmentAttributes::Element
{
float mLowerBound;
float mUpperBound;
SurfaceMaterialAttributes mAdjustedMaterials;
};

```
#### SwampBiomeSurface;
```cpp
/* 198711 */
struct SwampBiomeSurface;

```
#### SHPortalRoom::postProcess::$A4BF091F36AB25C4BAD93320DD623D59
```cpp
/* 31937 */
struct SHPortalRoom::postProcess::$A4BF091F36AB25C4BAD93320DD623D59
{
const Block **endPortalEye;
const Block **endPortalNoEye;
};

```
#### SPSCQueue<BatchedNetworkPeer::DataCallback,512>
```cpp
/* 421255 */
struct SPSCQueue<BatchedNetworkPeer::DataCallback,512>
{
Lockless::WeakAtomic<SPSCQueue<BatchedNetworkPeer::DataCallback,512>::Block *> mFrontBlock;
char mCachelineFiller[56];
Lockless::WeakAtomic<SPSCQueue<BatchedNetworkPeer::DataCallback,512>::Block *> mTailBlock;
size_t mLargestBlockSize;
};

```
#### SPSCQueue<BatchedNetworkPeer::DataCallback,512>::Block
```cpp
/* 421196 */
struct SPSCQueue<BatchedNetworkPeer::DataCallback,512>::Block
{
Lockless::WeakAtomic<unsigned long> front;
size_t localTail;
char cachelineFiller0[48];
Lockless::WeakAtomic<unsigned long> tail;
size_t localFront;
char cachelineFiller1[48];
Lockless::WeakAtomic<SPSCQueue<BatchedNetworkPeer::DataCallback,512>::Block *> next;
char *data;
const size_t sizeMask;
char *rawThis;
};

```
#### SaveTransactionManager
```cpp
/* 3012 */
struct SaveTransactionManager
{
SaveTransactionManager::ShowIconFunction mShowIconFunction;
};

```
#### SavedData
```cpp
/* 34295 */
struct SavedData
{
int (**_vptr$SavedData)(void);
bool mDirty;
std::string mId;
};

```
#### SavedDataStorage
```cpp
/* 87726 */
struct SavedDataStorage
{
int (**_vptr$SavedDataStorage)(void);
LevelStorage *levelStorage;
std::unordered_map<std::string,SavedData *> savedDatas;
};

```
#### ScaffoldingClimberDefinition
```cpp
/* 412552 */
struct ScaffoldingClimberDefinition
{
__int8 gap0[1];
};

```
#### ScaleByAgeComponent
```cpp
/* 58652 */
struct ScaleByAgeComponent
{
float mStartScale;
float mEndScale;
};

```
#### ScaleByAgeDefinition
```cpp
/* 107549 */
struct ScaleByAgeDefinition
{
float mStartScale;
float mEndScale;
};

```
#### ScatterParams
```cpp
/* 192991 */
struct ScatterParams
{
ScatterParams::CoordinateRange mX;
ScatterParams::CoordinateRange mZ;
ScatterParams::CoordinateRange mHeight;
ScatterParams::CoordinateEvaluationOrder mEvalOrder;
ScatterParams::ChanceInformation mScatterChance;
ExpressionNode mIterations;
};

```
#### ScatterParams::ChanceInformation
```cpp
/* 192995 */
struct ScatterParams::ChanceInformation
{
ExpressionNode mChancePercent;
int mNumerator;
int mDenominator;
};

```
#### ScatterParams::CoordinateRange
```cpp
/* 192992 */
struct ScatterParams::CoordinateRange
{
ExpressionNode mMinOrSingleValue;
ExpressionNode mMax;
uint32_t mGridStepCount;
ScatterParams::RandomDistributionType mDistribution;
};

```
#### ScatterParams::ScatteredPositions
```cpp
/* 198707 */
struct ScatterParams::ScatteredPositions
{
RenderParams *mMolangParams;
Random *mRandom;
const ScatterParams *mScatterParams;
BlockPos mOrigin;
uint32_t mIterations;
};

```
#### ScatterParams::_getPos::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 457571 */
struct ScatterParams::_getPos::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### ScatterParams::initMolangParams::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 457570 */
struct ScatterParams::initMolangParams::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SceneFactory;
```cpp
/* 81128 */
struct SceneFactory;

```
#### SceneStack;
```cpp
/* 81127 */
struct SceneStack;

```
#### Scheduler
```cpp
/* 4391 */
struct Scheduler
{
uint32_t mTotalFrames;
uint32_t mStarvedFrames;
uint32_t mPromotionFrames;
uint32_t mTargetFPS;
uint32_t mEffectiveFPS;
uint32_t mFramesOverBound;
double mAverageCallbackDuration;
double mTotalCoroutineDuration;
size_t mTotalRunCoroutines;
double mCoroutineTimeLimit;
std::unique_ptr<WorkerPool> mCoroutinePool;
std::chrono::time_point<std::chrono::_V2::system_clock,std::chrono::duration<long,std::ratio<1,1000000000> > > mNextStarveCheckTime;
std::thread::id mThreadID;
};

```
#### Scheduler::ScopedChangeScheduler
```cpp
/* 484341 */
struct Scheduler::ScopedChangeScheduler
{
BackgroundWorker *mParent;
};

```
#### SchedulerComponent
```cpp
/* 58798 */
struct SchedulerComponent
{
int mCurrentEventIndex;
};

```
#### SchedulerDefinition
```cpp
/* 58854 */
struct SchedulerDefinition
{
std::vector<DefinitionTrigger> mTriggerDefs;
unsigned int mMinDelayTicks;
unsigned int mMaxDelayTicks;
};

```
#### ScopedAutoreleasePool
```cpp
/* 87060 */
struct ScopedAutoreleasePool
{
__int8 gap0[1];
};

```
#### ScopedProfileTag
```cpp
/* 103054 */
struct ScopedProfileTag
{
__int8 gap0[1];
};

```
#### ScoreInfo
```cpp
/* 80247 */
struct ScoreInfo
{
const Objective *mObjective;
bool mValid;
int mValue;
};

```
#### ScoreInfoRef
```cpp
/* 80248 */
struct ScoreInfoRef
{
const Objective *mObjective;
bool mValid;
int *mValue;
};

```
#### ScorePacketInfo
```cpp
/* 70049 */
struct ScorePacketInfo
{
ScoreboardId mScoreboardId;
std::string mObjectiveName;
int mScoreValue;
IdentityDefinition::Type mIdentityType;
PlayerScoreboardId mPlayerId;
ActorUniqueID mEntityId;
std::string mFakePlayerName;
};

```
#### Scoreboard
```cpp
/* 80249 */
struct Scoreboard
{
int (**_vptr$Scoreboard)(void);
CommandSoftEnumRegistry mRegistry;
std::unordered_map<std::string,DisplayObjective> mDisplayObjectives;
IdentityDictionary mIdentityDict;
std::unordered_map<ScoreboardId,ScoreboardIdentityRef> mIdentityRefs;
bool mShouldUpdateUI;
std::unordered_map<std::string,std::unique_ptr<Objective>> mObjectives;
std::unordered_map<std::string,std::unique_ptr<ObjectiveCriteria>> mCriteria;
};

```
#### ScoreboardCommand::InitProxy
```cpp
/* 426836 */
struct ScoreboardCommand::InitProxy
{
Scoreboard *mScoreboard;
};

```
#### ScoreboardCommand::SetScoreOutput
```cpp
/* 426837 */
struct ScoreboardCommand::SetScoreOutput
{
int mSuccessCount;
int mFirstNewScore;
std::string mFirstSuccess;
};

```
#### ScoreboardId
```cpp
/* 70050 */
struct ScoreboardId
{
int64_t mRawID;
IdentityDefinition *mIdentityDef;
};

```
#### ScoreboardIdentityPacketInfo
```cpp
/* 70103 */
struct ScoreboardIdentityPacketInfo
{
ScoreboardId mScoreboardId;
PlayerScoreboardId mPlayerId;
};

```
#### ScoreboardIdentityRef
```cpp
/* 80250 */
struct ScoreboardIdentityRef
{
uint32_t mObjectiveReferences;
ScoreboardId mScoreboardId;
};

```
#### ScreenshotOptions
```cpp
/* 35042 */
struct ScreenshotOptions
{
bool mCropToRatio;
int mWidthRatio;
int mHeightRatio;
uint32_t mMaxWidth;
uint32_t mMaxHeight;
bool mRestrictScreenshotSize;
bool mApplySquareFrame;
Core::HeapPathBuffer mRequestedFileName;
Core::HeapPathBuffer mRequestedFilePath;
Core::HeapPathBuffer mRequestedExtension;
bool mReplaceImage;
bool mUseScreenshotsFolder;
bool mHideUI;
bool mLogRequest;
bool mWriteScreenshotToFile;
bool mIsSavegameScreenshot;
Core::HeapPathBuffer mOutFileName;
Core::HeapPathBuffer mOutFileDir;
Core::HeapPathBuffer mOutExtension;
};

```
#### ScriptApi::EMPTYObjectHandle
```cpp
/* 95649 */
struct ScriptApi::EMPTYObjectHandle
{
__int8 gap0[1];
};

```
#### ScriptApi::EventTracking
```cpp
/* 95734 */
struct ScriptApi::EventTracking
{
ScriptApi::ScriptObjectHandle mFunctionObject;
};

```
#### ScriptApi::JavaScriptErrorHandler;
```cpp
/* 95279 */
struct ScriptApi::JavaScriptErrorHandler;

```
#### ScriptApi::ScriptCallbackInterface
```cpp
/* 99153 */
struct ScriptApi::ScriptCallbackInterface
{
int (**_vptr$ScriptCallbackInterface)(void);
};

```
#### ScriptApi::ScriptFramework
```cpp
/* 99152 */
struct ScriptApi::ScriptFramework
{
int (**_vptr$ScriptFramework)(void);
std::unique_ptr<ScriptApi::ScriptLanguageInterface> mLanguageInterface;
std::vector<ScriptApi::ScriptSystemInfo> mScriptSystems;
std::unique_ptr<ScriptApi::ScriptReport> mScriptReportQueue;
};

```
#### ScriptApi::ScriptLanguageInterface
```cpp
/* 97714 */
struct ScriptApi::ScriptLanguageInterface
{
int (**_vptr$ScriptLanguageInterface)(void);
};

```
#### ScriptApi::ScriptReport
```cpp
/* 99141 */
struct ScriptApi::ScriptReport
{
std::vector<std::shared_ptr<ScriptApi::ScriptReportItem>> mReportItems;
};

```
#### ScriptApi::ScriptReportItem
```cpp
/* 95269 */
struct ScriptApi::ScriptReportItem
{
std::string mMessage;
ScriptApi::ScriptReportItemType mType;
std::unique_ptr<ScriptApi::JavaScriptErrorHandler> mErrorHandler;
};

```
#### ScriptApi::ScriptVersionInfo
```cpp
/* 99227 */
struct ScriptApi::ScriptVersionInfo
{
int32_t mMajorVersion;
int32_t mMinVerssion;
};

```
#### ScriptApi::WORKAROUNDS::tempActorComponent
```cpp
/* 423896 */
struct ScriptApi::WORKAROUNDS::tempActorComponent
{
ActorUniqueID mID;
};

```
#### ScriptApi::WORKAROUNDS::tempLevelComponent
```cpp
/* 424122 */
struct ScriptApi::WORKAROUNDS::tempLevelComponent
{
__int8 gap0[1];
};

```
#### ScriptBinderComponent
```cpp
/* 96379 */
struct ScriptBinderComponent
{
int (**_vptr$ScriptBinderComponent)(void);
};

```
#### ScriptBinderTemplate
```cpp
/* 95815 */
struct ScriptBinderTemplate
{
int (**_vptr$ScriptBinderTemplate)(void);
};

```
#### ScriptBinderTemplateController
```cpp
/* 98718 */
struct ScriptBinderTemplateController
{
std::unordered_map<std::string,std::unique_ptr<ScriptBinderTemplate>> mTemplates;
};

```
#### ScriptCommandCallbackData
```cpp
/* 95647 */
struct ScriptCommandCallbackData
{
ScriptApi::ScriptObjectHandle mFunction;
std::string mCommand;
bool mCallbackReceived;
Json::Value mData;
};

```
#### ScriptCommandFactory
```cpp
/* 475676 */
struct ScriptCommandFactory
{
__int8 gap0[1];
};

```
#### ScriptEngine::ScriptQueueData
```cpp
/* 99171 */
struct ScriptEngine::ScriptQueueData
{
Core::HeapPathBuffer mScriptPath;
std::string mScriptName;
std::string mScriptContent;
std::string mPackID;
std::string mPackVersion;
uint64_t mScriptHash;
};

```
#### ScriptEngineWithContext<ScriptServerContext>::createEntity::$C3475C4D5343D48D4C7832305B127EAE
```cpp
/* 99880 */
struct ScriptEngineWithContext<ScriptServerContext>::createEntity::$C3475C4D5343D48D4C7832305B127EAE
{
ScriptEngineWithContext<ScriptServerContext> *this;
ScriptApi::ScriptObjectHandle *entityHandle;
const std::string *templateName;
const ScriptApi::ScriptVersionInfo *info;
};

```
#### ScriptEventData
```cpp
/* 96208 */
struct ScriptEventData
{
int (**_vptr$ScriptEventData)(void);
std::string mEventName;
};

```
#### ScriptEventListener
```cpp
/* 97518 */
struct ScriptEventListener
{
int (**_vptr$ScriptEventListener)(void);
};

```
#### ScriptObjectBinder
```cpp
/* 96427 */
struct ScriptObjectBinder
{
const std::string mTypeIdentifier;
unsigned int mComponentsInUse;
std::vector<std::unique_ptr<ScriptBinderComponent>> mComponents;
};

```
#### ScriptOnlyComponents<ScriptServerContext>
```cpp
/* 99148 */
struct ScriptOnlyComponents<ScriptServerContext>
{
std::map<std::string,Json::Value> mScriptOnlyComponentDefs;
};

```
#### ScriptOnlyComponents<ScriptServerContext>::ScriptOnly
```cpp
/* 97603 */
struct ScriptOnlyComponents<ScriptServerContext>::ScriptOnly
{
std::map<std::string,Json::Value> mLookup;
};

```
#### ScriptOnlyEventsData<ScriptServerContext>
```cpp
/* 99149 */
struct ScriptOnlyEventsData<ScriptServerContext>
{
std::map<std::string,Json::Value> mScriptOnlyEventsData;
};

```
#### ScriptQueries
```cpp
/* 99151 */
struct ScriptQueries
{
entt::DefaultRegistry mRegistryView;
};

```
#### ScriptQueryComponent
```cpp
/* 423826 */
struct ScriptQueryComponent
{
std::unordered_set<std::string> mFilters;
ScriptQueryComponent::ViewType mType;
std::string mSpatialTag;
std::string mCoordinateTags[3];
};

```
#### ScriptServerContext
```cpp
/* 99139 */
struct ScriptServerContext
{
Level *mLevel;
Minecraft *mMinecraft;
PacketSender *mPacketSender;
entt::DefaultRegistry *mRegistry;
ScriptApi::ScriptReport *mScriptReport;
};

```
#### ScriptTemplateFactory<ScriptServerContext>
```cpp
/* 99142 */
struct ScriptTemplateFactory<ScriptServerContext>
{
ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::Entity> mEntities;
ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::Entity> mItemEntities;
ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::Component> mComponents;
ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::ReceivedEvent> mReceivedEvents;
ScriptTemplateFactory<ScriptServerContext>::HashedEntries mScriptEventDatas;
ScriptTemplateFactory<ScriptServerContext>::Entry<ScriptTemplateFactory<ScriptServerContext>::ReceivedEvent> mBroadcastEvent;
};

```
#### ScriptTemplateFactory<ScriptServerContext>::Component
```cpp
/* 95456 */
struct ScriptTemplateFactory<ScriptServerContext>::Component
{
int (**_vptr$Component)(void);
};

```
#### ScriptTemplateFactory<ScriptServerContext>::Entity
```cpp
/* 95381 */
struct ScriptTemplateFactory<ScriptServerContext>::Entity
{
int (**_vptr$Entity)(void);
};

```
#### ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::Component>
```cpp
/* 99144 */
struct ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::Component>
{
std::unordered_map<unsigned long,std::shared_ptr<ScriptTemplateFactory<ScriptServerContext>::Component>> mTemplates;
};

```
#### ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::Entity>
```cpp
/* 99143 */
struct ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::Entity>
{
std::unordered_map<unsigned long,std::shared_ptr<ScriptTemplateFactory<ScriptServerContext>::Entity>> mTemplates;
};

```
#### ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::ReceivedEvent>
```cpp
/* 99145 */
struct ScriptTemplateFactory<ScriptServerContext>::Entries<ScriptTemplateFactory<ScriptServerContext>::ReceivedEvent>
{
std::unordered_map<unsigned long,std::shared_ptr<ScriptTemplateFactory<ScriptServerContext>::ReceivedEvent>> mTemplates;
};

```
#### ScriptTemplateFactory<ScriptServerContext>::HashedEntries
```cpp
/* 99146 */
struct ScriptTemplateFactory<ScriptServerContext>::HashedEntries
{
std::unordered_set<unsigned long> mHashes;
};

```
#### ScriptTemplateFactory<ScriptServerContext>::ReceivedEvent
```cpp
/* 95540 */
struct ScriptTemplateFactory<ScriptServerContext>::ReceivedEvent
{
int (**_vptr$ReceivedEvent)(void);
};

```
#### SearchRequestTelemetry;
```cpp
/* 45324 */
struct SearchRequestTelemetry;

```
#### Seasons
```cpp
/* 34400 */
struct Seasons
{
Dimension *mDimension;
PerlinSimplexNoise mSnowNoise;
};

```
#### SeatDescription
```cpp
/* 55146 */
struct SeatDescription
{
Vec3 mPosition;
int mMinSeatCount;
int mMaxSeatCount;
float mSeatRotation;
bool mLockRiderRotation;
float mLockRiderRotationDegrees;
};

```
#### SecureStorage
```cpp
/* 479501 */
struct SecureStorage
{
int (**_vptr$SecureStorage)(void);
};

```
#### SelectorIterator<Actor>
```cpp
/* 90959 */
struct SelectorIterator<Actor>
{
CommandResultVector mTargets;
std::vector<Actor *>::iterator mIndex;
};

```
#### SelectorIterator<Player>
```cpp
/* 33510 */
struct SelectorIterator<Player>
{
CommandResultVector mTargets;
std::vector<Actor *>::iterator mIndex;
};

```
#### SemVersion::any_version_constructor
```cpp
/* 5623 */
struct SemVersion::any_version_constructor
{
__int8 gap0[1];
};

```
#### SendEventData
```cpp
/* 88826 */
struct SendEventData
{
float minActivationRange;
float maxActivationRange;
int cooldownTime;
int castDuration;
float weight;
bool doCastingAnimation;
int particleColor;
ActorFilterGroup targetFilter;
LevelSoundEvent startSound;
std::vector<SendEventStage> stages;
};

```
#### SensingComponent
```cpp
/* 58948 */
struct SensingComponent
{
SensingComponent::ActorSet mSeen;
SensingComponent::ActorSet mUnseen;
};

```
#### SerializedPersonaPieceHandle
```cpp
/* 74272 */
struct SerializedPersonaPieceHandle
{
std::string mPieceId;
persona::PieceType mPieceType;
mce::UUID mPackId;
bool mIsDefaultPiece;
std::string mProductId;
};

```
#### SerializedSkin
```cpp
/* 74239 */
struct SerializedSkin
{
std::string mId;
std::string fullId;
std::string mResourcePatch;
std::string mDefaultGeometryName;
mce::Image mSkinImage;
mce::Image mCapeImage;
std::vector<AnimatedImageData> mSkinAnimatedImages;
Json::Value mGeometryData;
Json::Value mGeometryDataMutable;
std::string mAnimationData;
std::string mCapeId;
bool mIsPremium;
bool mIsPersona;
bool mIsPersonaCapeOnClassicSkin;
TrustedSkinFlag mIsTrustedSkin;
std::vector<SerializedPersonaPieceHandle> mPersonaPieces;
std::string mArmSize;
std::unordered_map<persona::PieceType,TintMapColor> mPieceTintColors;
Color mSkinColor;
};

```
#### SerializedSkin_0
```cpp
/* 173180 */
struct SerializedSkin_0
{
std::string mId;
std::string fullId;
std::string mResourcePatch;
std::string mDefaultGeometryName;
mce::Image_0 mSkinImage;
mce::Image_0 mCapeImage;
std::vector<AnimatedImageData>_0 mSkinAnimatedImages;
Json::Value mGeometryData;
Json::Value mGeometryDataMutable;
std::string mAnimationData;
std::string mCapeId;
bool mIsPremium;
bool mIsPersona;
bool mIsPersonaCapeOnClassicSkin;
TrustedSkinFlag mIsTrustedSkin;
std::vector<SerializedPersonaPieceHandle> mPersonaPieces;
std::string mArmSize;
std::unordered_map<persona::PieceType,TintMapColor> mPieceTintColors;
Color mSkinColor;
};

```
#### ServerCommunicationInterface
```cpp
/* 4257 */
struct ServerCommunicationInterface
{
std::unique_ptr<RakNet::TCPInterface> mTCPConnection;
RakNet::SystemAddress mHostAddress;
};

```
#### ServerInstance::initializeServer::$1AF53268373D8F94D8C5F1843C50C698
```cpp
/* 87054 */
struct ServerInstance::initializeServer::$1AF53268373D8F94D8C5F1843C50C698
{
std::unordered_map<PackIdVersion,std::string> *packIdToContentKey;
ResourcePackRepository *resourcePackRepository;
};

```
#### ServerLocator
```cpp
/* 63710 */
struct ServerLocator
{
int (**_vptr$ServerLocator)(void);
};

```
#### ServerMetrics
```cpp
/* 8550 */
struct ServerMetrics
{
int (**_vptr$ServerMetrics)(void);
};

```
#### ServerMetricsImpl::DataTransferred
```cpp
/* 8105 */
struct ServerMetricsImpl::DataTransferred
{
uint64_t totalBytesReceived;
uint64_t totalBytesSent;
};

```
#### ServerNetworkHandler::Client
```cpp
/* 73788 */
struct ServerNetworkHandler::Client
{
std::unique_ptr<ConnectionRequest> mPrimaryRequest;
std::unordered_map<unsigned char,std::unique_ptr<SubClientConnectionRequest>> mSubClientRequests;
};

```
#### ServerNetworkHandler::_getActiveAndInProgressPlayerCount::$0EBB06E09BB4D485483DF06B22BB4AE5
```cpp
/* 77491 */
struct ServerNetworkHandler::_getActiveAndInProgressPlayerCount::$0EBB06E09BB4D485483DF06B22BB4AE5
{
const ServerNetworkHandler *this;
mce::UUID *excludePlayer;
int *numPlayers;
};

```
#### ServerNetworkHandler::_onClientAuthenticated::$40782884DF021EB8A0B68AECF65B4504
```cpp
/* 77489 */
struct ServerNetworkHandler::_onClientAuthenticated::$40782884DF021EB8A0B68AECF65B4504
{
ServerNetworkHandler *this;
};

```
#### ServerNetworkHandler::handle::$3CDCE61CA261A057C80CC046802E365C
```cpp
/* 77437 */
struct ServerNetworkHandler::handle::$3CDCE61CA261A057C80CC046802E365C
{
ServerNetworkHandler *this;
const NetworkIdentifier *source;
std::set<std::string> *downloading;
};

```
#### ServerNetworkHandler::handle::$ED428D87CD11B947B517AB43C0D6E540
```cpp
/* 76956 */
struct ServerNetworkHandler::handle::$ED428D87CD11B947B517AB43C0D6E540
{
ServerNetworkHandler *this;
const NetworkIdentifier source;
};

```
#### ServerPlayer::NearbyActor
```cpp
/* 89356 */
struct ServerPlayer::NearbyActor
{
bool isAutonomous;
ServerPlayer::NearbyActor::State state;
Actor *tempActor;
};

```
#### ServerPlayer::recoverR5LostInventoryAndXP::$566869B8F3A3697DD8479CC05753D205
```cpp
/* 90647 */
struct ServerPlayer::recoverR5LostInventoryAndXP::$566869B8F3A3697DD8479CC05753D205
{
std::vector<BlockPos> chestPositions;
};

```
#### ServerScoreboard::unit_test_ctor_t
```cpp
/* 294173 */
struct ServerScoreboard::unit_test_ctor_t
{
__int8 gap0[1];
};

```
#### ServiceLocator<AppConfigs>
```cpp
/* 5585 */
struct ServiceLocator<AppConfigs>
{
__int8 gap0[1];
};

```
#### ServiceLocator<AppPlatform>
```cpp
/* 5584 */
struct ServiceLocator<AppPlatform>
{
__int8 gap0[1];
};

```
#### ServiceLocator<ContentLog>
```cpp
/* 5586 */
struct ServiceLocator<ContentLog>
{
__int8 gap0[1];
};

```
#### ServiceLocator<Core::LoadTimeProfiler>
```cpp
/* 480120 */
struct ServiceLocator<Core::LoadTimeProfiler>
{
__int8 gap0[1];
};

```
#### ServiceLocator<EducationOptions>
```cpp
/* 81171 */
struct ServiceLocator<EducationOptions>
{
__int8 gap0[1];
};

```
#### ServiceLocator<FeatureToggles>
```cpp
/* 77439 */
struct ServiceLocator<FeatureToggles>
{
__int8 gap0[1];
};

```
#### ServiceLocator<IMinecraftEventing>
```cpp
/* 45361 */
struct ServiceLocator<IMinecraftEventing>
{
__int8 gap0[1];
};

```
#### ServiceLocator<NetworkDebugManager>
```cpp
/* 64308 */
struct ServiceLocator<NetworkDebugManager>
{
__int8 gap0[1];
};

```
#### ServiceLocator<PackManifest::CapabilityRegistry>
```cpp
/* 82679 */
struct ServiceLocator<PackManifest::CapabilityRegistry>
{
__int8 gap0[1];
};

```
#### ServiceLocator<ServerInstance>
```cpp
/* 87055 */
struct ServiceLocator<ServerInstance>
{
__int8 gap0[1];
};

```
#### ServiceOverrider<bool (*)(const char *,const char *,const char *,bool,int,const char *,const char *,bool)>
```cpp
/* 480590 */
struct ServiceOverrider<bool (*)(const char *,const char *,const char *,bool,int,const char *,const char *,bool)>
{
ThreadLocal<bool (**)(const char *,const char *,const char *,bool,int,const char *,const char *,bool)> mService;
bool (**mDefaultService)(const char *, const char *, const char *, bool, int, const char *, const char *, bool);
};

```
#### SharePtrRefTraits<PerlinSimplexNoise>
```cpp
/* 191523 */
struct SharePtrRefTraits<PerlinSimplexNoise>
{
__int8 gap0[1];
};

```
#### Shareable
```cpp
/* 417212 */
struct Shareable
{
int itemId;
int itemAux;
int wantAmount;
int surplusAmount;
int maxAmount;
int craftIntoItem;
int craftIntoItemAux;
int itemPriority;
};

```
#### ShareableDefinition
```cpp
/* 116674 */
struct ShareableDefinition
{
std::vector<Shareable> mItems;
bool mShareAllItems;
int mAllItemWantAmount;
int mAllItemSurplusAmount;
int mAllItemMaxAmount;
};

```
#### SharedAmplifiers
```cpp
/* 174643 */
struct SharedAmplifiers
{
__int8 gap0[1];
};

```
#### SharedAttributes
```cpp
/* 174606 */
struct SharedAttributes
{
__int8 gap0[1];
};

```
#### SharedBuffs
```cpp
/* 174644 */
struct SharedBuffs
{
__int8 gap0[1];
};

```
#### SharedCounter<ActivatorRailBlock>
```cpp
/* 251389 */
struct SharedCounter<ActivatorRailBlock>
{
ActivatorRailBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<AirBlock>
```cpp
/* 250879 */
struct SharedCounter<AirBlock>
{
AirBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<AirBlockItem>
```cpp
/* 180756 */
struct SharedCounter<AirBlockItem>
{
AirBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<AnvilBlock>
```cpp
/* 251440 */
struct SharedCounter<AnvilBlock>
{
AnvilBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ArmorItem>
```cpp
/* 183817 */
struct SharedCounter<ArmorItem>
{
ArmorItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ArmorStandItem>
```cpp
/* 183950 */
struct SharedCounter<ArmorStandItem>
{
ArmorStandItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ArrowItem>
```cpp
/* 183797 */
struct SharedCounter<ArrowItem>
{
ArrowItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<AuxDataBlockItem>
```cpp
/* 184012 */
struct SharedCounter<AuxDataBlockItem>
{
AuxDataBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BalloonItem>
```cpp
/* 183996 */
struct SharedCounter<BalloonItem>
{
BalloonItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BambooBlock>
```cpp
/* 251696 */
struct SharedCounter<BambooBlock>
{
BambooBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BambooBlockItem>
```cpp
/* 184057 */
struct SharedCounter<BambooBlockItem>
{
BambooBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BambooSapling>
```cpp
/* 251700 */
struct SharedCounter<BambooSapling>
{
BambooSapling *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BannerBlock>
```cpp
/* 251511 */
struct SharedCounter<BannerBlock>
{
BannerBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BannerItem>
```cpp
/* 183965 */
struct SharedCounter<BannerItem>
{
BannerItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BannerPatternItem>
```cpp
/* 183973 */
struct SharedCounter<BannerPatternItem>
{
BannerPatternItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BarrelBlock>
```cpp
/* 251731 */
struct SharedCounter<BarrelBlock>
{
BarrelBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BarrierBlock>
```cpp
/* 251688 */
struct SharedCounter<BarrierBlock>
{
BarrierBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BeaconBlock>
```cpp
/* 251412 */
struct SharedCounter<BeaconBlock>
{
BeaconBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BedBlock>
```cpp
/* 251128 */
struct SharedCounter<BedBlock>
{
BedBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BedItem>
```cpp
/* 183876 */
struct SharedCounter<BedItem>
{
BedItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BedrockBlock>
```cpp
/* 251076 */
struct SharedCounter<BedrockBlock>
{
BedrockBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BeehiveBlock>
```cpp
/* 251774 */
struct SharedCounter<BeehiveBlock>
{
BeehiveBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BeetrootBlock>
```cpp
/* 251591 */
struct SharedCounter<BeetrootBlock>
{
BeetrootBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BellBlock>
```cpp
/* 251739 */
struct SharedCounter<BellBlock>
{
BellBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BellBlockItem>
```cpp
/* 184065 */
struct SharedCounter<BellBlockItem>
{
BellBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BlastFurnaceBlock>
```cpp
/* 251719 */
struct SharedCounter<BlastFurnaceBlock>
{
BlastFurnaceBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BlockItem>
```cpp
/* 182765 */
struct SharedCounter<BlockItem>
{
BlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BlockLegacy>
```cpp
/* 13208 */
struct SharedCounter<BlockLegacy>
{
BlockLegacy *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BlockPlanterItem>
```cpp
/* 183809 */
struct SharedCounter<BlockPlanterItem>
{
BlockPlanterItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BlueIceBlock>
```cpp
/* 251619 */
struct SharedCounter<BlueIceBlock>
{
BlueIceBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BoatItem>
```cpp
/* 183851 */
struct SharedCounter<BoatItem>
{
BoatItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BookshelfBlock>
```cpp
/* 251181 */
struct SharedCounter<BookshelfBlock>
{
BookshelfBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BottleItem>
```cpp
/* 183894 */
struct SharedCounter<BottleItem>
{
BottleItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BowItem>
```cpp
/* 183793 */
struct SharedCounter<BowItem>
{
BowItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BrewingStandBlock>
```cpp
/* 251362 */
struct SharedCounter<BrewingStandBlock>
{
BrewingStandBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BubbleColumnBlock>
```cpp
/* 251680 */
struct SharedCounter<BubbleColumnBlock>
{
BubbleColumnBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<BucketItem>
```cpp
/* 183835 */
struct SharedCounter<BucketItem>
{
BucketItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CactusBlock>
```cpp
/* 251267 */
struct SharedCounter<CactusBlock>
{
CactusBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CakeBlock>
```cpp
/* 251302 */
struct SharedCounter<CakeBlock>
{
CakeBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CameraBlock>
```cpp
/* 251583 */
struct SharedCounter<CameraBlock>
{
CameraBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CameraItem>
```cpp
/* 183979 */
struct SharedCounter<CameraItem>
{
CameraItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CampfireBlock>
```cpp
/* 251751 */
struct SharedCounter<CampfireBlock>
{
CampfireBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CarrotBlock>
```cpp
/* 251424 */
struct SharedCounter<CarrotBlock>
{
CarrotBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CarrotOnAStickItem>
```cpp
/* 183928 */
struct SharedCounter<CarrotOnAStickItem>
{
CarrotOnAStickItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CartographyTableBlock>
```cpp
/* 251727 */
struct SharedCounter<CartographyTableBlock>
{
CartographyTableBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CauldronBlock>
```cpp
/* 251366 */
struct SharedCounter<CauldronBlock>
{
CauldronBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ChemicalHeatBlock>
```cpp
/* 251633 */
struct SharedCounter<ChemicalHeatBlock>
{
ChemicalHeatBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ChemistryAuxDataBlockItem>
```cpp
/* 184069 */
struct SharedCounter<ChemistryAuxDataBlockItem>
{
ChemistryAuxDataBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ChemistryItem>
```cpp
/* 183990 */
struct SharedCounter<ChemistryItem>
{
ChemistryItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ChemistryTableBlock>
```cpp
/* 251626 */
struct SharedCounter<ChemistryTableBlock>
{
ChemistryTableBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ChestBlock>
```cpp
/* 251200 */
struct SharedCounter<ChestBlock>
{
ChestBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ChorusFlowerBlock>
```cpp
/* 251527 */
struct SharedCounter<ChorusFlowerBlock>
{
ChorusFlowerBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ChorusPlantBlock>
```cpp
/* 251575 */
struct SharedCounter<ChorusPlantBlock>
{
ChorusPlantBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ClayBlock>
```cpp
/* 251271 */
struct SharedCounter<ClayBlock>
{
ClayBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ClockItem>
```cpp
/* 183870 */
struct SharedCounter<ClockItem>
{
ClockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ClothBlock>
```cpp
/* 251158 */
struct SharedCounter<ClothBlock>
{
ClothBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ClothBlockItem>
```cpp
/* 184016 */
struct SharedCounter<ClothBlockItem>
{
ClothBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CoalItem>
```cpp
/* 183801 */
struct SharedCounter<CoalItem>
{
CoalItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CocoaBlock>
```cpp
/* 251393 */
struct SharedCounter<CocoaBlock>
{
CocoaBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ColoredBlock>
```cpp
/* 251471 */
struct SharedCounter<ColoredBlock>
{
ColoredBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ColoredTorchBlock>
```cpp
/* 251637 */
struct SharedCounter<ColoredTorchBlock>
{
ColoredTorchBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CommandBlock>
```cpp
/* 251409 */
struct SharedCounter<CommandBlock>
{
CommandBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ComparatorBlock>
```cpp
/* 251448 */
struct SharedCounter<ComparatorBlock>
{
ComparatorBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CompassItem>
```cpp
/* 183863 */
struct SharedCounter<CompassItem>
{
CompassItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ComposterBlock>
```cpp
/* 251763 */
struct SharedCounter<ComposterBlock>
{
ComposterBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CompoundItem>
```cpp
/* 183983 */
struct SharedCounter<CompoundItem>
{
CompoundItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ConcreteBlock>
```cpp
/* 251567 */
struct SharedCounter<ConcreteBlock>
{
ConcreteBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ConcretePowderBlock>
```cpp
/* 251571 */
struct SharedCounter<ConcretePowderBlock>
{
ConcretePowderBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ConduitBlock>
```cpp
/* 251676 */
struct SharedCounter<ConduitBlock>
{
ConduitBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<Coral>
```cpp
/* 251644 */
struct SharedCounter<Coral>
{
Coral *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CoralBlock>
```cpp
/* 251648 */
struct SharedCounter<CoralBlock>
{
CoralBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CoralFan>
```cpp
/* 251652 */
struct SharedCounter<CoralFan>
{
CoralFan *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CoralFanBlockItem>
```cpp
/* 184025 */
struct SharedCounter<CoralFanBlockItem>
{
CoralFanBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CoralFanHang>
```cpp
/* 251656 */
struct SharedCounter<CoralFanHang>
{
CoralFanHang *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CropBlock>
```cpp
/* 251211 */
struct SharedCounter<CropBlock>
{
CropBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<CrossbowItem>
```cpp
/* 183969 */
struct SharedCounter<CrossbowItem>
{
CrossbowItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DaylightDetectorBlock>
```cpp
/* 251452 */
struct SharedCounter<DaylightDetectorBlock>
{
DaylightDetectorBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DeadBush>
```cpp
/* 251150 */
struct SharedCounter<DeadBush>
{
DeadBush *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DetectorRailBlock>
```cpp
/* 251135 */
struct SharedCounter<DetectorRailBlock>
{
DetectorRailBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DirtBlock>
```cpp
/* 251064 */
struct SharedCounter<DirtBlock>
{
DirtBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DispenserBlock>
```cpp
/* 251116 */
struct SharedCounter<DispenserBlock>
{
DispenserBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DoorBlock>
```cpp
/* 251226 */
struct SharedCounter<DoorBlock>
{
DoorBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DoorItem>
```cpp
/* 183831 */
struct SharedCounter<DoorItem>
{
DoorItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DoublePlantBlock>
```cpp
/* 251507 */
struct SharedCounter<DoublePlantBlock>
{
DoublePlantBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DragonEggBlock>
```cpp
/* 251377 */
struct SharedCounter<DragonEggBlock>
{
DragonEggBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DriedKelpBlock>
```cpp
/* 251664 */
struct SharedCounter<DriedKelpBlock>
{
DriedKelpBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DropperBlock>
```cpp
/* 251385 */
struct SharedCounter<DropperBlock>
{
DropperBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<DyePowderItem>
```cpp
/* 183873 */
struct SharedCounter<DyePowderItem>
{
DyePowderItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EggItem>
```cpp
/* 183859 */
struct SharedCounter<EggItem>
{
EggItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ElementBlock>
```cpp
/* 251641 */
struct SharedCounter<ElementBlock>
{
ElementBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ElementBlockItem>
```cpp
/* 184073 */
struct SharedCounter<ElementBlockItem>
{
ElementBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EmptyMapItem>
```cpp
/* 183921 */
struct SharedCounter<EmptyMapItem>
{
EmptyMapItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EnchantedBookItem>
```cpp
/* 183855 */
struct SharedCounter<EnchantedBookItem>
{
EnchantedBookItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EnchantingTableBlock>
```cpp
/* 251358 */
struct SharedCounter<EnchantingTableBlock>
{
EnchantingTableBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EndCrystalItem>
```cpp
/* 183954 */
struct SharedCounter<EndCrystalItem>
{
EndCrystalItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EndGatewayBlock>
```cpp
/* 251543 */
struct SharedCounter<EndGatewayBlock>
{
EndGatewayBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EndPortalBlock>
```cpp
/* 251369 */
struct SharedCounter<EndPortalBlock>
{
EndPortalBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EndPortalFrameBlock>
```cpp
/* 251373 */
struct SharedCounter<EndPortalFrameBlock>
{
EndPortalFrameBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EndRodBlock>
```cpp
/* 251539 */
struct SharedCounter<EndRodBlock>
{
EndRodBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EnderChestBlock>
```cpp
/* 251397 */
struct SharedCounter<EnderChestBlock>
{
EnderChestBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EnderEyeItem>
```cpp
/* 183898 */
struct SharedCounter<EnderEyeItem>
{
EnderEyeItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<EnderpearlItem>
```cpp
/* 183887 */
struct SharedCounter<EnderpearlItem>
{
EnderpearlItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ExperiencePotionItem>
```cpp
/* 183905 */
struct SharedCounter<ExperiencePotionItem>
{
ExperiencePotionItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FarmBlock>
```cpp
/* 251215 */
struct SharedCounter<FarmBlock>
{
FarmBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FenceBlock>
```cpp
/* 251283 */
struct SharedCounter<FenceBlock>
{
FenceBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FenceGateBlock>
```cpp
/* 251342 */
struct SharedCounter<FenceGateBlock>
{
FenceGateBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FireBlock>
```cpp
/* 251623 */
struct SharedCounter<FireBlock>
{
FireBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FireChargeItem>
```cpp
/* 183909 */
struct SharedCounter<FireChargeItem>
{
FireChargeItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FireworkChargeItem>
```cpp
/* 183935 */
struct SharedCounter<FireworkChargeItem>
{
FireworkChargeItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FireworksItem>
```cpp
/* 183932 */
struct SharedCounter<FireworksItem>
{
FireworksItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FishingRodItem>
```cpp
/* 183866 */
struct SharedCounter<FishingRodItem>
{
FishingRodItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FlintAndSteelItem>
```cpp
/* 183789 */
struct SharedCounter<FlintAndSteelItem>
{
FlintAndSteelItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FlowerBlock>
```cpp
/* 251162 */
struct SharedCounter<FlowerBlock>
{
FlowerBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FlowerPotBlock>
```cpp
/* 251420 */
struct SharedCounter<FlowerPotBlock>
{
FlowerPotBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FrostedIceBlock>
```cpp
/* 251535 */
struct SharedCounter<FrostedIceBlock>
{
FrostedIceBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<FurnaceBlock>
```cpp
/* 251218 */
struct SharedCounter<FurnaceBlock>
{
FurnaceBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<GlassBlock>
```cpp
/* 251112 */
struct SharedCounter<GlassBlock>
{
GlassBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<GlazedTerracottaBlock>
```cpp
/* 251563 */
struct SharedCounter<GlazedTerracottaBlock>
{
GlazedTerracottaBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<GlowStickItem>
```cpp
/* 184008 */
struct SharedCounter<GlowStickItem>
{
GlowStickItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<GrassBlock>
```cpp
/* 251060 */
struct SharedCounter<GrassBlock>
{
GrassBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<GrassPathBlock>
```cpp
/* 251519 */
struct SharedCounter<GrassPathBlock>
{
GrassPathBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<GravelBlock>
```cpp
/* 251092 */
struct SharedCounter<GravelBlock>
{
GravelBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<GrindstoneBlock>
```cpp
/* 251715 */
struct SharedCounter<GrindstoneBlock>
{
GrindstoneBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HangingActorItem>
```cpp
/* 183823 */
struct SharedCounter<HangingActorItem>
{
HangingActorItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HatchetItem>
```cpp
/* 183785 */
struct SharedCounter<HatchetItem>
{
HatchetItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HayBlockBlock>
```cpp
/* 251499 */
struct SharedCounter<HayBlockBlock>
{
HayBlockBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HoeItem>
```cpp
/* 183813 */
struct SharedCounter<HoeItem>
{
HoeItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HoneyBlock>
```cpp
/* 251777 */
struct SharedCounter<HoneyBlock>
{
HoneyBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HoneycombBlock>
```cpp
/* 251781 */
struct SharedCounter<HoneycombBlock>
{
HoneycombBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HopperBlock>
```cpp
/* 251459 */
struct SharedCounter<HopperBlock>
{
HopperBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HorseArmorItem>
```cpp
/* 183938 */
struct SharedCounter<HorseArmorItem>
{
HorseArmorItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<HugeMushroomBlock>
```cpp
/* 251323 */
struct SharedCounter<HugeMushroomBlock>
{
HugeMushroomBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<IceBlock>
```cpp
/* 251259 */
struct SharedCounter<IceBlock>
{
IceBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<IceBombItem>
```cpp
/* 183986 */
struct SharedCounter<IceBombItem>
{
IceBombItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<InvisibleBlock>
```cpp
/* 251308 */
struct SharedCounter<InvisibleBlock>
{
InvisibleBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<Item>
```cpp
/* 13202 */
struct SharedCounter<Item>
{
Item *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ItemFrameBlock>
```cpp
/* 251523 */
struct SharedCounter<ItemFrameBlock>
{
ItemFrameBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<JigsawBlock>
```cpp
/* 251755 */
struct SharedCounter<JigsawBlock>
{
JigsawBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<JukeboxBlock>
```cpp
/* 251279 */
struct SharedCounter<JukeboxBlock>
{
JukeboxBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<KelpBlock>
```cpp
/* 251660 */
struct SharedCounter<KelpBlock>
{
KelpBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LadderBlock>
```cpp
/* 251229 */
struct SharedCounter<LadderBlock>
{
LadderBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LanternBlock>
```cpp
/* 251747 */
struct SharedCounter<LanternBlock>
{
LanternBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LeadItem>
```cpp
/* 183947 */
struct SharedCounter<LeadItem>
{
LeadItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LeafBlockItem>
```cpp
/* 184037 */
struct SharedCounter<LeafBlockItem>
{
LeafBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LecternBlock>
```cpp
/* 251712 */
struct SharedCounter<LecternBlock>
{
LecternBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LeverBlock>
```cpp
/* 251237 */
struct SharedCounter<LeverBlock>
{
LeverBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LightBlock>
```cpp
/* 251766 */
struct SharedCounter<LightBlock>
{
LightBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LightGemBlock>
```cpp
/* 251295 */
struct SharedCounter<LightGemBlock>
{
LightGemBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LingeringPotionItem>
```cpp
/* 183961 */
struct SharedCounter<LingeringPotionItem>
{
LingeringPotionItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LiquidBlockDynamic>
```cpp
/* 251080 */
struct SharedCounter<LiquidBlockDynamic>
{
LiquidBlockDynamic *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LiquidBlockStatic>
```cpp
/* 251084 */
struct SharedCounter<LiquidBlockStatic>
{
LiquidBlockStatic *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<LoomBlock>
```cpp
/* 251735 */
struct SharedCounter<LoomBlock>
{
LoomBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MagmaBlock>
```cpp
/* 251547 */
struct SharedCounter<MagmaBlock>
{
MagmaBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MapItem>
```cpp
/* 183880 */
struct SharedCounter<MapItem>
{
MapItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MedicineItem>
```cpp
/* 184000 */
struct SharedCounter<MedicineItem>
{
MedicineItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MelonBlock>
```cpp
/* 251330 */
struct SharedCounter<MelonBlock>
{
MelonBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MetalBlock>
```cpp
/* 251169 */
struct SharedCounter<MetalBlock>
{
MetalBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MinecartItem>
```cpp
/* 183839 */
struct SharedCounter<MinecartItem>
{
MinecartItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MobPlacerItem>
```cpp
/* 183902 */
struct SharedCounter<MobPlacerItem>
{
MobPlacerItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MobSpawnerBlock>
```cpp
/* 251193 */
struct SharedCounter<MobSpawnerBlock>
{
MobSpawnerBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MonsterEggBlock>
```cpp
/* 251316 */
struct SharedCounter<MonsterEggBlock>
{
MonsterEggBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MovingBlock>
```cpp
/* 251603 */
struct SharedCounter<MovingBlock>
{
MovingBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MushroomBlock>
```cpp
/* 251165 */
struct SharedCounter<MushroomBlock>
{
MushroomBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<MyceliumBlock>
```cpp
/* 251346 */
struct SharedCounter<MyceliumBlock>
{
MyceliumBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<NetherReactorBlock>
```cpp
/* 251599 */
struct SharedCounter<NetherReactorBlock>
{
NetherReactorBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<NetherWartBlock>
```cpp
/* 251354 */
struct SharedCounter<NetherWartBlock>
{
NetherWartBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<NewLeafBlock>
```cpp
/* 251479 */
struct SharedCounter<NewLeafBlock>
{
NewLeafBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<NewLogBlock>
```cpp
/* 251483 */
struct SharedCounter<NewLogBlock>
{
NewLogBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<NoteBlock>
```cpp
/* 251124 */
struct SharedCounter<NoteBlock>
{
NoteBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ObserverBlock>
```cpp
/* 251607 */
struct SharedCounter<ObserverBlock>
{
ObserverBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ObsidianBlock>
```cpp
/* 251185 */
struct SharedCounter<ObsidianBlock>
{
ObsidianBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<OldLeafBlock>
```cpp
/* 251104 */
struct SharedCounter<OldLeafBlock>
{
OldLeafBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<OldLogBlock>
```cpp
/* 251100 */
struct SharedCounter<OldLogBlock>
{
OldLogBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<OreBlock>
```cpp
/* 251096 */
struct SharedCounter<OreBlock>
{
OreBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PickaxeItem>
```cpp
/* 183781 */
struct SharedCounter<PickaxeItem>
{
PickaxeItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PistonArmBlock>
```cpp
/* 251154 */
struct SharedCounter<PistonArmBlock>
{
PistonArmBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PistonBlock>
```cpp
/* 251139 */
struct SharedCounter<PistonBlock>
{
PistonBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PlanksBlock>
```cpp
/* 251068 */
struct SharedCounter<PlanksBlock>
{
PlanksBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PodzolBlock>
```cpp
/* 251587 */
struct SharedCounter<PodzolBlock>
{
PodzolBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PortalBlock>
```cpp
/* 251299 */
struct SharedCounter<PortalBlock>
{
PortalBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PotatoBlock>
```cpp
/* 251428 */
struct SharedCounter<PotatoBlock>
{
PotatoBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PotionItem>
```cpp
/* 183891 */
struct SharedCounter<PotionItem>
{
PotionItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PoweredRailBlock>
```cpp
/* 251131 */
struct SharedCounter<PoweredRailBlock>
{
PoweredRailBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PressurePlateBlock>
```cpp
/* 251241 */
struct SharedCounter<PressurePlateBlock>
{
PressurePlateBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PrismarineBlock>
```cpp
/* 251491 */
struct SharedCounter<PrismarineBlock>
{
PrismarineBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<PumpkinBlock>
```cpp
/* 251287 */
struct SharedCounter<PumpkinBlock>
{
PumpkinBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<QuartzBlockBlock>
```cpp
/* 251463 */
struct SharedCounter<QuartzBlockBlock>
{
QuartzBlockBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RailBlock>
```cpp
/* 251233 */
struct SharedCounter<RailBlock>
{
RailBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RapidFertilizerItem>
```cpp
/* 183993 */
struct SharedCounter<RapidFertilizerItem>
{
RapidFertilizerItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RecordItem>
```cpp
/* 183941 */
struct SharedCounter<RecordItem>
{
RecordItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RedStoneDustItem>
```cpp
/* 183843 */
struct SharedCounter<RedStoneDustItem>
{
RedStoneDustItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RedStoneOreBlock>
```cpp
/* 251244 */
struct SharedCounter<RedStoneOreBlock>
{
RedStoneOreBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RedStoneWireBlock>
```cpp
/* 251203 */
struct SharedCounter<RedStoneWireBlock>
{
RedStoneWireBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RedstoneBlock>
```cpp
/* 251455 */
struct SharedCounter<RedstoneBlock>
{
RedstoneBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RedstoneLampBlock>
```cpp
/* 251381 */
struct SharedCounter<RedstoneLampBlock>
{
RedstoneLampBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RedstoneTorchBlock>
```cpp
/* 251248 */
struct SharedCounter<RedstoneTorchBlock>
{
RedstoneTorchBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ReedBlock>
```cpp
/* 251275 */
struct SharedCounter<ReedBlock>
{
ReedBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RepeaterBlock>
```cpp
/* 251305 */
struct SharedCounter<RepeaterBlock>
{
RepeaterBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<RotatedPillarBlock>
```cpp
/* 251551 */
struct SharedCounter<RotatedPillarBlock>
{
RotatedPillarBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SandBlock>
```cpp
/* 251088 */
struct SharedCounter<SandBlock>
{
SandBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SandStoneBlock>
```cpp
/* 251120 */
struct SharedCounter<SandStoneBlock>
{
SandStoneBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<Sapling>
```cpp
/* 251072 */
struct SharedCounter<Sapling>
{
Sapling *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SaplingBlockItem>
```cpp
/* 184033 */
struct SharedCounter<SaplingBlockItem>
{
SaplingBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ScaffoldingBlock>
```cpp
/* 251692 */
struct SharedCounter<ScaffoldingBlock>
{
ScaffoldingBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ScaffoldingBlockItem>
```cpp
/* 184061 */
struct SharedCounter<ScaffoldingBlockItem>
{
ScaffoldingBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SeaGrass>
```cpp
/* 251668 */
struct SharedCounter<SeaGrass>
{
SeaGrass *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SeaLanternBlock>
```cpp
/* 251495 */
struct SharedCounter<SeaLanternBlock>
{
SeaLanternBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SeaPickle>
```cpp
/* 251672 */
struct SharedCounter<SeaPickle>
{
SeaPickle *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SeaPickleBlockItem>
```cpp
/* 184029 */
struct SharedCounter<SeaPickleBlockItem>
{
SeaPickleBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ShearsItem>
```cpp
/* 183883 */
struct SharedCounter<ShearsItem>
{
ShearsItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ShieldItem>
```cpp
/* 183820 */
struct SharedCounter<ShieldItem>
{
ShieldItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ShovelItem>
```cpp
/* 183777 */
struct SharedCounter<ShovelItem>
{
ShovelItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ShulkerBoxBlock>
```cpp
/* 251559 */
struct SharedCounter<ShulkerBoxBlock>
{
ShulkerBoxBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ShulkerBoxBlockItem>
```cpp
/* 184053 */
struct SharedCounter<ShulkerBoxBlockItem>
{
ShulkerBoxBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SignBlock>
```cpp
/* 251222 */
struct SharedCounter<SignBlock>
{
SignBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SignItem>
```cpp
/* 183827 */
struct SharedCounter<SignItem>
{
SignItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SkullBlock>
```cpp
/* 251436 */
struct SharedCounter<SkullBlock>
{
SkullBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SkullItem>
```cpp
/* 183924 */
struct SharedCounter<SkullItem>
{
SkullItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SlimeBlock>
```cpp
/* 251487 */
struct SharedCounter<SlimeBlock>
{
SlimeBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SmokerBlock>
```cpp
/* 251723 */
struct SharedCounter<SmokerBlock>
{
SmokerBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SnowBlock>
```cpp
/* 251263 */
struct SharedCounter<SnowBlock>
{
SnowBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SnowballItem>
```cpp
/* 183847 */
struct SharedCounter<SnowballItem>
{
SnowballItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SoulSandBlock>
```cpp
/* 251291 */
struct SharedCounter<SoulSandBlock>
{
SoulSandBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SparklerItem>
```cpp
/* 184004 */
struct SharedCounter<SparklerItem>
{
SparklerItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SplashPotionItem>
```cpp
/* 183958 */
struct SharedCounter<SplashPotionItem>
{
SplashPotionItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SpongeBlock>
```cpp
/* 251108 */
struct SharedCounter<SpongeBlock>
{
SpongeBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StainedGlassBlock>
```cpp
/* 251579 */
struct SharedCounter<StainedGlassBlock>
{
StainedGlassBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StainedGlassPaneBlock>
```cpp
/* 251475 */
struct SharedCounter<StainedGlassPaneBlock>
{
StainedGlassPaneBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StairBlock>
```cpp
/* 251197 */
struct SharedCounter<StairBlock>
{
StairBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StemBlock>
```cpp
/* 251334 */
struct SharedCounter<StemBlock>
{
StemBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StoneBlock>
```cpp
/* 251056 */
struct SharedCounter<StoneBlock>
{
StoneBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StoneBrickBlock>
```cpp
/* 251319 */
struct SharedCounter<StoneBrickBlock>
{
StoneBrickBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StoneButtonBlock>
```cpp
/* 251252 */
struct SharedCounter<StoneButtonBlock>
{
StoneButtonBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StoneSlabBlock2>
```cpp
/* 251515 */
struct SharedCounter<StoneSlabBlock2>
{
StoneSlabBlock2 *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StoneSlabBlock3>
```cpp
/* 251704 */
struct SharedCounter<StoneSlabBlock3>
{
StoneSlabBlock3 *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StoneSlabBlock4>
```cpp
/* 251708 */
struct SharedCounter<StoneSlabBlock4>
{
StoneSlabBlock4 *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StoneSlabBlock>
```cpp
/* 251173 */
struct SharedCounter<StoneSlabBlock>
{
StoneSlabBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StoneSlabBlockItem>
```cpp
/* 184020 */
struct SharedCounter<StoneSlabBlockItem>
{
StoneSlabBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StonecutterBlock>
```cpp
/* 251595 */
struct SharedCounter<StonecutterBlock>
{
StonecutterBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StrippedLogBlock>
```cpp
/* 251615 */
struct SharedCounter<StrippedLogBlock>
{
StrippedLogBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StructureBlock>
```cpp
/* 251611 */
struct SharedCounter<StructureBlock>
{
StructureBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<StructureVoid>
```cpp
/* 251555 */
struct SharedCounter<StructureVoid>
{
StructureVoid *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SuspiciousStewItem>
```cpp
/* 183976 */
struct SharedCounter<SuspiciousStewItem>
{
SuspiciousStewItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<SweetBerryBushBlock>
```cpp
/* 251743 */
struct SharedCounter<SweetBerryBushBlock>
{
SweetBerryBushBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TallGrass>
```cpp
/* 251146 */
struct SharedCounter<TallGrass>
{
TallGrass *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<ThinFenceBlock>
```cpp
/* 251326 */
struct SharedCounter<ThinFenceBlock>
{
ThinFenceBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TntBlock>
```cpp
/* 251177 */
struct SharedCounter<TntBlock>
{
TntBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TopSnowBlock>
```cpp
/* 251256 */
struct SharedCounter<TopSnowBlock>
{
TopSnowBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TopSnowBlockItem>
```cpp
/* 184049 */
struct SharedCounter<TopSnowBlockItem>
{
TopSnowBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TorchBlock>
```cpp
/* 251189 */
struct SharedCounter<TorchBlock>
{
TorchBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TrapDoorBlock>
```cpp
/* 251312 */
struct SharedCounter<TrapDoorBlock>
{
TrapDoorBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TridentItem>
```cpp
/* 183944 */
struct SharedCounter<TridentItem>
{
TridentItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TripWireBlock>
```cpp
/* 251405 */
struct SharedCounter<TripWireBlock>
{
TripWireBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TripWireHookBlock>
```cpp
/* 251401 */
struct SharedCounter<TripWireHookBlock>
{
TripWireHookBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<TurtleEggBlock>
```cpp
/* 251684 */
struct SharedCounter<TurtleEggBlock>
{
TurtleEggBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<UnderwaterTorchBlock>
```cpp
/* 251629 */
struct SharedCounter<UnderwaterTorchBlock>
{
UnderwaterTorchBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<UndyedShulkerBoxBlock>
```cpp
/* 251531 */
struct SharedCounter<UndyedShulkerBoxBlock>
{
UndyedShulkerBoxBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<VineBlock>
```cpp
/* 251338 */
struct SharedCounter<VineBlock>
{
VineBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WallBlock>
```cpp
/* 251416 */
struct SharedCounter<WallBlock>
{
WallBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WaterLilyBlockItem>
```cpp
/* 184045 */
struct SharedCounter<WaterLilyBlockItem>
{
WaterLilyBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WaterlilyBlock>
```cpp
/* 251350 */
struct SharedCounter<WaterlilyBlock>
{
WaterlilyBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WeaponItem>
```cpp
/* 183805 */
struct SharedCounter<WeaponItem>
{
WeaponItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WebBlock>
```cpp
/* 251142 */
struct SharedCounter<WebBlock>
{
WebBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WeightedPressurePlateBlock>
```cpp
/* 251444 */
struct SharedCounter<WeightedPressurePlateBlock>
{
WeightedPressurePlateBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WitherRoseBlock>
```cpp
/* 251770 */
struct SharedCounter<WitherRoseBlock>
{
WitherRoseBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WoodBlock>
```cpp
/* 251759 */
struct SharedCounter<WoodBlock>
{
WoodBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WoodButtonBlock>
```cpp
/* 251432 */
struct SharedCounter<WoodButtonBlock>
{
WoodButtonBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WoodSlabBlock>
```cpp
/* 251467 */
struct SharedCounter<WoodSlabBlock>
{
WoodSlabBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WoodSlabBlockItem>
```cpp
/* 184041 */
struct SharedCounter<WoodSlabBlockItem>
{
WoodSlabBlockItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WoolCarpetBlock>
```cpp
/* 251503 */
struct SharedCounter<WoolCarpetBlock>
{
WoolCarpetBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WorkbenchBlock>
```cpp
/* 251207 */
struct SharedCounter<WorkbenchBlock>
{
WorkbenchBlock *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WritableBookItem>
```cpp
/* 183913 */
struct SharedCounter<WritableBookItem>
{
WritableBookItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedCounter<WrittenBookItem>
```cpp
/* 183917 */
struct SharedCounter<WrittenBookItem>
{
WrittenBookItem *ptr;
std::atomic<int> share_count;
std::atomic<int> weak_count;
};

```
#### SharedModifiers
```cpp
/* 174645 */
struct SharedModifiers
{
__int8 gap0[1];
};

```
#### SharedPtr<ActivatorRailBlock>
```cpp
/* 251388 */
struct SharedPtr<ActivatorRailBlock>
{
SharedCounter<ActivatorRailBlock> *pc;
};

```
#### SharedPtr<AirBlock>
```cpp
/* 250878 */
struct SharedPtr<AirBlock>
{
SharedCounter<AirBlock> *pc;
};

```
#### SharedPtr<AirBlockItem>
```cpp
/* 180755 */
struct SharedPtr<AirBlockItem>
{
SharedCounter<AirBlockItem> *pc;
};

```
#### SharedPtr<AnvilBlock>
```cpp
/* 251439 */
struct SharedPtr<AnvilBlock>
{
SharedCounter<AnvilBlock> *pc;
};

```
#### SharedPtr<ArmorItem>
```cpp
/* 183816 */
struct SharedPtr<ArmorItem>
{
SharedCounter<ArmorItem> *pc;
};

```
#### SharedPtr<ArmorStandItem>
```cpp
/* 183949 */
struct SharedPtr<ArmorStandItem>
{
SharedCounter<ArmorStandItem> *pc;
};

```
#### SharedPtr<ArrowItem>
```cpp
/* 183796 */
struct SharedPtr<ArrowItem>
{
SharedCounter<ArrowItem> *pc;
};

```
#### SharedPtr<AuxDataBlockItem>
```cpp
/* 184011 */
struct SharedPtr<AuxDataBlockItem>
{
SharedCounter<AuxDataBlockItem> *pc;
};

```
#### SharedPtr<BalloonItem>
```cpp
/* 183995 */
struct SharedPtr<BalloonItem>
{
SharedCounter<BalloonItem> *pc;
};

```
#### SharedPtr<BambooBlock>
```cpp
/* 251695 */
struct SharedPtr<BambooBlock>
{
SharedCounter<BambooBlock> *pc;
};

```
#### SharedPtr<BambooBlockItem>
```cpp
/* 184056 */
struct SharedPtr<BambooBlockItem>
{
SharedCounter<BambooBlockItem> *pc;
};

```
#### SharedPtr<BambooSapling>
```cpp
/* 251699 */
struct SharedPtr<BambooSapling>
{
SharedCounter<BambooSapling> *pc;
};

```
#### SharedPtr<BannerBlock>
```cpp
/* 251510 */
struct SharedPtr<BannerBlock>
{
SharedCounter<BannerBlock> *pc;
};

```
#### SharedPtr<BannerItem>
```cpp
/* 183964 */
struct SharedPtr<BannerItem>
{
SharedCounter<BannerItem> *pc;
};

```
#### SharedPtr<BannerPatternItem>
```cpp
/* 183972 */
struct SharedPtr<BannerPatternItem>
{
SharedCounter<BannerPatternItem> *pc;
};

```
#### SharedPtr<BarrelBlock>
```cpp
/* 251730 */
struct SharedPtr<BarrelBlock>
{
SharedCounter<BarrelBlock> *pc;
};

```
#### SharedPtr<BarrierBlock>
```cpp
/* 251687 */
struct SharedPtr<BarrierBlock>
{
SharedCounter<BarrierBlock> *pc;
};

```
#### SharedPtr<BeaconBlock>
```cpp
/* 251411 */
struct SharedPtr<BeaconBlock>
{
SharedCounter<BeaconBlock> *pc;
};

```
#### SharedPtr<BedBlock>
```cpp
/* 251127 */
struct SharedPtr<BedBlock>
{
SharedCounter<BedBlock> *pc;
};

```
#### SharedPtr<BedItem>
```cpp
/* 183875 */
struct SharedPtr<BedItem>
{
SharedCounter<BedItem> *pc;
};

```
#### SharedPtr<BedrockBlock>
```cpp
/* 251075 */
struct SharedPtr<BedrockBlock>
{
SharedCounter<BedrockBlock> *pc;
};

```
#### SharedPtr<BeehiveBlock>
```cpp
/* 251773 */
struct SharedPtr<BeehiveBlock>
{
SharedCounter<BeehiveBlock> *pc;
};

```
#### SharedPtr<BeetrootBlock>
```cpp
/* 251590 */
struct SharedPtr<BeetrootBlock>
{
SharedCounter<BeetrootBlock> *pc;
};

```
#### SharedPtr<BellBlock>
```cpp
/* 251738 */
struct SharedPtr<BellBlock>
{
SharedCounter<BellBlock> *pc;
};

```
#### SharedPtr<BellBlockItem>
```cpp
/* 184064 */
struct SharedPtr<BellBlockItem>
{
SharedCounter<BellBlockItem> *pc;
};

```
#### SharedPtr<BlastFurnaceBlock>
```cpp
/* 251718 */
struct SharedPtr<BlastFurnaceBlock>
{
SharedCounter<BlastFurnaceBlock> *pc;
};

```
#### SharedPtr<BlockItem>
```cpp
/* 182764 */
struct SharedPtr<BlockItem>
{
SharedCounter<BlockItem> *pc;
};

```
#### SharedPtr<BlockLegacy>
```cpp
/* 13209 */
struct SharedPtr<BlockLegacy>
{
SharedCounter<BlockLegacy> *pc;
};

```
#### SharedPtr<BlockPlanterItem>
```cpp
/* 183808 */
struct SharedPtr<BlockPlanterItem>
{
SharedCounter<BlockPlanterItem> *pc;
};

```
#### SharedPtr<BlueIceBlock>
```cpp
/* 251618 */
struct SharedPtr<BlueIceBlock>
{
SharedCounter<BlueIceBlock> *pc;
};

```
#### SharedPtr<BoatItem>
```cpp
/* 183850 */
struct SharedPtr<BoatItem>
{
SharedCounter<BoatItem> *pc;
};

```
#### SharedPtr<BookshelfBlock>
```cpp
/* 251180 */
struct SharedPtr<BookshelfBlock>
{
SharedCounter<BookshelfBlock> *pc;
};

```
#### SharedPtr<BottleItem>
```cpp
/* 183893 */
struct SharedPtr<BottleItem>
{
SharedCounter<BottleItem> *pc;
};

```
#### SharedPtr<BowItem>
```cpp
/* 183792 */
struct SharedPtr<BowItem>
{
SharedCounter<BowItem> *pc;
};

```
#### SharedPtr<BrewingStandBlock>
```cpp
/* 251361 */
struct SharedPtr<BrewingStandBlock>
{
SharedCounter<BrewingStandBlock> *pc;
};

```
#### SharedPtr<BubbleColumnBlock>
```cpp
/* 251679 */
struct SharedPtr<BubbleColumnBlock>
{
SharedCounter<BubbleColumnBlock> *pc;
};

```
#### SharedPtr<BucketItem>
```cpp
/* 183834 */
struct SharedPtr<BucketItem>
{
SharedCounter<BucketItem> *pc;
};

```
#### SharedPtr<CactusBlock>
```cpp
/* 251266 */
struct SharedPtr<CactusBlock>
{
SharedCounter<CactusBlock> *pc;
};

```
#### SharedPtr<CakeBlock>
```cpp
/* 251301 */
struct SharedPtr<CakeBlock>
{
SharedCounter<CakeBlock> *pc;
};

```
#### SharedPtr<CameraBlock>
```cpp
/* 251582 */
struct SharedPtr<CameraBlock>
{
SharedCounter<CameraBlock> *pc;
};

```
#### SharedPtr<CameraItem>
```cpp
/* 183978 */
struct SharedPtr<CameraItem>
{
SharedCounter<CameraItem> *pc;
};

```
#### SharedPtr<CampfireBlock>
```cpp
/* 251750 */
struct SharedPtr<CampfireBlock>
{
SharedCounter<CampfireBlock> *pc;
};

```
#### SharedPtr<CarrotBlock>
```cpp
/* 251423 */
struct SharedPtr<CarrotBlock>
{
SharedCounter<CarrotBlock> *pc;
};

```
#### SharedPtr<CarrotOnAStickItem>
```cpp
/* 183927 */
struct SharedPtr<CarrotOnAStickItem>
{
SharedCounter<CarrotOnAStickItem> *pc;
};

```
#### SharedPtr<CartographyTableBlock>
```cpp
/* 251726 */
struct SharedPtr<CartographyTableBlock>
{
SharedCounter<CartographyTableBlock> *pc;
};

```
#### SharedPtr<CauldronBlock>
```cpp
/* 251365 */
struct SharedPtr<CauldronBlock>
{
SharedCounter<CauldronBlock> *pc;
};

```
#### SharedPtr<ChemicalHeatBlock>
```cpp
/* 251632 */
struct SharedPtr<ChemicalHeatBlock>
{
SharedCounter<ChemicalHeatBlock> *pc;
};

```
#### SharedPtr<ChemistryAuxDataBlockItem>
```cpp
/* 184068 */
struct SharedPtr<ChemistryAuxDataBlockItem>
{
SharedCounter<ChemistryAuxDataBlockItem> *pc;
};

```
#### SharedPtr<ChemistryItem>
```cpp
/* 183989 */
struct SharedPtr<ChemistryItem>
{
SharedCounter<ChemistryItem> *pc;
};

```
#### SharedPtr<ChemistryTableBlock>
```cpp
/* 251625 */
struct SharedPtr<ChemistryTableBlock>
{
SharedCounter<ChemistryTableBlock> *pc;
};

```
#### SharedPtr<ChestBlock>
```cpp
/* 251199 */
struct SharedPtr<ChestBlock>
{
SharedCounter<ChestBlock> *pc;
};

```
#### SharedPtr<ChorusFlowerBlock>
```cpp
/* 251526 */
struct SharedPtr<ChorusFlowerBlock>
{
SharedCounter<ChorusFlowerBlock> *pc;
};

```
#### SharedPtr<ChorusPlantBlock>
```cpp
/* 251574 */
struct SharedPtr<ChorusPlantBlock>
{
SharedCounter<ChorusPlantBlock> *pc;
};

```
#### SharedPtr<ClayBlock>
```cpp
/* 251270 */
struct SharedPtr<ClayBlock>
{
SharedCounter<ClayBlock> *pc;
};

```
#### SharedPtr<ClockItem>
```cpp
/* 183869 */
struct SharedPtr<ClockItem>
{
SharedCounter<ClockItem> *pc;
};

```
#### SharedPtr<ClothBlock>
```cpp
/* 251157 */
struct SharedPtr<ClothBlock>
{
SharedCounter<ClothBlock> *pc;
};

```
#### SharedPtr<ClothBlockItem>
```cpp
/* 184015 */
struct SharedPtr<ClothBlockItem>
{
SharedCounter<ClothBlockItem> *pc;
};

```
#### SharedPtr<CoalItem>
```cpp
/* 183800 */
struct SharedPtr<CoalItem>
{
SharedCounter<CoalItem> *pc;
};

```
#### SharedPtr<CocoaBlock>
```cpp
/* 251392 */
struct SharedPtr<CocoaBlock>
{
SharedCounter<CocoaBlock> *pc;
};

```
#### SharedPtr<ColoredBlock>
```cpp
/* 251470 */
struct SharedPtr<ColoredBlock>
{
SharedCounter<ColoredBlock> *pc;
};

```
#### SharedPtr<ColoredTorchBlock>
```cpp
/* 251636 */
struct SharedPtr<ColoredTorchBlock>
{
SharedCounter<ColoredTorchBlock> *pc;
};

```
#### SharedPtr<CommandBlock>
```cpp
/* 251408 */
struct SharedPtr<CommandBlock>
{
SharedCounter<CommandBlock> *pc;
};

```
#### SharedPtr<ComparatorBlock>
```cpp
/* 251447 */
struct SharedPtr<ComparatorBlock>
{
SharedCounter<ComparatorBlock> *pc;
};

```
#### SharedPtr<CompassItem>
```cpp
/* 183862 */
struct SharedPtr<CompassItem>
{
SharedCounter<CompassItem> *pc;
};

```
#### SharedPtr<ComposterBlock>
```cpp
/* 251762 */
struct SharedPtr<ComposterBlock>
{
SharedCounter<ComposterBlock> *pc;
};

```
#### SharedPtr<CompoundItem>
```cpp
/* 183982 */
struct SharedPtr<CompoundItem>
{
SharedCounter<CompoundItem> *pc;
};

```
#### SharedPtr<ConcreteBlock>
```cpp
/* 251566 */
struct SharedPtr<ConcreteBlock>
{
SharedCounter<ConcreteBlock> *pc;
};

```
#### SharedPtr<ConcretePowderBlock>
```cpp
/* 251570 */
struct SharedPtr<ConcretePowderBlock>
{
SharedCounter<ConcretePowderBlock> *pc;
};

```
#### SharedPtr<ConduitBlock>
```cpp
/* 251675 */
struct SharedPtr<ConduitBlock>
{
SharedCounter<ConduitBlock> *pc;
};

```
#### SharedPtr<Coral>
```cpp
/* 251643 */
struct SharedPtr<Coral>
{
SharedCounter<Coral> *pc;
};

```
#### SharedPtr<CoralBlock>
```cpp
/* 251647 */
struct SharedPtr<CoralBlock>
{
SharedCounter<CoralBlock> *pc;
};

```
#### SharedPtr<CoralFan>
```cpp
/* 251651 */
struct SharedPtr<CoralFan>
{
SharedCounter<CoralFan> *pc;
};

```
#### SharedPtr<CoralFanBlockItem>
```cpp
/* 184024 */
struct SharedPtr<CoralFanBlockItem>
{
SharedCounter<CoralFanBlockItem> *pc;
};

```
#### SharedPtr<CoralFanHang>
```cpp
/* 251655 */
struct SharedPtr<CoralFanHang>
{
SharedCounter<CoralFanHang> *pc;
};

```
#### SharedPtr<CropBlock>
```cpp
/* 251210 */
struct SharedPtr<CropBlock>
{
SharedCounter<CropBlock> *pc;
};

```
#### SharedPtr<CrossbowItem>
```cpp
/* 183968 */
struct SharedPtr<CrossbowItem>
{
SharedCounter<CrossbowItem> *pc;
};

```
#### SharedPtr<DaylightDetectorBlock>
```cpp
/* 251451 */
struct SharedPtr<DaylightDetectorBlock>
{
SharedCounter<DaylightDetectorBlock> *pc;
};

```
#### SharedPtr<DeadBush>
```cpp
/* 251149 */
struct SharedPtr<DeadBush>
{
SharedCounter<DeadBush> *pc;
};

```
#### SharedPtr<DetectorRailBlock>
```cpp
/* 251134 */
struct SharedPtr<DetectorRailBlock>
{
SharedCounter<DetectorRailBlock> *pc;
};

```
#### SharedPtr<DirtBlock>
```cpp
/* 251063 */
struct SharedPtr<DirtBlock>
{
SharedCounter<DirtBlock> *pc;
};

```
#### SharedPtr<DispenserBlock>
```cpp
/* 251115 */
struct SharedPtr<DispenserBlock>
{
SharedCounter<DispenserBlock> *pc;
};

```
#### SharedPtr<DoorBlock>
```cpp
/* 251225 */
struct SharedPtr<DoorBlock>
{
SharedCounter<DoorBlock> *pc;
};

```
#### SharedPtr<DoorItem>
```cpp
/* 183830 */
struct SharedPtr<DoorItem>
{
SharedCounter<DoorItem> *pc;
};

```
#### SharedPtr<DoublePlantBlock>
```cpp
/* 251506 */
struct SharedPtr<DoublePlantBlock>
{
SharedCounter<DoublePlantBlock> *pc;
};

```
#### SharedPtr<DragonEggBlock>
```cpp
/* 251376 */
struct SharedPtr<DragonEggBlock>
{
SharedCounter<DragonEggBlock> *pc;
};

```
#### SharedPtr<DriedKelpBlock>
```cpp
/* 251663 */
struct SharedPtr<DriedKelpBlock>
{
SharedCounter<DriedKelpBlock> *pc;
};

```
#### SharedPtr<DropperBlock>
```cpp
/* 251384 */
struct SharedPtr<DropperBlock>
{
SharedCounter<DropperBlock> *pc;
};

```
#### SharedPtr<DyePowderItem>
```cpp
/* 183872 */
struct SharedPtr<DyePowderItem>
{
SharedCounter<DyePowderItem> *pc;
};

```
#### SharedPtr<EggItem>
```cpp
/* 183858 */
struct SharedPtr<EggItem>
{
SharedCounter<EggItem> *pc;
};

```
#### SharedPtr<ElementBlock>
```cpp
/* 251640 */
struct SharedPtr<ElementBlock>
{
SharedCounter<ElementBlock> *pc;
};

```
#### SharedPtr<ElementBlockItem>
```cpp
/* 184072 */
struct SharedPtr<ElementBlockItem>
{
SharedCounter<ElementBlockItem> *pc;
};

```
#### SharedPtr<EmptyMapItem>
```cpp
/* 183920 */
struct SharedPtr<EmptyMapItem>
{
SharedCounter<EmptyMapItem> *pc;
};

```
#### SharedPtr<EnchantedBookItem>
```cpp
/* 183854 */
struct SharedPtr<EnchantedBookItem>
{
SharedCounter<EnchantedBookItem> *pc;
};

```
#### SharedPtr<EnchantingTableBlock>
```cpp
/* 251357 */
struct SharedPtr<EnchantingTableBlock>
{
SharedCounter<EnchantingTableBlock> *pc;
};

```
#### SharedPtr<EndCrystalItem>
```cpp
/* 183953 */
struct SharedPtr<EndCrystalItem>
{
SharedCounter<EndCrystalItem> *pc;
};

```
#### SharedPtr<EndGatewayBlock>
```cpp
/* 251542 */
struct SharedPtr<EndGatewayBlock>
{
SharedCounter<EndGatewayBlock> *pc;
};

```
#### SharedPtr<EndPortalBlock>
```cpp
/* 251368 */
struct SharedPtr<EndPortalBlock>
{
SharedCounter<EndPortalBlock> *pc;
};

```
#### SharedPtr<EndPortalFrameBlock>
```cpp
/* 251372 */
struct SharedPtr<EndPortalFrameBlock>
{
SharedCounter<EndPortalFrameBlock> *pc;
};

```
#### SharedPtr<EndRodBlock>
```cpp
/* 251538 */
struct SharedPtr<EndRodBlock>
{
SharedCounter<EndRodBlock> *pc;
};

```
#### SharedPtr<EnderChestBlock>
```cpp
/* 251396 */
struct SharedPtr<EnderChestBlock>
{
SharedCounter<EnderChestBlock> *pc;
};

```
#### SharedPtr<EnderEyeItem>
```cpp
/* 183897 */
struct SharedPtr<EnderEyeItem>
{
SharedCounter<EnderEyeItem> *pc;
};

```
#### SharedPtr<EnderpearlItem>
```cpp
/* 183886 */
struct SharedPtr<EnderpearlItem>
{
SharedCounter<EnderpearlItem> *pc;
};

```
#### SharedPtr<ExperiencePotionItem>
```cpp
/* 183904 */
struct SharedPtr<ExperiencePotionItem>
{
SharedCounter<ExperiencePotionItem> *pc;
};

```
#### SharedPtr<FarmBlock>
```cpp
/* 251214 */
struct SharedPtr<FarmBlock>
{
SharedCounter<FarmBlock> *pc;
};

```
#### SharedPtr<FenceBlock>
```cpp
/* 251282 */
struct SharedPtr<FenceBlock>
{
SharedCounter<FenceBlock> *pc;
};

```
#### SharedPtr<FenceGateBlock>
```cpp
/* 251341 */
struct SharedPtr<FenceGateBlock>
{
SharedCounter<FenceGateBlock> *pc;
};

```
#### SharedPtr<FireBlock>
```cpp
/* 251622 */
struct SharedPtr<FireBlock>
{
SharedCounter<FireBlock> *pc;
};

```
#### SharedPtr<FireChargeItem>
```cpp
/* 183908 */
struct SharedPtr<FireChargeItem>
{
SharedCounter<FireChargeItem> *pc;
};

```
#### SharedPtr<FireworkChargeItem>
```cpp
/* 183934 */
struct SharedPtr<FireworkChargeItem>
{
SharedCounter<FireworkChargeItem> *pc;
};

```
#### SharedPtr<FireworksItem>
```cpp
/* 183931 */
struct SharedPtr<FireworksItem>
{
SharedCounter<FireworksItem> *pc;
};

```
#### SharedPtr<FishingRodItem>
```cpp
/* 183865 */
struct SharedPtr<FishingRodItem>
{
SharedCounter<FishingRodItem> *pc;
};

```
#### SharedPtr<FlintAndSteelItem>
```cpp
/* 183788 */
struct SharedPtr<FlintAndSteelItem>
{
SharedCounter<FlintAndSteelItem> *pc;
};

```
#### SharedPtr<FlowerBlock>
```cpp
/* 251161 */
struct SharedPtr<FlowerBlock>
{
SharedCounter<FlowerBlock> *pc;
};

```
#### SharedPtr<FlowerPotBlock>
```cpp
/* 251419 */
struct SharedPtr<FlowerPotBlock>
{
SharedCounter<FlowerPotBlock> *pc;
};

```
#### SharedPtr<FrostedIceBlock>
```cpp
/* 251534 */
struct SharedPtr<FrostedIceBlock>
{
SharedCounter<FrostedIceBlock> *pc;
};

```
#### SharedPtr<FurnaceBlock>
```cpp
/* 251217 */
struct SharedPtr<FurnaceBlock>
{
SharedCounter<FurnaceBlock> *pc;
};

```
#### SharedPtr<GlassBlock>
```cpp
/* 251111 */
struct SharedPtr<GlassBlock>
{
SharedCounter<GlassBlock> *pc;
};

```
#### SharedPtr<GlazedTerracottaBlock>
```cpp
/* 251562 */
struct SharedPtr<GlazedTerracottaBlock>
{
SharedCounter<GlazedTerracottaBlock> *pc;
};

```
#### SharedPtr<GlowStickItem>
```cpp
/* 184007 */
struct SharedPtr<GlowStickItem>
{
SharedCounter<GlowStickItem> *pc;
};

```
#### SharedPtr<GrassBlock>
```cpp
/* 251059 */
struct SharedPtr<GrassBlock>
{
SharedCounter<GrassBlock> *pc;
};

```
#### SharedPtr<GrassPathBlock>
```cpp
/* 251518 */
struct SharedPtr<GrassPathBlock>
{
SharedCounter<GrassPathBlock> *pc;
};

```
#### SharedPtr<GravelBlock>
```cpp
/* 251091 */
struct SharedPtr<GravelBlock>
{
SharedCounter<GravelBlock> *pc;
};

```
#### SharedPtr<GrindstoneBlock>
```cpp
/* 251714 */
struct SharedPtr<GrindstoneBlock>
{
SharedCounter<GrindstoneBlock> *pc;
};

```
#### SharedPtr<HangingActorItem>
```cpp
/* 183822 */
struct SharedPtr<HangingActorItem>
{
SharedCounter<HangingActorItem> *pc;
};

```
#### SharedPtr<HatchetItem>
```cpp
/* 183784 */
struct SharedPtr<HatchetItem>
{
SharedCounter<HatchetItem> *pc;
};

```
#### SharedPtr<HayBlockBlock>
```cpp
/* 251498 */
struct SharedPtr<HayBlockBlock>
{
SharedCounter<HayBlockBlock> *pc;
};

```
#### SharedPtr<HoeItem>
```cpp
/* 183812 */
struct SharedPtr<HoeItem>
{
SharedCounter<HoeItem> *pc;
};

```
#### SharedPtr<HoneyBlock>
```cpp
/* 251776 */
struct SharedPtr<HoneyBlock>
{
SharedCounter<HoneyBlock> *pc;
};

```
#### SharedPtr<HoneycombBlock>
```cpp
/* 251780 */
struct SharedPtr<HoneycombBlock>
{
SharedCounter<HoneycombBlock> *pc;
};

```
#### SharedPtr<HopperBlock>
```cpp
/* 251458 */
struct SharedPtr<HopperBlock>
{
SharedCounter<HopperBlock> *pc;
};

```
#### SharedPtr<HorseArmorItem>
```cpp
/* 183937 */
struct SharedPtr<HorseArmorItem>
{
SharedCounter<HorseArmorItem> *pc;
};

```
#### SharedPtr<HugeMushroomBlock>
```cpp
/* 251322 */
struct SharedPtr<HugeMushroomBlock>
{
SharedCounter<HugeMushroomBlock> *pc;
};

```
#### SharedPtr<IceBlock>
```cpp
/* 251258 */
struct SharedPtr<IceBlock>
{
SharedCounter<IceBlock> *pc;
};

```
#### SharedPtr<IceBombItem>
```cpp
/* 183985 */
struct SharedPtr<IceBombItem>
{
SharedCounter<IceBombItem> *pc;
};

```
#### SharedPtr<InvisibleBlock>
```cpp
/* 251307 */
struct SharedPtr<InvisibleBlock>
{
SharedCounter<InvisibleBlock> *pc;
};

```
#### SharedPtr<Item>
```cpp
/* 13205 */
struct SharedPtr<Item>
{
SharedCounter<Item> *pc;
};

```
#### SharedPtr<ItemFrameBlock>
```cpp
/* 251522 */
struct SharedPtr<ItemFrameBlock>
{
SharedCounter<ItemFrameBlock> *pc;
};

```
#### SharedPtr<JigsawBlock>
```cpp
/* 251754 */
struct SharedPtr<JigsawBlock>
{
SharedCounter<JigsawBlock> *pc;
};

```
#### SharedPtr<JukeboxBlock>
```cpp
/* 251278 */
struct SharedPtr<JukeboxBlock>
{
SharedCounter<JukeboxBlock> *pc;
};

```
#### SharedPtr<KelpBlock>
```cpp
/* 251659 */
struct SharedPtr<KelpBlock>
{
SharedCounter<KelpBlock> *pc;
};

```
#### SharedPtr<LadderBlock>
```cpp
/* 251228 */
struct SharedPtr<LadderBlock>
{
SharedCounter<LadderBlock> *pc;
};

```
#### SharedPtr<LanternBlock>
```cpp
/* 251746 */
struct SharedPtr<LanternBlock>
{
SharedCounter<LanternBlock> *pc;
};

```
#### SharedPtr<LeadItem>
```cpp
/* 183946 */
struct SharedPtr<LeadItem>
{
SharedCounter<LeadItem> *pc;
};

```
#### SharedPtr<LeafBlockItem>
```cpp
/* 184036 */
struct SharedPtr<LeafBlockItem>
{
SharedCounter<LeafBlockItem> *pc;
};

```
#### SharedPtr<LecternBlock>
```cpp
/* 251711 */
struct SharedPtr<LecternBlock>
{
SharedCounter<LecternBlock> *pc;
};

```
#### SharedPtr<LeverBlock>
```cpp
/* 251236 */
struct SharedPtr<LeverBlock>
{
SharedCounter<LeverBlock> *pc;
};

```
#### SharedPtr<LightBlock>
```cpp
/* 251765 */
struct SharedPtr<LightBlock>
{
SharedCounter<LightBlock> *pc;
};

```
#### SharedPtr<LightGemBlock>
```cpp
/* 251294 */
struct SharedPtr<LightGemBlock>
{
SharedCounter<LightGemBlock> *pc;
};

```
#### SharedPtr<LingeringPotionItem>
```cpp
/* 183960 */
struct SharedPtr<LingeringPotionItem>
{
SharedCounter<LingeringPotionItem> *pc;
};

```
#### SharedPtr<LiquidBlockDynamic>
```cpp
/* 251079 */
struct SharedPtr<LiquidBlockDynamic>
{
SharedCounter<LiquidBlockDynamic> *pc;
};

```
#### SharedPtr<LiquidBlockStatic>
```cpp
/* 251083 */
struct SharedPtr<LiquidBlockStatic>
{
SharedCounter<LiquidBlockStatic> *pc;
};

```
#### SharedPtr<LoomBlock>
```cpp
/* 251734 */
struct SharedPtr<LoomBlock>
{
SharedCounter<LoomBlock> *pc;
};

```
#### SharedPtr<MagmaBlock>
```cpp
/* 251546 */
struct SharedPtr<MagmaBlock>
{
SharedCounter<MagmaBlock> *pc;
};

```
#### SharedPtr<MapItem>
```cpp
/* 183879 */
struct SharedPtr<MapItem>
{
SharedCounter<MapItem> *pc;
};

```
#### SharedPtr<MedicineItem>
```cpp
/* 183999 */
struct SharedPtr<MedicineItem>
{
SharedCounter<MedicineItem> *pc;
};

```
#### SharedPtr<MelonBlock>
```cpp
/* 251329 */
struct SharedPtr<MelonBlock>
{
SharedCounter<MelonBlock> *pc;
};

```
#### SharedPtr<MetalBlock>
```cpp
/* 251168 */
struct SharedPtr<MetalBlock>
{
SharedCounter<MetalBlock> *pc;
};

```
#### SharedPtr<MinecartItem>
```cpp
/* 183838 */
struct SharedPtr<MinecartItem>
{
SharedCounter<MinecartItem> *pc;
};

```
#### SharedPtr<MobPlacerItem>
```cpp
/* 183901 */
struct SharedPtr<MobPlacerItem>
{
SharedCounter<MobPlacerItem> *pc;
};

```
#### SharedPtr<MobSpawnerBlock>
```cpp
/* 251192 */
struct SharedPtr<MobSpawnerBlock>
{
SharedCounter<MobSpawnerBlock> *pc;
};

```
#### SharedPtr<MonsterEggBlock>
```cpp
/* 251315 */
struct SharedPtr<MonsterEggBlock>
{
SharedCounter<MonsterEggBlock> *pc;
};

```
#### SharedPtr<MovingBlock>
```cpp
/* 251602 */
struct SharedPtr<MovingBlock>
{
SharedCounter<MovingBlock> *pc;
};

```
#### SharedPtr<MushroomBlock>
```cpp
/* 251164 */
struct SharedPtr<MushroomBlock>
{
SharedCounter<MushroomBlock> *pc;
};

```
#### SharedPtr<MyceliumBlock>
```cpp
/* 251345 */
struct SharedPtr<MyceliumBlock>
{
SharedCounter<MyceliumBlock> *pc;
};

```
#### SharedPtr<NetherReactorBlock>
```cpp
/* 251598 */
struct SharedPtr<NetherReactorBlock>
{
SharedCounter<NetherReactorBlock> *pc;
};

```
#### SharedPtr<NetherWartBlock>
```cpp
/* 251353 */
struct SharedPtr<NetherWartBlock>
{
SharedCounter<NetherWartBlock> *pc;
};

```
#### SharedPtr<NewLeafBlock>
```cpp
/* 251478 */
struct SharedPtr<NewLeafBlock>
{
SharedCounter<NewLeafBlock> *pc;
};

```
#### SharedPtr<NewLogBlock>
```cpp
/* 251482 */
struct SharedPtr<NewLogBlock>
{
SharedCounter<NewLogBlock> *pc;
};

```
#### SharedPtr<NoteBlock>
```cpp
/* 251123 */
struct SharedPtr<NoteBlock>
{
SharedCounter<NoteBlock> *pc;
};

```
#### SharedPtr<ObserverBlock>
```cpp
/* 251606 */
struct SharedPtr<ObserverBlock>
{
SharedCounter<ObserverBlock> *pc;
};

```
#### SharedPtr<ObsidianBlock>
```cpp
/* 251184 */
struct SharedPtr<ObsidianBlock>
{
SharedCounter<ObsidianBlock> *pc;
};

```
#### SharedPtr<OldLeafBlock>
```cpp
/* 251103 */
struct SharedPtr<OldLeafBlock>
{
SharedCounter<OldLeafBlock> *pc;
};

```
#### SharedPtr<OldLogBlock>
```cpp
/* 251099 */
struct SharedPtr<OldLogBlock>
{
SharedCounter<OldLogBlock> *pc;
};

```
#### SharedPtr<OreBlock>
```cpp
/* 251095 */
struct SharedPtr<OreBlock>
{
SharedCounter<OreBlock> *pc;
};

```
#### SharedPtr<PickaxeItem>
```cpp
/* 183780 */
struct SharedPtr<PickaxeItem>
{
SharedCounter<PickaxeItem> *pc;
};

```
#### SharedPtr<PistonArmBlock>
```cpp
/* 251153 */
struct SharedPtr<PistonArmBlock>
{
SharedCounter<PistonArmBlock> *pc;
};

```
#### SharedPtr<PistonBlock>
```cpp
/* 251138 */
struct SharedPtr<PistonBlock>
{
SharedCounter<PistonBlock> *pc;
};

```
#### SharedPtr<PlanksBlock>
```cpp
/* 251067 */
struct SharedPtr<PlanksBlock>
{
SharedCounter<PlanksBlock> *pc;
};

```
#### SharedPtr<PodzolBlock>
```cpp
/* 251586 */
struct SharedPtr<PodzolBlock>
{
SharedCounter<PodzolBlock> *pc;
};

```
#### SharedPtr<PortalBlock>
```cpp
/* 251298 */
struct SharedPtr<PortalBlock>
{
SharedCounter<PortalBlock> *pc;
};

```
#### SharedPtr<PotatoBlock>
```cpp
/* 251427 */
struct SharedPtr<PotatoBlock>
{
SharedCounter<PotatoBlock> *pc;
};

```
#### SharedPtr<PotionItem>
```cpp
/* 183890 */
struct SharedPtr<PotionItem>
{
SharedCounter<PotionItem> *pc;
};

```
#### SharedPtr<PoweredRailBlock>
```cpp
/* 251130 */
struct SharedPtr<PoweredRailBlock>
{
SharedCounter<PoweredRailBlock> *pc;
};

```
#### SharedPtr<PressurePlateBlock>
```cpp
/* 251240 */
struct SharedPtr<PressurePlateBlock>
{
SharedCounter<PressurePlateBlock> *pc;
};

```
#### SharedPtr<PrismarineBlock>
```cpp
/* 251490 */
struct SharedPtr<PrismarineBlock>
{
SharedCounter<PrismarineBlock> *pc;
};

```
#### SharedPtr<PumpkinBlock>
```cpp
/* 251286 */
struct SharedPtr<PumpkinBlock>
{
SharedCounter<PumpkinBlock> *pc;
};

```
#### SharedPtr<QuartzBlockBlock>
```cpp
/* 251462 */
struct SharedPtr<QuartzBlockBlock>
{
SharedCounter<QuartzBlockBlock> *pc;
};

```
#### SharedPtr<RailBlock>
```cpp
/* 251232 */
struct SharedPtr<RailBlock>
{
SharedCounter<RailBlock> *pc;
};

```
#### SharedPtr<RapidFertilizerItem>
```cpp
/* 183992 */
struct SharedPtr<RapidFertilizerItem>
{
SharedCounter<RapidFertilizerItem> *pc;
};

```
#### SharedPtr<RecordItem>
```cpp
/* 183940 */
struct SharedPtr<RecordItem>
{
SharedCounter<RecordItem> *pc;
};

```
#### SharedPtr<RedStoneDustItem>
```cpp
/* 183842 */
struct SharedPtr<RedStoneDustItem>
{
SharedCounter<RedStoneDustItem> *pc;
};

```
#### SharedPtr<RedStoneOreBlock>
```cpp
/* 251243 */
struct SharedPtr<RedStoneOreBlock>
{
SharedCounter<RedStoneOreBlock> *pc;
};

```
#### SharedPtr<RedStoneWireBlock>
```cpp
/* 251202 */
struct SharedPtr<RedStoneWireBlock>
{
SharedCounter<RedStoneWireBlock> *pc;
};

```
#### SharedPtr<RedstoneBlock>
```cpp
/* 251454 */
struct SharedPtr<RedstoneBlock>
{
SharedCounter<RedstoneBlock> *pc;
};

```
#### SharedPtr<RedstoneLampBlock>
```cpp
/* 251380 */
struct SharedPtr<RedstoneLampBlock>
{
SharedCounter<RedstoneLampBlock> *pc;
};

```
#### SharedPtr<RedstoneTorchBlock>
```cpp
/* 251247 */
struct SharedPtr<RedstoneTorchBlock>
{
SharedCounter<RedstoneTorchBlock> *pc;
};

```
#### SharedPtr<ReedBlock>
```cpp
/* 251274 */
struct SharedPtr<ReedBlock>
{
SharedCounter<ReedBlock> *pc;
};

```
#### SharedPtr<RepeaterBlock>
```cpp
/* 251304 */
struct SharedPtr<RepeaterBlock>
{
SharedCounter<RepeaterBlock> *pc;
};

```
#### SharedPtr<RotatedPillarBlock>
```cpp
/* 251550 */
struct SharedPtr<RotatedPillarBlock>
{
SharedCounter<RotatedPillarBlock> *pc;
};

```
#### SharedPtr<SandBlock>
```cpp
/* 251087 */
struct SharedPtr<SandBlock>
{
SharedCounter<SandBlock> *pc;
};

```
#### SharedPtr<SandStoneBlock>
```cpp
/* 251119 */
struct SharedPtr<SandStoneBlock>
{
SharedCounter<SandStoneBlock> *pc;
};

```
#### SharedPtr<Sapling>
```cpp
/* 251071 */
struct SharedPtr<Sapling>
{
SharedCounter<Sapling> *pc;
};

```
#### SharedPtr<SaplingBlockItem>
```cpp
/* 184032 */
struct SharedPtr<SaplingBlockItem>
{
SharedCounter<SaplingBlockItem> *pc;
};

```
#### SharedPtr<ScaffoldingBlock>
```cpp
/* 251691 */
struct SharedPtr<ScaffoldingBlock>
{
SharedCounter<ScaffoldingBlock> *pc;
};

```
#### SharedPtr<ScaffoldingBlockItem>
```cpp
/* 184060 */
struct SharedPtr<ScaffoldingBlockItem>
{
SharedCounter<ScaffoldingBlockItem> *pc;
};

```
#### SharedPtr<SeaGrass>
```cpp
/* 251667 */
struct SharedPtr<SeaGrass>
{
SharedCounter<SeaGrass> *pc;
};

```
#### SharedPtr<SeaLanternBlock>
```cpp
/* 251494 */
struct SharedPtr<SeaLanternBlock>
{
SharedCounter<SeaLanternBlock> *pc;
};

```
#### SharedPtr<SeaPickle>
```cpp
/* 251671 */
struct SharedPtr<SeaPickle>
{
SharedCounter<SeaPickle> *pc;
};

```
#### SharedPtr<SeaPickleBlockItem>
```cpp
/* 184028 */
struct SharedPtr<SeaPickleBlockItem>
{
SharedCounter<SeaPickleBlockItem> *pc;
};

```
#### SharedPtr<ShearsItem>
```cpp
/* 183882 */
struct SharedPtr<ShearsItem>
{
SharedCounter<ShearsItem> *pc;
};

```
#### SharedPtr<ShieldItem>
```cpp
/* 183819 */
struct SharedPtr<ShieldItem>
{
SharedCounter<ShieldItem> *pc;
};

```
#### SharedPtr<ShovelItem>
```cpp
/* 183776 */
struct SharedPtr<ShovelItem>
{
SharedCounter<ShovelItem> *pc;
};

```
#### SharedPtr<ShulkerBoxBlock>
```cpp
/* 251558 */
struct SharedPtr<ShulkerBoxBlock>
{
SharedCounter<ShulkerBoxBlock> *pc;
};

```
#### SharedPtr<ShulkerBoxBlockItem>
```cpp
/* 184052 */
struct SharedPtr<ShulkerBoxBlockItem>
{
SharedCounter<ShulkerBoxBlockItem> *pc;
};

```
#### SharedPtr<SignBlock>
```cpp
/* 251221 */
struct SharedPtr<SignBlock>
{
SharedCounter<SignBlock> *pc;
};

```
#### SharedPtr<SignItem>
```cpp
/* 183826 */
struct SharedPtr<SignItem>
{
SharedCounter<SignItem> *pc;
};

```
#### SharedPtr<SkullBlock>
```cpp
/* 251435 */
struct SharedPtr<SkullBlock>
{
SharedCounter<SkullBlock> *pc;
};

```
#### SharedPtr<SkullItem>
```cpp
/* 183923 */
struct SharedPtr<SkullItem>
{
SharedCounter<SkullItem> *pc;
};

```
#### SharedPtr<SlimeBlock>
```cpp
/* 251486 */
struct SharedPtr<SlimeBlock>
{
SharedCounter<SlimeBlock> *pc;
};

```
#### SharedPtr<SmokerBlock>
```cpp
/* 251722 */
struct SharedPtr<SmokerBlock>
{
SharedCounter<SmokerBlock> *pc;
};

```
#### SharedPtr<SnowBlock>
```cpp
/* 251262 */
struct SharedPtr<SnowBlock>
{
SharedCounter<SnowBlock> *pc;
};

```
#### SharedPtr<SnowballItem>
```cpp
/* 183846 */
struct SharedPtr<SnowballItem>
{
SharedCounter<SnowballItem> *pc;
};

```
#### SharedPtr<SoulSandBlock>
```cpp
/* 251290 */
struct SharedPtr<SoulSandBlock>
{
SharedCounter<SoulSandBlock> *pc;
};

```
#### SharedPtr<SparklerItem>
```cpp
/* 184003 */
struct SharedPtr<SparklerItem>
{
SharedCounter<SparklerItem> *pc;
};

```
#### SharedPtr<SplashPotionItem>
```cpp
/* 183957 */
struct SharedPtr<SplashPotionItem>
{
SharedCounter<SplashPotionItem> *pc;
};

```
#### SharedPtr<SpongeBlock>
```cpp
/* 251107 */
struct SharedPtr<SpongeBlock>
{
SharedCounter<SpongeBlock> *pc;
};

```
#### SharedPtr<StainedGlassBlock>
```cpp
/* 251578 */
struct SharedPtr<StainedGlassBlock>
{
SharedCounter<StainedGlassBlock> *pc;
};

```
#### SharedPtr<StainedGlassPaneBlock>
```cpp
/* 251474 */
struct SharedPtr<StainedGlassPaneBlock>
{
SharedCounter<StainedGlassPaneBlock> *pc;
};

```
#### SharedPtr<StairBlock>
```cpp
/* 251196 */
struct SharedPtr<StairBlock>
{
SharedCounter<StairBlock> *pc;
};

```
#### SharedPtr<StemBlock>
```cpp
/* 251333 */
struct SharedPtr<StemBlock>
{
SharedCounter<StemBlock> *pc;
};

```
#### SharedPtr<StoneBlock>
```cpp
/* 251055 */
struct SharedPtr<StoneBlock>
{
SharedCounter<StoneBlock> *pc;
};

```
#### SharedPtr<StoneBrickBlock>
```cpp
/* 251318 */
struct SharedPtr<StoneBrickBlock>
{
SharedCounter<StoneBrickBlock> *pc;
};

```
#### SharedPtr<StoneButtonBlock>
```cpp
/* 251251 */
struct SharedPtr<StoneButtonBlock>
{
SharedCounter<StoneButtonBlock> *pc;
};

```
#### SharedPtr<StoneSlabBlock2>
```cpp
/* 251514 */
struct SharedPtr<StoneSlabBlock2>
{
SharedCounter<StoneSlabBlock2> *pc;
};

```
#### SharedPtr<StoneSlabBlock3>
```cpp
/* 251703 */
struct SharedPtr<StoneSlabBlock3>
{
SharedCounter<StoneSlabBlock3> *pc;
};

```
#### SharedPtr<StoneSlabBlock4>
```cpp
/* 251707 */
struct SharedPtr<StoneSlabBlock4>
{
SharedCounter<StoneSlabBlock4> *pc;
};

```
#### SharedPtr<StoneSlabBlock>
```cpp
/* 251172 */
struct SharedPtr<StoneSlabBlock>
{
SharedCounter<StoneSlabBlock> *pc;
};

```
#### SharedPtr<StoneSlabBlockItem>
```cpp
/* 184019 */
struct SharedPtr<StoneSlabBlockItem>
{
SharedCounter<StoneSlabBlockItem> *pc;
};

```
#### SharedPtr<StonecutterBlock>
```cpp
/* 251594 */
struct SharedPtr<StonecutterBlock>
{
SharedCounter<StonecutterBlock> *pc;
};

```
#### SharedPtr<StrippedLogBlock>
```cpp
/* 251614 */
struct SharedPtr<StrippedLogBlock>
{
SharedCounter<StrippedLogBlock> *pc;
};

```
#### SharedPtr<StructureBlock>
```cpp
/* 251610 */
struct SharedPtr<StructureBlock>
{
SharedCounter<StructureBlock> *pc;
};

```
#### SharedPtr<StructureVoid>
```cpp
/* 251554 */
struct SharedPtr<StructureVoid>
{
SharedCounter<StructureVoid> *pc;
};

```
#### SharedPtr<SuspiciousStewItem>
```cpp
/* 183975 */
struct SharedPtr<SuspiciousStewItem>
{
SharedCounter<SuspiciousStewItem> *pc;
};

```
#### SharedPtr<SweetBerryBushBlock>
```cpp
/* 251742 */
struct SharedPtr<SweetBerryBushBlock>
{
SharedCounter<SweetBerryBushBlock> *pc;
};

```
#### SharedPtr<TallGrass>
```cpp
/* 251145 */
struct SharedPtr<TallGrass>
{
SharedCounter<TallGrass> *pc;
};

```
#### SharedPtr<ThinFenceBlock>
```cpp
/* 251325 */
struct SharedPtr<ThinFenceBlock>
{
SharedCounter<ThinFenceBlock> *pc;
};

```
#### SharedPtr<TntBlock>
```cpp
/* 251176 */
struct SharedPtr<TntBlock>
{
SharedCounter<TntBlock> *pc;
};

```
#### SharedPtr<TopSnowBlock>
```cpp
/* 251255 */
struct SharedPtr<TopSnowBlock>
{
SharedCounter<TopSnowBlock> *pc;
};

```
#### SharedPtr<TopSnowBlockItem>
```cpp
/* 184048 */
struct SharedPtr<TopSnowBlockItem>
{
SharedCounter<TopSnowBlockItem> *pc;
};

```
#### SharedPtr<TorchBlock>
```cpp
/* 251188 */
struct SharedPtr<TorchBlock>
{
SharedCounter<TorchBlock> *pc;
};

```
#### SharedPtr<TrapDoorBlock>
```cpp
/* 251311 */
struct SharedPtr<TrapDoorBlock>
{
SharedCounter<TrapDoorBlock> *pc;
};

```
#### SharedPtr<TridentItem>
```cpp
/* 183943 */
struct SharedPtr<TridentItem>
{
SharedCounter<TridentItem> *pc;
};

```
#### SharedPtr<TripWireBlock>
```cpp
/* 251404 */
struct SharedPtr<TripWireBlock>
{
SharedCounter<TripWireBlock> *pc;
};

```
#### SharedPtr<TripWireHookBlock>
```cpp
/* 251400 */
struct SharedPtr<TripWireHookBlock>
{
SharedCounter<TripWireHookBlock> *pc;
};

```
#### SharedPtr<TurtleEggBlock>
```cpp
/* 251683 */
struct SharedPtr<TurtleEggBlock>
{
SharedCounter<TurtleEggBlock> *pc;
};

```
#### SharedPtr<UnderwaterTorchBlock>
```cpp
/* 251628 */
struct SharedPtr<UnderwaterTorchBlock>
{
SharedCounter<UnderwaterTorchBlock> *pc;
};

```
#### SharedPtr<UndyedShulkerBoxBlock>
```cpp
/* 251530 */
struct SharedPtr<UndyedShulkerBoxBlock>
{
SharedCounter<UndyedShulkerBoxBlock> *pc;
};

```
#### SharedPtr<VineBlock>
```cpp
/* 251337 */
struct SharedPtr<VineBlock>
{
SharedCounter<VineBlock> *pc;
};

```
#### SharedPtr<WallBlock>
```cpp
/* 251415 */
struct SharedPtr<WallBlock>
{
SharedCounter<WallBlock> *pc;
};

```
#### SharedPtr<WaterLilyBlockItem>
```cpp
/* 184044 */
struct SharedPtr<WaterLilyBlockItem>
{
SharedCounter<WaterLilyBlockItem> *pc;
};

```
#### SharedPtr<WaterlilyBlock>
```cpp
/* 251349 */
struct SharedPtr<WaterlilyBlock>
{
SharedCounter<WaterlilyBlock> *pc;
};

```
#### SharedPtr<WeaponItem>
```cpp
/* 183804 */
struct SharedPtr<WeaponItem>
{
SharedCounter<WeaponItem> *pc;
};

```
#### SharedPtr<WebBlock>
```cpp
/* 251141 */
struct SharedPtr<WebBlock>
{
SharedCounter<WebBlock> *pc;
};

```
#### SharedPtr<WeightedPressurePlateBlock>
```cpp
/* 251443 */
struct SharedPtr<WeightedPressurePlateBlock>
{
SharedCounter<WeightedPressurePlateBlock> *pc;
};

```
#### SharedPtr<WitherRoseBlock>
```cpp
/* 251769 */
struct SharedPtr<WitherRoseBlock>
{
SharedCounter<WitherRoseBlock> *pc;
};

```
#### SharedPtr<WoodBlock>
```cpp
/* 251758 */
struct SharedPtr<WoodBlock>
{
SharedCounter<WoodBlock> *pc;
};

```
#### SharedPtr<WoodButtonBlock>
```cpp
/* 251431 */
struct SharedPtr<WoodButtonBlock>
{
SharedCounter<WoodButtonBlock> *pc;
};

```
#### SharedPtr<WoodSlabBlock>
```cpp
/* 251466 */
struct SharedPtr<WoodSlabBlock>
{
SharedCounter<WoodSlabBlock> *pc;
};

```
#### SharedPtr<WoodSlabBlockItem>
```cpp
/* 184040 */
struct SharedPtr<WoodSlabBlockItem>
{
SharedCounter<WoodSlabBlockItem> *pc;
};

```
#### SharedPtr<WoolCarpetBlock>
```cpp
/* 251502 */
struct SharedPtr<WoolCarpetBlock>
{
SharedCounter<WoolCarpetBlock> *pc;
};

```
#### SharedPtr<WorkbenchBlock>
```cpp
/* 251206 */
struct SharedPtr<WorkbenchBlock>
{
SharedCounter<WorkbenchBlock> *pc;
};

```
#### SharedPtr<WritableBookItem>
```cpp
/* 183912 */
struct SharedPtr<WritableBookItem>
{
SharedCounter<WritableBookItem> *pc;
};

```
#### SharedPtr<WrittenBookItem>
```cpp
/* 183916 */
struct SharedPtr<WrittenBookItem>
{
SharedCounter<WrittenBookItem> *pc;
};

```
#### ShieldItemUtils
```cpp
/* 183434 */
struct ShieldItemUtils
{
__int8 gap0[1];
};

```
#### ShoreTransformation;
```cpp
/* 198717 */
struct ShoreTransformation;

```
#### Shulker::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 171018 */
struct Shulker::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Silverfish::spawnAnim::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 171020 */
struct Silverfish::spawnAnim::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SimpleContainer
```cpp
/* 89261 */
struct SimpleContainer
{
__int8 baseclass_0[244];
int mSize;
std::vector<ItemStack> mItems;
};

```
#### SimplexNoise
```cpp
/* 34414 */
struct SimplexNoise
{
Vec3 mOrigin;
int mNoiseMap[512];
};

```
#### SkinAdjustments
```cpp
/* 88757 */
struct SkinAdjustments
{
unsigned int mAnimOverrideBitmask;
};

```
#### SkinData
```cpp
/* 44370 */
struct SkinData
{
std::optional<int> mVariant;
std::optional<int> mMarkVariant;
};

```
#### SkinHash
```cpp
/* 171257 */
struct SkinHash
{
size_t geoLength;
uint64_t shaData[8];
};

```
#### SkinInfoData
```cpp
/* 173189 */
struct SkinInfoData
{
int (**_vptr$SkinInfoData)(void);
std::string mDefaultMeshName;
bool mIsAlphaTest;
bool mIsDirty;
SerializedSkin mSkin;
};

```
#### SlabBlockItem::_useOn::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 227140 */
struct SlabBlockItem::_useOn::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SlotDescriptor
```cpp
/* 100018 */
struct SlotDescriptor
{
int mSlot;
std::vector<ItemInstance> mAcceptedItems;
const Item *mItem;
std::string mInteractText;
DefinitionTrigger mOnEquip;
DefinitionTrigger mOnUnequip;
};

```
#### SlotDropChance
```cpp
/* 89150 */
struct SlotDropChance
{
EquipmentSlot mSlot;
float mDropChance;
};

```
#### SmallSet<Actor *>
```cpp
/* 88055 */
struct SmallSet<Actor *>
{
std::vector<Actor *> c;
};

```
#### SmallSet<ActorUniqueID>
```cpp
/* 238400 */
struct SmallSet<ActorUniqueID>
{
std::vector<ActorUniqueID> c;
};

```
#### SmallSet<DBChunkStorage *>
```cpp
/* 462662 */
struct SmallSet<DBChunkStorage *>
{
std::vector<DBChunkStorage *> c;
};

```
#### SmallSet<WorkerPool *>
```cpp
/* 81991 */
struct SmallSet<WorkerPool *>
{
std::vector<WorkerPool *> c;
};

```
#### SnapshotFilenameAndLength
```cpp
/* 6450 */
struct SnapshotFilenameAndLength
{
std::string filename;
uint64_t filesize;
};

```
#### Social::Events::IEventListener;
```cpp
/* 42828 */
struct Social::Events::IEventListener;

```
#### Social::Events::Measurement
```cpp
/* 43074 */
struct Social::Events::Measurement
{
std::string mName;
Json::Value mValue;
int mValueDivisorForAverage;
Social::Events::Measurement::AggregationType mType;
};

```
#### Social::Events::Property
```cpp
/* 42921 */
struct Social::Events::Property
{
std::string mName;
Json::Value mValue;
};

```
#### Social::GameConnectionInfo
```cpp
/* 63698 */
struct Social::GameConnectionInfo
{
Social::ConnectionType mType;
std::string mHostIpAddress;
std::string mUnresolvedUrl;
int mPort;
std::string mRakNetGUID;
ThirdPartyInfo mThirdPartyServerInfo;
};

```
#### Social::IUserManager;
```cpp
/* 44956 */
struct Social::IUserManager;

```
#### Social::MultiplayerService;
```cpp
/* 479541 */
struct Social::MultiplayerService;

```
#### Social::User;
```cpp
/* 44200 */
struct Social::User;

```
#### Social::UserPicturePath
```cpp
/* 44126 */
struct Social::UserPicturePath
{
std::shared_ptr<ResourceLocation> mLocation;
};

```
#### Social::XboxLiveUser;
```cpp
/* 45093 */
struct Social::XboxLiveUser;

```
#### SortItemInstanceIdAux
```cpp
/* 75857 */
struct SortItemInstanceIdAux
{
__int8 gap0[1];
};

```
#### SoundItem;
```cpp
/* 87050 */
struct SoundItem;

```
#### SoundPlayer;
```cpp
/* 86997 */
struct SoundPlayer;

```
#### SparklerItem::ColorInfo
```cpp
/* 457256 */
struct SparklerItem::ColorInfo
{
ItemColor mDyeId;
CompoundType mColorCompound;
int mVariantIndex;
int mRGB;
};

```
#### SpatialActorNetworkData
```cpp
/* 77504 */
struct SpatialActorNetworkData
{
Actor *mEntity;
bool mHasInitializedLastSent;
bool mAutoSend;
MoveActorAbsoluteData mLastSentMoveData;
MoveActorAbsoluteData mLastReceivedMoveData;
};

```
#### SpawnActorComponent
```cpp
/* 59118 */
struct SpawnActorComponent
{
std::vector<SpawnActorEntry> mSpawnEntries;
};

```
#### SpawnActorParameters
```cpp
/* 59072 */
struct SpawnActorParameters
{
bool mSpawnsItemStack;
int mSpawnTimeMin;
int mSpawnTimeMax;
int mSpawnTimer;
LevelSoundEvent mSpawnSound;
const Item *mItem;
std::string mEntityDefinition;
std::string mSpawnMethod;
ActorFilterGroup mFilters;
bool mSingleUse;
bool mShouldLeash;
int mNumToSpawn;
};

```
#### SpawnConditions
```cpp
/* 37046 */
struct SpawnConditions
{
bool isOnSurface;
bool isInWater;
bool isInLava;
bool isUnderground;
uint64_t delayEndWorldAge;
int rawBrightness;
BlockPos pos;
};

```
#### SpawnGroupData
```cpp
/* 190808 */
struct SpawnGroupData
{
std::string mIdentifier;
std::vector<MobSpawnRules> mSpawnRules;
};

```
#### SpecificEnchantFunction::EnchantInfo
```cpp
/* 291647 */
struct SpecificEnchantFunction::EnchantInfo
{
Enchant::Type enchantment;
int level;
};

```
#### SpikeFeature::EndSpike
```cpp
/* 255156 */
struct SpikeFeature::EndSpike
{
const int mCenterX;
const int mCenterZ;
const int mRadius;
const int mHeight;
const bool mGuarded;
const AABB mTopBoundingBox;
};

```
#### SpongeBlock::_spawnAbsorbParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 460015 */
struct SpongeBlock::_spawnAbsorbParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Squid::aiStep::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124436 */
struct Squid::aiStep::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Squid::spawnInkParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124435 */
struct Squid::spawnInkParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Squid::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124437 */
struct Squid::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### StackResultStorageEntity
```cpp
/* 13182 */
struct StackResultStorageEntity
{
std::optional<EntityContext> mContext;
};

```
#### StackResultStorageFeature
```cpp
/* 31083 */
struct StackResultStorageFeature
{
std::optional<std::reference_wrapper<FeatureRegistry> > mRegistry;
size_t mIndex;
};

```
#### StackResultStorageSharePtr<EntityRegistry>
```cpp
/* 13165 */
struct StackResultStorageSharePtr<EntityRegistry>
{
std::shared_ptr<EntityRegistry> mValue;
};

```
#### StackResultStorageSharePtr<PerlinSimplexNoise>
```cpp
/* 191531 */
struct StackResultStorageSharePtr<PerlinSimplexNoise>
{
std::shared_ptr<PerlinSimplexNoise> mValue;
};

```
#### StackStats
```cpp
/* 45335 */
struct StackStats
{
PackType mStackType;
uint32_t mPackCount;
double mParseTime;
};

```
#### StackedGraphBars::ColorKey
```cpp
/* 421771 */
struct StackedGraphBars::ColorKey
{
char colorTag;
std::string name;
};

```
#### StartGamePacket::write::$5498B64B1945F9BCA5158804213C50F5
```cpp
/* 80901 */
struct StartGamePacket::write::$5498B64B1945F9BCA5158804213C50F5
{
std::unique_ptr<ListTag> *blockPaletteList;
};

```
#### StateAnimationVariable
```cpp
/* 125167 */
struct StateAnimationVariable
{
HashedString mVariableName;
ExpressionNode mInput;
std::vector<AnimationValueCurveKeyFrame> mKeyFrames;
};

```
#### StateVectorComponent
```cpp
/* 45380 */
struct StateVectorComponent
{
Vec3 mPos;
Vec3 mPosPrev;
Vec3 mPosDelta;
};

```
#### Stopwatch
```cpp
/* 85830 */
struct Stopwatch
{
int (**_vptr$Stopwatch)(void);
double _st;
double _tt;
double _last;
double _max;
int _count;
int _printcounter;
};

```
#### StoreSearchTelemetryData;
```cpp
/* 45340 */
struct StoreSearchTelemetryData;

```
#### StrongholdFeature::StrongholdResult
```cpp
/* 42641 */
struct StrongholdFeature::StrongholdResult
{
bool success;
ChunkPos location;
};

```
#### StructureBlockPalette
```cpp
/* 77486 */
struct StructureBlockPalette
{
std::vector<std::unique_ptr<CompoundTag>> mStructurePaletteIdToSerializationId;
std::unordered_map<unsigned long,StructureBlockPalette::BlockPositionData> mBlockPositionData;
};

```
#### StructureBlockPalette::BlockPositionData
```cpp
/* 74447 */
struct StructureBlockPalette::BlockPositionData
{
std::unique_ptr<CompoundTag> mBlockEntityData;
std::vector<StructureBlockPalette::TickingQueueData> mTickData;
};

```
#### StructureBlockPalette::TickingQueueData
```cpp
/* 74460 */
struct StructureBlockPalette::TickingQueueData
{
int mTickDelay;
};

```
#### StructureEditorData
```cpp
/* 45347 */
struct StructureEditorData
{
std::string mStructureName;
std::string mDataField;
bool mIncludePlayers;
bool mShowBoundingBox;
StructureRedstoneSaveMode mRedstoneSaveMode;
StructureBlockType mType;
StructureSettings mSettings;
};

```
#### StructureEditorData_0
```cpp
/* 80908 */
struct StructureEditorData_0
{
std::string mStructureName;
std::string mDataField;
bool mIncludePlayers;
bool mShowBoundingBox;
StructureRedstoneSaveMode mRedstoneSaveMode;
StructureBlockType mType;
StructureSettings_0 mSettings;
};

```
#### StructureEditorData_1
```cpp
/* 238479 */
struct StructureEditorData_1
{
std::string mStructureName;
std::string mDataField;
bool mIncludePlayers;
bool mShowBoundingBox;
StructureRedstoneSaveMode mRedstoneSaveMode;
StructureBlockType mType;
StructureSettings_1 mSettings;
};

```
#### StructureFeature::findFarAwayStructures::StructureInfo
```cpp
/* 287709 */
struct StructureFeature::findFarAwayStructures::StructureInfo
{
ChunkPos min;
ChunkPos max;
ChunkPos id;
};

```
#### StructureHelpers
```cpp
/* 287770 */
struct StructureHelpers
{
__int8 gap0[1];
};

```
#### StructureIntegrityProcessor
```cpp
/* 288382 */
struct StructureIntegrityProcessor
{
float mIntegrity;
RandomSeed mStartSeed;
};

```
#### StructureIntegrityProcessor_0
```cpp
/* 462024 */
struct StructureIntegrityProcessor_0
{
float mIntegrity;
RandomSeed_0 mStartSeed;
};

```
#### StructureManager
```cpp
/* 32815 */
struct StructureManager
{
SharedMutex mRepositoryMutex;
std::unordered_map<std::string,std::unique_ptr<LegacyStructureTemplate>> mLegacyStructureRepository;
std::unordered_map<std::string,std::unique_ptr<StructureTemplate>> mStructureRepository;
LevelStorage *mLevelStorage;
ResourcePackManager *mPackManager;
};

```
#### StructurePiece
```cpp
/* 31308 */
struct StructurePiece
{
int (**_vptr$StructurePiece)(void);
BoundingBox mBoundingBox;
int mOrientation;
int mGenDepth;
};

```
#### StructurePoolActorRule
```cpp
/* 35465 */
struct StructurePoolActorRule
{
const Unique<IStructurePoolActorPredicate> mSourcePredicate;
const std::string mResultActor;
};

```
#### StructurePoolBlockRule
```cpp
/* 35649 */
struct StructurePoolBlockRule
{
const Unique<IStructurePoolBlockPredicate> mSourcePredicate;
const Unique<IStructurePoolBlockPredicate> mTargetPredicate;
const Block *mResultBlock;
};

```
#### StructurePoolBlockTagRule
```cpp
/* 35906 */
struct StructurePoolBlockTagRule
{
const Unique<IStructurePoolBlockTagPredicate> mSourcePredicate;
const std::string mResultKey;
const std::string mResultValue;
};

```
#### StructurePoolElement
```cpp
/* 31953 */
struct StructurePoolElement
{
int (**_vptr$StructurePoolElement)(void);
std::once_flag mTemplateOnceFlag;
std::optional<StructurePoolElement::LazyTemplate> mTemplate;
std::string mLocation;
StructureManager *mManager;
bool mValid;
Projection mProjection;
const StructurePoolBlockRuleList *mBlockRules;
const StructurePoolBlockTagRuleList *mBlockTagRules;
const StructurePoolActorRuleList *mActorRules;
};

```
#### StructurePoolElement::LazyTemplate
```cpp
/* 289311 */
struct StructurePoolElement::LazyTemplate
{
LegacyStructureTemplate *mStructure;
std::vector<JigsawBlockInfo> mJigsawMarkers;
};

```
#### StructureStart
```cpp
/* 38732 */
struct StructureStart
{
int (**_vptr$StructureStart)(void);
BoundingBox boundingBox;
int chunkX;
int chunkZ;
PieceList pieces;
};

```
#### StructureTelemetryClientData
```cpp
/* 45349 */
struct StructureTelemetryClientData
{
uint32_t mSizeEditCount;
uint32_t mOffsetEditCount;
uint32_t mRotationEditCount;
uint32_t mMirrorEditCount;
};

```
#### StructureTelemetryServerData
```cpp
/* 77485 */
struct StructureTelemetryServerData
{
bool mHasBeenActivatedByRedstone;
bool mHasLoadedIntoUnloadedChunks;
BlockPos mLastOffsetWhenLoadingIntoUnloadedChunks;
};

```
#### StructureTemplate
```cpp
/* 41934 */
struct StructureTemplate
{
std::string mName;
StructureTemplateData mStructureTemplateData;
};

```
#### StructureTemplate::_fillBlockInfo::$2FA47CEBC638377704193C5643AD3DC1
```cpp
/* 288378 */
struct StructureTemplate::_fillBlockInfo::$2FA47CEBC638377704193C5643AD3DC1
{
std::map<const Block *,int> *blockToIndex;
StructureBlockPalette *structureBlockPalette;
const Block *voidBlock;
};

```
#### StructureTemplateData
```cpp
/* 74503 */
struct StructureTemplateData
{
int (**_vptr$StructureTemplateData)(void);
int mFormatVersion;
BlockPos mSize;
BlockPos mStructureWorldOrigin;
std::vector<int> mBlockIndices;
std::vector<int> mExtraBlockIndices;
std::unordered_map<std::string,StructureBlockPalette> mPalettes;
std::vector<std::unique_ptr<CompoundTag>> mEntityData;
};

```
#### StructureTemplateFeature::BoundingBox2D
```cpp
/* 280104 */
struct StructureTemplateFeature::BoundingBox2D
{
Vec2 min;
Vec2 max;
};

```
#### StructureTemplatePool
```cpp
/* 32001 */
struct StructureTemplatePool
{
std::string mName;
std::vector<const StructurePoolElement *> mTemplates;
std::string mFallback;
};

```
#### SubChunk
```cpp
/* 35007 */
struct SubChunk
{
DirtyTicksCounter mDirtyTicksCounter;
std::unique_ptr<SubChunkBrightnessStorage> mLight;
std::unique_ptr<SubChunkBlockStorage> mBlocks[2];
SubChunkBlockStorage *mBlocksReadPtr[2];
SpinLock *mWriteLock;
};

```
#### SubChunkBlockPos
```cpp
/* 34732 */
struct SubChunkBlockPos
{
SubChunkBlockPos::$F507DBCC95B5F1F0349D6A6FBF2E560F _anon_0;
};

```
#### SubChunkBlockPos::$F507DBCC95B5F1F0349D6A6FBF2E560F::$E23C018BDD51DA9542B42FDC09D6AA49
```cpp
/* 34734 */
struct SubChunkBlockPos::$F507DBCC95B5F1F0349D6A6FBF2E560F::$E23C018BDD51DA9542B42FDC09D6AA49
{
uint8_t x;
uint8_t y;
uint8_t z;
};

```
#### SubChunkBlockStorage
```cpp
/* 33596 */
struct SubChunkBlockStorage
{
int (**_vptr$SubChunkBlockStorage)(void);
};

```
#### SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 253613 */
struct SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$242ED9D411BD064A57C4553B835CD0FE
```cpp
/* 253619 */
struct SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$242ED9D411BD064A57C4553B835CD0FE
{
const std::bitset<2> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$633D66453D3F5664A26EE59CDFD22959
```cpp
/* 253620 */
struct SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$633D66453D3F5664A26EE59CDFD22959
{
const std::bitset<2> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
```cpp
/* 253621 */
struct SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
{
uint16_t *max;
std::vector<unsigned short> *outOfBoundSlots;
size_t *idx;
};

```
#### SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
```cpp
/* 253617 */
struct SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
{
const BoundingBox *box;
};

```
#### SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
```cpp
/* 253616 */
struct SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
{
uint32_t height;
uint32_t radius;
const BlockPos *pos;
};

```
#### SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::findUsedIndices::$89D4AD7C0CE71E5C121270538A6F6D8C
```cpp
/* 253618 */
struct SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::findUsedIndices::$89D4AD7C0CE71E5C121270538A6F6D8C
{
std::bitset<2> *existing;
};

```
#### SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::makePrunedCopy::$5C37BA6189407DC409FF9D08D5F65A9E
```cpp
/* 253615 */
struct SubChunkBlockStoragePaletted<1,SubChunkBlockStorage::Type::Paletted1>::makePrunedCopy::$5C37BA6189407DC409FF9D08D5F65A9E
{
std::array<unsigned long,2> *remappingLookup;
};

```
#### SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 253670 */
struct SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$6F135F9B09AF7761430A35C180173A8C
```cpp
/* 253675 */
struct SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$6F135F9B09AF7761430A35C180173A8C
{
const std::bitset<4096> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$290B4DE2DB2BE431220A17F6F7E7C4F0
```cpp
/* 253676 */
struct SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$290B4DE2DB2BE431220A17F6F7E7C4F0
{
const std::bitset<4096> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
```cpp
/* 253677 */
struct SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
{
uint16_t *max;
std::vector<unsigned short> *outOfBoundSlots;
size_t *idx;
};

```
#### SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
```cpp
/* 253673 */
struct SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
{
const BoundingBox *box;
};

```
#### SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
```cpp
/* 253672 */
struct SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
{
uint32_t height;
uint32_t radius;
const BlockPos *pos;
};

```
#### SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::findUsedIndices::$6336BD0E2483FB0EFB3F76DC3EBC5309
```cpp
/* 253674 */
struct SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::findUsedIndices::$6336BD0E2483FB0EFB3F76DC3EBC5309
{
std::bitset<4096> *existing;
};

```
#### SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::makePrunedCopy::$2185D287A3144BABD0B238662BD24236
```cpp
/* 253671 */
struct SubChunkBlockStoragePaletted<16,SubChunkBlockStorage::Type::Paletted16>::makePrunedCopy::$2185D287A3144BABD0B238662BD24236
{
std::array<unsigned long,4096> *remappingLookup;
};

```
#### SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 253622 */
struct SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$66FA6D0B33FF0D79D1FAEF5E715B6A50
```cpp
/* 253627 */
struct SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$66FA6D0B33FF0D79D1FAEF5E715B6A50
{
const std::bitset<4> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$5D469001403E80B2A426E4718973955B
```cpp
/* 253628 */
struct SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$5D469001403E80B2A426E4718973955B
{
const std::bitset<4> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
```cpp
/* 253629 */
struct SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
{
uint16_t *max;
std::vector<unsigned short> *outOfBoundSlots;
size_t *idx;
};

```
#### SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
```cpp
/* 253625 */
struct SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
{
const BoundingBox *box;
};

```
#### SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
```cpp
/* 253624 */
struct SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
{
uint32_t height;
uint32_t radius;
const BlockPos *pos;
};

```
#### SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::findUsedIndices::$D3A89A71AD77E1A6A761C588139D92F8
```cpp
/* 253626 */
struct SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::findUsedIndices::$D3A89A71AD77E1A6A761C588139D92F8
{
std::bitset<4> *existing;
};

```
#### SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::makePrunedCopy::$97D49D667F65B59D64A1CF6C21EF1D86
```cpp
/* 253623 */
struct SubChunkBlockStoragePaletted<2,SubChunkBlockStorage::Type::Paletted2>::makePrunedCopy::$97D49D667F65B59D64A1CF6C21EF1D86
{
std::array<unsigned long,4> *remappingLookup;
};

```
#### SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 253630 */
struct SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$C26F408D3D152A4098209C2CE9387EF2
```cpp
/* 253635 */
struct SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$C26F408D3D152A4098209C2CE9387EF2
{
const std::bitset<8> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$09FE199C713A938B3B17002F6F47058A
```cpp
/* 253636 */
struct SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$09FE199C713A938B3B17002F6F47058A
{
const std::bitset<8> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
```cpp
/* 253637 */
struct SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
{
uint16_t *max;
std::vector<unsigned short> *outOfBoundSlots;
size_t *idx;
};

```
#### SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
```cpp
/* 253633 */
struct SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
{
const BoundingBox *box;
};

```
#### SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
```cpp
/* 253632 */
struct SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
{
uint32_t height;
uint32_t radius;
const BlockPos *pos;
};

```
#### SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::findUsedIndices::$5D1D4294B57C53DD4C7D10D4AE89381A
```cpp
/* 253634 */
struct SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::findUsedIndices::$5D1D4294B57C53DD4C7D10D4AE89381A
{
std::bitset<8> *existing;
};

```
#### SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::makePrunedCopy::$9D7F1A052824D1DF666118F69FC3070A
```cpp
/* 253631 */
struct SubChunkBlockStoragePaletted<3,SubChunkBlockStorage::Type::Paletted3>::makePrunedCopy::$9D7F1A052824D1DF666118F69FC3070A
{
std::array<unsigned long,8> *remappingLookup;
};

```
#### SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 253638 */
struct SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$4917742FCBCB7D234EAD1B5E3DA1DE4E
```cpp
/* 253643 */
struct SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$4917742FCBCB7D234EAD1B5E3DA1DE4E
{
const std::bitset<16> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$28E5234A30BDDE39C7BEB7FA929ADF5A
```cpp
/* 253644 */
struct SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$28E5234A30BDDE39C7BEB7FA929ADF5A
{
const std::bitset<16> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
```cpp
/* 253645 */
struct SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
{
uint16_t *max;
std::vector<unsigned short> *outOfBoundSlots;
size_t *idx;
};

```
#### SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
```cpp
/* 253641 */
struct SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
{
const BoundingBox *box;
};

```
#### SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
```cpp
/* 253640 */
struct SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
{
uint32_t height;
uint32_t radius;
const BlockPos *pos;
};

```
#### SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::findUsedIndices::$900FAD5FCE8D58777B797CA0B7FA2138
```cpp
/* 253642 */
struct SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::findUsedIndices::$900FAD5FCE8D58777B797CA0B7FA2138
{
std::bitset<16> *existing;
};

```
#### SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::makePrunedCopy::$05DA6B700FA0222B559606B9A00A1F7D
```cpp
/* 253639 */
struct SubChunkBlockStoragePaletted<4,SubChunkBlockStorage::Type::Paletted4>::makePrunedCopy::$05DA6B700FA0222B559606B9A00A1F7D
{
std::array<unsigned long,16> *remappingLookup;
};

```
#### SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 253646 */
struct SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$AAA3ED88E6F951360D315A860A822F3A
```cpp
/* 253651 */
struct SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$AAA3ED88E6F951360D315A860A822F3A
{
const std::bitset<32> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$ED58595EF437FEAFABE4C940374EA69A
```cpp
/* 253652 */
struct SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$ED58595EF437FEAFABE4C940374EA69A
{
const std::bitset<32> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
```cpp
/* 253653 */
struct SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
{
uint16_t *max;
std::vector<unsigned short> *outOfBoundSlots;
size_t *idx;
};

```
#### SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
```cpp
/* 253649 */
struct SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
{
const BoundingBox *box;
};

```
#### SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
```cpp
/* 253648 */
struct SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
{
uint32_t height;
uint32_t radius;
const BlockPos *pos;
};

```
#### SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::findUsedIndices::$C463AA8D3B7416B6EACBAB570E768265
```cpp
/* 253650 */
struct SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::findUsedIndices::$C463AA8D3B7416B6EACBAB570E768265
{
std::bitset<32> *existing;
};

```
#### SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::makePrunedCopy::$CC93A48B8F76E12549E857D7142C04AB
```cpp
/* 253647 */
struct SubChunkBlockStoragePaletted<5,SubChunkBlockStorage::Type::Paletted5>::makePrunedCopy::$CC93A48B8F76E12549E857D7142C04AB
{
std::array<unsigned long,32> *remappingLookup;
};

```
#### SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 253654 */
struct SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$B5E2A92EF98D0403FD7DBC5576FA3DFE
```cpp
/* 253659 */
struct SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$B5E2A92EF98D0403FD7DBC5576FA3DFE
{
const std::bitset<64> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$704CDF7438A6CF9DB4A498AA560B0A22
```cpp
/* 253660 */
struct SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$704CDF7438A6CF9DB4A498AA560B0A22
{
const std::bitset<64> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
```cpp
/* 253661 */
struct SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
{
uint16_t *max;
std::vector<unsigned short> *outOfBoundSlots;
size_t *idx;
};

```
#### SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
```cpp
/* 253657 */
struct SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
{
const BoundingBox *box;
};

```
#### SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
```cpp
/* 253656 */
struct SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
{
uint32_t height;
uint32_t radius;
const BlockPos *pos;
};

```
#### SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::findUsedIndices::$2990B7D608F6D64D2C15233EADEB07CB
```cpp
/* 253658 */
struct SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::findUsedIndices::$2990B7D608F6D64D2C15233EADEB07CB
{
std::bitset<64> *existing;
};

```
#### SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::makePrunedCopy::$B8D88B99E42BC318262126A78F11A7E5
```cpp
/* 253655 */
struct SubChunkBlockStoragePaletted<6,SubChunkBlockStorage::Type::Paletted6>::makePrunedCopy::$B8D88B99E42BC318262126A78F11A7E5
{
std::array<unsigned long,64> *remappingLookup;
};

```
#### SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 253662 */
struct SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::SubChunkBlockStoragePaletted::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$1AEE232A0E96F160F80275F43A812658
```cpp
/* 253667 */
struct SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:357:64)>::$1AEE232A0E96F160F80275F43A812658
{
const std::bitset<256> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$40981709DD800CB46A7EC240DF9DEAFC
```cpp
/* 253668 */
struct SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::_fetchBlocksInShape<(lambda at _Minecraftpe_handheld_src_common_world_level_chunk_SubChunkBlockStoragePaletted_h:371:67)>::$40981709DD800CB46A7EC240DF9DEAFC
{
const std::bitset<256> *indices;
const BlockPos *positionOfChunk;
const BlockPos *pos;
uint16_t *index;
const buffer_span<const Block *> *palette;
std::vector<BlockFetchResult> *output;
const SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC *shapePredicate;
};

```
#### SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
```cpp
/* 253669 */
struct SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::_zeroIndicesGreaterEqualThan::$BF7C779BDE86076AE2754C92A6BC7645
{
uint16_t *max;
std::vector<unsigned short> *outOfBoundSlots;
size_t *idx;
};

```
#### SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
```cpp
/* 253665 */
struct SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::fetchBlocksInBox::$C6B2610503636021CCB9EBE3476F26BC
{
const BoundingBox *box;
};

```
#### SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
```cpp
/* 253664 */
struct SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::fetchBlocksInCylinder::$40F19BD02D6D15FED988956B86A67BFC
{
uint32_t height;
uint32_t radius;
const BlockPos *pos;
};

```
#### SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::findUsedIndices::$34AB7F28A08EB8CC59CD205CAB614B75
```cpp
/* 253666 */
struct SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::findUsedIndices::$34AB7F28A08EB8CC59CD205CAB614B75
{
std::bitset<256> *existing;
};

```
#### SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::makePrunedCopy::$3817DFAD228892A6745DC344E6C4662F
```cpp
/* 253663 */
struct SubChunkBlockStoragePaletted<8,SubChunkBlockStorage::Type::Paletted8>::makePrunedCopy::$3817DFAD228892A6745DC344E6C4662F
{
std::array<unsigned long,256> *remappingLookup;
};

```
#### SubChunkBrightnessStorage
```cpp
/* 33558 */
struct SubChunkBrightnessStorage
{
std::array<SubChunkBrightnessStorage::LightPair,4096> mLight;
};

```
#### SubChunkBrightnessStorage::LightPair
```cpp
/* 33561 */
struct SubChunkBrightnessStorage::LightPair
{
SubChunkBrightnessStorage::LightPair::$C82CAE701F9C96804622E94D041F6011 _anon_0;
};

```
#### SubChunkBrightnessStorage::LightPair::$C82CAE701F9C96804622E94D041F6011::$FEA8D14758525B4BCA5C0100E71C9EA7
```cpp
/* 33563 */
struct SubChunkBrightnessStorage::LightPair::$C82CAE701F9C96804622E94D041F6011::$FEA8D14758525B4BCA5C0100E71C9EA7
{
unsigned __int8 blockLight : 4;
unsigned __int8 skyLight : 4;
};

```
#### SubChunkLightIndex
```cpp
/* 252527 */
struct SubChunkLightIndex
{
SubChunkLightIndex::$D642419CEF3A4ECC892D938F72F5EEEF _anon_0;
};

```
#### SubChunkLightIndex::$D642419CEF3A4ECC892D938F72F5EEEF::$1B14A3B4ACC00D53AE1F0B03F21ED5AD
```cpp
/* 252530 */
struct SubChunkLightIndex::$D642419CEF3A4ECC892D938F72F5EEEF::$1B14A3B4ACC00D53AE1F0B03F21ED5AD
{
unsigned __int32 mToDoIndex : 18;
unsigned __int32 mPad2 : 14;
};

```
#### SubChunkLightIndex::$D642419CEF3A4ECC892D938F72F5EEEF::$C5E0CE72C99D254AFB51B3E72BF5B343
```cpp
/* 252529 */
struct SubChunkLightIndex::$D642419CEF3A4ECC892D938F72F5EEEF::$C5E0CE72C99D254AFB51B3E72BF5B343
{
unsigned __int32 mSubChunkBlockY : 4;
unsigned __int32 mChunkIndexY : 2;
unsigned __int32 mSubChunkBlockZ : 4;
unsigned __int32 mChunkIndexZ : 2;
unsigned __int32 mSubChunkBlockX : 4;
unsigned __int32 mChunkIndexX : 2;
unsigned __int32 mPad : 8;
};

```
#### SubChunkRelighter
```cpp
/* 252862 */
struct SubChunkRelighter
{
bool mNeedToResetToDoBits;
std::bitset<196608> mToDo;
std::array<unsigned char,4096> mOldAbsorption;
std::vector<SubChunkLightIndex> mAdditiveBlocksToProcess[2][16];
std::vector<SubChunkLightIndex> mEdgeBlocksToProcess[16];
std::vector<SubChunkLightIndex> mBlocksToProcess[16];
std::vector<SubChunkLightIndex> mAbsorptionBlocksToProcess;
std::vector<SubtractiveLightInfo> mSubtractiveBlocks[2];
SubChunk *mSubChunkPtrArray[3][4][4];
bool mSubChunkPtrArrayValid[3][4][4];
bool mSubChunkTouched[3][4][4];
ChunkPos mCenterChunkPos;
size_t mCenterSubChunkIndex;
BlockSource *mSource;
bool mOriginalLighting;
SubChunkRelighter::LightPair mDefaultLightPair;
const Block *mDefaultBlock;
};

```
#### SubChunkStorageFormat::$4A48E9E2C062D44B94D66378C25E9D86
```cpp
/* 253612 */
struct SubChunkStorageFormat::$4A48E9E2C062D44B94D66378C25E9D86
{
__int8 network : 1;
__int8 type : 7;
};

```
#### SubClientConnectionRequest
```cpp
/* 73929 */
struct SubClientConnectionRequest
{
Unique<UnverifiedCertificate> mCertificateData;
Unique<Certificate> mCertificate;
Unique<WebToken> mRawToken;
};

```
#### SubpackInfoCollection
```cpp
/* 5712 */
struct SubpackInfoCollection
{
std::vector<SubpackInfo> mSubpackInfo;
};

```
#### SubtractiveLightInfo
```cpp
/* 252566 */
struct SubtractiveLightInfo
{
SubtractiveLightInfo::$6B0E6A960ECE12370BB5BB4D4B3FBF4C _anon_0;
};

```
#### SubtreeDefinition::load::$2A59718DDDE9B252D2E2D9E1042A23A6
```cpp
/* 454213 */
struct SubtreeDefinition::load::$2A59718DDDE9B252D2E2D9E1042A23A6
{
SubtreeDefinition *this;
};

```
#### SurfaceBuilderComponent
```cpp
/* 190841 */
struct SurfaceBuilderComponent
{
ISurfaceBuilder *mSurfaceBuilder;
};

```
#### SurfaceBuilderRegistry
```cpp
/* 88421 */
struct SurfaceBuilderRegistry
{
std::vector<SurfaceBuilderRegistry::Element> mSurfaceBuilders;
};

```
#### SurfaceBuilderRegistry::Element
```cpp
/* 88434 */
struct SurfaceBuilderRegistry::Element
{
std::unique_ptr<ISurfaceBuilder> mBuilder;
SurfaceBuilderRegistry::ScoringFunc mScoringFunc;
};

```
#### SurfaceMaterialAdjustmentAttributes
```cpp
/* 193919 */
struct SurfaceMaterialAdjustmentAttributes
{
std::vector<SurfaceMaterialAdjustmentAttributes::Element> mAdjustments;
};

```
#### SurfaceMaterialAdjustmentAttributes::Element
```cpp
/* 193031 */
struct SurfaceMaterialAdjustmentAttributes::Element
{
float mLowerBound;
float mUpperBound;
SurfaceMaterialAttributes mAdjustedMaterials;
};

```
#### SwampBiomeSurface;
```cpp
/* 198711 */
struct SwampBiomeSurface;

```
