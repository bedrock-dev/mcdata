#### CSHA1
```cpp
/* 478096 */
struct CSHA1
{
unsigned int m_state[5];
unsigned int m_count[2];
unsigned int m_reserved0[1];
unsigned __int8 m_buffer[64];
unsigned __int8 m_digest[20];
unsigned int m_reserved1[3];
unsigned __int8 m_workspace[64];
SHA1_WORKSPACE_BLOCK *m_block;
};

```
#### CameraCallbacks;
```cpp
/* 457056 */
struct CameraCallbacks;

```
#### CameraItemComponent
```cpp
/* 180676 */
struct CameraItemComponent
{
int (**_vptr$CameraItemComponent)(void);
float mBlackBarsDuration;
float mBlackBarsScreenRatio;
float mShutterScreenRatio;
float mShutterDuration;
float mPictureDuration;
float mSlideAwayDuration;
bool mPlacingTripod;
uint64_t mPlacingTripodClientTick;
uint64_t mPlacingTripodServerTick;
CameraCallbacks *mCallbacks;
};

```
#### Cat::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124057 */
struct Cat::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### CauldronBlock::spawnPotionParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 226316 */
struct CauldronBlock::spawnPotionParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### CauldronBlock::spawnSplashParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 226317 */
struct CauldronBlock::spawnSplashParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### ChangeDimensionRequest
```cpp
/* 89834 */
struct ChangeDimensionRequest
{
ChangeDimensionRequest::State mState;
DimensionType mFromDimensionId;
DimensionType mToDimensionId;
Vec3 mPosition;
bool mUsePortal;
bool mRespawn;
Unique<CompoundTag> mAgentTag;
};

```
#### ChannelTransform
```cpp
/* 124574 */
struct ChannelTransform
{
ExpressionNode mXYZ[3];
Vec3 mAxis;
ChannelTransformAxisType mTransformDataType;
};

```
#### ChemistryIngredient
```cpp
/* 456240 */
struct ChemistryIngredient
{
ItemInstance mItem;
};

```
#### ChemistryRecipes
```cpp
/* 457266 */
struct ChemistryRecipes
{
__int8 gap0[1];
};

```
#### Chicken::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124065 */
struct Chicken::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### ChunkBlockPos
```cpp
/* 33813 */
struct ChunkBlockPos
{
uint8_t x;
uint8_t z;
Height y;
};

```
#### ChunkBuildOrderPolicyBase
```cpp
/* 34799 */
struct ChunkBuildOrderPolicyBase
{
int (**_vptr$ChunkBuildOrderPolicyBase)(void);
};

```
#### ChunkPos
```cpp
/* 5799 */
struct ChunkPos
{
ChunkPos::$9F8988CC0F9198BEB3D9C07F7FC1F2E7 _anon_0;
};

```
#### ChunkPos::$9F8988CC0F9198BEB3D9C07F7FC1F2E7::$71D3E18752AF5CECAE552A00ECF6483C
```cpp
/* 5801 */
struct ChunkPos::$9F8988CC0F9198BEB3D9C07F7FC1F2E7::$71D3E18752AF5CECAE552A00ECF6483C
{
int x;
int z;
};

```
#### ChunkSource
```cpp
/* 34214 */
struct ChunkSource
{
int (**_vptr$ChunkSource)(void);
int mChunkSide;
Level *mLevel;
Dimension *mDimension;
ChunkSource *mParent;
Unique<ChunkSource> mOwnedParent;
LevelChunkBuilderData *mLevelChunkBuilderData;
};

```
#### CircuitComponentList
```cpp
/* 34454 */
struct CircuitComponentList
{
std::vector<CircuitComponentList::Item> mComponents;
};

```
#### CircuitComponentList::Item
```cpp
/* 34467 */
struct CircuitComponentList::Item
{
BaseCircuitComponent *mComponent;
int mDampening;
BlockPos mPos;
FacingID mDirection;
bool mDirectlyPowered;
int mData;
};

```
#### CircuitSceneGraph
```cpp
/* 34425 */
struct CircuitSceneGraph
{
CircuitSceneGraph::ComponentMap mAllComponents;
CircuitComponentList mActiveComponents;
CircuitSceneGraph::ComponentsPerPosMap mActiveComponentsPerChunk;
CircuitSceneGraph::ComponentsPerPosMap mPowerAssociationMap;
std::unordered_map<BlockPos,CircuitSceneGraph::PendingEntry> mPendingAdds;
std::unordered_map<BlockPos,CircuitSceneGraph::PendingEntry> mPendingUpdates;
std::unordered_map<BlockPos,std::vector<BlockPos>> mComponentsToReEvaluate;
std::vector<CircuitSceneGraph::PendingEntry> mPendingRemoves;
};

```
#### CircuitSystem::LevelChunkTracking
```cpp
/* 34569 */
struct CircuitSystem::LevelChunkTracking
{
BlockPos mChunkPos;
};

```
#### CircuitTrackingInfo::Entry
```cpp
/* 292130 */
struct CircuitTrackingInfo::Entry
{
BaseCircuitComponent *mComponent;
BlockPos mPos;
FacingID mDirection;
uint64_t mTypeID;
};

```
#### ClacksServer::ExecutionAndResult
```cpp
/* 7501 */
struct ClacksServer::ExecutionAndResult
{
ResetEventObj execution;
grpc::Status error;
};

```
#### ClassID
```cpp
/* 40727 */
struct ClassID
{
__int8 gap0[1];
};

```
#### ClientBlobCache::Server::ActiveTransfer
```cpp
/* 73674 */
struct ClientBlobCache::Server::ActiveTransfer
{
ClientBlobCache::Server::ActiveTransfersManager *mCache;
NetworkIdentifier mOwner;
std::unordered_map<unsigned long,std::shared_ptr<ClientBlobCache::Server::Blob>> mIdsWaitingForACK;
};

```
#### ClientBlobCache::Server::ActiveTransfersManager
```cpp
/* 73628 */
struct ClientBlobCache::Server::ActiveTransfersManager
{
std::unordered_map<NetworkIdentifier,std::unique_ptr<ClientBlobCache::Server::ActiveTransfersManager::TransferTracker>> mTransferTrackerMap;
ClientBlobCache::Server::ActiveTransfersManager::CacheMap mSentBlobs;
size_t mCacheSizeBytes;
};

```
#### ClientBlobCache::Server::Blob
```cpp
/* 68463 */
struct ClientBlobCache::Server::Blob
{
const ClientBlobCache::BlobId id;
const std::string data;
};

```
#### ClientBlobCache::Server::TransferBuilder
```cpp
/* 77424 */
struct ClientBlobCache::Server::TransferBuilder
{
ClientBlobCache::Server::ActiveTransfer mTransfer;
};

```
#### ClimateAttributes
```cpp
/* 193499 */
struct ClimateAttributes
{
float mTemperature;
float mDownfall;
float mSnowAccumulationMin;
float mSnowAccumulationMax;
};

```
#### ClockSpriteCalculator
```cpp
/* 88760 */
struct ClockSpriteCalculator
{
int mFrame;
float mRot;
float mRotA;
};

```
#### CloneCommand::execute::CloneBlockInfo
```cpp
/* 424868 */
struct CloneCommand::execute::CloneBlockInfo
{
BlockPos mPos;
const Block *mState;
std::unique_ptr<CompoundTag> mTag;
};

```
#### Color
```cpp
/* 33169 */
struct Color
{
float r;
float g;
float b;
float a;
};

```
#### ColorPaletteAttributes
```cpp
/* 191006 */
struct ColorPaletteAttributes
{
std::string mPaletteName;
};

```
#### ColumnCachedData
```cpp
/* 33669 */
struct ColumnCachedData
{
int grassColor;
int waterColor;
};

```
#### CommandArea
```cpp
/* 90986 */
struct CommandArea
{
std::unique_ptr<ChunkViewSource> mChunkSource;
BlockSource mBlockSource;
};

```
#### CommandAreaFactory
```cpp
/* 91477 */
struct CommandAreaFactory
{
Dimension *mDimension;
};

```
#### CommandBlock::_executeChain::$8760BA774438E6A855C8C1CB8DE2843F
```cpp
/* 459308 */
struct CommandBlock::_executeChain::$8760BA774438E6A855C8C1CB8DE2843F
{
const CommandBlock *this;
};

```
#### CommandFilePath
```cpp
/* 90965 */
struct CommandFilePath
{
std::string mText;
};

```
#### CommandFlag
```cpp
/* 1614 */
struct CommandFlag
{
uint8_t flag;
};

```
#### CommandItem
```cpp
/* 90962 */
struct CommandItem
{
int mVersion;
int mId;
};

```
#### CommandLexer
```cpp
/* 5665 */
struct CommandLexer
{
const std::string *mInput;
CommandLexer::Token mToken;
};

```
#### CommandLexer::Token
```cpp
/* 5666 */
struct CommandLexer::Token
{
const char *text;
uint32_t length;
CommandLexer::TokenType type;
};

```
#### CommandMessage
```cpp
/* 6364 */
struct CommandMessage
{
std::vector<CommandMessage::MessageComponent> mData;
};

```
#### CommandMessage::MessageComponent
```cpp
/* 6331 */
struct CommandMessage::MessageComponent
{
std::string string;
std::unique_ptr<CommandSelector<Actor>> selection;
};

```
#### CommandOrigin
```cpp
/* 1616 */
struct CommandOrigin
{
int (**_vptr$CommandOrigin)(void);
mce::UUID mUUID;
};

```
#### CommandOriginData
```cpp
/* 78833 */
struct CommandOriginData
{
CommandOriginType mType;
mce::UUID mUUID;
std::string mRequestId;
int64_t mPlayerId;
};

```
#### CommandOutputMessage
```cpp
/* 6083 */
struct CommandOutputMessage
{
CommandOutputMessageType mType;
std::string mMessageId;
std::vector<std::string> mParams;
};

```
#### CommandOutputParameter::CommandOutputParameter::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 91536 */
struct CommandOutputParameter::CommandOutputParameter::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### CommandOutputSender
```cpp
/* 4443 */
struct CommandOutputSender
{
int (**_vptr$CommandOutputSender)(void);
Automation::AutomationClient *mAutomationClient;
std::function<void (AutomationCmdOutput &)> mEmplaceTestCommandOutputCallback;
};

```
#### CommandPosition
```cpp
/* 33044 */
struct CommandPosition
{
Vec3 mOffset;
bool mRelativeX;
bool mRelativeY;
bool mRelativeZ;
bool mLocal;
};

```
#### CommandRawText
```cpp
/* 90960 */
struct CommandRawText
{
std::string mText;
};

```
#### CommandRegistry
```cpp
/* 1503 */
struct CommandRegistry
{
std::function<void (const Packet &)> mNetworkUpdateCallback;
CommandRegistry::ScoreboardScoreAccessor mGetScoreForObjective;
std::vector<CommandRegistry::ParseRule> mRules;
CommandRegistry::ParseTableMap mParseTables;
std::vector<CommandRegistry::OptionalParameterChain> mOptionals;
std::vector<std::string> mEnumValues;
std::vector<CommandRegistry::Enum> mEnums;
std::vector<CommandRegistry::Factorization> mFactorizations;
std::vector<std::string> mPostfixes;
std::map<std::string,unsigned int> mEnumLookup;
std::map<std::string,unsigned long> mEnumValueLookup;
std::vector<CommandRegistry::Symbol> mCommandSymbols;
std::map<std::string,CommandRegistry::Signature> mSignatures;
std::map<typeid_t<CommandRegistry>,int> mTypeLookup;
std::map<std::string,std::string> mAliases;
std::vector<SemanticConstraint> mSemanticConstraints;
std::map<SemanticConstraint,unsigned char> mSemanticConstraintLookup;
std::vector<CommandRegistry::ConstrainedValue> mConstrainedValues;
std::map<std::pair<unsigned long,unsigned int>,unsigned int> mConstrainedValueLookup;
std::vector<CommandRegistry::SoftEnum> mSoftEnums;
std::map<std::string,unsigned int> mSoftEnumLookup;
std::vector<CommandRegistry::RegistryState> mStateStack;
CommandRegistry::ParamSymbols mArgs;
CommandRegistry::CommandOverrideFunctor mCommandOverrideFunctor;
};

```
#### CommandRegistry::ConstrainedValue
```cpp
/* 1567 */
struct CommandRegistry::ConstrainedValue
{
CommandRegistry::Symbol mValue;
CommandRegistry::Symbol mEnum;
std::vector<unsigned char> mConstraints;
};

```
#### CommandRegistry::DefaultIdConverter<AgentCommand::Mode>
```cpp
/* 476454 */
struct CommandRegistry::DefaultIdConverter<AgentCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<AgentCommands::CollectCommand::CollectionSpecification>
```cpp
/* 476455 */
struct CommandRegistry::DefaultIdConverter<AgentCommands::CollectCommand::CollectionSpecification>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<AgentCommands::Direction>
```cpp
/* 476453 */
struct CommandRegistry::DefaultIdConverter<AgentCommands::Direction>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<BlockSlot>
```cpp
/* 426570 */
struct CommandRegistry::DefaultIdConverter<BlockSlot>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<ChangeSettingCommand::Setting>
```cpp
/* 6284 */
struct CommandRegistry::DefaultIdConverter<ChangeSettingCommand::Setting>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<CloneCommand::CloneMode>
```cpp
/* 424974 */
struct CommandRegistry::DefaultIdConverter<CloneCommand::CloneMode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<CloneCommand::MaskMode>
```cpp
/* 424973 */
struct CommandRegistry::DefaultIdConverter<CloneCommand::MaskMode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<CommandItem>
```cpp
/* 93242 */
struct CommandRegistry::DefaultIdConverter<CommandItem>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<Difficulty>
```cpp
/* 425122 */
struct CommandRegistry::DefaultIdConverter<Difficulty>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<EffectCommand::Mode>
```cpp
/* 425322 */
struct CommandRegistry::DefaultIdConverter<EffectCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<Enchant::Type>
```cpp
/* 94436 */
struct CommandRegistry::DefaultIdConverter<Enchant::Type>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<EquipmentSlot>
```cpp
/* 426571 */
struct CommandRegistry::DefaultIdConverter<EquipmentSlot>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<ExecuteCommand::Mode>
```cpp
/* 425418 */
struct CommandRegistry::DefaultIdConverter<ExecuteCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<FillCommand::FillMode>
```cpp
/* 425513 */
struct CommandRegistry::DefaultIdConverter<FillCommand::FillMode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<GameType>
```cpp
/* 93243 */
struct CommandRegistry::DefaultIdConverter<GameType>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<ListDCommand::DetailMode>
```cpp
/* 425967 */
struct CommandRegistry::DefaultIdConverter<ListDCommand::DetailMode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<ObjectiveSortOrder>
```cpp
/* 426875 */
struct CommandRegistry::DefaultIdConverter<ObjectiveSortOrder>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<PermissionCommand::Action>
```cpp
/* 426289 */
struct CommandRegistry::DefaultIdConverter<PermissionCommand::Action>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<PermissionCommand::AvailableCommandPermissionPresets>
```cpp
/* 426290 */
struct CommandRegistry::DefaultIdConverter<PermissionCommand::AvailableCommandPermissionPresets>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<ReplaceItemCommand::TargetType>
```cpp
/* 426572 */
struct CommandRegistry::DefaultIdConverter<ReplaceItemCommand::TargetType>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<SaveCommand::Mode>
```cpp
/* 6637 */
struct CommandRegistry::DefaultIdConverter<SaveCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<ScoreboardCommand::Action>
```cpp
/* 426874 */
struct CommandRegistry::DefaultIdConverter<ScoreboardCommand::Action>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<ScoreboardCommand::Category>
```cpp
/* 426873 */
struct CommandRegistry::DefaultIdConverter<ScoreboardCommand::Category>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<SetBlockCommand::SetBlockMode>
```cpp
/* 426971 */
struct CommandRegistry::DefaultIdConverter<SetBlockCommand::SetBlockMode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<StructureFeatureType>
```cpp
/* 94435 */
struct CommandRegistry::DefaultIdConverter<StructureFeatureType>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TagCommand::Action>
```cpp
/* 427377 */
struct CommandRegistry::DefaultIdConverter<TagCommand::Action>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TeleportCommand::FacingResult>
```cpp
/* 427474 */
struct CommandRegistry::DefaultIdConverter<TeleportCommand::FacingResult>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TestForBlocksCommand::Mode>
```cpp
/* 427659 */
struct CommandRegistry::DefaultIdConverter<TestForBlocksCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TickingAreaCommand::AddAreaType>
```cpp
/* 427930 */
struct CommandRegistry::DefaultIdConverter<TickingAreaCommand::AddAreaType>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TickingAreaCommand::Mode>
```cpp
/* 427929 */
struct CommandRegistry::DefaultIdConverter<TickingAreaCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TickingAreaCommand::TargetDimensions>
```cpp
/* 427931 */
struct CommandRegistry::DefaultIdConverter<TickingAreaCommand::TargetDimensions>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TimeCommand::Mode>
```cpp
/* 428127 */
struct CommandRegistry::DefaultIdConverter<TimeCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TimeCommand::Query>
```cpp
/* 428128 */
struct CommandRegistry::DefaultIdConverter<TimeCommand::Query>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TimeCommand::TimeSpec>
```cpp
/* 428129 */
struct CommandRegistry::DefaultIdConverter<TimeCommand::TimeSpec>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TitleCommand::Mode>
```cpp
/* 428284 */
struct CommandRegistry::DefaultIdConverter<TitleCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TitleRawCommand::Mode>
```cpp
/* 428379 */
struct CommandRegistry::DefaultIdConverter<TitleRawCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<VideoStreamConnectPacket::Action>
```cpp
/* 428495 */
struct CommandRegistry::DefaultIdConverter<VideoStreamConnectPacket::Action>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<WeatherCommand::WeatherRequest>
```cpp
/* 428676 */
struct CommandRegistry::DefaultIdConverter<WeatherCommand::WeatherRequest>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<WeatherCommand::WeatherType>
```cpp
/* 428675 */
struct CommandRegistry::DefaultIdConverter<WeatherCommand::WeatherType>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<WhitelistCommand::Action>
```cpp
/* 6816 */
struct CommandRegistry::DefaultIdConverter<WhitelistCommand::Action>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<bool>
```cpp
/* 93244 */
struct CommandRegistry::DefaultIdConverter<bool>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<const ActorDefinitionIdentifier *>
```cpp
/* 94434 */
struct CommandRegistry::DefaultIdConverter<const ActorDefinitionIdentifier *>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<const Block *>
```cpp
/* 93246 */
struct CommandRegistry::DefaultIdConverter<const Block *>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<const MobEffect *>
```cpp
/* 425323 */
struct CommandRegistry::DefaultIdConverter<const MobEffect *>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<int>
```cpp
/* 93245 */
struct CommandRegistry::DefaultIdConverter<int>
{
__int8 gap0[1];
};

```
#### CommandRegistry::Enum
```cpp
/* 1203 */
struct CommandRegistry::Enum
{
std::string name;
typeid_t<CommandRegistry> type;
CommandRegistry::ParseFunction parse;
_BYTE gap30[8];
std::vector<std::pair<unsigned long,unsigned long>> values;
};

```
#### CommandRegistry::Factorization
```cpp
/* 1239 */
struct CommandRegistry::Factorization
{
CommandRegistry::Terminal commandSymbol;
};

```
#### CommandRegistry::LexicalToken
```cpp
/* 49176 */
struct CommandRegistry::LexicalToken
{
const char *mText;
uint32_t mLength;
CommandRegistry::Terminal mType;
CommandRegistry::Terminal mIdentifierInfo;
const CommandRegistry *mRegistry;
};

```
#### CommandRegistry::OptionalParameterChain
```cpp
/* 1167 */
struct CommandRegistry::OptionalParameterChain
{
int parameterCount;
CommandRegistry::RuleIndex followingRuleIndex;
CommandRegistry::Symbol paramSymbol;
};

```
#### CommandRegistry::ParamSymbols
```cpp
/* 1607 */
struct CommandRegistry::ParamSymbols
{
CommandRegistry::Terminal x;
CommandRegistry::Terminal y;
CommandRegistry::Terminal z;
CommandRegistry::Terminal dx;
CommandRegistry::Terminal dy;
CommandRegistry::Terminal dz;
CommandRegistry::Terminal r;
CommandRegistry::Terminal rm;
CommandRegistry::Terminal rx;
CommandRegistry::Terminal rxm;
CommandRegistry::Terminal ry;
CommandRegistry::Terminal rym;
CommandRegistry::Terminal l;
CommandRegistry::Terminal lm;
CommandRegistry::Terminal c;
CommandRegistry::Terminal m;
CommandRegistry::Terminal name;
CommandRegistry::Terminal type;
CommandRegistry::Terminal score;
CommandRegistry::Terminal tag;
};

```
#### CommandRegistry::ParseRule
```cpp
/* 1071 */
struct CommandRegistry::ParseRule
{
CommandRegistry::NonTerminal nonTerminal;
CommandRegistry::ProcessFunction process;
CommandRegistry::SymbolVector derivation;
CommandVersion versions;
};

```
#### CommandRegistry::ParseTable
```cpp
/* 1125 */
struct CommandRegistry::ParseTable
{
CommandRegistry::ParseSet first;
CommandRegistry::ParseSet follow;
CommandRegistry::PredictTable predict;
};

```
#### CommandRegistry::ParseToken
```cpp
/* 1615 */
struct CommandRegistry::ParseToken
{
std::unique_ptr<CommandRegistry::ParseToken> child;
std::unique_ptr<CommandRegistry::ParseToken> next;
CommandRegistry::ParseToken *parent;
const char *text;
uint32_t length;
CommandRegistry::Symbol type;
};

```
#### CommandRegistry::RegistryState
```cpp
/* 1606 */
struct CommandRegistry::RegistryState
{
uint32_t signatureCount;
uint32_t enumValueCount;
uint32_t postfixCount;
uint32_t enumCount;
uint32_t factorizationCount;
uint32_t optionalCount;
uint32_t ruleCount;
uint32_t softEnumCount;
uint32_t constraintCount;
std::vector<unsigned int> constrainedValueCount;
std::vector<unsigned int> softEnumValuesCount;
};

```
#### CommandRegistry::SemanticInfo
```cpp
/* 5676 */
struct CommandRegistry::SemanticInfo
{
bool mIsValid;
std::vector<CommandRegistry::Symbol> mConstrainedParams;
std::string mSoftEnumText;
std::string mSoftEnumEscapeCharExceptions;
std::set<CommandRegistry::Symbol> mAlreadyCompletedSymbols;
};

```
#### CommandRegistry::SoftEnum
```cpp
/* 1593 */
struct CommandRegistry::SoftEnum
{
std::string mName;
std::vector<std::string> mValues;
};

```
#### CommandRegistry::Symbol
```cpp
/* 1407 */
struct CommandRegistry::Symbol
{
int mValue;
};

```
#### CommandSelectorResults<Actor>
```cpp
/* 6316 */
struct CommandSelectorResults<Actor>
{
CommandResultVector mTargets;
};

```
#### CommandSelectorResults<Player>
```cpp
/* 6317 */
struct CommandSelectorResults<Player>
{
CommandResultVector mTargets;
};

```
#### CommandSoftEnumRegistry
```cpp
/* 88496 */
struct CommandSoftEnumRegistry
{
CommandRegistry *mRegistry;
};

```
#### CommandSyntaxInformation
```cpp
/* 5681 */
struct CommandSyntaxInformation
{
bool isValid;
std::string description;
std::vector<OverloadSyntaxInformation> possibilities;
};

```
#### CommandVersion
```cpp
/* 1476 */
struct CommandVersion
{
int mFrom;
int mTo;
};

```
#### CommandWildcardInt
```cpp
/* 90963 */
struct CommandWildcardInt
{
bool mIsWildcard;
int mValue;
};

```
#### ComparatorCapacitor
```cpp
/* 237970 */
struct ComparatorCapacitor
{
__int8 baseclass_0[68];
int mRearAnalogStrength;
int mSideAnalogStrengthRight;
int mSideAnalogStrengthLeft;
int mOldStrength;
ComparatorCapacitor::Mode mMode;
int mRearStrength;
int mSideStrengths;
bool mHasAnalogBeenSet;
CircuitComponentList mSideComponents;
};

```
#### CompareScheduledCallback
```cpp
/* 82474 */
struct CompareScheduledCallback
{
__int8 gap0[1];
};

```
#### CompassSpriteCalculator
```cpp
/* 88759 */
struct CompassSpriteCalculator
{
int mFrame;
float mRot;
float mRotA;
};

```
#### ComplexInventoryTransaction
```cpp
/* 76549 */
struct ComplexInventoryTransaction
{
int (**_vptr$ComplexInventoryTransaction)(void);
ComplexInventoryTransaction::Type mType;
InventoryTransaction mTransaction;
};

```
#### CompoundTagEditHelper
```cpp
/* 13371 */
struct CompoundTagEditHelper
{
Tag *mTag;
std::vector<Tag *> mParentTag;
std::vector<std::string> mTagName;
};

```
#### CompoundTagUpdater
```cpp
/* 13354 */
struct CompoundTagUpdater
{
uint32_t mVersion;
std::vector<std::function<bool (CompoundTagEditHelper &)>> mFilters;
std::vector<std::function<void (CompoundTagEditHelper &)>> mUpdates;
};

```
#### CompoundTagUpdaterBuilder
```cpp
/* 13574 */
struct CompoundTagUpdaterBuilder
{
CompoundTagUpdater *mUpdater;
};

```
#### CompoundTagUpdaterBuilder::TagType<ByteTag>
```cpp
/* 235034 */
struct CompoundTagUpdaterBuilder::TagType<ByteTag>
{
__int8 gap0[1];
};

```
#### CompoundTagUpdaterBuilder::TagType<IntTag>
```cpp
/* 235035 */
struct CompoundTagUpdaterBuilder::TagType<IntTag>
{
__int8 gap0[1];
};

```
#### CompoundTagVariant
```cpp
/* 60952 */
struct CompoundTagVariant
{
CompoundTagVariant::Variant mTagStorage;
};

```
#### ConduitBlockActor::_animateTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 237979 */
struct ConduitBlockActor::_animateTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### ConnectionDefinition
```cpp
/* 5663 */
struct ConnectionDefinition
{
uint16_t ipv4Port;
uint16_t ipv6Port;
ConnectionDefinition::PortBusyFallbackPolicy fallback;
int maxNumPlayers;
int maxNumConnections;
};

```
#### Connector
```cpp
/* 63711 */
struct Connector
{
int (**_vptr$Connector)(void);
};

```
#### Connector::ConnectionStateListener;
```cpp
/* 72969 */
struct Connector::ConnectionStateListener;

```
#### Connector::NatPunchInfo
```cpp
/* 73236 */
struct Connector::NatPunchInfo
{
bool isValid;
bool addressIsDirty;
bool succeeded;
RakNet::SystemAddress externalAddress;
RakNet::TimeMS startPingSentTime;
RakNet::TimeMS pingSentTime;
RakNet::TimeMS startPongReceivedTime;
RakNet::TimeMS pongReceivedTime;
};

```
#### ConsoleChunkBlender
```cpp
/* 477546 */
struct ConsoleChunkBlender
{
SpinLock mSpinLock;
float mInterpCorners[2][2];
float mInterpTable[16][16];
};

```
#### ContainerContentChangeListener
```cpp
/* 89316 */
struct ContainerContentChangeListener
{
int (**_vptr$ContainerContentChangeListener)(void);
};

```
#### ContainerEnumNameHasher
```cpp
/* 174786 */
struct ContainerEnumNameHasher
{
__int8 gap0[1];
};

```
#### ContainerFactory
```cpp
/* 175176 */
struct ContainerFactory
{
__int8 gap0[1];
};

```
#### ContainerItemStack
```cpp
/* 79729 */
struct ContainerItemStack
{
ItemStack itemStackInstance;
ItemInstance itemInstance;
};

```
#### ContainerMixDataEntry
```cpp
/* 75576 */
struct ContainerMixDataEntry
{
int fromItemId;
int reagentItemId;
int toItemId;
};

```
#### ContainerSizeChangeListener
```cpp
/* 173090 */
struct ContainerSizeChangeListener
{
int (**_vptr$ContainerSizeChangeListener)(void);
};

```
#### ContentCatalogPackSource;
```cpp
/* 84138 */
struct ContentCatalogPackSource;

```
#### ContentLog
```cpp
/* 3051 */
struct ContentLog
{
bool mEnabled;
std::vector<ContentLogEndPoint *> mEndPoints;
ThreadLocal<ThreadSpecificData> mThreadSpecificData;
Bedrock::Threading::Mutex mEndpointMutex;
};

```
#### ContentTierInfo
```cpp
/* 5785 */
struct ContentTierInfo
{
MemoryTier mMemoryTier;
};

```
#### ContentTierManager
```cpp
/* 5071 */
struct ContentTierManager
{
MemoryTier mMemoryTier;
};

```
#### ContextAccessor
```cpp
/* 421009 */
struct ContextAccessor
{
uint16_t mTypeId;
std::unique_ptr<ContextAccessor::TypeBase> mContext;
};

```
#### ContextAccessor::TypeBase
```cpp
/* 420937 */
struct ContextAccessor::TypeBase
{
__int8 gap0[1];
};

```
#### ContextAccessor::TypeDerived<EntityContext>
```cpp
/* 420968 */
struct ContextAccessor::TypeDerived<EntityContext>
{
EntityContext mData;
};

```
#### ContextMessage
```cpp
/* 480752 */
struct ContextMessage
{
LogArea mArea;
LogLevel mLevel;
std::string mMessage;
};

```
#### ContextMessageLoggerOptions
```cpp
/* 480816 */
struct ContextMessageLoggerOptions
{
bool mStoreMessages[4];
bool mAssertIfMessageTypeWasReceived[4];
bool mAssertInDestructorIfMessageTypeWasReceived[4];
bool mAllowMessagesToPostToParentMessageLoggers;
bool mOutputAllMessagesOnDestruction;
};

```
#### Control
```cpp
/* 116992 */
struct Control
{
int (**_vptr$Control)(void);
};

```
#### Core::BufferedFileOperations
```cpp
/* 481956 */
struct Core::BufferedFileOperations
{
__int8 gap0[1];
};

```
#### Core::BufferedFileOperations::_copyFileSection<8192>::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 481957 */
struct Core::BufferedFileOperations::_copyFileSection<8192>::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Core::DirectoryIterationItem
```cpp
/* 83872 */
struct Core::DirectoryIterationItem
{
Core::HeapPathBuffer mFullPathName;
Core::PathPart mName;
Core::FileSize mFileSize;
Core::FileSize mFileSizeAllocationOnDisk;
Core::FileType mType;
Core::FileTime mCreateTime;
Core::FileTime mModifyTime;
};

```
#### Core::DiskAccessDiagnostics
```cpp
/* 480877 */
struct Core::DiskAccessDiagnostics
{
std::chrono::_V2::steady_clock::duration mLogInterval;
std::chrono::_V2::steady_clock::time_point mLastLogTime;
double mWriteMBPerMinuteHWM;
double mWriteCountPerMinuteHWM;
};

```
#### Core::DiskAccessTracker
```cpp
/* 480898 */
struct Core::DiskAccessTracker
{
std::chrono::_V2::steady_clock::duration mBytesWrittenInterval;
std::chrono::_V2::steady_clock::duration mNumWritesInterval;
std::vector<Core::DiskAccessTracker::WriteOperation> mWriteOperations;
std::set<Core::PathBuffer<std::string >> mIgnoredPaths;
std::unique_ptr<Core::DiskAccessDiagnostics> mDiskAccessDiagnostics;
Bedrock::Threading::Mutex mMutex;
};

```
#### Core::DiskAccessTracker::WriteOperation
```cpp
/* 480830 */
struct Core::DiskAccessTracker::WriteOperation
{
Core::FileSize writeAmount;
std::chrono::_V2::steady_clock::time_point timePoint;
};

```
#### Core::File
```cpp
/* 5529 */
struct Core::File
{
std::unique_ptr<Core::FileImpl> muptFile;
std::unique_ptr<Core::FileSystemImpl> muptTransaction;
};

```
#### Core::FileOpenMode
```cpp
/* 5530 */
struct Core::FileOpenMode
{
__int8 mRead : 1;
__int8 mWrite : 1;
__int8 mCreate : 1;
__int8 mTruncate : 1;
__int8 mAppend : 1;
__int8 mBinary : 1;
};

```
#### Core::FilePathManager
```cpp
/* 5545 */
struct Core::FilePathManager
{
bool mIsDedicatedServer;
Core::HeapPathBuffer mRoot;
Core::HeapPathBuffer mPackagePath;
Core::HeapPathBuffer mDataUrl;
Core::HeapPathBuffer mExternalFilePath;
Core::HeapPathBuffer mTemporaryFilePath;
Core::HeapPathBuffer mCacheFilePath;
Core::HeapPathBuffer mSettingsPath;
};

```
#### Core::FileStats
```cpp
/* 479769 */
struct Core::FileStats
{
std::atomic<unsigned long> mNumSuccessfulWriteOperations;
std::atomic<unsigned long> mNumBytesWritten;
std::atomic<unsigned long> mNumFailedWriteOperations;
std::atomic<unsigned long> mNumSuccessfulReadOperations;
std::atomic<unsigned long> mNumBytesRead;
std::atomic<unsigned long> mNumFailedReadOperations;
std::atomic<unsigned long> mFileSystemSize;
std::atomic<unsigned long> mFileSystemAllocatedSize;
};

```
#### Core::FileStdStreamBuf
```cpp
/* 5526 */
struct Core::FileStdStreamBuf
{
__int8 baseclass_0[64];
Core::File mFile;
Core::FileOpenMode mFileOpenMode;
std::vector<char> mBuffer;
Core::FileSize mBufferSize;
};

```
#### Core::FileStorageArea::_beginTransaction::$A402370104E9C52EF545D733D86F5169
```cpp
/* 481579 */
struct Core::FileStorageArea::_beginTransaction::$A402370104E9C52EF545D733D86F5169
{
Core::FileStorageArea *this;
};

```
#### Core::FileStorageAreaObserver;
```cpp
/* 479784 */
struct Core::FileStorageAreaObserver;

```
#### Core::FileSystem
```cpp
/* 481922 */
struct Core::FileSystem
{
__int8 gap0[1];
};

```
#### Core::FileSystem::BasicFileData
```cpp
/* 481656 */
struct Core::FileSystem::BasicFileData
{
Core::HeapPathBuffer mPath;
Core::FileSize mSize;
};

```
#### Core::FileSystem::FileTransferProgress
```cpp
/* 481691 */
struct Core::FileSystem::FileTransferProgress
{
Core::FileSize mStartPosition;
Core::FileSize mBytesWritten;
Core::FileSize mBytesRemaining;
};

```
#### Core::FileSystem::copyDirectoryAndContentsRecursivelyWithLimit::$F457DC01F16FBA362CDB9DA581FCE3BD
```cpp
/* 481818 */
struct Core::FileSystem::copyDirectoryAndContentsRecursivelyWithLimit::$F457DC01F16FBA362CDB9DA581FCE3BD
{
bool *directoriesCreated;
std::vector<Core::PathBuffer<std::string >> *directories;
std::vector<Core::FileSystem::BasicFileData> *files;
Core::FileSize *currentFileBytesWritten;
};

```
#### Core::FileSystem::copyFlatFile::$F457DC01F16FBA362CDB9DA581FCE3BD
```cpp
/* 481835 */
struct Core::FileSystem::copyFlatFile::$F457DC01F16FBA362CDB9DA581FCE3BD
{
bool *directoriesCreated;
std::vector<Core::PathBuffer<std::string >> *directories;
std::vector<Core::FileSystem::BasicFileData> *files;
Core::FileSize *currentFileBytesWritten;
};

```
#### Core::FileSystemImpl
```cpp
/* 4554 */
struct Core::FileSystemImpl
{
int (**_vptr$FileSystemImpl)(void);
std::shared_ptr<Core::FileStorageArea> mpStorageArea;
bool mLoggingEnabled;
bool mTransactionEnded;
Core::FileAccessType mAccessType;
Core::FileStats mStats;
Bedrock::Threading::Mutex mFileLock;
std::vector<Core::FileImpl *> mFiles;
Core::FlatFileSystemImpl mFlatFileSystem;
};

```
#### Core::FlatFileManifest
```cpp
/* 481117 */
struct Core::FlatFileManifest
{
std::unordered_map<std::string,unsigned long> mManifestEntriesMap;
std::vector<Core::FlatFileManifestInfo> mManifestInfoVector;
size_t mEntriesCount;
uint64_t mVersion;
Core::HeapPathBuffer mManifestPath;
};

```
#### Core::FlatFileManifestTracker
```cpp
/* 479811 */
struct Core::FlatFileManifestTracker
{
Bedrock::Threading::Mutex mManifestsLock;
std::unordered_map<std::string,std::shared_ptr<Core::FlatFileManifest>> mManifestMap;
std::set<std::string> mManifestNames;
};

```
#### Core::FlatFileOperations
```cpp
/* 482745 */
struct Core::FlatFileOperations
{
__int8 gap0[1];
};

```
#### Core::FlatFileOperations::createFlatFile::$A33D1747C0AB08CA482DA30473C7FFB8
```cpp
/* 482754 */
struct Core::FlatFileOperations::createFlatFile::$A33D1747C0AB08CA482DA30473C7FFB8
{
bool *deleteTargetDirectory;
Core::FileSystemImpl **targetTransaction;
const Core::Path *targetDirectoryPath;
};

```
#### Core::FlatFileOperations::createFlatFile::$B53007EAE32060CC4F6B30C0745D046E
```cpp
/* 482726 */
struct Core::FlatFileOperations::createFlatFile::$B53007EAE32060CC4F6B30C0745D046E
{
std::unique_ptr<Core::FileImpl> *flatFile;
std::vector<char> *writeBuffer;
Core::FileSize *writeBufferSize;
};

```
#### Core::FlatFileSearchResult
```cpp
/* 482462 */
struct Core::FlatFileSearchResult
{
std::shared_ptr<const Core::FlatFileManifest> mManifest;
const Core::FlatFileManifestInfo *mManifestInfoEntry;
};

```
#### Core::FlatFileSystemImpl
```cpp
/* 482369 */
struct Core::FlatFileSystemImpl
{
Core::FileSystemImpl *mFileSystemImpl;
std::shared_ptr<Core::FlatFileManifestTracker> mFlatFileManifestTracker;
};

```
#### Core::FullCopyFileOperations
```cpp
/* 482800 */
struct Core::FullCopyFileOperations
{
__int8 gap0[1];
};

```
#### Core::LevelStorageResult
```cpp
/* 87049 */
struct Core::LevelStorageResult
{
Core::LevelStorageState state;
std::string telemetryMsg;
};

```
#### Core::LoadTimeData
```cpp
/* 479688 */
struct Core::LoadTimeData
{
const std::string mName;
int mScope;
double mTotalTime;
};

```
#### Core::Observer<Core::FileStorageAreaObserver,Core::SingleThreadedLock>;
```cpp
/* 481498 */
struct Core::Observer<Core::FileStorageAreaObserver,Core::SingleThreadedLock>;

```
#### Core::Observer<Social::MultiplayerServiceObserver,Core::SingleThreadedLock>
```cpp
/* 76904 */
struct Core::Observer<Social::MultiplayerServiceObserver,Core::SingleThreadedLock>
{
int (**_vptr$Observer)(void);
Core::Observer<Social::MultiplayerServiceObserver,Core::SingleThreadedLock>::SubjectType *mpSubject;
};

```
#### Core::Observer<Social::XboxLiveUserObserver,Core::SingleThreadedLock>
```cpp
/* 74585 */
struct Core::Observer<Social::XboxLiveUserObserver,Core::SingleThreadedLock>
{
int (**_vptr$Observer)(void);
Core::Observer<Social::XboxLiveUserObserver,Core::SingleThreadedLock>::SubjectType *mpSubject;
};

```
#### Core::Observer<WebviewObserver,Core::SingleThreadedLock>
```cpp
/* 44953 */
struct Core::Observer<WebviewObserver,Core::SingleThreadedLock>
{
int (**_vptr$Observer)(void);
Core::Observer<WebviewObserver,Core::SingleThreadedLock>::SubjectType *mpSubject;
};

```
#### Core::Path
```cpp
/* 5539 */
struct Core::Path
{
Core::PathPart mPathPart;
};

```
#### Core::PathBuffer<Core::StackString<char,1024> >
```cpp
/* 5063 */
struct Core::PathBuffer<Core::StackString<char,1024> >
{
Core::StackString<char,1024> mContainer;
};

```
#### Core::PathContainerConversions<Core::StackString<char,1024> >
```cpp
/* 5548 */
struct Core::PathContainerConversions<Core::StackString<char,1024> >
{
__int8 gap0[1];
};

```
#### Core::PathPart
```cpp
/* 676 */
struct Core::PathPart
{
std::string mUtf8StdString;
};

```
#### Core::Profile::CounterToken
```cpp
/* 63864 */
struct Core::Profile::CounterToken
{
MicroProfileToken mMicroProfileToken;
};

```
#### Core::Profile::FileCounters
```cpp
/* 485594 */
struct Core::Profile::FileCounters
{
uint64_t requests;
uint64_t retries;
uint64_t retrySuccess;
uint64_t failures;
};

```
#### Core::Profile::ProfileMultiSectionCPU
```cpp
/* 485592 */
struct Core::Profile::ProfileMultiSectionCPU
{
__int8 gap0[1];
};

```
#### Core::Profile::ProfileMultiSectionCPU::ProfileSectionSuspend
```cpp
/* 485593 */
struct Core::Profile::ProfileMultiSectionCPU::ProfileSectionSuspend
{
__int8 gap0[1];
};

```
#### Core::Profile::ProfileSectionCPU
```cpp
/* 32841 */
struct Core::Profile::ProfileSectionCPU
{
const Core::Profile::CPUProfileToken *mToken;
};

```
#### Core::Profile::ProfileThread
```cpp
/* 87047 */
struct Core::Profile::ProfileThread
{
__int8 gap0[1];
};

```
#### Core::Random
```cpp
/* 31072 */
struct Core::Random
{
RandomSeed mSeed;
uint32_t _mt[624];
int _mti;
bool mHaveNextNextGaussian;
float mNextNextGaussian;
int mInitedIdx;
};

```
#### Core::ScopedLoadTimeSection
```cpp
/* 479652 */
struct Core::ScopedLoadTimeSection
{
double mStartTime;
Core::LoadTimeData mProfileData;
};

```
#### Core::SingleThreadedLock
```cpp
/* 44760 */
struct Core::SingleThreadedLock
{
__int8 gap0[1];
};

```
#### Core::SplitPathT<1024,64>
```cpp
/* 13123 */
struct Core::SplitPathT<1024,64>
{
std::array<Core::Path,64> mParts;
size_t mNumParts;
};

```
#### Core::SplitPathT<1024,64>::SplitPathT::$1CC25A583192B38B92CA1589E23791C2
```cpp
/* 13248 */
struct Core::SplitPathT<1024,64>::SplitPathT::$1CC25A583192B38B92CA1589E23791C2
{
Core::SplitPathT<1024,64> *this;
__gnu_cxx::__normal_iterator<const char *,std::string > *splitEnd;
__gnu_cxx::__normal_iterator<const char *,std::string > *splitStart;
const std::string *fullPath;
};

```
#### Core::StackString<char,1024>
```cpp
/* 5064 */
struct Core::StackString<char,1024>
{
const size_t MAX_LENGTH;
std::array<char,1024> mBuf;
size_t mLength;
};

```
#### Core::StorageAreaState
```cpp
/* 479785 */
struct Core::StorageAreaState
{
Bedrock::Threading::Mutex mMutex;
Core::HeapPathBuffer mStorageAreaRootPath;
std::atomic<bool> mIsExtendDiskSpaceEvent;
std::atomic<bool> mIsLowDiskSpaceWarning;
std::atomic<bool> mIsOutOfDiskSpaceError;
std::atomic<bool> mIsCriticalDiskError;
std::vector<Core::StorageAreaStateListener *> mListeners;
};

```
#### Core::StorageAreaStateListener;
```cpp
/* 479798 */
struct Core::StorageAreaStateListener;

```
#### Core::StorageAreasTree
```cpp
/* 481500 */
struct Core::StorageAreasTree
{
Core::StorageAreasTree::TreeNode mRoot;
std::vector<Core::FileStorageArea *> mStorageAreas;
};

```
#### Core::StorageAreasTree::TreeChild
```cpp
/* 481200 */
struct Core::StorageAreasTree::TreeChild
{
HashedString mKey;
std::unique_ptr<Core::StorageAreasTree::TreeNode> mNode;
};

```
#### Core::StorageAreasTree::TreeNode
```cpp
/* 481209 */
struct Core::StorageAreasTree::TreeNode
{
std::vector<Core::StorageAreasTree::TreeChild> mChildren;
Core::FileStorageArea *mStorageArea;
};

```
#### Core::String
```cpp
/* 485134 */
struct Core::String
{
__int8 gap0[1];
};

```
#### Core::StringSpan
```cpp
/* 13124 */
struct Core::StringSpan
{
string_span mStringSpan;
};

```
#### Core::Subject<Core::FileStorageAreaObserver,Core::SingleThreadedLock>
```cpp
/* 479771 */
struct Core::Subject<Core::FileStorageAreaObserver,Core::SingleThreadedLock>
{
Core::SingleThreadedLock mLock;
std::vector<Core::FileStorageAreaObserver *> mObservers;
};

```
#### Core::Subject<Social::MultiplayerServiceObserver,Core::SingleThreadedLock>
```cpp
/* 76906 */
struct Core::Subject<Social::MultiplayerServiceObserver,Core::SingleThreadedLock>
{
Core::SingleThreadedLock mLock;
std::vector<Social::MultiplayerServiceObserver *> mObservers;
};

```
#### Core::Subject<Social::XboxLiveUserObserver,Core::SingleThreadedLock>
```cpp
/* 74587 */
struct Core::Subject<Social::XboxLiveUserObserver,Core::SingleThreadedLock>
{
Core::SingleThreadedLock mLock;
std::vector<Social::XboxLiveUserObserver *> mObservers;
};

```
#### Core::Subject<WebviewObserver,Core::SingleThreadedLock>
```cpp
/* 44955 */
struct Core::Subject<WebviewObserver,Core::SingleThreadedLock>
{
Core::SingleThreadedLock mLock;
std::vector<WebviewObserver *> mObservers;
};

```
#### Core::TransactionFrame
```cpp
/* 481729 */
struct Core::TransactionFrame
{
std::shared_ptr<Core::FileSystemImpl> msptTransaction;
Core::StackPathBuffer mCleanPath;
Core::Result mResult;
};

```
#### Core::TransactionFrameSourceTarget
```cpp
/* 481724 */
struct Core::TransactionFrameSourceTarget
{
Core::StackPathBuffer mSource;
Core::StackPathBuffer mTarget;
bool mSameStorageArea;
std::shared_ptr<Core::FileSystemImpl> msptSourceTransaction;
std::shared_ptr<Core::FileSystemImpl> msptTargetTransaction;
Core::Result mResult;
};

```
#### Core::UnzipFile
```cpp
/* 187041 */
struct Core::UnzipFile
{
std::unique_ptr<ZlibFileAccessWrapper> mZipFileSystemWrapper;
std::unique_ptr<Core::UnzipInternals> mZipFile;
};

```
#### Core::UnzipInternals
```cpp
/* 186970 */
struct Core::UnzipInternals
{
unzFile mZipFile;
};

```
#### Core::ZipUtils::UnzipSettings
```cpp
/* 84120 */
struct Core::ZipUtils::UnzipSettings
{
Core::ZipUtils::ZipFileRestrictions mRestrictions;
bool mDeleteZipOnSuccess;
bool mPreventOverwrites;
IFileAccess *mFileAccess;
std::string mPassword;
std::vector<std::string> mSelectedPaths;
};

```
#### Core::ZipUtils::ZipFileRestrictions
```cpp
/* 84121 */
struct Core::ZipUtils::ZipFileRestrictions
{
std::set<std::string> mForbiddenExtensions;
std::set<std::string> mRestrictedExtensions;
std::set<std::string> mForbiddenFilenames;
};

```
#### Core::ZipUtils::ZipProgress
```cpp
/* 83713 */
struct Core::ZipUtils::ZipProgress
{
std::atomic_uint mFilesDone;
std::atomic_uint mFilesSkipped;
std::atomic_uint mTotalFiles;
};

```
#### Core::ZipUtils::ZipProgressList
```cpp
/* 83991 */
struct Core::ZipUtils::ZipProgressList
{
std::vector<std::shared_ptr<Core::ZipUtils::ZipProgress>> mZipProgress;
Bedrock::Threading::Mutex mProgressLock;
};

```
#### Core::ZipUtils::unzipToFlatFile::$08149540B08F7C481DA597604321840B
```cpp
/* 483044 */
struct Core::ZipUtils::unzipToFlatFile::$08149540B08F7C481DA597604321840B
{
Core::File *flatFileData;
std::vector<char> *flatFileWriteBuffer;
Core::FileSize *flatFileWriteBufferSize;
Core::ZipUtils::unzipToFlatFile::$50374A4BB464550A3A71B057536681BD *cleanupFlatFile;
Core::ZipUtils::unzipToFlatFile::$FAF4479A2BA4AFA3BD422DA1BA9A6B87 *commitFunction;
};

```
#### Core::ZipUtils::unzipToFlatFile::$50374A4BB464550A3A71B057536681BD
```cpp
/* 483043 */
struct Core::ZipUtils::unzipToFlatFile::$50374A4BB464550A3A71B057536681BD
{
Core::File *flatFileData;
const Core::StackPathBuffer *flatFilePath;
};

```
#### Core::ZipUtils::unzipToFlatFile::$FAF4479A2BA4AFA3BD422DA1BA9A6B87
```cpp
/* 483045 */
struct Core::ZipUtils::unzipToFlatFile::$FAF4479A2BA4AFA3BD422DA1BA9A6B87
{
Core::File *flatFileData;
Core::ZipUtils::unzipToFlatFile::$50374A4BB464550A3A71B057536681BD *cleanupFlatFile;
const Core::StackPathBuffer *flatFilePath;
};

```
#### Core::`anonymous namespace'::TreeChildCompare
```cpp
/* 482898 */
struct Core::`anonymous namespace'::TreeChildCompare
{
__int8 gap0[1];
};

