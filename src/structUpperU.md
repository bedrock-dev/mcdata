#### UIProfanityContext
```cpp
/* 109097 */
struct UIProfanityContext
{
int (**_vptr$UIProfanityContext)(void);
ProfanityFilterContext mFilterMask;
std::unordered_map<std::string,int> mProfanityExactMap;
std::unordered_set<std::string> mProfanityContainsSet;
};

```
#### UPNPExternalIPResult
```cpp
/* 62646 */
struct UPNPExternalIPResult
{
bool bUPNPSupported;
char hostIPAddress[256];
};

```
#### UPNPInterface
```cpp
/* 62627 */
struct UPNPInterface
{
std::vector<UPNPInterface::ConnectionStateListener *> mConnectionStateListeners;
UPnPResultState<UPNPPortMappingResult> mUPnPPortMappingv4;
UPnPResultState<UPNPPortMappingResult> mUPnPPortMappingv6;
UPnPResultState<UPNPExternalIPResult> mUPnPExternalIP;
MPMCQueue<std::function<void ()> > mCompletedQueue;
};

```
#### UPNPInterface::ConnectionStateListener;
```cpp
/* 62640 */
struct UPNPInterface::ConnectionStateListener;

```
#### UPNPPortMappingResult
```cpp
/* 62642 */
struct UPNPPortMappingResult
{
bool bUPNPSupported;
char hostIPAddress[256];
unsigned __int16 externalPort;
unsigned __int16 internalPort;
};

```
#### UPnPResultState<UPNPExternalIPResult>
```cpp
/* 62645 */
struct UPnPResultState<UPNPExternalIPResult>
{
UPNPExternalIPResult result;
UpnpState state;
bool isValid;
AsyncTracker tracker;
};

```
#### UPnPResultState<UPNPPortMappingResult>
```cpp
/* 62641 */
struct UPnPResultState<UPNPPortMappingResult>
{
UPNPPortMappingResult result;
UpnpState state;
bool isValid;
AsyncTracker tracker;
};

```
#### UnderwaterTorchBlock::animateTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 460050 */
struct UnderwaterTorchBlock::animateTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### UnverifiedCertificate
```cpp
/* 7688 */
struct UnverifiedCertificate
{
const WebToken mRawToken;
Unique<UnverifiedCertificate> mParentUnverifiedCertificate;
};

```
#### UpdateAttributesPacket::AttributeData
```cpp
/* 75559 */
struct UpdateAttributesPacket::AttributeData
{
float mCurrentValue;
float mMinValue;
float mMaxValue;
float mDefaultValue;
HashedString mName;
};

```
#### UpdateAttributesPacket::AttributeData::AttributeData::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 80981 */
struct UpdateAttributesPacket::AttributeData::AttributeData::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### UpdateBlockPropertiesPacket::UpdateBlockPropertiesPacket::$5D452180F6FD32FDE19EF7DE5EC88D21
```cpp
/* 81087 */
struct UpdateBlockPropertiesPacket::UpdateBlockPropertiesPacket::$5D452180F6FD32FDE19EF7DE5EC88D21
{
Unique<CompoundTag> *defTag;
};

```
#### Util::CaseInsensitiveCompare
```cpp
/* 103854 */
struct Util::CaseInsensitiveCompare
{
__int8 gap0[1];
};

```
#### Util::CaseInsensitiveHash
```cpp
/* 103853 */
struct Util::CaseInsensitiveHash
{
__int8 gap0[1];
};

```
#### Util::HashString
```cpp
/* 45356 */
struct Util::HashString
{
std::string mText;
uint64_t mHash;
};

```
#### Util::HashString::HashFunc
```cpp
/* 46187 */
struct Util::HashString::HashFunc
{
__int8 gap0[1];
};

```
#### Util::LootTableUtils
```cpp
/* 428930 */
struct Util::LootTableUtils
{
__int8 gap0[1];
};

```
#### Util::compareNoCase::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 485115 */
struct Util::compareNoCase::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Util::toLower::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 485116 */
struct Util::toLower::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Util::toLowerInPlace::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 485118 */
struct Util::toLowerInPlace::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Util::toUpper::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 485117 */
struct Util::toUpper::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Util::toUpperInPlace::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 485119 */
struct Util::toUpperInPlace::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### UIProfanityContext
```cpp
/* 109097 */
struct UIProfanityContext
{
int (**_vptr$UIProfanityContext)(void);
ProfanityFilterContext mFilterMask;
std::unordered_map<std::string,int> mProfanityExactMap;
std::unordered_set<std::string> mProfanityContainsSet;
};

```
#### UPNPExternalIPResult
```cpp
/* 62646 */
struct UPNPExternalIPResult
{
bool bUPNPSupported;
char hostIPAddress[256];
};

```
#### UPNPInterface
```cpp
/* 62627 */
struct UPNPInterface
{
std::vector<UPNPInterface::ConnectionStateListener *> mConnectionStateListeners;
UPnPResultState<UPNPPortMappingResult> mUPnPPortMappingv4;
UPnPResultState<UPNPPortMappingResult> mUPnPPortMappingv6;
UPnPResultState<UPNPExternalIPResult> mUPnPExternalIP;
MPMCQueue<std::function<void ()> > mCompletedQueue;
};

```
#### UPNPInterface::ConnectionStateListener;
```cpp
/* 62640 */
struct UPNPInterface::ConnectionStateListener;

```
#### UPNPPortMappingResult
```cpp
/* 62642 */
struct UPNPPortMappingResult
{
bool bUPNPSupported;
char hostIPAddress[256];
unsigned __int16 externalPort;
unsigned __int16 internalPort;
};

```
#### UPnPResultState<UPNPExternalIPResult>
```cpp
/* 62645 */
struct UPnPResultState<UPNPExternalIPResult>
{
UPNPExternalIPResult result;
UpnpState state;
bool isValid;
AsyncTracker tracker;
};

```
#### UPnPResultState<UPNPPortMappingResult>
```cpp
/* 62641 */
struct UPnPResultState<UPNPPortMappingResult>
{
UPNPPortMappingResult result;
UpnpState state;
bool isValid;
AsyncTracker tracker;
};

```
#### UnderwaterTorchBlock::animateTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 460050 */
struct UnderwaterTorchBlock::animateTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### UnverifiedCertificate
```cpp
/* 7688 */
struct UnverifiedCertificate
{
const WebToken mRawToken;
Unique<UnverifiedCertificate> mParentUnverifiedCertificate;
};

```
#### UpdateAttributesPacket::AttributeData
```cpp
/* 75559 */
struct UpdateAttributesPacket::AttributeData
{
float mCurrentValue;
float mMinValue;
float mMaxValue;
float mDefaultValue;
HashedString mName;
};

```
#### UpdateAttributesPacket::AttributeData::AttributeData::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 80981 */
struct UpdateAttributesPacket::AttributeData::AttributeData::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### UpdateBlockPropertiesPacket::UpdateBlockPropertiesPacket::$5D452180F6FD32FDE19EF7DE5EC88D21
```cpp
/* 81087 */
struct UpdateBlockPropertiesPacket::UpdateBlockPropertiesPacket::$5D452180F6FD32FDE19EF7DE5EC88D21
{
Unique<CompoundTag> *defTag;
};

```
#### Util::CaseInsensitiveCompare
```cpp
/* 103854 */
struct Util::CaseInsensitiveCompare
{
__int8 gap0[1];
};

```
#### Util::CaseInsensitiveHash
```cpp
/* 103853 */
struct Util::CaseInsensitiveHash
{
__int8 gap0[1];
};

```
#### Util::HashString
```cpp
/* 45356 */
struct Util::HashString
{
std::string mText;
uint64_t mHash;
};

```
#### Util::HashString::HashFunc
```cpp
/* 46187 */
struct Util::HashString::HashFunc
{
__int8 gap0[1];
};

```
#### Util::LootTableUtils
```cpp
/* 428930 */
struct Util::LootTableUtils
{
__int8 gap0[1];
};

```
#### Util::compareNoCase::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 485115 */
struct Util::compareNoCase::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Util::toLower::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 485116 */
struct Util::toLower::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Util::toLowerInPlace::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 485118 */
struct Util::toLowerInPlace::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Util::toUpper::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 485117 */
struct Util::toUpper::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Util::toUpperInPlace::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 485119 */
struct Util::toUpperInPlace::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
