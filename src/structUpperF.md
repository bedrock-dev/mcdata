#### Facing
```cpp
/* 31928 */
struct Facing
{
__int8 gap0[1];
};

```
#### Facing::Plane
```cpp
/* 431490 */
struct Facing::Plane
{
__int8 gap0[1];
};

```
#### FeatureLoading::AbstractFeatureHolder
```cpp
/* 19717 */
struct FeatureLoading::AbstractFeatureHolder
{
__int8 gap0[1];
};

```
#### FeatureLoading::ConcreteFeatureHolder<AggregateFeature<PlaceType::Arbitrary> >
```cpp
/* 19887 */
struct FeatureLoading::ConcreteFeatureHolder<AggregateFeature<PlaceType::Arbitrary> >
{
AggregateFeature<PlaceType::Arbitrary> *mFeaturePtr;
};

```
#### FeatureLoading::ConcreteFeatureHolder<AggregateFeature<PlaceType::Sequential> >
```cpp
/* 20932 */
struct FeatureLoading::ConcreteFeatureHolder<AggregateFeature<PlaceType::Sequential> >
{
AggregateFeature<PlaceType::Sequential> *mFeaturePtr;
};

```
#### FeatureLoading::ConcreteFeatureHolder<OreFeature>
```cpp
/* 21616 */
struct FeatureLoading::ConcreteFeatureHolder<OreFeature>
{
OreFeature *mFeaturePtr;
};

```
#### FeatureLoading::ConcreteFeatureHolder<ScatterFeature>
```cpp
/* 22300 */
struct FeatureLoading::ConcreteFeatureHolder<ScatterFeature>
{
ScatterFeature *mFeaturePtr;
};

```
#### FeatureLoading::ConcreteFeatureHolder<SingleBlockFeature>
```cpp
/* 22984 */
struct FeatureLoading::ConcreteFeatureHolder<SingleBlockFeature>
{
SingleBlockFeature *mFeaturePtr;
};

```
#### FeatureLoading::ConcreteFeatureHolder<StructureTemplateFeature>
```cpp
/* 23668 */
struct FeatureLoading::ConcreteFeatureHolder<StructureTemplateFeature>
{
StructureTemplateFeature *mFeaturePtr;
};

```
#### FeatureLoading::ConcreteFeatureHolder<WeightedRandomFeature>
```cpp
/* 24352 */
struct FeatureLoading::ConcreteFeatureHolder<WeightedRandomFeature>
{
WeightedRandomFeature *mFeaturePtr;
};

```
#### FeatureLoading::FeatureRootParseContext
```cpp
/* 19890 */
struct FeatureLoading::FeatureRootParseContext
{
std::reference_wrapper<std::string > mFeatureName;
std::reference_wrapper<IWorldRegistriesProvider> mRegistryProvider;
std::unique_ptr<FeatureLoading::AbstractFeatureHolder> mFeatureHolder;
};

```
#### FeatureRefTraits
```cpp
/* 31079 */
struct FeatureRefTraits
{
__int8 gap0[1];
};

```
#### FeatureRegistry
```cpp
/* 19368 */
struct FeatureRegistry
{
std::vector<std::unique_ptr<IFeature>> mFeatureRegistry;
std::vector<OwnerPtrT<FeatureRefTraits>> mFeatureSlots;
std::unordered_map<StringKey,unsigned long> mFeatureLookupMap;
};

```
#### FeatureToggles
```cpp
/* 77440 */
struct FeatureToggles
{
FeatureToggles::FeatureTogglesArray mFeatures;
Core::HeapPathBuffer mFilePath;
};

```
#### FeatureToggles::FeatureToggle
```cpp
/* 75154 */
struct FeatureToggles::FeatureToggle
{
FeatureOptionID featureID;
FeatureOptionID dependencyFeatureID;
std::unique_ptr<Option> option;
FeatureToggles::SetupFunction setup;
FeatureToggles::LockFunction lock;
};

```
#### FeatureTypeFactory
```cpp
/* 31213 */
struct FeatureTypeFactory
{
JsonUtil::JsonSchemaRoot<FeatureLoading::FeatureRootParseContext> mSchema;
};

```
#### FeedItem
```cpp
/* 55144 */
struct FeedItem
{
const Item *mItem;
int mValue;
std::vector<FeedItem::Effect> mEffects;
};

```
#### FeedItem::Effect
```cpp
/* 53850 */
struct FeedItem::Effect
{
std::string descriptionId;
int id;
int duration;
int amplifier;
float chance;
};

```
#### FileAccessTransforms
```cpp
/* 422390 */
struct FileAccessTransforms
{
int (**_vptr$FileAccessTransforms)(void);
};

```
#### FileArchiver::Result
```cpp
/* 103114 */
struct FileArchiver::Result
{
FileArchiver::Outcome outcome;
Core::HeapPathBuffer fileName;
};

```
#### FileChunk
```cpp
/* 101640 */
struct FileChunk
{
std::vector<unsigned char> data;
FileChunkInfo info;
};

```
#### FileChunkInfo
```cpp
/* 101486 */
struct FileChunkInfo
{
int chunkID;
uint64_t startByte;
uint64_t endByte;
};

```
#### FileChunkManager
```cpp
/* 101724 */
struct FileChunkManager
{
uint64_t mTotalSize;
uint32_t mChunkSize;
int mTotalNbChunks;
int mRequestedChunks;
int mReceivedChunks;
int mWrittenChunks;
std::vector<FileChunkInfo> mChunkInfo;
MovePriorityQueue<FileChunk,std::less<FileChunk> > mChunkQueue;
};

```
#### FileInfo
```cpp
/* 101404 */
struct FileInfo
{
Core::HeapPathBuffer filePath;
uint64_t fileSize;
std::string fileHash;
};

```
#### FilePickerSettings
```cpp
/* 186654 */
struct FilePickerSettings
{
std::function<void (std::shared_ptr<FilePickerSettings>)> onCancel;
std::function<void (bool)> onOperationComplete;
std::function<void (std::shared_ptr<FilePickerSettings>,const Core::Path &)> onPick;
std::vector<FilePickerSettings::FileDescription> mFileDescriptions;
size_t mDefaultFileExtensionIndex;
FilePickerSettings::PickerType mPickerType;
std::string mDefaultFileName;
std::string mDefaultAlbumName;
std::string mFilePickerTitle;
};

```
#### FilePickerSettings::FileDescription
```cpp
/* 186675 */
struct FilePickerSettings::FileDescription
{
std::string Extension;
std::string Name;
};

```
#### FileUploadManager::MultiPartStreamHelper
```cpp
/* 101405 */
struct FileUploadManager::MultiPartStreamHelper
{
bool needHeader;
bool needTrailer;
std::string header;
std::string trailer;
uint64_t currentFileByte;
uint64_t totalFileByte;
uint64_t totalStreamSize;
};

```
#### FilterContext
```cpp
/* 39405 */
struct FilterContext
{
const Actor *mHost;
const Actor *mSubject;
const VariantParameterList *mParams;
const BlockSource *mRegion;
const Dimension *mDimension;
const Level *mLevel;
const Biome *mBiome;
BlockPos mPos;
const Block *mBlock;
const TagRegistry *mTagRegistry;
};

```
#### FilterGroup
```cpp
/* 9577 */
struct FilterGroup
{
int (**_vptr$FilterGroup)(void);
FilterGroup::CollectionType mCollectionType;
std::vector<std::shared_ptr<FilterGroup>> mChildren;
std::vector<std::shared_ptr<FilterTest>> mMembers;
};

```
#### FilterInput
```cpp
/* 114116 */
struct FilterInput
{
FilterParamType mType;
std::string mString;
int mIValue;
float mFValue;
};

```
#### FilterInputDefinition
```cpp
/* 114189 */
struct FilterInputDefinition
{
FilterInput mInput;
std::string mDescription;
};

```
#### FilterInputs
```cpp
/* 114433 */
struct FilterInputs
{
FilterSubject mSubject;
FilterInput mDomain;
FilterOperator mOperator;
FilterInput mValue;
};

```
#### FilterTest::Definition
```cpp
/* 114112 */
struct FilterTest::Definition
{
std::string mName;
std::string mDescription;
const FilterParamDefinition *mSubjectDefinition;
const FilterParamDefinition *mDomainDefinition;
const FilterParamDefinition *mOperatorDefinition;
const FilterParamDefinition *mValueDefinition;
std::function<std::shared_ptr<FilterTest> ()> mFactory;
};

```
#### FilteredTransformationAttributes<LegacyPreHillsEdgeTransformation>
```cpp
/* 10543 */
struct FilteredTransformationAttributes<LegacyPreHillsEdgeTransformation>
{
std::vector<PosibleTransformation> mTransformations;
};

```
#### FilteredTransformationAttributes<PostShoreEdgeTransformation>
```cpp
/* 39519 */
struct FilteredTransformationAttributes<PostShoreEdgeTransformation>
{
std::vector<PosibleTransformation> mTransformations;
};

```
#### FilteredTransformationAttributes<PreHillsEdgeTransformation>
```cpp
/* 12203 */
struct FilteredTransformationAttributes<PreHillsEdgeTransformation>
{
std::vector<PosibleTransformation> mTransformations;
};

```
#### Fish::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124174 */
struct Fish::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### FishingHook::_fishPosEvent::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 115606 */
struct FishingHook::_fishPosEvent::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### FishingHook::_fishTeaseEvent::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 115608 */
struct FishingHook::_fishTeaseEvent::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### FishingHook::_fishhookEvent::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 115607 */
struct FishingHook::_fishhookEvent::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### FlagComponent<(anonymous namespace)::IgnoreAutomaticFeatureRules>;
```cpp
/* 268525 */
struct FlagComponent<(anonymous namespace)::IgnoreAutomaticFeatureRules>;

```
#### FlatWorldGeneratorOptions::getDefault::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 285891 */
struct FlatWorldGeneratorOptions::getDefault::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### FloatRange
```cpp
/* 48706 */
struct FloatRange
{
float rangeMin;
float rangeMax;
};

```
#### FlockingDefinition
```cpp
/* 351664 */
struct FlockingDefinition
{
bool mInWater;
bool mMatchVariant;
bool mUseCenterOfMass;
int mLowFlockLimit;
int mHighFlockLimit;
float mGoalWeight;
float mLonerChance;
float mInfluenceRadius;
float mBreachInfluence;
float mSeparationWeight;
float mSeparationThreshold;
float mCohesionWeight;
float mCohesionThreshold;
float mInnerCohesionThres;
float mMinHeight;
float mMaxHeight;
float mBlockDistance;
float mBlockWeight;
};

```
#### FoliageColor
```cpp
/* 457465 */
struct FoliageColor
{
__int8 gap0[1];
};

```
#### Font;
```cpp
/* 122536 */
struct Font;

```
#### FoodItemComponent
```cpp
/* 173071 */
struct FoodItemComponent
{
const Item *mOwner;
int mNutrition;
float mSaturationModifier;
std::string mUsingConvertsTo;
FoodItemComponent::OnUseAction mOnUseAction;
Vec3 mOnUseRange;
CooldownType mCoolDownType;
int mCooldownTime;
bool mCanAlwaysEat;
std::vector<FoodItemComponent::Effect> mEffects;
std::vector<unsigned int> mRemoveEffects;
};

```
#### FoodItemComponent::Effect
```cpp
/* 172458 */
struct FoodItemComponent::Effect
{
const char *descriptionId;
int id;
int duration;
int amplifier;
float chance;
};

```
#### FormJsonValidator
```cpp
/* 428928 */
struct FormJsonValidator
{
__int8 gap0[1];
};

```
#### FrameUpdateContextBase;
```cpp
/* 90646 */
struct FrameUpdateContextBase;

```
#### FriendlySize
```cpp
/* 64313 */
struct FriendlySize
{
size_t bytes;
};

```
#### FullPlayerInventoryWrapper
```cpp
/* 424737 */
struct FullPlayerInventoryWrapper
{
PlayerInventoryProxy *mPlayerInventory;
SimpleContainer *mArmorInventory;
SimpleContainer *mHandInventory;
InventoryTransactionManager *mTransactionManager;
Player *mPlayer;
};

```
#### FunctionManager
```cpp
/* 87222 */
struct FunctionManager
{
int (**_vptr$FunctionManager)(void);
const GameRule *mGameRule;
bool mIsProcessingStack;
std::vector<FunctionManager::QueuedCommand> mCommandList;
std::unordered_map<const CommandOrigin *,FunctionManager::OriginMapping> mOriginMap;
std::unique_ptr<ICommandDispatcher> mCommandDispatcher;
std::unique_ptr<CommandOrigin> mTickOrigin;
std::unordered_map<std::string,std::unique_ptr<FunctionEntry>> mFunctions;
std::vector<FunctionEntry *> mTickFunctions;
};

```
#### FunctionManager::QueuedCommand
```cpp
/* 94529 */
struct FunctionManager::QueuedCommand
{
IFunctionEntry *mFunction;
const CommandOrigin *mOrigin;
};

```
#### Facing
```cpp
/* 31928 */
struct Facing
{
__int8 gap0[1];
};

```
#### Facing::Plane
```cpp
/* 431490 */
struct Facing::Plane
{
__int8 gap0[1];
};

```
#### FeatureLoading::AbstractFeatureHolder
```cpp
/* 19717 */
struct FeatureLoading::AbstractFeatureHolder
{
__int8 gap0[1];
};

```
#### FeatureLoading::ConcreteFeatureHolder<AggregateFeature<PlaceType::Arbitrary> >
```cpp
/* 19887 */
struct FeatureLoading::ConcreteFeatureHolder<AggregateFeature<PlaceType::Arbitrary> >
{
AggregateFeature<PlaceType::Arbitrary> *mFeaturePtr;
};

```
#### FeatureLoading::ConcreteFeatureHolder<AggregateFeature<PlaceType::Sequential> >
```cpp
/* 20932 */
struct FeatureLoading::ConcreteFeatureHolder<AggregateFeature<PlaceType::Sequential> >
{
AggregateFeature<PlaceType::Sequential> *mFeaturePtr;
};

```
#### FeatureLoading::ConcreteFeatureHolder<OreFeature>
```cpp
/* 21616 */
struct FeatureLoading::ConcreteFeatureHolder<OreFeature>
{
OreFeature *mFeaturePtr;
};

```
#### FeatureLoading::ConcreteFeatureHolder<ScatterFeature>
```cpp
/* 22300 */
struct FeatureLoading::ConcreteFeatureHolder<ScatterFeature>
{
ScatterFeature *mFeaturePtr;
};

```
#### FeatureLoading::ConcreteFeatureHolder<SingleBlockFeature>
```cpp
/* 22984 */
struct FeatureLoading::ConcreteFeatureHolder<SingleBlockFeature>
{
SingleBlockFeature *mFeaturePtr;
};

```
#### FeatureLoading::ConcreteFeatureHolder<StructureTemplateFeature>
```cpp
/* 23668 */
struct FeatureLoading::ConcreteFeatureHolder<StructureTemplateFeature>
{
StructureTemplateFeature *mFeaturePtr;
};

```
#### FeatureLoading::ConcreteFeatureHolder<WeightedRandomFeature>
```cpp
/* 24352 */
struct FeatureLoading::ConcreteFeatureHolder<WeightedRandomFeature>
{
WeightedRandomFeature *mFeaturePtr;
};

```
#### FeatureLoading::FeatureRootParseContext
```cpp
/* 19890 */
struct FeatureLoading::FeatureRootParseContext
{
std::reference_wrapper<std::string > mFeatureName;
std::reference_wrapper<IWorldRegistriesProvider> mRegistryProvider;
std::unique_ptr<FeatureLoading::AbstractFeatureHolder> mFeatureHolder;
};

```
#### FeatureRefTraits
```cpp
/* 31079 */
struct FeatureRefTraits
{
__int8 gap0[1];
};

```
#### FeatureRegistry
```cpp
/* 19368 */
struct FeatureRegistry
{
std::vector<std::unique_ptr<IFeature>> mFeatureRegistry;
std::vector<OwnerPtrT<FeatureRefTraits>> mFeatureSlots;
std::unordered_map<StringKey,unsigned long> mFeatureLookupMap;
};

```
#### FeatureToggles
```cpp
/* 77440 */
struct FeatureToggles
{
FeatureToggles::FeatureTogglesArray mFeatures;
Core::HeapPathBuffer mFilePath;
};

```
#### FeatureToggles::FeatureToggle
```cpp
/* 75154 */
struct FeatureToggles::FeatureToggle
{
FeatureOptionID featureID;
FeatureOptionID dependencyFeatureID;
std::unique_ptr<Option> option;
FeatureToggles::SetupFunction setup;
FeatureToggles::LockFunction lock;
};

```
#### FeatureTypeFactory
```cpp
/* 31213 */
struct FeatureTypeFactory
{
JsonUtil::JsonSchemaRoot<FeatureLoading::FeatureRootParseContext> mSchema;
};

```
#### FeedItem
```cpp
/* 55144 */
struct FeedItem
{
const Item *mItem;
int mValue;
std::vector<FeedItem::Effect> mEffects;
};

```
#### FeedItem::Effect
```cpp
/* 53850 */
struct FeedItem::Effect
{
std::string descriptionId;
int id;
int duration;
int amplifier;
float chance;
};

```
#### FileAccessTransforms
```cpp
/* 422390 */
struct FileAccessTransforms
{
int (**_vptr$FileAccessTransforms)(void);
};

```
#### FileArchiver::Result
```cpp
/* 103114 */
struct FileArchiver::Result
{
FileArchiver::Outcome outcome;
Core::HeapPathBuffer fileName;
};

```
#### FileChunk
```cpp
/* 101640 */
struct FileChunk
{
std::vector<unsigned char> data;
FileChunkInfo info;
};

```
#### FileChunkInfo
```cpp
/* 101486 */
struct FileChunkInfo
{
int chunkID;
uint64_t startByte;
uint64_t endByte;
};

```
#### FileChunkManager
```cpp
/* 101724 */
struct FileChunkManager
{
uint64_t mTotalSize;
uint32_t mChunkSize;
int mTotalNbChunks;
int mRequestedChunks;
int mReceivedChunks;
int mWrittenChunks;
std::vector<FileChunkInfo> mChunkInfo;
MovePriorityQueue<FileChunk,std::less<FileChunk> > mChunkQueue;
};

```
#### FileInfo
```cpp
/* 101404 */
struct FileInfo
{
Core::HeapPathBuffer filePath;
uint64_t fileSize;
std::string fileHash;
};

```
#### FilePickerSettings
```cpp
/* 186654 */
struct FilePickerSettings
{
std::function<void (std::shared_ptr<FilePickerSettings>)> onCancel;
std::function<void (bool)> onOperationComplete;
std::function<void (std::shared_ptr<FilePickerSettings>,const Core::Path &)> onPick;
std::vector<FilePickerSettings::FileDescription> mFileDescriptions;
size_t mDefaultFileExtensionIndex;
FilePickerSettings::PickerType mPickerType;
std::string mDefaultFileName;
std::string mDefaultAlbumName;
std::string mFilePickerTitle;
};

```
#### FilePickerSettings::FileDescription
```cpp
/* 186675 */
struct FilePickerSettings::FileDescription
{
std::string Extension;
std::string Name;
};

```
#### FileUploadManager::MultiPartStreamHelper
```cpp
/* 101405 */
struct FileUploadManager::MultiPartStreamHelper
{
bool needHeader;
bool needTrailer;
std::string header;
std::string trailer;
uint64_t currentFileByte;
uint64_t totalFileByte;
uint64_t totalStreamSize;
};

```
#### FilterContext
```cpp
/* 39405 */
struct FilterContext
{
const Actor *mHost;
const Actor *mSubject;
const VariantParameterList *mParams;
const BlockSource *mRegion;
const Dimension *mDimension;
const Level *mLevel;
const Biome *mBiome;
BlockPos mPos;
const Block *mBlock;
const TagRegistry *mTagRegistry;
};

```
#### FilterGroup
```cpp
/* 9577 */
struct FilterGroup
{
int (**_vptr$FilterGroup)(void);
FilterGroup::CollectionType mCollectionType;
std::vector<std::shared_ptr<FilterGroup>> mChildren;
std::vector<std::shared_ptr<FilterTest>> mMembers;
};

```
#### FilterInput
```cpp
/* 114116 */
struct FilterInput
{
FilterParamType mType;
std::string mString;
int mIValue;
float mFValue;
};

```
#### FilterInputDefinition
```cpp
/* 114189 */
struct FilterInputDefinition
{
FilterInput mInput;
std::string mDescription;
};

```
#### FilterInputs
```cpp
/* 114433 */
struct FilterInputs
{
FilterSubject mSubject;
FilterInput mDomain;
FilterOperator mOperator;
FilterInput mValue;
};

```
#### FilterTest::Definition
```cpp
/* 114112 */
struct FilterTest::Definition
{
std::string mName;
std::string mDescription;
const FilterParamDefinition *mSubjectDefinition;
const FilterParamDefinition *mDomainDefinition;
const FilterParamDefinition *mOperatorDefinition;
const FilterParamDefinition *mValueDefinition;
std::function<std::shared_ptr<FilterTest> ()> mFactory;
};

```
#### FilteredTransformationAttributes<LegacyPreHillsEdgeTransformation>
```cpp
/* 10543 */
struct FilteredTransformationAttributes<LegacyPreHillsEdgeTransformation>
{
std::vector<PosibleTransformation> mTransformations;
};

```
#### FilteredTransformationAttributes<PostShoreEdgeTransformation>
```cpp
/* 39519 */
struct FilteredTransformationAttributes<PostShoreEdgeTransformation>
{
std::vector<PosibleTransformation> mTransformations;
};

```
#### FilteredTransformationAttributes<PreHillsEdgeTransformation>
```cpp
/* 12203 */
struct FilteredTransformationAttributes<PreHillsEdgeTransformation>
{
std::vector<PosibleTransformation> mTransformations;
};

```
#### Fish::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124174 */
struct Fish::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### FishingHook::_fishPosEvent::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 115606 */
struct FishingHook::_fishPosEvent::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### FishingHook::_fishTeaseEvent::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 115608 */
struct FishingHook::_fishTeaseEvent::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### FishingHook::_fishhookEvent::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 115607 */
struct FishingHook::_fishhookEvent::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### FlagComponent<(anonymous namespace)::IgnoreAutomaticFeatureRules>;
```cpp
/* 268525 */
struct FlagComponent<(anonymous namespace)::IgnoreAutomaticFeatureRules>;

```
#### FlatWorldGeneratorOptions::getDefault::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 285891 */
struct FlatWorldGeneratorOptions::getDefault::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### FloatRange
```cpp
/* 48706 */
struct FloatRange
{
float rangeMin;
float rangeMax;
};

```
#### FlockingDefinition
```cpp
/* 351664 */
struct FlockingDefinition
{
bool mInWater;
bool mMatchVariant;
bool mUseCenterOfMass;
int mLowFlockLimit;
int mHighFlockLimit;
float mGoalWeight;
float mLonerChance;
float mInfluenceRadius;
float mBreachInfluence;
float mSeparationWeight;
float mSeparationThreshold;
float mCohesionWeight;
float mCohesionThreshold;
float mInnerCohesionThres;
float mMinHeight;
float mMaxHeight;
float mBlockDistance;
float mBlockWeight;
};

```
#### FoliageColor
```cpp
/* 457465 */
struct FoliageColor
{
__int8 gap0[1];
};

```
#### Font;
```cpp
/* 122536 */
struct Font;

```
#### FoodItemComponent
```cpp
/* 173071 */
struct FoodItemComponent
{
const Item *mOwner;
int mNutrition;
float mSaturationModifier;
std::string mUsingConvertsTo;
FoodItemComponent::OnUseAction mOnUseAction;
Vec3 mOnUseRange;
CooldownType mCoolDownType;
int mCooldownTime;
bool mCanAlwaysEat;
std::vector<FoodItemComponent::Effect> mEffects;
std::vector<unsigned int> mRemoveEffects;
};

```
#### FoodItemComponent::Effect
```cpp
/* 172458 */
struct FoodItemComponent::Effect
{
const char *descriptionId;
int id;
int duration;
int amplifier;
float chance;
};

```
#### FormJsonValidator
```cpp
/* 428928 */
struct FormJsonValidator
{
__int8 gap0[1];
};

```
#### FrameUpdateContextBase;
```cpp
/* 90646 */
struct FrameUpdateContextBase;

```
#### FriendlySize
```cpp
/* 64313 */
struct FriendlySize
{
size_t bytes;
};

```
#### FullPlayerInventoryWrapper
```cpp
/* 424737 */
struct FullPlayerInventoryWrapper
{
PlayerInventoryProxy *mPlayerInventory;
SimpleContainer *mArmorInventory;
SimpleContainer *mHandInventory;
InventoryTransactionManager *mTransactionManager;
Player *mPlayer;
};

```
#### FunctionManager
```cpp
/* 87222 */
struct FunctionManager
{
int (**_vptr$FunctionManager)(void);
const GameRule *mGameRule;
bool mIsProcessingStack;
std::vector<FunctionManager::QueuedCommand> mCommandList;
std::unordered_map<const CommandOrigin *,FunctionManager::OriginMapping> mOriginMap;
std::unique_ptr<ICommandDispatcher> mCommandDispatcher;
std::unique_ptr<CommandOrigin> mTickOrigin;
std::unordered_map<std::string,std::unique_ptr<FunctionEntry>> mFunctions;
std::vector<FunctionEntry *> mTickFunctions;
};

```
#### FunctionManager::QueuedCommand
```cpp
/* 94529 */
struct FunctionManager::QueuedCommand
{
IFunctionEntry *mFunction;
const CommandOrigin *mOrigin;
};

```