```
#### CraftableCompounds
```cpp
/* 237790 */
struct CraftableCompounds
{
int (**_vptr$CraftableCompounds)(void);
std::unordered_map<std::string,ItemStack> mComponentsToCompound;
std::unordered_map<int,std::vector<ItemStack>> mCompoundToComponents;
std::unordered_map<std::string,LabTableReactionType> mComponentsToReaction;
std::unordered_map<std::string,CompoundContainerType> mComponentsToContainerOverride;
};

```
#### CrashHandler
```cpp
/* 294342 */
struct CrashHandler
{
__int8 gap0[1];
};

```
#### CrashHelper
```cpp
/* 294353 */
struct CrashHelper
{
__int8 gap0[1];
};

```
#### CreativeGroupInfo
```cpp
/* 175699 */
struct CreativeGroupInfo
{
std::string mName;
__int16 mIconId;
__int16 mIconAux;
Unique<CompoundTag> mIconUserData;
};

```
#### CreativeItemCategoryEnumHasher
```cpp
/* 181614 */
struct CreativeItemCategoryEnumHasher
{
__int8 gap0[1];
};

```
#### Crypto::Asymmetric::Asymmetric;
```cpp
/* 45592 */
struct Crypto::Asymmetric::Asymmetric;

```
#### Crypto::Hash::Hash;
```cpp
/* 422015 */
struct Crypto::Hash::Hash;

