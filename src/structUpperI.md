#### I18n
```cpp
/* 60731 */
struct I18n
{
__int8 gap0[1];
};

```
#### I18n::LanguageChangedListener
```cpp
/* 60359 */
struct I18n::LanguageChangedListener
{
std::weak_ptr<bool> mWeakTracker;
std::function<void (const std::string &,bool)> mCallback;
};

```
#### IAppPlatform
```cpp
/* 6883 */
struct IAppPlatform
{
int (**_vptr$IAppPlatform)(void);
};

```
#### IBlockPlacementTarget
```cpp
/* 37061 */
struct IBlockPlacementTarget
{
int (**_vptr$IBlockPlacementTarget)(void);
};

```
#### IClientInstance;
```cpp
/* 13197 */
struct IClientInstance;

```
#### ICommandDispatcher
```cpp
/* 87558 */
struct ICommandDispatcher
{
int (**_vptr$ICommandDispatcher)(void);
};

```
#### IContainerManager
```cpp
/* 76093 */
struct IContainerManager
{
int (**_vptr$IContainerManager)(void);
};

```
#### IContentKeyProvider
```cpp
/* 2905 */
struct IContentKeyProvider
{
int (**_vptr$IContentKeyProvider)(void);
};

```
#### IDType<TagIDType>
```cpp
/* 38332 */
struct IDType<TagIDType>
{
size_t mID;
};

```
#### IDType<TagSetIDType>
```cpp
/* 38396 */
struct IDType<TagSetIDType>
{
size_t mID;
};

```
#### IDataInput
```cpp
/* 33518 */
struct IDataInput
{
int (**_vptr$IDataInput)(void);
};

```
#### IDataOutput
```cpp
/* 33517 */
struct IDataOutput
{
int (**_vptr$IDataOutput)(void);
};

```
#### IDefinitionSerializer
```cpp
/* 9966 */
struct IDefinitionSerializer
{
int (**_vptr$IDefinitionSerializer)(void);
std::string mName;
};

```
#### IEntitlementManager;
```cpp
/* 5778 */
struct IEntitlementManager;

```
#### IEntityComponent
```cpp
/* 44848 */
struct IEntityComponent
{
__int8 gap0[1];
};

```
#### IEntityInitializer;
```cpp
/* 10300 */
struct IEntityInitializer;

```
#### IEntityRegistryOwner
```cpp
/* 77490 */
struct IEntityRegistryOwner
{
int (**_vptr$IEntityRegistryOwner)(void);
};

```
#### IFeature
```cpp
/* 19389 */
struct IFeature
{
int (**_vptr$IFeature)(void);
};

```
#### IFileAccess
```cpp
/* 6929 */
struct IFileAccess
{
int (**_vptr$IFileAccess)(void);
};

```
#### IFileChunkUploader
```cpp
/* 101419 */
struct IFileChunkUploader
{
int (**_vptr$IFileChunkUploader)(void);
};

```
#### IFilePicker
```cpp
/* 101413 */
struct IFilePicker
{
int (**_vptr$IFilePicker)(void);
};

```
#### IFileReadAccess
```cpp
/* 482307 */
struct IFileReadAccess
{
int (**_vptr$IFileReadAccess)(void);
};

```
#### IFileWriteAccess
```cpp
/* 482309 */
struct IFileWriteAccess
{
int (**_vptr$IFileWriteAccess)(void);
};

```
#### IFunctionEntry
```cpp
/* 94530 */
struct IFunctionEntry
{
int (**_vptr$IFunctionEntry)(void);
};

```
#### IGameModuleDocumentation;
```cpp
/* 13220 */
struct IGameModuleDocumentation;

```
#### IGameModuleShared
```cpp
/* 587 */
struct IGameModuleShared
{
int (**_vptr$IGameModuleShared)(void);
};

```
#### IInPackagePacks::MetaData
```cpp
/* 9455 */
struct IInPackagePacks::MetaData
{
Core::HeapPathBuffer mPath;
bool mIsHidden;
PackCategory mPackCategory;
};

```
#### IJsonSerializable
```cpp
/* 6817 */
struct IJsonSerializable
{
int (**_vptr$IJsonSerializable)(void);
};

```
#### IMinecraftApp
```cpp
/* 5024 */
struct IMinecraftApp
{
int (**_vptr$IMinecraftApp)(void);
};

```
#### IPackTelemetry
```cpp
/* 5703 */
struct IPackTelemetry
{
int (**_vptr$IPackTelemetry)(void);
};

```
#### IPacketHandlerDispatcher;
```cpp
/* 64315 */
struct IPacketHandlerDispatcher;

```
#### IStructureConstraint
```cpp
/* 280050 */
struct IStructureConstraint
{
int (**_vptr$IStructureConstraint)(void);
};

```
#### IStructurePoolActorPredicate
```cpp
/* 35475 */
struct IStructurePoolActorPredicate
{
int (**_vptr$IStructurePoolActorPredicate)(void);
};

```
#### IStructurePoolBlockPredicate
```cpp
/* 35659 */
struct IStructurePoolBlockPredicate
{
int (**_vptr$IStructurePoolBlockPredicate)(void);
};

```
#### IStructurePoolBlockTagPredicate
```cpp
/* 35916 */
struct IStructurePoolBlockTagPredicate
{
int (**_vptr$IStructurePoolBlockTagPredicate)(void);
};

```
#### ISurfaceBuilder
```cpp
/* 88443 */
struct ISurfaceBuilder
{
int (**_vptr$ISurfaceBuilder)(void);
};

```
#### ITaskExecutionContext
```cpp
/* 484302 */
struct ITaskExecutionContext
{
int (**_vptr$ITaskExecutionContext)(void);
};

```
#### ITaskGroup
```cpp
/* 484164 */
struct ITaskGroup
{
int (**_vptr$ITaskGroup)(void);
};

```
#### ITextObject
```cpp
/* 100841 */
struct ITextObject
{
int (**_vptr$ITextObject)(void);
};

```
#### ITickingArea
```cpp
/* 34650 */
struct ITickingArea
{
int (**_vptr$ITickingArea)(void);
};

```
#### ITickingAreaView
```cpp
/* 99961 */
struct ITickingAreaView
{
int (**_vptr$ITickingAreaView)(void);
};

```
#### ITickingSystem
```cpp
/* 10238 */
struct ITickingSystem
{
int (**_vptr$ITickingSystem)(void);
};

```
#### IWorldRegistriesProvider
```cpp
/* 13149 */
struct IWorldRegistriesProvider
{
int (**_vptr$IWorldRegistriesProvider)(void);
};

```
#### IdentifierResult
```cpp
/* 99960 */
struct IdentifierResult
{
bool mValid;
std::string mIdentifier;
std::string mNamespace;
};

```
#### IdentityDictionary
```cpp
/* 293972 */
struct IdentityDictionary
{
std::unordered_map<PlayerScoreboardId,ScoreboardId> mPlayers;
std::unordered_map<ActorUniqueID,ScoreboardId> mEntities;
std::unordered_map<std::string,ScoreboardId> mFakes;
std::unordered_map<ScoreboardId,IdentityDefinition> mIdentityDefs;
};

```
#### IgnoreAutomaticFeatureRules;
```cpp
/* 198709 */
struct IgnoreAutomaticFeatureRules;

```
#### ImplicitFeatures;
```cpp
/* 222962 */
struct ImplicitFeatures;

```
#### ImprovedNoise
```cpp
/* 36175 */
struct ImprovedNoise
{
Vec3 mOrigin;
int mNoiseMap[512];
};

```
#### InMemoryFileStorage
```cpp
/* 463112 */
struct InMemoryFileStorage
{
leveldb::Env *mEnvironment;
Bedrock::Threading::Mutex mMutex;
std::vector<std::shared_ptr<InMemoryFile>> mInMemoryFiles;
std::vector<std::string> mDiskFilesToDelete;
};

```
#### IndexSet
```cpp
/* 38296 */
struct IndexSet
{
std::vector<unsigned long> mPacked;
std::vector<unsigned long> mSparse;
};

```
#### InheritanceTree<BiomeRegistry::BiomeParent>
```cpp
/* 221980 */
struct InheritanceTree<BiomeRegistry::BiomeParent>
{
std::unordered_map<std::string,InheritanceTree<BiomeRegistry::BiomeParent>::InheritanceTreeNode,std::hash<std::string>,std::equal_to<std::string >,std::allocator<std::pair<const std::string,InheritanceTree<BiomeRegistry::BiomeParent>::InheritanceTreeNode> > > mNodes;
Bedrock::Threading::Mutex mNodeLock;
};

```
#### InputHandler;
```cpp
/* 421169 */
struct InputHandler;

```
#### InsomniaComponent
```cpp
/* 56273 */
struct InsomniaComponent
{
int mTimeSinceRest;
float mDaysUntilInsomnia;
int mTicksUntilInsomnia;
};

```
#### InsomniaDefinition
```cpp
/* 107848 */
struct InsomniaDefinition
{
float mDaysUntilInsomnia;
};

```
#### IntOption::_validate::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 81832 */
struct IntOption::_validate::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### IntRange
```cpp
/* 48707 */
struct IntRange
{
int rangeMin;
int rangeMax;
};

```
#### InteractComponent
```cpp
/* 54342 */
struct InteractComponent
{
__int16 mCoolDownCounter;
};

```
#### InteractDefinition
```cpp
/* 55040 */
struct InteractDefinition
{
std::vector<Interaction> mInteractions;
};

```
#### Interaction
```cpp
/* 55041 */
struct Interaction
{
int mRequiresCoolDown;
bool mSwing;
bool mUseItem;
int mHurtItem;
ItemDefinition mTransformItem;
std::string mInteractText;
std::string mAddItemsTable;
std::string mSpawnItemsTable;
ParticleType mParticleOnStartType;
bool mParticleOffsetTowardsInteractor;
float mParticleOffsetY;
std::vector<LevelSoundEvent> mPlaySounds;
std::vector<ActorDefinitionIdentifier> mSpawnEntities;
DefinitionTrigger mOnInteraction;
};

```
#### InvalidPacksFilterGroup
```cpp
/* 5786 */
struct InvalidPacksFilterGroup
{
std::vector<PackType> packFilters;
};

```
#### InventoryAction
```cpp
/* 33288 */
struct InventoryAction
{
InventorySource mSource;
uint32_t mSlot;
ItemStack mFromItem;
ItemStack mToItem;
};

```
#### InventoryActionPacket;
```cpp
/* 77412 */
struct InventoryActionPacket;

```
#### InventorySource
```cpp
/* 33265 */
struct InventorySource
{
InventorySourceType mType;
ContainerID mContainerId;
InventorySource::InventorySourceFlags mFlags;
};

```
#### InventoryTransaction
```cpp
/* 33190 */
struct InventoryTransaction
{
std::unordered_map<InventorySource,std::vector<InventoryAction>> mActions;
std::vector<InventoryTransactionItemGroup> mContents;
};

```
#### InventoryTransactionManager
```cpp
/* 33521 */
struct InventoryTransactionManager
{
Player *mPlayer;
Unique<InventoryTransaction> mCurrentTransaction;
std::vector<InventoryAction> mExpectedActions;
};

```
#### IronGolem::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124186 */
struct IronGolem::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### IsPlayer<Actor>
```cpp
/* 93884 */
struct IsPlayer<Actor>
{
__int8 gap0[1];
};

```
#### IsPlayer<Player>
```cpp
/* 93885 */
struct IsPlayer<Player>
{
__int8 gap0[1];
};

```
#### IsotropicFaceData
```cpp
/* 45379 */
struct IsotropicFaceData
{
unsigned int mFaceTextureIsotropic;
unsigned int mIsotropicFaceEnabled;
};

```
#### Item
```cpp
/* 13203 */
struct Item
{
int (**_vptr$Item)(void);
byte m_maxStackSize;
std::string m_textureAtlasFile;
int m_frameCount;
bool m_animatesInToolbar;
bool mIsMirroredArt;
UseAnimation mUseAnim;
const std::string *mHoverTextColorFormat;
const TextureUVCoordinateSet *mIconTexture;
const TextureAtlasItem *mIconAtlas;
bool mUsesRenderingAdjustment;
Vec3 mRenderingAdjTrans;
Vec3 mRenderingAdjRot;
float mRenderingAdjScale;
__int16 mId;
std::string mDescriptionId;
std::string mRawNameId;
std::string mNamespace;
HashedString mFullName;
__int16 mMaxDamage;
__int8 mIsGlint : 1;
__int8 mHandEquipped : 1;
__int8 mIsStackedByData : 1;
__int8 mRequiresWorldBuilder : 1;
__int8 mExplodable : 1;
__int8 mShouldDespawn : 1;
__int8 mAllowOffhand : 1;
__int8 mIgnoresPermissions : 1;
__int8 mExperimental : 1;
int mMaxUseDuration;
BaseGameVersion mMinRequiredBaseGameVersion;
WeakPtr<BlockLegacy> mLegacyBlock;
CreativeItemCategory mCreativeCategory;
Item *mCraftingRemainingItem;
std::unique_ptr<FoodItemComponent> mFoodComponent;
std::unique_ptr<SeedItemComponent> mSeedComponent;
std::unique_ptr<CameraItemComponent> mCameraComponent;
std::vector<std::function<void ()>> mOnResetBAIcallbacks;
};

```
#### Item::Tier
```cpp
/* 183748 */
struct Item::Tier
{
const int mLevel;
const int mUses;
const float mSpeed;
const int mDamage;
const int mEnchantmentValue;
};

```
#### ItemAcquisitionMethodMap
```cpp
/* 182541 */
struct ItemAcquisitionMethodMap
{
__int8 gap0[1];
};

```
#### ItemDefinition
```cpp
/* 48709 */
struct ItemDefinition
{
int itemId;
int auxValue;
};

```
#### ItemEnchants
```cpp
/* 13210 */
struct ItemEnchants
{
int mSlot;
std::vector<EnchantmentInstance> mItemEnchants[3];
};

```
#### ItemEventListener;
```cpp
/* 88289 */
struct ItemEventListener;

```
#### ItemListSerializer
```cpp
/* 428929 */
struct ItemListSerializer
{
__int8 gap0[1];
};

```
#### ItemPack
```cpp
/* 184673 */
struct ItemPack
{
std::unordered_map<ItemDescriptor,int,ItemPack::KeyHasher,std::equal_to<ItemDescriptor>,std::allocator<std::pair<const ItemDescriptor,int> > > mIngredients;
};

```
#### ItemPack::KeyHasher
```cpp
/* 184548 */
struct ItemPack::KeyHasher
{
__int8 gap0[1];
};

```
#### ItemRegistry
```cpp
/* 180759 */
struct ItemRegistry
{
__int8 gap0[1];
};

```
#### ItemStackBase
```cpp
/* 33289 */
struct ItemStackBase
{
int (**_vptr$ItemStackBase)(void);
WeakPtr<Item> mItem;
Unique<CompoundTag> mUserData;
const Block *mBlock;
__int16 mAuxValue;
byte mCount;
bool mValid;
std::chrono::_V2::steady_clock::time_point mPickupTime;
bool mShowPickUp;
std::vector<const BlockLegacy *> mCanPlaceOn;
size_t mCanPlaceOnHash;
std::vector<const BlockLegacy *> mCanDestroy;
size_t mCanDestroyHash;
Tick mBlockingTick;
Unique<ItemInstance> mChargedItem;
};

```
#### ItemStackBase::_loadComponents::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 183002 */
struct ItemStackBase::_loadComponents::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### ItemState
```cpp
/* 27965 */
struct ItemState
{
int (**_vptr$ItemState)(void);
const size_t mID;
const size_t mVariationCount;
const std::string mName;
ItemState::StateListNode mNode;
};

```
#### ItemState::StateListNode
```cpp
/* 226295 */
struct ItemState::StateListNode
{
ItemState::StateListNode *mNext;
ItemState::StateListNode *mPrev;
ItemState *mState;
};

```
#### ItemStateInstance
```cpp
/* 27964 */
struct ItemStateInstance
{
const unsigned int mMaxBits;
uint32_t mStartBit;
uint32_t mNumBits;
uint32_t mVariationCount;
uint32_t mMask;
bool mInitialized;
const ItemState *mState;
};

```
#### ItemUseInventoryTransaction::resendBlocksAroundArea::$AAED32D802A7A0D4B8CDA03B8D4F5BA0
```cpp
/* 180616 */
struct ItemUseInventoryTransaction::resendBlocksAroundArea::$AAED32D802A7A0D4B8CDA03B8D4F5BA0
{
Player *player;
BlockSource *region;
};

```
#### ItemUseMethodMap
```cpp
/* 182507 */
struct ItemUseMethodMap
{
__int8 gap0[1];
};

```
#### I18n
```cpp
/* 60731 */
struct I18n
{
__int8 gap0[1];
};

```
#### I18n::LanguageChangedListener
```cpp
/* 60359 */
struct I18n::LanguageChangedListener
{
std::weak_ptr<bool> mWeakTracker;
std::function<void (const std::string &,bool)> mCallback;
};

```
#### IAppPlatform
```cpp
/* 6883 */
struct IAppPlatform
{
int (**_vptr$IAppPlatform)(void);
};

```
#### IBlockPlacementTarget
```cpp
/* 37061 */
struct IBlockPlacementTarget
{
int (**_vptr$IBlockPlacementTarget)(void);
};

```
#### IClientInstance;
```cpp
/* 13197 */
struct IClientInstance;

```
#### ICommandDispatcher
```cpp
/* 87558 */
struct ICommandDispatcher
{
int (**_vptr$ICommandDispatcher)(void);
};

```
#### IContainerManager
```cpp
/* 76093 */
struct IContainerManager
{
int (**_vptr$IContainerManager)(void);
};

```
#### IContentKeyProvider
```cpp
/* 2905 */
struct IContentKeyProvider
{
int (**_vptr$IContentKeyProvider)(void);
};

```
#### IDType<TagIDType>
```cpp
/* 38332 */
struct IDType<TagIDType>
{
size_t mID;
};

```
#### IDType<TagSetIDType>
```cpp
/* 38396 */
struct IDType<TagSetIDType>
{
size_t mID;
};

```
#### IDataInput
```cpp
/* 33518 */
struct IDataInput
{
int (**_vptr$IDataInput)(void);
};

```
#### IDataOutput
```cpp
/* 33517 */
struct IDataOutput
{
int (**_vptr$IDataOutput)(void);
};

```
#### IDefinitionSerializer
```cpp
/* 9966 */
struct IDefinitionSerializer
{
int (**_vptr$IDefinitionSerializer)(void);
std::string mName;
};

```
#### IEntitlementManager;
```cpp
/* 5778 */
struct IEntitlementManager;

```
#### IEntityComponent
```cpp
/* 44848 */
struct IEntityComponent
{
__int8 gap0[1];
};

```
#### IEntityInitializer;
```cpp
/* 10300 */
struct IEntityInitializer;

```
#### IEntityRegistryOwner
```cpp
/* 77490 */
struct IEntityRegistryOwner
{
int (**_vptr$IEntityRegistryOwner)(void);
};

```
#### IFeature
```cpp
/* 19389 */
struct IFeature
{
int (**_vptr$IFeature)(void);
};

```
#### IFileAccess
```cpp
/* 6929 */
struct IFileAccess
{
int (**_vptr$IFileAccess)(void);
};

```
#### IFileChunkUploader
```cpp
/* 101419 */
struct IFileChunkUploader
{
int (**_vptr$IFileChunkUploader)(void);
};

```
#### IFilePicker
```cpp
/* 101413 */
struct IFilePicker
{
int (**_vptr$IFilePicker)(void);
};

```
#### IFileReadAccess
```cpp
/* 482307 */
struct IFileReadAccess
{
int (**_vptr$IFileReadAccess)(void);
};

```
#### IFileWriteAccess
```cpp
/* 482309 */
struct IFileWriteAccess
{
int (**_vptr$IFileWriteAccess)(void);
};

```
#### IFunctionEntry
```cpp
/* 94530 */
struct IFunctionEntry
{
int (**_vptr$IFunctionEntry)(void);
};

```
#### IGameModuleDocumentation;
```cpp
/* 13220 */
struct IGameModuleDocumentation;

```
#### IGameModuleShared
```cpp
/* 587 */
struct IGameModuleShared
{
int (**_vptr$IGameModuleShared)(void);
};

```
#### IInPackagePacks::MetaData
```cpp
/* 9455 */
struct IInPackagePacks::MetaData
{
Core::HeapPathBuffer mPath;
bool mIsHidden;
PackCategory mPackCategory;
};

```
#### IJsonSerializable
```cpp
/* 6817 */
struct IJsonSerializable
{
int (**_vptr$IJsonSerializable)(void);
};

```
#### IMinecraftApp
```cpp
/* 5024 */
struct IMinecraftApp
{
int (**_vptr$IMinecraftApp)(void);
};

```
#### IPackTelemetry
```cpp
/* 5703 */
struct IPackTelemetry
{
int (**_vptr$IPackTelemetry)(void);
};

```
#### IPacketHandlerDispatcher;
```cpp
/* 64315 */
struct IPacketHandlerDispatcher;

```
#### IStructureConstraint
```cpp
/* 280050 */
struct IStructureConstraint
{
int (**_vptr$IStructureConstraint)(void);
};

```
#### IStructurePoolActorPredicate
```cpp
/* 35475 */
struct IStructurePoolActorPredicate
{
int (**_vptr$IStructurePoolActorPredicate)(void);
};

```
#### IStructurePoolBlockPredicate
```cpp
/* 35659 */
struct IStructurePoolBlockPredicate
{
int (**_vptr$IStructurePoolBlockPredicate)(void);
};

```
#### IStructurePoolBlockTagPredicate
```cpp
/* 35916 */
struct IStructurePoolBlockTagPredicate
{
int (**_vptr$IStructurePoolBlockTagPredicate)(void);
};

```
#### ISurfaceBuilder
```cpp
/* 88443 */
struct ISurfaceBuilder
{
int (**_vptr$ISurfaceBuilder)(void);
};

```
#### ITaskExecutionContext
```cpp
/* 484302 */
struct ITaskExecutionContext
{
int (**_vptr$ITaskExecutionContext)(void);
};

```
#### ITaskGroup
```cpp
/* 484164 */
struct ITaskGroup
{
int (**_vptr$ITaskGroup)(void);
};

```
#### ITextObject
```cpp
/* 100841 */
struct ITextObject
{
int (**_vptr$ITextObject)(void);
};

```
#### ITickingArea
```cpp
/* 34650 */
struct ITickingArea
{
int (**_vptr$ITickingArea)(void);
};

```
#### ITickingAreaView
```cpp
/* 99961 */
struct ITickingAreaView
{
int (**_vptr$ITickingAreaView)(void);
};

```
#### ITickingSystem
```cpp
/* 10238 */
struct ITickingSystem
{
int (**_vptr$ITickingSystem)(void);
};

```
#### IWorldRegistriesProvider
```cpp
/* 13149 */
struct IWorldRegistriesProvider
{
int (**_vptr$IWorldRegistriesProvider)(void);
};

```
#### IdentifierResult
```cpp
/* 99960 */
struct IdentifierResult
{
bool mValid;
std::string mIdentifier;
std::string mNamespace;
};

```
#### IdentityDictionary
```cpp
/* 293972 */
struct IdentityDictionary
{
std::unordered_map<PlayerScoreboardId,ScoreboardId> mPlayers;
std::unordered_map<ActorUniqueID,ScoreboardId> mEntities;
std::unordered_map<std::string,ScoreboardId> mFakes;
std::unordered_map<ScoreboardId,IdentityDefinition> mIdentityDefs;
};

```
#### IgnoreAutomaticFeatureRules;
```cpp
/* 198709 */
struct IgnoreAutomaticFeatureRules;

```
#### ImplicitFeatures;
```cpp
/* 222962 */
struct ImplicitFeatures;

```
#### ImprovedNoise
```cpp
/* 36175 */
struct ImprovedNoise
{
Vec3 mOrigin;
int mNoiseMap[512];
};

```
#### InMemoryFileStorage
```cpp
/* 463112 */
struct InMemoryFileStorage
{
leveldb::Env *mEnvironment;
Bedrock::Threading::Mutex mMutex;
std::vector<std::shared_ptr<InMemoryFile>> mInMemoryFiles;
std::vector<std::string> mDiskFilesToDelete;
};

```
#### IndexSet
```cpp
/* 38296 */
struct IndexSet
{
std::vector<unsigned long> mPacked;
std::vector<unsigned long> mSparse;
};

```
#### InheritanceTree<BiomeRegistry::BiomeParent>
```cpp
/* 221980 */
struct InheritanceTree<BiomeRegistry::BiomeParent>
{
std::unordered_map<std::string,InheritanceTree<BiomeRegistry::BiomeParent>::InheritanceTreeNode,std::hash<std::string>,std::equal_to<std::string >,std::allocator<std::pair<const std::string,InheritanceTree<BiomeRegistry::BiomeParent>::InheritanceTreeNode> > > mNodes;
Bedrock::Threading::Mutex mNodeLock;
};

```
#### InputHandler;
```cpp
/* 421169 */
struct InputHandler;

```
#### InsomniaComponent
```cpp
/* 56273 */
struct InsomniaComponent
{
int mTimeSinceRest;
float mDaysUntilInsomnia;
int mTicksUntilInsomnia;
};

```
#### InsomniaDefinition
```cpp
/* 107848 */
struct InsomniaDefinition
{
float mDaysUntilInsomnia;
};

```
#### IntOption::_validate::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 81832 */
struct IntOption::_validate::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### IntRange
```cpp
/* 48707 */
struct IntRange
{
int rangeMin;
int rangeMax;
};

```
#### InteractComponent
```cpp
/* 54342 */
struct InteractComponent
{
__int16 mCoolDownCounter;
};

```
#### InteractDefinition
```cpp
/* 55040 */
struct InteractDefinition
{
std::vector<Interaction> mInteractions;
};

```
#### Interaction
```cpp
/* 55041 */
struct Interaction
{
int mRequiresCoolDown;
bool mSwing;
bool mUseItem;
int mHurtItem;
ItemDefinition mTransformItem;
std::string mInteractText;
std::string mAddItemsTable;
std::string mSpawnItemsTable;
ParticleType mParticleOnStartType;
bool mParticleOffsetTowardsInteractor;
float mParticleOffsetY;
std::vector<LevelSoundEvent> mPlaySounds;
std::vector<ActorDefinitionIdentifier> mSpawnEntities;
DefinitionTrigger mOnInteraction;
};

```
#### InvalidPacksFilterGroup
```cpp
/* 5786 */
struct InvalidPacksFilterGroup
{
std::vector<PackType> packFilters;
};

```
#### InventoryAction
```cpp
/* 33288 */
struct InventoryAction
{
InventorySource mSource;
uint32_t mSlot;
ItemStack mFromItem;
ItemStack mToItem;
};

```
#### InventoryActionPacket;
```cpp
/* 77412 */
struct InventoryActionPacket;

```
#### InventorySource
```cpp
/* 33265 */
struct InventorySource
{
InventorySourceType mType;
ContainerID mContainerId;
InventorySource::InventorySourceFlags mFlags;
};

```
#### InventoryTransaction
```cpp
/* 33190 */
struct InventoryTransaction
{
std::unordered_map<InventorySource,std::vector<InventoryAction>> mActions;
std::vector<InventoryTransactionItemGroup> mContents;
};

```
#### InventoryTransactionManager
```cpp
/* 33521 */
struct InventoryTransactionManager
{
Player *mPlayer;
Unique<InventoryTransaction> mCurrentTransaction;
std::vector<InventoryAction> mExpectedActions;
};

```
#### IronGolem::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124186 */
struct IronGolem::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### IsPlayer<Actor>
```cpp
/* 93884 */
struct IsPlayer<Actor>
{
__int8 gap0[1];
};

```
#### IsPlayer<Player>
```cpp
/* 93885 */
struct IsPlayer<Player>
{
__int8 gap0[1];
};

```
#### IsotropicFaceData
```cpp
/* 45379 */
struct IsotropicFaceData
{
unsigned int mFaceTextureIsotropic;
unsigned int mIsotropicFaceEnabled;
};

```
#### Item
```cpp
/* 13203 */
struct Item
{
int (**_vptr$Item)(void);
byte m_maxStackSize;
std::string m_textureAtlasFile;
int m_frameCount;
bool m_animatesInToolbar;
bool mIsMirroredArt;
UseAnimation mUseAnim;
const std::string *mHoverTextColorFormat;
const TextureUVCoordinateSet *mIconTexture;
const TextureAtlasItem *mIconAtlas;
bool mUsesRenderingAdjustment;
Vec3 mRenderingAdjTrans;
Vec3 mRenderingAdjRot;
float mRenderingAdjScale;
__int16 mId;
std::string mDescriptionId;
std::string mRawNameId;
std::string mNamespace;
HashedString mFullName;
__int16 mMaxDamage;
__int8 mIsGlint : 1;
__int8 mHandEquipped : 1;
__int8 mIsStackedByData : 1;
__int8 mRequiresWorldBuilder : 1;
__int8 mExplodable : 1;
__int8 mShouldDespawn : 1;
__int8 mAllowOffhand : 1;
__int8 mIgnoresPermissions : 1;
__int8 mExperimental : 1;
int mMaxUseDuration;
BaseGameVersion mMinRequiredBaseGameVersion;
WeakPtr<BlockLegacy> mLegacyBlock;
CreativeItemCategory mCreativeCategory;
Item *mCraftingRemainingItem;
std::unique_ptr<FoodItemComponent> mFoodComponent;
std::unique_ptr<SeedItemComponent> mSeedComponent;
std::unique_ptr<CameraItemComponent> mCameraComponent;
std::vector<std::function<void ()>> mOnResetBAIcallbacks;
};

```
#### Item::Tier
```cpp
/* 183748 */
struct Item::Tier
{
const int mLevel;
const int mUses;
const float mSpeed;
const int mDamage;
const int mEnchantmentValue;
};

```
#### ItemAcquisitionMethodMap
```cpp
/* 182541 */
struct ItemAcquisitionMethodMap
{
__int8 gap0[1];
};

```
#### ItemDefinition
```cpp
/* 48709 */
struct ItemDefinition
{
int itemId;
int auxValue;
};

```
#### ItemEnchants
```cpp
/* 13210 */
struct ItemEnchants
{
int mSlot;
std::vector<EnchantmentInstance> mItemEnchants[3];
};

```
#### ItemEventListener;
```cpp
/* 88289 */
struct ItemEventListener;

```
#### ItemListSerializer
```cpp
/* 428929 */
struct ItemListSerializer
{
__int8 gap0[1];
};

```
#### ItemPack
```cpp
/* 184673 */
struct ItemPack
{
std::unordered_map<ItemDescriptor,int,ItemPack::KeyHasher,std::equal_to<ItemDescriptor>,std::allocator<std::pair<const ItemDescriptor,int> > > mIngredients;
};

```
#### ItemPack::KeyHasher
```cpp
/* 184548 */
struct ItemPack::KeyHasher
{
__int8 gap0[1];
};

```
#### ItemRegistry
```cpp
/* 180759 */
struct ItemRegistry
{
__int8 gap0[1];
};

```
#### ItemStackBase
```cpp
/* 33289 */
struct ItemStackBase
{
int (**_vptr$ItemStackBase)(void);
WeakPtr<Item> mItem;
Unique<CompoundTag> mUserData;
const Block *mBlock;
__int16 mAuxValue;
byte mCount;
bool mValid;
std::chrono::_V2::steady_clock::time_point mPickupTime;
bool mShowPickUp;
std::vector<const BlockLegacy *> mCanPlaceOn;
size_t mCanPlaceOnHash;
std::vector<const BlockLegacy *> mCanDestroy;
size_t mCanDestroyHash;
Tick mBlockingTick;
Unique<ItemInstance> mChargedItem;
};

```
#### ItemStackBase::_loadComponents::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 183002 */
struct ItemStackBase::_loadComponents::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### ItemState
```cpp
/* 27965 */
struct ItemState
{
int (**_vptr$ItemState)(void);
const size_t mID;
const size_t mVariationCount;
const std::string mName;
ItemState::StateListNode mNode;
};

```
#### ItemState::StateListNode
```cpp
/* 226295 */
struct ItemState::StateListNode
{
ItemState::StateListNode *mNext;
ItemState::StateListNode *mPrev;
ItemState *mState;
};

```
#### ItemStateInstance
```cpp
/* 27964 */
struct ItemStateInstance
{
const unsigned int mMaxBits;
uint32_t mStartBit;
uint32_t mNumBits;
uint32_t mVariationCount;
uint32_t mMask;
bool mInitialized;
const ItemState *mState;
};

```
#### ItemUseInventoryTransaction::resendBlocksAroundArea::$AAED32D802A7A0D4B8CDA03B8D4F5BA0
```cpp
/* 180616 */
struct ItemUseInventoryTransaction::resendBlocksAroundArea::$AAED32D802A7A0D4B8CDA03B8D4F5BA0
{
Player *player;
BlockSource *region;
};

```
#### ItemUseMethodMap
```cpp
/* 182507 */
struct ItemUseMethodMap
{
__int8 gap0[1];
};

```
