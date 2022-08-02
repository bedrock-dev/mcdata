#### EducationLocalLevelSettings
```cpp
/* 4341 */
struct EducationLocalLevelSettings
{
bool hasQuiz;
};

```
#### EducationMetadata
```cpp
/* 83525 */
struct EducationMetadata
{
EducationMetadata::ContentType mContentType;
int mEstimatedTime;
std::string mDescription;
std::string mGoals;
std::vector<std::string> mTasks;
std::vector<std::string> mInstructions;
std::string mLinkToMore;
int mOrder;
EducationMetadata::UserType mRole;
};

```
#### ElementInfo
```cpp
/* 226408 */
struct ElementInfo
{
ElementCategory mCategory;
const char *mName;
};

```
#### Elf32_Ehdr
```cpp
/* 486288 */
struct Elf32_Ehdr
{
unsigned __int8 e_ident[16];
Elf32_Half e_type;
Elf32_Half e_machine;
Elf32_Word e_version;
Elf32_Addr e_entry;
Elf32_Off e_phoff;
Elf32_Off e_shoff;
Elf32_Word e_flags;
Elf32_Half e_ehsize;
Elf32_Half e_phentsize;
Elf32_Half e_phnum;
Elf32_Half e_shentsize;
Elf32_Half e_shnum;
Elf32_Half e_shstrndx;
};

```
#### Elf32_Nhdr
```cpp
/* 486275 */
struct Elf32_Nhdr
{
Elf32_Word n_namesz;
Elf32_Word n_descsz;
Elf32_Word n_type;
};

```
#### Elf32_Phdr
```cpp
/* 486303 */
struct Elf32_Phdr
{
Elf32_Word p_type;
Elf32_Off p_offset;
Elf32_Addr p_vaddr;
Elf32_Addr p_paddr;
Elf32_Word p_filesz;
Elf32_Word p_memsz;
Elf32_Word p_flags;
Elf32_Word p_align;
};

```
#### Elf32_Shdr
```cpp
/* 486294 */
struct Elf32_Shdr
{
Elf32_Word sh_name;
Elf32_Word sh_type;
Elf32_Word sh_flags;
Elf32_Addr sh_addr;
Elf32_Off sh_offset;
Elf32_Word sh_size;
Elf32_Word sh_link;
Elf32_Word sh_info;
Elf32_Word sh_addralign;
Elf32_Word sh_entsize;
};

```
#### Elf64_Dyn
```cpp
/* 3 */
struct Elf64_Dyn
{
unsigned __int64 d_tag;
unsigned __int64 d_un;
};

```
#### Elf64_Dyn_0
```cpp
/* 486211 */
struct Elf64_Dyn_0
{
Elf64_Sxword d_tag;
Elf64_Dyn_0::$066E28680D19619270844BF7D45F9743 d_un;
};

```
#### Elf64_Ehdr
```cpp
/* 486284 */
struct Elf64_Ehdr
{
unsigned __int8 e_ident[16];
Elf64_Half e_type;
Elf64_Half e_machine;
Elf64_Word e_version;
Elf64_Addr e_entry;
Elf64_Off e_phoff;
Elf64_Off e_shoff;
Elf64_Word e_flags;
Elf64_Half e_ehsize;
Elf64_Half e_phentsize;
Elf64_Half e_phnum;
Elf64_Half e_shentsize;
Elf64_Half e_shnum;
Elf64_Half e_shstrndx;
};

```
#### Elf64_Nhdr
```cpp
/* 486280 */
struct Elf64_Nhdr
{
Elf64_Word n_namesz;
Elf64_Word n_descsz;
Elf64_Word n_type;
};

```
#### Elf64_Phdr
```cpp
/* 486216 */
struct Elf64_Phdr
{
Elf64_Word p_type;
Elf64_Word p_flags;
Elf64_Off p_offset;
Elf64_Addr p_vaddr;
Elf64_Addr p_paddr;
Elf64_Xword p_filesz;
Elf64_Xword p_memsz;
Elf64_Xword p_align;
};

```
#### Elf64_Shdr
```cpp
/* 486299 */
struct Elf64_Shdr
{
Elf64_Word sh_name;
Elf64_Word sh_type;
Elf64_Xword sh_flags;
Elf64_Addr sh_addr;
Elf64_Off sh_offset;
Elf64_Xword sh_size;
Elf64_Word sh_link;
Elf64_Word sh_info;
Elf64_Xword sh_addralign;
Elf64_Xword sh_entsize;
};

```
#### Elf64_auxv_t
```cpp
/* 486232 */
struct Elf64_auxv_t
{
uint64_t a_type;
Elf64_auxv_t::$218B18A37F77BA833A070E25C7DC6FF2 a_un;
};

```
#### EnableGetWeakRef<EntityRefTraits>
```cpp
/* 9892 */
struct EnableGetWeakRef<EntityRefTraits>
{
__int8 gap0[1];
};

```
#### EnableGetWeakRef<EntityRegistryRefTraits>
```cpp
/* 9764 */
struct EnableGetWeakRef<EntityRegistryRefTraits>
{
__int8 gap0[1];
};

```
#### EnchantUtils
```cpp
/* 185725 */
struct EnchantUtils
{
__int8 gap0[1];
};

```
#### EnchantmentInstance
```cpp
/* 44085 */
struct EnchantmentInstance
{
Enchant::Type mEnchantType;
int mLevel;
};

```
#### EndCityPieces
```cpp
/* 461975 */
struct EndCityPieces
{
__int8 gap0[1];
};

```
#### EndCityPieces::SectionGenerator
```cpp
/* 461726 */
struct EndCityPieces::SectionGenerator
{
int (**_vptr$SectionGenerator)(void);
};

```
#### EndDragonFight
```cpp
/* 169784 */
struct EndDragonFight
{
BlockSource *mRegion;
std::vector<int> mGateways;
Unique<BlockPatternBuilder> mExitPortalPattern;
int mCrystalsAlive;
int mTicksSinceCrystalsScanned;
int mTicksSincePortalScanned;
int mTicksSinceLastPlayerScan;
bool mDragonKilled;
bool mPreviouslyKilled;
bool mDragonSpawned;
ActorUniqueID mDragonUUID;
BlockPos mPortalLocation;
const BlockPos mDragonSpawnPos;
RespawnAnimation mRespawnStage;
int mRespawnTime;
std::vector<ActorUniqueID> mRespawnCrystals;
EndDragonFightVersion mFightVersion;
EndDragonFight::GateWayGenerator mEntryGenerator;
EndDragonFight::GateWayGenerator mExitGenerator;
EndDragonFight::GatewayTask mBuildingOrVerifyingEndGatewayPair;
std::deque<std::tuple<EndDragonFight::GatewayTask,EndDragonFight::GateWayGenerator,EndDragonFight::GateWayGenerator>> mGatewayTasks;
};

```
#### EndDragonFight::_setEndGatewayBlockActorExitPosition::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 255257 */
struct EndDragonFight::_setEndGatewayBlockActorExitPosition::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### EndGatewayBlock::animateTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 459352 */
struct EndGatewayBlock::animateTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### EndPortalShape
```cpp
/* 459395 */
struct EndPortalShape
{
BlockSource *mSource;
int mRightDir;
int mLeftDir;
int mDepthDir;
BlockPos mBottomLeft;
BlockPos mOrigin;
int mBlockDirection;
std::vector<std::vector<const Block *>> mPortalPattern;
};

```
#### EntityCanonicalName::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 114949 */
struct EntityCanonicalName::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### EntityId
```cpp
/* 9730 */
struct EntityId
{
uint32_t mRawId;
};

```
#### EntityNetId
```cpp
/* 77830 */
struct EntityNetId
{
uint32_t mRawId;
};

```
#### EntityOptionalOwnerRef
```cpp
/* 187576 */
struct EntityOptionalOwnerRef
{
OwnerPtr<EntityId> mOwnedEntity;
WeakRef<EntityId> mWeakEntity;
};

```
#### EntityRefTraits
```cpp
/* 13169 */
struct EntityRefTraits
{
__int8 gap0[1];
};

```
#### EntityRegistryBase::ICanModifyComponentPoolDuringView
```cpp
/* 9763 */
struct EntityRegistryBase::ICanModifyComponentPoolDuringView
{
__int8 gap0[1];
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,ActorComponent,RailMovementComponent>
```cpp
/* 421160 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,ActorComponent,RailMovementComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ActorFlagComponent<BurnsInDaylightFlag> >
```cpp
/* 52163 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ActorFlagComponent<BurnsInDaylightFlag> >
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ActorFlagComponent<EnvironmentSensorFlag> >
```cpp
/* 55312 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ActorFlagComponent<EnvironmentSensorFlag> >
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,AgeableComponent>
```cpp
/* 49716 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,AgeableComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,AgentCommandComponent>
```cpp
/* 49877 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,AgentCommandComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,AngryComponent>
```cpp
/* 50037 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,AngryComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,AreaAttackComponent>
```cpp
/* 50162 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,AreaAttackComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BalloonComponent>
```cpp
/* 50283 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BalloonComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BehaviorComponent>
```cpp
/* 50659 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BehaviorComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BlockBreakSensorComponent>
```cpp
/* 50845 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BlockBreakSensorComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BodyControlComponent>
```cpp
/* 50994 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BodyControlComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BoostableComponent>
```cpp
/* 51166 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BoostableComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BossComponent>
```cpp
/* 51424 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BossComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BreakBlocksComponent>
```cpp
/* 51545 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BreakBlocksComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BreakDoorAnnotationComponent>
```cpp
/* 51676 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BreakDoorAnnotationComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BreathableComponent>
```cpp
/* 51808 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BreathableComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BreedableComponent>
```cpp
/* 51933 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BreedableComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BribeableComponent>
```cpp
/* 52048 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BribeableComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,CommandBlockComponent>
```cpp
/* 52285 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,CommandBlockComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,DamageOverTimeComponent>
```cpp
/* 52411 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,DamageOverTimeComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,DanceComponent>
```cpp
/* 52561 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,DanceComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,DespawnComponent>
```cpp
/* 52676 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,DespawnComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,DwellerComponent>
```cpp
/* 53673 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,DwellerComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,EntitySensorComponent>
```cpp
/* 53787 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,EntitySensorComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ExplodeComponent>
```cpp
/* 55438 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ExplodeComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,FlockingComponent>
```cpp
/* 55563 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,FlockingComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,GoalSelectorComponent>
```cpp
/* 55764 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,GoalSelectorComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,GrowsCropComponent>
```cpp
/* 55920 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,GrowsCropComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,HopperComponent>
```cpp
/* 56037 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,HopperComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,HurtOnConditionComponent>
```cpp
/* 56245 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,HurtOnConditionComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,InsomniaComponent>
```cpp
/* 56363 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,InsomniaComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,InteractComponent>
```cpp
/* 56431 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,InteractComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,JumpControlComponent>
```cpp
/* 56579 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,JumpControlComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,LeashableComponent>
```cpp
/* 56781 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,LeashableComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,LegacyTradeableComponent>
```cpp
/* 59812 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,LegacyTradeableComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,LookAtComponent>
```cpp
/* 56937 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,LookAtComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,LookControlComponent>
```cpp
/* 57082 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,LookControlComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,MobEffectComponent>
```cpp
/* 57196 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,MobEffectComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,MountTamingComponent>
```cpp
/* 57342 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,MountTamingComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,MoveControlComponent>
```cpp
/* 57477 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,MoveControlComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,NavigationComponent>
```cpp
/* 57608 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,NavigationComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,OpenDoorAnnotationComponent>
```cpp
/* 57794 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,OpenDoorAnnotationComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,PeekComponent>
```cpp
/* 57946 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,PeekComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ProjectileComponent>
```cpp
/* 58238 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ProjectileComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,RaidBossComponent>
```cpp
/* 58399 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,RaidBossComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,RailActivatorComponent>
```cpp
/* 58513 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,RailActivatorComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ScaffoldingClimberComponent>
```cpp
/* 58628 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ScaffoldingClimberComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ScaleByAgeComponent,AgeableComponent>
```cpp
/* 58749 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ScaleByAgeComponent,AgeableComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,SchedulerComponent>
```cpp
/* 58913 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,SchedulerComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,SensingComponent>
```cpp
/* 59056 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,SensingComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,SpawnActorComponent>
```cpp
/* 59340 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,SpawnActorComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TargetNearbyComponent>
```cpp
/* 59459 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TargetNearbyComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TeleportComponent>
```cpp
/* 59575 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TeleportComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TimerComponent>
```cpp
/* 59738 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TimerComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TrailComponent>
```cpp
/* 59926 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TrailComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TransformationComponent>
```cpp
/* 60050 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TransformationComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,SurfaceBuilderComponent>
```cpp
/* 222971 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,SurfaceBuilderComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryRefTraits
```cpp
/* 13158 */
struct EntityRegistryRefTraits
{
__int8 gap0[1];
};