```
#### Crypto::Hash::IHash;
```cpp
/* 421369 */
struct Crypto::Hash::IHash;

```
#### Crypto::Hash;
```cpp
/* 486919 */
struct Crypto::Hash;

```
#### Crypto::Random::Random;
```cpp
/* 486917 */
struct Crypto::Random::Random;

```
#### Crypto::Random;
```cpp
/* 486918 */
struct Crypto::Random;

```
#### Crypto::Symmetric::Symmetric;
```cpp
/* 421339 */
struct Crypto::Symmetric::Symmetric;

```
#### Crypto::encryptedFileHeader::$5002CB87BB9EDBB12D0797D08A1D72BD
```cpp
/* 422721 */
struct Crypto::encryptedFileHeader::$5002CB87BB9EDBB12D0797D08A1D72BD
{
unsigned int _version;
Crypto::signatureValue _efsignature;
unsigned int _data1;
unsigned int _data2;
unsigned __int8 _IdSize;
char _IdName[239];
};

```
#### CustomDebugMapColorAttributes
```cpp
/* 191150 */
struct CustomDebugMapColorAttributes
{
int mDebugMapColor;
};

```
#### CustomDebugMapColorOddAttributes
```cpp
/* 191186 */
struct CustomDebugMapColorOddAttributes
{
int mDebugMapOddColor;
};

