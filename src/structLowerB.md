#### batch_control;
```cpp
/* 486931 */
struct batch_control;

```
#### buffer_span<Actor *>
```cpp
/* 35029 */
struct buffer_span<Actor *>
{
Actor *const *mBegin;
Actor *const *mEnd;
};

```
#### buffer_span<Actor *>::iterator
```cpp
/* 186239 */
struct buffer_span<Actor *>::iterator
{
Actor *const *mPtr;
};

```
#### buffer_span<ActorUniqueID>;
```cpp
/* 238403 */
struct buffer_span<ActorUniqueID>;

```
#### buffer_span<BlockID>
```cpp
/* 35024 */
struct buffer_span<BlockID>
{
const BlockID *mBegin;
const BlockID *mEnd;
};

```
#### buffer_span<BlockID>::iterator;
```cpp
/* 186038 */
struct buffer_span<BlockID>::iterator;

```
#### buffer_span<ChunkPos>
```cpp
/* 37037 */
struct buffer_span<ChunkPos>
{
const ChunkPos *mBegin;
const ChunkPos *mEnd;
};

```
#### buffer_span<ChunkPos>::iterator
```cpp
/* 37038 */
struct buffer_span<ChunkPos>::iterator
{
const ChunkPos *mPtr;
};

```
#### buffer_span<DBChunkStorage *>;
```cpp
/* 462857 */
struct buffer_span<DBChunkStorage *>;

```
#### buffer_span<NibblePair>
```cpp
/* 35025 */
struct buffer_span<NibblePair>
{
const NibblePair *mBegin;
const NibblePair *mEnd;
};

```
#### buffer_span<NibblePair>::iterator;
```cpp
/* 35027 */
struct buffer_span<NibblePair>::iterator;

```
#### buffer_span<Pos>
```cpp
/* 36714 */
struct buffer_span<Pos>
{
const Pos *mBegin;
const Pos *mEnd;
};

```
#### buffer_span<Pos>::iterator;
```cpp
/* 252366 */
struct buffer_span<Pos>::iterator;

```
#### buffer_span<SubChunk>
```cpp
/* 35016 */
struct buffer_span<SubChunk>
{
const SubChunk *mBegin;
const SubChunk *mEnd;
};

```
#### buffer_span<SubChunk>::iterator;
```cpp
/* 35017 */
struct buffer_span<SubChunk>::iterator;

```
#### buffer_span<WorkerPool *>
```cpp
/* 82011 */
struct buffer_span<WorkerPool *>
{
WorkerPool *const *mBegin;
WorkerPool *const *mEnd;
};

```
#### buffer_span<WorkerPool *>::iterator;
```cpp
/* 484577 */
struct buffer_span<WorkerPool *>::iterator;

```
#### buffer_span<bool>
```cpp
/* 45350 */
struct buffer_span<bool>
{
const bool *mBegin;
const bool *mEnd;
};

```
#### buffer_span<bool>::iterator;
```cpp
/* 484920 */
struct buffer_span<bool>::iterator;

```
#### buffer_span<const Block *>
```cpp
/* 35015 */
struct buffer_span<const Block *>
{
const Block *const *mBegin;
const Block *const *mEnd;
};

```
#### buffer_span<const Block *>::iterator;
```cpp
/* 37035 */
struct buffer_span<const Block *>::iterator;

```
#### buffer_span<int>
```cpp
/* 45351 */
struct buffer_span<int>
{
const int *mBegin;
const int *mEnd;
};

```
#### buffer_span<int>::iterator;
```cpp
/* 484922 */
struct buffer_span<int>::iterator;

```
#### buffer_span<unsigned int>::iterator
```cpp
/* 78786 */
struct buffer_span<unsigned int>::iterator
{
const unsigned int *mPtr;
};

```
#### buffer_span_mut<Actor *>;
```cpp
/* 186240 */
struct buffer_span_mut<Actor *>;

```
#### buffer_span_mut<BlockID>;
```cpp
/* 186039 */
struct buffer_span_mut<BlockID>;

```
#### buffer_span_mut<ChunkPos>;
```cpp
/* 37039 */
struct buffer_span_mut<ChunkPos>;

```
#### buffer_span_mut<NibblePair>;
```cpp
/* 35028 */
struct buffer_span_mut<NibblePair>;

```
#### buffer_span_mut<Pos>;
```cpp
/* 252367 */
struct buffer_span_mut<Pos>;

```
#### buffer_span_mut<SubChunk>
```cpp
/* 35018 */
struct buffer_span_mut<SubChunk>
{
SubChunk *mBegin;
SubChunk *mEnd;
};

```
#### buffer_span_mut<SubChunk>::iterator
```cpp
/* 35019 */
struct buffer_span_mut<SubChunk>::iterator
{
SubChunk *mPtr;
};

```
#### buffer_span_mut<WorkerPool *>;
```cpp
/* 484578 */
struct buffer_span_mut<WorkerPool *>;

```
#### buffer_span_mut<bool>;
```cpp
/* 484921 */
struct buffer_span_mut<bool>;

```
#### buffer_span_mut<const Block *>
```cpp
/* 35011 */
struct buffer_span_mut<const Block *>
{
const Block **mBegin;
const Block **mEnd;
};

```
#### buffer_span_mut<const Block *>::iterator
```cpp
/* 35013 */
struct buffer_span_mut<const Block *>::iterator
{
const Block **mPtr;
};

```
#### buffer_span_mut<int>;
```cpp
/* 484923 */
struct buffer_span_mut<int>;

```
#### buffer_span_mut<long>
```cpp
/* 35014 */
struct buffer_span_mut<long>
{
__int64 *mBegin;
__int64 *mEnd;
};

```
#### buffer_span_mut<long>::iterator;
```cpp
/* 37033 */
struct buffer_span_mut<long>::iterator;

```
#### buffer_span_mut<unsigned int>
```cpp
/* 78787 */
struct buffer_span_mut<unsigned int>
{
unsigned int *mBegin;
unsigned int *mEnd;
};

```
#### buffer_span_mut<unsigned int>::iterator;
```cpp
/* 183200 */
struct buffer_span_mut<unsigned int>::iterator;

```
#### batch_control;
```cpp
/* 486931 */
struct batch_control;

```
#### buffer_span<Actor *>
```cpp
/* 35029 */
struct buffer_span<Actor *>
{
Actor *const *mBegin;
Actor *const *mEnd;
};

```
#### buffer_span<Actor *>::iterator
```cpp
/* 186239 */
struct buffer_span<Actor *>::iterator
{
Actor *const *mPtr;
};

```
#### buffer_span<ActorUniqueID>;
```cpp
/* 238403 */
struct buffer_span<ActorUniqueID>;

```
#### buffer_span<BlockID>
```cpp
/* 35024 */
struct buffer_span<BlockID>
{
const BlockID *mBegin;
const BlockID *mEnd;
};

```
#### buffer_span<BlockID>::iterator;
```cpp
/* 186038 */
struct buffer_span<BlockID>::iterator;

```
#### buffer_span<ChunkPos>
```cpp
/* 37037 */
struct buffer_span<ChunkPos>
{
const ChunkPos *mBegin;
const ChunkPos *mEnd;
};

```
#### buffer_span<ChunkPos>::iterator
```cpp
/* 37038 */
struct buffer_span<ChunkPos>::iterator
{
const ChunkPos *mPtr;
};

```
#### buffer_span<DBChunkStorage *>;
```cpp
/* 462857 */
struct buffer_span<DBChunkStorage *>;

```
#### buffer_span<NibblePair>
```cpp
/* 35025 */
struct buffer_span<NibblePair>
{
const NibblePair *mBegin;
const NibblePair *mEnd;
};

```
#### buffer_span<NibblePair>::iterator;
```cpp
/* 35027 */
struct buffer_span<NibblePair>::iterator;

```
#### buffer_span<Pos>
```cpp
/* 36714 */
struct buffer_span<Pos>
{
const Pos *mBegin;
const Pos *mEnd;
};

```
#### buffer_span<Pos>::iterator;
```cpp
/* 252366 */
struct buffer_span<Pos>::iterator;

```
#### buffer_span<SubChunk>
```cpp
/* 35016 */
struct buffer_span<SubChunk>
{
const SubChunk *mBegin;
const SubChunk *mEnd;
};

```
#### buffer_span<SubChunk>::iterator;
```cpp
/* 35017 */
struct buffer_span<SubChunk>::iterator;

```
#### buffer_span<WorkerPool *>
```cpp
/* 82011 */
struct buffer_span<WorkerPool *>
{
WorkerPool *const *mBegin;
WorkerPool *const *mEnd;
};

```
#### buffer_span<WorkerPool *>::iterator;
```cpp
/* 484577 */
struct buffer_span<WorkerPool *>::iterator;

```
#### buffer_span<bool>
```cpp
/* 45350 */
struct buffer_span<bool>
{
const bool *mBegin;
const bool *mEnd;
};

```
#### buffer_span<bool>::iterator;
```cpp
/* 484920 */
struct buffer_span<bool>::iterator;

```
#### buffer_span<const Block *>
```cpp
/* 35015 */
struct buffer_span<const Block *>
{
const Block *const *mBegin;
const Block *const *mEnd;
};

```
#### buffer_span<const Block *>::iterator;
```cpp
/* 37035 */
struct buffer_span<const Block *>::iterator;

```
#### buffer_span<int>
```cpp
/* 45351 */
struct buffer_span<int>
{
const int *mBegin;
const int *mEnd;
};

```
#### buffer_span<int>::iterator;
```cpp
/* 484922 */
struct buffer_span<int>::iterator;

```
#### buffer_span<unsigned int>::iterator
```cpp
/* 78786 */
struct buffer_span<unsigned int>::iterator
{
const unsigned int *mPtr;
};

```
#### buffer_span_mut<Actor *>;
```cpp
/* 186240 */
struct buffer_span_mut<Actor *>;

```
#### buffer_span_mut<BlockID>;
```cpp
/* 186039 */
struct buffer_span_mut<BlockID>;

```
#### buffer_span_mut<ChunkPos>;
```cpp
/* 37039 */
struct buffer_span_mut<ChunkPos>;

```
#### buffer_span_mut<NibblePair>;
```cpp
/* 35028 */
struct buffer_span_mut<NibblePair>;

```
#### buffer_span_mut<Pos>;
```cpp
/* 252367 */
struct buffer_span_mut<Pos>;

```
#### buffer_span_mut<SubChunk>
```cpp
/* 35018 */
struct buffer_span_mut<SubChunk>
{
SubChunk *mBegin;
SubChunk *mEnd;
};

```
#### buffer_span_mut<SubChunk>::iterator
```cpp
/* 35019 */
struct buffer_span_mut<SubChunk>::iterator
{
SubChunk *mPtr;
};

```
#### buffer_span_mut<WorkerPool *>;
```cpp
/* 484578 */
struct buffer_span_mut<WorkerPool *>;

```
#### buffer_span_mut<bool>;
```cpp
/* 484921 */
struct buffer_span_mut<bool>;

```
#### buffer_span_mut<const Block *>
```cpp
/* 35011 */
struct buffer_span_mut<const Block *>
{
const Block **mBegin;
const Block **mEnd;
};

```
#### buffer_span_mut<const Block *>::iterator
```cpp
/* 35013 */
struct buffer_span_mut<const Block *>::iterator
{
const Block **mPtr;
};

```
#### buffer_span_mut<int>;
```cpp
/* 484923 */
struct buffer_span_mut<int>;

```
#### buffer_span_mut<long>
```cpp
/* 35014 */
struct buffer_span_mut<long>
{
__int64 *mBegin;
__int64 *mEnd;
};

```
#### buffer_span_mut<long>::iterator;
```cpp
/* 37033 */
struct buffer_span_mut<long>::iterator;

```
#### buffer_span_mut<unsigned int>
```cpp
/* 78787 */
struct buffer_span_mut<unsigned int>
{
unsigned int *mBegin;
unsigned int *mEnd;
};

```
#### buffer_span_mut<unsigned int>::iterator;
```cpp
/* 183200 */
struct buffer_span_mut<unsigned int>::iterator;

```
