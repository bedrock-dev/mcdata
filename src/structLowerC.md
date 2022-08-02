#### census_context;
```cpp
/* 7965 */
struct census_context;

```
#### cg::ImageBuffer;
```cpp
/* 35041 */
struct cg::ImageBuffer;

```
#### cg::ImageDescription
```cpp
/* 457060 */
struct cg::ImageDescription
{
uint32_t mWidth;
uint32_t mHeight;
mce::TextureFormat mTextureFormat;
cg::ColorSpace mColorSpace;
bool mIsCubemap;
uint32_t mArraySize;
};

```
#### child_call;
```cpp
/* 486749 */
struct child_call;

```
#### cmsghdr
```cpp
/* 485738 */
struct cmsghdr
{
size_t cmsg_len;
int cmsg_level;
int cmsg_type;
unsigned __int8 __cmsg_data[];
};

```
#### com::mojang::clacks::protocol::Commands
```cpp
/* 7928 */
struct com::mojang::clacks::protocol::Commands
{
__int8 gap0[1];
};

```
#### com::mojang::clacks::protocol::Commands::StubInterface::experimental_async_interface
```cpp
/* 8773 */
struct com::mojang::clacks::protocol::Commands::StubInterface::experimental_async_interface
{
int (**_vptr$experimental_async_interface)(void);
};

```
#### com::mojang::clacks::protocol::EmptyDefaultTypeInternal
```cpp
/* 486547 */
struct com::mojang::clacks::protocol::EmptyDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::Empty> _instance;
};

```
#### com::mojang::clacks::protocol::LevelFileAndSizeDefaultTypeInternal
```cpp
/* 486571 */
struct com::mojang::clacks::protocol::LevelFileAndSizeDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::LevelFileAndSize> _instance;
};

```
#### com::mojang::clacks::protocol::MessageDefaultTypeInternal
```cpp
/* 486550 */
struct com::mojang::clacks::protocol::MessageDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::Message> _instance;
};

```
#### com::mojang::clacks::protocol::MetricReport
```cpp
/* 7630 */
struct com::mojang::clacks::protocol::MetricReport
{
__int8 baseclass_0[8];
google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
com::mojang::clacks::protocol::MetricReport::MetricUnion metric_;
google::protobuf::internal::CachedSize _cached_size_;
google::protobuf::uint32 _oneof_case_[1];
};

```
#### com::mojang::clacks::protocol::MetricReportDefaultTypeInternal
```cpp
/* 486586 */
struct com::mojang::clacks::protocol::MetricReportDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::MetricReport> _instance;
const com::mojang::clacks::protocol::MetricReport_BandwithMetric *bandwith_;
const com::mojang::clacks::protocol::MetricReport_LatencyMetric *latency_;
google::protobuf::int64 ticktime_;
};

```
#### com::mojang::clacks::protocol::MetricReport_BandwithMetricDefaultTypeInternal
```cpp
/* 486580 */
struct com::mojang::clacks::protocol::MetricReport_BandwithMetricDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::MetricReport_BandwithMetric> _instance;
};

```
#### com::mojang::clacks::protocol::MetricReport_LatencyMetricDefaultTypeInternal
```cpp
/* 486583 */
struct com::mojang::clacks::protocol::MetricReport_LatencyMetricDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::MetricReport_LatencyMetric> _instance;
};

```
#### com::mojang::clacks::protocol::PlayerAndMessageDefaultTypeInternal
```cpp
/* 486565 */
struct com::mojang::clacks::protocol::PlayerAndMessageDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::PlayerAndMessage> _instance;
};

```
#### com::mojang::clacks::protocol::PlayerInfo
```cpp
/* 7933 */
struct com::mojang::clacks::protocol::PlayerInfo
{
__int8 baseclass_0[8];
google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
com::mojang::clacks::protocol::Xuid *xuid_;
com::mojang::clacks::protocol::PlayerName *name_;
int playertype_;
google::protobuf::internal::CachedSize _cached_size_;
};

```
#### com::mojang::clacks::protocol::PlayerInfoDefaultTypeInternal
```cpp
/* 486559 */
struct com::mojang::clacks::protocol::PlayerInfoDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::PlayerInfo> _instance;
};

```
#### com::mojang::clacks::protocol::PlayerListDefaultTypeInternal
```cpp
/* 486562 */
struct com::mojang::clacks::protocol::PlayerListDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::PlayerList> _instance;
};

```
#### com::mojang::clacks::protocol::PlayerNameDefaultTypeInternal
```cpp
/* 486556 */
struct com::mojang::clacks::protocol::PlayerNameDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::PlayerName> _instance;
};

```
#### com::mojang::clacks::protocol::SaveQueryResultDefaultTypeInternal
```cpp
/* 486574 */
struct com::mojang::clacks::protocol::SaveQueryResultDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::SaveQueryResult> _instance;
};

```
#### com::mojang::clacks::protocol::SaveStateResult
```cpp
/* 7932 */
struct com::mojang::clacks::protocol::SaveStateResult
{
__int8 baseclass_0[8];
google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
int savestate_;
google::protobuf::internal::CachedSize _cached_size_;
};

```
#### com::mojang::clacks::protocol::SaveStateResultDefaultTypeInternal
```cpp
/* 486577 */
struct com::mojang::clacks::protocol::SaveStateResultDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::SaveStateResult> _instance;
};

```
#### com::mojang::clacks::protocol::SettingsDefaultTypeInternal
```cpp
/* 486568 */
struct com::mojang::clacks::protocol::SettingsDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::Settings> _instance;
int difficultysetting_;
int cheatssetting_;
};

```
#### com::mojang::clacks::protocol::XuidDefaultTypeInternal
```cpp
/* 486553 */
struct com::mojang::clacks::protocol::XuidDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::Xuid> _instance;
};

```
#### commands::Postfix
```cpp
/* 428725 */
struct commands::Postfix
{
const char *postfix;
};

```
#### commands::SoftEnum
```cpp
/* 426876 */
struct commands::SoftEnum
{
const char *name;
};

```
#### createUniqueRakPeer::$0DB58CF58EC7BF1F4DDADE930FB66FD4;
```cpp
/* 77651 */
struct createUniqueRakPeer::$0DB58CF58EC7BF1F4DDADE930FB66FD4;

```
#### curfile64_info
```cpp
/* 485438 */
struct curfile64_info
{
z_stream stream;
int stream_initialised;
uInt pos_in_buffered_data;
ZPOS64_T pos_local_header;
char *central_header;
uLong size_centralExtra;
uLong size_centralheader;
uLong size_centralExtraFree;
uLong flag;
int method;
int raw;
Byte buffered_data[65536];
uLong dosDate;
uLong crc32;
int encrypt;
int zip64;
ZPOS64_T pos_zip64extrainfo;
ZPOS64_T totalCompressedData;
ZPOS64_T totalUncompressedData;
};

```
#### curl_httppost;
```cpp
/* 485602 */
struct curl_httppost;

```
#### curl_slist;
```cpp
/* 485603 */
struct curl_slist;

```
#### census_context;
```cpp
/* 7965 */
struct census_context;

```
#### cg::ImageBuffer;
```cpp
/* 35041 */
struct cg::ImageBuffer;

```
#### cg::ImageDescription
```cpp
/* 457060 */
struct cg::ImageDescription
{
uint32_t mWidth;
uint32_t mHeight;
mce::TextureFormat mTextureFormat;
cg::ColorSpace mColorSpace;
bool mIsCubemap;
uint32_t mArraySize;
};

```
#### child_call;
```cpp
/* 486749 */
struct child_call;

```
#### cmsghdr
```cpp
/* 485738 */
struct cmsghdr
{
size_t cmsg_len;
int cmsg_level;
int cmsg_type;
unsigned __int8 __cmsg_data[];
};

```
#### com::mojang::clacks::protocol::Commands
```cpp
/* 7928 */
struct com::mojang::clacks::protocol::Commands
{
__int8 gap0[1];
};

```
#### com::mojang::clacks::protocol::Commands::StubInterface::experimental_async_interface
```cpp
/* 8773 */
struct com::mojang::clacks::protocol::Commands::StubInterface::experimental_async_interface
{
int (**_vptr$experimental_async_interface)(void);
};

```
#### com::mojang::clacks::protocol::EmptyDefaultTypeInternal
```cpp
/* 486547 */
struct com::mojang::clacks::protocol::EmptyDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::Empty> _instance;
};

```
#### com::mojang::clacks::protocol::LevelFileAndSizeDefaultTypeInternal
```cpp
/* 486571 */
struct com::mojang::clacks::protocol::LevelFileAndSizeDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::LevelFileAndSize> _instance;
};

```
#### com::mojang::clacks::protocol::MessageDefaultTypeInternal
```cpp
/* 486550 */
struct com::mojang::clacks::protocol::MessageDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::Message> _instance;
};

```
#### com::mojang::clacks::protocol::MetricReport
```cpp
/* 7630 */
struct com::mojang::clacks::protocol::MetricReport
{
__int8 baseclass_0[8];
google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
com::mojang::clacks::protocol::MetricReport::MetricUnion metric_;
google::protobuf::internal::CachedSize _cached_size_;
google::protobuf::uint32 _oneof_case_[1];
};

```
#### com::mojang::clacks::protocol::MetricReportDefaultTypeInternal
```cpp
/* 486586 */
struct com::mojang::clacks::protocol::MetricReportDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::MetricReport> _instance;
const com::mojang::clacks::protocol::MetricReport_BandwithMetric *bandwith_;
const com::mojang::clacks::protocol::MetricReport_LatencyMetric *latency_;
google::protobuf::int64 ticktime_;
};

```
#### com::mojang::clacks::protocol::MetricReport_BandwithMetricDefaultTypeInternal
```cpp
/* 486580 */
struct com::mojang::clacks::protocol::MetricReport_BandwithMetricDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::MetricReport_BandwithMetric> _instance;
};

```
#### com::mojang::clacks::protocol::MetricReport_LatencyMetricDefaultTypeInternal
```cpp
/* 486583 */
struct com::mojang::clacks::protocol::MetricReport_LatencyMetricDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::MetricReport_LatencyMetric> _instance;
};

```
#### com::mojang::clacks::protocol::PlayerAndMessageDefaultTypeInternal
```cpp
/* 486565 */
struct com::mojang::clacks::protocol::PlayerAndMessageDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::PlayerAndMessage> _instance;
};

```
#### com::mojang::clacks::protocol::PlayerInfo
```cpp
/* 7933 */
struct com::mojang::clacks::protocol::PlayerInfo
{
__int8 baseclass_0[8];
google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
com::mojang::clacks::protocol::Xuid *xuid_;
com::mojang::clacks::protocol::PlayerName *name_;
int playertype_;
google::protobuf::internal::CachedSize _cached_size_;
};

```
#### com::mojang::clacks::protocol::PlayerInfoDefaultTypeInternal
```cpp
/* 486559 */
struct com::mojang::clacks::protocol::PlayerInfoDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::PlayerInfo> _instance;
};

```
#### com::mojang::clacks::protocol::PlayerListDefaultTypeInternal
```cpp
/* 486562 */
struct com::mojang::clacks::protocol::PlayerListDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::PlayerList> _instance;
};

```
#### com::mojang::clacks::protocol::PlayerNameDefaultTypeInternal
```cpp
/* 486556 */
struct com::mojang::clacks::protocol::PlayerNameDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::PlayerName> _instance;
};

```
#### com::mojang::clacks::protocol::SaveQueryResultDefaultTypeInternal
```cpp
/* 486574 */
struct com::mojang::clacks::protocol::SaveQueryResultDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::SaveQueryResult> _instance;
};

```
#### com::mojang::clacks::protocol::SaveStateResult
```cpp
/* 7932 */
struct com::mojang::clacks::protocol::SaveStateResult
{
__int8 baseclass_0[8];
google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
int savestate_;
google::protobuf::internal::CachedSize _cached_size_;
};

```
#### com::mojang::clacks::protocol::SaveStateResultDefaultTypeInternal
```cpp
/* 486577 */
struct com::mojang::clacks::protocol::SaveStateResultDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::SaveStateResult> _instance;
};

```
#### com::mojang::clacks::protocol::SettingsDefaultTypeInternal
```cpp
/* 486568 */
struct com::mojang::clacks::protocol::SettingsDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::Settings> _instance;
int difficultysetting_;
int cheatssetting_;
};

```
#### com::mojang::clacks::protocol::XuidDefaultTypeInternal
```cpp
/* 486553 */
struct com::mojang::clacks::protocol::XuidDefaultTypeInternal
{
google::protobuf::internal::ExplicitlyConstructed<com::mojang::clacks::protocol::Xuid> _instance;
};

```
#### commands::Postfix
```cpp
/* 428725 */
struct commands::Postfix
{
const char *postfix;
};

```
#### commands::SoftEnum
```cpp
/* 426876 */
struct commands::SoftEnum
{
const char *name;
};

```
#### createUniqueRakPeer::$0DB58CF58EC7BF1F4DDADE930FB66FD4;
```cpp
/* 77651 */
struct createUniqueRakPeer::$0DB58CF58EC7BF1F4DDADE930FB66FD4;

```
#### curfile64_info
```cpp
/* 485438 */
struct curfile64_info
{
z_stream stream;
int stream_initialised;
uInt pos_in_buffered_data;
ZPOS64_T pos_local_header;
char *central_header;
uLong size_centralExtra;
uLong size_centralheader;
uLong size_centralExtraFree;
uLong flag;
int method;
int raw;
Byte buffered_data[65536];
uLong dosDate;
uLong crc32;
int encrypt;
int zip64;
ZPOS64_T pos_zip64extrainfo;
ZPOS64_T totalCompressedData;
ZPOS64_T totalUncompressedData;
};

```
#### curl_httppost;
```cpp
/* 485602 */
struct curl_httppost;

```
#### curl_slist;
```cpp
/* 485603 */
struct curl_slist;

```