```
#### CustomFoliageColorAttributes
```cpp
/* 190970 */
struct CustomFoliageColorAttributes
{
int mFoliageColor;
};

```
#### CustomGrassColorAttributes
```cpp
/* 191078 */
struct CustomGrassColorAttributes
{
int mGrassColor;
};

```
#### CustomHumidityAttributes
```cpp
/* 191294 */
struct CustomHumidityAttributes
{
bool mIsHumid;
};

```
#### CustomMapFoliageColorAttributes
```cpp
/* 191042 */
struct CustomMapFoliageColorAttributes
{
int mMapFoliageColor;
};

```
#### CustomMapGrassColorAttributes
```cpp
/* 191114 */
struct CustomMapGrassColorAttributes
{
int mMapGrassColor;
};

```
#### CustomSkyColorAttributes
```cpp
/* 190934 */
struct CustomSkyColorAttributes
{
Color mSkyColor;
};

```
#### CustomTemperatureCategoryAttributes
```cpp
/* 191258 */
struct CustomTemperatureCategoryAttributes
{
Biome::BiomeTempCategory mTemperatureCategory;
};

```
#### CSHA1
```cpp
/* 478096 */
struct CSHA1
{
unsigned int m_state[5];
unsigned int m_count[2];
unsigned int m_reserved0[1];
unsigned __int8 m_buffer[64];
unsigned __int8 m_digest[20];
unsigned int m_reserved1[3];
unsigned __int8 m_workspace[64];
SHA1_WORKSPACE_BLOCK *m_block;
};

