#### Objective
```cpp
/* 80244 */
struct Objective
{
std::unordered_map<ScoreboardId,int> mScores;
const std::string mName;
std::string mDisplayName;
const ObjectiveCriteria *mCriteria;
};

```
#### OceanFrozenBiomeSurface;
```cpp
/* 198712 */
struct OceanFrozenBiomeSurface;

```
#### OceanRuinConfiguration
```cpp
/* 41638 */
struct OceanRuinConfiguration
{
OceanTempCategory type;
float largeProbability;
float clusterProbability;
};

```
#### OceanRuinPieces
```cpp
/* 42258 */
struct OceanRuinPieces
{
__int8 gap0[1];
};

```
#### Ocelot::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124189 */
struct Ocelot::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Offer;
```cpp
/* 45317 */
struct Offer;

```
#### OnHitSubcomponent
```cpp
/* 57961 */
struct OnHitSubcomponent
{
int (**_vptr$OnHitSubcomponent)(void);
};

```
#### OpenDoorAnnotationComponent
```cpp
/* 57685 */
struct OpenDoorAnnotationComponent
{
std::queue<BlockPos> mPassedDoorPositions;
};

```
#### Option
```cpp
/* 45329 */
struct Option
{
int (**_vptr$Option)(void);
std::unique_ptr<OptionLock> mLock;
std::vector<OptionObserver> mObservers;
std::string mSaveTag;
std::string mTelemetryProperty;
const OptionID mID;
const OptionOwnerType mOwnerType;
OptionType mOptionType;
const std::string mCaptionId;
const OptionResetFlags mOptionResetFlags;
Option *mOverrideSource;
std::function<void (bool)> mRequestSaveCallback;
};

```
#### OptionLock
```cpp
/* 81365 */
struct OptionLock
{
std::function<bool ()> isModifiableCondition;
void *mToken;
};

```
#### OptionObserver
```cpp
/* 81355 */
struct OptionObserver
{
void *mToken;
ValueChangedCallback mOnValueChangeCallback;
InputModeValueChangedCallback mOnInputModeValueChangeCallback;
};

```
#### OptionalString
```cpp
/* 60801 */
struct OptionalString
{
bool valid;
std::string string;
};

```
#### Options;
```cpp
/* 43587 */
struct Options;

```
#### OverloadSyntaxInformation
```cpp
/* 92014 */
struct OverloadSyntaxInformation
{
std::string text;
OverloadSyntaxInformation::CursorPos start;
OverloadSyntaxInformation::CursorPos length;
};

```
#### OverworldGenerator::_makeLayers::$2867EA52F754A99BBF15CBCDF29DF3E2
```cpp
/* 40684 */
struct OverworldGenerator::_makeLayers::$2867EA52F754A99BBF15CBCDF29DF3E2
{
const BiomeRegistry *biomeRegistry;
};

```
#### OverworldHeightAttributes
```cpp
/* 193575 */
struct OverworldHeightAttributes
{
BiomeHeight mHeightParams;
};

```
#### OwnerStorageFeature
```cpp
/* 19404 */
struct OwnerStorageFeature
{
std::optional<std::reference_wrapper<FeatureRegistry> > mRegistry;
size_t mIndex;
};

```
#### OwnerStorageSharePtr<EntityRegistry>;
```cpp
/* 13164 */
struct OwnerStorageSharePtr<EntityRegistry>;

```
#### OwnerStorageSharePtr<EntityRegistryOwned>
```cpp
/* 13160 */
struct OwnerStorageSharePtr<EntityRegistryOwned>
{
std::shared_ptr<EntityRegistryOwned> mValue;
};

```
#### OwnerStorageSharePtr<PerlinSimplexNoise>
```cpp
/* 191375 */
struct OwnerStorageSharePtr<PerlinSimplexNoise>
{
std::shared_ptr<PerlinSimplexNoise> mValue;
};

```
#### Objective
```cpp
/* 80244 */
struct Objective
{
std::unordered_map<ScoreboardId,int> mScores;
const std::string mName;
std::string mDisplayName;
const ObjectiveCriteria *mCriteria;
};

```
#### OceanFrozenBiomeSurface;
```cpp
/* 198712 */
struct OceanFrozenBiomeSurface;

```
#### OceanRuinConfiguration
```cpp
/* 41638 */
struct OceanRuinConfiguration
{
OceanTempCategory type;
float largeProbability;
float clusterProbability;
};

```
#### OceanRuinPieces
```cpp
/* 42258 */
struct OceanRuinPieces
{
__int8 gap0[1];
};

```
#### Ocelot::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124189 */
struct Ocelot::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Offer;
```cpp
/* 45317 */
struct Offer;

```
#### OnHitSubcomponent
```cpp
/* 57961 */
struct OnHitSubcomponent
{
int (**_vptr$OnHitSubcomponent)(void);
};

```
#### OpenDoorAnnotationComponent
```cpp
/* 57685 */
struct OpenDoorAnnotationComponent
{
std::queue<BlockPos> mPassedDoorPositions;
};

```
#### Option
```cpp
/* 45329 */
struct Option
{
int (**_vptr$Option)(void);
std::unique_ptr<OptionLock> mLock;
std::vector<OptionObserver> mObservers;
std::string mSaveTag;
std::string mTelemetryProperty;
const OptionID mID;
const OptionOwnerType mOwnerType;
OptionType mOptionType;
const std::string mCaptionId;
const OptionResetFlags mOptionResetFlags;
Option *mOverrideSource;
std::function<void (bool)> mRequestSaveCallback;
};

```
#### OptionLock
```cpp
/* 81365 */
struct OptionLock
{
std::function<bool ()> isModifiableCondition;
void *mToken;
};

```
#### OptionObserver
```cpp
/* 81355 */
struct OptionObserver
{
void *mToken;
ValueChangedCallback mOnValueChangeCallback;
InputModeValueChangedCallback mOnInputModeValueChangeCallback;
};

```
#### OptionalString
```cpp
/* 60801 */
struct OptionalString
{
bool valid;
std::string string;
};

```
#### Options;
```cpp
/* 43587 */
struct Options;

```
#### OverloadSyntaxInformation
```cpp
/* 92014 */
struct OverloadSyntaxInformation
{
std::string text;
OverloadSyntaxInformation::CursorPos start;
OverloadSyntaxInformation::CursorPos length;
};

```
#### OverworldGenerator::_makeLayers::$2867EA52F754A99BBF15CBCDF29DF3E2
```cpp
/* 40684 */
struct OverworldGenerator::_makeLayers::$2867EA52F754A99BBF15CBCDF29DF3E2
{
const BiomeRegistry *biomeRegistry;
};

```
#### OverworldHeightAttributes
```cpp
/* 193575 */
struct OverworldHeightAttributes
{
BiomeHeight mHeightParams;
};

```
#### OwnerStorageFeature
```cpp
/* 19404 */
struct OwnerStorageFeature
{
std::optional<std::reference_wrapper<FeatureRegistry> > mRegistry;
size_t mIndex;
};

```
#### OwnerStorageSharePtr<EntityRegistry>;
```cpp
/* 13164 */
struct OwnerStorageSharePtr<EntityRegistry>;

```
#### OwnerStorageSharePtr<EntityRegistryOwned>
```cpp
/* 13160 */
struct OwnerStorageSharePtr<EntityRegistryOwned>
{
std::shared_ptr<EntityRegistryOwned> mValue;
};

```
#### OwnerStorageSharePtr<PerlinSimplexNoise>
```cpp
/* 191375 */
struct OwnerStorageSharePtr<PerlinSimplexNoise>
{
std::shared_ptr<PerlinSimplexNoise> mValue;
};

```