```
#### EntitySensorComponent
```cpp
/* 53697 */
struct EntitySensorComponent
{
float mSensorRange;
int mMinimumCount;
int mMaximumCount;
bool mRequireAll;
ActorFilterGroup mEventCondition;
std::string mEventName;
};

```
#### EntitySensorDefinition
```cpp
/* 340470 */
struct EntitySensorDefinition
{
float mSensorRange;
int mMinimumCount;
int mMaximumCount;
bool mRequireAll;
ActorFilterGroup mEventCondition;
std::string mEventName;
};

```
#### EntitySystems
```cpp
/* 13221 */
struct EntitySystems
{
std::vector<std::unique_ptr<ITickingSystem>> mTickingSystems;
Unique<PlayerInteractionSystem> mPlayerInteractionSystem;
};

```
#### EnumBitset<RenderCapability,14>
```cpp
/* 483999 */
struct EnumBitset<RenderCapability,14>
{
std::bitset<14> mBitset;
};

```
#### EnumBitset<ScriptLogType,3>
```cpp
/* 99213 */
struct EnumBitset<ScriptLogType,3>
{
std::bitset<3> mBitset;
};

```
#### EnvironmentRequirement
```cpp
/* 319446 */
struct EnvironmentRequirement
{
std::set<const Block *> mBlockTypes;
unsigned int mNumBlocksRequired;
unsigned int mSearchRadius;
};