```
#### CameraCallbacks;
```cpp
/* 457056 */
struct CameraCallbacks;

```
#### CameraItemComponent
```cpp
/* 180676 */
struct CameraItemComponent
{
int (**_vptr$CameraItemComponent)(void);
float mBlackBarsDuration;
float mBlackBarsScreenRatio;
float mShutterScreenRatio;
float mShutterDuration;
float mPictureDuration;
float mSlideAwayDuration;
bool mPlacingTripod;
uint64_t mPlacingTripodClientTick;
uint64_t mPlacingTripodServerTick;
CameraCallbacks *mCallbacks;
};

```
#### Cat::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124057 */
struct Cat::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### CauldronBlock::spawnPotionParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 226316 */
struct CauldronBlock::spawnPotionParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### CauldronBlock::spawnSplashParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 226317 */
struct CauldronBlock::spawnSplashParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### ChangeDimensionRequest
```cpp
/* 89834 */
struct ChangeDimensionRequest
{
ChangeDimensionRequest::State mState;
DimensionType mFromDimensionId;
DimensionType mToDimensionId;
Vec3 mPosition;
bool mUsePortal;
bool mRespawn;
Unique<CompoundTag> mAgentTag;
};

```
#### ChannelTransform
```cpp
/* 124574 */
struct ChannelTransform
{
ExpressionNode mXYZ[3];
Vec3 mAxis;
ChannelTransformAxisType mTransformDataType;
};

```
#### ChemistryIngredient
```cpp
/* 456240 */
struct ChemistryIngredient
{
ItemInstance mItem;
};

```
#### ChemistryRecipes
```cpp
/* 457266 */
struct ChemistryRecipes
{
__int8 gap0[1];
};

```
#### Chicken::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124065 */
struct Chicken::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### ChunkBlockPos
```cpp
/* 33813 */
struct ChunkBlockPos
{
uint8_t x;
uint8_t z;
Height y;
};

```
#### ChunkBuildOrderPolicyBase
```cpp
/* 34799 */
struct ChunkBuildOrderPolicyBase
{
int (**_vptr$ChunkBuildOrderPolicyBase)(void);
};

```
#### ChunkPos
```cpp
/* 5799 */
struct ChunkPos
{
ChunkPos::$9F8988CC0F9198BEB3D9C07F7FC1F2E7 _anon_0;
};

```
#### ChunkPos::$9F8988CC0F9198BEB3D9C07F7FC1F2E7::$71D3E18752AF5CECAE552A00ECF6483C
```cpp
/* 5801 */
struct ChunkPos::$9F8988CC0F9198BEB3D9C07F7FC1F2E7::$71D3E18752AF5CECAE552A00ECF6483C
{
int x;
int z;
};

```
#### ChunkSource
```cpp
/* 34214 */
struct ChunkSource
{
int (**_vptr$ChunkSource)(void);
int mChunkSide;
Level *mLevel;
Dimension *mDimension;
ChunkSource *mParent;
Unique<ChunkSource> mOwnedParent;
LevelChunkBuilderData *mLevelChunkBuilderData;
};

```
#### CircuitComponentList
```cpp
/* 34454 */
struct CircuitComponentList
{
std::vector<CircuitComponentList::Item> mComponents;
};

```
#### CircuitComponentList::Item
```cpp
/* 34467 */
struct CircuitComponentList::Item
{
BaseCircuitComponent *mComponent;
int mDampening;
BlockPos mPos;
FacingID mDirection;
bool mDirectlyPowered;
int mData;
};

```
#### CircuitSceneGraph
```cpp
/* 34425 */
struct CircuitSceneGraph
{
CircuitSceneGraph::ComponentMap mAllComponents;
CircuitComponentList mActiveComponents;
CircuitSceneGraph::ComponentsPerPosMap mActiveComponentsPerChunk;
CircuitSceneGraph::ComponentsPerPosMap mPowerAssociationMap;
std::unordered_map<BlockPos,CircuitSceneGraph::PendingEntry> mPendingAdds;
std::unordered_map<BlockPos,CircuitSceneGraph::PendingEntry> mPendingUpdates;
std::unordered_map<BlockPos,std::vector<BlockPos>> mComponentsToReEvaluate;
std::vector<CircuitSceneGraph::PendingEntry> mPendingRemoves;
};

```
#### CircuitSystem::LevelChunkTracking
```cpp
/* 34569 */
struct CircuitSystem::LevelChunkTracking
{
BlockPos mChunkPos;
};

```
#### CircuitTrackingInfo::Entry
```cpp
/* 292130 */
struct CircuitTrackingInfo::Entry
{
BaseCircuitComponent *mComponent;
BlockPos mPos;
FacingID mDirection;
uint64_t mTypeID;
};

```
#### ClacksServer::ExecutionAndResult
```cpp
/* 7501 */
struct ClacksServer::ExecutionAndResult
{
ResetEventObj execution;
grpc::Status error;
};

```
#### ClassID
```cpp
/* 40727 */
struct ClassID
{
__int8 gap0[1];
};

```
#### ClientBlobCache::Server::ActiveTransfer
```cpp
/* 73674 */
struct ClientBlobCache::Server::ActiveTransfer
{
ClientBlobCache::Server::ActiveTransfersManager *mCache;
NetworkIdentifier mOwner;
std::unordered_map<unsigned long,std::shared_ptr<ClientBlobCache::Server::Blob>> mIdsWaitingForACK;
};

```
#### ClientBlobCache::Server::ActiveTransfersManager
```cpp
/* 73628 */
struct ClientBlobCache::Server::ActiveTransfersManager
{
std::unordered_map<NetworkIdentifier,std::unique_ptr<ClientBlobCache::Server::ActiveTransfersManager::TransferTracker>> mTransferTrackerMap;
ClientBlobCache::Server::ActiveTransfersManager::CacheMap mSentBlobs;
size_t mCacheSizeBytes;
};

```
#### ClientBlobCache::Server::Blob
```cpp
/* 68463 */
struct ClientBlobCache::Server::Blob
{
const ClientBlobCache::BlobId id;
const std::string data;
};

```
#### ClientBlobCache::Server::TransferBuilder
```cpp
/* 77424 */
struct ClientBlobCache::Server::TransferBuilder
{
ClientBlobCache::Server::ActiveTransfer mTransfer;
};

```
#### ClimateAttributes
```cpp
/* 193499 */
struct ClimateAttributes
{
float mTemperature;
float mDownfall;
float mSnowAccumulationMin;
float mSnowAccumulationMax;
};

```
#### ClockSpriteCalculator
```cpp
/* 88760 */
struct ClockSpriteCalculator
{
int mFrame;
float mRot;
float mRotA;
};

```
#### CloneCommand::execute::CloneBlockInfo
```cpp
/* 424868 */
struct CloneCommand::execute::CloneBlockInfo
{
BlockPos mPos;
const Block *mState;
std::unique_ptr<CompoundTag> mTag;
};

```
#### Color
```cpp
/* 33169 */
struct Color
{
float r;
float g;
float b;
float a;
};

```
#### ColorPaletteAttributes
```cpp
/* 191006 */
struct ColorPaletteAttributes
{
std::string mPaletteName;
};

```
#### ColumnCachedData
```cpp
/* 33669 */
struct ColumnCachedData
{
int grassColor;
int waterColor;
};

```
#### CommandArea
```cpp
/* 90986 */
struct CommandArea
{
std::unique_ptr<ChunkViewSource> mChunkSource;
BlockSource mBlockSource;
};

```
#### CommandAreaFactory
```cpp
/* 91477 */
struct CommandAreaFactory
{
Dimension *mDimension;
};

```
#### CommandBlock::_executeChain::$8760BA774438E6A855C8C1CB8DE2843F
```cpp
/* 459308 */
struct CommandBlock::_executeChain::$8760BA774438E6A855C8C1CB8DE2843F
{
const CommandBlock *this;
};

```
#### CommandFilePath
```cpp
/* 90965 */
struct CommandFilePath
{
std::string mText;
};

```
#### CommandFlag
```cpp
/* 1614 */
struct CommandFlag
{
uint8_t flag;
};

```
#### CommandItem
```cpp
/* 90962 */
struct CommandItem
{
int mVersion;
int mId;
};

```
#### CommandLexer
```cpp
/* 5665 */
struct CommandLexer
{
const std::string *mInput;
CommandLexer::Token mToken;
};

```
#### CommandLexer::Token
```cpp
/* 5666 */
struct CommandLexer::Token
{
const char *text;
uint32_t length;
CommandLexer::TokenType type;
};

```
#### CommandMessage
```cpp
/* 6364 */
struct CommandMessage
{
std::vector<CommandMessage::MessageComponent> mData;
};

```
#### CommandMessage::MessageComponent
```cpp
/* 6331 */
struct CommandMessage::MessageComponent
{
std::string string;
std::unique_ptr<CommandSelector<Actor>> selection;
};

```
#### CommandOrigin
```cpp
/* 1616 */
struct CommandOrigin
{
int (**_vptr$CommandOrigin)(void);
mce::UUID mUUID;
};

```
#### CommandOriginData
```cpp
/* 78833 */
struct CommandOriginData
{
CommandOriginType mType;
mce::UUID mUUID;
std::string mRequestId;
int64_t mPlayerId;
};

```
#### CommandOutputMessage
```cpp
/* 6083 */
struct CommandOutputMessage
{
CommandOutputMessageType mType;
std::string mMessageId;
std::vector<std::string> mParams;
};

```
#### CommandOutputParameter::CommandOutputParameter::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 91536 */
struct CommandOutputParameter::CommandOutputParameter::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### CommandOutputSender
```cpp
/* 4443 */
struct CommandOutputSender
{
int (**_vptr$CommandOutputSender)(void);
Automation::AutomationClient *mAutomationClient;
std::function<void (AutomationCmdOutput &)> mEmplaceTestCommandOutputCallback;
};

```
#### CommandPosition
```cpp
/* 33044 */
struct CommandPosition
{
Vec3 mOffset;
bool mRelativeX;
bool mRelativeY;
bool mRelativeZ;
bool mLocal;
};

```
#### CommandRawText
```cpp
/* 90960 */
struct CommandRawText
{
std::string mText;
};

```
#### CommandRegistry
```cpp
/* 1503 */
struct CommandRegistry
{
std::function<void (const Packet &)> mNetworkUpdateCallback;
CommandRegistry::ScoreboardScoreAccessor mGetScoreForObjective;
std::vector<CommandRegistry::ParseRule> mRules;
CommandRegistry::ParseTableMap mParseTables;
std::vector<CommandRegistry::OptionalParameterChain> mOptionals;
std::vector<std::string> mEnumValues;
std::vector<CommandRegistry::Enum> mEnums;
std::vector<CommandRegistry::Factorization> mFactorizations;
std::vector<std::string> mPostfixes;
std::map<std::string,unsigned int> mEnumLookup;
std::map<std::string,unsigned long> mEnumValueLookup;
std::vector<CommandRegistry::Symbol> mCommandSymbols;
std::map<std::string,CommandRegistry::Signature> mSignatures;
std::map<typeid_t<CommandRegistry>,int> mTypeLookup;
std::map<std::string,std::string> mAliases;
std::vector<SemanticConstraint> mSemanticConstraints;
std::map<SemanticConstraint,unsigned char> mSemanticConstraintLookup;
std::vector<CommandRegistry::ConstrainedValue> mConstrainedValues;
std::map<std::pair<unsigned long,unsigned int>,unsigned int> mConstrainedValueLookup;
std::vector<CommandRegistry::SoftEnum> mSoftEnums;
std::map<std::string,unsigned int> mSoftEnumLookup;
std::vector<CommandRegistry::RegistryState> mStateStack;
CommandRegistry::ParamSymbols mArgs;
CommandRegistry::CommandOverrideFunctor mCommandOverrideFunctor;
};

```
#### CommandRegistry::ConstrainedValue
```cpp
/* 1567 */
struct CommandRegistry::ConstrainedValue
{
CommandRegistry::Symbol mValue;
CommandRegistry::Symbol mEnum;
std::vector<unsigned char> mConstraints;
};

