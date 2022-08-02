#### JigsawBlockInfo
```cpp
/* 287330 */
struct JigsawBlockInfo
{
BlockPos mPos;
const Block *mBlock;
const Block *mFinalBlock;
std::string mAttachmentType;
std::string mTargetPool;
};

```
#### JigsawJunction
```cpp
/* 40688 */
struct JigsawJunction
{
BlockPos mSourceBlockPos;
int mDeltaSourceY;
int mDeltaTargetY;
Projection mSourceProjection;
Projection mTargetProjection;
};

```
#### JigsawStructureActorRulesRegistry
```cpp
/* 32824 */
struct JigsawStructureActorRulesRegistry
{
JigsawStructureActorRulesRegistry::ActorRulesRegistryMap mActorRulesRegistry;
JigsawStructureActorRulesRegistry::ActorRulesLookupMap mActorRuleLookupMap;
};

```
#### JigsawStructureBlockTagRulesRegistry
```cpp
/* 32821 */
struct JigsawStructureBlockTagRulesRegistry
{
JigsawStructureBlockTagRulesRegistry::BlockTagRulesRegistryMap mBlockTagRulesRegistry;
JigsawStructureBlockTagRulesRegistry::BlockTagRulesLookupMap mBlockTagRuleLookupMap;
};

```
#### JigsawStructureElementRegistry
```cpp
/* 32827 */
struct JigsawStructureElementRegistry
{
JigsawStructureElementRegistry::StructureElementRegistry mElementRegistry;
JigsawStructureElementRegistry::StructureElementLookupMap mElementLookupMap;
};

```
#### JigsawStructureRegistry
```cpp
/* 32816 */
struct JigsawStructureRegistry
{
JigsawStructureRegistry::JigsawPoolLookupMap mJigsawPoolLookupMap;
JigsawStructureBlockRulesRegistry mJigsawBlockRulesRegistry;
JigsawStructureBlockTagRulesRegistry mJigsawBlockTagRulesRegistry;
JigsawStructureActorRulesRegistry mJigsawActorRulesRegistry;
JigsawStructureElementRegistry mJigsawElementRegistry;
};

```
#### JsonValidator
```cpp
/* 83335 */
struct JsonValidator
{
__int8 gap0[1];
};

```
#### JsonValidator::Property
```cpp
/* 82820 */
struct JsonValidator::Property
{
std::vector<Json::ValueType> mTypes;
bool mIsRequired;
bool mRequiresConditionalProperty;
std::string mDescription;
JsonValidator::Property::PropertyPtr mChildProperty;
std::vector<std::pair<Json::Value,std::shared_ptr<JsonValidator::Property> >> mConditionalPropertiesByValue;
std::vector<std::pair<Json::ValueType,std::shared_ptr<JsonValidator::Property> >> mConditionalPropertiesByType;
std::unordered_map<std::string,std::shared_ptr<JsonValidator::Property>> mPropertyMap;
};

```
#### JsonValidator::generateDocs::DocumentationState
```cpp
/* 296398 */
struct JsonValidator::generateDocs::DocumentationState
{
const JsonValidator::Property *prop;
Json::Value *data;
};

```
#### JsonValidator::validate::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 296594 */
struct JsonValidator::validate::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### JsonValidator::validate::ValidationState
```cpp
/* 296326 */
struct JsonValidator::validate::ValidationState
{
const JsonValidator::Property *prop;
const Json::Value *data;
const Json::Value *parent;
bool checkType;
std::string name;
};

```
#### JukeboxBlockActor::tick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 238028 */
struct JukeboxBlockActor::tick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### JumpControlComponent
```cpp
/* 56476 */
struct JumpControlComponent
{
bool mJumping;
bool mSwimming;
float mJumpPower;
JumpType mJumpType;
JumpInfo mJumpInfo[4];
Unique<JumpControl> mJumpControl;
};

```
#### JumpInfo
```cpp
/* 56478 */
struct JumpInfo
{
int mAnimDuration;
int mJumpDelay;
float mDistanceScale;
float mHeight;
};

```
#### JigsawBlockInfo
```cpp
/* 287330 */
struct JigsawBlockInfo
{
BlockPos mPos;
const Block *mBlock;
const Block *mFinalBlock;
std::string mAttachmentType;
std::string mTargetPool;
};

```
#### JigsawJunction
```cpp
/* 40688 */
struct JigsawJunction
{
BlockPos mSourceBlockPos;
int mDeltaSourceY;
int mDeltaTargetY;
Projection mSourceProjection;
Projection mTargetProjection;
};

```
#### JigsawStructureActorRulesRegistry
```cpp
/* 32824 */
struct JigsawStructureActorRulesRegistry
{
JigsawStructureActorRulesRegistry::ActorRulesRegistryMap mActorRulesRegistry;
JigsawStructureActorRulesRegistry::ActorRulesLookupMap mActorRuleLookupMap;
};

```
#### JigsawStructureBlockTagRulesRegistry
```cpp
/* 32821 */
struct JigsawStructureBlockTagRulesRegistry
{
JigsawStructureBlockTagRulesRegistry::BlockTagRulesRegistryMap mBlockTagRulesRegistry;
JigsawStructureBlockTagRulesRegistry::BlockTagRulesLookupMap mBlockTagRuleLookupMap;
};

```
#### JigsawStructureElementRegistry
```cpp
/* 32827 */
struct JigsawStructureElementRegistry
{
JigsawStructureElementRegistry::StructureElementRegistry mElementRegistry;
JigsawStructureElementRegistry::StructureElementLookupMap mElementLookupMap;
};

```
#### JigsawStructureRegistry
```cpp
/* 32816 */
struct JigsawStructureRegistry
{
JigsawStructureRegistry::JigsawPoolLookupMap mJigsawPoolLookupMap;
JigsawStructureBlockRulesRegistry mJigsawBlockRulesRegistry;
JigsawStructureBlockTagRulesRegistry mJigsawBlockTagRulesRegistry;
JigsawStructureActorRulesRegistry mJigsawActorRulesRegistry;
JigsawStructureElementRegistry mJigsawElementRegistry;
};

```
#### JsonValidator
```cpp
/* 83335 */
struct JsonValidator
{
__int8 gap0[1];
};

```
#### JsonValidator::Property
```cpp
/* 82820 */
struct JsonValidator::Property
{
std::vector<Json::ValueType> mTypes;
bool mIsRequired;
bool mRequiresConditionalProperty;
std::string mDescription;
JsonValidator::Property::PropertyPtr mChildProperty;
std::vector<std::pair<Json::Value,std::shared_ptr<JsonValidator::Property> >> mConditionalPropertiesByValue;
std::vector<std::pair<Json::ValueType,std::shared_ptr<JsonValidator::Property> >> mConditionalPropertiesByType;
std::unordered_map<std::string,std::shared_ptr<JsonValidator::Property>> mPropertyMap;
};

```
#### JsonValidator::generateDocs::DocumentationState
```cpp
/* 296398 */
struct JsonValidator::generateDocs::DocumentationState
{
const JsonValidator::Property *prop;
Json::Value *data;
};

```
#### JsonValidator::validate::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 296594 */
struct JsonValidator::validate::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### JsonValidator::validate::ValidationState
```cpp
/* 296326 */
struct JsonValidator::validate::ValidationState
{
const JsonValidator::Property *prop;
const Json::Value *data;
const Json::Value *parent;
bool checkType;
std::string name;
};

```
#### JukeboxBlockActor::tick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 238028 */
struct JukeboxBlockActor::tick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### JumpControlComponent
```cpp
/* 56476 */
struct JumpControlComponent
{
bool mJumping;
bool mSwimming;
float mJumpPower;
JumpType mJumpType;
JumpInfo mJumpInfo[4];
Unique<JumpControl> mJumpControl;
};

```
#### JumpInfo
```cpp
/* 56478 */
struct JumpInfo
{
int mAnimDuration;
int mJumpDelay;
float mDistanceScale;
float mHeight;
};

```