```
#### EnvironmentSensorDefinition
```cpp
/* 55250 */
struct EnvironmentSensorDefinition
{
std::vector<DefinitionTrigger> mTriggers;
};

```
#### EnvironmentSensorFlag;
```cpp
/* 55299 */
struct EnvironmentSensorFlag;

```
#### EquippableComponent
```cpp
/* 100067 */
struct EquippableComponent
{
std::vector<SlotDescriptor> mSlots;
};

```
#### EquippableDefinition
```cpp
/* 100099 */
struct EquippableDefinition
{
std::vector<SlotDescriptor> mSlots;
};

```
#### ErrorPathStack
```cpp
/* 83338 */
struct ErrorPathStack
{
std::vector<std::string> *mErrorPath;
};

```
#### EvalParams
```cpp
/* 109091 */
struct EvalParams
{
MolangVariableMap mTempVariables;
};

```
#### EventCoordinator<ActorEventListener>
```cpp
/* 13234 */
struct EventCoordinator<ActorEventListener>
{
std::vector<ActorEventListener *> mListeners;
std::vector<std::function<EventResult (ActorEventListener *)>> mEventsToProcess;
std::thread::id mThreadId;
bool mThreadIdInitialized;
unsigned int mThreadCheckIndex;
};

```
#### EventCoordinator<BlockEventListener>
```cpp
/* 13235 */
struct EventCoordinator<BlockEventListener>
{
std::vector<BlockEventListener *> mListeners;
std::vector<std::function<EventResult (BlockEventListener *)>> mEventsToProcess;
std::thread::id mThreadId;
bool mThreadIdInitialized;
unsigned int mThreadCheckIndex;
};

```
#### EventCoordinator<ItemEventListener>
```cpp
/* 88276 */
struct EventCoordinator<ItemEventListener>
{
std::vector<ItemEventListener *> mListeners;
std::vector<std::function<EventResult (ItemEventListener *)>> mEventsToProcess;
std::thread::id mThreadId;
bool mThreadIdInitialized;
unsigned int mThreadCheckIndex;
};

```
#### EventCoordinator<LevelEventListener>
```cpp
/* 88242 */
struct EventCoordinator<LevelEventListener>
{
std::vector<LevelEventListener *> mListeners;
std::vector<std::function<EventResult (LevelEventListener *)>> mEventsToProcess;
std::thread::id mThreadId;
bool mThreadIdInitialized;
unsigned int mThreadCheckIndex;
};

```
#### EventCoordinator<NetworkPacketEventListener>
```cpp
/* 63025 */
struct EventCoordinator<NetworkPacketEventListener>
{
std::vector<NetworkPacketEventListener *> mListeners;
std::vector<std::function<EventResult (NetworkPacketEventListener *)>> mEventsToProcess;
std::thread::id mThreadId;
bool mThreadIdInitialized;
unsigned int mThreadCheckIndex;
};

```
#### EventCoordinator<PlayerEventListener>
```cpp
/* 13233 */
struct EventCoordinator<PlayerEventListener>
{
std::vector<PlayerEventListener *> mListeners;
std::vector<std::function<EventResult (PlayerEventListener *)>> mEventsToProcess;
std::thread::id mThreadId;
bool mThreadIdInitialized;
unsigned int mThreadCheckIndex;
};