```
#### CommandRegistry::DefaultIdConverter<AgentCommand::Mode>
```cpp
/* 476454 */
struct CommandRegistry::DefaultIdConverter<AgentCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<AgentCommands::CollectCommand::CollectionSpecification>
```cpp
/* 476455 */
struct CommandRegistry::DefaultIdConverter<AgentCommands::CollectCommand::CollectionSpecification>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<AgentCommands::Direction>
```cpp
/* 476453 */
struct CommandRegistry::DefaultIdConverter<AgentCommands::Direction>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<BlockSlot>
```cpp
/* 426570 */
struct CommandRegistry::DefaultIdConverter<BlockSlot>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<ChangeSettingCommand::Setting>
```cpp
/* 6284 */
struct CommandRegistry::DefaultIdConverter<ChangeSettingCommand::Setting>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<CloneCommand::CloneMode>
```cpp
/* 424974 */
struct CommandRegistry::DefaultIdConverter<CloneCommand::CloneMode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<CloneCommand::MaskMode>
```cpp
/* 424973 */
struct CommandRegistry::DefaultIdConverter<CloneCommand::MaskMode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<CommandItem>
```cpp
/* 93242 */
struct CommandRegistry::DefaultIdConverter<CommandItem>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<Difficulty>
```cpp
/* 425122 */
struct CommandRegistry::DefaultIdConverter<Difficulty>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<EffectCommand::Mode>
```cpp
/* 425322 */
struct CommandRegistry::DefaultIdConverter<EffectCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<Enchant::Type>
```cpp
/* 94436 */
struct CommandRegistry::DefaultIdConverter<Enchant::Type>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<EquipmentSlot>
```cpp
/* 426571 */
struct CommandRegistry::DefaultIdConverter<EquipmentSlot>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<ExecuteCommand::Mode>
```cpp
/* 425418 */
struct CommandRegistry::DefaultIdConverter<ExecuteCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<FillCommand::FillMode>
```cpp
/* 425513 */
struct CommandRegistry::DefaultIdConverter<FillCommand::FillMode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<GameType>
```cpp
/* 93243 */
struct CommandRegistry::DefaultIdConverter<GameType>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<ListDCommand::DetailMode>
```cpp
/* 425967 */
struct CommandRegistry::DefaultIdConverter<ListDCommand::DetailMode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<ObjectiveSortOrder>
```cpp
/* 426875 */
struct CommandRegistry::DefaultIdConverter<ObjectiveSortOrder>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<PermissionCommand::Action>
```cpp
/* 426289 */
struct CommandRegistry::DefaultIdConverter<PermissionCommand::Action>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<PermissionCommand::AvailableCommandPermissionPresets>
```cpp
/* 426290 */
struct CommandRegistry::DefaultIdConverter<PermissionCommand::AvailableCommandPermissionPresets>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<ReplaceItemCommand::TargetType>
```cpp
/* 426572 */
struct CommandRegistry::DefaultIdConverter<ReplaceItemCommand::TargetType>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<SaveCommand::Mode>
```cpp
/* 6637 */
struct CommandRegistry::DefaultIdConverter<SaveCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<ScoreboardCommand::Action>
```cpp
/* 426874 */
struct CommandRegistry::DefaultIdConverter<ScoreboardCommand::Action>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<ScoreboardCommand::Category>
```cpp
/* 426873 */
struct CommandRegistry::DefaultIdConverter<ScoreboardCommand::Category>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<SetBlockCommand::SetBlockMode>
```cpp
/* 426971 */
struct CommandRegistry::DefaultIdConverter<SetBlockCommand::SetBlockMode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<StructureFeatureType>
```cpp
/* 94435 */
struct CommandRegistry::DefaultIdConverter<StructureFeatureType>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TagCommand::Action>
```cpp
/* 427377 */
struct CommandRegistry::DefaultIdConverter<TagCommand::Action>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TeleportCommand::FacingResult>
```cpp
/* 427474 */
struct CommandRegistry::DefaultIdConverter<TeleportCommand::FacingResult>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TestForBlocksCommand::Mode>
```cpp
/* 427659 */
struct CommandRegistry::DefaultIdConverter<TestForBlocksCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TickingAreaCommand::AddAreaType>
```cpp
/* 427930 */
struct CommandRegistry::DefaultIdConverter<TickingAreaCommand::AddAreaType>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TickingAreaCommand::Mode>
```cpp
/* 427929 */
struct CommandRegistry::DefaultIdConverter<TickingAreaCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TickingAreaCommand::TargetDimensions>
```cpp
/* 427931 */
struct CommandRegistry::DefaultIdConverter<TickingAreaCommand::TargetDimensions>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TimeCommand::Mode>
```cpp
/* 428127 */
struct CommandRegistry::DefaultIdConverter<TimeCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TimeCommand::Query>
```cpp
/* 428128 */
struct CommandRegistry::DefaultIdConverter<TimeCommand::Query>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TimeCommand::TimeSpec>
```cpp
/* 428129 */
struct CommandRegistry::DefaultIdConverter<TimeCommand::TimeSpec>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TitleCommand::Mode>
```cpp
/* 428284 */
struct CommandRegistry::DefaultIdConverter<TitleCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<TitleRawCommand::Mode>
```cpp
/* 428379 */
struct CommandRegistry::DefaultIdConverter<TitleRawCommand::Mode>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<VideoStreamConnectPacket::Action>
```cpp
/* 428495 */
struct CommandRegistry::DefaultIdConverter<VideoStreamConnectPacket::Action>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<WeatherCommand::WeatherRequest>
```cpp
/* 428676 */
struct CommandRegistry::DefaultIdConverter<WeatherCommand::WeatherRequest>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<WeatherCommand::WeatherType>
```cpp
/* 428675 */
struct CommandRegistry::DefaultIdConverter<WeatherCommand::WeatherType>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<WhitelistCommand::Action>
```cpp
/* 6816 */
struct CommandRegistry::DefaultIdConverter<WhitelistCommand::Action>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<bool>
```cpp
/* 93244 */
struct CommandRegistry::DefaultIdConverter<bool>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<const ActorDefinitionIdentifier *>
```cpp
/* 94434 */
struct CommandRegistry::DefaultIdConverter<const ActorDefinitionIdentifier *>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<const Block *>
```cpp
/* 93246 */
struct CommandRegistry::DefaultIdConverter<const Block *>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<const MobEffect *>
```cpp
/* 425323 */
struct CommandRegistry::DefaultIdConverter<const MobEffect *>
{
__int8 gap0[1];
};

```
#### CommandRegistry::DefaultIdConverter<int>
```cpp
/* 93245 */
struct CommandRegistry::DefaultIdConverter<int>
{
__int8 gap0[1];
};

```
#### CommandRegistry::Enum
```cpp
/* 1203 */
struct CommandRegistry::Enum
{
std::string name;
typeid_t<CommandRegistry> type;
CommandRegistry::ParseFunction parse;
_BYTE gap30[8];
std::vector<std::pair<unsigned long,unsigned long>> values;
};

```
#### CommandRegistry::Factorization
```cpp
/* 1239 */
struct CommandRegistry::Factorization
{
CommandRegistry::Terminal commandSymbol;
};

```
#### CommandRegistry::LexicalToken
```cpp
/* 49176 */
struct CommandRegistry::LexicalToken
{
const char *mText;
uint32_t mLength;
CommandRegistry::Terminal mType;
CommandRegistry::Terminal mIdentifierInfo;
const CommandRegistry *mRegistry;
};

```
#### CommandRegistry::OptionalParameterChain
```cpp
/* 1167 */
struct CommandRegistry::OptionalParameterChain
{
int parameterCount;
CommandRegistry::RuleIndex followingRuleIndex;
CommandRegistry::Symbol paramSymbol;
};

```
#### CommandRegistry::ParamSymbols
```cpp
/* 1607 */
struct CommandRegistry::ParamSymbols
{
CommandRegistry::Terminal x;
CommandRegistry::Terminal y;
CommandRegistry::Terminal z;
CommandRegistry::Terminal dx;
CommandRegistry::Terminal dy;
CommandRegistry::Terminal dz;
CommandRegistry::Terminal r;
CommandRegistry::Terminal rm;
CommandRegistry::Terminal rx;
CommandRegistry::Terminal rxm;
CommandRegistry::Terminal ry;
CommandRegistry::Terminal rym;
CommandRegistry::Terminal l;
CommandRegistry::Terminal lm;
CommandRegistry::Terminal c;
CommandRegistry::Terminal m;
CommandRegistry::Terminal name;
CommandRegistry::Terminal type;
CommandRegistry::Terminal score;
CommandRegistry::Terminal tag;
};

```
#### CommandRegistry::ParseRule
```cpp
/* 1071 */
struct CommandRegistry::ParseRule
{
CommandRegistry::NonTerminal nonTerminal;
CommandRegistry::ProcessFunction process;
CommandRegistry::SymbolVector derivation;
CommandVersion versions;
};

```
#### CommandRegistry::ParseTable
```cpp
/* 1125 */
struct CommandRegistry::ParseTable
{
CommandRegistry::ParseSet first;
CommandRegistry::ParseSet follow;
CommandRegistry::PredictTable predict;
};

```
#### CommandRegistry::ParseToken
```cpp
/* 1615 */
struct CommandRegistry::ParseToken
{
std::unique_ptr<CommandRegistry::ParseToken> child;
std::unique_ptr<CommandRegistry::ParseToken> next;
CommandRegistry::ParseToken *parent;
const char *text;
uint32_t length;
CommandRegistry::Symbol type;
};

```
#### CommandRegistry::RegistryState
```cpp
/* 1606 */
struct CommandRegistry::RegistryState
{
uint32_t signatureCount;
uint32_t enumValueCount;
uint32_t postfixCount;
uint32_t enumCount;
uint32_t factorizationCount;
uint32_t optionalCount;
uint32_t ruleCount;
uint32_t softEnumCount;
uint32_t constraintCount;
std::vector<unsigned int> constrainedValueCount;
std::vector<unsigned int> softEnumValuesCount;
};

```
#### CommandRegistry::SemanticInfo
```cpp
/* 5676 */
struct CommandRegistry::SemanticInfo
{
bool mIsValid;
std::vector<CommandRegistry::Symbol> mConstrainedParams;
std::string mSoftEnumText;
std::string mSoftEnumEscapeCharExceptions;
std::set<CommandRegistry::Symbol> mAlreadyCompletedSymbols;
};

```
#### CommandRegistry::SoftEnum
```cpp
/* 1593 */
struct CommandRegistry::SoftEnum
{
std::string mName;
std::vector<std::string> mValues;
};

```
#### CommandRegistry::Symbol
```cpp
/* 1407 */
struct CommandRegistry::Symbol
{
int mValue;
};

```
#### CommandSelectorResults<Actor>
```cpp
/* 6316 */
struct CommandSelectorResults<Actor>
{
CommandResultVector mTargets;
};

```
#### CommandSelectorResults<Player>
```cpp
/* 6317 */
struct CommandSelectorResults<Player>
{
CommandResultVector mTargets;
};

```
#### CommandSoftEnumRegistry
```cpp
/* 88496 */
struct CommandSoftEnumRegistry
{
CommandRegistry *mRegistry;
};

```
#### CommandSyntaxInformation
```cpp
/* 5681 */
struct CommandSyntaxInformation
{
bool isValid;
std::string description;
std::vector<OverloadSyntaxInformation> possibilities;
};

```
#### CommandVersion
```cpp
/* 1476 */
struct CommandVersion
{
int mFrom;
int mTo;
};

```
#### CommandWildcardInt
```cpp
/* 90963 */
struct CommandWildcardInt
{
bool mIsWildcard;
int mValue;
};

```
#### ComparatorCapacitor
```cpp
/* 237970 */
struct ComparatorCapacitor
{
__int8 baseclass_0[68];
int mRearAnalogStrength;
int mSideAnalogStrengthRight;
int mSideAnalogStrengthLeft;
int mOldStrength;
ComparatorCapacitor::Mode mMode;
int mRearStrength;
int mSideStrengths;
bool mHasAnalogBeenSet;
CircuitComponentList mSideComponents;
};

```
#### CompareScheduledCallback
```cpp
/* 82474 */
struct CompareScheduledCallback
{
__int8 gap0[1];
};

```
#### CompassSpriteCalculator
```cpp
/* 88759 */
struct CompassSpriteCalculator
{
int mFrame;
float mRot;
float mRotA;
};

```
#### ComplexInventoryTransaction
```cpp
/* 76549 */
struct ComplexInventoryTransaction
{
int (**_vptr$ComplexInventoryTransaction)(void);
ComplexInventoryTransaction::Type mType;
InventoryTransaction mTransaction;
};

```
#### CompoundTagEditHelper
```cpp
/* 13371 */
struct CompoundTagEditHelper
{
Tag *mTag;
std::vector<Tag *> mParentTag;
std::vector<std::string> mTagName;
};

```
#### CompoundTagUpdater
```cpp
/* 13354 */
struct CompoundTagUpdater
{
uint32_t mVersion;
std::vector<std::function<bool (CompoundTagEditHelper &)>> mFilters;
std::vector<std::function<void (CompoundTagEditHelper &)>> mUpdates;
};

```
#### CompoundTagUpdaterBuilder
```cpp
/* 13574 */
struct CompoundTagUpdaterBuilder
{
CompoundTagUpdater *mUpdater;
};

```
#### CompoundTagUpdaterBuilder::TagType<ByteTag>
```cpp
/* 235034 */
struct CompoundTagUpdaterBuilder::TagType<ByteTag>
{
__int8 gap0[1];
};

```
#### CompoundTagUpdaterBuilder::TagType<IntTag>
```cpp
/* 235035 */
struct CompoundTagUpdaterBuilder::TagType<IntTag>
{
__int8 gap0[1];
};

```
#### CompoundTagVariant
```cpp
/* 60952 */
struct CompoundTagVariant
{
CompoundTagVariant::Variant mTagStorage;
};

```
#### ConduitBlockActor::_animateTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 237979 */
struct ConduitBlockActor::_animateTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### ConnectionDefinition
```cpp
/* 5663 */
struct ConnectionDefinition
{
uint16_t ipv4Port;
uint16_t ipv6Port;
ConnectionDefinition::PortBusyFallbackPolicy fallback;
int maxNumPlayers;
int maxNumConnections;
};

```
#### Connector
```cpp
/* 63711 */
struct Connector
{
int (**_vptr$Connector)(void);
};

```
#### Connector::ConnectionStateListener;
```cpp
/* 72969 */
struct Connector::ConnectionStateListener;

```
#### Connector::NatPunchInfo
```cpp
/* 73236 */
struct Connector::NatPunchInfo
{
bool isValid;
bool addressIsDirty;
bool succeeded;
RakNet::SystemAddress externalAddress;
RakNet::TimeMS startPingSentTime;
RakNet::TimeMS pingSentTime;
RakNet::TimeMS startPongReceivedTime;
RakNet::TimeMS pongReceivedTime;
};

```
#### ConsoleChunkBlender
```cpp
/* 477546 */
struct ConsoleChunkBlender
{
SpinLock mSpinLock;
float mInterpCorners[2][2];
float mInterpTable[16][16];
};

```
#### ContainerContentChangeListener
```cpp
/* 89316 */
struct ContainerContentChangeListener
{
int (**_vptr$ContainerContentChangeListener)(void);
};

```
#### ContainerEnumNameHasher
```cpp
/* 174786 */
struct ContainerEnumNameHasher
{
__int8 gap0[1];
};

```
#### ContainerFactory
```cpp
/* 175176 */
struct ContainerFactory
{
__int8 gap0[1];
};

```
#### ContainerItemStack
```cpp
/* 79729 */
struct ContainerItemStack
{
ItemStack itemStackInstance;
ItemInstance itemInstance;
};

```
#### ContainerMixDataEntry
```cpp
/* 75576 */
struct ContainerMixDataEntry
{
int fromItemId;
int reagentItemId;
int toItemId;
};

```
#### ContainerSizeChangeListener
```cpp
/* 173090 */
struct ContainerSizeChangeListener
{
int (**_vptr$ContainerSizeChangeListener)(void);
};

```
#### ContentCatalogPackSource;
```cpp
/* 84138 */
struct ContentCatalogPackSource;

```
#### ContentLog
```cpp
/* 3051 */
struct ContentLog
{
bool mEnabled;
std::vector<ContentLogEndPoint *> mEndPoints;
ThreadLocal<ThreadSpecificData> mThreadSpecificData;
Bedrock::Threading::Mutex mEndpointMutex;
};

```
#### ContentTierInfo
```cpp
/* 5785 */
struct ContentTierInfo
{
MemoryTier mMemoryTier;
};

```
#### ContentTierManager
```cpp
/* 5071 */
struct ContentTierManager
{
MemoryTier mMemoryTier;
};

```
#### ContextAccessor
```cpp
/* 421009 */
struct ContextAccessor
{
uint16_t mTypeId;
std::unique_ptr<ContextAccessor::TypeBase> mContext;
};

```
#### ContextAccessor::TypeBase
```cpp
/* 420937 */
struct ContextAccessor::TypeBase
{
__int8 gap0[1];
};

```
#### ContextAccessor::TypeDerived<EntityContext>
```cpp
/* 420968 */
struct ContextAccessor::TypeDerived<EntityContext>
{
EntityContext mData;
};

```
#### ContextMessage
```cpp
/* 480752 */
struct ContextMessage
{
LogArea mArea;
LogLevel mLevel;
std::string mMessage;
};

```
#### ContextMessageLoggerOptions
```cpp
/* 480816 */
struct ContextMessageLoggerOptions
{
bool mStoreMessages[4];
bool mAssertIfMessageTypeWasReceived[4];
bool mAssertInDestructorIfMessageTypeWasReceived[4];
bool mAllowMessagesToPostToParentMessageLoggers;
bool mOutputAllMessagesOnDestruction;
};

```
#### Control
```cpp
/* 116992 */
struct Control
{
int (**_vptr$Control)(void);
};

```
#### Core::BufferedFileOperations
```cpp
/* 481956 */
struct Core::BufferedFileOperations
{
__int8 gap0[1];
};

```
#### Core::BufferedFileOperations::_copyFileSection<8192>::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 481957 */
struct Core::BufferedFileOperations::_copyFileSection<8192>::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Core::DirectoryIterationItem
```cpp
/* 83872 */
struct Core::DirectoryIterationItem
{
Core::HeapPathBuffer mFullPathName;
Core::PathPart mName;
Core::FileSize mFileSize;
Core::FileSize mFileSizeAllocationOnDisk;
Core::FileType mType;
Core::FileTime mCreateTime;
Core::FileTime mModifyTime;
};

```
#### Core::DiskAccessDiagnostics
```cpp
/* 480877 */
struct Core::DiskAccessDiagnostics
{
std::chrono::_V2::steady_clock::duration mLogInterval;
std::chrono::_V2::steady_clock::time_point mLastLogTime;
double mWriteMBPerMinuteHWM;
double mWriteCountPerMinuteHWM;
};

```
#### Core::DiskAccessTracker
```cpp
/* 480898 */
struct Core::DiskAccessTracker
{
std::chrono::_V2::steady_clock::duration mBytesWrittenInterval;
std::chrono::_V2::steady_clock::duration mNumWritesInterval;
std::vector<Core::DiskAccessTracker::WriteOperation> mWriteOperations;
std::set<Core::PathBuffer<std::string >> mIgnoredPaths;
std::unique_ptr<Core::DiskAccessDiagnostics> mDiskAccessDiagnostics;
Bedrock::Threading::Mutex mMutex;
};

```
#### Core::DiskAccessTracker::WriteOperation
```cpp
/* 480830 */
struct Core::DiskAccessTracker::WriteOperation
{
Core::FileSize writeAmount;
std::chrono::_V2::steady_clock::time_point timePoint;
};

```
#### Core::File
```cpp
/* 5529 */
struct Core::File
{
std::unique_ptr<Core::FileImpl> muptFile;
std::unique_ptr<Core::FileSystemImpl> muptTransaction;
};

```
#### Core::FileOpenMode
```cpp
/* 5530 */
struct Core::FileOpenMode
{
__int8 mRead : 1;
__int8 mWrite : 1;
__int8 mCreate : 1;
__int8 mTruncate : 1;
__int8 mAppend : 1;
__int8 mBinary : 1;
};

```
#### Core::FilePathManager
```cpp
/* 5545 */
struct Core::FilePathManager
{
bool mIsDedicatedServer;
Core::HeapPathBuffer mRoot;
Core::HeapPathBuffer mPackagePath;
Core::HeapPathBuffer mDataUrl;
Core::HeapPathBuffer mExternalFilePath;
Core::HeapPathBuffer mTemporaryFilePath;
Core::HeapPathBuffer mCacheFilePath;
Core::HeapPathBuffer mSettingsPath;
};

```
#### Core::FileStats
```cpp
/* 479769 */
struct Core::FileStats
{
std::atomic<unsigned long> mNumSuccessfulWriteOperations;
std::atomic<unsigned long> mNumBytesWritten;
std::atomic<unsigned long> mNumFailedWriteOperations;
std::atomic<unsigned long> mNumSuccessfulReadOperations;
std::atomic<unsigned long> mNumBytesRead;
std::atomic<unsigned long> mNumFailedReadOperations;
std::atomic<unsigned long> mFileSystemSize;
std::atomic<unsigned long> mFileSystemAllocatedSize;
};

```
#### Core::FileStdStreamBuf
```cpp
/* 5526 */
struct Core::FileStdStreamBuf
{
__int8 baseclass_0[64];
Core::File mFile;
Core::FileOpenMode mFileOpenMode;
std::vector<char> mBuffer;
Core::FileSize mBufferSize;
};

```
#### Core::FileStorageArea::_beginTransaction::$A402370104E9C52EF545D733D86F5169
```cpp
/* 481579 */
struct Core::FileStorageArea::_beginTransaction::$A402370104E9C52EF545D733D86F5169
{
Core::FileStorageArea *this;
};

```
#### Core::FileStorageAreaObserver;
```cpp
/* 479784 */
struct Core::FileStorageAreaObserver;

```
#### Core::FileSystem
```cpp
/* 481922 */
struct Core::FileSystem
{
__int8 gap0[1];
};

```
#### Core::FileSystem::BasicFileData
```cpp
/* 481656 */
struct Core::FileSystem::BasicFileData
{
Core::HeapPathBuffer mPath;
Core::FileSize mSize;
};

```
#### Core::FileSystem::FileTransferProgress
```cpp
/* 481691 */
struct Core::FileSystem::FileTransferProgress
{
Core::FileSize mStartPosition;
Core::FileSize mBytesWritten;
Core::FileSize mBytesRemaining;
};

```
#### Core::FileSystem::copyDirectoryAndContentsRecursivelyWithLimit::$F457DC01F16FBA362CDB9DA581FCE3BD
```cpp
/* 481818 */
struct Core::FileSystem::copyDirectoryAndContentsRecursivelyWithLimit::$F457DC01F16FBA362CDB9DA581FCE3BD
{
bool *directoriesCreated;
std::vector<Core::PathBuffer<std::string >> *directories;
std::vector<Core::FileSystem::BasicFileData> *files;
Core::FileSize *currentFileBytesWritten;
};

```
#### Core::FileSystem::copyFlatFile::$F457DC01F16FBA362CDB9DA581FCE3BD
```cpp
/* 481835 */
struct Core::FileSystem::copyFlatFile::$F457DC01F16FBA362CDB9DA581FCE3BD
{
bool *directoriesCreated;
std::vector<Core::PathBuffer<std::string >> *directories;
std::vector<Core::FileSystem::BasicFileData> *files;
Core::FileSize *currentFileBytesWritten;
};

```
#### Core::FileSystemImpl
```cpp
/* 4554 */
struct Core::FileSystemImpl
{
int (**_vptr$FileSystemImpl)(void);
std::shared_ptr<Core::FileStorageArea> mpStorageArea;
bool mLoggingEnabled;
bool mTransactionEnded;
Core::FileAccessType mAccessType;
Core::FileStats mStats;
Bedrock::Threading::Mutex mFileLock;
std::vector<Core::FileImpl *> mFiles;
Core::FlatFileSystemImpl mFlatFileSystem;
};

```
#### Core::FlatFileManifest
```cpp
/* 481117 */
struct Core::FlatFileManifest
{
std::unordered_map<std::string,unsigned long> mManifestEntriesMap;
std::vector<Core::FlatFileManifestInfo> mManifestInfoVector;
size_t mEntriesCount;
uint64_t mVersion;
Core::HeapPathBuffer mManifestPath;
};

```
#### Core::FlatFileManifestTracker
```cpp
/* 479811 */
struct Core::FlatFileManifestTracker
{
Bedrock::Threading::Mutex mManifestsLock;
std::unordered_map<std::string,std::shared_ptr<Core::FlatFileManifest>> mManifestMap;
std::set<std::string> mManifestNames;
};

```
#### Core::FlatFileOperations
```cpp
/* 482745 */
struct Core::FlatFileOperations
{
__int8 gap0[1];
};

```
#### Core::FlatFileOperations::createFlatFile::$A33D1747C0AB08CA482DA30473C7FFB8
```cpp
/* 482754 */
struct Core::FlatFileOperations::createFlatFile::$A33D1747C0AB08CA482DA30473C7FFB8
{
bool *deleteTargetDirectory;
Core::FileSystemImpl **targetTransaction;
const Core::Path *targetDirectoryPath;
};

```
#### Core::FlatFileOperations::createFlatFile::$B53007EAE32060CC4F6B30C0745D046E
```cpp
/* 482726 */
struct Core::FlatFileOperations::createFlatFile::$B53007EAE32060CC4F6B30C0745D046E
{
std::unique_ptr<Core::FileImpl> *flatFile;
std::vector<char> *writeBuffer;
Core::FileSize *writeBufferSize;
};

```
#### Core::FlatFileSearchResult
```cpp
/* 482462 */
struct Core::FlatFileSearchResult
{
std::shared_ptr<const Core::FlatFileManifest> mManifest;
const Core::FlatFileManifestInfo *mManifestInfoEntry;
};

```
#### Core::FlatFileSystemImpl
```cpp
/* 482369 */
struct Core::FlatFileSystemImpl
{
Core::FileSystemImpl *mFileSystemImpl;
std::shared_ptr<Core::FlatFileManifestTracker> mFlatFileManifestTracker;
};

```
#### Core::FullCopyFileOperations
```cpp
/* 482800 */
struct Core::FullCopyFileOperations
{
__int8 gap0[1];
};

```
#### Core::LevelStorageResult
```cpp
/* 87049 */
struct Core::LevelStorageResult
{
Core::LevelStorageState state;
std::string telemetryMsg;
};

```
#### Core::LoadTimeData
```cpp
/* 479688 */
struct Core::LoadTimeData
{
const std::string mName;
int mScope;
double mTotalTime;
};

```
#### Core::Observer<Core::FileStorageAreaObserver,Core::SingleThreadedLock>;
```cpp
/* 481498 */
struct Core::Observer<Core::FileStorageAreaObserver,Core::SingleThreadedLock>;

```
#### Core::Observer<Social::MultiplayerServiceObserver,Core::SingleThreadedLock>
```cpp
/* 76904 */
struct Core::Observer<Social::MultiplayerServiceObserver,Core::SingleThreadedLock>
{
int (**_vptr$Observer)(void);
Core::Observer<Social::MultiplayerServiceObserver,Core::SingleThreadedLock>::SubjectType *mpSubject;
};

```
#### Core::Observer<Social::XboxLiveUserObserver,Core::SingleThreadedLock>
```cpp
/* 74585 */
struct Core::Observer<Social::XboxLiveUserObserver,Core::SingleThreadedLock>
{
int (**_vptr$Observer)(void);
Core::Observer<Social::XboxLiveUserObserver,Core::SingleThreadedLock>::SubjectType *mpSubject;
};

```
#### Core::Observer<WebviewObserver,Core::SingleThreadedLock>
```cpp
/* 44953 */
struct Core::Observer<WebviewObserver,Core::SingleThreadedLock>
{
int (**_vptr$Observer)(void);
Core::Observer<WebviewObserver,Core::SingleThreadedLock>::SubjectType *mpSubject;
};

```
#### Core::Path
```cpp
/* 5539 */
struct Core::Path
{
Core::PathPart mPathPart;
};

```
#### Core::PathBuffer<Core::StackString<char,1024> >
```cpp
/* 5063 */
struct Core::PathBuffer<Core::StackString<char,1024> >
{
Core::StackString<char,1024> mContainer;
};

```
#### Core::PathContainerConversions<Core::StackString<char,1024> >
```cpp
/* 5548 */
struct Core::PathContainerConversions<Core::StackString<char,1024> >
{
__int8 gap0[1];
};

```
#### Core::PathPart
```cpp
/* 676 */
struct Core::PathPart
{
std::string mUtf8StdString;
};

```
#### Core::Profile::CounterToken
```cpp
/* 63864 */
struct Core::Profile::CounterToken
{
MicroProfileToken mMicroProfileToken;
};

```
#### Core::Profile::FileCounters
```cpp
/* 485594 */
struct Core::Profile::FileCounters
{
uint64_t requests;
uint64_t retries;
uint64_t retrySuccess;
uint64_t failures;
};

```
#### Core::Profile::ProfileMultiSectionCPU
```cpp
/* 485592 */
struct Core::Profile::ProfileMultiSectionCPU
{
__int8 gap0[1];
};

```
#### Core::Profile::ProfileMultiSectionCPU::ProfileSectionSuspend
```cpp
/* 485593 */
struct Core::Profile::ProfileMultiSectionCPU::ProfileSectionSuspend
{
__int8 gap0[1];
};

```
#### Core::Profile::ProfileSectionCPU
```cpp
/* 32841 */
struct Core::Profile::ProfileSectionCPU
{
const Core::Profile::CPUProfileToken *mToken;
};

```
#### Core::Profile::ProfileThread
```cpp
/* 87047 */
struct Core::Profile::ProfileThread
{
__int8 gap0[1];
};

```
#### Core::Random
```cpp
/* 31072 */
struct Core::Random
{
RandomSeed mSeed;
uint32_t _mt[624];
int _mti;
bool mHaveNextNextGaussian;
float mNextNextGaussian;
int mInitedIdx;
};

```
#### Core::ScopedLoadTimeSection
```cpp
/* 479652 */
struct Core::ScopedLoadTimeSection
{
double mStartTime;
Core::LoadTimeData mProfileData;
};

```
#### Core::SingleThreadedLock
```cpp
/* 44760 */
struct Core::SingleThreadedLock
{
__int8 gap0[1];
};

```
#### Core::SplitPathT<1024,64>
```cpp
/* 13123 */
struct Core::SplitPathT<1024,64>
{
std::array<Core::Path,64> mParts;
size_t mNumParts;
};

```
#### Core::SplitPathT<1024,64>::SplitPathT::$1CC25A583192B38B92CA1589E23791C2
```cpp
/* 13248 */
struct Core::SplitPathT<1024,64>::SplitPathT::$1CC25A583192B38B92CA1589E23791C2
{
Core::SplitPathT<1024,64> *this;
__gnu_cxx::__normal_iterator<const char *,std::string > *splitEnd;
__gnu_cxx::__normal_iterator<const char *,std::string > *splitStart;
const std::string *fullPath;
};

```
#### Core::StackString<char,1024>
```cpp
/* 5064 */
struct Core::StackString<char,1024>
{
const size_t MAX_LENGTH;
std::array<char,1024> mBuf;
size_t mLength;
};

```
#### Core::StorageAreaState
```cpp
/* 479785 */
struct Core::StorageAreaState
{
Bedrock::Threading::Mutex mMutex;
Core::HeapPathBuffer mStorageAreaRootPath;
std::atomic<bool> mIsExtendDiskSpaceEvent;
std::atomic<bool> mIsLowDiskSpaceWarning;
std::atomic<bool> mIsOutOfDiskSpaceError;
std::atomic<bool> mIsCriticalDiskError;
std::vector<Core::StorageAreaStateListener *> mListeners;
};

```
#### Core::StorageAreaStateListener;
```cpp
/* 479798 */
struct Core::StorageAreaStateListener;

```
#### Core::StorageAreasTree
```cpp
/* 481500 */
struct Core::StorageAreasTree
{
Core::StorageAreasTree::TreeNode mRoot;
std::vector<Core::FileStorageArea *> mStorageAreas;
};

```
#### Core::StorageAreasTree::TreeChild
```cpp
/* 481200 */
struct Core::StorageAreasTree::TreeChild
{
HashedString mKey;
std::unique_ptr<Core::StorageAreasTree::TreeNode> mNode;
};

```
#### Core::StorageAreasTree::TreeNode
```cpp
/* 481209 */
struct Core::StorageAreasTree::TreeNode
{
std::vector<Core::StorageAreasTree::TreeChild> mChildren;
Core::FileStorageArea *mStorageArea;
};

```
#### Core::String
```cpp
/* 485134 */
struct Core::String
{
__int8 gap0[1];
};

```
#### Core::StringSpan
```cpp
/* 13124 */
struct Core::StringSpan
{
string_span mStringSpan;
};

```
#### Core::Subject<Core::FileStorageAreaObserver,Core::SingleThreadedLock>
```cpp
/* 479771 */
struct Core::Subject<Core::FileStorageAreaObserver,Core::SingleThreadedLock>
{
Core::SingleThreadedLock mLock;
std::vector<Core::FileStorageAreaObserver *> mObservers;
};

```
#### Core::Subject<Social::MultiplayerServiceObserver,Core::SingleThreadedLock>
```cpp
/* 76906 */
struct Core::Subject<Social::MultiplayerServiceObserver,Core::SingleThreadedLock>
{
Core::SingleThreadedLock mLock;
std::vector<Social::MultiplayerServiceObserver *> mObservers;
};

```
#### Core::Subject<Social::XboxLiveUserObserver,Core::SingleThreadedLock>
```cpp
/* 74587 */
struct Core::Subject<Social::XboxLiveUserObserver,Core::SingleThreadedLock>
{
Core::SingleThreadedLock mLock;
std::vector<Social::XboxLiveUserObserver *> mObservers;
};

```
#### Core::Subject<WebviewObserver,Core::SingleThreadedLock>
```cpp
/* 44955 */
struct Core::Subject<WebviewObserver,Core::SingleThreadedLock>
{
Core::SingleThreadedLock mLock;
std::vector<WebviewObserver *> mObservers;
};

```
#### Core::TransactionFrame
```cpp
/* 481729 */
struct Core::TransactionFrame
{
std::shared_ptr<Core::FileSystemImpl> msptTransaction;
Core::StackPathBuffer mCleanPath;
Core::Result mResult;
};

```
#### Core::TransactionFrameSourceTarget
```cpp
/* 481724 */
struct Core::TransactionFrameSourceTarget
{
Core::StackPathBuffer mSource;
Core::StackPathBuffer mTarget;
bool mSameStorageArea;
std::shared_ptr<Core::FileSystemImpl> msptSourceTransaction;
std::shared_ptr<Core::FileSystemImpl> msptTargetTransaction;
Core::Result mResult;
};

```
#### Core::UnzipFile
```cpp
/* 187041 */
struct Core::UnzipFile
{
std::unique_ptr<ZlibFileAccessWrapper> mZipFileSystemWrapper;
std::unique_ptr<Core::UnzipInternals> mZipFile;
};

```
#### Core::UnzipInternals
```cpp
/* 186970 */
struct Core::UnzipInternals
{
unzFile mZipFile;
};

```
#### Core::ZipUtils::UnzipSettings
```cpp
/* 84120 */
struct Core::ZipUtils::UnzipSettings
{
Core::ZipUtils::ZipFileRestrictions mRestrictions;
bool mDeleteZipOnSuccess;
bool mPreventOverwrites;
IFileAccess *mFileAccess;
std::string mPassword;
std::vector<std::string> mSelectedPaths;
};

```
#### Core::ZipUtils::ZipFileRestrictions
```cpp
/* 84121 */
struct Core::ZipUtils::ZipFileRestrictions
{
std::set<std::string> mForbiddenExtensions;
std::set<std::string> mRestrictedExtensions;
std::set<std::string> mForbiddenFilenames;
};

```
#### Core::ZipUtils::ZipProgress
```cpp
/* 83713 */
struct Core::ZipUtils::ZipProgress
{
std::atomic_uint mFilesDone;
std::atomic_uint mFilesSkipped;
std::atomic_uint mTotalFiles;
};

```
#### Core::ZipUtils::ZipProgressList
```cpp
/* 83991 */
struct Core::ZipUtils::ZipProgressList
{
std::vector<std::shared_ptr<Core::ZipUtils::ZipProgress>> mZipProgress;
Bedrock::Threading::Mutex mProgressLock;
};

```
#### Core::ZipUtils::unzipToFlatFile::$08149540B08F7C481DA597604321840B
```cpp
/* 483044 */
struct Core::ZipUtils::unzipToFlatFile::$08149540B08F7C481DA597604321840B
{
Core::File *flatFileData;
std::vector<char> *flatFileWriteBuffer;
Core::FileSize *flatFileWriteBufferSize;
Core::ZipUtils::unzipToFlatFile::$50374A4BB464550A3A71B057536681BD *cleanupFlatFile;
Core::ZipUtils::unzipToFlatFile::$FAF4479A2BA4AFA3BD422DA1BA9A6B87 *commitFunction;
};

```
#### Core::ZipUtils::unzipToFlatFile::$50374A4BB464550A3A71B057536681BD
```cpp
/* 483043 */
struct Core::ZipUtils::unzipToFlatFile::$50374A4BB464550A3A71B057536681BD
{
Core::File *flatFileData;
const Core::StackPathBuffer *flatFilePath;
};

```
#### Core::ZipUtils::unzipToFlatFile::$FAF4479A2BA4AFA3BD422DA1BA9A6B87
```cpp
/* 483045 */
struct Core::ZipUtils::unzipToFlatFile::$FAF4479A2BA4AFA3BD422DA1BA9A6B87
{
Core::File *flatFileData;
Core::ZipUtils::unzipToFlatFile::$50374A4BB464550A3A71B057536681BD *cleanupFlatFile;
const Core::StackPathBuffer *flatFilePath;
};

```
#### Core::`anonymous namespace'::TreeChildCompare
```cpp
/* 482898 */
struct Core::`anonymous namespace'::TreeChildCompare
{
__int8 gap0[1];
};

