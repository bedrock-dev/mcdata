#### NameAction
```cpp
/* 89189 */
struct NameAction
{
std::vector<std::string> mNameFilters;
DefinitionTrigger mOnNamed;
};

```
#### NameableComponent
```cpp
/* 54594 */
struct NameableComponent
{
bool mAllowNameTagRenaming;
bool mAlwaysShow;
};

```
#### NavigationComponent
```cpp
/* 56707 */
struct NavigationComponent
{
bool mAvoidDamageBlocks;
bool mAvoidPortals;
bool mAvoidSun;
bool mAvoidWater;
bool mCanBreach;
bool mCanFloat;
bool mCanJump;
bool mCanOpenDoors;
bool mCanPassDoors;
bool mCanSink;
bool mIsAmphibious;
bool mIsFollowingRivers;
bool mHasEndPathRadius;
bool mHasDestination;
int mTick;
int mTickTimeout;
int mLastStuckCheck;
float mEndPathRadiusSqr;
float mSpeed;
float mTerminationThreshold;
Vec3 mLastStuckCheckPosition;
Vec3 mTargetOffset;
Unique<PathNavigation> mNavigation;
Unique<Path> mPath;
};

```
#### NbtIo
```cpp
/* 61751 */
struct NbtIo
{
__int8 gap0[1];
};

```
#### NetEventCallback
```cpp
/* 63003 */
struct NetEventCallback
{
int (**_vptr$NetEventCallback)(void);
};

```
#### NetherBiomeSurface;
```cpp
/* 198713 */
struct NetherBiomeSurface;

```
#### NetherGenerator::ThreadData
```cpp
/* 36222 */
struct NetherGenerator::ThreadData
{
Random random;
std::array<long,32768> blockBuffer;
};

```
#### NetworkChangeObserver;
```cpp
/* 6912 */
struct NetworkChangeObserver;

```
#### NetworkChunkPublisher
```cpp
/* 88549 */
struct NetworkChunkPublisher
{
int (**_vptr$NetworkChunkPublisher)(void);
Level *mLevel;
NetworkHandler *mNetworkHandler;
NetworkIdentifier mOwner;
ClientBlobCache::Server::ActiveTransfersManager *mClientCache;
SubClientId mSubClientId;
BlockPos mLastChunkUpdatePosition;
uint32_t mLastChunkUpdateRadius;
uint32_t mHandleForChunkBuildOrderUpdates;
int mChunksSentSinceStart;
std::unique_ptr<ChunkViewSource> mSource;
GridArea<std::shared_ptr<LevelChunk> >::AddCallback mAddCallback;
std::string mCacheSerializeBuffer;
std::unordered_map<ChunkPos,std::weak_ptr<LevelChunk>> mQueuedChunks;
};

```
#### NetworkComponent
```cpp
/* 79612 */
struct NetworkComponent
{
EntityNetId mEntityNetId;
};

```
#### NetworkDebugManager
```cpp
/* 64309 */
struct NetworkDebugManager
{
std::array<NetworkDebugManager::Tracker,4> mTrackers;
TrackerType mRenderGraphMode;
std::set<NetworkStatistics *> mStatistics;
};

```
#### NetworkHandler::Connection
```cpp
/* 8335 */
struct NetworkHandler::Connection
{
NetworkIdentifier mId;
NetworkHandler::Connection::Type mType;
std::weak_ptr<NetworkPacketRecorder> mNetworkPacketRecorder;
std::weak_ptr<EncryptedNetworkPeer> mEncryptedPeer;
std::weak_ptr<BatchedNetworkPeer> mBatchedPeer;
std::shared_ptr<NetworkPeer> mPeer;
std::chrono::time_point<std::chrono::_V2::steady_clock,std::chrono::duration<long,std::ratio<1,1000000000> > > mLastPacketTime;
std::chrono::time_point<std::chrono::_V2::steady_clock,std::chrono::duration<long,std::ratio<1,1000000000> > > mClosedTime;
bool mShouldCloseConnection;
bool mDisconnected;
std::bitset<2> mPausedChannels;
std::queue<std::string> mResumedPackets;
std::array<std::vector<std::string>,2> mPausedPackets;
};

```
#### NetworkHandler::IncomingPacketQueue
```cpp
/* 63002 */
struct NetworkHandler::IncomingPacketQueue
{
NetEventCallback *mCallbacksObj;
Bedrock::Threading::Mutex mMutex;
};

```
#### NetworkPacketEventListener
```cpp
/* 63038 */
struct NetworkPacketEventListener
{
int (**_vptr$NetworkPacketEventListener)(void);
};

```
#### NetworkPacketRecorder;
```cpp
/* 8222 */
struct NetworkPacketRecorder;

```
#### NetworkPeer
```cpp
/* 8247 */
struct NetworkPeer
{
int (**_vptr$NetworkPeer)(void);
std::shared_ptr<NetworkPeer> mPeer;
};

```
#### NetworkPeer::NetworkStatus
```cpp
/* 8630 */
struct NetworkPeer::NetworkStatus
{
NetworkPeer::NetworkLoad mLoad;
int mCurrentPing;
int mAveragePing;
int mApproximateMaxBps;
float mCurrentPacketLoss;
float mAveragePacketLoss;
uint64_t mTotalBytesReceived;
uint64_t mTotalBytesSent;
};

```
#### NetworkSettingOptions
```cpp
/* 72561 */
struct NetworkSettingOptions
{
uint16_t mCompressionThreshold;
};

```
#### NetworkStatistics::OverviewStats
```cpp
/* 63800 */
struct NetworkStatistics::OverviewStats
{
unsigned int sentBytesUnpacked;
unsigned int sentBytesPacked;
unsigned int receivedBytesUnpacked;
unsigned int receivedBytesPacked;
};

```
#### NetworkStatistics::PacketStats
```cpp
/* 63835 */
struct NetworkStatistics::PacketStats
{
unsigned int id;
unsigned int sentNum;
unsigned int sentBytes;
unsigned int receivedNum;
unsigned int receivedBytes;
};

```
#### NewType<int>
```cpp
/* 13185 */
struct NewType<int>
{
NewType<int>::Raw value;
};

```
#### NewType<long>
```cpp
/* 45313 */
struct NewType<long>
{
NewType<long>::Raw value;
};

```
#### NewType<unsigned short>
```cpp
/* 13216 */
struct NewType<unsigned short>
{
NewType<unsigned short>::Raw value;
};

```
#### NibblePair
```cpp
/* 35026 */
struct NibblePair
{
unsigned __int8 first : 4;
unsigned __int8 second : 4;
};

```
#### NoiseBasedColorPalette;
```cpp
/* 198718 */
struct NoiseBasedColorPalette;

```
#### NoiseBasedTemperatureAttributes
```cpp
/* 191330 */
struct NoiseBasedTemperatureAttributes
{
TemperatureCategory mTemperatureCategory;
};

```
#### NoteBlock::triggerEvent::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 459573 */
struct NoteBlock::triggerEvent::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### NpcAction
```cpp
/* 45374 */
struct NpcAction
{
int (**_vptr$NpcAction)(void);
const NpcActionType mType;
NpcActionMode mMode;
std::string mButtonName;
std::string mEvaluatedButtonName;
std::string mText;
std::optional<std::string > mEvaluatedText;
};

```
#### NpcComponent
```cpp
/* 44884 */
struct NpcComponent
{
int mCurrentSkin;
NpcGUIOffset mPortraitOffsets;
NpcGUIOffset mPickerOffsets;
std::vector<SkinData> mNPCSkins;
Json::Value mNPCData;
NpcActions mActions;
std::optional<std::string > mInteractText;
NpcComponent::TextFilter mInteractTextFilter;
};

```
#### NpcGUIOffset
```cpp
/* 44885 */
struct NpcGUIOffset
{
Vec3 mTranslation;
Vec3 mRotation;
Vec3 mScale;
};

```
#### NullSoundPlayer
```cpp
/* 86996 */
struct NullSoundPlayer
{
__int8 baseclass_0[8];
};

```
#### NameAction
```cpp
/* 89189 */
struct NameAction
{
std::vector<std::string> mNameFilters;
DefinitionTrigger mOnNamed;
};

```
#### NameableComponent
```cpp
/* 54594 */
struct NameableComponent
{
bool mAllowNameTagRenaming;
bool mAlwaysShow;
};

```
#### NavigationComponent
```cpp
/* 56707 */
struct NavigationComponent
{
bool mAvoidDamageBlocks;
bool mAvoidPortals;
bool mAvoidSun;
bool mAvoidWater;
bool mCanBreach;
bool mCanFloat;
bool mCanJump;
bool mCanOpenDoors;
bool mCanPassDoors;
bool mCanSink;
bool mIsAmphibious;
bool mIsFollowingRivers;
bool mHasEndPathRadius;
bool mHasDestination;
int mTick;
int mTickTimeout;
int mLastStuckCheck;
float mEndPathRadiusSqr;
float mSpeed;
float mTerminationThreshold;
Vec3 mLastStuckCheckPosition;
Vec3 mTargetOffset;
Unique<PathNavigation> mNavigation;
Unique<Path> mPath;
};

```
#### NbtIo
```cpp
/* 61751 */
struct NbtIo
{
__int8 gap0[1];
};

```
#### NetEventCallback
```cpp
/* 63003 */
struct NetEventCallback
{
int (**_vptr$NetEventCallback)(void);
};

```
#### NetherBiomeSurface;
```cpp
/* 198713 */
struct NetherBiomeSurface;

```
#### NetherGenerator::ThreadData
```cpp
/* 36222 */
struct NetherGenerator::ThreadData
{
Random random;
std::array<long,32768> blockBuffer;
};

```
#### NetworkChangeObserver;
```cpp
/* 6912 */
struct NetworkChangeObserver;

```
#### NetworkChunkPublisher
```cpp
/* 88549 */
struct NetworkChunkPublisher
{
int (**_vptr$NetworkChunkPublisher)(void);
Level *mLevel;
NetworkHandler *mNetworkHandler;
NetworkIdentifier mOwner;
ClientBlobCache::Server::ActiveTransfersManager *mClientCache;
SubClientId mSubClientId;
BlockPos mLastChunkUpdatePosition;
uint32_t mLastChunkUpdateRadius;
uint32_t mHandleForChunkBuildOrderUpdates;
int mChunksSentSinceStart;
std::unique_ptr<ChunkViewSource> mSource;
GridArea<std::shared_ptr<LevelChunk> >::AddCallback mAddCallback;
std::string mCacheSerializeBuffer;
std::unordered_map<ChunkPos,std::weak_ptr<LevelChunk>> mQueuedChunks;
};

```
#### NetworkComponent
```cpp
/* 79612 */
struct NetworkComponent
{
EntityNetId mEntityNetId;
};

```
#### NetworkDebugManager
```cpp
/* 64309 */
struct NetworkDebugManager
{
std::array<NetworkDebugManager::Tracker,4> mTrackers;
TrackerType mRenderGraphMode;
std::set<NetworkStatistics *> mStatistics;
};

```
#### NetworkHandler::Connection
```cpp
/* 8335 */
struct NetworkHandler::Connection
{
NetworkIdentifier mId;
NetworkHandler::Connection::Type mType;
std::weak_ptr<NetworkPacketRecorder> mNetworkPacketRecorder;
std::weak_ptr<EncryptedNetworkPeer> mEncryptedPeer;
std::weak_ptr<BatchedNetworkPeer> mBatchedPeer;
std::shared_ptr<NetworkPeer> mPeer;
std::chrono::time_point<std::chrono::_V2::steady_clock,std::chrono::duration<long,std::ratio<1,1000000000> > > mLastPacketTime;
std::chrono::time_point<std::chrono::_V2::steady_clock,std::chrono::duration<long,std::ratio<1,1000000000> > > mClosedTime;
bool mShouldCloseConnection;
bool mDisconnected;
std::bitset<2> mPausedChannels;
std::queue<std::string> mResumedPackets;
std::array<std::vector<std::string>,2> mPausedPackets;
};

```
#### NetworkHandler::IncomingPacketQueue
```cpp
/* 63002 */
struct NetworkHandler::IncomingPacketQueue
{
NetEventCallback *mCallbacksObj;
Bedrock::Threading::Mutex mMutex;
};

```
#### NetworkPacketEventListener
```cpp
/* 63038 */
struct NetworkPacketEventListener
{
int (**_vptr$NetworkPacketEventListener)(void);
};

```
#### NetworkPacketRecorder;
```cpp
/* 8222 */
struct NetworkPacketRecorder;

```
#### NetworkPeer
```cpp
/* 8247 */
struct NetworkPeer
{
int (**_vptr$NetworkPeer)(void);
std::shared_ptr<NetworkPeer> mPeer;
};

```
#### NetworkPeer::NetworkStatus
```cpp
/* 8630 */
struct NetworkPeer::NetworkStatus
{
NetworkPeer::NetworkLoad mLoad;
int mCurrentPing;
int mAveragePing;
int mApproximateMaxBps;
float mCurrentPacketLoss;
float mAveragePacketLoss;
uint64_t mTotalBytesReceived;
uint64_t mTotalBytesSent;
};

```
#### NetworkSettingOptions
```cpp
/* 72561 */
struct NetworkSettingOptions
{
uint16_t mCompressionThreshold;
};

```
#### NetworkStatistics::OverviewStats
```cpp
/* 63800 */
struct NetworkStatistics::OverviewStats
{
unsigned int sentBytesUnpacked;
unsigned int sentBytesPacked;
unsigned int receivedBytesUnpacked;
unsigned int receivedBytesPacked;
};

```
#### NetworkStatistics::PacketStats
```cpp
/* 63835 */
struct NetworkStatistics::PacketStats
{
unsigned int id;
unsigned int sentNum;
unsigned int sentBytes;
unsigned int receivedNum;
unsigned int receivedBytes;
};

```
#### NewType<int>
```cpp
/* 13185 */
struct NewType<int>
{
NewType<int>::Raw value;
};

```
#### NewType<long>
```cpp
/* 45313 */
struct NewType<long>
{
NewType<long>::Raw value;
};

```
#### NewType<unsigned short>
```cpp
/* 13216 */
struct NewType<unsigned short>
{
NewType<unsigned short>::Raw value;
};

```
#### NibblePair
```cpp
/* 35026 */
struct NibblePair
{
unsigned __int8 first : 4;
unsigned __int8 second : 4;
};

```
#### NoiseBasedColorPalette;
```cpp
/* 198718 */
struct NoiseBasedColorPalette;

```
#### NoiseBasedTemperatureAttributes
```cpp
/* 191330 */
struct NoiseBasedTemperatureAttributes
{
TemperatureCategory mTemperatureCategory;
};

```
#### NoteBlock::triggerEvent::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 459573 */
struct NoteBlock::triggerEvent::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### NpcAction
```cpp
/* 45374 */
struct NpcAction
{
int (**_vptr$NpcAction)(void);
const NpcActionType mType;
NpcActionMode mMode;
std::string mButtonName;
std::string mEvaluatedButtonName;
std::string mText;
std::optional<std::string > mEvaluatedText;
};

```
#### NpcComponent
```cpp
/* 44884 */
struct NpcComponent
{
int mCurrentSkin;
NpcGUIOffset mPortraitOffsets;
NpcGUIOffset mPickerOffsets;
std::vector<SkinData> mNPCSkins;
Json::Value mNPCData;
NpcActions mActions;
std::optional<std::string > mInteractText;
NpcComponent::TextFilter mInteractTextFilter;
};

```
#### NpcGUIOffset
```cpp
/* 44885 */
struct NpcGUIOffset
{
Vec3 mTranslation;
Vec3 mRotation;
Vec3 mScale;
};

```
#### NullSoundPlayer
```cpp
/* 86996 */
struct NullSoundPlayer
{
__int8 baseclass_0[8];
};

```
