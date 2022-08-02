#### GUIDGenerator
```cpp
/* 486272 */
struct GUIDGenerator
{
__int8 gap0[1];
};

```
#### GameCallbacks
```cpp
/* 76900 */
struct GameCallbacks
{
int (**_vptr$GameCallbacks)(void);
};

```
#### GameRule
```cpp
/* 945 */
struct GameRule
{
bool mShouldSave;
GameRule::Type mType;
GameRule::Value mValue;
std::string mName;
bool mAllowUseInCommand;
bool mIsDefaultSet;
bool mRequiresCheats;
GameRule::TagDataNotFoundCallback mTagNotFoundCallback;
GameRule::ValidateValueCallback mValidateValueCallback;
};

```
#### GameRule::ValidationError
```cpp
/* 954 */
struct GameRule::ValidationError
{
bool mSuccess;
std::string mErrorDescription;
std::vector<std::string> mErrorParameters;
};

```
#### GameRuleCommand::InitProxy
```cpp
/* 425707 */
struct GameRuleCommand::InitProxy
{
GameRules *mGameRules;
};

```
#### GameRules
```cpp
/* 5695 */
struct GameRules
{
GameRules::GameRuleMap mGameRules;
};

```
#### GameRules::_registerRules::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 290596 */
struct GameRules::_registerRules::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### GameRulesChangedPacketData
```cpp
/* 5698 */
struct GameRulesChangedPacketData
{
std::vector<GameRule> mRules;
};

```
#### GameVersion
```cpp
/* 5654 */
struct GameVersion
{
uint32_t mDigit[5];
std::string mString;
};

```
#### GeneDefinition
```cpp
/* 109107 */
struct GeneDefinition
{
std::string mName;
IntRange mAlleleRange;
std::vector<GeneticVariant> mGeneticVariants;
};

```
#### GeneticVariant
```cpp
/* 109108 */
struct GeneticVariant
{
IntRange mainAllele;
IntRange hiddenAllele;
IntRange eitherAllele;
IntRange bothAllele;
DefinitionTrigger onBorn;
};

```
#### GeneticsComponent
```cpp
/* 107795 */
struct GeneticsComponent
{
std::vector<GeneticsComponent::Gene> mGenes;
const GeneticsDefinition *mGeneticsDescription;
Random *mRandom;
};

```
#### GeneticsComponent::Gene
```cpp
/* 105778 */
struct GeneticsComponent::Gene
{
int mainAllele;
int hiddenAllele;
};

```
#### GeneticsDefinition
```cpp
/* 107770 */
struct GeneticsDefinition
{
float mMutationRate;
std::vector<GeneDefinition> mGeneDefinitions;
};

```
#### Ghast::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 170977 */
struct Ghast::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### GiveableComponent
```cpp
/* 54774 */
struct GiveableComponent
{
std::vector<unsigned long> mCoolDownTimeStamps;
};

```
#### GiveableDefinition
```cpp
/* 367783 */
struct GiveableDefinition
{
std::vector<GiveableTrigger> mTriggers;
};

```
#### GoalDefinition
```cpp
/* 47660 */
struct GoalDefinition
{
std::string mName;
int mPriority;
int mRequiredControlFlags;
int mScanInterval;
float mTargetSearchHeight;
int mPersistTargetTicks;
float mWithinDefault;
float mMaxDist;
float mMaxFlee;
float mWalkSpeedModifier;
float mSprintSpeedModifier;
float mProbabilityPerStrength;
float mSneakSpeedModifier;
ActorType mEntityType;
std::vector<MobDescriptor> mMobDescriptions;
bool mIgnoreVisibility;
float mStartDistance;
float mStopDistance;
int mRoarDuration;
int mRoarAttackTime;
int mRoarDamage;
int mRoarStrength;
int mRoarRange;
ActorFilterGroup mKnockbackFilter;
ActorFilterGroup mDamageFilter;
DefinitionTrigger mOnRoarEnd;
float mYd;
float mStalkSpeed;
float mMaxStalkDist;
float mLeapHeight;
float mLeapDistance;
float mPounceMaxDistance;
float mStrikeDistance;
float mStuckTime;
ActorFilterGroup mBlockFilter;
float mLookDistance;
int mAngleOfViewX;
int mAngleOfViewY;
float mProbability;
ActorFilterGroup mTargetFilter;
int mMinLookTime;
int mMaxLookTime;
int mMinLookAroundTime;
int mMaxLookAroundTime;
float mMinimumRadius;
bool mBroadcast;
float mBroadcastRange;
DefinitionTrigger mWithinRadiusEvent;
DefinitionTrigger mHurtByTargetEvent;
float mPercentChance;
ActorCategory mAttackTypes;
int mRandomStopInterval;
float mReachMultiplier;
float mMeleeFOV;
bool mAttackOnce;
int mRandomSoundInterval;
bool mRequireCompletePath;
DefinitionTrigger mOnAttack;
float mAttackDuration;
float mHitDelay;
LevelSoundEvent mDelayedAttackSound;
DefinitionTrigger mOnEat;
int mDelayBeforeEating;
int mWaitTime;
float mExploreDist;
std::vector<DefinitionTrigger> mOnHomeTriggers;
std::vector<DefinitionTrigger> mOnFailedTriggers;
DefinitionTrigger mOnLayEvent;
DefinitionTrigger mOnWorkArrivalEvent;
float mTargetDist;
float mSpeedModifier;
int mSearchRange;
int mSearchHeight;
int mSearchCount;
float mGoalRadius;
GoalDefinition::$A96817768A54EC800FE0CCD12036E025 mMoveToBlockGoalData;
float mWithin;
bool mIgnoreMobDamage;
bool mForceUse;
float mLookAhead;
float mCenteredGap;
float mMoveSpeed;
int mEntityCount;
int mXZDist;
int mYDist;
float mYOffset;
int mInterval;
float mCooldown;
__int8 mCanLandOnTrees : 1;
float mRangedFOV;
int mAttackIntervalMin;
int mAttackIntervalMax;
float mAttackRadius;
float mChargeChargedTrigger;
float mChargeShootTrigger;
int mBurstShots;
float mBurstInterval;
__int8 mMustSee : 1;
__int8 mMustReach : 1;
__int8 mCloseDoorAfter : 1;
__int8 mCanGetScared : 1;
__int8 mOnlyAtNight : 1;
__int8 mMustBeOnGround : 1;
__int8 mTrackTarget : 1;
__int8 mAlertSameType : 1;
__int8 mReselectTargets : 1;
bool mHurtOwner;
int mMustSeeForgetTicks;
std::vector<ItemDescriptor> mItemList;
bool mCanTemptVertically;
int mMaxToEat;
int mEatDelay;
int mFullDelay;
int mInitialEatDelay;
std::set<const Block *> mBlockList;
float mFloatHeightOffset;
bool mRandomReselect;
FloatRange mFloatDuration;
IntRange mHoverHeight;
float mDuration;
FloatRange mRadiusRange;
int mRadiusChangeChance;
FloatRange mAboveTargetRange;
FloatRange mHeightOffsetRange;
int mHeightChangeChance;
FloatRange mDelayRange;
std::vector<SummonSpellData> mSummonSpellData;
POIType mPOIType;
int mGoalCooldown;
int mActiveTime;
int mRandomSoundIntervalMin;
int mRandomSoundIntervalMax;
bool mCanWorkInRain;
int mWorkInRainTolerance;
float mFollowDistance;
float mBlockDistance;
std::vector<SendEventData> mSendEventData;
int mStartDelay;
int mMaxFailedAttempts;
bool mAvoidWater;
bool mPreferWater;
bool mTargetNeeded;
float mMountDistance;
std::vector<DrinkPotionData> mDrinkPotionData;
float mDrinkSpeedModifier;
float mDropItemChance;
DefinitionTrigger mOnDropAttemptEvent;
float mOfferingDistance;
std::string mLootTable;
FloatRange mTimeOfDayRange;
float mSnackingCooldown;
float mSnackingCooldownMin;
float mStopSnackingChance;
float mStopChance;
float mStartChance;
float mSittingTimeMin;
float mSittingCooldown;
std::string mSound;
std::string mPrepareSound;
float mPrepareTime;
std::string mAggroSound;
DefinitionTrigger mOnDefendEvent;
float mSleepYOffset;
float mSleepColliderHeight;
float mSleepColliderWidth;
float mCooldownMax;
float mCooldownMin;
float mDetectMobDistance;
float mDetectMobHeight;
ActorFilterGroup mCanNapFilters;
ActorFilterGroup mWakeMobExceptionFilters;
float mInterestTime;
float mRemoveItemTime;
float mCarriedItemSwitchTime;
float mInterestCooldown;
float mCooldownTimeoutTime;
ActorDefinitionIdentifier mDesiredMingleType;
float mMingleDistance;
int mMinLookCount;
int mMaxLookCount;
FloatRange mSoundInterval;
FloatRange mJumpInterval;
DefinitionTrigger mOnCelebrationEndEvent;
std::string mCelebrationSound;
};

```
#### GoalDefinition_0
```cpp
/* 117054 */
struct GoalDefinition_0
{
std::string mName;
int mPriority;
int mRequiredControlFlags;
int mScanInterval;
float mTargetSearchHeight;
int mPersistTargetTicks;
float mWithinDefault;
float mMaxDist;
float mMaxFlee;
float mWalkSpeedModifier;
float mSprintSpeedModifier;
float mProbabilityPerStrength;
float mSneakSpeedModifier;
ActorType mEntityType;
std::vector<MobDescriptor> mMobDescriptions;
bool mIgnoreVisibility;
float mStartDistance;
float mStopDistance;
int mRoarDuration;
int mRoarAttackTime;
int mRoarDamage;
int mRoarStrength;
int mRoarRange;
ActorFilterGroup mKnockbackFilter;
ActorFilterGroup mDamageFilter;
DefinitionTrigger mOnRoarEnd;
float mYd;
float mStalkSpeed;
float mMaxStalkDist;
float mLeapHeight;
float mLeapDistance;
float mPounceMaxDistance;
float mStrikeDistance;
float mStuckTime;
ActorFilterGroup mBlockFilter;
float mLookDistance;
int mAngleOfViewX;
int mAngleOfViewY;
float mProbability;
ActorFilterGroup mTargetFilter;
int mMinLookTime;
int mMaxLookTime;
int mMinLookAroundTime;
int mMaxLookAroundTime;
float mMinimumRadius;
bool mBroadcast;
float mBroadcastRange;
DefinitionTrigger mWithinRadiusEvent;
DefinitionTrigger mHurtByTargetEvent;
float mPercentChance;
ActorCategory mAttackTypes;
int mRandomStopInterval;
float mReachMultiplier;
float mMeleeFOV;
bool mAttackOnce;
int mRandomSoundInterval;
bool mRequireCompletePath;
DefinitionTrigger mOnAttack;
float mAttackDuration;
float mHitDelay;
LevelSoundEvent mDelayedAttackSound;
DefinitionTrigger mOnEat;
int mDelayBeforeEating;
int mWaitTime;
float mExploreDist;
std::vector<DefinitionTrigger> mOnHomeTriggers;
std::vector<DefinitionTrigger> mOnFailedTriggers;
DefinitionTrigger mOnLayEvent;
DefinitionTrigger mOnWorkArrivalEvent;
float mTargetDist;
float mSpeedModifier;
int mSearchRange;
int mSearchHeight;
int mSearchCount;
float mGoalRadius;
GoalDefinition::$957942B4FBBCA72D92900834D61C4C9E mMoveToBlockGoalData;
float mWithin;
bool mIgnoreMobDamage;
bool mForceUse;
float mLookAhead;
float mCenteredGap;
float mMoveSpeed;
int mEntityCount;
int mXZDist;
int mYDist;
float mYOffset;
int mInterval;
float mCooldown;
__int8 mCanLandOnTrees : 1;
float mRangedFOV;
int mAttackIntervalMin;
int mAttackIntervalMax;
float mAttackRadius;
float mChargeChargedTrigger;
float mChargeShootTrigger;
int mBurstShots;
float mBurstInterval;
__int8 mMustSee : 1;
__int8 mMustReach : 1;
__int8 mCloseDoorAfter : 1;
__int8 mCanGetScared : 1;
__int8 mOnlyAtNight : 1;
__int8 mMustBeOnGround : 1;
__int8 mTrackTarget : 1;
__int8 mAlertSameType : 1;
__int8 mReselectTargets : 1;
bool mHurtOwner;
int mMustSeeForgetTicks;
std::vector<ItemDescriptor> mItemList;
bool mCanTemptVertically;
int mMaxToEat;
int mEatDelay;
int mFullDelay;
int mInitialEatDelay;
std::set<const Block *> mBlockList;
float mFloatHeightOffset;
bool mRandomReselect;
FloatRange mFloatDuration;
IntRange mHoverHeight;
float mDuration;
FloatRange mRadiusRange;
int mRadiusChangeChance;
FloatRange mAboveTargetRange;
FloatRange mHeightOffsetRange;
int mHeightChangeChance;
FloatRange mDelayRange;
std::vector<SummonSpellData> mSummonSpellData;
POIType mPOIType;
int mGoalCooldown;
int mActiveTime;
int mRandomSoundIntervalMin;
int mRandomSoundIntervalMax;
bool mCanWorkInRain;
int mWorkInRainTolerance;
float mFollowDistance;
float mBlockDistance;
std::vector<SendEventData> mSendEventData;
int mStartDelay;
int mMaxFailedAttempts;
bool mAvoidWater;
bool mPreferWater;
bool mTargetNeeded;
float mMountDistance;
std::vector<DrinkPotionData> mDrinkPotionData;
float mDrinkSpeedModifier;
float mDropItemChance;
DefinitionTrigger mOnDropAttemptEvent;
float mOfferingDistance;
std::string mLootTable;
FloatRange mTimeOfDayRange;
float mSnackingCooldown;
float mSnackingCooldownMin;
float mStopSnackingChance;
float mStopChance;
float mStartChance;
float mSittingTimeMin;
float mSittingCooldown;
std::string mSound;
std::string mPrepareSound;
float mPrepareTime;
std::string mAggroSound;
DefinitionTrigger mOnDefendEvent;
float mSleepYOffset;
float mSleepColliderHeight;
float mSleepColliderWidth;
float mCooldownMax;
float mCooldownMin;
float mDetectMobDistance;
float mDetectMobHeight;
ActorFilterGroup mCanNapFilters;
ActorFilterGroup mWakeMobExceptionFilters;
float mInterestTime;
float mRemoveItemTime;
float mCarriedItemSwitchTime;
float mInterestCooldown;
float mCooldownTimeoutTime;
ActorDefinitionIdentifier mDesiredMingleType;
float mMingleDistance;
int mMinLookCount;
int mMaxLookCount;
FloatRange mSoundInterval;
FloatRange mJumpInterval;
DefinitionTrigger mOnCelebrationEndEvent;
std::string mCelebrationSound;
};

```
#### GoalDefinition_0::parse::$77030C46F7368D1C8A31176E7D1C3EB3
```cpp
/* 122519 */
struct GoalDefinition_0::parse::$77030C46F7368D1C8A31176E7D1C3EB3
{
GoalDefinition_0 *this;
};

```
#### GoalSelectorComponent
```cpp
/* 55649 */
struct GoalSelectorComponent
{
std::vector<PrioritizedGoal> mTargetGoals;
std::vector<PrioritizedGoal> mNormalGoals;
};

```
#### GridPos
```cpp
/* 42720 */
struct GridPos
{
int x;
int z;
};

```
#### GrowsCropComponent
```cpp
/* 55805 */
struct GrowsCropComponent
{
int mCharges;
BlockPos mTargetCrop;
BlockPos mLastGrownCrop;
};

```
#### GrowsCropDefinition
```cpp
/* 55861 */
struct GrowsCropDefinition
{
int mCharges;
float mChance;
};

```
#### GUIDGenerator
```cpp
/* 486272 */
struct GUIDGenerator
{
__int8 gap0[1];
};

```
#### GameCallbacks
```cpp
/* 76900 */
struct GameCallbacks
{
int (**_vptr$GameCallbacks)(void);
};

```
#### GameRule
```cpp
/* 945 */
struct GameRule
{
bool mShouldSave;
GameRule::Type mType;
GameRule::Value mValue;
std::string mName;
bool mAllowUseInCommand;
bool mIsDefaultSet;
bool mRequiresCheats;
GameRule::TagDataNotFoundCallback mTagNotFoundCallback;
GameRule::ValidateValueCallback mValidateValueCallback;
};

```
#### GameRule::ValidationError
```cpp
/* 954 */
struct GameRule::ValidationError
{
bool mSuccess;
std::string mErrorDescription;
std::vector<std::string> mErrorParameters;
};

```
#### GameRuleCommand::InitProxy
```cpp
/* 425707 */
struct GameRuleCommand::InitProxy
{
GameRules *mGameRules;
};

```
#### GameRules
```cpp
/* 5695 */
struct GameRules
{
GameRules::GameRuleMap mGameRules;
};

```
#### GameRules::_registerRules::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 290596 */
struct GameRules::_registerRules::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### GameRulesChangedPacketData
```cpp
/* 5698 */
struct GameRulesChangedPacketData
{
std::vector<GameRule> mRules;
};

```
#### GameVersion
```cpp
/* 5654 */
struct GameVersion
{
uint32_t mDigit[5];
std::string mString;
};

```
#### GeneDefinition
```cpp
/* 109107 */
struct GeneDefinition
{
std::string mName;
IntRange mAlleleRange;
std::vector<GeneticVariant> mGeneticVariants;
};

```
#### GeneticVariant
```cpp
/* 109108 */
struct GeneticVariant
{
IntRange mainAllele;
IntRange hiddenAllele;
IntRange eitherAllele;
IntRange bothAllele;
DefinitionTrigger onBorn;
};

```
#### GeneticsComponent
```cpp
/* 107795 */
struct GeneticsComponent
{
std::vector<GeneticsComponent::Gene> mGenes;
const GeneticsDefinition *mGeneticsDescription;
Random *mRandom;
};

```
#### GeneticsComponent::Gene
```cpp
/* 105778 */
struct GeneticsComponent::Gene
{
int mainAllele;
int hiddenAllele;
};

```
#### GeneticsDefinition
```cpp
/* 107770 */
struct GeneticsDefinition
{
float mMutationRate;
std::vector<GeneDefinition> mGeneDefinitions;
};

```
#### Ghast::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 170977 */
struct Ghast::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### GiveableComponent
```cpp
/* 54774 */
struct GiveableComponent
{
std::vector<unsigned long> mCoolDownTimeStamps;
};

```
#### GiveableDefinition
```cpp
/* 367783 */
struct GiveableDefinition
{
std::vector<GiveableTrigger> mTriggers;
};

```
#### GoalDefinition
```cpp
/* 47660 */
struct GoalDefinition
{
std::string mName;
int mPriority;
int mRequiredControlFlags;
int mScanInterval;
float mTargetSearchHeight;
int mPersistTargetTicks;
float mWithinDefault;
float mMaxDist;
float mMaxFlee;
float mWalkSpeedModifier;
float mSprintSpeedModifier;
float mProbabilityPerStrength;
float mSneakSpeedModifier;
ActorType mEntityType;
std::vector<MobDescriptor> mMobDescriptions;
bool mIgnoreVisibility;
float mStartDistance;
float mStopDistance;
int mRoarDuration;
int mRoarAttackTime;
int mRoarDamage;
int mRoarStrength;
int mRoarRange;
ActorFilterGroup mKnockbackFilter;
ActorFilterGroup mDamageFilter;
DefinitionTrigger mOnRoarEnd;
float mYd;
float mStalkSpeed;
float mMaxStalkDist;
float mLeapHeight;
float mLeapDistance;
float mPounceMaxDistance;
float mStrikeDistance;
float mStuckTime;
ActorFilterGroup mBlockFilter;
float mLookDistance;
int mAngleOfViewX;
int mAngleOfViewY;
float mProbability;
ActorFilterGroup mTargetFilter;
int mMinLookTime;
int mMaxLookTime;
int mMinLookAroundTime;
int mMaxLookAroundTime;
float mMinimumRadius;
bool mBroadcast;
float mBroadcastRange;
DefinitionTrigger mWithinRadiusEvent;
DefinitionTrigger mHurtByTargetEvent;
float mPercentChance;
ActorCategory mAttackTypes;
int mRandomStopInterval;
float mReachMultiplier;
float mMeleeFOV;
bool mAttackOnce;
int mRandomSoundInterval;
bool mRequireCompletePath;
DefinitionTrigger mOnAttack;
float mAttackDuration;
float mHitDelay;
LevelSoundEvent mDelayedAttackSound;
DefinitionTrigger mOnEat;
int mDelayBeforeEating;
int mWaitTime;
float mExploreDist;
std::vector<DefinitionTrigger> mOnHomeTriggers;
std::vector<DefinitionTrigger> mOnFailedTriggers;
DefinitionTrigger mOnLayEvent;
DefinitionTrigger mOnWorkArrivalEvent;
float mTargetDist;
float mSpeedModifier;
int mSearchRange;
int mSearchHeight;
int mSearchCount;
float mGoalRadius;
GoalDefinition::$A96817768A54EC800FE0CCD12036E025 mMoveToBlockGoalData;
float mWithin;
bool mIgnoreMobDamage;
bool mForceUse;
float mLookAhead;
float mCenteredGap;
float mMoveSpeed;
int mEntityCount;
int mXZDist;
int mYDist;
float mYOffset;
int mInterval;
float mCooldown;
__int8 mCanLandOnTrees : 1;
float mRangedFOV;
int mAttackIntervalMin;
int mAttackIntervalMax;
float mAttackRadius;
float mChargeChargedTrigger;
float mChargeShootTrigger;
int mBurstShots;
float mBurstInterval;
__int8 mMustSee : 1;
__int8 mMustReach : 1;
__int8 mCloseDoorAfter : 1;
__int8 mCanGetScared : 1;
__int8 mOnlyAtNight : 1;
__int8 mMustBeOnGround : 1;
__int8 mTrackTarget : 1;
__int8 mAlertSameType : 1;
__int8 mReselectTargets : 1;
bool mHurtOwner;
int mMustSeeForgetTicks;
std::vector<ItemDescriptor> mItemList;
bool mCanTemptVertically;
int mMaxToEat;
int mEatDelay;
int mFullDelay;
int mInitialEatDelay;
std::set<const Block *> mBlockList;
float mFloatHeightOffset;
bool mRandomReselect;
FloatRange mFloatDuration;
IntRange mHoverHeight;
float mDuration;
FloatRange mRadiusRange;
int mRadiusChangeChance;
FloatRange mAboveTargetRange;
FloatRange mHeightOffsetRange;
int mHeightChangeChance;
FloatRange mDelayRange;
std::vector<SummonSpellData> mSummonSpellData;
POIType mPOIType;
int mGoalCooldown;
int mActiveTime;
int mRandomSoundIntervalMin;
int mRandomSoundIntervalMax;
bool mCanWorkInRain;
int mWorkInRainTolerance;
float mFollowDistance;
float mBlockDistance;
std::vector<SendEventData> mSendEventData;
int mStartDelay;
int mMaxFailedAttempts;
bool mAvoidWater;
bool mPreferWater;
bool mTargetNeeded;
float mMountDistance;
std::vector<DrinkPotionData> mDrinkPotionData;
float mDrinkSpeedModifier;
float mDropItemChance;
DefinitionTrigger mOnDropAttemptEvent;
float mOfferingDistance;
std::string mLootTable;
FloatRange mTimeOfDayRange;
float mSnackingCooldown;
float mSnackingCooldownMin;
float mStopSnackingChance;
float mStopChance;
float mStartChance;
float mSittingTimeMin;
float mSittingCooldown;
std::string mSound;
std::string mPrepareSound;
float mPrepareTime;
std::string mAggroSound;
DefinitionTrigger mOnDefendEvent;
float mSleepYOffset;
float mSleepColliderHeight;
float mSleepColliderWidth;
float mCooldownMax;
float mCooldownMin;
float mDetectMobDistance;
float mDetectMobHeight;
ActorFilterGroup mCanNapFilters;
ActorFilterGroup mWakeMobExceptionFilters;
float mInterestTime;
float mRemoveItemTime;
float mCarriedItemSwitchTime;
float mInterestCooldown;
float mCooldownTimeoutTime;
ActorDefinitionIdentifier mDesiredMingleType;
float mMingleDistance;
int mMinLookCount;
int mMaxLookCount;
FloatRange mSoundInterval;
FloatRange mJumpInterval;
DefinitionTrigger mOnCelebrationEndEvent;
std::string mCelebrationSound;
};

```
#### GoalDefinition_0
```cpp
/* 117054 */
struct GoalDefinition_0
{
std::string mName;
int mPriority;
int mRequiredControlFlags;
int mScanInterval;
float mTargetSearchHeight;
int mPersistTargetTicks;
float mWithinDefault;
float mMaxDist;
float mMaxFlee;
float mWalkSpeedModifier;
float mSprintSpeedModifier;
float mProbabilityPerStrength;
float mSneakSpeedModifier;
ActorType mEntityType;
std::vector<MobDescriptor> mMobDescriptions;
bool mIgnoreVisibility;
float mStartDistance;
float mStopDistance;
int mRoarDuration;
int mRoarAttackTime;
int mRoarDamage;
int mRoarStrength;
int mRoarRange;
ActorFilterGroup mKnockbackFilter;
ActorFilterGroup mDamageFilter;
DefinitionTrigger mOnRoarEnd;
float mYd;
float mStalkSpeed;
float mMaxStalkDist;
float mLeapHeight;
float mLeapDistance;
float mPounceMaxDistance;
float mStrikeDistance;
float mStuckTime;
ActorFilterGroup mBlockFilter;
float mLookDistance;
int mAngleOfViewX;
int mAngleOfViewY;
float mProbability;
ActorFilterGroup mTargetFilter;
int mMinLookTime;
int mMaxLookTime;
int mMinLookAroundTime;
int mMaxLookAroundTime;
float mMinimumRadius;
bool mBroadcast;
float mBroadcastRange;
DefinitionTrigger mWithinRadiusEvent;
DefinitionTrigger mHurtByTargetEvent;
float mPercentChance;
ActorCategory mAttackTypes;
int mRandomStopInterval;
float mReachMultiplier;
float mMeleeFOV;
bool mAttackOnce;
int mRandomSoundInterval;
bool mRequireCompletePath;
DefinitionTrigger mOnAttack;
float mAttackDuration;
float mHitDelay;
LevelSoundEvent mDelayedAttackSound;
DefinitionTrigger mOnEat;
int mDelayBeforeEating;
int mWaitTime;
float mExploreDist;
std::vector<DefinitionTrigger> mOnHomeTriggers;
std::vector<DefinitionTrigger> mOnFailedTriggers;
DefinitionTrigger mOnLayEvent;
DefinitionTrigger mOnWorkArrivalEvent;
float mTargetDist;
float mSpeedModifier;
int mSearchRange;
int mSearchHeight;
int mSearchCount;
float mGoalRadius;
GoalDefinition::$957942B4FBBCA72D92900834D61C4C9E mMoveToBlockGoalData;
float mWithin;
bool mIgnoreMobDamage;
bool mForceUse;
float mLookAhead;
float mCenteredGap;
float mMoveSpeed;
int mEntityCount;
int mXZDist;
int mYDist;
float mYOffset;
int mInterval;
float mCooldown;
__int8 mCanLandOnTrees : 1;
float mRangedFOV;
int mAttackIntervalMin;
int mAttackIntervalMax;
float mAttackRadius;
float mChargeChargedTrigger;
float mChargeShootTrigger;
int mBurstShots;
float mBurstInterval;
__int8 mMustSee : 1;
__int8 mMustReach : 1;
__int8 mCloseDoorAfter : 1;
__int8 mCanGetScared : 1;
__int8 mOnlyAtNight : 1;
__int8 mMustBeOnGround : 1;
__int8 mTrackTarget : 1;
__int8 mAlertSameType : 1;
__int8 mReselectTargets : 1;
bool mHurtOwner;
int mMustSeeForgetTicks;
std::vector<ItemDescriptor> mItemList;
bool mCanTemptVertically;
int mMaxToEat;
int mEatDelay;
int mFullDelay;
int mInitialEatDelay;
std::set<const Block *> mBlockList;
float mFloatHeightOffset;
bool mRandomReselect;
FloatRange mFloatDuration;
IntRange mHoverHeight;
float mDuration;
FloatRange mRadiusRange;
int mRadiusChangeChance;
FloatRange mAboveTargetRange;
FloatRange mHeightOffsetRange;
int mHeightChangeChance;
FloatRange mDelayRange;
std::vector<SummonSpellData> mSummonSpellData;
POIType mPOIType;
int mGoalCooldown;
int mActiveTime;
int mRandomSoundIntervalMin;
int mRandomSoundIntervalMax;
bool mCanWorkInRain;
int mWorkInRainTolerance;
float mFollowDistance;
float mBlockDistance;
std::vector<SendEventData> mSendEventData;
int mStartDelay;
int mMaxFailedAttempts;
bool mAvoidWater;
bool mPreferWater;
bool mTargetNeeded;
float mMountDistance;
std::vector<DrinkPotionData> mDrinkPotionData;
float mDrinkSpeedModifier;
float mDropItemChance;
DefinitionTrigger mOnDropAttemptEvent;
float mOfferingDistance;
std::string mLootTable;
FloatRange mTimeOfDayRange;
float mSnackingCooldown;
float mSnackingCooldownMin;
float mStopSnackingChance;
float mStopChance;
float mStartChance;
float mSittingTimeMin;
float mSittingCooldown;
std::string mSound;
std::string mPrepareSound;
float mPrepareTime;
std::string mAggroSound;
DefinitionTrigger mOnDefendEvent;
float mSleepYOffset;
float mSleepColliderHeight;
float mSleepColliderWidth;
float mCooldownMax;
float mCooldownMin;
float mDetectMobDistance;
float mDetectMobHeight;
ActorFilterGroup mCanNapFilters;
ActorFilterGroup mWakeMobExceptionFilters;
float mInterestTime;
float mRemoveItemTime;
float mCarriedItemSwitchTime;
float mInterestCooldown;
float mCooldownTimeoutTime;
ActorDefinitionIdentifier mDesiredMingleType;
float mMingleDistance;
int mMinLookCount;
int mMaxLookCount;
FloatRange mSoundInterval;
FloatRange mJumpInterval;
DefinitionTrigger mOnCelebrationEndEvent;
std::string mCelebrationSound;
};

```
#### GoalDefinition_0::parse::$77030C46F7368D1C8A31176E7D1C3EB3
```cpp
/* 122519 */
struct GoalDefinition_0::parse::$77030C46F7368D1C8A31176E7D1C3EB3
{
GoalDefinition_0 *this;
};

```
#### GoalSelectorComponent
```cpp
/* 55649 */
struct GoalSelectorComponent
{
std::vector<PrioritizedGoal> mTargetGoals;
std::vector<PrioritizedGoal> mNormalGoals;
};

```
#### GridPos
```cpp
/* 42720 */
struct GridPos
{
int x;
int z;
};

```
#### GrowsCropComponent
```cpp
/* 55805 */
struct GrowsCropComponent
{
int mCharges;
BlockPos mTargetCrop;
BlockPos mLastGrownCrop;
};

```
#### GrowsCropDefinition
```cpp
/* 55861 */
struct GrowsCropDefinition
{
int mCharges;
float mChance;
};

```
