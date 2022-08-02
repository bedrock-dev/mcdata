#### MCRESULT
```cpp
/* 5830 */
struct MCRESULT
{
bool mSuccess;
MCCATEGORY mCategory;
uint16_t mCode;
};

```
#### MDCPUInformation::$0748DD84010D68691F5D57D46D5A06CC
```cpp
/* 485801 */
struct MDCPUInformation::$0748DD84010D68691F5D57D46D5A06CC
{
uint64_t processor_features[2];
};

```
#### MDCPUInformation::$506F9874F29A8F83AA6970C5F347F260
```cpp
/* 485799 */
struct MDCPUInformation::$506F9874F29A8F83AA6970C5F347F260
{
uint32_t vendor_id[3];
uint32_t version_information;
uint32_t feature_information;
uint32_t amd_extended_cpu_features;
};

```
#### MDCPUInformation::$67D17742F1A1285D3D22720ACA1D139F
```cpp
/* 485800 */
struct MDCPUInformation::$67D17742F1A1285D3D22720ACA1D139F
{
uint32_t cpuid;
uint32_t elf_hwcaps;
};

```
#### MDException
```cpp
/* 485794 */
struct MDException
{
uint32_t exception_code;
uint32_t exception_flags;
uint64_t exception_record;
uint64_t exception_address;
uint32_t number_parameters;
uint32_t __align;
uint64_t exception_information[15];
};

```
#### MDGUID
```cpp
/* 485735 */
struct MDGUID
{
uint32_t data1;
uint16_t data2;
uint16_t data3;
uint8_t data4[8];
};

```
#### MDLocationDescriptor
```cpp
/* 485745 */
struct MDLocationDescriptor
{
uint32_t data_size;
MDRVA rva;
};

```
#### MDMemoryDescriptor
```cpp
/* 485762 */
struct MDMemoryDescriptor
{
uint64_t start_of_memory_range;
MDLocationDescriptor memory;
};

```
#### MDRawContextAMD64
```cpp
/* 485786 */
struct MDRawContextAMD64
{
uint64_t p1_home;
uint64_t p2_home;
uint64_t p3_home;
uint64_t p4_home;
uint64_t p5_home;
uint64_t p6_home;
uint32_t context_flags;
uint32_t mx_csr;
uint16_t cs;
uint16_t ds;
uint16_t es;
uint16_t fs;
uint16_t gs;
uint16_t ss;
uint32_t eflags;
uint64_t dr0;
uint64_t dr1;
uint64_t dr2;
uint64_t dr3;
uint64_t dr6;
uint64_t dr7;
uint64_t rax;
uint64_t rcx;
uint64_t rdx;
uint64_t rbx;
uint64_t rsp;
uint64_t rbp;
uint64_t rsi;
uint64_t rdi;
uint64_t r8;
uint64_t r9;
uint64_t r10;
uint64_t r11;
uint64_t r12;
uint64_t r13;
uint64_t r14;
uint64_t r15;
uint64_t rip;
MDRawContextAMD64::$D520141881593523D1DB94D2DAC55DA9 _anon_0;
uint128_struct vector_register[26];
uint64_t vector_control;
uint64_t debug_control;
uint64_t last_branch_to_rip;
uint64_t last_branch_from_rip;
uint64_t last_exception_to_rip;
uint64_t last_exception_from_rip;
};

```
#### MDRawContextAMD64::$D520141881593523D1DB94D2DAC55DA9::$9C157CD774907A924DA545D68DEB0CD6
```cpp
/* 485790 */
struct MDRawContextAMD64::$D520141881593523D1DB94D2DAC55DA9::$9C157CD774907A924DA545D68DEB0CD6
{
uint128_struct header[2];
uint128_struct legacy[8];
uint128_struct xmm0;
uint128_struct xmm1;
uint128_struct xmm2;
uint128_struct xmm3;
uint128_struct xmm4;
uint128_struct xmm5;
uint128_struct xmm6;
uint128_struct xmm7;
uint128_struct xmm8;
uint128_struct xmm9;
uint128_struct xmm10;
uint128_struct xmm11;
uint128_struct xmm12;
uint128_struct xmm13;
uint128_struct xmm14;
uint128_struct xmm15;
};

```
#### MDRawDirectory
```cpp
/* 485778 */
struct MDRawDirectory
{
uint32_t stream_type;
MDLocationDescriptor location;
};

```
#### MDRawLinkMap64
```cpp
/* 485773 */
struct MDRawLinkMap64
{
uint64_t addr;
MDRVA name;
uint64_t ld;
};

```
#### MDRawSystemInfo
```cpp
/* 485797 */
struct MDRawSystemInfo
{
uint16_t processor_architecture;
uint16_t processor_level;
uint16_t processor_revision;
uint8_t number_of_processors;
uint8_t product_type;
uint32_t major_version;
uint32_t minor_version;
uint32_t build_number;
uint32_t platform_id;
MDRVA csd_version_rva;
uint16_t suite_mask;
uint16_t reserved2;
MDCPUInformation cpu;
};

```
#### MDRawThread
```cpp
/* 486200 */
struct MDRawThread
{
uint32_t thread_id;
uint32_t suspend_count;
uint32_t priority_class;
uint32_t priority;
uint64_t teb;
MDMemoryDescriptor stack;
MDLocationDescriptor thread_context;
};

```
#### MDVSFixedFileInfo
```cpp
/* 486202 */
struct MDVSFixedFileInfo
{
uint32_t signature;
uint32_t struct_version;
uint32_t file_version_hi;
uint32_t file_version_lo;
uint32_t product_version_hi;
uint32_t product_version_lo;
uint32_t file_flags_mask;
uint32_t file_flags;
uint32_t file_os;
uint32_t file_type;
uint32_t file_subtype;
uint32_t file_date_hi;
uint32_t file_date_lo;
};

```
#### MDXmmSaveArea32AMD64
```cpp
/* 485788 */
struct MDXmmSaveArea32AMD64
{
uint16_t control_word;
uint16_t status_word;
uint8_t tag_word;
uint8_t reserved1;
uint16_t error_opcode;
uint32_t error_offset;
uint16_t error_selector;
uint16_t reserved2;
uint32_t data_offset;
uint16_t data_selector;
uint16_t reserved3;
uint32_t mx_csr;
uint32_t mx_csr_mask;
uint128_struct float_registers[8];
uint128_struct xmm_registers[16];
uint8_t reserved4[96];
};

```
#### ManagedWanderingTraderComponent
```cpp
/* 106783 */
struct ManagedWanderingTraderComponent
{
__int8 gap0[1];
};

```
#### MapItemSavedData
```cpp
/* 77448 */
struct MapItemSavedData
{
size_t mUpdateInterval;
ActorUniqueID mMapId;
ActorUniqueID mParentMapId;
bool mIsFullyExplored;
bool mPreviewIncomplete;
BlockPos mOrigin;
DimensionType mDimension;
int8_t mScale;
std::vector<unsigned int> mPixels;
std::vector<std::shared_ptr<MapItemTrackedActor>> mTrackedEntities;
bool mUnlimitedTracking;
bool mDirty;
bool mLocked;
MapItemSavedData::DecorationCollection mDecorations;
};

```
#### MapItemSavedData::ChunkBounds
```cpp
/* 77450 */
struct MapItemSavedData::ChunkBounds
{
uint32_t x0;
uint32_t z0;
uint32_t x1;
uint32_t z1;
};

```
#### MapItemTrackedActor
```cpp
/* 77447 */
struct MapItemTrackedActor
{
MapItemTrackedActor::UniqueId mUniqueId;
int mStep;
bool mNeedsResend;
uint32_t mMinDirtyX;
uint32_t mMinDirtyY;
uint32_t mMaxDirtyX;
uint32_t mMaxDirtyY;
int mTick;
float mLastRotation;
MapDecoration::Type mDecorationType;
DimensionType mDimensionId;
std::unique_ptr<ChunkViewSource> mChunkViewSource;
};

```
#### MarketplaceSkinValidator
```cpp
/* 171379 */
struct MarketplaceSkinValidator
{
__int8 gap0[1];
};

```
#### Material
```cpp
/* 109109 */
struct Material
{
MaterialType mType;
bool mFlammable;
bool mNeverBuildable;
bool mAlwaysDestroyable;
bool mReplaceable;
bool mLiquid;
float mTranslucency;
bool mBlocksMotion;
bool mBlocksPrecipitation;
bool mSolid;
bool mSuperHot;
Color mMaterialColor;
};

```
#### MaterialVariants
```cpp
/* 47748 */
struct MaterialVariants
{
mce::MaterialPtr mSkinningMaterialPtr;
mce::MaterialPtr mSkinningColorMaterialPtr;
};

```
#### Matrix
```cpp
/* 109095 */
struct Matrix
{
glm::mat4x4 _m;
};

```
#### MemoryMappedFileAccess::StreamHandle
```cpp
/* 482053 */
struct MemoryMappedFileAccess::StreamHandle
{
MemoryMappedFileAccess::StreamDetails *mStream;
size_t mPosition;
};

```
#### MerchantRecipe
```cpp
/* 47228 */
struct MerchantRecipe
{
ItemInstance mBuyA;
ItemInstance mBuyB;
ItemInstance mSell;
int mTier;
int mUses;
int mMaxUses;
unsigned int mTraderExp;
bool mRewardExp;
int mDemand;
int mBuyCountA;
int mBuyCountB;
float mPriceMultiplierA;
float mPriceMultiplierB;
};

```
#### MerchantRecipeList
```cpp
/* 44344 */
struct MerchantRecipeList
{
int (**_vptr$MerchantRecipeList)(void);
std::vector<MerchantRecipe> mRecipeList;
std::vector<unsigned int> mTierExpRequirements;
};

```
#### MinecraftEventing::fireEventMultiplayerSessionUpdate::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 45360 */
struct MinecraftEventing::fireEventMultiplayerSessionUpdate::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### MinecraftPackets
```cpp
/* 72564 */
struct MinecraftPackets
{
__int8 gap0[1];
};

```
#### MinecraftScheduler
```cpp
/* 81864 */
struct MinecraftScheduler
{
__int8 gap0[1];
};

```
#### MinecraftWorkerPool
```cpp
/* 81990 */
struct MinecraftWorkerPool
{
__int8 gap0[1];
};

```
#### MingleComponent
```cpp
/* 122580 */
struct MingleComponent
{
MingleComponent::MingleState mMingleState;
ActorUniqueID mPartnerId;
ActorUniqueID mPreviousPartnerId;
};

```
#### Mob::JumpPreventionResult
```cpp
/* 116608 */
struct Mob::JumpPreventionResult
{
bool mJumpIsPrevented;
BlockPos mPreventingBlockBlockPos;
};

```
#### Mob::hurtEffects::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 116680 */
struct Mob::hurtEffects::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Mob::tickEffects::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 116679 */
struct Mob::tickEffects::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Mob::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 116681 */
struct Mob::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### MobDescriptor
```cpp
/* 88783 */
struct MobDescriptor
{
ActorFilterGroup mTargetFilter;
float mMaxDist;
float mMaxHeight;
float mMaxFlee;
float mWalkSpeedModifier;
float mSprintSpeedModifier;
bool mOverrideMustSee;
bool mMustSee;
int mMustSeeForgetTicks;
int mPriority;
};

```
#### MobEffect
```cpp
/* 44718 */
struct MobEffect
{
int (**_vptr$MobEffect)(void);
const unsigned int mId;
bool mIsHarmful;
Color mColor;
std::string mDescriptionId;
int mIcon;
float mDurationModifier;
bool mIsDisabled;
std::string mResourceName;
std::string mIconName;
bool mEffectVisible;
Util::HashString mComponentName;
std::shared_ptr<Amplifier> mValueAmplifier;
std::shared_ptr<Amplifier> mDurationAmplifier;
std::vector<std::pair<const Attribute *,std::shared_ptr<AttributeBuff> >> mAttributeBuffs;
std::vector<std::pair<const Attribute *,std::shared_ptr<AttributeModifier> >> mAttributeModifiers;
};

```
#### MobEffectComponent
```cpp
/* 57106 */
struct MobEffectComponent
{
float mEffectRange;
unsigned int mEffectId;
int mEffectTime;
ActorFilterGroup mEntityFilter;
};

```
#### MobEffectDefinition
```cpp
/* 441945 */
struct MobEffectDefinition
{
float mEffectRange;
unsigned int mEffectId;
int mEffectTime;
ActorFilterGroup mEntityFilter;
};

```
#### MobEffectInstance
```cpp
/* 44171 */
struct MobEffectInstance
{
unsigned int mId;
int mDuration;
int mDurationEasy;
int mDurationNormal;
int mDurationHard;
int mAmplifier;
bool mDisplayOnScreenTextureAnimation;
bool mAmbient;
bool mNoCounter;
bool mEffectVisible;
};

```
#### MobEventCommand::InitProxy
```cpp
/* 424408 */
struct MobEventCommand::InitProxy
{
MobEvents *mMobEvents;
};

```
#### MobSpawnHerdInfo
```cpp
/* 36555 */
struct MobSpawnHerdInfo
{
uint32_t mMinCount;
uint32_t mMaxCount;
uint32_t mHerdEventSkipCount;
uint32_t mInitialEventCount;
std::string mInitialEvent;
std::string mHerdEvent;
};

```
#### MobSpawnInfo
```cpp
/* 190279 */
struct MobSpawnInfo
{
__int8 gap0[1];
};

```
#### MolangDataDrivenGeometry
```cpp
/* 109084 */
struct MolangDataDrivenGeometry
{
DataDrivenGeometry *mGeometry;
HashedString mName;
};

```
#### MolangGenericQueryFunction
```cpp
/* 429025 */
struct MolangGenericQueryFunction
{
GenericQueryFunctionAccessor mAccessor;
std::string mDocumentation;
size_t mMinArgumentCount;
size_t mMaxArgumentCount;
};

```
#### MolangGenericQueryFunctionPtr
```cpp
/* 109088 */
struct MolangGenericQueryFunctionPtr
{
const GenericQueryFunctionAccessor *mGenericQueryFunctionPtr;
HashedString mName;
};

```
#### MolangQueryFunction
```cpp
/* 428951 */
struct MolangQueryFunction
{
QueryFunctionAccessor mAccessor;
std::string mDocumentation;
size_t mMinArgumentCount;
size_t mMaxArgumentCount;
};

```
#### MolangQueryFunctionPtr
```cpp
/* 109086 */
struct MolangQueryFunctionPtr
{
const QueryFunctionAccessor *mQueryFunctionPtr;
HashedString mName;
};

```
#### MolangScriptArg
```cpp
/* 47718 */
struct MolangScriptArg
{
MolangScriptArgData mData;
};

```
#### MonumentRoomFitter
```cpp
/* 286560 */
struct MonumentRoomFitter
{
int (**_vptr$MonumentRoomFitter)(void);
};

```
#### MountTameableDefinition
```cpp
/* 57285 */
struct MountTameableDefinition
{
int mMinTemper;
int mMaxTemper;
int mAttemptTemperMod;
std::string mFeedText;
std::string mRideText;
DefinitionTrigger mOnTame;
std::vector<FeedItem> mFeedItems;
std::vector<const Item *> mAutoRejectItems;
};

```
#### MountTamingComponent
```cpp
/* 54630 */
struct MountTamingComponent
{
int mTemper;
int mCounter;
int mTemperMod;
int mWaitCount;
};

```
#### MoveActorAbsoluteData::Header::$1C528A707D3385C2A7E4697785F3087B
```cpp
/* 77499 */
struct MoveActorAbsoluteData::Header::$1C528A707D3385C2A7E4697785F3087B
{
__int8 mIsOnGround : 1;
__int8 mTeleported : 1;
__int8 mForceMoveLocalEntity : 1;
};

```
#### MoveActorDeltaData
```cpp
/* 77500 */
struct MoveActorDeltaData
{
ActorRuntimeID mRuntimeId;
MoveActorDeltaData::Header mHeader;
int32_t mDeltaPositionX;
int32_t mDeltaPositionY;
int32_t mDeltaPositionZ;
int8_t mRotX;
int8_t mRotY;
int8_t mRotYHead;
MoveActorAbsoluteData mPreviousData;
};

```
#### MoveActorDeltaData::Header::$37FEEDC365990D64A8C0F1A90869C4B6
```cpp
/* 77502 */
struct MoveActorDeltaData::Header::$37FEEDC365990D64A8C0F1A90869C4B6
{
__int8 mContainsPositionX : 1;
__int8 mContainsPositionY : 1;
__int8 mContainsPositionZ : 1;
__int8 mContainsRotationX : 1;
__int8 mContainsRotationY : 1;
__int8 mContainsRotationYHead : 1;
__int8 mIsOnGround : 1;
__int8 mTeleported : 1;
__int8 mForceMoveLocalEntity : 1;
};

```
#### MoveControlComponent
```cpp
/* 57378 */
struct MoveControlComponent
{
bool mHasWanted;
Vec3 mWantedPosition;
bool mShouldBreach;
float mMaxTurn;
float mSpeedModifier;
Shared<MoveControl> mMoveControl;
};

```
#### MoveToPOIGoal
```cpp
/* 118329 */
struct MoveToPOIGoal
{
__int8 baseclass_0[116];
POIType mPOIType;
AABB mPOIBoundingBox;
bool mUsingBoundingBox;
bool mRequireSameY;
Unique<Path> mPath;
};

```
#### MutateBiomeTransformation;
```cpp
/* 198716 */
struct MutateBiomeTransformation;

```
#### MutationFactorData
```cpp
/* 319705 */
struct MutationFactorData
{
float mVariant;
float mExtraVariant;
float mColor;
};

```
#### MCRESULT
```cpp
/* 5830 */
struct MCRESULT
{
bool mSuccess;
MCCATEGORY mCategory;
uint16_t mCode;
};

```
#### MDCPUInformation::$0748DD84010D68691F5D57D46D5A06CC
```cpp
/* 485801 */
struct MDCPUInformation::$0748DD84010D68691F5D57D46D5A06CC
{
uint64_t processor_features[2];
};

```
#### MDCPUInformation::$506F9874F29A8F83AA6970C5F347F260
```cpp
/* 485799 */
struct MDCPUInformation::$506F9874F29A8F83AA6970C5F347F260
{
uint32_t vendor_id[3];
uint32_t version_information;
uint32_t feature_information;
uint32_t amd_extended_cpu_features;
};

```
#### MDCPUInformation::$67D17742F1A1285D3D22720ACA1D139F
```cpp
/* 485800 */
struct MDCPUInformation::$67D17742F1A1285D3D22720ACA1D139F
{
uint32_t cpuid;
uint32_t elf_hwcaps;
};

```
#### MDException
```cpp
/* 485794 */
struct MDException
{
uint32_t exception_code;
uint32_t exception_flags;
uint64_t exception_record;
uint64_t exception_address;
uint32_t number_parameters;
uint32_t __align;
uint64_t exception_information[15];
};

```
#### MDGUID
```cpp
/* 485735 */
struct MDGUID
{
uint32_t data1;
uint16_t data2;
uint16_t data3;
uint8_t data4[8];
};

```
#### MDLocationDescriptor
```cpp
/* 485745 */
struct MDLocationDescriptor
{
uint32_t data_size;
MDRVA rva;
};

```
#### MDMemoryDescriptor
```cpp
/* 485762 */
struct MDMemoryDescriptor
{
uint64_t start_of_memory_range;
MDLocationDescriptor memory;
};

```
#### MDRawContextAMD64
```cpp
/* 485786 */
struct MDRawContextAMD64
{
uint64_t p1_home;
uint64_t p2_home;
uint64_t p3_home;
uint64_t p4_home;
uint64_t p5_home;
uint64_t p6_home;
uint32_t context_flags;
uint32_t mx_csr;
uint16_t cs;
uint16_t ds;
uint16_t es;
uint16_t fs;
uint16_t gs;
uint16_t ss;
uint32_t eflags;
uint64_t dr0;
uint64_t dr1;
uint64_t dr2;
uint64_t dr3;
uint64_t dr6;
uint64_t dr7;
uint64_t rax;
uint64_t rcx;
uint64_t rdx;
uint64_t rbx;
uint64_t rsp;
uint64_t rbp;
uint64_t rsi;
uint64_t rdi;
uint64_t r8;
uint64_t r9;
uint64_t r10;
uint64_t r11;
uint64_t r12;
uint64_t r13;
uint64_t r14;
uint64_t r15;
uint64_t rip;
MDRawContextAMD64::$D520141881593523D1DB94D2DAC55DA9 _anon_0;
uint128_struct vector_register[26];
uint64_t vector_control;
uint64_t debug_control;
uint64_t last_branch_to_rip;
uint64_t last_branch_from_rip;
uint64_t last_exception_to_rip;
uint64_t last_exception_from_rip;
};

```
#### MDRawContextAMD64::$D520141881593523D1DB94D2DAC55DA9::$9C157CD774907A924DA545D68DEB0CD6
```cpp
/* 485790 */
struct MDRawContextAMD64::$D520141881593523D1DB94D2DAC55DA9::$9C157CD774907A924DA545D68DEB0CD6
{
uint128_struct header[2];
uint128_struct legacy[8];
uint128_struct xmm0;
uint128_struct xmm1;
uint128_struct xmm2;
uint128_struct xmm3;
uint128_struct xmm4;
uint128_struct xmm5;
uint128_struct xmm6;
uint128_struct xmm7;
uint128_struct xmm8;
uint128_struct xmm9;
uint128_struct xmm10;
uint128_struct xmm11;
uint128_struct xmm12;
uint128_struct xmm13;
uint128_struct xmm14;
uint128_struct xmm15;
};

```
#### MDRawDirectory
```cpp
/* 485778 */
struct MDRawDirectory
{
uint32_t stream_type;
MDLocationDescriptor location;
};

```
#### MDRawLinkMap64
```cpp
/* 485773 */
struct MDRawLinkMap64
{
uint64_t addr;
MDRVA name;
uint64_t ld;
};

```
#### MDRawSystemInfo
```cpp
/* 485797 */
struct MDRawSystemInfo
{
uint16_t processor_architecture;
uint16_t processor_level;
uint16_t processor_revision;
uint8_t number_of_processors;
uint8_t product_type;
uint32_t major_version;
uint32_t minor_version;
uint32_t build_number;
uint32_t platform_id;
MDRVA csd_version_rva;
uint16_t suite_mask;
uint16_t reserved2;
MDCPUInformation cpu;
};

```
#### MDRawThread
```cpp
/* 486200 */
struct MDRawThread
{
uint32_t thread_id;
uint32_t suspend_count;
uint32_t priority_class;
uint32_t priority;
uint64_t teb;
MDMemoryDescriptor stack;
MDLocationDescriptor thread_context;
};

```
#### MDVSFixedFileInfo
```cpp
/* 486202 */
struct MDVSFixedFileInfo
{
uint32_t signature;
uint32_t struct_version;
uint32_t file_version_hi;
uint32_t file_version_lo;
uint32_t product_version_hi;
uint32_t product_version_lo;
uint32_t file_flags_mask;
uint32_t file_flags;
uint32_t file_os;
uint32_t file_type;
uint32_t file_subtype;
uint32_t file_date_hi;
uint32_t file_date_lo;
};

```
#### MDXmmSaveArea32AMD64
```cpp
/* 485788 */
struct MDXmmSaveArea32AMD64
{
uint16_t control_word;
uint16_t status_word;
uint8_t tag_word;
uint8_t reserved1;
uint16_t error_opcode;
uint32_t error_offset;
uint16_t error_selector;
uint16_t reserved2;
uint32_t data_offset;
uint16_t data_selector;
uint16_t reserved3;
uint32_t mx_csr;
uint32_t mx_csr_mask;
uint128_struct float_registers[8];
uint128_struct xmm_registers[16];
uint8_t reserved4[96];
};

```
#### ManagedWanderingTraderComponent
```cpp
/* 106783 */
struct ManagedWanderingTraderComponent
{
__int8 gap0[1];
};

```
#### MapItemSavedData
```cpp
/* 77448 */
struct MapItemSavedData
{
size_t mUpdateInterval;
ActorUniqueID mMapId;
ActorUniqueID mParentMapId;
bool mIsFullyExplored;
bool mPreviewIncomplete;
BlockPos mOrigin;
DimensionType mDimension;
int8_t mScale;
std::vector<unsigned int> mPixels;
std::vector<std::shared_ptr<MapItemTrackedActor>> mTrackedEntities;
bool mUnlimitedTracking;
bool mDirty;
bool mLocked;
MapItemSavedData::DecorationCollection mDecorations;
};

```
#### MapItemSavedData::ChunkBounds
```cpp
/* 77450 */
struct MapItemSavedData::ChunkBounds
{
uint32_t x0;
uint32_t z0;
uint32_t x1;
uint32_t z1;
};

```
#### MapItemTrackedActor
```cpp
/* 77447 */
struct MapItemTrackedActor
{
MapItemTrackedActor::UniqueId mUniqueId;
int mStep;
bool mNeedsResend;
uint32_t mMinDirtyX;
uint32_t mMinDirtyY;
uint32_t mMaxDirtyX;
uint32_t mMaxDirtyY;
int mTick;
float mLastRotation;
MapDecoration::Type mDecorationType;
DimensionType mDimensionId;
std::unique_ptr<ChunkViewSource> mChunkViewSource;
};

```
#### MarketplaceSkinValidator
```cpp
/* 171379 */
struct MarketplaceSkinValidator
{
__int8 gap0[1];
};

```
#### Material
```cpp
/* 109109 */
struct Material
{
MaterialType mType;
bool mFlammable;
bool mNeverBuildable;
bool mAlwaysDestroyable;
bool mReplaceable;
bool mLiquid;
float mTranslucency;
bool mBlocksMotion;
bool mBlocksPrecipitation;
bool mSolid;
bool mSuperHot;
Color mMaterialColor;
};

```
#### MaterialVariants
```cpp
/* 47748 */
struct MaterialVariants
{
mce::MaterialPtr mSkinningMaterialPtr;
mce::MaterialPtr mSkinningColorMaterialPtr;
};

```
#### Matrix
```cpp
/* 109095 */
struct Matrix
{
glm::mat4x4 _m;
};

```
#### MemoryMappedFileAccess::StreamHandle
```cpp
/* 482053 */
struct MemoryMappedFileAccess::StreamHandle
{
MemoryMappedFileAccess::StreamDetails *mStream;
size_t mPosition;
};

```
#### MerchantRecipe
```cpp
/* 47228 */
struct MerchantRecipe
{
ItemInstance mBuyA;
ItemInstance mBuyB;
ItemInstance mSell;
int mTier;
int mUses;
int mMaxUses;
unsigned int mTraderExp;
bool mRewardExp;
int mDemand;
int mBuyCountA;
int mBuyCountB;
float mPriceMultiplierA;
float mPriceMultiplierB;
};

```
#### MerchantRecipeList
```cpp
/* 44344 */
struct MerchantRecipeList
{
int (**_vptr$MerchantRecipeList)(void);
std::vector<MerchantRecipe> mRecipeList;
std::vector<unsigned int> mTierExpRequirements;
};

```
#### MinecraftEventing::fireEventMultiplayerSessionUpdate::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 45360 */
struct MinecraftEventing::fireEventMultiplayerSessionUpdate::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### MinecraftPackets
```cpp
/* 72564 */
struct MinecraftPackets
{
__int8 gap0[1];
};

```
#### MinecraftScheduler
```cpp
/* 81864 */
struct MinecraftScheduler
{
__int8 gap0[1];
};

```
#### MinecraftWorkerPool
```cpp
/* 81990 */
struct MinecraftWorkerPool
{
__int8 gap0[1];
};

```
#### MingleComponent
```cpp
/* 122580 */
struct MingleComponent
{
MingleComponent::MingleState mMingleState;
ActorUniqueID mPartnerId;
ActorUniqueID mPreviousPartnerId;
};

```
#### Mob::JumpPreventionResult
```cpp
/* 116608 */
struct Mob::JumpPreventionResult
{
bool mJumpIsPrevented;
BlockPos mPreventingBlockBlockPos;
};

```
#### Mob::hurtEffects::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 116680 */
struct Mob::hurtEffects::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Mob::tickEffects::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 116679 */
struct Mob::tickEffects::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Mob::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 116681 */
struct Mob::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### MobDescriptor
```cpp
/* 88783 */
struct MobDescriptor
{
ActorFilterGroup mTargetFilter;
float mMaxDist;
float mMaxHeight;
float mMaxFlee;
float mWalkSpeedModifier;
float mSprintSpeedModifier;
bool mOverrideMustSee;
bool mMustSee;
int mMustSeeForgetTicks;
int mPriority;
};

```
#### MobEffect
```cpp
/* 44718 */
struct MobEffect
{
int (**_vptr$MobEffect)(void);
const unsigned int mId;
bool mIsHarmful;
Color mColor;
std::string mDescriptionId;
int mIcon;
float mDurationModifier;
bool mIsDisabled;
std::string mResourceName;
std::string mIconName;
bool mEffectVisible;
Util::HashString mComponentName;
std::shared_ptr<Amplifier> mValueAmplifier;
std::shared_ptr<Amplifier> mDurationAmplifier;
std::vector<std::pair<const Attribute *,std::shared_ptr<AttributeBuff> >> mAttributeBuffs;
std::vector<std::pair<const Attribute *,std::shared_ptr<AttributeModifier> >> mAttributeModifiers;
};

```
#### MobEffectComponent
```cpp
/* 57106 */
struct MobEffectComponent
{
float mEffectRange;
unsigned int mEffectId;
int mEffectTime;
ActorFilterGroup mEntityFilter;
};

```
#### MobEffectDefinition
```cpp
/* 441945 */
struct MobEffectDefinition
{
float mEffectRange;
unsigned int mEffectId;
int mEffectTime;
ActorFilterGroup mEntityFilter;
};

```
#### MobEffectInstance
```cpp
/* 44171 */
struct MobEffectInstance
{
unsigned int mId;
int mDuration;
int mDurationEasy;
int mDurationNormal;
int mDurationHard;
int mAmplifier;
bool mDisplayOnScreenTextureAnimation;
bool mAmbient;
bool mNoCounter;
bool mEffectVisible;
};

```
#### MobEventCommand::InitProxy
```cpp
/* 424408 */
struct MobEventCommand::InitProxy
{
MobEvents *mMobEvents;
};

```
#### MobSpawnHerdInfo
```cpp
/* 36555 */
struct MobSpawnHerdInfo
{
uint32_t mMinCount;
uint32_t mMaxCount;
uint32_t mHerdEventSkipCount;
uint32_t mInitialEventCount;
std::string mInitialEvent;
std::string mHerdEvent;
};

```
#### MobSpawnInfo
```cpp
/* 190279 */
struct MobSpawnInfo
{
__int8 gap0[1];
};

```
#### MolangDataDrivenGeometry
```cpp
/* 109084 */
struct MolangDataDrivenGeometry
{
DataDrivenGeometry *mGeometry;
HashedString mName;
};

```
#### MolangGenericQueryFunction
```cpp
/* 429025 */
struct MolangGenericQueryFunction
{
GenericQueryFunctionAccessor mAccessor;
std::string mDocumentation;
size_t mMinArgumentCount;
size_t mMaxArgumentCount;
};

```
#### MolangGenericQueryFunctionPtr
```cpp
/* 109088 */
struct MolangGenericQueryFunctionPtr
{
const GenericQueryFunctionAccessor *mGenericQueryFunctionPtr;
HashedString mName;
};

```
#### MolangQueryFunction
```cpp
/* 428951 */
struct MolangQueryFunction
{
QueryFunctionAccessor mAccessor;
std::string mDocumentation;
size_t mMinArgumentCount;
size_t mMaxArgumentCount;
};

```
#### MolangQueryFunctionPtr
```cpp
/* 109086 */
struct MolangQueryFunctionPtr
{
const QueryFunctionAccessor *mQueryFunctionPtr;
HashedString mName;
};

```
#### MolangScriptArg
```cpp
/* 47718 */
struct MolangScriptArg
{
MolangScriptArgData mData;
};

```
#### MonumentRoomFitter
```cpp
/* 286560 */
struct MonumentRoomFitter
{
int (**_vptr$MonumentRoomFitter)(void);
};

```
#### MountTameableDefinition
```cpp
/* 57285 */
struct MountTameableDefinition
{
int mMinTemper;
int mMaxTemper;
int mAttemptTemperMod;
std::string mFeedText;
std::string mRideText;
DefinitionTrigger mOnTame;
std::vector<FeedItem> mFeedItems;
std::vector<const Item *> mAutoRejectItems;
};

```
#### MountTamingComponent
```cpp
/* 54630 */
struct MountTamingComponent
{
int mTemper;
int mCounter;
int mTemperMod;
int mWaitCount;
};

```
#### MoveActorAbsoluteData::Header::$1C528A707D3385C2A7E4697785F3087B
```cpp
/* 77499 */
struct MoveActorAbsoluteData::Header::$1C528A707D3385C2A7E4697785F3087B
{
__int8 mIsOnGround : 1;
__int8 mTeleported : 1;
__int8 mForceMoveLocalEntity : 1;
};

```
#### MoveActorDeltaData
```cpp
/* 77500 */
struct MoveActorDeltaData
{
ActorRuntimeID mRuntimeId;
MoveActorDeltaData::Header mHeader;
int32_t mDeltaPositionX;
int32_t mDeltaPositionY;
int32_t mDeltaPositionZ;
int8_t mRotX;
int8_t mRotY;
int8_t mRotYHead;
MoveActorAbsoluteData mPreviousData;
};

```
#### MoveActorDeltaData::Header::$37FEEDC365990D64A8C0F1A90869C4B6
```cpp
/* 77502 */
struct MoveActorDeltaData::Header::$37FEEDC365990D64A8C0F1A90869C4B6
{
__int8 mContainsPositionX : 1;
__int8 mContainsPositionY : 1;
__int8 mContainsPositionZ : 1;
__int8 mContainsRotationX : 1;
__int8 mContainsRotationY : 1;
__int8 mContainsRotationYHead : 1;
__int8 mIsOnGround : 1;
__int8 mTeleported : 1;
__int8 mForceMoveLocalEntity : 1;
};

```
#### MoveControlComponent
```cpp
/* 57378 */
struct MoveControlComponent
{
bool mHasWanted;
Vec3 mWantedPosition;
bool mShouldBreach;
float mMaxTurn;
float mSpeedModifier;
Shared<MoveControl> mMoveControl;
};

```
#### MoveToPOIGoal
```cpp
/* 118329 */
struct MoveToPOIGoal
{
__int8 baseclass_0[116];
POIType mPOIType;
AABB mPOIBoundingBox;
bool mUsingBoundingBox;
bool mRequireSameY;
Unique<Path> mPath;
};

```
#### MutateBiomeTransformation;
```cpp
/* 198716 */
struct MutateBiomeTransformation;

```
#### MutationFactorData
```cpp
/* 319705 */
struct MutationFactorData
{
float mVariant;
float mExtraVariant;
float mColor;
};

```