```
#### CraftableCompounds
```cpp
/* 237790 */
struct CraftableCompounds
{
int (**_vptr$CraftableCompounds)(void);
std::unordered_map<std::string,ItemStack> mComponentsToCompound;
std::unordered_map<int,std::vector<ItemStack>> mCompoundToComponents;
std::unordered_map<std::string,LabTableReactionType> mComponentsToReaction;
std::unordered_map<std::string,CompoundContainerType> mComponentsToContainerOverride;
};

```
#### CrashHandler
```cpp
/* 294342 */
struct CrashHandler
{
__int8 gap0[1];
};

```
#### CrashHelper
```cpp
/* 294353 */
struct CrashHelper
{
__int8 gap0[1];
};

```
#### CreativeGroupInfo
```cpp
/* 175699 */
struct CreativeGroupInfo
{
std::string mName;
__int16 mIconId;
__int16 mIconAux;
Unique<CompoundTag> mIconUserData;
};

```
#### CreativeItemCategoryEnumHasher
```cpp
/* 181614 */
struct CreativeItemCategoryEnumHasher
{
__int8 gap0[1];
};

```
#### Crypto::Asymmetric::Asymmetric;
```cpp
/* 45592 */
struct Crypto::Asymmetric::Asymmetric;

```
#### Crypto::Hash::Hash;
```cpp
/* 422015 */
struct Crypto::Hash::Hash;

