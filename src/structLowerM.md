#### mce::Blob
```cpp
/* 74244 */
struct mce::Blob
{
std::unique_ptr<unsigned char []> mBlob;
size_t mSize;
};

```
#### mce::Image
```cpp
/* 74240 */
struct mce::Image
{
mce::ImageFormat imageFormat;
uint32_t mWidth;
uint32_t mHeight;
mce::ImageUsage mUsage;
mce::Image::Storage mImageBytes;
};

```
#### mce::Image_0
```cpp
/* 173107 */
struct mce::Image_0
{
mce::ImageFormat imageFormat;
uint32_t mWidth;
uint32_t mHeight;
mce::ImageUsage_0 mUsage;
mce::Image::Storage mImageBytes;
};

```
#### mce::MaterialPtr
```cpp
/* 47749 */
struct mce::MaterialPtr
{
__int8 gap0[1];
};

```
#### mce::Math
```cpp
/* 5915 */
struct mce::Math
{
__int8 gap0[1];
};

```
#### mce::MathUtility
```cpp
/* 483068 */
struct mce::MathUtility
{
__int8 gap0[1];
};

```
#### mce::UUID
```cpp
/* 2174 */
struct mce::UUID
{
uint64_t Data[2];
};

```
#### mce::`anonymous namespace'::MathInitializer
```cpp
/* 483064 */
struct mce::`anonymous namespace'::MathInitializer
{
__int8 gap0[1];
};

```
#### mclc::ConversionReport;
```cpp
/* 45359 */
struct mclc::ConversionReport;

```
#### mcontext_t
```cpp
/* 485607 */
struct mcontext_t
{
gregset_t gregs;
fpregset_t fpregs;
unsigned __int64 __reserved1[8];
};

```
#### moodycamel::ConcurrentQueueDefaultTraits
```cpp
/* 7019 */
struct moodycamel::ConcurrentQueueDefaultTraits
{
__int8 gap0[1];
};

```
#### moodycamel::ConsumerToken
```cpp
/* 7020 */
struct moodycamel::ConsumerToken
{
uint32_t initialOffset;
uint32_t lastKnownGlobalOffset;
uint32_t itemsConsumedFromCurrent;
moodycamel::details::ConcurrentQueueProducerTypelessBase *currentProducer;
moodycamel::details::ConcurrentQueueProducerTypelessBase *desiredProducer;
};

```
#### moodycamel::ProducerToken
```cpp
/* 6850 */
struct moodycamel::ProducerToken
{
moodycamel::details::ConcurrentQueueProducerTypelessBase *producer;
};

```
#### moodycamel::details::ConcurrentQueueProducerTypelessBase
```cpp
/* 6849 */
struct moodycamel::details::ConcurrentQueueProducerTypelessBase
{
moodycamel::details::ConcurrentQueueProducerTypelessBase *next;
std::atomic<bool> inactive;
moodycamel::ProducerToken *token;
};

```
#### moodycamel::details::_hash_32_or_64<true>
```cpp
/* 8624 */
struct moodycamel::details::_hash_32_or_64<true>
{
__int8 gap0[1];
};

```
#### moodycamel::details::thread_id_converter<unsigned long>
```cpp
/* 8625 */
struct moodycamel::details::thread_id_converter<unsigned long>
{
__int8 gap0[1];
};

```
#### msghdr
```cpp
/* 486711 */
struct msghdr
{
void *msg_name;
socklen_t msg_namelen;
iovec *msg_iov;
size_t msg_iovlen;
void *msg_control;
size_t msg_controllen;
int msg_flags;
};

```
#### mce::Blob
```cpp
/* 74244 */
struct mce::Blob
{
std::unique_ptr<unsigned char []> mBlob;
size_t mSize;
};

```
#### mce::Image
```cpp
/* 74240 */
struct mce::Image
{
mce::ImageFormat imageFormat;
uint32_t mWidth;
uint32_t mHeight;
mce::ImageUsage mUsage;
mce::Image::Storage mImageBytes;
};

```
#### mce::Image_0
```cpp
/* 173107 */
struct mce::Image_0
{
mce::ImageFormat imageFormat;
uint32_t mWidth;
uint32_t mHeight;
mce::ImageUsage_0 mUsage;
mce::Image::Storage mImageBytes;
};

```
#### mce::MaterialPtr
```cpp
/* 47749 */
struct mce::MaterialPtr
{
__int8 gap0[1];
};

```
#### mce::Math
```cpp
/* 5915 */
struct mce::Math
{
__int8 gap0[1];
};

```
#### mce::MathUtility
```cpp
/* 483068 */
struct mce::MathUtility
{
__int8 gap0[1];
};

```
#### mce::UUID
```cpp
/* 2174 */
struct mce::UUID
{
uint64_t Data[2];
};

```
#### mce::`anonymous namespace'::MathInitializer
```cpp
/* 483064 */
struct mce::`anonymous namespace'::MathInitializer
{
__int8 gap0[1];
};

```
#### mclc::ConversionReport;
```cpp
/* 45359 */
struct mclc::ConversionReport;

```
#### mcontext_t
```cpp
/* 485607 */
struct mcontext_t
{
gregset_t gregs;
fpregset_t fpregs;
unsigned __int64 __reserved1[8];
};

```
#### moodycamel::ConcurrentQueueDefaultTraits
```cpp
/* 7019 */
struct moodycamel::ConcurrentQueueDefaultTraits
{
__int8 gap0[1];
};

```
#### moodycamel::ConsumerToken
```cpp
/* 7020 */
struct moodycamel::ConsumerToken
{
uint32_t initialOffset;
uint32_t lastKnownGlobalOffset;
uint32_t itemsConsumedFromCurrent;
moodycamel::details::ConcurrentQueueProducerTypelessBase *currentProducer;
moodycamel::details::ConcurrentQueueProducerTypelessBase *desiredProducer;
};

```
#### moodycamel::ProducerToken
```cpp
/* 6850 */
struct moodycamel::ProducerToken
{
moodycamel::details::ConcurrentQueueProducerTypelessBase *producer;
};

```
#### moodycamel::details::ConcurrentQueueProducerTypelessBase
```cpp
/* 6849 */
struct moodycamel::details::ConcurrentQueueProducerTypelessBase
{
moodycamel::details::ConcurrentQueueProducerTypelessBase *next;
std::atomic<bool> inactive;
moodycamel::ProducerToken *token;
};

```
#### moodycamel::details::_hash_32_or_64<true>
```cpp
/* 8624 */
struct moodycamel::details::_hash_32_or_64<true>
{
__int8 gap0[1];
};

```
#### moodycamel::details::thread_id_converter<unsigned long>
```cpp
/* 8625 */
struct moodycamel::details::thread_id_converter<unsigned long>
{
__int8 gap0[1];
};

```
#### msghdr
```cpp
/* 486711 */
struct msghdr
{
void *msg_name;
socklen_t msg_namelen;
iovec *msg_iov;
size_t msg_iovlen;
void *msg_control;
size_t msg_controllen;
int msg_flags;
};

```