```
#### EventCoordinator<ScriptEventListener>
```cpp
/* 99208 */
struct EventCoordinator<ScriptEventListener>
{
std::vector<ScriptEventListener *> mListeners;
std::vector<std::function<EventResult (ScriptEventListener *)>> mEventsToProcess;
std::thread::id mThreadId;
bool mThreadIdInitialized;
unsigned int mThreadCheckIndex;
};

```
#### EventCoordinator<ServerInstanceEventListener>
```cpp
/* 439 */
struct EventCoordinator<ServerInstanceEventListener>
{
std::vector<ServerInstanceEventListener *> mListeners;
std::vector<std::function<EventResult (ServerInstanceEventListener *)>> mEventsToProcess;
std::thread::id mThreadId;
bool mThreadIdInitialized;
unsigned int mThreadCheckIndex;
};

```
#### EventInfo
```cpp
/* 99958 */
struct EventInfo
{
std::string mEventName;
};

```
#### EventPacket::Data
```cpp
/* 13310 */
struct EventPacket::Data
{
EventPacket::Type mType;
Util::Byte mUsePlayerID;
EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB _anon_0;
std::string mEntityName;
std::string mCommandName;
std::string mResultKey;
std::string mResultString;
std::string mErrorList;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$103E0A04995712B8D39AE343EA50817C
```cpp
/* 13313 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$103E0A04995712B8D39AE343EA50817C
{
MinecraftEventing::AchievementIds mAchievementId;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$43709AFFC502E7A13BA1073C610D8549
```cpp
/* 13317 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$43709AFFC502E7A13BA1073C610D8549
{
bool mKilledByOwner;
int64_t mKillerEntityId;
int64_t mKilledMobId;
int32_t mDamageSource;
ActorType mKilledMobType;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$5B316CCC98B60A95F92E231D823C7BE3
```cpp
/* 13328 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$5B316CCC98B60A95F92E231D823C7BE3
{
__int16 mItemId;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$61A09D83502661C769654363F1382707
```cpp
/* 13330 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$61A09D83502661C769654363F1382707
{
float mPositionDelta;
float mObservedScore;
float mThresholdDistance;
float mThresholdScore;
int mThresholdDuration_ms;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$731817FF9A1D8A7F7DE35EC2646A852E
```cpp
/* 13316 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$731817FF9A1D8A7F7DE35EC2646A852E
{
int mFromDimension;
int mToDimension;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$922D880B3EFBF7F2063214579535BD95
```cpp
/* 13331 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$922D880B3EFBF7F2063214579535BD95
{
MovementEventType mEventType;
float mObservedScore;
float mAveragePosDelta;
float mTotalPosDelta;
float mMinPosDelta;
float mMaxPosDelta;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$92C02C0BC48AA2105788421214C7C1B7
```cpp
/* 13322 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$92C02C0BC48AA2105788421214C7C1B7
{
int32_t mResult;
int32_t mResultNumber;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$A01EA2DF6590CA7397A67CCFB21A7F86
```cpp
/* 13323 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$A01EA2DF6590CA7397A67CCFB21A7F86
{
int32_t mItemId;
int32_t mItemAux;
int32_t mLayerIndex;
int32_t mPatternId;
int32_t mPatternColor;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$A05CE60CF11B1B9B38674E8A09580618
```cpp
/* 13327 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$A05CE60CF11B1B9B38674E8A09580618
{
__int16 mItemId;
MinecraftEventing::POIBlockInteractionType mInteractionType;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$CFC5415F71714946B1482A4EA070D3F8
```cpp
/* 13315 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$CFC5415F71714946B1482A4EA070D3F8
{
int mBuiltInDimension;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$EA4713E4A3566411BE29AE280F22E9DF
```cpp
/* 13324 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$EA4713E4A3566411BE29AE280F22E9DF
{
int32_t mSuccessCount;
int32_t mErrorCount;
};

```
#### ExecCtxNext;
```cpp
/* 486933 */
struct ExecCtxNext;

```
#### ExecCtxPluck;
```cpp
/* 486934 */
struct ExecCtxPluck;

```
#### ExpandoModelElement
```cpp
/* 175620 */
struct ExpandoModelElement
{
ContainerItemStack item;
ContainerExpandStatus status;
std::string groupName;
};

```
#### ExperienceRewardComponent
```cpp
/* 107631 */
struct ExperienceRewardComponent
{
std::vector<ExpressionNode> mOnBred;
std::vector<ExpressionNode> mOnDeath;
};

```
#### ExperienceRewardDefinition
```cpp
/* 348090 */
struct ExperienceRewardDefinition
{
std::vector<ExpressionNode> mOnBred;
std::vector<ExpressionNode> mOnDeath;
};

```
#### Explosion
```cpp
/* 190223 */
struct Explosion
{
Vec3 mPos;
float mRadius;
BlockPosSet mToBlow;
bool mFire;
bool mBreaking;
bool mAllowUnderwater;
Actor *mSource;
BlockSource *mRegion;
float mMaxResistance;
Random mRandom;
};

```
#### ExpressionNode
```cpp
/* 47716 */
struct ExpressionNode
{
ExpressionOp mOp;
MolangScriptArg mValue;
std::vector<ExpressionNode> mChildren;
uint64_t mUsedTokenFlags;
std::string _mExpressionString;
};

```
#### ExtendedCertificate
```cpp
/* 8031 */
struct ExtendedCertificate
{
__int8 gap0[1];
};

```
#### ExtraLicenseData
```cpp
/* 45339 */
struct ExtraLicenseData
{
int64_t mValidationTime;
int64_t mRetryUntilTime;
int64_t mRetryAttempts;
};

```
#### EyeOfEnder::normalTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 170703 */
struct EyeOfEnder::normalTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### EducationLocalLevelSettings
```cpp
/* 4341 */
struct EducationLocalLevelSettings
{
bool hasQuiz;
};

```
#### EducationMetadata
```cpp
/* 83525 */
struct EducationMetadata
{
EducationMetadata::ContentType mContentType;
int mEstimatedTime;
std::string mDescription;
std::string mGoals;
std::vector<std::string> mTasks;
std::vector<std::string> mInstructions;
std::string mLinkToMore;
int mOrder;
EducationMetadata::UserType mRole;
};

```
#### ElementInfo
```cpp
/* 226408 */
struct ElementInfo
{
ElementCategory mCategory;
const char *mName;
};

```
#### Elf32_Ehdr
```cpp
/* 486288 */
struct Elf32_Ehdr
{
unsigned __int8 e_ident[16];
Elf32_Half e_type;
Elf32_Half e_machine;
Elf32_Word e_version;
Elf32_Addr e_entry;
Elf32_Off e_phoff;
Elf32_Off e_shoff;
Elf32_Word e_flags;
Elf32_Half e_ehsize;
Elf32_Half e_phentsize;
Elf32_Half e_phnum;
Elf32_Half e_shentsize;
Elf32_Half e_shnum;
Elf32_Half e_shstrndx;
};

```
#### Elf32_Nhdr
```cpp
/* 486275 */
struct Elf32_Nhdr
{
Elf32_Word n_namesz;
Elf32_Word n_descsz;
Elf32_Word n_type;
};

```
#### Elf32_Phdr
```cpp
/* 486303 */
struct Elf32_Phdr
{
Elf32_Word p_type;
Elf32_Off p_offset;
Elf32_Addr p_vaddr;
Elf32_Addr p_paddr;
Elf32_Word p_filesz;
Elf32_Word p_memsz;
Elf32_Word p_flags;
Elf32_Word p_align;
};

```
#### Elf32_Shdr
```cpp
/* 486294 */
struct Elf32_Shdr
{
Elf32_Word sh_name;
Elf32_Word sh_type;
Elf32_Word sh_flags;
Elf32_Addr sh_addr;
Elf32_Off sh_offset;
Elf32_Word sh_size;
Elf32_Word sh_link;
Elf32_Word sh_info;
Elf32_Word sh_addralign;
Elf32_Word sh_entsize;
};

```
#### Elf64_Dyn
```cpp
/* 3 */
struct Elf64_Dyn
{
unsigned __int64 d_tag;
unsigned __int64 d_un;
};

```
#### Elf64_Dyn_0
```cpp
/* 486211 */
struct Elf64_Dyn_0
{
Elf64_Sxword d_tag;
Elf64_Dyn_0::$066E28680D19619270844BF7D45F9743 d_un;
};

```
#### Elf64_Ehdr
```cpp
/* 486284 */
struct Elf64_Ehdr
{
unsigned __int8 e_ident[16];
Elf64_Half e_type;
Elf64_Half e_machine;
Elf64_Word e_version;
Elf64_Addr e_entry;
Elf64_Off e_phoff;
Elf64_Off e_shoff;
Elf64_Word e_flags;
Elf64_Half e_ehsize;
Elf64_Half e_phentsize;
Elf64_Half e_phnum;
Elf64_Half e_shentsize;
Elf64_Half e_shnum;
Elf64_Half e_shstrndx;
};

```
#### Elf64_Nhdr
```cpp
/* 486280 */
struct Elf64_Nhdr
{
Elf64_Word n_namesz;
Elf64_Word n_descsz;
Elf64_Word n_type;
};

```
#### Elf64_Phdr
```cpp
/* 486216 */
struct Elf64_Phdr
{
Elf64_Word p_type;
Elf64_Word p_flags;
Elf64_Off p_offset;
Elf64_Addr p_vaddr;
Elf64_Addr p_paddr;
Elf64_Xword p_filesz;
Elf64_Xword p_memsz;
Elf64_Xword p_align;
};

```
#### Elf64_Shdr
```cpp
/* 486299 */
struct Elf64_Shdr
{
Elf64_Word sh_name;
Elf64_Word sh_type;
Elf64_Xword sh_flags;
Elf64_Addr sh_addr;
Elf64_Off sh_offset;
Elf64_Xword sh_size;
Elf64_Word sh_link;
Elf64_Word sh_info;
Elf64_Xword sh_addralign;
Elf64_Xword sh_entsize;
};

```
#### Elf64_auxv_t
```cpp
/* 486232 */
struct Elf64_auxv_t
{
uint64_t a_type;
Elf64_auxv_t::$218B18A37F77BA833A070E25C7DC6FF2 a_un;
};

```
#### EnableGetWeakRef<EntityRefTraits>
```cpp
/* 9892 */
struct EnableGetWeakRef<EntityRefTraits>
{
__int8 gap0[1];
};

```
#### EnableGetWeakRef<EntityRegistryRefTraits>
```cpp
/* 9764 */
struct EnableGetWeakRef<EntityRegistryRefTraits>
{
__int8 gap0[1];
};

```
#### EnchantUtils
```cpp
/* 185725 */
struct EnchantUtils
{
__int8 gap0[1];
};

```
#### EnchantmentInstance
```cpp
/* 44085 */
struct EnchantmentInstance
{
Enchant::Type mEnchantType;
int mLevel;
};

```
#### EndCityPieces
```cpp
/* 461975 */
struct EndCityPieces
{
__int8 gap0[1];
};

```
#### EndCityPieces::SectionGenerator
```cpp
/* 461726 */
struct EndCityPieces::SectionGenerator
{
int (**_vptr$SectionGenerator)(void);
};

```
#### EndDragonFight
```cpp
/* 169784 */
struct EndDragonFight
{
BlockSource *mRegion;
std::vector<int> mGateways;
Unique<BlockPatternBuilder> mExitPortalPattern;
int mCrystalsAlive;
int mTicksSinceCrystalsScanned;
int mTicksSincePortalScanned;
int mTicksSinceLastPlayerScan;
bool mDragonKilled;
bool mPreviouslyKilled;
bool mDragonSpawned;
ActorUniqueID mDragonUUID;
BlockPos mPortalLocation;
const BlockPos mDragonSpawnPos;
RespawnAnimation mRespawnStage;
int mRespawnTime;
std::vector<ActorUniqueID> mRespawnCrystals;
EndDragonFightVersion mFightVersion;
EndDragonFight::GateWayGenerator mEntryGenerator;
EndDragonFight::GateWayGenerator mExitGenerator;
EndDragonFight::GatewayTask mBuildingOrVerifyingEndGatewayPair;
std::deque<std::tuple<EndDragonFight::GatewayTask,EndDragonFight::GateWayGenerator,EndDragonFight::GateWayGenerator>> mGatewayTasks;
};

```
#### EndDragonFight::_setEndGatewayBlockActorExitPosition::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 255257 */
struct EndDragonFight::_setEndGatewayBlockActorExitPosition::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### EndGatewayBlock::animateTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 459352 */
struct EndGatewayBlock::animateTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### EndPortalShape
```cpp
/* 459395 */
struct EndPortalShape
{
BlockSource *mSource;
int mRightDir;
int mLeftDir;
int mDepthDir;
BlockPos mBottomLeft;
BlockPos mOrigin;
int mBlockDirection;
std::vector<std::vector<const Block *>> mPortalPattern;
};

```
#### EntityCanonicalName::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 114949 */
struct EntityCanonicalName::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### EntityId
```cpp
/* 9730 */
struct EntityId
{
uint32_t mRawId;
};

```
#### EntityNetId
```cpp
/* 77830 */
struct EntityNetId
{
uint32_t mRawId;
};

```
#### EntityOptionalOwnerRef
```cpp
/* 187576 */
struct EntityOptionalOwnerRef
{
OwnerPtr<EntityId> mOwnedEntity;
WeakRef<EntityId> mWeakEntity;
};

```
#### EntityRefTraits
```cpp
/* 13169 */
struct EntityRefTraits
{
__int8 gap0[1];
};

```
#### EntityRegistryBase::ICanModifyComponentPoolDuringView
```cpp
/* 9763 */
struct EntityRegistryBase::ICanModifyComponentPoolDuringView
{
__int8 gap0[1];
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,ActorComponent,RailMovementComponent>
```cpp
/* 421160 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,ActorComponent,RailMovementComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ActorFlagComponent<BurnsInDaylightFlag> >
```cpp
/* 52163 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ActorFlagComponent<BurnsInDaylightFlag> >
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ActorFlagComponent<EnvironmentSensorFlag> >
```cpp
/* 55312 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ActorFlagComponent<EnvironmentSensorFlag> >
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,AgeableComponent>
```cpp
/* 49716 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,AgeableComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,AgentCommandComponent>
```cpp
/* 49877 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,AgentCommandComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,AngryComponent>
```cpp
/* 50037 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,AngryComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,AreaAttackComponent>
```cpp
/* 50162 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,AreaAttackComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BalloonComponent>
```cpp
/* 50283 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BalloonComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BehaviorComponent>
```cpp
/* 50659 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BehaviorComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BlockBreakSensorComponent>
```cpp
/* 50845 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BlockBreakSensorComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BodyControlComponent>
```cpp
/* 50994 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BodyControlComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BoostableComponent>
```cpp
/* 51166 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BoostableComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BossComponent>
```cpp
/* 51424 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BossComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BreakBlocksComponent>
```cpp
/* 51545 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BreakBlocksComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BreakDoorAnnotationComponent>
```cpp
/* 51676 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BreakDoorAnnotationComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BreathableComponent>
```cpp
/* 51808 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BreathableComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BreedableComponent>
```cpp
/* 51933 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BreedableComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BribeableComponent>
```cpp
/* 52048 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,BribeableComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,CommandBlockComponent>
```cpp
/* 52285 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,CommandBlockComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,DamageOverTimeComponent>
```cpp
/* 52411 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,DamageOverTimeComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,DanceComponent>
```cpp
/* 52561 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,DanceComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,DespawnComponent>
```cpp
/* 52676 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,DespawnComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,DwellerComponent>
```cpp
/* 53673 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,DwellerComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,EntitySensorComponent>
```cpp
/* 53787 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,EntitySensorComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ExplodeComponent>
```cpp
/* 55438 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ExplodeComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,FlockingComponent>
```cpp
/* 55563 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,FlockingComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,GoalSelectorComponent>
```cpp
/* 55764 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,GoalSelectorComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,GrowsCropComponent>
```cpp
/* 55920 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,GrowsCropComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,HopperComponent>
```cpp
/* 56037 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,HopperComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,HurtOnConditionComponent>
```cpp
/* 56245 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,HurtOnConditionComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,InsomniaComponent>
```cpp
/* 56363 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,InsomniaComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,InteractComponent>
```cpp
/* 56431 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,InteractComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,JumpControlComponent>
```cpp
/* 56579 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,JumpControlComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,LeashableComponent>
```cpp
/* 56781 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,LeashableComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,LegacyTradeableComponent>
```cpp
/* 59812 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,LegacyTradeableComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,LookAtComponent>
```cpp
/* 56937 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,LookAtComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,LookControlComponent>
```cpp
/* 57082 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,LookControlComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,MobEffectComponent>
```cpp
/* 57196 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,MobEffectComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,MountTamingComponent>
```cpp
/* 57342 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,MountTamingComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,MoveControlComponent>
```cpp
/* 57477 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,MoveControlComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,NavigationComponent>
```cpp
/* 57608 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,NavigationComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,OpenDoorAnnotationComponent>
```cpp
/* 57794 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,OpenDoorAnnotationComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,PeekComponent>
```cpp
/* 57946 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,PeekComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ProjectileComponent>
```cpp
/* 58238 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ProjectileComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,RaidBossComponent>
```cpp
/* 58399 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,RaidBossComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,RailActivatorComponent>
```cpp
/* 58513 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,RailActivatorComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ScaffoldingClimberComponent>
```cpp
/* 58628 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ScaffoldingClimberComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ScaleByAgeComponent,AgeableComponent>
```cpp
/* 58749 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,ScaleByAgeComponent,AgeableComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,SchedulerComponent>
```cpp
/* 58913 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,SchedulerComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,SensingComponent>
```cpp
/* 59056 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,SensingComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,SpawnActorComponent>
```cpp
/* 59340 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,SpawnActorComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TargetNearbyComponent>
```cpp
/* 59459 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TargetNearbyComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TeleportComponent>
```cpp
/* 59575 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TeleportComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TimerComponent>
```cpp
/* 59738 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TimerComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TrailComponent>
```cpp
/* 59926 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TrailComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TransformationComponent>
```cpp
/* 60050 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,FlagComponent<ActorTickedFlag>,ActorComponent,TransformationComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryBase::View<EntityContext,EntityRegistry,SurfaceBuilderComponent>
```cpp
/* 222971 */
struct EntityRegistryBase::View<EntityContext,EntityRegistry,SurfaceBuilderComponent>
{
EntityRegistry *mRegistry;
};

```
#### EntityRegistryRefTraits
```cpp
/* 13158 */
struct EntityRegistryRefTraits
{
__int8 gap0[1];
};

```
#### EntitySensorComponent
```cpp
/* 53697 */
struct EntitySensorComponent
{
float mSensorRange;
int mMinimumCount;
int mMaximumCount;
bool mRequireAll;
ActorFilterGroup mEventCondition;
std::string mEventName;
};

```
#### EntitySensorDefinition
```cpp
/* 340470 */
struct EntitySensorDefinition
{
float mSensorRange;
int mMinimumCount;
int mMaximumCount;
bool mRequireAll;
ActorFilterGroup mEventCondition;
std::string mEventName;
};

```
#### EntitySystems
```cpp
/* 13221 */
struct EntitySystems
{
std::vector<std::unique_ptr<ITickingSystem>> mTickingSystems;
Unique<PlayerInteractionSystem> mPlayerInteractionSystem;
};

```
#### EnumBitset<RenderCapability,14>
```cpp
/* 483999 */
struct EnumBitset<RenderCapability,14>
{
std::bitset<14> mBitset;
};

```
#### EnumBitset<ScriptLogType,3>
```cpp
/* 99213 */
struct EnumBitset<ScriptLogType,3>
{
std::bitset<3> mBitset;
};

```
#### EnvironmentRequirement
```cpp
/* 319446 */
struct EnvironmentRequirement
{
std::set<const Block *> mBlockTypes;
unsigned int mNumBlocksRequired;
unsigned int mSearchRadius;
};

```
#### EnvironmentSensorDefinition
```cpp
/* 55250 */
struct EnvironmentSensorDefinition
{
std::vector<DefinitionTrigger> mTriggers;
};

```
#### EnvironmentSensorFlag;
```cpp
/* 55299 */
struct EnvironmentSensorFlag;

```
#### EquippableComponent
```cpp
/* 100067 */
struct EquippableComponent
{
std::vector<SlotDescriptor> mSlots;
};

```
#### EquippableDefinition
```cpp
/* 100099 */
struct EquippableDefinition
{
std::vector<SlotDescriptor> mSlots;
};

```
#### ErrorPathStack
```cpp
/* 83338 */
struct ErrorPathStack
{
std::vector<std::string> *mErrorPath;
};

```
#### EvalParams
```cpp
/* 109091 */
struct EvalParams
{
MolangVariableMap mTempVariables;
};

```
#### EventCoordinator<ActorEventListener>
```cpp
/* 13234 */
struct EventCoordinator<ActorEventListener>
{
std::vector<ActorEventListener *> mListeners;
std::vector<std::function<EventResult (ActorEventListener *)>> mEventsToProcess;
std::thread::id mThreadId;
bool mThreadIdInitialized;
unsigned int mThreadCheckIndex;
};

```
#### EventCoordinator<BlockEventListener>
```cpp
/* 13235 */
struct EventCoordinator<BlockEventListener>
{
std::vector<BlockEventListener *> mListeners;
std::vector<std::function<EventResult (BlockEventListener *)>> mEventsToProcess;
std::thread::id mThreadId;
bool mThreadIdInitialized;
unsigned int mThreadCheckIndex;
};

```
#### EventCoordinator<ItemEventListener>
```cpp
/* 88276 */
struct EventCoordinator<ItemEventListener>
{
std::vector<ItemEventListener *> mListeners;
std::vector<std::function<EventResult (ItemEventListener *)>> mEventsToProcess;
std::thread::id mThreadId;
bool mThreadIdInitialized;
unsigned int mThreadCheckIndex;
};

```
#### EventCoordinator<LevelEventListener>
```cpp
/* 88242 */
struct EventCoordinator<LevelEventListener>
{
std::vector<LevelEventListener *> mListeners;
std::vector<std::function<EventResult (LevelEventListener *)>> mEventsToProcess;
std::thread::id mThreadId;
bool mThreadIdInitialized;
unsigned int mThreadCheckIndex;
};

```
#### EventCoordinator<NetworkPacketEventListener>
```cpp
/* 63025 */
struct EventCoordinator<NetworkPacketEventListener>
{
std::vector<NetworkPacketEventListener *> mListeners;
std::vector<std::function<EventResult (NetworkPacketEventListener *)>> mEventsToProcess;
std::thread::id mThreadId;
bool mThreadIdInitialized;
unsigned int mThreadCheckIndex;
};

```
#### EventCoordinator<PlayerEventListener>
```cpp
/* 13233 */
struct EventCoordinator<PlayerEventListener>
{
std::vector<PlayerEventListener *> mListeners;
std::vector<std::function<EventResult (PlayerEventListener *)>> mEventsToProcess;
std::thread::id mThreadId;
bool mThreadIdInitialized;
unsigned int mThreadCheckIndex;
};

```
#### EventCoordinator<ScriptEventListener>
```cpp
/* 99208 */
struct EventCoordinator<ScriptEventListener>
{
std::vector<ScriptEventListener *> mListeners;
std::vector<std::function<EventResult (ScriptEventListener *)>> mEventsToProcess;
std::thread::id mThreadId;
bool mThreadIdInitialized;
unsigned int mThreadCheckIndex;
};

```
#### EventCoordinator<ServerInstanceEventListener>
```cpp
/* 439 */
struct EventCoordinator<ServerInstanceEventListener>
{
std::vector<ServerInstanceEventListener *> mListeners;
std::vector<std::function<EventResult (ServerInstanceEventListener *)>> mEventsToProcess;
std::thread::id mThreadId;
bool mThreadIdInitialized;
unsigned int mThreadCheckIndex;
};

```
#### EventInfo
```cpp
/* 99958 */
struct EventInfo
{
std::string mEventName;
};

```
#### EventPacket::Data
```cpp
/* 13310 */
struct EventPacket::Data
{
EventPacket::Type mType;
Util::Byte mUsePlayerID;
EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB _anon_0;
std::string mEntityName;
std::string mCommandName;
std::string mResultKey;
std::string mResultString;
std::string mErrorList;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$103E0A04995712B8D39AE343EA50817C
```cpp
/* 13313 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$103E0A04995712B8D39AE343EA50817C
{
MinecraftEventing::AchievementIds mAchievementId;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$43709AFFC502E7A13BA1073C610D8549
```cpp
/* 13317 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$43709AFFC502E7A13BA1073C610D8549
{
bool mKilledByOwner;
int64_t mKillerEntityId;
int64_t mKilledMobId;
int32_t mDamageSource;
ActorType mKilledMobType;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$5B316CCC98B60A95F92E231D823C7BE3
```cpp
/* 13328 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$5B316CCC98B60A95F92E231D823C7BE3
{
__int16 mItemId;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$61A09D83502661C769654363F1382707
```cpp
/* 13330 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$61A09D83502661C769654363F1382707
{
float mPositionDelta;
float mObservedScore;
float mThresholdDistance;
float mThresholdScore;
int mThresholdDuration_ms;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$731817FF9A1D8A7F7DE35EC2646A852E
```cpp
/* 13316 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$731817FF9A1D8A7F7DE35EC2646A852E
{
int mFromDimension;
int mToDimension;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$922D880B3EFBF7F2063214579535BD95
```cpp
/* 13331 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$922D880B3EFBF7F2063214579535BD95
{
MovementEventType mEventType;
float mObservedScore;
float mAveragePosDelta;
float mTotalPosDelta;
float mMinPosDelta;
float mMaxPosDelta;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$92C02C0BC48AA2105788421214C7C1B7
```cpp
/* 13322 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$92C02C0BC48AA2105788421214C7C1B7
{
int32_t mResult;
int32_t mResultNumber;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$A01EA2DF6590CA7397A67CCFB21A7F86
```cpp
/* 13323 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$A01EA2DF6590CA7397A67CCFB21A7F86
{
int32_t mItemId;
int32_t mItemAux;
int32_t mLayerIndex;
int32_t mPatternId;
int32_t mPatternColor;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$A05CE60CF11B1B9B38674E8A09580618
```cpp
/* 13327 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$A05CE60CF11B1B9B38674E8A09580618
{
__int16 mItemId;
MinecraftEventing::POIBlockInteractionType mInteractionType;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$CFC5415F71714946B1482A4EA070D3F8
```cpp
/* 13315 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$CFC5415F71714946B1482A4EA070D3F8
{
int mBuiltInDimension;
};

```
#### EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$EA4713E4A3566411BE29AE280F22E9DF
```cpp
/* 13324 */
struct EventPacket::Data::$A9B56BB2A8A14AFA32257D71180A3DDB::$EA4713E4A3566411BE29AE280F22E9DF
{
int32_t mSuccessCount;
int32_t mErrorCount;
};

```
#### ExecCtxNext;
```cpp
/* 486933 */
struct ExecCtxNext;

```
#### ExecCtxPluck;
```cpp
/* 486934 */
struct ExecCtxPluck;

```
#### ExpandoModelElement
```cpp
/* 175620 */
struct ExpandoModelElement
{
ContainerItemStack item;
ContainerExpandStatus status;
std::string groupName;
};

```
#### ExperienceRewardComponent
```cpp
/* 107631 */
struct ExperienceRewardComponent
{
std::vector<ExpressionNode> mOnBred;
std::vector<ExpressionNode> mOnDeath;
};

```
#### ExperienceRewardDefinition
```cpp
/* 348090 */
struct ExperienceRewardDefinition
{
std::vector<ExpressionNode> mOnBred;
std::vector<ExpressionNode> mOnDeath;
};

```
#### Explosion
```cpp
/* 190223 */
struct Explosion
{
Vec3 mPos;
float mRadius;
BlockPosSet mToBlow;
bool mFire;
bool mBreaking;
bool mAllowUnderwater;
Actor *mSource;
BlockSource *mRegion;
float mMaxResistance;
Random mRandom;
};

```
#### ExpressionNode
```cpp
/* 47716 */
struct ExpressionNode
{
ExpressionOp mOp;
MolangScriptArg mValue;
std::vector<ExpressionNode> mChildren;
uint64_t mUsedTokenFlags;
std::string _mExpressionString;
};

```
#### ExtendedCertificate
```cpp
/* 8031 */
struct ExtendedCertificate
{
__int8 gap0[1];
};

```
#### ExtraLicenseData
```cpp
/* 45339 */
struct ExtraLicenseData
{
int64_t mValidationTime;
int64_t mRetryUntilTime;
int64_t mRetryAttempts;
};

```
#### EyeOfEnder::normalTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 170703 */
struct EyeOfEnder::normalTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