```
#### Crypto::Hash::IHash;
```cpp
/* 421369 */
struct Crypto::Hash::IHash;

```
#### Crypto::Hash;
```cpp
/* 486919 */
struct Crypto::Hash;

```
#### Crypto::Random::Random;
```cpp
/* 486917 */
struct Crypto::Random::Random;

```
#### Crypto::Random;
```cpp
/* 486918 */
struct Crypto::Random;

```
#### Crypto::Symmetric::Symmetric;
```cpp
/* 421339 */
struct Crypto::Symmetric::Symmetric;

```
#### Crypto::encryptedFileHeader::$5002CB87BB9EDBB12D0797D08A1D72BD
```cpp
/* 422721 */
struct Crypto::encryptedFileHeader::$5002CB87BB9EDBB12D0797D08A1D72BD
{
unsigned int _version;
Crypto::signatureValue _efsignature;
unsigned int _data1;
unsigned int _data2;
unsigned __int8 _IdSize;
char _IdName[239];
};

```
#### CustomDebugMapColorAttributes
```cpp
/* 191150 */
struct CustomDebugMapColorAttributes
{
int mDebugMapColor;
};

```
#### CustomDebugMapColorOddAttributes
```cpp
/* 191186 */
struct CustomDebugMapColorOddAttributes
{
int mDebugMapOddColor;
};

```
#### CustomFoliageColorAttributes
```cpp
/* 190970 */
struct CustomFoliageColorAttributes
{
int mFoliageColor;
};

```
#### CustomGrassColorAttributes
```cpp
/* 191078 */
struct CustomGrassColorAttributes
{
int mGrassColor;
};

```
#### CustomHumidityAttributes
```cpp
/* 191294 */
struct CustomHumidityAttributes
{
bool mIsHumid;
};

```
#### CustomMapFoliageColorAttributes
```cpp
/* 191042 */
struct CustomMapFoliageColorAttributes
{
int mMapFoliageColor;
};

```
#### CustomMapGrassColorAttributes
```cpp
/* 191114 */
struct CustomMapGrassColorAttributes
{
int mMapGrassColor;
};

```
#### CustomSkyColorAttributes
```cpp
/* 190934 */
struct CustomSkyColorAttributes
{
Color mSkyColor;
};

```
#### CustomTemperatureCategoryAttributes
```cpp
/* 191258 */
struct CustomTemperatureCategoryAttributes
{
Biome::BiomeTempCategory mTemperatureCategory;
};

```
