#### DBStorage::DBStorageToken
```cpp
/* 462651 */
struct DBStorage::DBStorageToken
{
std::atomic<int> *mRefCounter;
};

```
#### DBStorage::PendingWrite
```cpp
/* 462401 */
struct DBStorage::PendingWrite
{
int mNumPending;
std::shared_ptr<std::string > mValue;
};

```
#### DBStorageEnvironmentChain
```cpp
/* 462033 */
struct DBStorageEnvironmentChain
{
std::unique_ptr<EncryptedProxyEnv> mEncryptedEnv;
std::unique_ptr<FlushableEnv> mFlushableEnv;
std::unique_ptr<FlushableEnv> mPreSnapshotBufferEnv;
std::unique_ptr<SnapshotEnv> mSnapshotEnv;
std::unique_ptr<CompactionListenerEnv> mCompactionListenerEnv;
leveldb::Env *mWrappedEnv;
Core::HeapPathBuffer mDbPath;
};

```
#### DBStorageWriteBatch::PerfContext
```cpp
/* 462967 */
struct DBStorageWriteBatch::PerfContext
{
uint64_t mOperation;
uint64_t mSize;
const std::string mKey;
const char *mReason;
};

```
#### DamageOverTimeComponent
```cpp
/* 52310 */
struct DamageOverTimeComponent
{
int mHurtValue;
int mDamageTimeInterval;
int mDamageTime;
};

```
#### DamageOverTimeDefinition
```cpp
/* 107749 */
struct DamageOverTimeDefinition
{
int mDamagePerHurt;
float mTimeBetweenHurt;
};

```
#### DamageSensorDefinition
```cpp
/* 100654 */
struct DamageSensorDefinition
{
std::vector<DamageSensorTrigger> mTriggers;
};

```
#### DamageSensorTrigger
```cpp
/* 100573 */
struct DamageSensorTrigger
{
DefinitionTrigger mOnDamage;
bool mDealsDamage;
ActorDamageCause mCause;
float mDamageMultipler;
std::string mOnDamageSound;
};

```
#### DanceComponent
```cpp
/* 52461 */
struct DanceComponent
{
Unique<DanceComponentListener> mListener;
};

```
#### DataDrivenBiomeSurface;
```cpp
/* 198710 */
struct DataDrivenBiomeSurface;

```
#### DataDrivenGeometry;
```cpp
/* 109085 */
struct DataDrivenGeometry;

```
#### DataDrivenModel;
```cpp
/* 88684 */
struct DataDrivenModel;

```
#### DataLoadHelper
```cpp
/* 13231 */
struct DataLoadHelper
{
int (**_vptr$DataLoadHelper)(void);
};

```
#### DataStructures::CircularLinkedList<HuffmanEncodingTreeNode *>
```cpp
/* 478142 */
struct DataStructures::CircularLinkedList<HuffmanEncodingTreeNode *>
{
unsigned int list_size;
DataStructures::CircularLinkedList<HuffmanEncodingTreeNode *>::node *root;
DataStructures::CircularLinkedList<HuffmanEncodingTreeNode *>::node *position;
};

```
#### DataStructures::CircularLinkedList<HuffmanEncodingTreeNode *>::node
```cpp
/* 478143 */
struct DataStructures::CircularLinkedList<HuffmanEncodingTreeNode *>::node
{
HuffmanEncodingTreeNode *item;
DataStructures::CircularLinkedList<HuffmanEncodingTreeNode *>::node *previous;
DataStructures::CircularLinkedList<HuffmanEncodingTreeNode *>::node *next;
};

```
#### DataStructures::Heap<unsigned long,RakNet::InternalPacket *,false>::HeapNode
```cpp
/* 478009 */
struct DataStructures::Heap<unsigned long,RakNet::InternalPacket *,false>::HeapNode
{
unsigned __int64 weight;
RakNet::InternalPacket *data;
};

```
#### DataStructures::List<DataStructures::Heap<unsigned long,RakNet::InternalPacket *,false>::HeapNode>
```cpp
/* 478008 */
struct DataStructures::List<DataStructures::Heap<unsigned long,RakNet::InternalPacket *,false>::HeapNode>
{
DataStructures::Heap<unsigned long,RakNet::InternalPacket *,false>::HeapNode *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::MapNode>
```cpp
/* 478109 */
struct DataStructures::List<DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::MapNode>
{
DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::MapNode *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<DataStructures::RangeNode<RakNet::uint24_t> >
```cpp
/* 478022 */
struct DataStructures::List<DataStructures::RangeNode<RakNet::uint24_t> >
{
DataStructures::RangeNode<RakNet::uint24_t> *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::InternalPacket *>
```cpp
/* 478017 */
struct DataStructures::List<RakNet::InternalPacket *>
{
RakNet::InternalPacket **listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::PluginInterface2 *>
```cpp
/* 478038 */
struct DataStructures::List<RakNet::PluginInterface2 *>
{
RakNet::PluginInterface2 **listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::RakNetGUID>
```cpp
/* 478083 */
struct DataStructures::List<RakNet::RakNetGUID>
{
RakNet::RakNetGUID *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::RakNetSocket2 *>
```cpp
/* 478059 */
struct DataStructures::List<RakNet::RakNetSocket2 *>
{
RakNet::RakNetSocket2 **listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::RakNetStatistics>
```cpp
/* 478084 */
struct DataStructures::List<RakNet::RakNetStatistics>
{
RakNet::RakNetStatistics *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::RakPeer::BanStruct *>
```cpp
/* 478036 */
struct DataStructures::List<RakNet::RakPeer::BanStruct *>
{
RakNet::RakPeer::BanStruct **listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::RakString::SharedString *>
```cpp
/* 73591 */
struct DataStructures::List<RakNet::RakString::SharedString *>
{
RakNet::RakString::SharedString **listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::RakString>
```cpp
/* 478061 */
struct DataStructures::List<RakNet::RakString>
{
RakNet::RakString *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::ReliabilityLayer::UnreliableWithAckReceiptNode>
```cpp
/* 478002 */
struct DataStructures::List<RakNet::ReliabilityLayer::UnreliableWithAckReceiptNode>
{
RakNet::ReliabilityLayer::UnreliableWithAckReceiptNode *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::SplitPacketChannel *>
```cpp
/* 478012 */
struct DataStructures::List<RakNet::SplitPacketChannel *>
{
RakNet::SplitPacketChannel **listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::SystemAddress>
```cpp
/* 478082 */
struct DataStructures::List<RakNet::SystemAddress>
{
RakNet::SystemAddress *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<StrAndBool>
```cpp
/* 478117 */
struct DataStructures::List<StrAndBool>
{
StrAndBool *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<bool>
```cpp
/* 478018 */
struct DataStructures::List<bool>
{
bool *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<int>
```cpp
/* 478137 */
struct DataStructures::List<int>
{
int *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<unsigned int>
```cpp
/* 478019 */
struct DataStructures::List<unsigned int>
{
unsigned int *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::MapNode
```cpp
/* 478110 */
struct DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::MapNode
{
int mapNodeKey;
RakNet::HuffmanEncodingTree *mapNodeData;
};

```
#### DataStructures::MemoryPool<RakNet::InternalPacket>::MemoryWithPage
```cpp
/* 478093 */
struct DataStructures::MemoryPool<RakNet::InternalPacket>::MemoryWithPage
{
RakNet::InternalPacket userMemory;
DataStructures::MemoryPool<RakNet::InternalPacket>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::InternalPacket>::Page
```cpp
/* 478006 */
struct DataStructures::MemoryPool<RakNet::InternalPacket>::Page
{
DataStructures::MemoryPool<RakNet::InternalPacket>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::InternalPacket>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::InternalPacket>::Page *next;
DataStructures::MemoryPool<RakNet::InternalPacket>::Page *prev;
};

```
#### DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::MemoryWithPage
```cpp
/* 478095 */
struct DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::MemoryWithPage
{
RakNet::InternalPacketRefCountedData userMemory;
DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::Page
```cpp
/* 478025 */
struct DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::Page
{
DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::Page *next;
DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::Page *prev;
};

```
#### DataStructures::MemoryPool<RakNet::Packet>::MemoryWithPage
```cpp
/* 478067 */
struct DataStructures::MemoryPool<RakNet::Packet>::MemoryWithPage
{
RakNet::Packet userMemory;
DataStructures::MemoryPool<RakNet::Packet>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::Packet>::Page
```cpp
/* 478066 */
struct DataStructures::MemoryPool<RakNet::Packet>::Page
{
DataStructures::MemoryPool<RakNet::Packet>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::Packet>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::Packet>::Page *next;
DataStructures::MemoryPool<RakNet::Packet>::Page *prev;
};

```
#### DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::MemoryWithPage
```cpp
/* 478047 */
struct DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::MemoryWithPage
{
RakNet::RakPeer::BufferedCommandStruct userMemory;
DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::Page
```cpp
/* 478046 */
struct DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::Page
{
DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::Page *next;
DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::Page *prev;
};

```
#### DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::MemoryWithPage
```cpp
/* 478057 */
struct DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::MemoryWithPage
{
RakNet::RakPeer::SocketQueryOutput userMemory;
DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::Page
```cpp
/* 478056 */
struct DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::Page
{
DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::Page *next;
DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::Page *prev;
};

```
#### DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::MemoryWithPage
```cpp
/* 478092 */
struct DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::MemoryWithPage
{
RakNet::ReliabilityLayer::MessageNumberNode userMemory;
DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::Page
```cpp
/* 478001 */
struct DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::Page
{
DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::Page *next;
DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::Page *prev;
};

```
#### DataStructures::MemoryPool<RakNet::RemoteClient *>::MemoryWithPage
```cpp
/* 478134 */
struct DataStructures::MemoryPool<RakNet::RemoteClient *>::MemoryWithPage
{
RakNet::RemoteClient *userMemory;
DataStructures::MemoryPool<RakNet::RemoteClient *>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::RemoteClient *>::Page
```cpp
/* 478133 */
struct DataStructures::MemoryPool<RakNet::RemoteClient *>::Page
{
DataStructures::MemoryPool<RakNet::RemoteClient *>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::RemoteClient *>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::RemoteClient *>::Page *next;
DataStructures::MemoryPool<RakNet::RemoteClient *>::Page *prev;
};

```
#### DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::MemoryWithPage
```cpp
/* 478035 */
struct DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::MemoryWithPage
{
RakNet::RemoteSystemIndex userMemory;
DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::Page
```cpp
/* 478034 */
struct DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::Page
{
DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::Page *next;
DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::Page *prev;
};

```
#### DataStructures::MemoryPool<RakNet::SystemAddress>::MemoryWithPage
```cpp
/* 478129 */
struct DataStructures::MemoryPool<RakNet::SystemAddress>::MemoryWithPage
{
RakNet::SystemAddress userMemory;
DataStructures::MemoryPool<RakNet::SystemAddress>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::SystemAddress>::Page
```cpp
/* 478128 */
struct DataStructures::MemoryPool<RakNet::SystemAddress>::Page
{
DataStructures::MemoryPool<RakNet::SystemAddress>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::SystemAddress>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::SystemAddress>::Page *next;
DataStructures::MemoryPool<RakNet::SystemAddress>::Page *prev;
};

```
#### DataStructures::OrderedList<RakNet::uint24_t,DataStructures::RangeNode<RakNet::uint24_t>,&DataStructures::RangeNodeComp>
```cpp
/* 478021 */
struct DataStructures::OrderedList<RakNet::uint24_t,DataStructures::RangeNode<RakNet::uint24_t>,&DataStructures::RangeNodeComp>
{
DataStructures::List<DataStructures::RangeNode<RakNet::uint24_t> > orderedList;
};

```
#### DataStructures::OrderedList<char *,StrAndBool,&RakNet::StrAndBoolComp>
```cpp
/* 478116 */
struct DataStructures::OrderedList<char *,StrAndBool,&RakNet::StrAndBoolComp>
{
DataStructures::List<StrAndBool> orderedList;
};

```
#### DataStructures::OrderedList<int,DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::MapNode,&DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::NodeComparisonFunc>
```cpp
/* 478108 */
struct DataStructures::OrderedList<int,DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::MapNode,&DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::NodeComparisonFunc>
{
DataStructures::List<DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::MapNode> orderedList;
};

```
#### DataStructures::OrderedList<unsigned short,RakNet::SplitPacketChannel *,&RakNet::SplitPacketChannelComp>
```cpp
/* 478011 */
struct DataStructures::OrderedList<unsigned short,RakNet::SplitPacketChannel *,&RakNet::SplitPacketChannelComp>
{
DataStructures::List<RakNet::SplitPacketChannel *> orderedList;
};

```
#### DataStructures::RangeList<RakNet::uint24_t>
```cpp
/* 478020 */
struct DataStructures::RangeList<RakNet::uint24_t>
{
DataStructures::OrderedList<RakNet::uint24_t,DataStructures::RangeNode<RakNet::uint24_t>,&DataStructures::RangeNodeComp> ranges;
};

```
#### DataStructures::RangeNode<RakNet::uint24_t>
```cpp
/* 478023 */
struct DataStructures::RangeNode<RakNet::uint24_t>
{
RakNet::uint24_t minIndex;
RakNet::uint24_t maxIndex;
};

```
#### DataStructures::ThreadsafeAllocatingQueue<RakNet::Packet>
```cpp
/* 478125 */
struct DataStructures::ThreadsafeAllocatingQueue<RakNet::Packet>
{
DataStructures::MemoryPool<RakNet::Packet> memoryPool;
RakNet::SimpleMutex memoryPoolMutex;
DataStructures::Queue<RakNet::Packet *> queue;
RakNet::SimpleMutex queueMutex;
};

```
#### DataStructures::ThreadsafeAllocatingQueue<RakNet::RakPeer::BufferedCommandStruct>
```cpp
/* 478044 */
struct DataStructures::ThreadsafeAllocatingQueue<RakNet::RakPeer::BufferedCommandStruct>
{
DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct> memoryPool;
RakNet::SimpleMutex memoryPoolMutex;
DataStructures::Queue<RakNet::RakPeer::BufferedCommandStruct *> queue;
RakNet::SimpleMutex queueMutex;
};

```
#### DataStructures::ThreadsafeAllocatingQueue<RakNet::RakPeer::SocketQueryOutput>
```cpp
/* 478054 */
struct DataStructures::ThreadsafeAllocatingQueue<RakNet::RakPeer::SocketQueryOutput>
{
DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput> memoryPool;
RakNet::SimpleMutex memoryPoolMutex;
DataStructures::Queue<RakNet::RakPeer::SocketQueryOutput *> queue;
RakNet::SimpleMutex queueMutex;
};

```
#### DataStructures::ThreadsafeAllocatingQueue<RakNet::RemoteClient *>
```cpp
/* 478131 */
struct DataStructures::ThreadsafeAllocatingQueue<RakNet::RemoteClient *>
{
DataStructures::MemoryPool<RakNet::RemoteClient *> memoryPool;
RakNet::SimpleMutex memoryPoolMutex;
DataStructures::Queue<RakNet::RemoteClient **> queue;
RakNet::SimpleMutex queueMutex;
};

```
#### DataStructures::ThreadsafeAllocatingQueue<RakNet::SystemAddress>
```cpp
/* 478126 */
struct DataStructures::ThreadsafeAllocatingQueue<RakNet::SystemAddress>
{
DataStructures::MemoryPool<RakNet::SystemAddress> memoryPool;
RakNet::SimpleMutex memoryPoolMutex;
DataStructures::Queue<RakNet::SystemAddress *> queue;
RakNet::SimpleMutex queueMutex;
};

```
#### DataTypeMap::copyFor<BlockPos>
```cpp
/* 109124 */
struct DataTypeMap::copyFor<BlockPos>
{
__int8 gap0[1];
};

```
#### DataTypeMap::copyFor<CompoundTag>
```cpp
/* 116860 */
struct DataTypeMap::copyFor<CompoundTag>
{
__int8 gap0[1];
};

```
#### DataTypeMap::copyFor<Vec3>
```cpp
/* 109121 */
struct DataTypeMap::copyFor<Vec3>
{
__int8 gap0[1];
};

```
#### DataTypeMap::copyFor<float>
```cpp
/* 58762 */
struct DataTypeMap::copyFor<float>
{
__int8 gap0[1];
};

```
#### DataTypeMap::copyFor<int>
```cpp
/* 48723 */
struct DataTypeMap::copyFor<int>
{
__int8 gap0[1];
};

```
#### DataTypeMap::copyFor<long>
```cpp
/* 48720 */
struct DataTypeMap::copyFor<long>
{
__int8 gap0[1];
};

```
#### DataTypeMap::copyFor<short>
```cpp
/* 51817 */
struct DataTypeMap::copyFor<short>
{
__int8 gap0[1];
};

```
#### DataTypeMap::copyFor<signed char>
```cpp
/* 49188 */
struct DataTypeMap::copyFor<signed char>
{
__int8 gap0[1];
};

```
#### DataTypeMap::neqFor<BlockPos>
```cpp
/* 109123 */
struct DataTypeMap::neqFor<BlockPos>
{
__int8 gap0[1];
};

```
#### DataTypeMap::neqFor<CompoundTag>
```cpp
/* 116859 */
struct DataTypeMap::neqFor<CompoundTag>
{
__int8 gap0[1];
};

```
#### DataTypeMap::neqFor<Vec3>
```cpp
/* 109126 */
struct DataTypeMap::neqFor<Vec3>
{
__int8 gap0[1];
};

```
#### DataTypeMap::neqFor<float>
```cpp
/* 58761 */
struct DataTypeMap::neqFor<float>
{
__int8 gap0[1];
};

```
#### DataTypeMap::neqFor<int>
```cpp
/* 48722 */
struct DataTypeMap::neqFor<int>
{
__int8 gap0[1];
};

```
#### DataTypeMap::neqFor<long>
```cpp
/* 109125 */
struct DataTypeMap::neqFor<long>
{
__int8 gap0[1];
};

```
#### DataTypeMap::neqFor<short>
```cpp
/* 51816 */
struct DataTypeMap::neqFor<short>
{
__int8 gap0[1];
};

```
#### DataTypeMap::neqFor<signed char>
```cpp
/* 49187 */
struct DataTypeMap::neqFor<signed char>
{
__int8 gap0[1];
};

```
#### DataTypeMap::typeFor<BlockPos>
```cpp
/* 109122 */
struct DataTypeMap::typeFor<BlockPos>
{
__int8 gap0[1];
};

```
#### DataTypeMap::typeFor<CompoundTag>
```cpp
/* 116858 */
struct DataTypeMap::typeFor<CompoundTag>
{
__int8 gap0[1];
};

```
#### DataTypeMap::typeFor<Vec3>
```cpp
/* 108405 */
struct DataTypeMap::typeFor<Vec3>
{
__int8 gap0[1];
};

```
#### DataTypeMap::typeFor<float>
```cpp
/* 58760 */
struct DataTypeMap::typeFor<float>
{
__int8 gap0[1];
};

```
#### DataTypeMap::typeFor<int>
```cpp
/* 48721 */
struct DataTypeMap::typeFor<int>
{
__int8 gap0[1];
};

```
#### DataTypeMap::typeFor<long>
```cpp
/* 48371 */
struct DataTypeMap::typeFor<long>
{
__int8 gap0[1];
};

```
#### DataTypeMap::typeFor<short>
```cpp
/* 51815 */
struct DataTypeMap::typeFor<short>
{
__int8 gap0[1];
};

```
#### DataTypeMap::typeFor<signed char>
```cpp
/* 49186 */
struct DataTypeMap::typeFor<signed char>
{
__int8 gap0[1];
};

```
#### DateManager
```cpp
/* 82680 */
struct DateManager
{
unsigned int mTimeScale;
time_t mRealTime;
time_t mTime;
Bedrock::Threading::Mutex mScheduledCallbacksMutex;
std::priority_queue<ScheduledCallback,std::vector<ScheduledCallback>,CompareScheduledCallback> mScheduledCallbacks;
};

```
#### DebugAssertException
```cpp
/* 485138 */
struct DebugAssertException
{
__int8 baseclass_0[8];
std::unique_ptr<char []> mDescription;
std::unique_ptr<char []> mArgument;
std::unique_ptr<char []> mInfo;
int mLine;
std::unique_ptr<char []> mFile;
std::unique_ptr<char []> mFunction;
};

```
#### DebugEndPoint;
```cpp
/* 4236 */
struct DebugEndPoint;

```
#### DebugLogScope
```cpp
/* 31299 */
struct DebugLogScope
{
bool mPopScope;
};

```
#### DebugRenderer
```cpp
/* 122535 */
struct DebugRenderer
{
__int8 gap0[1];
};

```
#### DedicatedServerCommands
```cpp
/* 5841 */
struct DedicatedServerCommands
{
__int8 gap0[1];
};

```
#### DefinitionEvent
```cpp
/* 46260 */
struct DefinitionEvent
{
float mProbability;
ActorFilterGroup mFilter;
std::string mName;
DefinitionEventType mType;
std::vector<std::string> mGroups;
std::vector<std::string> mRemoveGroups;
std::vector<DefinitionEvent> mChildren;
};

```
#### DefinitionEventLoader
```cpp
/* 428885 */
struct DefinitionEventLoader
{
__int8 gap0[1];
};

```
#### DefinitionEventLoader::loadEvent::$308FE320F1A5CE0A1A20921AD32B0459
```cpp
/* 428886 */
struct DefinitionEventLoader::loadEvent::$308FE320F1A5CE0A1A20921AD32B0459
{
DefinitionEvent *defEvent;
};

```
#### DefinitionInstanceGroup
```cpp
/* 13227 */
struct DefinitionInstanceGroup
{
std::vector<std::shared_ptr<IDefinitionInstance>> mDefinitionList;
std::unordered_map<std::string,std::shared_ptr<IDefinitionInstance>> mDefinitionMap;
std::unordered_map<unsigned short,std::string> mTypeIdToDefinitionName;
};

```
#### DefinitionModifier
```cpp
/* 109815 */
struct DefinitionModifier
{
std::vector<std::string> mAddGroups;
std::vector<std::string> mRemoveGroups;
};

```
#### DefinitionTrigger
```cpp
/* 47400 */
struct DefinitionTrigger
{
std::string mType;
std::string mTarget;
ActorFilterGroup mFilter;
};

```
#### DelayedDeleter<SubChunkBlockStorage>
```cpp
/* 253102 */
struct DelayedDeleter<SubChunkBlockStorage>
{
DelayedDeleter<SubChunkBlockStorage>::EntryQueue mEntries;
Bedrock::Threading::Mutex mEntriesMutex;
};

```
#### DelayedDeleter<SubChunkBrightnessStorage>
```cpp
/* 253128 */
struct DelayedDeleter<SubChunkBrightnessStorage>
{
DelayedDeleter<SubChunkBrightnessStorage>::EntryQueue mEntries;
Bedrock::Threading::Mutex mEntriesMutex;
};

```
#### DenySameParentsVariantData
```cpp
/* 319706 */
struct DenySameParentsVariantData
{
float mChance;
int mVariantRangeMin;
int mVariantRangeMax;
};

```
#### Description
```cpp
/* 47677 */
struct Description
{
int (**_vptr$Description)(void);
};

```
#### DimensionConversionData
```cpp
/* 190220 */
struct DimensionConversionData
{
Vec3 mOverworldSpawnPoint;
int mNetherScale;
};

```
#### Direction
```cpp
/* 31926 */
struct Direction
{
__int8 gap0[1];
};

```
#### DirtyTicksCounter
```cpp
/* 35002 */
struct DirtyTicksCounter
{
int totalTime;
int lastChange;
};

```
#### DistanceConstraint
```cpp
/* 50282 */
struct DistanceConstraint
{
float mConstraintMass;
Vec3 mConstraintAxis;
float mBias;
bool mShouldEnforce;
float mMassA;
float mMassB;
float mDesiredDistance;
};

```
#### DrinkPotionData
```cpp
/* 88852 */
struct DrinkPotionData
{
int mPotionId;
float mChance;
ActorFilterGroup mFilter;
};

```
#### DwellerComponent
```cpp
/* 53494 */
struct DwellerComponent
{
bool mCanFindPOI;
bool mCanMigrate;
bool mHasJoinedDwelling;
bool mFixUpRole;
bool mRewardPlayersOnFirstFounding;
HashedString mPreferredProfession;
int mFirstFoundingReward;
int mUpdateIntervalVariant;
size_t mDwellingUpdateInterval;
size_t mUpdateIntervalBase;
float mDwellingBoundsTolerance;
DwellerComponent::DwellingType mType;
DwellerRole mRole;
mce::UUID mDwellingUniqueID;
};

```
#### DBStorage::DBStorageToken
```cpp
/* 462651 */
struct DBStorage::DBStorageToken
{
std::atomic<int> *mRefCounter;
};

```
#### DBStorage::PendingWrite
```cpp
/* 462401 */
struct DBStorage::PendingWrite
{
int mNumPending;
std::shared_ptr<std::string > mValue;
};

```
#### DBStorageEnvironmentChain
```cpp
/* 462033 */
struct DBStorageEnvironmentChain
{
std::unique_ptr<EncryptedProxyEnv> mEncryptedEnv;
std::unique_ptr<FlushableEnv> mFlushableEnv;
std::unique_ptr<FlushableEnv> mPreSnapshotBufferEnv;
std::unique_ptr<SnapshotEnv> mSnapshotEnv;
std::unique_ptr<CompactionListenerEnv> mCompactionListenerEnv;
leveldb::Env *mWrappedEnv;
Core::HeapPathBuffer mDbPath;
};

```
#### DBStorageWriteBatch::PerfContext
```cpp
/* 462967 */
struct DBStorageWriteBatch::PerfContext
{
uint64_t mOperation;
uint64_t mSize;
const std::string mKey;
const char *mReason;
};

```
#### DamageOverTimeComponent
```cpp
/* 52310 */
struct DamageOverTimeComponent
{
int mHurtValue;
int mDamageTimeInterval;
int mDamageTime;
};

```
#### DamageOverTimeDefinition
```cpp
/* 107749 */
struct DamageOverTimeDefinition
{
int mDamagePerHurt;
float mTimeBetweenHurt;
};

```
#### DamageSensorDefinition
```cpp
/* 100654 */
struct DamageSensorDefinition
{
std::vector<DamageSensorTrigger> mTriggers;
};

```
#### DamageSensorTrigger
```cpp
/* 100573 */
struct DamageSensorTrigger
{
DefinitionTrigger mOnDamage;
bool mDealsDamage;
ActorDamageCause mCause;
float mDamageMultipler;
std::string mOnDamageSound;
};

```
#### DanceComponent
```cpp
/* 52461 */
struct DanceComponent
{
Unique<DanceComponentListener> mListener;
};

```
#### DataDrivenBiomeSurface;
```cpp
/* 198710 */
struct DataDrivenBiomeSurface;

```
#### DataDrivenGeometry;
```cpp
/* 109085 */
struct DataDrivenGeometry;

```
#### DataDrivenModel;
```cpp
/* 88684 */
struct DataDrivenModel;

```
#### DataLoadHelper
```cpp
/* 13231 */
struct DataLoadHelper
{
int (**_vptr$DataLoadHelper)(void);
};

```
#### DataStructures::CircularLinkedList<HuffmanEncodingTreeNode *>
```cpp
/* 478142 */
struct DataStructures::CircularLinkedList<HuffmanEncodingTreeNode *>
{
unsigned int list_size;
DataStructures::CircularLinkedList<HuffmanEncodingTreeNode *>::node *root;
DataStructures::CircularLinkedList<HuffmanEncodingTreeNode *>::node *position;
};

```
#### DataStructures::CircularLinkedList<HuffmanEncodingTreeNode *>::node
```cpp
/* 478143 */
struct DataStructures::CircularLinkedList<HuffmanEncodingTreeNode *>::node
{
HuffmanEncodingTreeNode *item;
DataStructures::CircularLinkedList<HuffmanEncodingTreeNode *>::node *previous;
DataStructures::CircularLinkedList<HuffmanEncodingTreeNode *>::node *next;
};

```
#### DataStructures::Heap<unsigned long,RakNet::InternalPacket *,false>::HeapNode
```cpp
/* 478009 */
struct DataStructures::Heap<unsigned long,RakNet::InternalPacket *,false>::HeapNode
{
unsigned __int64 weight;
RakNet::InternalPacket *data;
};

```
#### DataStructures::List<DataStructures::Heap<unsigned long,RakNet::InternalPacket *,false>::HeapNode>
```cpp
/* 478008 */
struct DataStructures::List<DataStructures::Heap<unsigned long,RakNet::InternalPacket *,false>::HeapNode>
{
DataStructures::Heap<unsigned long,RakNet::InternalPacket *,false>::HeapNode *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::MapNode>
```cpp
/* 478109 */
struct DataStructures::List<DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::MapNode>
{
DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::MapNode *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<DataStructures::RangeNode<RakNet::uint24_t> >
```cpp
/* 478022 */
struct DataStructures::List<DataStructures::RangeNode<RakNet::uint24_t> >
{
DataStructures::RangeNode<RakNet::uint24_t> *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::InternalPacket *>
```cpp
/* 478017 */
struct DataStructures::List<RakNet::InternalPacket *>
{
RakNet::InternalPacket **listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::PluginInterface2 *>
```cpp
/* 478038 */
struct DataStructures::List<RakNet::PluginInterface2 *>
{
RakNet::PluginInterface2 **listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::RakNetGUID>
```cpp
/* 478083 */
struct DataStructures::List<RakNet::RakNetGUID>
{
RakNet::RakNetGUID *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::RakNetSocket2 *>
```cpp
/* 478059 */
struct DataStructures::List<RakNet::RakNetSocket2 *>
{
RakNet::RakNetSocket2 **listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::RakNetStatistics>
```cpp
/* 478084 */
struct DataStructures::List<RakNet::RakNetStatistics>
{
RakNet::RakNetStatistics *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::RakPeer::BanStruct *>
```cpp
/* 478036 */
struct DataStructures::List<RakNet::RakPeer::BanStruct *>
{
RakNet::RakPeer::BanStruct **listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::RakString::SharedString *>
```cpp
/* 73591 */
struct DataStructures::List<RakNet::RakString::SharedString *>
{
RakNet::RakString::SharedString **listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::RakString>
```cpp
/* 478061 */
struct DataStructures::List<RakNet::RakString>
{
RakNet::RakString *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::ReliabilityLayer::UnreliableWithAckReceiptNode>
```cpp
/* 478002 */
struct DataStructures::List<RakNet::ReliabilityLayer::UnreliableWithAckReceiptNode>
{
RakNet::ReliabilityLayer::UnreliableWithAckReceiptNode *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::SplitPacketChannel *>
```cpp
/* 478012 */
struct DataStructures::List<RakNet::SplitPacketChannel *>
{
RakNet::SplitPacketChannel **listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<RakNet::SystemAddress>
```cpp
/* 478082 */
struct DataStructures::List<RakNet::SystemAddress>
{
RakNet::SystemAddress *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<StrAndBool>
```cpp
/* 478117 */
struct DataStructures::List<StrAndBool>
{
StrAndBool *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<bool>
```cpp
/* 478018 */
struct DataStructures::List<bool>
{
bool *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<int>
```cpp
/* 478137 */
struct DataStructures::List<int>
{
int *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::List<unsigned int>
```cpp
/* 478019 */
struct DataStructures::List<unsigned int>
{
unsigned int *listArray;
unsigned int list_size;
unsigned int allocation_size;
};

```
#### DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::MapNode
```cpp
/* 478110 */
struct DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::MapNode
{
int mapNodeKey;
RakNet::HuffmanEncodingTree *mapNodeData;
};

```
#### DataStructures::MemoryPool<RakNet::InternalPacket>::MemoryWithPage
```cpp
/* 478093 */
struct DataStructures::MemoryPool<RakNet::InternalPacket>::MemoryWithPage
{
RakNet::InternalPacket userMemory;
DataStructures::MemoryPool<RakNet::InternalPacket>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::InternalPacket>::Page
```cpp
/* 478006 */
struct DataStructures::MemoryPool<RakNet::InternalPacket>::Page
{
DataStructures::MemoryPool<RakNet::InternalPacket>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::InternalPacket>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::InternalPacket>::Page *next;
DataStructures::MemoryPool<RakNet::InternalPacket>::Page *prev;
};

```
#### DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::MemoryWithPage
```cpp
/* 478095 */
struct DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::MemoryWithPage
{
RakNet::InternalPacketRefCountedData userMemory;
DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::Page
```cpp
/* 478025 */
struct DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::Page
{
DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::Page *next;
DataStructures::MemoryPool<RakNet::InternalPacketRefCountedData>::Page *prev;
};

```
#### DataStructures::MemoryPool<RakNet::Packet>::MemoryWithPage
```cpp
/* 478067 */
struct DataStructures::MemoryPool<RakNet::Packet>::MemoryWithPage
{
RakNet::Packet userMemory;
DataStructures::MemoryPool<RakNet::Packet>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::Packet>::Page
```cpp
/* 478066 */
struct DataStructures::MemoryPool<RakNet::Packet>::Page
{
DataStructures::MemoryPool<RakNet::Packet>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::Packet>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::Packet>::Page *next;
DataStructures::MemoryPool<RakNet::Packet>::Page *prev;
};

```
#### DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::MemoryWithPage
```cpp
/* 478047 */
struct DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::MemoryWithPage
{
RakNet::RakPeer::BufferedCommandStruct userMemory;
DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::Page
```cpp
/* 478046 */
struct DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::Page
{
DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::Page *next;
DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct>::Page *prev;
};

```
#### DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::MemoryWithPage
```cpp
/* 478057 */
struct DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::MemoryWithPage
{
RakNet::RakPeer::SocketQueryOutput userMemory;
DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::Page
```cpp
/* 478056 */
struct DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::Page
{
DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::Page *next;
DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput>::Page *prev;
};

```
#### DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::MemoryWithPage
```cpp
/* 478092 */
struct DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::MemoryWithPage
{
RakNet::ReliabilityLayer::MessageNumberNode userMemory;
DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::Page
```cpp
/* 478001 */
struct DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::Page
{
DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::Page *next;
DataStructures::MemoryPool<RakNet::ReliabilityLayer::MessageNumberNode>::Page *prev;
};

```
#### DataStructures::MemoryPool<RakNet::RemoteClient *>::MemoryWithPage
```cpp
/* 478134 */
struct DataStructures::MemoryPool<RakNet::RemoteClient *>::MemoryWithPage
{
RakNet::RemoteClient *userMemory;
DataStructures::MemoryPool<RakNet::RemoteClient *>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::RemoteClient *>::Page
```cpp
/* 478133 */
struct DataStructures::MemoryPool<RakNet::RemoteClient *>::Page
{
DataStructures::MemoryPool<RakNet::RemoteClient *>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::RemoteClient *>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::RemoteClient *>::Page *next;
DataStructures::MemoryPool<RakNet::RemoteClient *>::Page *prev;
};

```
#### DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::MemoryWithPage
```cpp
/* 478035 */
struct DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::MemoryWithPage
{
RakNet::RemoteSystemIndex userMemory;
DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::Page
```cpp
/* 478034 */
struct DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::Page
{
DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::Page *next;
DataStructures::MemoryPool<RakNet::RemoteSystemIndex>::Page *prev;
};

```
#### DataStructures::MemoryPool<RakNet::SystemAddress>::MemoryWithPage
```cpp
/* 478129 */
struct DataStructures::MemoryPool<RakNet::SystemAddress>::MemoryWithPage
{
RakNet::SystemAddress userMemory;
DataStructures::MemoryPool<RakNet::SystemAddress>::Page *parentPage;
};

```
#### DataStructures::MemoryPool<RakNet::SystemAddress>::Page
```cpp
/* 478128 */
struct DataStructures::MemoryPool<RakNet::SystemAddress>::Page
{
DataStructures::MemoryPool<RakNet::SystemAddress>::MemoryWithPage **availableStack;
int availableStackSize;
DataStructures::MemoryPool<RakNet::SystemAddress>::MemoryWithPage *block;
DataStructures::MemoryPool<RakNet::SystemAddress>::Page *next;
DataStructures::MemoryPool<RakNet::SystemAddress>::Page *prev;
};

```
#### DataStructures::OrderedList<RakNet::uint24_t,DataStructures::RangeNode<RakNet::uint24_t>,&DataStructures::RangeNodeComp>
```cpp
/* 478021 */
struct DataStructures::OrderedList<RakNet::uint24_t,DataStructures::RangeNode<RakNet::uint24_t>,&DataStructures::RangeNodeComp>
{
DataStructures::List<DataStructures::RangeNode<RakNet::uint24_t> > orderedList;
};

```
#### DataStructures::OrderedList<char *,StrAndBool,&RakNet::StrAndBoolComp>
```cpp
/* 478116 */
struct DataStructures::OrderedList<char *,StrAndBool,&RakNet::StrAndBoolComp>
{
DataStructures::List<StrAndBool> orderedList;
};

```
#### DataStructures::OrderedList<int,DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::MapNode,&DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::NodeComparisonFunc>
```cpp
/* 478108 */
struct DataStructures::OrderedList<int,DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::MapNode,&DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::NodeComparisonFunc>
{
DataStructures::List<DataStructures::Map<int,RakNet::HuffmanEncodingTree *,&DataStructures::defaultMapKeyComparison>::MapNode> orderedList;
};

```
#### DataStructures::OrderedList<unsigned short,RakNet::SplitPacketChannel *,&RakNet::SplitPacketChannelComp>
```cpp
/* 478011 */
struct DataStructures::OrderedList<unsigned short,RakNet::SplitPacketChannel *,&RakNet::SplitPacketChannelComp>
{
DataStructures::List<RakNet::SplitPacketChannel *> orderedList;
};

```
#### DataStructures::RangeList<RakNet::uint24_t>
```cpp
/* 478020 */
struct DataStructures::RangeList<RakNet::uint24_t>
{
DataStructures::OrderedList<RakNet::uint24_t,DataStructures::RangeNode<RakNet::uint24_t>,&DataStructures::RangeNodeComp> ranges;
};

```
#### DataStructures::RangeNode<RakNet::uint24_t>
```cpp
/* 478023 */
struct DataStructures::RangeNode<RakNet::uint24_t>
{
RakNet::uint24_t minIndex;
RakNet::uint24_t maxIndex;
};

```
#### DataStructures::ThreadsafeAllocatingQueue<RakNet::Packet>
```cpp
/* 478125 */
struct DataStructures::ThreadsafeAllocatingQueue<RakNet::Packet>
{
DataStructures::MemoryPool<RakNet::Packet> memoryPool;
RakNet::SimpleMutex memoryPoolMutex;
DataStructures::Queue<RakNet::Packet *> queue;
RakNet::SimpleMutex queueMutex;
};

```
#### DataStructures::ThreadsafeAllocatingQueue<RakNet::RakPeer::BufferedCommandStruct>
```cpp
/* 478044 */
struct DataStructures::ThreadsafeAllocatingQueue<RakNet::RakPeer::BufferedCommandStruct>
{
DataStructures::MemoryPool<RakNet::RakPeer::BufferedCommandStruct> memoryPool;
RakNet::SimpleMutex memoryPoolMutex;
DataStructures::Queue<RakNet::RakPeer::BufferedCommandStruct *> queue;
RakNet::SimpleMutex queueMutex;
};

```
#### DataStructures::ThreadsafeAllocatingQueue<RakNet::RakPeer::SocketQueryOutput>
```cpp
/* 478054 */
struct DataStructures::ThreadsafeAllocatingQueue<RakNet::RakPeer::SocketQueryOutput>
{
DataStructures::MemoryPool<RakNet::RakPeer::SocketQueryOutput> memoryPool;
RakNet::SimpleMutex memoryPoolMutex;
DataStructures::Queue<RakNet::RakPeer::SocketQueryOutput *> queue;
RakNet::SimpleMutex queueMutex;
};

```
#### DataStructures::ThreadsafeAllocatingQueue<RakNet::RemoteClient *>
```cpp
/* 478131 */
struct DataStructures::ThreadsafeAllocatingQueue<RakNet::RemoteClient *>
{
DataStructures::MemoryPool<RakNet::RemoteClient *> memoryPool;
RakNet::SimpleMutex memoryPoolMutex;
DataStructures::Queue<RakNet::RemoteClient **> queue;
RakNet::SimpleMutex queueMutex;
};

```
#### DataStructures::ThreadsafeAllocatingQueue<RakNet::SystemAddress>
```cpp
/* 478126 */
struct DataStructures::ThreadsafeAllocatingQueue<RakNet::SystemAddress>
{
DataStructures::MemoryPool<RakNet::SystemAddress> memoryPool;
RakNet::SimpleMutex memoryPoolMutex;
DataStructures::Queue<RakNet::SystemAddress *> queue;
RakNet::SimpleMutex queueMutex;
};

```
#### DataTypeMap::copyFor<BlockPos>
```cpp
/* 109124 */
struct DataTypeMap::copyFor<BlockPos>
{
__int8 gap0[1];
};

```
#### DataTypeMap::copyFor<CompoundTag>
```cpp
/* 116860 */
struct DataTypeMap::copyFor<CompoundTag>
{
__int8 gap0[1];
};

```
#### DataTypeMap::copyFor<Vec3>
```cpp
/* 109121 */
struct DataTypeMap::copyFor<Vec3>
{
__int8 gap0[1];
};

```
#### DataTypeMap::copyFor<float>
```cpp
/* 58762 */
struct DataTypeMap::copyFor<float>
{
__int8 gap0[1];
};

```
#### DataTypeMap::copyFor<int>
```cpp
/* 48723 */
struct DataTypeMap::copyFor<int>
{
__int8 gap0[1];
};

```
#### DataTypeMap::copyFor<long>
```cpp
/* 48720 */
struct DataTypeMap::copyFor<long>
{
__int8 gap0[1];
};

```
#### DataTypeMap::copyFor<short>
```cpp
/* 51817 */
struct DataTypeMap::copyFor<short>
{
__int8 gap0[1];
};

```
#### DataTypeMap::copyFor<signed char>
```cpp
/* 49188 */
struct DataTypeMap::copyFor<signed char>
{
__int8 gap0[1];
};

```
#### DataTypeMap::neqFor<BlockPos>
```cpp
/* 109123 */
struct DataTypeMap::neqFor<BlockPos>
{
__int8 gap0[1];
};

```
#### DataTypeMap::neqFor<CompoundTag>
```cpp
/* 116859 */
struct DataTypeMap::neqFor<CompoundTag>
{
__int8 gap0[1];
};

```
#### DataTypeMap::neqFor<Vec3>
```cpp
/* 109126 */
struct DataTypeMap::neqFor<Vec3>
{
__int8 gap0[1];
};

```
#### DataTypeMap::neqFor<float>
```cpp
/* 58761 */
struct DataTypeMap::neqFor<float>
{
__int8 gap0[1];
};

```
#### DataTypeMap::neqFor<int>
```cpp
/* 48722 */
struct DataTypeMap::neqFor<int>
{
__int8 gap0[1];
};

```
#### DataTypeMap::neqFor<long>
```cpp
/* 109125 */
struct DataTypeMap::neqFor<long>
{
__int8 gap0[1];
};

```
#### DataTypeMap::neqFor<short>
```cpp
/* 51816 */
struct DataTypeMap::neqFor<short>
{
__int8 gap0[1];
};

```
#### DataTypeMap::neqFor<signed char>
```cpp
/* 49187 */
struct DataTypeMap::neqFor<signed char>
{
__int8 gap0[1];
};

```
#### DataTypeMap::typeFor<BlockPos>
```cpp
/* 109122 */
struct DataTypeMap::typeFor<BlockPos>
{
__int8 gap0[1];
};

```
#### DataTypeMap::typeFor<CompoundTag>
```cpp
/* 116858 */
struct DataTypeMap::typeFor<CompoundTag>
{
__int8 gap0[1];
};

```
#### DataTypeMap::typeFor<Vec3>
```cpp
/* 108405 */
struct DataTypeMap::typeFor<Vec3>
{
__int8 gap0[1];
};

```
#### DataTypeMap::typeFor<float>
```cpp
/* 58760 */
struct DataTypeMap::typeFor<float>
{
__int8 gap0[1];
};

```
#### DataTypeMap::typeFor<int>
```cpp
/* 48721 */
struct DataTypeMap::typeFor<int>
{
__int8 gap0[1];
};

```
#### DataTypeMap::typeFor<long>
```cpp
/* 48371 */
struct DataTypeMap::typeFor<long>
{
__int8 gap0[1];
};

```
#### DataTypeMap::typeFor<short>
```cpp
/* 51815 */
struct DataTypeMap::typeFor<short>
{
__int8 gap0[1];
};

```
#### DataTypeMap::typeFor<signed char>
```cpp
/* 49186 */
struct DataTypeMap::typeFor<signed char>
{
__int8 gap0[1];
};

```
#### DateManager
```cpp
/* 82680 */
struct DateManager
{
unsigned int mTimeScale;
time_t mRealTime;
time_t mTime;
Bedrock::Threading::Mutex mScheduledCallbacksMutex;
std::priority_queue<ScheduledCallback,std::vector<ScheduledCallback>,CompareScheduledCallback> mScheduledCallbacks;
};

```
#### DebugAssertException
```cpp
/* 485138 */
struct DebugAssertException
{
__int8 baseclass_0[8];
std::unique_ptr<char []> mDescription;
std::unique_ptr<char []> mArgument;
std::unique_ptr<char []> mInfo;
int mLine;
std::unique_ptr<char []> mFile;
std::unique_ptr<char []> mFunction;
};

```
#### DebugEndPoint;
```cpp
/* 4236 */
struct DebugEndPoint;

```
#### DebugLogScope
```cpp
/* 31299 */
struct DebugLogScope
{
bool mPopScope;
};

```
#### DebugRenderer
```cpp
/* 122535 */
struct DebugRenderer
{
__int8 gap0[1];
};

```
#### DedicatedServerCommands
```cpp
/* 5841 */
struct DedicatedServerCommands
{
__int8 gap0[1];
};

```
#### DefinitionEvent
```cpp
/* 46260 */
struct DefinitionEvent
{
float mProbability;
ActorFilterGroup mFilter;
std::string mName;
DefinitionEventType mType;
std::vector<std::string> mGroups;
std::vector<std::string> mRemoveGroups;
std::vector<DefinitionEvent> mChildren;
};

```
#### DefinitionEventLoader
```cpp
/* 428885 */
struct DefinitionEventLoader
{
__int8 gap0[1];
};

```
#### DefinitionEventLoader::loadEvent::$308FE320F1A5CE0A1A20921AD32B0459
```cpp
/* 428886 */
struct DefinitionEventLoader::loadEvent::$308FE320F1A5CE0A1A20921AD32B0459
{
DefinitionEvent *defEvent;
};

```
#### DefinitionInstanceGroup
```cpp
/* 13227 */
struct DefinitionInstanceGroup
{
std::vector<std::shared_ptr<IDefinitionInstance>> mDefinitionList;
std::unordered_map<std::string,std::shared_ptr<IDefinitionInstance>> mDefinitionMap;
std::unordered_map<unsigned short,std::string> mTypeIdToDefinitionName;
};

```
#### DefinitionModifier
```cpp
/* 109815 */
struct DefinitionModifier
{
std::vector<std::string> mAddGroups;
std::vector<std::string> mRemoveGroups;
};

```
#### DefinitionTrigger
```cpp
/* 47400 */
struct DefinitionTrigger
{
std::string mType;
std::string mTarget;
ActorFilterGroup mFilter;
};

```
#### DelayedDeleter<SubChunkBlockStorage>
```cpp
/* 253102 */
struct DelayedDeleter<SubChunkBlockStorage>
{
DelayedDeleter<SubChunkBlockStorage>::EntryQueue mEntries;
Bedrock::Threading::Mutex mEntriesMutex;
};

```
#### DelayedDeleter<SubChunkBrightnessStorage>
```cpp
/* 253128 */
struct DelayedDeleter<SubChunkBrightnessStorage>
{
DelayedDeleter<SubChunkBrightnessStorage>::EntryQueue mEntries;
Bedrock::Threading::Mutex mEntriesMutex;
};

```
#### DenySameParentsVariantData
```cpp
/* 319706 */
struct DenySameParentsVariantData
{
float mChance;
int mVariantRangeMin;
int mVariantRangeMax;
};

```
#### Description
```cpp
/* 47677 */
struct Description
{
int (**_vptr$Description)(void);
};

```
#### DimensionConversionData
```cpp
/* 190220 */
struct DimensionConversionData
{
Vec3 mOverworldSpawnPoint;
int mNetherScale;
};

```
#### Direction
```cpp
/* 31926 */
struct Direction
{
__int8 gap0[1];
};

```
#### DirtyTicksCounter
```cpp
/* 35002 */
struct DirtyTicksCounter
{
int totalTime;
int lastChange;
};

```
#### DistanceConstraint
```cpp
/* 50282 */
struct DistanceConstraint
{
float mConstraintMass;
Vec3 mConstraintAxis;
float mBias;
bool mShouldEnforce;
float mMassA;
float mMassB;
float mDesiredDistance;
};

```
#### DrinkPotionData
```cpp
/* 88852 */
struct DrinkPotionData
{
int mPotionId;
float mChance;
ActorFilterGroup mFilter;
};

```
#### DwellerComponent
```cpp
/* 53494 */
struct DwellerComponent
{
bool mCanFindPOI;
bool mCanMigrate;
bool mHasJoinedDwelling;
bool mFixUpRole;
bool mRewardPlayersOnFirstFounding;
HashedString mPreferredProfession;
int mFirstFoundingReward;
int mUpdateIntervalVariant;
size_t mDwellingUpdateInterval;
size_t mUpdateIntervalBase;
float mDwellingBoundsTolerance;
DwellerComponent::DwellingType mType;
DwellerRole mRole;
mce::UUID mDwellingUniqueID;
};

```
