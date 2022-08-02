#### AABBContactPoint
```cpp
/* 109072 */
struct AABBContactPoint
{
int mNormalIndex;
float mSignedPenetration;
Vec3 mNormal;
};

```
#### AABBPred
```cpp
/* 88939 */
struct AABBPred
{
__int8 gap0[1];
};

```
#### AABBShapeComponent
```cpp
/* 50040 */
struct AABBShapeComponent
{
AABB mAABB;
Vec2 mBBDim;
};

```
#### Abilities
```cpp
/* 5694 */
struct Abilities
{
std::unique_ptr<PermissionsHandler> mPermissions;
std::array<Ability,18> mAbilities;
std::array<Ability,8> mCustomAbilityCache;
};

```
#### ActionQueue
```cpp
/* 89271 */
struct ActionQueue
{
std::deque<ActionEvent> mQueue;
};

```
#### ActivationArguments;
```cpp
/* 5510 */
struct ActivationArguments;

```
#### ActivationUri;
```cpp
/* 103888 */
struct ActivationUri;

```
#### Actor
```cpp
/* 1058 */
struct Actor
{
int (**_vptr$Actor)(void);
OwnerPtr<EntityId> mEntity;
Actor::InitializationMethod mInitMethod;
std::string mCustomInitEventName;
VariantParameterList mInitParams;
bool mForceInitMethodToSpawnOnReload;
bool mRequiresReload;
DimensionType mDimensionId;
bool mAdded;
ActorDefinitionGroup *mDefinitions;
Unique<ActorDefinitionDescriptor> mCurrentDescription;
ActorUniqueID mUniqueID;
Shared<RopeSystem> mLeashRopeSystem;
Vec2 mRot;
Vec2 mRotPrev;
float mSwimAmount;
float mSwimPrev;
ChunkPos mChunkPos;
Vec3 mRenderPos;
Vec2 mRenderRot;
int mAmbientSoundTime;
int mLastHurtByPlayerTime;
ActorCategory mCategories;
SynchedActorData mEntityData;
Unique<SpatialActorNetworkData> mNetworkData;
Vec3 mSentDelta;
float mScale;
float mScalePrev;
HashType64 mNameTagHash;
bool mOnGround;
bool mWasOnGround;
bool mHorizontalCollision;
bool mVerticalCollision;
bool mCollision;
const Block *mInsideBlock;
BlockPos mInsideBlockPos;
float mFallDistance;
bool mIgnoreLighting;
bool mFilterLighting;
Color mTintColor;
Color mTintColor2;
float mStepSoundVolume;
float mStepSoundPitch;
AABB *mLastHitBB;
std::vector<AABB> mSubBBs;
float mTerrainSurfaceOffset;
float mHeightOffset;
float mExplosionOffset;
float mShadowOffset;
float mMaxAutoStep;
float mPushthrough;
float mWalkDistPrev;
float mWalkDist;
float mMoveDist;
int mNextStep;
float mBlockMovementSlowdownMultiplier;
bool mImmobile;
bool mWasInWater;
bool mHasEnteredWater;
bool mHeadInWater;
bool mIsWet;
Vec2 mSlideOffset;
Vec3 mHeadOffset;
Vec3 mEyeOffset;
Vec3 mBreathingOffset;
Vec3 mMouthOffset;
Vec3 mDropOffset;
bool mFirstTick;
int mTickCount;
int mInvulnerableTime;
int mLastHealth;
bool mFallDamageImmune;
bool mHurtMarked;
bool mWasHurtLastFrame;
bool mInvulnerable;
bool mAlwaysFireImmune;
int mOnFire;
int mFlameTexFrameIndex;
float mFlameFrameIncrementTime;
bool mOnHotBlock;
int mClientSideFireTransitionStartTick;
bool mClientSideFireTransitionLatch;
int mPortalCooldown;
BlockPos mPortalBlockPos;
PortalAxis mPortalEntranceAxis;
int mInsidePortalTime;
std::vector<ActorUniqueID> mRiderIDs;
std::vector<ActorUniqueID> mRiderIDsToRemove;
ActorUniqueID mRidingID;
ActorUniqueID mRidingPrevID;
ActorUniqueID mPushedByID;
bool mInheritRotationWhenRiding;
bool mRidersChanged;
bool mBlocksBuilding;
bool mUsesOneWayCollision;
bool mForcedLoading;
bool mPrevPosRotSetThisTick;
bool mTeleportedThisTick;
bool mForceSendMotionPacket;
float mSoundVolume;
int mShakeTime;
float mWalkAnimSpeedMultiplier;
float mWalkAnimSpeedO;
float mWalkAnimSpeed;
float mWalkAnimPos;
ActorUniqueID mLegacyUniqueID;
bool mHighlightedThisFrame;
bool mInitialized;
BlockSource *mRegion;
Dimension *mDimension;
Level *mLevel;
HashedString mActorRendererId;
HashedString mActorRendererIdThatAnimationComponentWasInitializedWith;
bool mChanged;
bool mRemoved;
bool mGlobal;
bool mAutonomous;
ActorType mActorType;
ActorDefinitionIdentifier mActorIdentifier;
std::unique_ptr<BaseAttributeMap> mAttributes;
Unique<EconomyTradeableComponent> mEconomyTradeableComponent;
std::shared_ptr<AnimationComponent> mAnimationComponent;
AABBShapeComponent mAABBComponent;
StateVectorComponent mStateVectorComponent;
ActorUniqueID mTargetId;
bool mLootDropped;
float mRestrictRadius;
BlockPos mRestrictCenter;
ActorUniqueID mInLovePartner;
MobEffectInstanceList mMobEffects;
bool mEffectsDirty;
bool mPersistingTrade;
Unique<CompoundTag> mPersistingTradeOffers;
int mPersistingTradeRiches;
ActorRuntimeID mRuntimeID;
Color mHurtColor;
bool mEnforceRiderRotationLimit;
std::unique_ptr<ActorDefinitionDiffList> mDefinitionList;
bool mHasLimitedLife;
int mLimitedLifeTicks;
int mForceVisibleTimerTicks;
std::string mFilteredNameTag;
bool mIsStuckItem;
float mRidingExitDistance;
bool mIsSafeToSleepNear;
ActorTerrainInterlockData mTerrainInterlockData;
SimpleContainer mArmor;
float mArmorDropChance[4];
SimpleContainer mHand;
float mHandDropChance[2];
bool mIsKnockedBackOnDeath;
std::vector<AABB> mOnewayPhysicsBlocks;
bool mStuckInCollider;
float mLastPenetration;
bool mCollidableMobNear;
bool mCollidableMob;
bool mChainedDamageEffects;
int mDamageNearbyMobsTick;
bool mWasInBubbleColumn;
bool mWasInWallLastTick;
int mTicksInWall;
bool mIsExperimental;
Unique<ActionQueue> mActionQueue;
MolangVariableMap mMolangVariables;
CompoundTag mCachedComponentData;
ActorUniqueID mFishingHookID;
};

```
#### Actor::baseTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 109104 */
struct Actor::baseTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Actor::spawnDeathParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 109120 */
struct Actor::spawnDeathParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Actor::spawnTrailBubbles::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 109105 */
struct Actor::spawnTrailBubbles::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### ActorAnimationBase
```cpp
/* 125154 */
struct ActorAnimationBase
{
__int8 gap0[1];
};

```
#### ActorAnimationController
```cpp
/* 109075 */
struct ActorAnimationController
{
HashedString mName;
size_t mInitialStateIndex;
std::vector<std::shared_ptr<ActorAnimationControllerState>> mStates;
std::string mSourceFilePathWithExtension;
};

```
#### ActorAnimationControllerGroup
```cpp
/* 87817 */
struct ActorAnimationControllerGroup
{
std::unordered_map<HashedString,std::shared_ptr<ActorAnimationControllerInfo>> mAnimationControllers;
};

```
#### ActorAnimationControllerInfo
```cpp
/* 88672 */
struct ActorAnimationControllerInfo
{
HashedString mName;
std::unique_ptr<ActorAnimationController> mPtr;
};

```
#### ActorAnimationControllerPtr
```cpp
/* 104552 */
struct ActorAnimationControllerPtr
{
std::shared_ptr<ActorAnimationControllerInfo> mActorAnimationControllerInfoPtr;
};

```
#### ActorAnimationControllerState
```cpp
/* 125153 */
struct ActorAnimationControllerState
{
HashedString mName;
std::vector<StateAnimationVariable> mVariables;
std::vector<std::pair<HashedString,ExpressionNode>> mAnimations;
std::vector<ActorParticleEffect> mParticleEffects;
std::vector<ActorAnimationEvent> mEvents[2];
std::vector<ActorAnimationControllerStateTransition> mTransitions;
std::vector<ActorSoundEffect> mSoundEffects;
bool mBlendViaShortestPath;
std::vector<AnimationValueCurveKeyFrame> mBlendTransitionKeyFrames;
};

```
#### ActorAnimationControllerStateTransition
```cpp
/* 125204 */
struct ActorAnimationControllerStateTransition
{
std::string mTargetStateName;
size_t mTargetStateIndex;
ExpressionNode mTransitionExpression;
};

```
#### ActorAnimationInfo
```cpp
/* 104516 */
struct ActorAnimationInfo
{
HashedString mName;
std::unique_ptr<ActorSkeletalAnimation> mPtr;
};

```
#### ActorClassTree
```cpp
/* 109133 */
struct ActorClassTree
{
__int8 gap0[1];
};

```
#### ActorComponent
```cpp
/* 48121 */
struct ActorComponent
{
Actor *mActor;
};

```
#### ActorDefinition
```cpp
/* 89038 */
struct ActorDefinition
{
ActorDefinitionDescriptor mDescription;
IdentifierDescription mIdentifier;
RuntimeIdentifierDescription mRuntimeIdentifier;
IsSpawnableDescription mIsSpawnable;
IsSummonableDescription mIsSummonable;
IsExperimentalDescription mIsExperimental;
AnimationsDescription mAnimationsDescription;
AnimationScriptsDescription mAnimationScriptsDescription;
std::vector<GoalDefinition> mGoalDefinitions;
std::vector<ActorDefinitionAttribute> mAttributes;
std::unordered_map<std::string,DefinitionEvent> mEventHandlers;
AnimationResourceDefinitionMap mAnimationResourceDefinitionMap;
AttackDescription mAttack;
MobEffectChangeDescription mMobEffects;
AmbientSoundIntervalDescription mAmbientSoundInterval;
CanClimbDescription mCanClimb;
CanFlyDescription mCanFly;
CanPowerJumpDescription mCanPowerJump;
CollisionBoxDescription mCollisionBox;
Color2Description mColor2;
ColorDescription mColor;
DefaultLookAngleDescription mDefaultLookAngle;
DyeableDescription mDyeable;
EquipmentTableDescription mEquipmentTable;
FamilyTypeDescription mFamilyTypes;
FireImmuneDescription mFireImmune;
FloatsInLiquidDescription mFloatsInLiquid;
FlyingSpeedDescription mFlyingSpeed;
FootSizeDescription mFootSize;
FrictionModifierDescription mFrictionModifier;
GroundOffsetDescription mSurfaceOffset;
IsBabyDescription mIsBaby;
IsChargedDescription mIsCharged;
IsChestedDescription mIsChested;
IsHiddenWhenInvisibleDescription mIsHiddenWhenInvisible;
IsIgnitedDescription mIsIgnited;
IsIllagerCaptainDescription mIsIllagerCaptain;
IsSaddledDescription mIsSaddled;
IsShakingDescription mIsShaking;
IsShearedDescription mIsSheared;
IsStunnedDescription mIsStunned;
IsStackableDescription mIsStackable;
IsTamedDescription mIsTamed;
ItemControlDescription mItemControllable;
LootTableDescription mLootTable;
PushThroughDescription mPushthrough;
ScaleDescription mScale;
SoundVolumeDescription mSoundVolume;
WalkAnimationSpeedDescription mWalkAnimSpeedMultiplier;
WantsJockeyDescription mWantsJockey;
WASDControlledDescription mWASDControlled;
OnDeathDescription mOnDeath;
OnFriendlyAngerDescription mOnFriendlyAnger;
OnHurtByPlayerDescription mOnHurtByPlayer;
OnHurtDescription mOnHurt;
OnIgniteDescription mOnIgnite;
OnStartLandingDescription mOnStartLanding;
OnStartTakeoffDescription mOnStartTakeoff;
OnTargetAcquiredDescription mOnTargetAcquired;
OnTargetEscapeDescription mOnTargetEscape;
OnWakeWithOwnerDescription mOnWakeWithOwner;
AmphibiousMoveControlDescription mAmphibiousMoveControl;
AngryDescription mAngry;
BehaviorTreeDescription mBehavior;
BreakBlocksDescription mBreakBlocks;
BreakDoorAnnotationDescription mBreakDoorAnnotation;
BucketableDescription mBucketable;
CommandBlockDescription mCommandBlock;
ContainerDescription mContainer;
DespawnDescription mDespawn;
DwellerDescription mDweller;
GenericMoveControlDescription mGenericMoveControl;
GlideMoveControlDescription mGlideMoveControl;
HideDescription mHide;
IllagerBeastBlockedDescription mIllagerBeastBlocked;
ManagedWanderingTraderDescription mManagedWanderingTrader;
MarkVariantDescription mMarkVariant;
MoveControlBasicDescription mMoveControl;
MoveControlDolphinDescription mDolphinSwimControl;
MoveControlFlyDescription mFlyControl;
MoveControlSkipDescription mHopControl;
MoveControlHoverDescription mHoverControl;
MoveControlSwayDescription mSwimControl;
NameableDescription mNameable;
NavigationClimbDescription mWallClimberNavigation;
NavigationFloatDescription mFloatNavigation;
NavigationFlyDescription mFlyingNavigation;
NavigationHoverDescription mHoverNavigation;
NavigationGenericDescription mGenericNavigation;
NavigationSwimDescription mWaterboundNavigation;
NavigationWalkDescription mNavigation;
PersistentDescription mPersistent;
PreferredPathDescription mPreferredPath;
ProjectileDescription mProjectile;
PushableDescription mPushable;
RaidTriggerDescription mRaidTrigger;
RailActivatorDescription mRailActivator;
RideableDescription mRideable;
ShooterDescription mShooter;
SittableDescription mSittable;
SkinIDDescription mSkinID;
SlimeMoveControlDescription mSlimeMoveControl;
SpawnActorDescription mSpawnEntity;
StrengthDescription mStrength;
TagsDescription mTags;
TameableDescription mTameable;
TrailDescription mTrail;
TrustingDescription mTrusting;
TargetNearbyDescription mTargetNearby;
TeleportDescription mTeleport;
TickWorldDescription mTickWorld;
TimerDescription mTimer;
TradeResupplyDescription mTradeResupply;
TrustDescription mTrust;
EconomyTradeableDescription mEconomyTradeable;
TransformationDescription mTransformation;
VariantDescription mVariant;
WaterMovementDescription mWaterMovement;
DynamicJumpControlDescription mDynamicJumpControl;
JumpControlDescription mJumpControl;
OpenDoorAnnotationDescription mOpenDoorAnnotation;
NpcDescription mNpc;
TripodCameraDescription mTripodCamera;
};

```
#### ActorDefinition::parse::$AAE48C984D581248ECCF7B3C863DEC20
```cpp
/* 110223 */
struct ActorDefinition::parse::$AAE48C984D581248ECCF7B3C863DEC20
{
std::string *name;
Json::Value *root;
ActorDefinition *this;
ActorDefinitionDescriptor *desc;
};

```
#### ActorDefinition::parseAttributes::$6BAFC40004D8C3E8E3A064C81F470774
```cpp
/* 110222 */
struct ActorDefinition::parseAttributes::$6BAFC40004D8C3E8E3A064C81F470774
{
__gnu_cxx::__normal_iterator<std::string *,std::vector<std::string> > *iter;
ActorDefinition *this;
ActorDefinitionDescriptor *desc;
};

```
#### ActorDefinitionAttribute
```cpp
/* 47673 */
struct ActorDefinitionAttribute
{
std::string name;
float min;
float max;
FloatRange value;
};

```
#### ActorDefinitionDescriptor
```cpp
/* 47637 */
struct ActorDefinitionDescriptor
{
std::unordered_set<Util::HashString,Util::HashString::HashFunc,std::equal_to<Util::HashString>,std::allocator<Util::HashString> > mComponentNames;
IdentifierDescription mIdentifier;
RuntimeIdentifierDescription mRuntimeIdentifier;
IsSpawnableDescription mIsSpawnable;
IsSummonableDescription mIsSummonable;
IsExperimentalDescription mIsExperimental;
AnimationsDescription mAnimationsDescription;
AnimationScriptsDescription mAnimationScriptsDescription;
std::vector<GoalDefinition> mGoalDefinitions;
std::vector<ActorDefinitionAttribute> mAttributes;
std::unordered_map<std::string,DefinitionEvent> mEventHandlers;
DefinitionInstanceGroup mComponentDefinitionGroup;
Description *mAttack;
Description *mMobEffects;
Description *mAmbientSoundInterval;
Description *mCanClimb;
Description *mCanFly;
Description *mCanPowerJump;
Description *mCollisionBox;
Description *mColor2;
Description *mColor;
Description *mDefaultLookAngle;
Description *mDyeable;
Description *mEquipmentTable;
Description *mFamilyTypes;
Description *mFireImmune;
Description *mFloatsInLiquid;
Description *mFlyingSpeed;
Description *mFootSize;
Description *mFrictionModifier;
Description *mSurfaceOffset;
Description *mIsBaby;
Description *mIsCharged;
Description *mIsChested;
Description *mIsHiddenWhenInvisible;
Description *mIsIgnited;
Description *mIsIllagerCaptain;
Description *mIsSaddled;
Description *mIsShaking;
Description *mIsSheared;
Description *mIsStunned;
Description *mIsStackable;
Description *mIsTamed;
Description *mItemControllable;
Description *mLootTable;
Description *mPushthrough;
Description *mScale;
Description *mSoundVolume;
Description *mWalkAnimSpeedMultiplier;
Description *mWantsJockey;
Description *mWASDControlled;
Description *mOnDeath;
Description *mOnFriendlyAnger;
Description *mOnHurtByPlayer;
Description *mOnHurt;
Description *mOnIgnite;
Description *mOnStartLanding;
Description *mOnStartTakeoff;
Description *mOnTargetAcquired;
Description *mOnTargetEscape;
Description *mOnWakeWithOwner;
Description *mAmphibiousMoveControl;
Description *mAngry;
Description *mBehavior;
Description *mBreakBlocks;
Description *mBreakDoorAnnotation;
Description *mBucketable;
Description *mCommandBlock;
Description *mContainer;
Description *mDespawn;
Description *mDweller;
Description *mGenericMoveControl;
Description *mGlideMoveControl;
Description *mHide;
Description *mIllagerBeastBlocked;
Description *mManagedWanderingTrader;
Description *mMarkVariant;
Description *mMoveControl;
Description *mDolphinSwimControl;
Description *mFlyControl;
Description *mHopControl;
Description *mHoverControl;
Description *mSwimControl;
Description *mNameable;
Description *mWallClimberNavigation;
Description *mFloatNavigation;
Description *mFlyingNavigation;
Description *mHoverNavigation;
Description *mGenericNavigation;
Description *mWaterboundNavigation;
Description *mNavigation;
Description *mPersistent;
Description *mPreferredPath;
Description *mProjectile;
Description *mPushable;
Description *mRaidTrigger;
Description *mRailActivator;
Description *mRideable;
Description *mShooter;
Description *mSittable;
Description *mSkinID;
Description *mSlimeMoveControl;
Description *mSpawnEntity;
Description *mStrength;
Description *mTags;
Description *mTameable;
Description *mTrail;
Description *mTrusting;
Description *mTargetNearby;
Description *mTeleport;
Description *mTickWorld;
Description *mTimer;
Description *mTradeResupply;
Description *mTrust;
Description *mEconomyTradeable;
Description *mTransformation;
Description *mVariant;
Description *mWaterMovement;
Description *mDynamicJumpControl;
Description *mJumpControl;
Description *mOpenDoorAnnotation;
Description *mNpc;
Description *mTripodCamera;
};

```
#### ActorDefinitionDiffList
```cpp
/* 89022 */
struct ActorDefinitionDiffList
{
ActorDefinitionGroup *mDefinitions;
std::vector<std::pair<bool,ActorDefinitionPtr>> mDefinitionStack;
Unique<ActorDefinitionDescriptor> mChangedDescription;
bool mChanged;
DefinitionInstanceGroup mAddedDefinitionGroup;
DefinitionInstanceGroup mRemovedDefinitionGroup;
};

```
#### ActorDefinitionGroup
```cpp
/* 13228 */
struct ActorDefinitionGroup
{
int (**_vptr$ActorDefinitionGroup)(void);
std::unordered_set<ActorDefinitionPtr *> mRegisteredPtrs;
ActorDefinitionGroup::ActorDefinitionList mDefinitions;
std::unordered_map<std::string,ActorDefinitionGroup::EDLWrapper> mTemplateMap;
ResourcePackManager *mResourcePackManager;
Bedrock::Threading::Mutex mReferenceMutex;
IMinecraftEventing *mEventing;
bool mExperimentalEnabled;
ActorComponentFactory *mComponentFactory;
};

```
#### ActorDefinitionGroup::EDLWrapper
```cpp
/* 110632 */
struct ActorDefinitionGroup::EDLWrapper
{
ActorDefinitionGroup::ActorDefinitionList mList;
};

```
#### ActorDefinitionIdentifier
```cpp
/* 13229 */
struct ActorDefinitionIdentifier
{
std::string mNamespace;
std::string mIdentifier;
std::string mInitEvent;
std::string mFullName;
HashedString mCanonicalName;
};

```
#### ActorDefinitionPtr
```cpp
/* 89037 */
struct ActorDefinitionPtr
{
ActorDefinitionGroup *mGroup;
ActorDefinition *mPtr;
};

```
#### ActorEventListener
```cpp
/* 10786 */
struct ActorEventListener
{
int (**_vptr$ActorEventListener)(void);
};

```
#### ActorFactory
```cpp
/* 13223 */
struct ActorFactory
{
Level *mLevel;
std::shared_ptr<IEntityInitializer> mEntityInitializer;
ActorComponentFactory mComponentFactory;
};

```
#### ActorFilterGroup::LegacyMapping
```cpp
/* 114111 */
struct ActorFilterGroup::LegacyMapping
{
FilterGroup::CollectionType mType;
const FilterTest::Definition *mFilterDef;
FilterSubject mSubject;
FilterOperator mOperator;
ActorFilterGroup::Processing mProcess;
};

```
#### ActorLegacySaveConverter
```cpp
/* 114705 */
struct ActorLegacySaveConverter
{
__int8 gap0[1];
};

```
#### ActorMapping
```cpp
/* 114825 */
struct ActorMapping
{
std::string mNamespace;
std::string mPrimaryName;
std::string mAlternateName;
HashedString mCanonicalName;
};

```
#### ActorRenderData;
```cpp
/* 88685 */
struct ActorRenderData;

```
#### ActorRenderer;
```cpp
/* 122538 */
struct ActorRenderer;

```
#### ActorResourceDefinitionGroup;
```cpp
/* 183342 */
struct ActorResourceDefinitionGroup;

```
#### ActorRuntimeID
```cpp
/* 77428 */
struct ActorRuntimeID
{
uint64_t rawID;
};

```
#### ActorSkeletalAnimation
```cpp
/* 109074 */
struct ActorSkeletalAnimation
{
HashedString mName;
float mAnimationLength;
bool mShouldLoop;
bool mOverridePreviousAnimation;
ExpressionNode mBlendWeight;
ExpressionNode mAnimTimeUpdate;
std::vector<BoneAnimation> mBoneAnimations;
std::vector<ActorParticleEffectEvent> mParticleEffectEvents;
std::vector<ActorSoundEffectEvent> mSoundEffectEvents;
std::vector<ActorAnimationEvent> mEvents;
bool mIsExperimental;
std::string mSourceFilePathWithExtension;
};

```
#### ActorSkeletalAnimationPtr
```cpp
/* 104510 */
struct ActorSkeletalAnimationPtr
{
std::shared_ptr<ActorAnimationInfo> mActorAnimationInfoPtr;
};

```
#### ActorSoundEffect
```cpp
/* 124758 */
struct ActorSoundEffect
{
HashedString mSoundEffectName;
};

```
#### ActorSpawnRuleBase
```cpp
/* 451716 */
struct ActorSpawnRuleBase
{
int (**_vptr$ActorSpawnRuleBase)(void);
std::unordered_map<std::string,int> mSpawnDelayStartMap;
};

```
#### ActorTickedFlag;
```cpp
/* 49679 */
struct ActorTickedFlag;

```
#### ActorUniqueID
```cpp
/* 34910 */
struct ActorUniqueID
{
int64_t rawID;
};

```
#### AddMobPacket;
```cpp
/* 77408 */
struct AddMobPacket;

```
#### AddRiderComponent
```cpp
/* 107595 */
struct AddRiderComponent
{
ActorDefinitionIdentifier mRiderType;
};

```
#### AddRiderDefinition
```cpp
/* 107570 */
struct AddRiderDefinition
{
ActorDefinitionIdentifier mEntityType;
};

```
#### AdventureSettings
```cpp
/* 5808 */
struct AdventureSettings
{
bool noPvM;
bool noMvP;
bool immutableWorld;
bool showNameTags;
bool autoJump;
};

```
#### AgeableComponent
```cpp
/* 49334 */
struct AgeableComponent
{
int mAge;
};

```
#### AgeableDefinition
```cpp
/* 49590 */
struct AgeableDefinition
{
float mSecondsAsBaby;
std::vector<ActorDefinitionFeedItem> mFeedItems;
std::vector<const Item *> mDropItems;
DefinitionTrigger mOnGrowUp;
};

```
#### Agent::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 116991 */
struct Agent::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### AgentRenderData
```cpp
/* 116990 */
struct AgentRenderData
{
float mEaseIn;
int mOldTime;
};

```
#### AgentServerCommands
```cpp
/* 475678 */
struct AgentServerCommands
{
__int8 gap0[1];
};

```
#### AllWorkerConfigurations
```cpp
/* 81967 */
struct AllWorkerConfigurations
{
ThreadConfiguration MainThread;
ThreadConfiguration ServerThread;
WorkerConfiguration Async;
WorkerConfiguration Disk;
WorkerConfiguration Network;
WorkerConfiguration Rendering;
WorkerConfiguration LevelDB;
WorkerConfiguration LevelDBCompaction;
WorkerConfiguration ConnectedStorage;
WorkerConfiguration Watchdog;
};

```
#### Amplifier
```cpp
/* 171055 */
struct Amplifier
{
int (**_vptr$Amplifier)(void);
};

```
#### AngryComponent
```cpp
/* 49940 */
struct AngryComponent
{
int mDuration;
int mDurationDelta;
bool mHasTicked;
bool mBroadcastAnger;
int mBroadcastRange;
ActorFilterGroup mBroadcastFilter;
};

```
#### AnimationComponent
```cpp
/* 88640 */
struct AnimationComponent
{
size_t mLastReloadInitTimeStamp;
const ActorAnimationControllerStatePlayer *mCurrentAnimationControllerStatePlayer;
std::vector<std::unique_ptr<ActorAnimationPlayer>> mComponentAnimationPlayers;
std::vector<std::shared_ptr<ActorAnimationControllerInfo>> mOwnedAnimationControllers;
std::unique_ptr<std::unordered_map<HashedString,ModelPartLocator>> mModelPartLocators;
RenderParams mRenderParams;
ActorAnimationPlayer *mPlaySingleAnimation;
AnimationResourceDefinitionMap *mAnimationResourceDefinitionMap;
const ActorParticleEffectMap *mParticleEffectMap;
std::function<void (ActorAnimationPlayer &)> mAnimationComponentInitFunction;
std::vector<AnimationComponent::ChildAnimationComponentInfo> mChildAnimationComponents;
int mBoneOrientationGroupIndexToUseForPosing;
std::unordered_map<SkeletalHierarchyIndex,std::vector<BoneOrientation>> mBoneOrientations;
bool mAnimationComponentInitialized;
AnimationComponentGroup mAnimationComponentGroup;
AnimationComponentID mOwnerUUID;
int64_t mLastUpdateFrame;
};

```
#### AnimationComponent::ChildAnimationComponentInfo
```cpp
/* 88711 */
struct AnimationComponent::ChildAnimationComponentInfo
{
const void *mChildObjectKey;
MolangVariableMap mMolangVariableMap;
std::shared_ptr<AnimationComponent> mChildAnimationComponent;
};

```
#### AnimationComponent::setInitializedScriptsRun::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 170512 */
struct AnimationComponent::setInitializedScriptsRun::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### AnimationComponentID
```cpp
/* 88740 */
struct AnimationComponentID
{
AnimationComponentID::$9FA17E7D7DCEEBB7713B7193F23D45BD mData;
};

```
#### AnimationComponentID::$9FA17E7D7DCEEBB7713B7193F23D45BD::$65CCC15F238CE74967BBE3340E99BC94
```cpp
/* 88742 */
struct AnimationComponentID::$9FA17E7D7DCEEBB7713B7193F23D45BD::$65CCC15F238CE74967BBE3340E99BC94
{
unsigned __int64 mActorUniqueId : 54;
unsigned __int64 mAttachableDepth : 4;
unsigned __int64 mAttachableIndex : 6;
};

```
#### AnimationResourceDefinitionMap
```cpp
/* 88692 */
struct AnimationResourceDefinitionMap
{
ActorAnimationMap mActorAnimationMap;
ActorAnimationControllerMap mActorAnimationControllerMap;
ActorAnimateScriptArray mActorAnimateScriptArray;
};

```
#### AnimationValueCurveKeyFrame
```cpp
/* 125124 */
struct AnimationValueCurveKeyFrame
{
float mInputValue;
float mOutputValue;
};

```
#### AppConfigsFactory
```cpp
/* 81150 */
struct AppConfigsFactory
{
__int8 gap0[1];
};

```
#### AppLifecycleContext
```cpp
/* 6918 */
struct AppLifecycleContext
{
bool mAppliedHasGraphicsContext;
bool mAppliedIsCurrentlyResumed;
bool mHasGraphicsContext;
bool mIsCurrentlyResumed;
};

```
#### AppPlatformListener
```cpp
/* 86438 */
struct AppPlatformListener
{
int (**_vptr$AppPlatformListener)(void);
AppPlatform *platform;
};

```
#### AppendOnlyAtomicLookupTable<SubChunk,16>
```cpp
/* 35000 */
struct AppendOnlyAtomicLookupTable<SubChunk,16>
{
std::aligned_storage<56,8>::type mArray[16];
std::atomic_size_t mSize;
SpinLock mAppendLock;
};

```
#### ArbitraryBiomeComponent
```cpp
/* 220344 */
struct ArbitraryBiomeComponent
{
std::string mName;
Json::Value mPayload;
};

```
#### AreaAttackComponent
```cpp
/* 50065 */
struct AreaAttackComponent
{
float mDamageRange;
int mDamagePerTick;
ActorDamageCause mDamageCause;
ActorFilterGroup mEntityFilter;
};

```
#### AreaAttackDefinition
```cpp
/* 437653 */
struct AreaAttackDefinition
{
float mDamageRange;
int mDamagePerTick;
ActorDamageCause mDamageCause;
ActorFilterGroup mEntityFilter;
};

```
#### ArmorItem::ArmorMaterial
```cpp
/* 180650 */
struct ArmorItem::ArmorMaterial
{
int mDurabilityMultiplier;
int slotProtections[4];
int mEnchantmentValue;
};

```
#### ArmorStand::Pose
```cpp
/* 115418 */
struct ArmorStand::Pose
{
Vec3 mHeadPose;
Vec3 mBodyPose;
Vec3 mRightArmPose;
Vec3 mLeftArmPose;
Vec3 mRightLegPose;
Vec3 mLeftLegPose;
Vec3 mRightItemPose;
};

```
#### ArmorStand::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 115475 */
struct ArmorStand::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Arrow::normalTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 173211 */
struct Arrow::normalTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### AsyncTracker
```cpp
/* 62644 */
struct AsyncTracker
{
bool isCurrentWaitingOnCall;
bool mWasCallAborted;
std::chrono::_V2::steady_clock::time_point operationStartTime;
std::chrono::seconds timeLimit;
bool mHasRetryBeenRequested;
std::chrono::_V2::steady_clock::time_point mRetryTime;
};

```
#### AsynchronousIPResolver
```cpp
/* 73445 */
struct AsynchronousIPResolver
{
std::string mUrl;
std::shared_ptr<AsynchronousIPResolver::ResolvedIp> mResolvedIpPtr;
};

```
#### AtlasItemManager
```cpp
/* 104229 */
struct AtlasItemManager
{
std::unordered_map<std::string,TextureAtlasItem> mTextureAtlasItems;
};

```
#### Attribute
```cpp
/* 74148 */
struct Attribute
{
RedefinitionMode mRedefinitionMode;
bool mSyncable;
uint32_t mIDValue;
HashedString mName;
};

```
#### AttributeBuffInfo
```cpp
/* 174250 */
struct AttributeBuffInfo
{
AttributeBuffType type;
ActorUniqueID source;
};

```
#### AttributeInstance
```cpp
/* 74113 */
struct AttributeInstance
{
int (**_vptr$AttributeInstance)(void);
BaseAttributeMap *mAttributeMap;
const Attribute *mAttribute;
std::vector<AttributeModifier> mModifierList;
std::vector<TemporalAttributeBuff> mTemporalBuffs;
std::vector<AttributeInstanceHandle> mListeners;
std::shared_ptr<AttributeInstanceDelegate> mDelegate;
AttributeInstance::$DA28B55148B6D6964D71615272628344 _anon_0;
AttributeInstance::$DA28B55148B6D6964D71615272628344 _anon_1;
};

```
#### AttributeInstance::$A0656A567348DC83B4AF251F24308A0F::$A2CB89779BDC0E5E7A2DBCEC2E3DC5D0
```cpp
/* 74185 */
struct AttributeInstance::$A0656A567348DC83B4AF251F24308A0F::$A2CB89779BDC0E5E7A2DBCEC2E3DC5D0
{
float mCurrentMinValue;
float mCurrentMaxValue;
float mCurrentValue;
};

```
#### AttributeInstance::$A0656A567348DC83B4AF251F24308A0F::$C619D87F19D17294536CF8D7230526DE
```cpp
/* 74184 */
struct AttributeInstance::$A0656A567348DC83B4AF251F24308A0F::$C619D87F19D17294536CF8D7230526DE
{
float mCurrentValues[3];
};

```
#### AttributeInstance::$DA28B55148B6D6964D71615272628344::$CBA65015C8EB93BF42E3CAB5E288923D
```cpp
/* 74182 */
struct AttributeInstance::$DA28B55148B6D6964D71615272628344::$CBA65015C8EB93BF42E3CAB5E288923D
{
float mDefaultValues[3];
};

```
#### AttributeInstance::$DA28B55148B6D6964D71615272628344::$F2BAED747831077325874A72B2A106F3
```cpp
/* 74183 */
struct AttributeInstance::$DA28B55148B6D6964D71615272628344::$F2BAED747831077325874A72B2A106F3
{
float mDefaultMinValue;
float mDefaultMaxValue;
float mDefaultValue;
};

```
#### AttributeInstanceDelegate
```cpp
/* 74180 */
struct AttributeInstanceDelegate
{
int (**_vptr$AttributeInstanceDelegate)(void);
AttributeInstanceHandle mAttributeHandle;
};

```
#### AttributeInstanceHandle
```cpp
/* 74147 */
struct AttributeInstanceHandle
{
uint32_t mAttributeID;
BaseAttributeMap *mAttributeMap;
};

```
#### AutoCompleteInformation
```cpp
/* 5686 */
struct AutoCompleteInformation
{
std::vector<AutoCompleteOption> possibilities;
};

```
#### AutomaticID<Dimension,int>
```cpp
/* 5792 */
struct AutomaticID<Dimension,int>
{
int runtimeID;
};

```
#### Automation::AutomationSession
```cpp
/* 6381 */
struct Automation::AutomationSession
{
__int8 gap0[1];
};

```
#### Automation::CommandOrigin;
```cpp
/* 103887 */
struct Automation::CommandOrigin;

```
#### Automation::MessageHeader
```cpp
/* 430900 */
struct Automation::MessageHeader
{
std::string mRequestId;
Automation::MessagePurpose mMessagePurpose;
int mVersion;
};

```
#### Automation::Response
```cpp
/* 6407 */
struct Automation::Response
{
const Automation::Response::Type mType;
const std::string mMessage;
const std::string mId;
};

```
#### AutomationCmdOutput;
```cpp
/* 424402 */
struct AutomationCmdOutput;

```
#### AvailableCommandsPacket::ConstrainedValueData
```cpp
/* 78104 */
struct AvailableCommandsPacket::ConstrainedValueData
{
uint32_t enumValueSymbol;
uint32_t enumSymbol;
std::vector<unsigned char> constraints;
};

```
#### AvailableCommandsPacket::EnumData
```cpp
/* 77884 */
struct AvailableCommandsPacket::EnumData
{
std::string name;
std::vector<unsigned int> values;
};

```
#### AvailableCommandsPacket::OverloadData
```cpp
/* 77941 */
struct AvailableCommandsPacket::OverloadData
{
std::vector<AvailableCommandsPacket::ParamData> params;
};

```
#### AvailableCommandsPacket::SoftEnumData
```cpp
/* 78060 */
struct AvailableCommandsPacket::SoftEnumData
{
std::string name;
std::vector<std::string> values;
};

```
#### AABBContactPoint
```cpp
/* 109072 */
struct AABBContactPoint
{
int mNormalIndex;
float mSignedPenetration;
Vec3 mNormal;
};

```
#### AABBPred
```cpp
/* 88939 */
struct AABBPred
{
__int8 gap0[1];
};

```
#### AABBShapeComponent
```cpp
/* 50040 */
struct AABBShapeComponent
{
AABB mAABB;
Vec2 mBBDim;
};

```
#### Abilities
```cpp
/* 5694 */
struct Abilities
{
std::unique_ptr<PermissionsHandler> mPermissions;
std::array<Ability,18> mAbilities;
std::array<Ability,8> mCustomAbilityCache;
};

```
#### ActionQueue
```cpp
/* 89271 */
struct ActionQueue
{
std::deque<ActionEvent> mQueue;
};

```
#### ActivationArguments;
```cpp
/* 5510 */
struct ActivationArguments;

```
#### ActivationUri;
```cpp
/* 103888 */
struct ActivationUri;

```
#### Actor
```cpp
/* 1058 */
struct Actor
{
int (**_vptr$Actor)(void);
OwnerPtr<EntityId> mEntity;
Actor::InitializationMethod mInitMethod;
std::string mCustomInitEventName;
VariantParameterList mInitParams;
bool mForceInitMethodToSpawnOnReload;
bool mRequiresReload;
DimensionType mDimensionId;
bool mAdded;
ActorDefinitionGroup *mDefinitions;
Unique<ActorDefinitionDescriptor> mCurrentDescription;
ActorUniqueID mUniqueID;
Shared<RopeSystem> mLeashRopeSystem;
Vec2 mRot;
Vec2 mRotPrev;
float mSwimAmount;
float mSwimPrev;
ChunkPos mChunkPos;
Vec3 mRenderPos;
Vec2 mRenderRot;
int mAmbientSoundTime;
int mLastHurtByPlayerTime;
ActorCategory mCategories;
SynchedActorData mEntityData;
Unique<SpatialActorNetworkData> mNetworkData;
Vec3 mSentDelta;
float mScale;
float mScalePrev;
HashType64 mNameTagHash;
bool mOnGround;
bool mWasOnGround;
bool mHorizontalCollision;
bool mVerticalCollision;
bool mCollision;
const Block *mInsideBlock;
BlockPos mInsideBlockPos;
float mFallDistance;
bool mIgnoreLighting;
bool mFilterLighting;
Color mTintColor;
Color mTintColor2;
float mStepSoundVolume;
float mStepSoundPitch;
AABB *mLastHitBB;
std::vector<AABB> mSubBBs;
float mTerrainSurfaceOffset;
float mHeightOffset;
float mExplosionOffset;
float mShadowOffset;
float mMaxAutoStep;
float mPushthrough;
float mWalkDistPrev;
float mWalkDist;
float mMoveDist;
int mNextStep;
float mBlockMovementSlowdownMultiplier;
bool mImmobile;
bool mWasInWater;
bool mHasEnteredWater;
bool mHeadInWater;
bool mIsWet;
Vec2 mSlideOffset;
Vec3 mHeadOffset;
Vec3 mEyeOffset;
Vec3 mBreathingOffset;
Vec3 mMouthOffset;
Vec3 mDropOffset;
bool mFirstTick;
int mTickCount;
int mInvulnerableTime;
int mLastHealth;
bool mFallDamageImmune;
bool mHurtMarked;
bool mWasHurtLastFrame;
bool mInvulnerable;
bool mAlwaysFireImmune;
int mOnFire;
int mFlameTexFrameIndex;
float mFlameFrameIncrementTime;
bool mOnHotBlock;
int mClientSideFireTransitionStartTick;
bool mClientSideFireTransitionLatch;
int mPortalCooldown;
BlockPos mPortalBlockPos;
PortalAxis mPortalEntranceAxis;
int mInsidePortalTime;
std::vector<ActorUniqueID> mRiderIDs;
std::vector<ActorUniqueID> mRiderIDsToRemove;
ActorUniqueID mRidingID;
ActorUniqueID mRidingPrevID;
ActorUniqueID mPushedByID;
bool mInheritRotationWhenRiding;
bool mRidersChanged;
bool mBlocksBuilding;
bool mUsesOneWayCollision;
bool mForcedLoading;
bool mPrevPosRotSetThisTick;
bool mTeleportedThisTick;
bool mForceSendMotionPacket;
float mSoundVolume;
int mShakeTime;
float mWalkAnimSpeedMultiplier;
float mWalkAnimSpeedO;
float mWalkAnimSpeed;
float mWalkAnimPos;
ActorUniqueID mLegacyUniqueID;
bool mHighlightedThisFrame;
bool mInitialized;
BlockSource *mRegion;
Dimension *mDimension;
Level *mLevel;
HashedString mActorRendererId;
HashedString mActorRendererIdThatAnimationComponentWasInitializedWith;
bool mChanged;
bool mRemoved;
bool mGlobal;
bool mAutonomous;
ActorType mActorType;
ActorDefinitionIdentifier mActorIdentifier;
std::unique_ptr<BaseAttributeMap> mAttributes;
Unique<EconomyTradeableComponent> mEconomyTradeableComponent;
std::shared_ptr<AnimationComponent> mAnimationComponent;
AABBShapeComponent mAABBComponent;
StateVectorComponent mStateVectorComponent;
ActorUniqueID mTargetId;
bool mLootDropped;
float mRestrictRadius;
BlockPos mRestrictCenter;
ActorUniqueID mInLovePartner;
MobEffectInstanceList mMobEffects;
bool mEffectsDirty;
bool mPersistingTrade;
Unique<CompoundTag> mPersistingTradeOffers;
int mPersistingTradeRiches;
ActorRuntimeID mRuntimeID;
Color mHurtColor;
bool mEnforceRiderRotationLimit;
std::unique_ptr<ActorDefinitionDiffList> mDefinitionList;
bool mHasLimitedLife;
int mLimitedLifeTicks;
int mForceVisibleTimerTicks;
std::string mFilteredNameTag;
bool mIsStuckItem;
float mRidingExitDistance;
bool mIsSafeToSleepNear;
ActorTerrainInterlockData mTerrainInterlockData;
SimpleContainer mArmor;
float mArmorDropChance[4];
SimpleContainer mHand;
float mHandDropChance[2];
bool mIsKnockedBackOnDeath;
std::vector<AABB> mOnewayPhysicsBlocks;
bool mStuckInCollider;
float mLastPenetration;
bool mCollidableMobNear;
bool mCollidableMob;
bool mChainedDamageEffects;
int mDamageNearbyMobsTick;
bool mWasInBubbleColumn;
bool mWasInWallLastTick;
int mTicksInWall;
bool mIsExperimental;
Unique<ActionQueue> mActionQueue;
MolangVariableMap mMolangVariables;
CompoundTag mCachedComponentData;
ActorUniqueID mFishingHookID;
};

```
#### Actor::baseTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 109104 */
struct Actor::baseTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Actor::spawnDeathParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 109120 */
struct Actor::spawnDeathParticles::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Actor::spawnTrailBubbles::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 109105 */
struct Actor::spawnTrailBubbles::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### ActorAnimationBase
```cpp
/* 125154 */
struct ActorAnimationBase
{
__int8 gap0[1];
};

```
#### ActorAnimationController
```cpp
/* 109075 */
struct ActorAnimationController
{
HashedString mName;
size_t mInitialStateIndex;
std::vector<std::shared_ptr<ActorAnimationControllerState>> mStates;
std::string mSourceFilePathWithExtension;
};

```
#### ActorAnimationControllerGroup
```cpp
/* 87817 */
struct ActorAnimationControllerGroup
{
std::unordered_map<HashedString,std::shared_ptr<ActorAnimationControllerInfo>> mAnimationControllers;
};

```
#### ActorAnimationControllerInfo
```cpp
/* 88672 */
struct ActorAnimationControllerInfo
{
HashedString mName;
std::unique_ptr<ActorAnimationController> mPtr;
};

```
#### ActorAnimationControllerPtr
```cpp
/* 104552 */
struct ActorAnimationControllerPtr
{
std::shared_ptr<ActorAnimationControllerInfo> mActorAnimationControllerInfoPtr;
};

```
#### ActorAnimationControllerState
```cpp
/* 125153 */
struct ActorAnimationControllerState
{
HashedString mName;
std::vector<StateAnimationVariable> mVariables;
std::vector<std::pair<HashedString,ExpressionNode>> mAnimations;
std::vector<ActorParticleEffect> mParticleEffects;
std::vector<ActorAnimationEvent> mEvents[2];
std::vector<ActorAnimationControllerStateTransition> mTransitions;
std::vector<ActorSoundEffect> mSoundEffects;
bool mBlendViaShortestPath;
std::vector<AnimationValueCurveKeyFrame> mBlendTransitionKeyFrames;
};

```
#### ActorAnimationControllerStateTransition
```cpp
/* 125204 */
struct ActorAnimationControllerStateTransition
{
std::string mTargetStateName;
size_t mTargetStateIndex;
ExpressionNode mTransitionExpression;
};

```
#### ActorAnimationInfo
```cpp
/* 104516 */
struct ActorAnimationInfo
{
HashedString mName;
std::unique_ptr<ActorSkeletalAnimation> mPtr;
};

```
#### ActorClassTree
```cpp
/* 109133 */
struct ActorClassTree
{
__int8 gap0[1];
};

```
#### ActorComponent
```cpp
/* 48121 */
struct ActorComponent
{
Actor *mActor;
};

```
#### ActorDefinition
```cpp
/* 89038 */
struct ActorDefinition
{
ActorDefinitionDescriptor mDescription;
IdentifierDescription mIdentifier;
RuntimeIdentifierDescription mRuntimeIdentifier;
IsSpawnableDescription mIsSpawnable;
IsSummonableDescription mIsSummonable;
IsExperimentalDescription mIsExperimental;
AnimationsDescription mAnimationsDescription;
AnimationScriptsDescription mAnimationScriptsDescription;
std::vector<GoalDefinition> mGoalDefinitions;
std::vector<ActorDefinitionAttribute> mAttributes;
std::unordered_map<std::string,DefinitionEvent> mEventHandlers;
AnimationResourceDefinitionMap mAnimationResourceDefinitionMap;
AttackDescription mAttack;
MobEffectChangeDescription mMobEffects;
AmbientSoundIntervalDescription mAmbientSoundInterval;
CanClimbDescription mCanClimb;
CanFlyDescription mCanFly;
CanPowerJumpDescription mCanPowerJump;
CollisionBoxDescription mCollisionBox;
Color2Description mColor2;
ColorDescription mColor;
DefaultLookAngleDescription mDefaultLookAngle;
DyeableDescription mDyeable;
EquipmentTableDescription mEquipmentTable;
FamilyTypeDescription mFamilyTypes;
FireImmuneDescription mFireImmune;
FloatsInLiquidDescription mFloatsInLiquid;
FlyingSpeedDescription mFlyingSpeed;
FootSizeDescription mFootSize;
FrictionModifierDescription mFrictionModifier;
GroundOffsetDescription mSurfaceOffset;
IsBabyDescription mIsBaby;
IsChargedDescription mIsCharged;
IsChestedDescription mIsChested;
IsHiddenWhenInvisibleDescription mIsHiddenWhenInvisible;
IsIgnitedDescription mIsIgnited;
IsIllagerCaptainDescription mIsIllagerCaptain;
IsSaddledDescription mIsSaddled;
IsShakingDescription mIsShaking;
IsShearedDescription mIsSheared;
IsStunnedDescription mIsStunned;
IsStackableDescription mIsStackable;
IsTamedDescription mIsTamed;
ItemControlDescription mItemControllable;
LootTableDescription mLootTable;
PushThroughDescription mPushthrough;
ScaleDescription mScale;
SoundVolumeDescription mSoundVolume;
WalkAnimationSpeedDescription mWalkAnimSpeedMultiplier;
WantsJockeyDescription mWantsJockey;
WASDControlledDescription mWASDControlled;
OnDeathDescription mOnDeath;
OnFriendlyAngerDescription mOnFriendlyAnger;
OnHurtByPlayerDescription mOnHurtByPlayer;
OnHurtDescription mOnHurt;
OnIgniteDescription mOnIgnite;
OnStartLandingDescription mOnStartLanding;
OnStartTakeoffDescription mOnStartTakeoff;
OnTargetAcquiredDescription mOnTargetAcquired;
OnTargetEscapeDescription mOnTargetEscape;
OnWakeWithOwnerDescription mOnWakeWithOwner;
AmphibiousMoveControlDescription mAmphibiousMoveControl;
AngryDescription mAngry;
BehaviorTreeDescription mBehavior;
BreakBlocksDescription mBreakBlocks;
BreakDoorAnnotationDescription mBreakDoorAnnotation;
BucketableDescription mBucketable;
CommandBlockDescription mCommandBlock;
ContainerDescription mContainer;
DespawnDescription mDespawn;
DwellerDescription mDweller;
GenericMoveControlDescription mGenericMoveControl;
GlideMoveControlDescription mGlideMoveControl;
HideDescription mHide;
IllagerBeastBlockedDescription mIllagerBeastBlocked;
ManagedWanderingTraderDescription mManagedWanderingTrader;
MarkVariantDescription mMarkVariant;
MoveControlBasicDescription mMoveControl;
MoveControlDolphinDescription mDolphinSwimControl;
MoveControlFlyDescription mFlyControl;
MoveControlSkipDescription mHopControl;
MoveControlHoverDescription mHoverControl;
MoveControlSwayDescription mSwimControl;
NameableDescription mNameable;
NavigationClimbDescription mWallClimberNavigation;
NavigationFloatDescription mFloatNavigation;
NavigationFlyDescription mFlyingNavigation;
NavigationHoverDescription mHoverNavigation;
NavigationGenericDescription mGenericNavigation;
NavigationSwimDescription mWaterboundNavigation;
NavigationWalkDescription mNavigation;
PersistentDescription mPersistent;
PreferredPathDescription mPreferredPath;
ProjectileDescription mProjectile;
PushableDescription mPushable;
RaidTriggerDescription mRaidTrigger;
RailActivatorDescription mRailActivator;
RideableDescription mRideable;
ShooterDescription mShooter;
SittableDescription mSittable;
SkinIDDescription mSkinID;
SlimeMoveControlDescription mSlimeMoveControl;
SpawnActorDescription mSpawnEntity;
StrengthDescription mStrength;
TagsDescription mTags;
TameableDescription mTameable;
TrailDescription mTrail;
TrustingDescription mTrusting;
TargetNearbyDescription mTargetNearby;
TeleportDescription mTeleport;
TickWorldDescription mTickWorld;
TimerDescription mTimer;
TradeResupplyDescription mTradeResupply;
TrustDescription mTrust;
EconomyTradeableDescription mEconomyTradeable;
TransformationDescription mTransformation;
VariantDescription mVariant;
WaterMovementDescription mWaterMovement;
DynamicJumpControlDescription mDynamicJumpControl;
JumpControlDescription mJumpControl;
OpenDoorAnnotationDescription mOpenDoorAnnotation;
NpcDescription mNpc;
TripodCameraDescription mTripodCamera;
};

```
#### ActorDefinition::parse::$AAE48C984D581248ECCF7B3C863DEC20
```cpp
/* 110223 */
struct ActorDefinition::parse::$AAE48C984D581248ECCF7B3C863DEC20
{
std::string *name;
Json::Value *root;
ActorDefinition *this;
ActorDefinitionDescriptor *desc;
};

```
#### ActorDefinition::parseAttributes::$6BAFC40004D8C3E8E3A064C81F470774
```cpp
/* 110222 */
struct ActorDefinition::parseAttributes::$6BAFC40004D8C3E8E3A064C81F470774
{
__gnu_cxx::__normal_iterator<std::string *,std::vector<std::string> > *iter;
ActorDefinition *this;
ActorDefinitionDescriptor *desc;
};

```
#### ActorDefinitionAttribute
```cpp
/* 47673 */
struct ActorDefinitionAttribute
{
std::string name;
float min;
float max;
FloatRange value;
};

```
#### ActorDefinitionDescriptor
```cpp
/* 47637 */
struct ActorDefinitionDescriptor
{
std::unordered_set<Util::HashString,Util::HashString::HashFunc,std::equal_to<Util::HashString>,std::allocator<Util::HashString> > mComponentNames;
IdentifierDescription mIdentifier;
RuntimeIdentifierDescription mRuntimeIdentifier;
IsSpawnableDescription mIsSpawnable;
IsSummonableDescription mIsSummonable;
IsExperimentalDescription mIsExperimental;
AnimationsDescription mAnimationsDescription;
AnimationScriptsDescription mAnimationScriptsDescription;
std::vector<GoalDefinition> mGoalDefinitions;
std::vector<ActorDefinitionAttribute> mAttributes;
std::unordered_map<std::string,DefinitionEvent> mEventHandlers;
DefinitionInstanceGroup mComponentDefinitionGroup;
Description *mAttack;
Description *mMobEffects;
Description *mAmbientSoundInterval;
Description *mCanClimb;
Description *mCanFly;
Description *mCanPowerJump;
Description *mCollisionBox;
Description *mColor2;
Description *mColor;
Description *mDefaultLookAngle;
Description *mDyeable;
Description *mEquipmentTable;
Description *mFamilyTypes;
Description *mFireImmune;
Description *mFloatsInLiquid;
Description *mFlyingSpeed;
Description *mFootSize;
Description *mFrictionModifier;
Description *mSurfaceOffset;
Description *mIsBaby;
Description *mIsCharged;
Description *mIsChested;
Description *mIsHiddenWhenInvisible;
Description *mIsIgnited;
Description *mIsIllagerCaptain;
Description *mIsSaddled;
Description *mIsShaking;
Description *mIsSheared;
Description *mIsStunned;
Description *mIsStackable;
Description *mIsTamed;
Description *mItemControllable;
Description *mLootTable;
Description *mPushthrough;
Description *mScale;
Description *mSoundVolume;
Description *mWalkAnimSpeedMultiplier;
Description *mWantsJockey;
Description *mWASDControlled;
Description *mOnDeath;
Description *mOnFriendlyAnger;
Description *mOnHurtByPlayer;
Description *mOnHurt;
Description *mOnIgnite;
Description *mOnStartLanding;
Description *mOnStartTakeoff;
Description *mOnTargetAcquired;
Description *mOnTargetEscape;
Description *mOnWakeWithOwner;
Description *mAmphibiousMoveControl;
Description *mAngry;
Description *mBehavior;
Description *mBreakBlocks;
Description *mBreakDoorAnnotation;
Description *mBucketable;
Description *mCommandBlock;
Description *mContainer;
Description *mDespawn;
Description *mDweller;
Description *mGenericMoveControl;
Description *mGlideMoveControl;
Description *mHide;
Description *mIllagerBeastBlocked;
Description *mManagedWanderingTrader;
Description *mMarkVariant;
Description *mMoveControl;
Description *mDolphinSwimControl;
Description *mFlyControl;
Description *mHopControl;
Description *mHoverControl;
Description *mSwimControl;
Description *mNameable;
Description *mWallClimberNavigation;
Description *mFloatNavigation;
Description *mFlyingNavigation;
Description *mHoverNavigation;
Description *mGenericNavigation;
Description *mWaterboundNavigation;
Description *mNavigation;
Description *mPersistent;
Description *mPreferredPath;
Description *mProjectile;
Description *mPushable;
Description *mRaidTrigger;
Description *mRailActivator;
Description *mRideable;
Description *mShooter;
Description *mSittable;
Description *mSkinID;
Description *mSlimeMoveControl;
Description *mSpawnEntity;
Description *mStrength;
Description *mTags;
Description *mTameable;
Description *mTrail;
Description *mTrusting;
Description *mTargetNearby;
Description *mTeleport;
Description *mTickWorld;
Description *mTimer;
Description *mTradeResupply;
Description *mTrust;
Description *mEconomyTradeable;
Description *mTransformation;
Description *mVariant;
Description *mWaterMovement;
Description *mDynamicJumpControl;
Description *mJumpControl;
Description *mOpenDoorAnnotation;
Description *mNpc;
Description *mTripodCamera;
};

```
#### ActorDefinitionDiffList
```cpp
/* 89022 */
struct ActorDefinitionDiffList
{
ActorDefinitionGroup *mDefinitions;
std::vector<std::pair<bool,ActorDefinitionPtr>> mDefinitionStack;
Unique<ActorDefinitionDescriptor> mChangedDescription;
bool mChanged;
DefinitionInstanceGroup mAddedDefinitionGroup;
DefinitionInstanceGroup mRemovedDefinitionGroup;
};

```
#### ActorDefinitionGroup
```cpp
/* 13228 */
struct ActorDefinitionGroup
{
int (**_vptr$ActorDefinitionGroup)(void);
std::unordered_set<ActorDefinitionPtr *> mRegisteredPtrs;
ActorDefinitionGroup::ActorDefinitionList mDefinitions;
std::unordered_map<std::string,ActorDefinitionGroup::EDLWrapper> mTemplateMap;
ResourcePackManager *mResourcePackManager;
Bedrock::Threading::Mutex mReferenceMutex;
IMinecraftEventing *mEventing;
bool mExperimentalEnabled;
ActorComponentFactory *mComponentFactory;
};

```
#### ActorDefinitionGroup::EDLWrapper
```cpp
/* 110632 */
struct ActorDefinitionGroup::EDLWrapper
{
ActorDefinitionGroup::ActorDefinitionList mList;
};

```
#### ActorDefinitionIdentifier
```cpp
/* 13229 */
struct ActorDefinitionIdentifier
{
std::string mNamespace;
std::string mIdentifier;
std::string mInitEvent;
std::string mFullName;
HashedString mCanonicalName;
};

```
#### ActorDefinitionPtr
```cpp
/* 89037 */
struct ActorDefinitionPtr
{
ActorDefinitionGroup *mGroup;
ActorDefinition *mPtr;
};

```
#### ActorEventListener
```cpp
/* 10786 */
struct ActorEventListener
{
int (**_vptr$ActorEventListener)(void);
};

```
#### ActorFactory
```cpp
/* 13223 */
struct ActorFactory
{
Level *mLevel;
std::shared_ptr<IEntityInitializer> mEntityInitializer;
ActorComponentFactory mComponentFactory;
};

```
#### ActorFilterGroup::LegacyMapping
```cpp
/* 114111 */
struct ActorFilterGroup::LegacyMapping
{
FilterGroup::CollectionType mType;
const FilterTest::Definition *mFilterDef;
FilterSubject mSubject;
FilterOperator mOperator;
ActorFilterGroup::Processing mProcess;
};

```
#### ActorLegacySaveConverter
```cpp
/* 114705 */
struct ActorLegacySaveConverter
{
__int8 gap0[1];
};

```
#### ActorMapping
```cpp
/* 114825 */
struct ActorMapping
{
std::string mNamespace;
std::string mPrimaryName;
std::string mAlternateName;
HashedString mCanonicalName;
};

```
#### ActorRenderData;
```cpp
/* 88685 */
struct ActorRenderData;

```
#### ActorRenderer;
```cpp
/* 122538 */
struct ActorRenderer;

```
#### ActorResourceDefinitionGroup;
```cpp
/* 183342 */
struct ActorResourceDefinitionGroup;

```
#### ActorRuntimeID
```cpp
/* 77428 */
struct ActorRuntimeID
{
uint64_t rawID;
};

```
#### ActorSkeletalAnimation
```cpp
/* 109074 */
struct ActorSkeletalAnimation
{
HashedString mName;
float mAnimationLength;
bool mShouldLoop;
bool mOverridePreviousAnimation;
ExpressionNode mBlendWeight;
ExpressionNode mAnimTimeUpdate;
std::vector<BoneAnimation> mBoneAnimations;
std::vector<ActorParticleEffectEvent> mParticleEffectEvents;
std::vector<ActorSoundEffectEvent> mSoundEffectEvents;
std::vector<ActorAnimationEvent> mEvents;
bool mIsExperimental;
std::string mSourceFilePathWithExtension;
};

```
#### ActorSkeletalAnimationPtr
```cpp
/* 104510 */
struct ActorSkeletalAnimationPtr
{
std::shared_ptr<ActorAnimationInfo> mActorAnimationInfoPtr;
};

```
#### ActorSoundEffect
```cpp
/* 124758 */
struct ActorSoundEffect
{
HashedString mSoundEffectName;
};

```
#### ActorSpawnRuleBase
```cpp
/* 451716 */
struct ActorSpawnRuleBase
{
int (**_vptr$ActorSpawnRuleBase)(void);
std::unordered_map<std::string,int> mSpawnDelayStartMap;
};

```
#### ActorTickedFlag;
```cpp
/* 49679 */
struct ActorTickedFlag;

```
#### ActorUniqueID
```cpp
/* 34910 */
struct ActorUniqueID
{
int64_t rawID;
};

```
#### AddMobPacket;
```cpp
/* 77408 */
struct AddMobPacket;

```
#### AddRiderComponent
```cpp
/* 107595 */
struct AddRiderComponent
{
ActorDefinitionIdentifier mRiderType;
};

```
#### AddRiderDefinition
```cpp
/* 107570 */
struct AddRiderDefinition
{
ActorDefinitionIdentifier mEntityType;
};

```
#### AdventureSettings
```cpp
/* 5808 */
struct AdventureSettings
{
bool noPvM;
bool noMvP;
bool immutableWorld;
bool showNameTags;
bool autoJump;
};

```
#### AgeableComponent
```cpp
/* 49334 */
struct AgeableComponent
{
int mAge;
};

```
#### AgeableDefinition
```cpp
/* 49590 */
struct AgeableDefinition
{
float mSecondsAsBaby;
std::vector<ActorDefinitionFeedItem> mFeedItems;
std::vector<const Item *> mDropItems;
DefinitionTrigger mOnGrowUp;
};

```
#### Agent::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 116991 */
struct Agent::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### AgentRenderData
```cpp
/* 116990 */
struct AgentRenderData
{
float mEaseIn;
int mOldTime;
};

```
#### AgentServerCommands
```cpp
/* 475678 */
struct AgentServerCommands
{
__int8 gap0[1];
};

```
#### AllWorkerConfigurations
```cpp
/* 81967 */
struct AllWorkerConfigurations
{
ThreadConfiguration MainThread;
ThreadConfiguration ServerThread;
WorkerConfiguration Async;
WorkerConfiguration Disk;
WorkerConfiguration Network;
WorkerConfiguration Rendering;
WorkerConfiguration LevelDB;
WorkerConfiguration LevelDBCompaction;
WorkerConfiguration ConnectedStorage;
WorkerConfiguration Watchdog;
};

```
#### Amplifier
```cpp
/* 171055 */
struct Amplifier
{
int (**_vptr$Amplifier)(void);
};

```
#### AngryComponent
```cpp
/* 49940 */
struct AngryComponent
{
int mDuration;
int mDurationDelta;
bool mHasTicked;
bool mBroadcastAnger;
int mBroadcastRange;
ActorFilterGroup mBroadcastFilter;
};

```
#### AnimationComponent
```cpp
/* 88640 */
struct AnimationComponent
{
size_t mLastReloadInitTimeStamp;
const ActorAnimationControllerStatePlayer *mCurrentAnimationControllerStatePlayer;
std::vector<std::unique_ptr<ActorAnimationPlayer>> mComponentAnimationPlayers;
std::vector<std::shared_ptr<ActorAnimationControllerInfo>> mOwnedAnimationControllers;
std::unique_ptr<std::unordered_map<HashedString,ModelPartLocator>> mModelPartLocators;
RenderParams mRenderParams;
ActorAnimationPlayer *mPlaySingleAnimation;
AnimationResourceDefinitionMap *mAnimationResourceDefinitionMap;
const ActorParticleEffectMap *mParticleEffectMap;
std::function<void (ActorAnimationPlayer &)> mAnimationComponentInitFunction;
std::vector<AnimationComponent::ChildAnimationComponentInfo> mChildAnimationComponents;
int mBoneOrientationGroupIndexToUseForPosing;
std::unordered_map<SkeletalHierarchyIndex,std::vector<BoneOrientation>> mBoneOrientations;
bool mAnimationComponentInitialized;
AnimationComponentGroup mAnimationComponentGroup;
AnimationComponentID mOwnerUUID;
int64_t mLastUpdateFrame;
};

```
#### AnimationComponent::ChildAnimationComponentInfo
```cpp
/* 88711 */
struct AnimationComponent::ChildAnimationComponentInfo
{
const void *mChildObjectKey;
MolangVariableMap mMolangVariableMap;
std::shared_ptr<AnimationComponent> mChildAnimationComponent;
};

```
#### AnimationComponent::setInitializedScriptsRun::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 170512 */
struct AnimationComponent::setInitializedScriptsRun::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### AnimationComponentID
```cpp
/* 88740 */
struct AnimationComponentID
{
AnimationComponentID::$9FA17E7D7DCEEBB7713B7193F23D45BD mData;
};

```
#### AnimationComponentID::$9FA17E7D7DCEEBB7713B7193F23D45BD::$65CCC15F238CE74967BBE3340E99BC94
```cpp
/* 88742 */
struct AnimationComponentID::$9FA17E7D7DCEEBB7713B7193F23D45BD::$65CCC15F238CE74967BBE3340E99BC94
{
unsigned __int64 mActorUniqueId : 54;
unsigned __int64 mAttachableDepth : 4;
unsigned __int64 mAttachableIndex : 6;
};

```
#### AnimationResourceDefinitionMap
```cpp
/* 88692 */
struct AnimationResourceDefinitionMap
{
ActorAnimationMap mActorAnimationMap;
ActorAnimationControllerMap mActorAnimationControllerMap;
ActorAnimateScriptArray mActorAnimateScriptArray;
};

```
#### AnimationValueCurveKeyFrame
```cpp
/* 125124 */
struct AnimationValueCurveKeyFrame
{
float mInputValue;
float mOutputValue;
};

```
#### AppConfigsFactory
```cpp
/* 81150 */
struct AppConfigsFactory
{
__int8 gap0[1];
};

```
#### AppLifecycleContext
```cpp
/* 6918 */
struct AppLifecycleContext
{
bool mAppliedHasGraphicsContext;
bool mAppliedIsCurrentlyResumed;
bool mHasGraphicsContext;
bool mIsCurrentlyResumed;
};

```
#### AppPlatformListener
```cpp
/* 86438 */
struct AppPlatformListener
{
int (**_vptr$AppPlatformListener)(void);
AppPlatform *platform;
};

```
#### AppendOnlyAtomicLookupTable<SubChunk,16>
```cpp
/* 35000 */
struct AppendOnlyAtomicLookupTable<SubChunk,16>
{
std::aligned_storage<56,8>::type mArray[16];
std::atomic_size_t mSize;
SpinLock mAppendLock;
};

```
#### ArbitraryBiomeComponent
```cpp
/* 220344 */
struct ArbitraryBiomeComponent
{
std::string mName;
Json::Value mPayload;
};

```
#### AreaAttackComponent
```cpp
/* 50065 */
struct AreaAttackComponent
{
float mDamageRange;
int mDamagePerTick;
ActorDamageCause mDamageCause;
ActorFilterGroup mEntityFilter;
};

```
#### AreaAttackDefinition
```cpp
/* 437653 */
struct AreaAttackDefinition
{
float mDamageRange;
int mDamagePerTick;
ActorDamageCause mDamageCause;
ActorFilterGroup mEntityFilter;
};

```
#### ArmorItem::ArmorMaterial
```cpp
/* 180650 */
struct ArmorItem::ArmorMaterial
{
int mDurabilityMultiplier;
int slotProtections[4];
int mEnchantmentValue;
};

```
#### ArmorStand::Pose
```cpp
/* 115418 */
struct ArmorStand::Pose
{
Vec3 mHeadPose;
Vec3 mBodyPose;
Vec3 mRightArmPose;
Vec3 mLeftArmPose;
Vec3 mRightLegPose;
Vec3 mLeftLegPose;
Vec3 mRightItemPose;
};

```
#### ArmorStand::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 115475 */
struct ArmorStand::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Arrow::normalTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 173211 */
struct Arrow::normalTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### AsyncTracker
```cpp
/* 62644 */
struct AsyncTracker
{
bool isCurrentWaitingOnCall;
bool mWasCallAborted;
std::chrono::_V2::steady_clock::time_point operationStartTime;
std::chrono::seconds timeLimit;
bool mHasRetryBeenRequested;
std::chrono::_V2::steady_clock::time_point mRetryTime;
};

```
#### AsynchronousIPResolver
```cpp
/* 73445 */
struct AsynchronousIPResolver
{
std::string mUrl;
std::shared_ptr<AsynchronousIPResolver::ResolvedIp> mResolvedIpPtr;
};

```
#### AtlasItemManager
```cpp
/* 104229 */
struct AtlasItemManager
{
std::unordered_map<std::string,TextureAtlasItem> mTextureAtlasItems;
};

```
#### Attribute
```cpp
/* 74148 */
struct Attribute
{
RedefinitionMode mRedefinitionMode;
bool mSyncable;
uint32_t mIDValue;
HashedString mName;
};

```
#### AttributeBuffInfo
```cpp
/* 174250 */
struct AttributeBuffInfo
{
AttributeBuffType type;
ActorUniqueID source;
};

```
#### AttributeInstance
```cpp
/* 74113 */
struct AttributeInstance
{
int (**_vptr$AttributeInstance)(void);
BaseAttributeMap *mAttributeMap;
const Attribute *mAttribute;
std::vector<AttributeModifier> mModifierList;
std::vector<TemporalAttributeBuff> mTemporalBuffs;
std::vector<AttributeInstanceHandle> mListeners;
std::shared_ptr<AttributeInstanceDelegate> mDelegate;
AttributeInstance::$DA28B55148B6D6964D71615272628344 _anon_0;
AttributeInstance::$DA28B55148B6D6964D71615272628344 _anon_1;
};

```
#### AttributeInstance::$A0656A567348DC83B4AF251F24308A0F::$A2CB89779BDC0E5E7A2DBCEC2E3DC5D0
```cpp
/* 74185 */
struct AttributeInstance::$A0656A567348DC83B4AF251F24308A0F::$A2CB89779BDC0E5E7A2DBCEC2E3DC5D0
{
float mCurrentMinValue;
float mCurrentMaxValue;
float mCurrentValue;
};

```
#### AttributeInstance::$A0656A567348DC83B4AF251F24308A0F::$C619D87F19D17294536CF8D7230526DE
```cpp
/* 74184 */
struct AttributeInstance::$A0656A567348DC83B4AF251F24308A0F::$C619D87F19D17294536CF8D7230526DE
{
float mCurrentValues[3];
};

```
#### AttributeInstance::$DA28B55148B6D6964D71615272628344::$CBA65015C8EB93BF42E3CAB5E288923D
```cpp
/* 74182 */
struct AttributeInstance::$DA28B55148B6D6964D71615272628344::$CBA65015C8EB93BF42E3CAB5E288923D
{
float mDefaultValues[3];
};

```
#### AttributeInstance::$DA28B55148B6D6964D71615272628344::$F2BAED747831077325874A72B2A106F3
```cpp
/* 74183 */
struct AttributeInstance::$DA28B55148B6D6964D71615272628344::$F2BAED747831077325874A72B2A106F3
{
float mDefaultMinValue;
float mDefaultMaxValue;
float mDefaultValue;
};

```
#### AttributeInstanceDelegate
```cpp
/* 74180 */
struct AttributeInstanceDelegate
{
int (**_vptr$AttributeInstanceDelegate)(void);
AttributeInstanceHandle mAttributeHandle;
};

```
#### AttributeInstanceHandle
```cpp
/* 74147 */
struct AttributeInstanceHandle
{
uint32_t mAttributeID;
BaseAttributeMap *mAttributeMap;
};

```
#### AutoCompleteInformation
```cpp
/* 5686 */
struct AutoCompleteInformation
{
std::vector<AutoCompleteOption> possibilities;
};

```
#### AutomaticID<Dimension,int>
```cpp
/* 5792 */
struct AutomaticID<Dimension,int>
{
int runtimeID;
};

```
#### Automation::AutomationSession
```cpp
/* 6381 */
struct Automation::AutomationSession
{
__int8 gap0[1];
};

```
#### Automation::CommandOrigin;
```cpp
/* 103887 */
struct Automation::CommandOrigin;

```
#### Automation::MessageHeader
```cpp
/* 430900 */
struct Automation::MessageHeader
{
std::string mRequestId;
Automation::MessagePurpose mMessagePurpose;
int mVersion;
};

```
#### Automation::Response
```cpp
/* 6407 */
struct Automation::Response
{
const Automation::Response::Type mType;
const std::string mMessage;
const std::string mId;
};

```
#### AutomationCmdOutput;
```cpp
/* 424402 */
struct AutomationCmdOutput;

```
#### AvailableCommandsPacket::ConstrainedValueData
```cpp
/* 78104 */
struct AvailableCommandsPacket::ConstrainedValueData
{
uint32_t enumValueSymbol;
uint32_t enumSymbol;
std::vector<unsigned char> constraints;
};

```
#### AvailableCommandsPacket::EnumData
```cpp
/* 77884 */
struct AvailableCommandsPacket::EnumData
{
std::string name;
std::vector<unsigned int> values;
};

```
#### AvailableCommandsPacket::OverloadData
```cpp
/* 77941 */
struct AvailableCommandsPacket::OverloadData
{
std::vector<AvailableCommandsPacket::ParamData> params;
};

```
#### AvailableCommandsPacket::SoftEnumData
```cpp
/* 78060 */
struct AvailableCommandsPacket::SoftEnumData
{
std::string name;
std::vector<std::string> values;
};

```
