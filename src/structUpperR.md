#### Rabbit::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124390 */
struct Rabbit::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Raid
```cpp
/* 52779 */
struct Raid
{
Raid::RaidState mCurrentRaidState;
Raid::GroupNumberType mCurrentGroupNumber;
Raid::GroupNumberType mNumGroupsInRaid;
Tick mTicksInState;
const Raid::DurationType mRaidPreparationTime;
const Raid::DurationType mGroupCompleteDelay;
Raid::DurationType mTicksUntilGroupComplete;
const Raid::DurationType mLocationHelpDelay;
Raid::DurationType mTicksUntilLocationHelp;
Vec3 mCurrentGroupSpawnPoint;
Raid::ActorIDCollection mRaiders;
Raid::RaiderCountType mNumRaidersSpawnedInCurrentGroup;
const Raid::FailureCountType mAllowedSpawnFailures;
Raid::FailureCountType mSpawnFailures;
const Raid::PickSpawnPointCallback mPickSpawnPointCallback;
const Raid::SpawnGroupCallback mSpawnGroupCallback;
const Raid::DoesActorExistCallback mDoesActorExistCallback;
Raid::NotificationCallback mOnSpawnPointChosenCallback;
Raid::NotificationCallback mOnGroupSpawnedCallback;
Raid::NotificationCallback mOnAwardRewardsCallback;
Raid::NotificationCallback mOnHelpLocateRaidersCallback;
};

```
#### RaidBossComponent
```cpp
/* 58284 */
struct RaidBossComponent
{
Weak<Village> mVillage;
ActorUniqueID mOwnerID;
std::string mName;
std::string mProgress;
int mPlayersRegistered;
bool mWaveStarted;
bool mRaidInProgress;
bool mHealthBarVisible;
float mHealthPercent;
AABB mBossBarVisibleBounds;
std::chrono::_V2::steady_clock::time_point mLastPlayerUpdate;
};

```
#### RailActivatorComponent
```cpp
/* 58423 */
struct RailActivatorComponent
{
__int8 gap0[1];
};

```
#### RailMovement
```cpp
/* 476685 */
struct RailMovement
{
__int8 gap0[1];
};

```
#### RailMovementComponent
```cpp
/* 107667 */
struct RailMovementComponent
{
float mMaxSpeed;
};

```
#### RailMovementDefinition
```cpp
/* 442674 */
struct RailMovementDefinition
{
float mMaxSpeed;
};

```
#### RakNet::AddressOrGUID
```cpp
/* 8619 */
struct RakNet::AddressOrGUID
{
RakNet::RakNetGUID rakNetGuid;
RakNet::SystemAddress systemAddress;
};

```
#### RakNet::BPSTracker
```cpp
/* 478026 */
struct RakNet::BPSTracker
{
uint64_t total1;
uint64_t lastSec1;
DataStructures::Queue<RakNet::BPSTracker::TimeAndValue2> dataQueue;
};

```
#### RakNet::BPSTracker::TimeAndValue2
```cpp
/* 478028 */
struct RakNet::BPSTracker::TimeAndValue2
{
uint64_t value1;
CCTimeType time;
};

```
#### RakNet::CCRakNetSlidingWindow
```cpp
/* 478016 */
struct RakNet::CCRakNetSlidingWindow
{
uint32_t MAXIMUM_MTU_INCLUDING_UDP_HEADER;
double cwnd;
double ssThresh;
CCTimeType oldestUnsentAck;
DatagramSequenceNumberType nextDatagramSequenceNumber;
DatagramSequenceNumberType nextCongestionControlBlock;
bool backoffThisBlock;
bool speedUpThisBlock;
DatagramSequenceNumberType expectedNextSequenceNumber;
bool _isContinuousSend;
double lastRtt;
double estimatedRTT;
double deviationRtt;
};

```
#### RakNet::HuffmanEncodingTree
```cpp
/* 478111 */
struct RakNet::HuffmanEncodingTree
{
HuffmanEncodingTreeNode *root;
RakNet::HuffmanEncodingTree::CharacterEncoding encodingTable[256];
};

```
#### RakNet::InternalPacketFixedSizeTransmissionHeader
```cpp
/* 477989 */
struct RakNet::InternalPacketFixedSizeTransmissionHeader
{
RakNet::MessageNumberType reliableMessageNumber;
RakNet::OrderingIndexType orderingIndex;
RakNet::OrderingIndexType sequencingIndex;
unsigned __int8 orderingChannel;
RakNet::SplitPacketIdType splitPacketId;
RakNet::SplitPacketIndexType splitPacketIndex;
RakNet::SplitPacketIndexType splitPacketCount;
RakNet::BitSize_t dataBitLength;
PacketReliability reliability;
};

```
#### RakNet::LocklessUint32_t
```cpp
/* 478121 */
struct RakNet::LocklessUint32_t
{
volatile uint32_t value;
};

```
#### RakNet::NetworkAdapter
```cpp
/* 73240 */
struct RakNet::NetworkAdapter
{
unsigned int attributeFlags;
int interfaceIndex;
bool isDisabled;
RakNet::SystemAddress addresses[21];
};

```
#### RakNet::PluginInterface2
```cpp
/* 478039 */
struct RakNet::PluginInterface2
{
int (**_vptr$PluginInterface2)(void);
RakNet::RakPeerInterface *rakPeerInterface;
RakNet::TCPInterface *tcpInterface;
};

```
#### RakNet::PublicKey;
```cpp
/* 478070 */
struct RakNet::PublicKey;

```
#### RakNet::RNS2EventHandler
```cpp
/* 477984 */
struct RakNet::RNS2EventHandler
{
int (**_vptr$RNS2EventHandler)(void);
};

```
#### RakNet::RNS2RecvStruct
```cpp
/* 478053 */
struct RakNet::RNS2RecvStruct
{
char data[1400];
int bytesRead;
RakNet::SystemAddress systemAddress;
RakNet::TimeUS timeRead;
RakNet::RakNetSocket2 *socket;
};

```
#### RakNet::RNS2_Windows_Linux_360
```cpp
/* 478150 */
struct RakNet::RNS2_Windows_Linux_360
{
__int8 gap0[1];
};

```
#### RakNet::RakNetSocket2Allocator
```cpp
/* 478151 */
struct RakNet::RakNetSocket2Allocator
{
__int8 gap0[1];
};

```
#### RakNet::RakNetStatistics
```cpp
/* 63850 */
struct RakNet::RakNetStatistics
{
uint64_t valueOverLastSecond[7];
uint64_t runningTotal[7];
RakNet::TimeUS connectionStartTime;
bool isLimitedByCongestionControl;
uint64_t BPSLimitByCongestionControl;
bool isLimitedByOutgoingBandwidthLimit;
uint64_t BPSLimitByOutgoingBandwidthLimit;
unsigned int messageInSendBuffer[4];
double bytesInSendBuffer[4];
unsigned int messagesInResendBuffer;
uint64_t bytesInResendBuffer;
float packetlossLastSecond;
float packetlossTotal;
};

```
#### RakNet::RakPeer::PingAndClockDifferential
```cpp
/* 478029 */
struct RakNet::RakPeer::PingAndClockDifferential
{
unsigned __int16 pingTime;
RakNet::Time clockDifferential;
};

```
#### RakNet::RakPeer::RemoteSystemStruct
```cpp
/* 477985 */
struct RakNet::RakPeer::RemoteSystemStruct
{
bool isActive;
RakNet::SystemAddress systemAddress;
RakNet::SystemAddress myExternalSystemAddress;
RakNet::SystemAddress theirInternalSystemAddress[20];
RakNet::ReliabilityLayer reliabilityLayer;
bool weInitiatedTheConnection;
RakNet::RakPeer::PingAndClockDifferential pingAndClockDifferential[5];
RakNet::Time pingAndClockDifferentialWriteIndex;
unsigned __int16 lowestPing;
RakNet::Time nextPingTime;
RakNet::Time lastReliableSend;
RakNet::Time connectionTime;
RakNet::RakNetGUID guid;
int MTUSize;
RakNet::RakNetSocket2 *rakNetSocket;
RakNet::SystemIndex remoteSystemIndex;
RakNet::RakPeer::RemoteSystemStruct::ConnectMode connectMode;
};

```
#### RakNet::RakPeer::SocketQueryOutput
```cpp
/* 478058 */
struct RakNet::RakPeer::SocketQueryOutput
{
DataStructures::List<RakNet::RakNetSocket2 *> sockets;
};

```
#### RakNet::RakPeerInterface
```cpp
/* 63571 */
struct RakNet::RakPeerInterface
{
int (**_vptr$RakPeerInterface)(void);
};

```
#### RakNet::RakString
```cpp
/* 73585 */
struct RakNet::RakString
{
RakNet::RakString::SharedString *sharedString;
};

```
#### RakNet::RakThread
```cpp
/* 478088 */
struct RakNet::RakThread
{
__int8 gap0[1];
};

```
#### RakNet::ReliabilityLayer
```cpp
/* 477986 */
struct RakNet::ReliabilityLayer
{
DataStructures::Queue<RakNet::InternalPacket *> outputQueue;
int splitMessageProgressInterval;
CCTimeType unreliableTimeout;
DataStructures::Queue<RakNet::ReliabilityLayer::DatagramHistoryNode> datagramHistory;
DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode> datagramHistoryMessagePool;
DataStructures::List<RakNet::ReliabilityLayer::UnreliableWithAckReceiptNode> unreliableWithAckReceiptHistory;
DatagramSequenceNumberType datagramHistoryPopCount;
DataStructures::MemoryPool<RakNet::InternalPacket> internalPacketPool;
RakNet::InternalPacket *resendBuffer[512];
RakNet::InternalPacket *resendLinkedListHead;
RakNet::InternalPacket *unreliableLinkedListHead;
RakNet::TimeMS timeLastDatagramArrived;
DataStructures::Heap<unsigned long,RakNet::InternalPacket *,false> outgoingPacketBuffer;
RakNet::reliabilityHeapWeightType outgoingPacketBufferNextWeights[4];
DataStructures::OrderedList<unsigned short,RakNet::SplitPacketChannel *,&RakNet::SplitPacketChannelComp> splitPacketChannelList;
RakNet::MessageNumberType sendReliableMessageNumberIndex;
RakNet::MessageNumberType internalOrderIndex;
bool deadConnection;
bool cheater;
RakNet::SplitPacketIdType splitPacketId;
RakNet::TimeMS timeoutTime;
RakNet::RakNetStatistics statistics;
RakNet::OrderingIndexType orderedWriteIndex[32];
RakNet::OrderingIndexType sequencedWriteIndex[32];
RakNet::OrderingIndexType orderedReadIndex[32];
RakNet::OrderingIndexType highestSequencedReadIndex[32];
DataStructures::Heap<unsigned long,RakNet::InternalPacket *,false> orderingHeaps[32];
RakNet::OrderingIndexType heapIndexOffsets[32];
DataStructures::Queue<bool> hasReceivedPacketQueue;
DatagramSequenceNumberType receivedPacketsBaseIndex;
bool resetReceivedPackets;
CCTimeType lastUpdateTime;
CCTimeType timeBetweenPackets;
CCTimeType nextSendTime;
CCTimeType ackPingSum;
unsigned __int8 ackPingIndex;
RakNet::RemoteSystemTimeType remoteSystemTime;
CCTimeType nextAllowedThroughputSample;
bool bandwidthExceededStatistic;
__int64 throughputCapCountdown;
unsigned int receivePacketCount;
CCTimeType elapsedTimeSinceLastUpdate;
CCTimeType nextAckTimeToSend;
RakNet::CCRakNetSlidingWindow congestionManager;
uint32_t unacknowledgedBytes;
DataStructures::List<RakNet::InternalPacket *> packetsToSendThisUpdate;
DataStructures::List<bool> packetsToDeallocThisUpdate;
DataStructures::List<unsigned int> packetsToSendThisUpdateDatagramBoundaries;
DataStructures::List<bool> datagramsToSendThisUpdateIsPair;
DataStructures::List<unsigned int> datagramSizesInBytes;
RakNet::BitSize_t datagramSizeSoFar;
RakNet::BitSize_t allDatagramSizesSoFar;
double totalUserDataBytesAcked;
CCTimeType timeOfLastContinualSend;
CCTimeType timeToNextUnreliableCull;
DataStructures::RangeList<RakNet::uint24_t> incomingAcks;
int countdownToNextPacketPair;
DataStructures::RangeList<RakNet::uint24_t> acknowlegements;
DataStructures::RangeList<RakNet::uint24_t> NAKs;
bool remoteSystemNeedsBAndAS;
DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData> refCountedDataPool;
RakNet::BPSTracker bpsMetrics[7];
CCTimeType lastBpsClear;
};

```
#### RakNet::ReliabilityLayer::DatagramHistoryNode
```cpp
/* 477999 */
struct RakNet::ReliabilityLayer::DatagramHistoryNode
{
RakNet::ReliabilityLayer::MessageNumberNode *head;
CCTimeType timeSent;
};

```
#### RakNet::ReliabilityLayer::MessageNumberNode
```cpp
/* 478072 */
struct RakNet::ReliabilityLayer::MessageNumberNode
{
DatagramSequenceNumberType messageNumber;
RakNet::ReliabilityLayer::MessageNumberNode *next;
};

```
#### RakNet::ReliabilityLayer::UnreliableWithAckReceiptNode
```cpp
/* 478003 */
struct RakNet::ReliabilityLayer::UnreliableWithAckReceiptNode
{
DatagramSequenceNumberType datagramNumber;
uint32_t sendReceiptSerial;
RakNet::TimeUS nextActionTime;
};

```
#### RakNet::RemoteClient
```cpp
/* 478123 */
struct RakNet::RemoteClient
{
__TCPSOCKET__ socket;
RakNet::SystemAddress systemAddress;
DataStructures::ByteQueue outgoingData;
bool isActive;
RakNet::SimpleMutex outgoingDataMutex;
RakNet::SimpleMutex isActiveMutex;
};

```
#### RakNet::RemoteSystemIndex
```cpp
/* 478032 */
struct RakNet::RemoteSystemIndex
{
unsigned int index;
RakNet::RemoteSystemIndex *next;
};

```
#### RakNet::SimpleMutex
```cpp
/* 73587 */
struct RakNet::SimpleMutex
{
pthread_mutex_t hMutex;
};

```
#### RakNet::SocketDescriptor
```cpp
/* 63572 */
struct RakNet::SocketDescriptor
{
unsigned __int16 port;
char hostAddress[32];
__int16 socketFamily;
unsigned __int16 remotePortRakNetWasStartedOn_PS3_PSP2;
int chromeInstance;
bool blockingSocket;
unsigned int extraSocketOptions;
};

```
#### RakNet::SocketLayer
```cpp
/* 478101 */
struct RakNet::SocketLayer
{
__int8 gap0[1];
};

```
#### RakNet::SplitPacketChannel
```cpp
/* 478013 */
struct RakNet::SplitPacketChannel
{
CCTimeType lastUpdateTime;
RakNet::SortedSplittedPackets splitPacketList;
RakNet::InternalPacket *firstPacket;
};

```
#### RakNet::StringCompressor
```cpp
/* 478106 */
struct RakNet::StringCompressor
{
DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison> huffmanEncodingTrees;
};

```
#### RakNet::StringTable
```cpp
/* 478115 */
struct RakNet::StringTable
{
DataStructures::OrderedList<char *,StrAndBool,&RakNet::StrAndBoolComp> orderedStringList;
};

```
#### RakNet::TCPInterface
```cpp
/* 4266 */
struct RakNet::TCPInterface
{
int (**_vptr$TCPInterface)(void);
DataStructures::List<RakNet::PluginInterface2 *> messageHandlerList;
RakNet::LocklessUint32_t isStarted;
RakNet::LocklessUint32_t threadRunning;
__TCPSOCKET__ listenSocket;
unsigned __int16 listenPort;
unsigned __int16 listenMaxIncomingConnections;
unsigned __int16 listenSocketFamily;
char *listenHostAddress;
DataStructures::Queue<RakNet::Packet *> headPush;
DataStructures::Queue<RakNet::Packet *> tailPush;
RakNet::RemoteClient *remoteClients;
int remoteClientsLength;
DataStructures::ThreadsafeAllocatingQueue<RakNet::Packet> incomingMessages;
DataStructures::ThreadsafeAllocatingQueue<RakNet::SystemAddress> newIncomingConnections;
DataStructures::ThreadsafeAllocatingQueue<RakNet::SystemAddress> lostConnections;
DataStructures::ThreadsafeAllocatingQueue<RakNet::SystemAddress> requestedCloseConnections;
DataStructures::ThreadsafeAllocatingQueue<RakNet::RemoteClient *> newRemoteClients;
RakNet::SimpleMutex completedConnectionAttemptMutex;
RakNet::SimpleMutex failedConnectionAttemptMutex;
DataStructures::Queue<RakNet::SystemAddress> completedConnectionAttempts;
DataStructures::Queue<RakNet::SystemAddress> failedConnectionAttempts;
int threadPriority;
DataStructures::List<int> blockingSocketList;
RakNet::SimpleMutex blockingSocketListMutex;
};

```
#### RakNet::uint24_t
```cpp
/* 477991 */
struct RakNet::uint24_t
{
uint32_t val;
};

```
#### RakNetInstance::ConnectionCallbacks
```cpp
/* 63501 */
struct RakNetInstance::ConnectionCallbacks
{
int (**_vptr$ConnectionCallbacks)(void);
};

```
#### RakNetInstance::PingCallbackData
```cpp
/* 73014 */
struct RakNetInstance::PingCallbackData
{
std::string mAddress;
std::function<void (unsigned int)> mAction;
};

```
#### RakNetInstance::_storeLocalIP::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 73243 */
struct RakNetInstance::_storeLocalIP::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### RakPeerHelper
```cpp
/* 63697 */
struct RakPeerHelper
{
RakNet::StartupResult mResult;
int mConnectionIndices[2];
uint16_t mBoundPorts[2];
RakPeerHelper::IPSupportInterface *mIPSupportInterface;
};

```
#### RakPeerHelper::IPSupportInterface
```cpp
/* 63502 */
struct RakPeerHelper::IPSupportInterface
{
int (**_vptr$IPSupportInterface)(void);
};

```
#### RakStringCleanup
```cpp
/* 478086 */
struct RakStringCleanup
{
__int8 gap0[1];
};

```
#### Random
```cpp
/* 31214 */
struct Random
{
Bedrock::Application::ThreadOwner<Core::Random> mRandom;
};

```
#### RandomBreachingGoal
```cpp
/* 119064 */
struct RandomBreachingGoal
{
__int8 baseclass_0[68];
int mCooldown;
int mTimer;
int mAttempts;
};

```
#### RandomPos
```cpp
/* 123026 */
struct RandomPos
{
__int8 gap0[1];
};

```
#### RandomValueBounds
```cpp
/* 104696 */
struct RandomValueBounds
{
float mMin;
float mMax;
};

```
#### Range<int,-1>
```cpp
/* 31933 */
struct Range<int,-1>
{
const int mBeginIDX;
const int mEndIDX;
};

```
#### Range<int,-1>::iterator
```cpp
/* 31934 */
struct Range<int,-1>::iterator
{
int mIndex;
};

```
#### Range<int,1>
```cpp
/* 35195 */
struct Range<int,1>
{
const int mBeginIDX;
const int mEndIDX;
};

```
#### Range<int,1>::iterator
```cpp
/* 35196 */
struct Range<int,1>::iterator
{
int mIndex;
};

```
#### Range<short,1>
```cpp
/* 109116 */
struct Range<short,1>
{
const __int16 mBeginIDX;
const __int16 mEndIDX;
};

```
#### Range<short,1>::iterator
```cpp
/* 109117 */
struct Range<short,1>::iterator
{
__int16 mIndex;
};

```
#### Range<unsigned char,'_x01'>
```cpp
/* 185247 */
struct Range<unsigned char,'_x01'>
{
const unsigned __int8 mBeginIDX;
const unsigned __int8 mEndIDX;
};

```
#### Range<unsigned char,'_x01'>::iterator
```cpp
/* 185248 */
struct Range<unsigned char,'_x01'>::iterator
{
unsigned __int8 mIndex;
};

```
#### Range<unsigned int,1>
```cpp
/* 40599 */
struct Range<unsigned int,1>
{
const unsigned int mBeginIDX;
const unsigned int mEndIDX;
};

```
#### Range<unsigned int,1>::iterator
```cpp
/* 40600 */
struct Range<unsigned int,1>::iterator
{
unsigned int mIndex;
};

```
#### Range<unsigned long,1>
```cpp
/* 63715 */
struct Range<unsigned long,1>
{
const unsigned __int64 mBeginIDX;
const unsigned __int64 mEndIDX;
};

```
#### Range<unsigned long,1>::iterator
```cpp
/* 63716 */
struct Range<unsigned long,1>::iterator
{
unsigned __int64 mIndex;
};

```
#### Range<unsigned short,1>
```cpp
/* 103052 */
struct Range<unsigned short,1>
{
const unsigned __int16 mBeginIDX;
const unsigned __int16 mEndIDX;
};

```
#### Range<unsigned short,1>::iterator
```cpp
/* 103053 */
struct Range<unsigned short,1>::iterator
{
unsigned __int16 mIndex;
};

```
#### RateLimiter
```cpp
/* 484857 */
struct RateLimiter
{
const size_t mLimit;
const std::chrono::seconds mTimeIntervalSeconds;
std::vector<std::chrono::time_point<std::chrono::_V2::steady_clock,std::chrono::duration<long,std::ratio<1,1000000000> > >> mInstances;
};

```
#### ReadOnlyBinaryStream
```cpp
/* 33520 */
struct ReadOnlyBinaryStream
{
int (**_vptr$ReadOnlyBinaryStream)(void);
size_t mReadPointer;
const std::string mOwnedBuffer;
const std::string *mBuffer;
};

```
#### Recipe
```cpp
/* 75620 */
struct Recipe
{
int (**_vptr$Recipe)(void);
std::string mRecipeId;
ItemPack mMyItems;
mce::UUID mMyId;
int mWidth;
int mHeight;
int mPriority;
Recipe::Ingredients mMyIngredients;
Util::HashString mTag;
};

```
#### Recipes
```cpp
/* 77471 */
struct Recipes
{
ResourcePackManager *mResourcePackManager;
std::map<Util::HashString,std::map<std::string,std::unique_ptr<Recipe>>> mRecipes;
std::map<Recipes::FurnaceRecipeKey,ItemInstance> mFurnaceRecipes;
bool mInitializing;
std::map<ItemInstance,std::unordered_map<std::string,Recipe *>,SortItemInstanceIdAux,std::allocator<std::pair<const ItemInstance,std::unordered_map<std::string,Recipe *> > > > mRecipesByOutput;
RecipeListenerList mListeners;
};

```
#### Recipes::FurnaceRecipeKey
```cpp
/* 75806 */
struct Recipes::FurnaceRecipeKey
{
int mID;
Util::HashString mTag;
};

```
#### Recipes::addShapedRecipe::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 185249 */
struct Recipes::addShapedRecipe::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Recipes::addShapelessRecipe::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 185251 */
struct Recipes::addShapelessRecipe::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### RedstoneTorchCapacitor::State
```cpp
/* 464014 */
struct RedstoneTorchCapacitor::State
{
bool mOn;
bool mHalfFrame;
bool mChanged;
};

```
#### RegionFile
```cpp
/* 463321 */
struct RegionFile
{
int (**_vptr$RegionFile)(void);
Core::File mFile;
Core::HeapPathBuffer mFileName;
std::array<int,1024> mOffsets;
std::array<int,1024> mEmptyChunk;
RegionFile::FreeSectorMap mSectorFree;
};

```
#### RegisteredTagFilter
```cpp
/* 40659 */
struct RegisteredTagFilter
{
TagSetID mIncludeSet;
TagSetID mExcludeSet;
};

```
#### RenderParams
```cpp
/* 88682 */
struct RenderParams
{
BaseActorRenderContext *mBaseActorRenderContext;
MolangVariableMap *mVariables;
AnimationComponent *mAnimationComponent;
AnimationComponent *mRootAnimationComponent;
DataDrivenModel *mRootModel;
DataDrivenModel *mModel;
Actor *mActor;
BlockSource *mBlockSource;
ActorRenderData *mActorRenderData;
int32_t mVertexCount;
uint16_t mSubRenderLayerIndex;
std::function<float ()> mRandomFunction;
float mCameraDistance;
float mParams[8];
RenderParams::$3D9EB0E7A2790D70080124A37CC6ABC8 mFlags;
};

```
#### RenderParams::$3D9EB0E7A2790D70080124A37CC6ABC8::$7CDB70B13784CF5DCA20C1417F11D194
```cpp
/* 88690 */
struct RenderParams::$3D9EB0E7A2790D70080124A37CC6ABC8::$7CDB70B13784CF5DCA20C1417F11D194
{
unsigned __int32 mIsChild : 1;
};

```
#### ResourceInformation
```cpp
/* 5756 */
struct ResourceInformation
{
std::string mDescription;
SemVersion mVersion;
mce::UUID mUUID;
ResourceInformation::ResourceType mType;
std::string mEntry;
};

```
#### ResourceLoadManager
```cpp
/* 60803 */
struct ResourceLoadManager
{
Scheduler *mScheduler;
WorkerPool *mWorkerPool;
std::map<ResourceLoadType,std::unique_ptr<ResourceLoadManager::ResourceLoadTaskGroup>> mResourceLoadTaskGroups;
size_t mAppSuspended;
};

```
#### ResourceLoadManager::LoadOrder
```cpp
/* 60805 */
struct ResourceLoadManager::LoadOrder
{
__int8 gap0[1];
};

```
#### ResourceLoadManager::TaskGroupState
```cpp
/* 84459 */
struct ResourceLoadManager::TaskGroupState
{
bool mRunning;
size_t mPaused;
};

```
#### ResourceLoader
```cpp
/* 85234 */
struct ResourceLoader
{
int (**_vptr$ResourceLoader)(void);
std::function<Core::PathBuffer<std::string > ()> mGetPath;
};

```
#### ResourceLocation
```cpp
/* 2549 */
struct ResourceLocation
{
ResourceFileSystem mFileSystem;
Core::HeapPathBuffer mPath;
HashType64 mPathHash;
size_t mFullHash;
};

```
#### ResourceMetadata
```cpp
/* 5771 */
struct ResourceMetadata
{
std::vector<std::string> mAuthors;
std::string mUrl;
std::string mLicense;
};

```
#### ResourcePack
```cpp
/* 4191 */
struct ResourcePack
{
bool mHidden;
bool mError;
Pack *mPack;
std::unique_ptr<PackAccessStrategy> mSubpackAccessStrategy;
PackReport mPackReport;
std::vector<std::unique_ptr<Pack>> mSubPacks;
std::vector<std::unique_ptr<ResourcePack>> mSubResourcePacks;
Core::HeapPathBuffer mIconPath;
double mLoadTime;
bool mIsBaseGamePack;
bool mIsSlicePack;
ResourceSignature mResourceSignature;
};

```
#### ResourcePackContents
```cpp
/* 5710 */
struct ResourcePackContents
{
uint32_t mUIJson;
uint32_t mUITextures;
uint32_t mSound;
uint32_t mBlockJson;
uint32_t mBlockTextures;
uint32_t mItemTextures;
uint32_t mEntityTextures;
uint32_t mModelGeometry;
uint32_t mAnimations;
uint32_t mMaterials;
uint32_t mLanguages;
};

```
#### ResourcePackListener
```cpp
/* 81168 */
struct ResourcePackListener
{
int (**_vptr$ResourcePackListener)(void);
};

```
#### ResourcePackMergeStrategy
```cpp
/* 85264 */
struct ResourcePackMergeStrategy
{
int (**_vptr$ResourcePackMergeStrategy)(void);
};

```
#### ResourcePackRepository
```cpp
/* 5700 */
struct ResourcePackRepository
{
Core::FilePathManager *mFilePathManager;
std::vector<std::unique_ptr<ResourcePack>> mAllResourcePacks;
std::unique_ptr<CompositePackSource> mPackSource;
std::unique_ptr<CompositePackSource> mCachePackSource;
std::unique_ptr<CompositePackSource> mWorldPackSource;
std::unique_ptr<CompositePackSource> mPremiumWorldTemplatePackSource;
std::unique_ptr<PackSourceReport> mPackSourceReport;
ResourcePack *mVanillaPack;
ResourcePack *mChemistryPack;
ResourcePack *mChemistryServerPack;
std::vector<ResourceLocation> mInvalidPackLocation;
std::vector<ResourceLocation> mInvalidBehaviorPackLocation;
std::vector<ResourceLocation> mInvalidResourcePackLocation;
std::vector<ResourceLocation> mInvalidTemplatePackLocation;
IMinecraftEventing *mEventing;
PackManifestFactory *mManifestFactory;
IContentAccessibilityProvider *mContentAccessibility;
Core::HeapPathBuffer mCurrentWorldPath;
Core::HeapPathBuffer mCurrentPremiumWorldTemplatePath;
ContentKeyMap mTempCacheContentKeys;
const int mKnownPacksFileVerison;
std::unique_ptr<PackSettingsFactory> mPackSettingsFactory;
PackSourceFactory *mPackSourceFactory;
ResourcePackRepository::KnownPackContainer mCachedValidUserPacks;
ResourcePackRepository::KnownPackContainer mCachedInvalidUserPacks;
std::map<void *,std::function<void (ResourcePack *)>> mRemoveResourcePackCallback;
std::unique_ptr<TaskGroup> mInitTaskGroup;
Bedrock::Threading::Mutex mInitializeMutex;
std::atomic<bool> mInitialized;
std::atomic<bool> mReloadUserPacksRequested;
std::atomic<bool> mRefreshPacksRequested;
ContentIdentity mCurrentPremiumWorldTemplateIdentity;
};

```
#### ResourcePackRepository::KnownPackContainer
```cpp
/* 5706 */
struct ResourcePackRepository::KnownPackContainer
{
std::vector<ResourcePackRepository::KnownPackInfo> mPacks;
};

```
#### ResourcePackRepository::KnownPackInfo
```cpp
/* 4094 */
struct ResourcePackRepository::KnownPackInfo
{
bool mDiscoveredOnDisk;
ResourceLocation mResourceLocation;
std::vector<std::string> mPastHashes;
PackIdVersion mIdentity;
};

```
#### ResourcePackStack
```cpp
/* 2991 */
struct ResourcePackStack
{
int (**_vptr$ResourcePackStack)(void);
ResourcePackStack::PackInstanceStack mStack;
std::unique_ptr<PackSourceReport> mPackSourceReport;
};

```
#### ResourcePackTransmissionManager
```cpp
/* 62768 */
struct ResourcePackTransmissionManager
{
std::unordered_map<unsigned long,std::unordered_map<std::string,std::shared_ptr<ResourcePackFileDownloaderManager>>> mResourceDownloadManagers;
std::unordered_map<unsigned long,std::unordered_map<std::string,std::shared_ptr<ResourcePackFileUploadManager>>> mResourceUploadManagers;
std::unordered_set<unsigned long> mRemovedResourceDownloadManagers;
std::unordered_set<unsigned long> mRemovedResourceUploadManagers;
std::unique_ptr<TaskGroup> mIOTaskGroup;
};

```
#### ResourcePacksInfoData
```cpp
/* 45309 */
struct ResourcePacksInfoData
{
bool mTexturePackRequired;
bool mHasScripts;
bool mHasExceptions;
std::vector<ResourcePackInfoData> mAddOnPacks;
std::vector<ResourcePackInfoData> mTexturePacks;
};

```
#### ResourcePath
```cpp
/* 60575 */
struct ResourcePath
{
std::string mPackId;
std::string mPath;
};

```
#### ResourceSignature
```cpp
/* 4193 */
struct ResourceSignature
{
std::unordered_map<std::string,std::string> mSignatureFileContents;
};

```
#### ResourceUtil
```cpp
/* 484001 */
struct ResourceUtil
{
__int8 gap0[1];
};

```
#### RiverTransformation;
```cpp
/* 40587 */
struct RiverTransformation;

```
#### RoleChecker
```cpp
/* 421290 */
struct RoleChecker
{
std::weak_ptr<RoleCheckerCallback> mPendingCallback;
};

```
#### RoleCheckerCallback
```cpp
/* 421295 */
struct RoleCheckerCallback
{
RoleChecker::OnRoleAcquired mCallback;
};

```
#### RopePoint
```cpp
/* 88873 */
struct RopePoint
{
Vec3 mOldPos;
Vec3 mToNewPos;
};

```
#### RopePointsRef
```cpp
/* 109073 */
struct RopePointsRef
{
const RopePoints *mPoints;
Bedrock::Threading::Mutex *mPointMutex;
};

```
#### RopeSystem
```cpp
/* 88859 */
struct RopeSystem
{
bool mWaveApplied;
RopePoints mQueuedRenderPoints;
RopePoints mRenderPoints;
std::vector<RopeNode> mNodes;
std::vector<AABBBucket> mColliderBuckets;
std::vector<RopeWave> mWaves;
RopeParams mParams;
std::set<AABB,AABBPred,std::allocator<AABB> > mBlacklistedColliders;
Vec3 mPrevStartPin;
Vec3 mPrevEndPin;
size_t mCutNode;
size_t mCutRenderNode;
size_t mMinNodes;
size_t mCutTicks;
ActorUniqueID mEndPinEntity;
std::atomic_flag mTicking;
Bedrock::Threading::Mutex mRenderMutex;
bool mAbandonCollision;
Vec3 mStartPin;
Vec3 mEndPin;
size_t mToCutNode;
};

```
#### RopeWave
```cpp
/* 88925 */
struct RopeWave
{
Vec3 mForce;
float mSpeed;
float mDamping;
size_t mCurNode;
float mDistAlongNode;
RopeWave::Direction mDir;
};

```
#### RuntimeLightingManager
```cpp
/* 34696 */
struct RuntimeLightingManager
{
std::unordered_map<ChunkPos,RuntimeLightingManager::RuntimeLightingSubchunkList> mLevelChunksToLight;
std::vector<RuntimeLightingManager::RelightingChunkElement> mListOfChunksToProcess;
std::vector<BlockPos> mProcessedSubchunks;
std::vector<BlockPos> mBrightnessChangedList;
Dimension *mDimension;
bool mWorkerScheduled;
float mLightingTimeboxTime;
};

```
#### RuntimeLightingManager::RelightingChunkElement
```cpp
/* 34731 */
struct RuntimeLightingManager::RelightingChunkElement
{
float mDist;
ChunkPos mChunkPos;
size_t mSubChunkIndex;
std::vector<SubChunkLightUpdate> *mAlteredBlockList;
};

```
#### RuntimeLightingManager::RuntimeLightingSubchunkList
```cpp
/* 253798 */
struct RuntimeLightingManager::RuntimeLightingSubchunkList
{
std::array<std::vector<SubChunkLightUpdate>,16> mAlteredSubchunkBlockList;
};

```
#### Rabbit::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124390 */
struct Rabbit::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Raid
```cpp
/* 52779 */
struct Raid
{
Raid::RaidState mCurrentRaidState;
Raid::GroupNumberType mCurrentGroupNumber;
Raid::GroupNumberType mNumGroupsInRaid;
Tick mTicksInState;
const Raid::DurationType mRaidPreparationTime;
const Raid::DurationType mGroupCompleteDelay;
Raid::DurationType mTicksUntilGroupComplete;
const Raid::DurationType mLocationHelpDelay;
Raid::DurationType mTicksUntilLocationHelp;
Vec3 mCurrentGroupSpawnPoint;
Raid::ActorIDCollection mRaiders;
Raid::RaiderCountType mNumRaidersSpawnedInCurrentGroup;
const Raid::FailureCountType mAllowedSpawnFailures;
Raid::FailureCountType mSpawnFailures;
const Raid::PickSpawnPointCallback mPickSpawnPointCallback;
const Raid::SpawnGroupCallback mSpawnGroupCallback;
const Raid::DoesActorExistCallback mDoesActorExistCallback;
Raid::NotificationCallback mOnSpawnPointChosenCallback;
Raid::NotificationCallback mOnGroupSpawnedCallback;
Raid::NotificationCallback mOnAwardRewardsCallback;
Raid::NotificationCallback mOnHelpLocateRaidersCallback;
};

```
#### RaidBossComponent
```cpp
/* 58284 */
struct RaidBossComponent
{
Weak<Village> mVillage;
ActorUniqueID mOwnerID;
std::string mName;
std::string mProgress;
int mPlayersRegistered;
bool mWaveStarted;
bool mRaidInProgress;
bool mHealthBarVisible;
float mHealthPercent;
AABB mBossBarVisibleBounds;
std::chrono::_V2::steady_clock::time_point mLastPlayerUpdate;
};

```
#### RailActivatorComponent
```cpp
/* 58423 */
struct RailActivatorComponent
{
__int8 gap0[1];
};

```
#### RailMovement
```cpp
/* 476685 */
struct RailMovement
{
__int8 gap0[1];
};

```
#### RailMovementComponent
```cpp
/* 107667 */
struct RailMovementComponent
{
float mMaxSpeed;
};

```
#### RailMovementDefinition
```cpp
/* 442674 */
struct RailMovementDefinition
{
float mMaxSpeed;
};

```
#### RakNet::AddressOrGUID
```cpp
/* 8619 */
struct RakNet::AddressOrGUID
{
RakNet::RakNetGUID rakNetGuid;
RakNet::SystemAddress systemAddress;
};

```
#### RakNet::BPSTracker
```cpp
/* 478026 */
struct RakNet::BPSTracker
{
uint64_t total1;
uint64_t lastSec1;
DataStructures::Queue<RakNet::BPSTracker::TimeAndValue2> dataQueue;
};

```
#### RakNet::BPSTracker::TimeAndValue2
```cpp
/* 478028 */
struct RakNet::BPSTracker::TimeAndValue2
{
uint64_t value1;
CCTimeType time;
};

```
#### RakNet::CCRakNetSlidingWindow
```cpp
/* 478016 */
struct RakNet::CCRakNetSlidingWindow
{
uint32_t MAXIMUM_MTU_INCLUDING_UDP_HEADER;
double cwnd;
double ssThresh;
CCTimeType oldestUnsentAck;
DatagramSequenceNumberType nextDatagramSequenceNumber;
DatagramSequenceNumberType nextCongestionControlBlock;
bool backoffThisBlock;
bool speedUpThisBlock;
DatagramSequenceNumberType expectedNextSequenceNumber;
bool _isContinuousSend;
double lastRtt;
double estimatedRTT;
double deviationRtt;
};

```
#### RakNet::HuffmanEncodingTree
```cpp
/* 478111 */
struct RakNet::HuffmanEncodingTree
{
HuffmanEncodingTreeNode *root;
RakNet::HuffmanEncodingTree::CharacterEncoding encodingTable[256];
};

```
#### RakNet::InternalPacketFixedSizeTransmissionHeader
```cpp
/* 477989 */
struct RakNet::InternalPacketFixedSizeTransmissionHeader
{
RakNet::MessageNumberType reliableMessageNumber;
RakNet::OrderingIndexType orderingIndex;
RakNet::OrderingIndexType sequencingIndex;
unsigned __int8 orderingChannel;
RakNet::SplitPacketIdType splitPacketId;
RakNet::SplitPacketIndexType splitPacketIndex;
RakNet::SplitPacketIndexType splitPacketCount;
RakNet::BitSize_t dataBitLength;
PacketReliability reliability;
};

```
#### RakNet::LocklessUint32_t
```cpp
/* 478121 */
struct RakNet::LocklessUint32_t
{
volatile uint32_t value;
};

```
#### RakNet::NetworkAdapter
```cpp
/* 73240 */
struct RakNet::NetworkAdapter
{
unsigned int attributeFlags;
int interfaceIndex;
bool isDisabled;
RakNet::SystemAddress addresses[21];
};

```
#### RakNet::PluginInterface2
```cpp
/* 478039 */
struct RakNet::PluginInterface2
{
int (**_vptr$PluginInterface2)(void);
RakNet::RakPeerInterface *rakPeerInterface;
RakNet::TCPInterface *tcpInterface;
};

```
#### RakNet::PublicKey;
```cpp
/* 478070 */
struct RakNet::PublicKey;

```
#### RakNet::RNS2EventHandler
```cpp
/* 477984 */
struct RakNet::RNS2EventHandler
{
int (**_vptr$RNS2EventHandler)(void);
};

```
#### RakNet::RNS2RecvStruct
```cpp
/* 478053 */
struct RakNet::RNS2RecvStruct
{
char data[1400];
int bytesRead;
RakNet::SystemAddress systemAddress;
RakNet::TimeUS timeRead;
RakNet::RakNetSocket2 *socket;
};

```
#### RakNet::RNS2_Windows_Linux_360
```cpp
/* 478150 */
struct RakNet::RNS2_Windows_Linux_360
{
__int8 gap0[1];
};

```
#### RakNet::RakNetSocket2Allocator
```cpp
/* 478151 */
struct RakNet::RakNetSocket2Allocator
{
__int8 gap0[1];
};

```
#### RakNet::RakNetStatistics
```cpp
/* 63850 */
struct RakNet::RakNetStatistics
{
uint64_t valueOverLastSecond[7];
uint64_t runningTotal[7];
RakNet::TimeUS connectionStartTime;
bool isLimitedByCongestionControl;
uint64_t BPSLimitByCongestionControl;
bool isLimitedByOutgoingBandwidthLimit;
uint64_t BPSLimitByOutgoingBandwidthLimit;
unsigned int messageInSendBuffer[4];
double bytesInSendBuffer[4];
unsigned int messagesInResendBuffer;
uint64_t bytesInResendBuffer;
float packetlossLastSecond;
float packetlossTotal;
};

```
#### RakNet::RakPeer::PingAndClockDifferential
```cpp
/* 478029 */
struct RakNet::RakPeer::PingAndClockDifferential
{
unsigned __int16 pingTime;
RakNet::Time clockDifferential;
};

```
#### RakNet::RakPeer::RemoteSystemStruct
```cpp
/* 477985 */
struct RakNet::RakPeer::RemoteSystemStruct
{
bool isActive;
RakNet::SystemAddress systemAddress;
RakNet::SystemAddress myExternalSystemAddress;
RakNet::SystemAddress theirInternalSystemAddress[20];
RakNet::ReliabilityLayer reliabilityLayer;
bool weInitiatedTheConnection;
RakNet::RakPeer::PingAndClockDifferential pingAndClockDifferential[5];
RakNet::Time pingAndClockDifferentialWriteIndex;
unsigned __int16 lowestPing;
RakNet::Time nextPingTime;
RakNet::Time lastReliableSend;
RakNet::Time connectionTime;
RakNet::RakNetGUID guid;
int MTUSize;
RakNet::RakNetSocket2 *rakNetSocket;
RakNet::SystemIndex remoteSystemIndex;
RakNet::RakPeer::RemoteSystemStruct::ConnectMode connectMode;
};

```
#### RakNet::RakPeer::SocketQueryOutput
```cpp
/* 478058 */
struct RakNet::RakPeer::SocketQueryOutput
{
DataStructures::List<RakNet::RakNetSocket2 *> sockets;
};

```
#### RakNet::RakPeerInterface
```cpp
/* 63571 */
struct RakNet::RakPeerInterface
{
int (**_vptr$RakPeerInterface)(void);
};

```
#### RakNet::RakString
```cpp
/* 73585 */
struct RakNet::RakString
{
RakNet::RakString::SharedString *sharedString;
};

```
#### RakNet::RakThread
```cpp
/* 478088 */
struct RakNet::RakThread
{
__int8 gap0[1];
};

```
#### RakNet::ReliabilityLayer
```cpp
/* 477986 */
struct RakNet::ReliabilityLayer
{
DataStructures::Queue<RakNet::InternalPacket *> outputQueue;
int splitMessageProgressInterval;
CCTimeType unreliableTimeout;
DataStructures::Queue<RakNet::ReliabilityLayer::DatagramHistoryNode> datagramHistory;
DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode> datagramHistoryMessagePool;
DataStructures::List<RakNet::ReliabilityLayer::UnreliableWithAckReceiptNode> unreliableWithAckReceiptHistory;
DatagramSequenceNumberType datagramHistoryPopCount;
DataStructures::MemoryPool<RakNet::InternalPacket> internalPacketPool;
RakNet::InternalPacket *resendBuffer[512];
RakNet::InternalPacket *resendLinkedListHead;
RakNet::InternalPacket *unreliableLinkedListHead;
RakNet::TimeMS timeLastDatagramArrived;
DataStructures::Heap<unsigned long,RakNet::InternalPacket *,false> outgoingPacketBuffer;
RakNet::reliabilityHeapWeightType outgoingPacketBufferNextWeights[4];
DataStructures::OrderedList<unsigned short,RakNet::SplitPacketChannel *,&RakNet::SplitPacketChannelComp> splitPacketChannelList;
RakNet::MessageNumberType sendReliableMessageNumberIndex;
RakNet::MessageNumberType internalOrderIndex;
bool deadConnection;
bool cheater;
RakNet::SplitPacketIdType splitPacketId;
RakNet::TimeMS timeoutTime;
RakNet::RakNetStatistics statistics;
RakNet::OrderingIndexType orderedWriteIndex[32];
RakNet::OrderingIndexType sequencedWriteIndex[32];
RakNet::OrderingIndexType orderedReadIndex[32];
RakNet::OrderingIndexType highestSequencedReadIndex[32];
DataStructures::Heap<unsigned long,RakNet::InternalPacket *,false> orderingHeaps[32];
RakNet::OrderingIndexType heapIndexOffsets[32];
DataStructures::Queue<bool> hasReceivedPacketQueue;
DatagramSequenceNumberType receivedPacketsBaseIndex;
bool resetReceivedPackets;
CCTimeType lastUpdateTime;
CCTimeType timeBetweenPackets;
CCTimeType nextSendTime;
CCTimeType ackPingSum;
unsigned __int8 ackPingIndex;
RakNet::RemoteSystemTimeType remoteSystemTime;
CCTimeType nextAllowedThroughputSample;
bool bandwidthExceededStatistic;
__int64 throughputCapCountdown;
unsigned int receivePacketCount;
CCTimeType elapsedTimeSinceLastUpdate;
CCTimeType nextAckTimeToSend;
RakNet::CCRakNetSlidingWindow congestionManager;
uint32_t unacknowledgedBytes;
DataStructures::List<RakNet::InternalPacket *> packetsToSendThisUpdate;
DataStructures::List<bool> packetsToDeallocThisUpdate;
DataStructures::List<unsigned int> packetsToSendThisUpdateDatagramBoundaries;
DataStructures::List<bool> datagramsToSendThisUpdateIsPair;
DataStructures::List<unsigned int> datagramSizesInBytes;
RakNet::BitSize_t datagramSizeSoFar;
RakNet::BitSize_t allDatagramSizesSoFar;
double totalUserDataBytesAcked;
CCTimeType timeOfLastContinualSend;
CCTimeType timeToNextUnreliableCull;
DataStructures::RangeList<RakNet::uint24_t> incomingAcks;
int countdownToNextPacketPair;
DataStructures::RangeList<RakNet::uint24_t> acknowlegements;
DataStructures::RangeList<RakNet::uint24_t> NAKs;
bool remoteSystemNeedsBAndAS;
DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData> refCountedDataPool;
RakNet::BPSTracker bpsMetrics[7];
CCTimeType lastBpsClear;
};

```
#### RakNet::ReliabilityLayer::DatagramHistoryNode
```cpp
/* 477999 */
struct RakNet::ReliabilityLayer::DatagramHistoryNode
{
RakNet::ReliabilityLayer::MessageNumberNode *head;
CCTimeType timeSent;
};

```
#### RakNet::ReliabilityLayer::MessageNumberNode
```cpp
/* 478072 */
struct RakNet::ReliabilityLayer::MessageNumberNode
{
DatagramSequenceNumberType messageNumber;
RakNet::ReliabilityLayer::MessageNumberNode *next;
};

```
#### RakNet::ReliabilityLayer::UnreliableWithAckReceiptNode
```cpp
/* 478003 */
struct RakNet::ReliabilityLayer::UnreliableWithAckReceiptNode
{
DatagramSequenceNumberType datagramNumber;
uint32_t sendReceiptSerial;
RakNet::TimeUS nextActionTime;
};

```
#### RakNet::RemoteClient
```cpp
/* 478123 */
struct RakNet::RemoteClient
{
__TCPSOCKET__ socket;
RakNet::SystemAddress systemAddress;
DataStructures::ByteQueue outgoingData;
bool isActive;
RakNet::SimpleMutex outgoingDataMutex;
RakNet::SimpleMutex isActiveMutex;
};

```
#### RakNet::RemoteSystemIndex
```cpp
/* 478032 */
struct RakNet::RemoteSystemIndex
{
unsigned int index;
RakNet::RemoteSystemIndex *next;
};

```
#### RakNet::SimpleMutex
```cpp
/* 73587 */
struct RakNet::SimpleMutex
{
pthread_mutex_t hMutex;
};

```
#### RakNet::SocketDescriptor
```cpp
/* 63572 */
struct RakNet::SocketDescriptor
{
unsigned __int16 port;
char hostAddress[32];
__int16 socketFamily;
unsigned __int16 remotePortRakNetWasStartedOn_PS3_PSP2;
int chromeInstance;
bool blockingSocket;
unsigned int extraSocketOptions;
};

```
#### RakNet::SocketLayer
```cpp
/* 478101 */
struct RakNet::SocketLayer
{
__int8 gap0[1];
};

```
#### RakNet::SplitPacketChannel
```cpp
/* 478013 */
struct RakNet::SplitPacketChannel
{
CCTimeType lastUpdateTime;
RakNet::SortedSplittedPackets splitPacketList;
RakNet::InternalPacket *firstPacket;
};

```
#### RakNet::StringCompressor
```cpp
/* 478106 */
struct RakNet::StringCompressor
{
DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison> huffmanEncodingTrees;
};

```
#### RakNet::StringTable
```cpp
/* 478115 */
struct RakNet::StringTable
{
DataStructures::OrderedList<char *,StrAndBool,&RakNet::StrAndBoolComp> orderedStringList;
};

```
#### RakNet::TCPInterface
```cpp
/* 4266 */
struct RakNet::TCPInterface
{
int (**_vptr$TCPInterface)(void);
DataStructures::List<RakNet::PluginInterface2 *> messageHandlerList;
RakNet::LocklessUint32_t isStarted;
RakNet::LocklessUint32_t threadRunning;
__TCPSOCKET__ listenSocket;
unsigned __int16 listenPort;
unsigned __int16 listenMaxIncomingConnections;
unsigned __int16 listenSocketFamily;
char *listenHostAddress;
DataStructures::Queue<RakNet::Packet *> headPush;
DataStructures::Queue<RakNet::Packet *> tailPush;
RakNet::RemoteClient *remoteClients;
int remoteClientsLength;
DataStructures::ThreadsafeAllocatingQueue<RakNet::Packet> incomingMessages;
DataStructures::ThreadsafeAllocatingQueue<RakNet::SystemAddress> newIncomingConnections;
DataStructures::ThreadsafeAllocatingQueue<RakNet::SystemAddress> lostConnections;
DataStructures::ThreadsafeAllocatingQueue<RakNet::SystemAddress> requestedCloseConnections;
DataStructures::ThreadsafeAllocatingQueue<RakNet::RemoteClient *> newRemoteClients;
RakNet::SimpleMutex completedConnectionAttemptMutex;
RakNet::SimpleMutex failedConnectionAttemptMutex;
DataStructures::Queue<RakNet::SystemAddress> completedConnectionAttempts;
DataStructures::Queue<RakNet::SystemAddress> failedConnectionAttempts;
int threadPriority;
DataStructures::List<int> blockingSocketList;
RakNet::SimpleMutex blockingSocketListMutex;
};

```
#### RakNet::uint24_t
```cpp
/* 477991 */
struct RakNet::uint24_t
{
uint32_t val;
};

```
#### RakNetInstance::ConnectionCallbacks
```cpp
/* 63501 */
struct RakNetInstance::ConnectionCallbacks
{
int (**_vptr$ConnectionCallbacks)(void);
};

```
#### RakNetInstance::PingCallbackData
```cpp
/* 73014 */
struct RakNetInstance::PingCallbackData
{
std::string mAddress;
std::function<void (unsigned int)> mAction;
};

```
#### RakNetInstance::_storeLocalIP::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 73243 */
struct RakNetInstance::_storeLocalIP::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### RakPeerHelper
```cpp
/* 63697 */
struct RakPeerHelper
{
RakNet::StartupResult mResult;
int mConnectionIndices[2];
uint16_t mBoundPorts[2];
RakPeerHelper::IPSupportInterface *mIPSupportInterface;
};

```
#### RakPeerHelper::IPSupportInterface
```cpp
/* 63502 */
struct RakPeerHelper::IPSupportInterface
{
int (**_vptr$IPSupportInterface)(void);
};

```
#### RakStringCleanup
```cpp
/* 478086 */
struct RakStringCleanup
{
__int8 gap0[1];
};

```
#### Random
```cpp
/* 31214 */
struct Random
{
Bedrock::Application::ThreadOwner<Core::Random> mRandom;
};

```
#### RandomBreachingGoal
```cpp
/* 119064 */
struct RandomBreachingGoal
{
__int8 baseclass_0[68];
int mCooldown;
int mTimer;
int mAttempts;
};

```
#### RandomPos
```cpp
/* 123026 */
struct RandomPos
{
__int8 gap0[1];
};

```
#### RandomValueBounds
```cpp
/* 104696 */
struct RandomValueBounds
{
float mMin;
float mMax;
};

```
#### Range<int,-1>
```cpp
/* 31933 */
struct Range<int,-1>
{
const int mBeginIDX;
const int mEndIDX;
};

```
#### Range<int,-1>::iterator
```cpp
/* 31934 */
struct Range<int,-1>::iterator
{
int mIndex;
};

```
#### Range<int,1>
```cpp
/* 35195 */
struct Range<int,1>
{
const int mBeginIDX;
const int mEndIDX;
};

```
#### Range<int,1>::iterator
```cpp
/* 35196 */
struct Range<int,1>::iterator
{
int mIndex;
};

```
#### Range<short,1>
```cpp
/* 109116 */
struct Range<short,1>
{
const __int16 mBeginIDX;
const __int16 mEndIDX;
};

```
#### Range<short,1>::iterator
```cpp
/* 109117 */
struct Range<short,1>::iterator
{
__int16 mIndex;
};

```
#### Range<unsigned char,'_x01'>
```cpp
/* 185247 */
struct Range<unsigned char,'_x01'>
{
const unsigned __int8 mBeginIDX;
const unsigned __int8 mEndIDX;
};

```
#### Range<unsigned char,'_x01'>::iterator
```cpp
/* 185248 */
struct Range<unsigned char,'_x01'>::iterator
{
unsigned __int8 mIndex;
};

```
#### Range<unsigned int,1>
```cpp
/* 40599 */
struct Range<unsigned int,1>
{
const unsigned int mBeginIDX;
const unsigned int mEndIDX;
};

```
#### Range<unsigned int,1>::iterator
```cpp
/* 40600 */
struct Range<unsigned int,1>::iterator
{
unsigned int mIndex;
};

```
#### Range<unsigned long,1>
```cpp
/* 63715 */
struct Range<unsigned long,1>
{
const unsigned __int64 mBeginIDX;
const unsigned __int64 mEndIDX;
};

```
#### Range<unsigned long,1>::iterator
```cpp
/* 63716 */
struct Range<unsigned long,1>::iterator
{
unsigned __int64 mIndex;
};

```
#### Range<unsigned short,1>
```cpp
/* 103052 */
struct Range<unsigned short,1>
{
const unsigned __int16 mBeginIDX;
const unsigned __int16 mEndIDX;
};

```
#### Range<unsigned short,1>::iterator
```cpp
/* 103053 */
struct Range<unsigned short,1>::iterator
{
unsigned __int16 mIndex;
};

```
#### RateLimiter
```cpp
/* 484857 */
struct RateLimiter
{
const size_t mLimit;
const std::chrono::seconds mTimeIntervalSeconds;
std::vector<std::chrono::time_point<std::chrono::_V2::steady_clock,std::chrono::duration<long,std::ratio<1,1000000000> > >> mInstances;
};

```
#### ReadOnlyBinaryStream
```cpp
/* 33520 */
struct ReadOnlyBinaryStream
{
int (**_vptr$ReadOnlyBinaryStream)(void);
size_t mReadPointer;
const std::string mOwnedBuffer;
const std::string *mBuffer;
};

```
#### Recipe
```cpp
/* 75620 */
struct Recipe
{
int (**_vptr$Recipe)(void);
std::string mRecipeId;
ItemPack mMyItems;
mce::UUID mMyId;
int mWidth;
int mHeight;
int mPriority;
Recipe::Ingredients mMyIngredients;
Util::HashString mTag;
};

```
#### Recipes
```cpp
/* 77471 */
struct Recipes
{
ResourcePackManager *mResourcePackManager;
std::map<Util::HashString,std::map<std::string,std::unique_ptr<Recipe>>> mRecipes;
std::map<Recipes::FurnaceRecipeKey,ItemInstance> mFurnaceRecipes;
bool mInitializing;
std::map<ItemInstance,std::unordered_map<std::string,Recipe *>,SortItemInstanceIdAux,std::allocator<std::pair<const ItemInstance,std::unordered_map<std::string,Recipe *> > > > mRecipesByOutput;
RecipeListenerList mListeners;
};

```
#### Recipes::FurnaceRecipeKey
```cpp
/* 75806 */
struct Recipes::FurnaceRecipeKey
{
int mID;
Util::HashString mTag;
};

```
#### Recipes::addShapedRecipe::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 185249 */
struct Recipes::addShapedRecipe::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Recipes::addShapelessRecipe::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 185251 */
struct Recipes::addShapelessRecipe::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### RedstoneTorchCapacitor::State
```cpp
/* 464014 */
struct RedstoneTorchCapacitor::State
{
bool mOn;
bool mHalfFrame;
bool mChanged;
};

```
#### RegionFile
```cpp
/* 463321 */
struct RegionFile
{
int (**_vptr$RegionFile)(void);
Core::File mFile;
Core::HeapPathBuffer mFileName;
std::array<int,1024> mOffsets;
std::array<int,1024> mEmptyChunk;
RegionFile::FreeSectorMap mSectorFree;
};

```
#### RegisteredTagFilter
```cpp
/* 40659 */
struct RegisteredTagFilter
{
TagSetID mIncludeSet;
TagSetID mExcludeSet;
};

```
#### RenderParams
```cpp
/* 88682 */
struct RenderParams
{
BaseActorRenderContext *mBaseActorRenderContext;
MolangVariableMap *mVariables;
AnimationComponent *mAnimationComponent;
AnimationComponent *mRootAnimationComponent;
DataDrivenModel *mRootModel;
DataDrivenModel *mModel;
Actor *mActor;
BlockSource *mBlockSource;
ActorRenderData *mActorRenderData;
int32_t mVertexCount;
uint16_t mSubRenderLayerIndex;
std::function<float ()> mRandomFunction;
float mCameraDistance;
float mParams[8];
RenderParams::$3D9EB0E7A2790D70080124A37CC6ABC8 mFlags;
};

```
#### RenderParams::$3D9EB0E7A2790D70080124A37CC6ABC8::$7CDB70B13784CF5DCA20C1417F11D194
```cpp
/* 88690 */
struct RenderParams::$3D9EB0E7A2790D70080124A37CC6ABC8::$7CDB70B13784CF5DCA20C1417F11D194
{
unsigned __int32 mIsChild : 1;
};

```
#### ResourceInformation
```cpp
/* 5756 */
struct ResourceInformation
{
std::string mDescription;
SemVersion mVersion;
mce::UUID mUUID;
ResourceInformation::ResourceType mType;
std::string mEntry;
};

```
#### ResourceLoadManager
```cpp
/* 60803 */
struct ResourceLoadManager
{
Scheduler *mScheduler;
WorkerPool *mWorkerPool;
std::map<ResourceLoadType,std::unique_ptr<ResourceLoadManager::ResourceLoadTaskGroup>> mResourceLoadTaskGroups;
size_t mAppSuspended;
};

```
#### ResourceLoadManager::LoadOrder
```cpp
/* 60805 */
struct ResourceLoadManager::LoadOrder
{
__int8 gap0[1];
};

```
#### ResourceLoadManager::TaskGroupState
```cpp
/* 84459 */
struct ResourceLoadManager::TaskGroupState
{
bool mRunning;
size_t mPaused;
};

```
#### ResourceLoader
```cpp
/* 85234 */
struct ResourceLoader
{
int (**_vptr$ResourceLoader)(void);
std::function<Core::PathBuffer<std::string > ()> mGetPath;
};

```
#### ResourceLocation
```cpp
/* 2549 */
struct ResourceLocation
{
ResourceFileSystem mFileSystem;
Core::HeapPathBuffer mPath;
HashType64 mPathHash;
size_t mFullHash;
};

```
#### ResourceMetadata
```cpp
/* 5771 */
struct ResourceMetadata
{
std::vector<std::string> mAuthors;
std::string mUrl;
std::string mLicense;
};

```
#### ResourcePack
```cpp
/* 4191 */
struct ResourcePack
{
bool mHidden;
bool mError;
Pack *mPack;
std::unique_ptr<PackAccessStrategy> mSubpackAccessStrategy;
PackReport mPackReport;
std::vector<std::unique_ptr<Pack>> mSubPacks;
std::vector<std::unique_ptr<ResourcePack>> mSubResourcePacks;
Core::HeapPathBuffer mIconPath;
double mLoadTime;
bool mIsBaseGamePack;
bool mIsSlicePack;
ResourceSignature mResourceSignature;
};

```
#### ResourcePackContents
```cpp
/* 5710 */
struct ResourcePackContents
{
uint32_t mUIJson;
uint32_t mUITextures;
uint32_t mSound;
uint32_t mBlockJson;
uint32_t mBlockTextures;
uint32_t mItemTextures;
uint32_t mEntityTextures;
uint32_t mModelGeometry;
uint32_t mAnimations;
uint32_t mMaterials;
uint32_t mLanguages;
};

```
#### ResourcePackListener
```cpp
/* 81168 */
struct ResourcePackListener
{
int (**_vptr$ResourcePackListener)(void);
};

```
#### ResourcePackMergeStrategy
```cpp
/* 85264 */
struct ResourcePackMergeStrategy
{
int (**_vptr$ResourcePackMergeStrategy)(void);
};

```
#### ResourcePackRepository
```cpp
/* 5700 */
struct ResourcePackRepository
{
Core::FilePathManager *mFilePathManager;
std::vector<std::unique_ptr<ResourcePack>> mAllResourcePacks;
std::unique_ptr<CompositePackSource> mPackSource;
std::unique_ptr<CompositePackSource> mCachePackSource;
std::unique_ptr<CompositePackSource> mWorldPackSource;
std::unique_ptr<CompositePackSource> mPremiumWorldTemplatePackSource;
std::unique_ptr<PackSourceReport> mPackSourceReport;
ResourcePack *mVanillaPack;
ResourcePack *mChemistryPack;
ResourcePack *mChemistryServerPack;
std::vector<ResourceLocation> mInvalidPackLocation;
std::vector<ResourceLocation> mInvalidBehaviorPackLocation;
std::vector<ResourceLocation> mInvalidResourcePackLocation;
std::vector<ResourceLocation> mInvalidTemplatePackLocation;
IMinecraftEventing *mEventing;
PackManifestFactory *mManifestFactory;
IContentAccessibilityProvider *mContentAccessibility;
Core::HeapPathBuffer mCurrentWorldPath;
Core::HeapPathBuffer mCurrentPremiumWorldTemplatePath;
ContentKeyMap mTempCacheContentKeys;
const int mKnownPacksFileVerison;
std::unique_ptr<PackSettingsFactory> mPackSettingsFactory;
PackSourceFactory *mPackSourceFactory;
ResourcePackRepository::KnownPackContainer mCachedValidUserPacks;
ResourcePackRepository::KnownPackContainer mCachedInvalidUserPacks;
std::map<void *,std::function<void (ResourcePack *)>> mRemoveResourcePackCallback;
std::unique_ptr<TaskGroup> mInitTaskGroup;
Bedrock::Threading::Mutex mInitializeMutex;
std::atomic<bool> mInitialized;
std::atomic<bool> mReloadUserPacksRequested;
std::atomic<bool> mRefreshPacksRequested;
ContentIdentity mCurrentPremiumWorldTemplateIdentity;
};

```
#### ResourcePackRepository::KnownPackContainer
```cpp
/* 5706 */
struct ResourcePackRepository::KnownPackContainer
{
std::vector<ResourcePackRepository::KnownPackInfo> mPacks;
};

```
#### ResourcePackRepository::KnownPackInfo
```cpp
/* 4094 */
struct ResourcePackRepository::KnownPackInfo
{
bool mDiscoveredOnDisk;
ResourceLocation mResourceLocation;
std::vector<std::string> mPastHashes;
PackIdVersion mIdentity;
};

```
#### ResourcePackStack
```cpp
/* 2991 */
struct ResourcePackStack
{
int (**_vptr$ResourcePackStack)(void);
ResourcePackStack::PackInstanceStack mStack;
std::unique_ptr<PackSourceReport> mPackSourceReport;
};

```
#### ResourcePackTransmissionManager
```cpp
/* 62768 */
struct ResourcePackTransmissionManager
{
std::unordered_map<unsigned long,std::unordered_map<std::string,std::shared_ptr<ResourcePackFileDownloaderManager>>> mResourceDownloadManagers;
std::unordered_map<unsigned long,std::unordered_map<std::string,std::shared_ptr<ResourcePackFileUploadManager>>> mResourceUploadManagers;
std::unordered_set<unsigned long> mRemovedResourceDownloadManagers;
std::unordered_set<unsigned long> mRemovedResourceUploadManagers;
std::unique_ptr<TaskGroup> mIOTaskGroup;
};

```
#### ResourcePacksInfoData
```cpp
/* 45309 */
struct ResourcePacksInfoData
{
bool mTexturePackRequired;
bool mHasScripts;
bool mHasExceptions;
std::vector<ResourcePackInfoData> mAddOnPacks;
std::vector<ResourcePackInfoData> mTexturePacks;
};

```
#### ResourcePath
```cpp
/* 60575 */
struct ResourcePath
{
std::string mPackId;
std::string mPath;
};

```
#### ResourceSignature
```cpp
/* 4193 */
struct ResourceSignature
{
std::unordered_map<std::string,std::string> mSignatureFileContents;
};

```
#### ResourceUtil
```cpp
/* 484001 */
struct ResourceUtil
{
__int8 gap0[1];
};

```
#### RiverTransformation;
```cpp
/* 40587 */
struct RiverTransformation;

```
#### RoleChecker
```cpp
/* 421290 */
struct RoleChecker
{
std::weak_ptr<RoleCheckerCallback> mPendingCallback;
};

```
#### RoleCheckerCallback
```cpp
/* 421295 */
struct RoleCheckerCallback
{
RoleChecker::OnRoleAcquired mCallback;
};

```
#### RopePoint
```cpp
/* 88873 */
struct RopePoint
{
Vec3 mOldPos;
Vec3 mToNewPos;
};

```
#### RopePointsRef
```cpp
/* 109073 */
struct RopePointsRef
{
const RopePoints *mPoints;
Bedrock::Threading::Mutex *mPointMutex;
};

```
#### RopeSystem
```cpp
/* 88859 */
struct RopeSystem
{
bool mWaveApplied;
RopePoints mQueuedRenderPoints;
RopePoints mRenderPoints;
std::vector<RopeNode> mNodes;
std::vector<AABBBucket> mColliderBuckets;
std::vector<RopeWave> mWaves;
RopeParams mParams;
std::set<AABB,AABBPred,std::allocator<AABB> > mBlacklistedColliders;
Vec3 mPrevStartPin;
Vec3 mPrevEndPin;
size_t mCutNode;
size_t mCutRenderNode;
size_t mMinNodes;
size_t mCutTicks;
ActorUniqueID mEndPinEntity;
std::atomic_flag mTicking;
Bedrock::Threading::Mutex mRenderMutex;
bool mAbandonCollision;
Vec3 mStartPin;
Vec3 mEndPin;
size_t mToCutNode;
};

```
#### RopeWave
```cpp
/* 88925 */
struct RopeWave
{
Vec3 mForce;
float mSpeed;
float mDamping;
size_t mCurNode;
float mDistAlongNode;
RopeWave::Direction mDir;
};

```
#### RuntimeLightingManager
```cpp
/* 34696 */
struct RuntimeLightingManager
{
std::unordered_map<ChunkPos,RuntimeLightingManager::RuntimeLightingSubchunkList> mLevelChunksToLight;
std::vector<RuntimeLightingManager::RelightingChunkElement> mListOfChunksToProcess;
std::vector<BlockPos> mProcessedSubchunks;
std::vector<BlockPos> mBrightnessChangedList;
Dimension *mDimension;
bool mWorkerScheduled;
float mLightingTimeboxTime;
};

```
#### RuntimeLightingManager::RelightingChunkElement
```cpp
/* 34731 */
struct RuntimeLightingManager::RelightingChunkElement
{
float mDist;
ChunkPos mChunkPos;
size_t mSubChunkIndex;
std::vector<SubChunkLightUpdate> *mAlteredBlockList;
};

```
#### RuntimeLightingManager::RuntimeLightingSubchunkList
```cpp
/* 253798 */
struct RuntimeLightingManager::RuntimeLightingSubchunkList
{
std::array<std::vector<SubChunkLightUpdate>,16> mAlteredSubchunkBlockList;
};

```
