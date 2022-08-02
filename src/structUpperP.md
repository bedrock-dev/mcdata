#### Pack
```cpp
/* 4192 */
struct Pack
{
std::unique_ptr<PackManifest> mManifest;
std::unique_ptr<PackAccessStrategy> mAccessStrategy;
std::unique_ptr<SubpackInfoCollection> mSubpackInfoStack;
std::unique_ptr<PackMetadata> mMetadata;
std::map<void *,std::function<void (Pack &)>> mPackUpdatedCallbacks;
std::map<void *,std::function<void (Pack &)>> mPackDeletedCallbacks;
};

```
#### PackAccessStrategy
```cpp
/* 3504 */
struct PackAccessStrategy
{
int (**_vptr$PackAccessStrategy)(void);
bool mAssetSetPopulated;
std::unordered_set<Core::PathBuffer<std::string >> mAssetSet;
};

```
#### PackAccessStrategyFactory
```cpp
/* 422545 */
struct PackAccessStrategyFactory
{
__int8 gap0[1];
};

```
#### PackContentItem;
```cpp
/* 422563 */
struct PackContentItem;

```
#### PackError
```cpp
/* 2150 */
struct PackError
{
int (**_vptr$PackError)(void);
std::vector<std::string> mErrorParameters;
int mErrorValue;
PackErrorType mPackErrorType;
};

```
#### PackErrorFactory
```cpp
/* 82213 */
struct PackErrorFactory
{
__int8 gap0[1];
};

```
#### PackInstanceId
```cpp
/* 2172 */
struct PackInstanceId
{
PackIdVersion mPackId;
std::string mSubpackName;
};

```
#### PackManifest::CapabilityRegisterer
```cpp
/* 81170 */
struct PackManifest::CapabilityRegisterer
{
__int8 gap0[1];
};

```
#### PackManifest::CapabilityRegistry
```cpp
/* 81156 */
struct PackManifest::CapabilityRegistry
{
std::unordered_set<std::string> mTrustedCapabilities;
std::unordered_set<std::string> mCapabilities;
};

```
#### PackManifestFactory
```cpp
/* 5702 */
struct PackManifestFactory
{
IPackTelemetry *mEventing;
};

```
#### PackMetadata
```cpp
/* 5709 */
struct PackMetadata
{
std::unique_ptr<EducationMetadata> mEducationMetadata;
};

```
#### PackMover
```cpp
/* 84124 */
struct PackMover
{
__int8 gap0[1];
};

```
#### PackSetting
```cpp
/* 43145 */
struct PackSetting
{
Json::Value *mValue;
std::vector<PackSettingObserver> mObservers;
};

```
#### PackSettingObserver
```cpp
/* 43158 */
struct PackSettingObserver
{
void *mToken;
PackSettingChangedCallback mChangeCallback;
};

```
#### PackSettings
```cpp
/* 2621 */
struct PackSettings
{
Json::Value mSettings;
std::unordered_map<std::string,PackSetting> mPackSettings;
};

```
#### PackSettingsFactory
```cpp
/* 3599 */
struct PackSettingsFactory
{
std::unordered_map<PackIdVersion,std::unique_ptr<PackSettings>> mPackSettings;
};

```
#### PackSettingsJsonValidator
```cpp
/* 102376 */
struct PackSettingsJsonValidator
{
__int8 gap0[1];
};

```
#### PackSettingsJsonValidator::getValidator::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 102377 */
struct PackSettingsJsonValidator::getValidator::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### PackSource
```cpp
/* 3913 */
struct PackSource
{
int (**_vptr$PackSource)(void);
};

```
#### PackSourceFactory
```cpp
/* 5704 */
struct PackSourceFactory
{
std::vector<std::unique_ptr<ContentCatalogPackSource>> mContentCatalogPackSources;
std::vector<std::unique_ptr<TreatmentPackSource>> mTreatmentPackSources;
std::vector<std::unique_ptr<DirectoryPackSource>> mDirectoryPackSources;
std::vector<std::unique_ptr<InPackagePackSource>> mInPackagePackSources;
std::vector<std::unique_ptr<WorldHistoryPackSource>> mWorldHistoryPackSources;
std::vector<std::unique_ptr<WorldTemplatePackSource>> mWorldTemplatePackSources;
PackSourceFactory::RealmsUnknownPackSources mRealmsUnknownPackSources;
std::shared_ptr<IInPackagePacks> mInPackagePacksProvider;
};

```
#### PackSourceFactory::RealmsUnknownPackSources
```cpp
/* 5705 */
struct PackSourceFactory::RealmsUnknownPackSources
{
std::unique_ptr<RealmsUnknownPackSource> realmsUnknownResourcePackSource;
std::unique_ptr<RealmsUnknownPackSource> realmsUnknownBehaviorPackSource;
};

```
#### PackSourceReport
```cpp
/* 3421 */
struct PackSourceReport
{
std::unordered_map<PackIdVersion,PackReport> mReports;
};

```
#### PackStats
```cpp
/* 4194 */
struct PackStats
{
uint32_t mOverriddenEntityCount;
uint32_t mCustomEntityCount;
uint32_t mCustomAnimationCount;
uint32_t mCustomEffectCount;
};

```
#### PacketHandlerDispatcherInstance<ActorEventPacket,false>
```cpp
/* 72458 */
struct PacketHandlerDispatcherInstance<ActorEventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ActorFallPacket,false>
```cpp
/* 72464 */
struct PacketHandlerDispatcherInstance<ActorFallPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ActorPickRequestPacket,false>
```cpp
/* 72456 */
struct PacketHandlerDispatcherInstance<ActorPickRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AddActorPacket,false>
```cpp
/* 72434 */
struct PacketHandlerDispatcherInstance<AddActorPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AddBehaviorTreePacket,false>
```cpp
/* 72521 */
struct PacketHandlerDispatcherInstance<AddBehaviorTreePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AddEntityPacket,false>
```cpp
/* 72435 */
struct PacketHandlerDispatcherInstance<AddEntityPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AddItemActorPacket,false>
```cpp
/* 72436 */
struct PacketHandlerDispatcherInstance<AddItemActorPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AddPaintingPacket,false>
```cpp
/* 72481 */
struct PacketHandlerDispatcherInstance<AddPaintingPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AddPlayerPacket,false>
```cpp
/* 72438 */
struct PacketHandlerDispatcherInstance<AddPlayerPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AdventureSettingsPacket,false>
```cpp
/* 72482 */
struct PacketHandlerDispatcherInstance<AdventureSettingsPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AnimatePacket,false>
```cpp
/* 72470 */
struct PacketHandlerDispatcherInstance<AnimatePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AnvilDamagePacket,false>
```cpp
/* 72558 */
struct PacketHandlerDispatcherInstance<AnvilDamagePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AutomationClientConnectPacket,false>
```cpp
/* 72536 */
struct PacketHandlerDispatcherInstance<AutomationClientConnectPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AvailableActorIdentifiersPacket,false>
```cpp
/* 72551 */
struct PacketHandlerDispatcherInstance<AvailableActorIdentifiersPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AvailableCommandsPacket,false>
```cpp
/* 72506 */
struct PacketHandlerDispatcherInstance<AvailableCommandsPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<BiomeDefinitionListPacket,false>
```cpp
/* 72550 */
struct PacketHandlerDispatcherInstance<BiomeDefinitionListPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<BlockActorDataPacket,true>
```cpp
/* 72484 */
struct PacketHandlerDispatcherInstance<BlockActorDataPacket,true>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<BlockEventPacket,false>
```cpp
/* 72454 */
struct PacketHandlerDispatcherInstance<BlockEventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<BlockPickRequestPacket,false>
```cpp
/* 72455 */
struct PacketHandlerDispatcherInstance<BlockPickRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<BookEditPacket,false>
```cpp
/* 72534 */
struct PacketHandlerDispatcherInstance<BookEditPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<BossEventPacket,false>
```cpp
/* 72505 */
struct PacketHandlerDispatcherInstance<BossEventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<CameraPacket,false>
```cpp
/* 72510 */
struct PacketHandlerDispatcherInstance<CameraPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ChangeDimensionPacket,false>
```cpp
/* 72490 */
struct PacketHandlerDispatcherInstance<ChangeDimensionPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ChunkRadiusUpdatedPacket,false>
```cpp
/* 72499 */
struct PacketHandlerDispatcherInstance<ChunkRadiusUpdatedPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ClientCacheBlobStatusPacket,false>
```cpp
/* 72425 */
struct PacketHandlerDispatcherInstance<ClientCacheBlobStatusPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ClientCacheMissResponsePacket,true>
```cpp
/* 72426 */
struct PacketHandlerDispatcherInstance<ClientCacheMissResponsePacket,true>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ClientCacheStatusPacket,false>
```cpp
/* 72424 */
struct PacketHandlerDispatcherInstance<ClientCacheStatusPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ClientToServerHandshakePacket,false>
```cpp
/* 72423 */
struct PacketHandlerDispatcherInstance<ClientToServerHandshakePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ClientboundMapItemDataPacket,false>
```cpp
/* 72500 */
struct PacketHandlerDispatcherInstance<ClientboundMapItemDataPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<CommandBlockUpdatePacket,false>
```cpp
/* 72509 */
struct PacketHandlerDispatcherInstance<CommandBlockUpdatePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<CommandOutputPacket,false>
```cpp
/* 72508 */
struct PacketHandlerDispatcherInstance<CommandOutputPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<CommandRequestPacket,false>
```cpp
/* 72507 */
struct PacketHandlerDispatcherInstance<CommandRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<CompletedUsingItemPacket,false>
```cpp
/* 72562 */
struct PacketHandlerDispatcherInstance<CompletedUsingItemPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ContainerClosePacket,false>
```cpp
/* 72474 */
struct PacketHandlerDispatcherInstance<ContainerClosePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ContainerOpenPacket,false>
```cpp
/* 72473 */
struct PacketHandlerDispatcherInstance<ContainerOpenPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ContainerSetDataPacket,false>
```cpp
/* 72475 */
struct PacketHandlerDispatcherInstance<ContainerSetDataPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<CraftingDataPacket,false>
```cpp
/* 72479 */
struct PacketHandlerDispatcherInstance<CraftingDataPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<CraftingEventPacket,false>
```cpp
/* 72480 */
struct PacketHandlerDispatcherInstance<CraftingEventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<DisconnectPacket,false>
```cpp
/* 72430 */
struct PacketHandlerDispatcherInstance<DisconnectPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<EducationSettingsPacket,false>
```cpp
/* 72554 */
struct PacketHandlerDispatcherInstance<EducationSettingsPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<EmotePacket,false>
```cpp
/* 72556 */
struct PacketHandlerDispatcherInstance<EmotePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<EventPacket,false>
```cpp
/* 72496 */
struct PacketHandlerDispatcherInstance<EventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<GameRulesChangedPacket,false>
```cpp
/* 72511 */
struct PacketHandlerDispatcherInstance<GameRulesChangedPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<GuiDataPickItemPacket,false>
```cpp
/* 72457 */
struct PacketHandlerDispatcherInstance<GuiDataPickItemPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<HurtArmorPacket,false>
```cpp
/* 72465 */
struct PacketHandlerDispatcherInstance<HurtArmorPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<InteractPacket,false>
```cpp
/* 72462 */
struct PacketHandlerDispatcherInstance<InteractPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<InventoryContentPacket,false>
```cpp
/* 72477 */
struct PacketHandlerDispatcherInstance<InventoryContentPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<InventorySlotPacket,false>
```cpp
/* 72478 */
struct PacketHandlerDispatcherInstance<InventorySlotPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<InventoryTransactionPacket,false>
```cpp
/* 72471 */
struct PacketHandlerDispatcherInstance<InventoryTransactionPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ItemFrameDropItemPacket,false>
```cpp
/* 72472 */
struct PacketHandlerDispatcherInstance<ItemFrameDropItemPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LabTablePacket,false>
```cpp
/* 72545 */
struct PacketHandlerDispatcherInstance<LabTablePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LecternUpdatePacket,false>
```cpp
/* 72552 */
struct PacketHandlerDispatcherInstance<LecternUpdatePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LevelChunkPacket,true>
```cpp
/* 72487 */
struct PacketHandlerDispatcherInstance<LevelChunkPacket,true>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LevelEventGenericPacket,false>
```cpp
/* 72453 */
struct PacketHandlerDispatcherInstance<LevelEventGenericPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LevelEventPacket,false>
```cpp
/* 72452 */
struct PacketHandlerDispatcherInstance<LevelEventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LevelSoundEventPacket,false>
```cpp
/* 72451 */
struct PacketHandlerDispatcherInstance<LevelSoundEventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LevelSoundEventPacketV1,false>
```cpp
/* 72450 */
struct PacketHandlerDispatcherInstance<LevelSoundEventPacketV1,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LevelSoundEventPacketV2,false>
```cpp
/* 72449 */
struct PacketHandlerDispatcherInstance<LevelSoundEventPacketV2,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LoginPacket,false>
```cpp
/* 72419 */
struct PacketHandlerDispatcherInstance<LoginPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MapCreateLockedCopyPacket,false>
```cpp
/* 72501 */
struct PacketHandlerDispatcherInstance<MapCreateLockedCopyPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MapInfoRequestPacket,false>
```cpp
/* 72502 */
struct PacketHandlerDispatcherInstance<MapInfoRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MobArmorEquipmentPacket,false>
```cpp
/* 72461 */
struct PacketHandlerDispatcherInstance<MobArmorEquipmentPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MobEffectPacket,false>
```cpp
/* 72459 */
struct PacketHandlerDispatcherInstance<MobEffectPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MobEquipmentPacket,false>
```cpp
/* 72460 */
struct PacketHandlerDispatcherInstance<MobEquipmentPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ModalFormRequestPacket,false>
```cpp
/* 72538 */
struct PacketHandlerDispatcherInstance<ModalFormRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ModalFormResponsePacket,false>
```cpp
/* 72539 */
struct PacketHandlerDispatcherInstance<ModalFormResponsePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MoveActorAbsolutePacket,false>
```cpp
/* 72439 */
struct PacketHandlerDispatcherInstance<MoveActorAbsolutePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MoveActorDeltaPacket,false>
```cpp
/* 72440 */
struct PacketHandlerDispatcherInstance<MoveActorDeltaPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MovePlayerPacket,false>
```cpp
/* 72441 */
struct PacketHandlerDispatcherInstance<MovePlayerPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MultiplayerSettingsPacket,false>
```cpp
/* 72557 */
struct PacketHandlerDispatcherInstance<MultiplayerSettingsPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<NetworkChunkPublisherUpdatePacket,false>
```cpp
/* 72516 */
struct PacketHandlerDispatcherInstance<NetworkChunkPublisherUpdatePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<NetworkSettingsPacket,false>
```cpp
/* 72560 */
struct PacketHandlerDispatcherInstance<NetworkSettingsPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<NetworkStackLatencyPacket,false>
```cpp
/* 72546 */
struct PacketHandlerDispatcherInstance<NetworkStackLatencyPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<NpcRequestPacket,false>
```cpp
/* 72535 */
struct PacketHandlerDispatcherInstance<NpcRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<OnScreenTextureAnimationPacket,false>
```cpp
/* 72540 */
struct PacketHandlerDispatcherInstance<OnScreenTextureAnimationPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PhotoTransferPacket,false>
```cpp
/* 72543 */
struct PacketHandlerDispatcherInstance<PhotoTransferPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PlaySoundPacket,false>
```cpp
/* 72523 */
struct PacketHandlerDispatcherInstance<PlaySoundPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PlayStatusPacket,false>
```cpp
/* 72421 */
struct PacketHandlerDispatcherInstance<PlayStatusPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PlayerActionPacket,false>
```cpp
/* 72463 */
struct PacketHandlerDispatcherInstance<PlayerActionPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PlayerAuthInputPacket,false>
```cpp
/* 72486 */
struct PacketHandlerDispatcherInstance<PlayerAuthInputPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PlayerHotbarPacket,false>
```cpp
/* 72476 */
struct PacketHandlerDispatcherInstance<PlayerHotbarPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PlayerInputPacket,false>
```cpp
/* 72485 */
struct PacketHandlerDispatcherInstance<PlayerInputPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PlayerListPacket,false>
```cpp
/* 72494 */
struct PacketHandlerDispatcherInstance<PlayerListPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PlayerSkinPacket,false>
```cpp
/* 72529 */
struct PacketHandlerDispatcherInstance<PlayerSkinPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PurchaseReceiptPacket,false>
```cpp
/* 72528 */
struct PacketHandlerDispatcherInstance<PurchaseReceiptPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<RemoveActorPacket,false>
```cpp
/* 72444 */
struct PacketHandlerDispatcherInstance<RemoveActorPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<RemoveEntityPacket,false>
```cpp
/* 72445 */
struct PacketHandlerDispatcherInstance<RemoveEntityPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<RemoveObjectivePacket,false>
```cpp
/* 72526 */
struct PacketHandlerDispatcherInstance<RemoveObjectivePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<RequestChunkRadiusPacket,false>
```cpp
/* 72498 */
struct PacketHandlerDispatcherInstance<RequestChunkRadiusPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ResourcePackChunkDataPacket,false>
```cpp
/* 72514 */
struct PacketHandlerDispatcherInstance<ResourcePackChunkDataPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ResourcePackChunkRequestPacket,false>
```cpp
/* 72515 */
struct PacketHandlerDispatcherInstance<ResourcePackChunkRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ResourcePackClientResponsePacket,false>
```cpp
/* 72429 */
struct PacketHandlerDispatcherInstance<ResourcePackClientResponsePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ResourcePackDataInfoPacket,false>
```cpp
/* 72513 */
struct PacketHandlerDispatcherInstance<ResourcePackDataInfoPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ResourcePackStackPacket,false>
```cpp
/* 72428 */
struct PacketHandlerDispatcherInstance<ResourcePackStackPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ResourcePacksInfoPacket,false>
```cpp
/* 72427 */
struct PacketHandlerDispatcherInstance<ResourcePacksInfoPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<RespawnPacket,false>
```cpp
/* 72443 */
struct PacketHandlerDispatcherInstance<RespawnPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<RiderJumpPacket,false>
```cpp
/* 72442 */
struct PacketHandlerDispatcherInstance<RiderJumpPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ScriptCustomEventPacket,false>
```cpp
/* 72549 */
struct PacketHandlerDispatcherInstance<ScriptCustomEventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ServerSettingsRequestPacket,false>
```cpp
/* 72541 */
struct PacketHandlerDispatcherInstance<ServerSettingsRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ServerSettingsResponsePacket,false>
```cpp
/* 72542 */
struct PacketHandlerDispatcherInstance<ServerSettingsResponsePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ServerToClientHandshakePacket,false>
```cpp
/* 72422 */
struct PacketHandlerDispatcherInstance<ServerToClientHandshakePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetActorDataPacket,false>
```cpp
/* 72466 */
struct PacketHandlerDispatcherInstance<SetActorDataPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetActorLinkPacket,false>
```cpp
/* 72483 */
struct PacketHandlerDispatcherInstance<SetActorLinkPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetActorMotionPacket,false>
```cpp
/* 72467 */
struct PacketHandlerDispatcherInstance<SetActorMotionPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetCommandsEnabledPacket,false>
```cpp
/* 72488 */
struct PacketHandlerDispatcherInstance<SetCommandsEnabledPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetDefaultGameTypePacket,false>
```cpp
/* 72492 */
struct PacketHandlerDispatcherInstance<SetDefaultGameTypePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetDifficultyPacket,false>
```cpp
/* 72489 */
struct PacketHandlerDispatcherInstance<SetDifficultyPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetDisplayObjectivePacket,false>
```cpp
/* 72527 */
struct PacketHandlerDispatcherInstance<SetDisplayObjectivePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetHealthPacket,false>
```cpp
/* 72468 */
struct PacketHandlerDispatcherInstance<SetHealthPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetLastHurtByPacket,false>
```cpp
/* 72533 */
struct PacketHandlerDispatcherInstance<SetLastHurtByPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetLocalPlayerAsInitializedPacket,false>
```cpp
/* 72548 */
struct PacketHandlerDispatcherInstance<SetLocalPlayerAsInitializedPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetPlayerGameTypePacket,false>
```cpp
/* 72491 */
struct PacketHandlerDispatcherInstance<SetPlayerGameTypePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetScorePacket,false>
```cpp
/* 72530 */
struct PacketHandlerDispatcherInstance<SetScorePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetScoreboardIdentityPacket,false>
```cpp
/* 72531 */
struct PacketHandlerDispatcherInstance<SetScoreboardIdentityPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetSpawnPositionPacket,false>
```cpp
/* 72469 */
struct PacketHandlerDispatcherInstance<SetSpawnPositionPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetTimePacket,false>
```cpp
/* 72431 */
struct PacketHandlerDispatcherInstance<SetTimePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetTitlePacket,false>
```cpp
/* 72522 */
struct PacketHandlerDispatcherInstance<SetTitlePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SettingsCommandPacket,false>
```cpp
/* 72555 */
struct PacketHandlerDispatcherInstance<SettingsCommandPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ShowCreditsPacket,false>
```cpp
/* 72512 */
struct PacketHandlerDispatcherInstance<ShowCreditsPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ShowProfilePacket,false>
```cpp
/* 72544 */
struct PacketHandlerDispatcherInstance<ShowProfilePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ShowStoreOfferPacket,false>
```cpp
/* 72525 */
struct PacketHandlerDispatcherInstance<ShowStoreOfferPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SimpleEventPacket,false>
```cpp
/* 72495 */
struct PacketHandlerDispatcherInstance<SimpleEventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SpawnExperienceOrbPacket,false>
```cpp
/* 72497 */
struct PacketHandlerDispatcherInstance<SpawnExperienceOrbPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SpawnParticleEffectPacket,false>
```cpp
/* 72448 */
struct PacketHandlerDispatcherInstance<SpawnParticleEffectPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<StartGamePacket,false>
```cpp
/* 72433 */
struct PacketHandlerDispatcherInstance<StartGamePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<StopSoundPacket,false>
```cpp
/* 72524 */
struct PacketHandlerDispatcherInstance<StopSoundPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<StructureBlockUpdatePacket,false>
```cpp
/* 72517 */
struct PacketHandlerDispatcherInstance<StructureBlockUpdatePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<StructureTemplateDataRequestPacket,false>
```cpp
/* 72518 */
struct PacketHandlerDispatcherInstance<StructureTemplateDataRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<StructureTemplateDataResponsePacket,false>
```cpp
/* 72519 */
struct PacketHandlerDispatcherInstance<StructureTemplateDataResponsePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SubClientLoginPacket,false>
```cpp
/* 72532 */
struct PacketHandlerDispatcherInstance<SubClientLoginPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<TakeItemActorPacket,false>
```cpp
/* 72437 */
struct PacketHandlerDispatcherInstance<TakeItemActorPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<TextPacket,false>
```cpp
/* 72432 */
struct PacketHandlerDispatcherInstance<TextPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<TickSyncPacket,false>
```cpp
/* 72559 */
struct PacketHandlerDispatcherInstance<TickSyncPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<TransferPacket,false>
```cpp
/* 72520 */
struct PacketHandlerDispatcherInstance<TransferPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<UpdateAttributesPacket,false>
```cpp
/* 72493 */
struct PacketHandlerDispatcherInstance<UpdateAttributesPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<UpdateBlockPacket,true>
```cpp
/* 72446 */
struct PacketHandlerDispatcherInstance<UpdateBlockPacket,true>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<UpdateBlockPropertiesPacket,false>
```cpp
/* 72553 */
struct PacketHandlerDispatcherInstance<UpdateBlockPropertiesPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<UpdateBlockSyncedPacket,true>
```cpp
/* 72447 */
struct PacketHandlerDispatcherInstance<UpdateBlockSyncedPacket,true>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<UpdateEquipPacket,false>
```cpp
/* 72504 */
struct PacketHandlerDispatcherInstance<UpdateEquipPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<UpdateSoftEnumPacket,false>
```cpp
/* 72547 */
struct PacketHandlerDispatcherInstance<UpdateSoftEnumPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<UpdateTradePacket,false>
```cpp
/* 72503 */
struct PacketHandlerDispatcherInstance<UpdateTradePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<VideoStreamConnectPacket,false>
```cpp
/* 72537 */
struct PacketHandlerDispatcherInstance<VideoStreamConnectPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHeader
```cpp
/* 63705 */
struct PacketHeader
{
PacketHeader::$1CBC6A59FA6FE466C7E4A934B3AAA5AD mData;
};

```
#### PacketHeader::$1CBC6A59FA6FE466C7E4A934B3AAA5AD::$51D560F567CE4629B2B28E9C1CA63A03
```cpp
/* 63707 */
struct PacketHeader::$1CBC6A59FA6FE466C7E4A934B3AAA5AD::$51D560F567CE4629B2B28E9C1CA63A03
{
unsigned __int32 mPacketId : 10;
unsigned __int32 mSenderSubId : 2;
unsigned __int32 mClientSubId : 2;
};

```
#### PacketObserver
```cpp
/* 8632 */
struct PacketObserver
{
int (**_vptr$PacketObserver)(void);
};

```
#### PageContent
```cpp
/* 77462 */
struct PageContent
{
std::string mText;
std::string mParsedText;
std::string mPhotoName;
};

```
#### Palette
```cpp
/* 430572 */
struct Palette
{
__int8 gap0[1];
};

```
#### Parser
```cpp
/* 48705 */
struct Parser
{
__int8 gap0[1];
};

```
#### Particle;
```cpp
/* 35039 */
struct Particle;

```
#### ParticleTypeMap
```cpp
/* 452106 */
struct ParticleTypeMap
{
__int8 gap0[1];
};

```
#### ParticlesBlockExplosionEvent
```cpp
/* 457300 */
struct ParticlesBlockExplosionEvent
{
float mRadius;
Vec3 mOrigin;
std::vector<Vec3> mPositions;
};

```
#### ParticlesTeleportTrailEvent
```cpp
/* 420880 */
struct ParticlesTeleportTrailEvent
{
Vec3 mStart;
Vec3 mEnd;
Vec2 mVariation;
float mDirScale;
int mCount;
};

```
#### Path::Node
```cpp
/* 57492 */
struct Path::Node
{
BlockPos pos;
NodeType type;
};

```
#### PathFinder
```cpp
/* 290114 */
struct PathFinder
{
BlockSource *mRegion;
BinaryHeap mOpenSet;
std::unordered_map<BlockPos,PathfinderNode> mNodes;
std::array<PathfinderNode *,32> mNeighbors;
bool mCanPassDoors;
bool mCanOpenDoors;
bool mAvoidWater;
bool mAvoidDamageBlocks;
bool mCanFloat;
bool mIsAmphibious;
bool mAvoidPortals;
bool mCanBreach;
bool mCanJump;
bool mEntityIsSwimmer;
bool mEntityIsFlyer;
bool mEntityIsFireImmune;
bool mEntityIsOnHotBlock;
bool mEntityIsWalker;
bool mEntityIsDoorOpener;
bool mEntityIsDoorBreaker;
bool mAllowBlockBreaking;
const PreferredPathDescription *mPathPrefs;
};

```
#### PathNavigation
```cpp
/* 56589 */
struct PathNavigation
{
int (**_vptr$PathNavigation)(void);
};

```
#### PatternEntry
```cpp
/* 255085 */
struct PatternEntry
{
const Block *mBlock;
PatternEntry::BlockEntryTester mBlockEntryTester;
};

```
#### PeekComponent
```cpp
/* 57831 */
struct PeekComponent
{
bool mHadTarget;
int mDuration;
};

```
#### PeekDefinition
```cpp
/* 57887 */
struct PeekDefinition
{
DefinitionTrigger mOnOpen;
DefinitionTrigger mOnClose;
DefinitionTrigger mOnTargetOpen;
};

```
#### PerfTimer::Node
```cpp
/* 102418 */
struct PerfTimer::Node
{
const char *name;
const char *function;
int line;
unsigned __int16 elementCount;
double inclusiveTime;
double startTime;
PerfTimer::Node *elements;
};

```
#### PerlinNoise
```cpp
/* 36162 */
struct PerlinNoise
{
const int mLevels;
const int mMinLevel;
std::vector<ImprovedNoise> mNoiseLevels;
};

```
#### PermissionsFile
```cpp
/* 2796 */
struct PermissionsFile
{
const Core::HeapPathBuffer mFilePath;
std::unordered_map<std::string,PlayerPermissionLevel> mPermissions;
};

```
#### PermissionsHandler
```cpp
/* 3287 */
struct PermissionsHandler
{
CommandPermissionLevel mCommandPermissions;
PlayerPermissionLevel mPlayerPermissions;
};

```
#### PersistentFlag;
```cpp
/* 109106 */
struct PersistentFlag;

```
#### Phantom::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 170999 */
struct Phantom::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### PhotoStorage
```cpp
/* 87736 */
struct PhotoStorage
{
Core::HeapPathBuffer mBaseDir;
Core::HeapPathBuffer mBookDir;
Core::HeapPathBuffer mPhotoDir;
Core::HeapPathBuffer mManifestDir;
std::unordered_set<std::string> mChecksums;
};

```
#### PhysicsDefinition
```cpp
/* 412109 */
struct PhysicsDefinition
{
bool mHasGravity;
bool mHasCollision;
};

```
#### Pillager::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 171009 */
struct Pillager::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### PillagerOutpostPieces
```cpp
/* 42404 */
struct PillagerOutpostPieces
{
__int8 gap0[1];
};

```
#### PingedCompatibleServer
```cpp
/* 73271 */
struct PingedCompatibleServer
{
std::string name;
std::string worldName;
GameType gameType;
int protocol;
std::string version;
int players;
int maxPlayers;
std::string originalAddress;
RakNet::SystemAddress address;
RakNet::TimeMS pingTime;
float pingLatency;
RakNet::RakNetGUID hostGuid;
};

```
#### PistonArmBlock::neighborChanged::$20F33069935F666947F060F39ADB7AD4
```cpp
/* 459616 */
struct PistonArmBlock::neighborChanged::$20F33069935F666947F060F39ADB7AD4
{
const BlockActor *blockActor;
BlockPos *pistonBasePos;
BlockSource *region;
const BlockPos *pos;
};

```
#### Player::CachedSpawnData
```cpp
/* 88613 */
struct Player::CachedSpawnData
{
DimensionType mRespawnDimensionId;
Vec3 mTeleportDestPos;
BlockPos mRespawnPosition;
bool mHasRespawnPosition;
BlockPos mSharedSpawnPosition;
bool mRespawnReady;
Vec3 mPlayerPos;
bool mIsForcedRespawn;
bool mIsAdventure;
bool mIsFlyingOrNotOverworld;
bool mPositionLoadedFromSave;
};

```
#### Player::Player::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 173076 */
struct Player::Player::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Player::checkNeedAutoJump::$6915C98F38B5DDADCE093124C9EFBE13
```cpp
/* 173079 */
struct Player::checkNeedAutoJump::$6915C98F38B5DDADCE093124C9EFBE13
{
BlockPos *obstacleBlockPos;
BlockSource *region;
AABB *bufferAABB;
Player *this;
float *obstacleHeight;
const AABB *playerAABB;
};

```
#### Player::checkNeedAutoJump::$B52B8B35601F6FAF57FCDEA392569712
```cpp
/* 173078 */
struct Player::checkNeedAutoJump::$B52B8B35601F6FAF57FCDEA392569712
{
BlockSource *region;
AABB *bufferAABB;
Player *this;
};

```
#### Player::take::$1BEE5056AEB754170F0D74900712D0BE
```cpp
/* 173077 */
struct Player::take::$1BEE5056AEB754170F0D74900712D0BE
{
Player *this;
};

```
#### Player::updateSkin::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 173080 */
struct Player::updateSkin::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### PlayerEventListener
```cpp
/* 10739 */
struct PlayerEventListener
{
int (**_vptr$PlayerEventListener)(void);
};

```
#### PlayerInteractionSystem
```cpp
/* 10282 */
struct PlayerInteractionSystem
{
std::vector<std::unique_ptr<PlayerInteractionSystem::InteractionMappingBase>> mInteractionMappings;
};

```
#### PlayerInteractionSystem::InteractionMappingBase
```cpp
/* 53893 */
struct PlayerInteractionSystem::InteractionMappingBase
{
int (**_vptr$InteractionMappingBase)(void);
};

```
#### PlayerInventoryProxy::SlotData
```cpp
/* 88614 */
struct PlayerInventoryProxy::SlotData
{
ContainerID mContainerId;
int mSlot;
};

```
#### PlayerListener;
```cpp
/* 88756 */
struct PlayerListener;

```
#### PlayerMovementTelemetryData
```cpp
/* 88583 */
struct PlayerMovementTelemetryData
{
int mCount;
float mTotalPosDelta;
float mMinPosDelta;
float mMaxPosDelta;
};

```
#### PlayerRespawnBlockRadiusRandomizer
```cpp
/* 88634 */
struct PlayerRespawnBlockRadiusRandomizer
{
uint32_t mSpawnRadius;
uint32_t mPossibleOrigins;
uint32_t mLargestPrime;
uint32_t mStartOrigin;
uint32_t mCurrentOrigin;
uint32_t mIterationCount;
};

```
#### PlayerRespawnRandomizer
```cpp
/* 88633 */
struct PlayerRespawnRandomizer
{
Random mRandom;
uint32_t mSpawnRadius;
uint32_t mSquaredRadius;
PlayerRespawnBlockRadiusRandomizer mPrimaryRandomizer;
PlayerRespawnBlockRadiusRandomizer mSecondaryRandomizer;
Vec3 mSpawnCenter;
Vec3 mPrimaryOffset;
Vec3 mPrimaryScale;
};

```
#### PlayerScoreboardId
```cpp
/* 70052 */
struct PlayerScoreboardId
{
int64_t mActorUniqueId;
};

```
#### PlayerStorageIds
```cpp
/* 77488 */
struct PlayerStorageIds
{
std::string MsaId;
std::string PlatformId;
std::string PlatformOnlineId;
std::string PlatformOfflineId;
std::string SelfSignedId;
std::string RandomClientId;
};

```
#### PortalBlock::animateTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 226772 */
struct PortalBlock::animateTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### PortalShape
```cpp
/* 190608 */
struct PortalShape
{
PortalAxis mAxis;
Facing::Name mRightDir;
Facing::Name mLeftDir;
int mNumPortalBlocks;
BlockPos mBottomLeft;
bool mBottomLeftValid;
int mHeight;
int mWidth;
};

```
#### Pos
```cpp
/* 5797 */
struct Pos
{
int x;
int y;
int z;
};

```
#### PostShoreEdgeTransformation;
```cpp
/* 40586 */
struct PostShoreEdgeTransformation;

```
#### PostprocessingManager
```cpp
/* 34355 */
struct PostprocessingManager
{
Bedrock::Threading::Mutex mManagerMutex;
std::unordered_set<ChunkPos> mAcquired;
};

```
#### PostprocessingManager::Owns
```cpp
/* 37056 */
struct PostprocessingManager::Owns
{
ChunkPos mPosition;
PostprocessingManager *mPpm;
};

```
#### PotionBrewing
```cpp
/* 77483 */
struct PotionBrewing
{
__int8 gap0[1];
};

```
#### PotionBrewing::Ingredient
```cpp
/* 76194 */
struct PotionBrewing::Ingredient
{
int mItemId;
int mData;
};

```
#### PotionBrewing::Mix<ItemInstance>
```cpp
/* 77484 */
struct PotionBrewing::Mix<ItemInstance>
{
ItemInstance mFrom;
PotionBrewing::Ingredient mIngredient;
ItemInstance mTo;
};

```
#### PotionBrewing::Mix<const Item &>
```cpp
/* 76229 */
struct PotionBrewing::Mix<const Item &>
{
const Item *mFrom;
PotionBrewing::Ingredient mIngredient;
const Item *mTo;
};

```
#### PotionMixDataEntry
```cpp
/* 75593 */
struct PotionMixDataEntry
{
int fromPotionId;
int reagentItemId;
int toPotionId;
};

```
#### PreHillsEdgeTransformation;
```cpp
/* 13150 */
struct PreHillsEdgeTransformation;

```
#### PrintStream;
```cpp
/* 61747 */
struct PrintStream;

```
#### ProfilerLite::NetworkStats
```cpp
/* 5538 */
struct ProfilerLite::NetworkStats
{
uint32_t sentPackets;
uint32_t sentBytes;
uint32_t receivedPackets;
uint32_t receivedBytes;
};

```
#### ProfilerLiteTelemetry
```cpp
/* 5516 */
struct ProfilerLiteTelemetry
{
float mAvgFps;
float mAvgServerSimTickTimeMS;
float mAvgClientSimTickTimeMS;
float mAvgBeginFrameTimeMS;
float mAvgInputTimeMS;
float mAvgRenderTimeMS;
float mAvgEndFrameTimeMS;
float mAvgRemainderTimePercent;
float mAvgUnaccountedTimePercent;
};

```
#### ProgressListener;
```cpp
/* 290484 */
struct ProgressListener;

```
#### ProjectileFactory
```cpp
/* 87903 */
struct ProjectileFactory
{
Level *mLevel;
};

```
#### PropertiesSettings
```cpp
/* 4777 */
struct PropertiesSettings
{
std::string mLevelSeed;
std::string mLevelName;
std::string mLevelType;
std::string mServerName;
NetworkAddress mRemoteServerCommunicationEndpoint;
NetworkAddress mClacksEndpoint;
uint16_t mServerPort;
uint16_t mServerPortv6;
int mMaxPlayers;
int mOpPermissionLevel;
std::string mDifficulty;
std::string mServerType;
std::string mGameMode;
std::string mLanguage;
std::string mServerId;
uint32_t mMaxThreads;
int mServerTickRange;
std::vector<std::string> mExtraTrustedKeys;
bool mUseWhitelist;
bool mIsOnlineMode;
bool mForceGameMode;
bool mAllowCheats;
bool mTexturePackRequired;
bool mUseMsaGamertagsOnly;
bool mIsContentLogFileEnabled;
int mMaxViewDistanceChunks;
std::chrono::minutes mMaxIdleTime;
std::string mDefaultPlayerPermissionLevel;
int mServerWakeupFrequency;
bool mServerAuthoritativeMovement;
float mPlayerMovementDistanceThreshold;
std::chrono::milliseconds mPlayerMovementDurationThreshold;
float mPlayerMovementScoreThreshold;
bool mShouldCorrectPlayerMovement;
float mWebsocketRetryTime;
bool mUseWebsocketEncryption;
uint16_t mCompressionThreshold;
std::unordered_map<std::string,std::string> mCustomProperties;
};

```
#### Pufferfish::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124388 */
struct Pufferfish::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### PushNotificationMessage
```cpp
/* 45337 */
struct PushNotificationMessage
{
PushNotificationType m_Type;
std::string m_Title;
std::string m_Description;
Json::Value m_PropertyBag;
};

```
#### PushableComponent
```cpp
/* 59229 */
struct PushableComponent
{
bool mIsPushable;
bool mIsPushableByPiston;
float mPushthrough;
};

```
#### Pack
```cpp
/* 4192 */
struct Pack
{
std::unique_ptr<PackManifest> mManifest;
std::unique_ptr<PackAccessStrategy> mAccessStrategy;
std::unique_ptr<SubpackInfoCollection> mSubpackInfoStack;
std::unique_ptr<PackMetadata> mMetadata;
std::map<void *,std::function<void (Pack &)>> mPackUpdatedCallbacks;
std::map<void *,std::function<void (Pack &)>> mPackDeletedCallbacks;
};

```
#### PackAccessStrategy
```cpp
/* 3504 */
struct PackAccessStrategy
{
int (**_vptr$PackAccessStrategy)(void);
bool mAssetSetPopulated;
std::unordered_set<Core::PathBuffer<std::string >> mAssetSet;
};

```
#### PackAccessStrategyFactory
```cpp
/* 422545 */
struct PackAccessStrategyFactory
{
__int8 gap0[1];
};

```
#### PackContentItem;
```cpp
/* 422563 */
struct PackContentItem;

```
#### PackError
```cpp
/* 2150 */
struct PackError
{
int (**_vptr$PackError)(void);
std::vector<std::string> mErrorParameters;
int mErrorValue;
PackErrorType mPackErrorType;
};

```
#### PackErrorFactory
```cpp
/* 82213 */
struct PackErrorFactory
{
__int8 gap0[1];
};

```
#### PackInstanceId
```cpp
/* 2172 */
struct PackInstanceId
{
PackIdVersion mPackId;
std::string mSubpackName;
};

```
#### PackManifest::CapabilityRegisterer
```cpp
/* 81170 */
struct PackManifest::CapabilityRegisterer
{
__int8 gap0[1];
};

```
#### PackManifest::CapabilityRegistry
```cpp
/* 81156 */
struct PackManifest::CapabilityRegistry
{
std::unordered_set<std::string> mTrustedCapabilities;
std::unordered_set<std::string> mCapabilities;
};

```
#### PackManifestFactory
```cpp
/* 5702 */
struct PackManifestFactory
{
IPackTelemetry *mEventing;
};

```
#### PackMetadata
```cpp
/* 5709 */
struct PackMetadata
{
std::unique_ptr<EducationMetadata> mEducationMetadata;
};

```
#### PackMover
```cpp
/* 84124 */
struct PackMover
{
__int8 gap0[1];
};

```
#### PackSetting
```cpp
/* 43145 */
struct PackSetting
{
Json::Value *mValue;
std::vector<PackSettingObserver> mObservers;
};

```
#### PackSettingObserver
```cpp
/* 43158 */
struct PackSettingObserver
{
void *mToken;
PackSettingChangedCallback mChangeCallback;
};

```
#### PackSettings
```cpp
/* 2621 */
struct PackSettings
{
Json::Value mSettings;
std::unordered_map<std::string,PackSetting> mPackSettings;
};

```
#### PackSettingsFactory
```cpp
/* 3599 */
struct PackSettingsFactory
{
std::unordered_map<PackIdVersion,std::unique_ptr<PackSettings>> mPackSettings;
};

```
#### PackSettingsJsonValidator
```cpp
/* 102376 */
struct PackSettingsJsonValidator
{
__int8 gap0[1];
};

```
#### PackSettingsJsonValidator::getValidator::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 102377 */
struct PackSettingsJsonValidator::getValidator::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### PackSource
```cpp
/* 3913 */
struct PackSource
{
int (**_vptr$PackSource)(void);
};

```
#### PackSourceFactory
```cpp
/* 5704 */
struct PackSourceFactory
{
std::vector<std::unique_ptr<ContentCatalogPackSource>> mContentCatalogPackSources;
std::vector<std::unique_ptr<TreatmentPackSource>> mTreatmentPackSources;
std::vector<std::unique_ptr<DirectoryPackSource>> mDirectoryPackSources;
std::vector<std::unique_ptr<InPackagePackSource>> mInPackagePackSources;
std::vector<std::unique_ptr<WorldHistoryPackSource>> mWorldHistoryPackSources;
std::vector<std::unique_ptr<WorldTemplatePackSource>> mWorldTemplatePackSources;
PackSourceFactory::RealmsUnknownPackSources mRealmsUnknownPackSources;
std::shared_ptr<IInPackagePacks> mInPackagePacksProvider;
};

```
#### PackSourceFactory::RealmsUnknownPackSources
```cpp
/* 5705 */
struct PackSourceFactory::RealmsUnknownPackSources
{
std::unique_ptr<RealmsUnknownPackSource> realmsUnknownResourcePackSource;
std::unique_ptr<RealmsUnknownPackSource> realmsUnknownBehaviorPackSource;
};

```
#### PackSourceReport
```cpp
/* 3421 */
struct PackSourceReport
{
std::unordered_map<PackIdVersion,PackReport> mReports;
};

```
#### PackStats
```cpp
/* 4194 */
struct PackStats
{
uint32_t mOverriddenEntityCount;
uint32_t mCustomEntityCount;
uint32_t mCustomAnimationCount;
uint32_t mCustomEffectCount;
};

```
#### PacketHandlerDispatcherInstance<ActorEventPacket,false>
```cpp
/* 72458 */
struct PacketHandlerDispatcherInstance<ActorEventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ActorFallPacket,false>
```cpp
/* 72464 */
struct PacketHandlerDispatcherInstance<ActorFallPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ActorPickRequestPacket,false>
```cpp
/* 72456 */
struct PacketHandlerDispatcherInstance<ActorPickRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AddActorPacket,false>
```cpp
/* 72434 */
struct PacketHandlerDispatcherInstance<AddActorPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AddBehaviorTreePacket,false>
```cpp
/* 72521 */
struct PacketHandlerDispatcherInstance<AddBehaviorTreePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AddEntityPacket,false>
```cpp
/* 72435 */
struct PacketHandlerDispatcherInstance<AddEntityPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AddItemActorPacket,false>
```cpp
/* 72436 */
struct PacketHandlerDispatcherInstance<AddItemActorPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AddPaintingPacket,false>
```cpp
/* 72481 */
struct PacketHandlerDispatcherInstance<AddPaintingPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AddPlayerPacket,false>
```cpp
/* 72438 */
struct PacketHandlerDispatcherInstance<AddPlayerPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AdventureSettingsPacket,false>
```cpp
/* 72482 */
struct PacketHandlerDispatcherInstance<AdventureSettingsPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AnimatePacket,false>
```cpp
/* 72470 */
struct PacketHandlerDispatcherInstance<AnimatePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AnvilDamagePacket,false>
```cpp
/* 72558 */
struct PacketHandlerDispatcherInstance<AnvilDamagePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AutomationClientConnectPacket,false>
```cpp
/* 72536 */
struct PacketHandlerDispatcherInstance<AutomationClientConnectPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AvailableActorIdentifiersPacket,false>
```cpp
/* 72551 */
struct PacketHandlerDispatcherInstance<AvailableActorIdentifiersPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<AvailableCommandsPacket,false>
```cpp
/* 72506 */
struct PacketHandlerDispatcherInstance<AvailableCommandsPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<BiomeDefinitionListPacket,false>
```cpp
/* 72550 */
struct PacketHandlerDispatcherInstance<BiomeDefinitionListPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<BlockActorDataPacket,true>
```cpp
/* 72484 */
struct PacketHandlerDispatcherInstance<BlockActorDataPacket,true>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<BlockEventPacket,false>
```cpp
/* 72454 */
struct PacketHandlerDispatcherInstance<BlockEventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<BlockPickRequestPacket,false>
```cpp
/* 72455 */
struct PacketHandlerDispatcherInstance<BlockPickRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<BookEditPacket,false>
```cpp
/* 72534 */
struct PacketHandlerDispatcherInstance<BookEditPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<BossEventPacket,false>
```cpp
/* 72505 */
struct PacketHandlerDispatcherInstance<BossEventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<CameraPacket,false>
```cpp
/* 72510 */
struct PacketHandlerDispatcherInstance<CameraPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ChangeDimensionPacket,false>
```cpp
/* 72490 */
struct PacketHandlerDispatcherInstance<ChangeDimensionPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ChunkRadiusUpdatedPacket,false>
```cpp
/* 72499 */
struct PacketHandlerDispatcherInstance<ChunkRadiusUpdatedPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ClientCacheBlobStatusPacket,false>
```cpp
/* 72425 */
struct PacketHandlerDispatcherInstance<ClientCacheBlobStatusPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ClientCacheMissResponsePacket,true>
```cpp
/* 72426 */
struct PacketHandlerDispatcherInstance<ClientCacheMissResponsePacket,true>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ClientCacheStatusPacket,false>
```cpp
/* 72424 */
struct PacketHandlerDispatcherInstance<ClientCacheStatusPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ClientToServerHandshakePacket,false>
```cpp
/* 72423 */
struct PacketHandlerDispatcherInstance<ClientToServerHandshakePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ClientboundMapItemDataPacket,false>
```cpp
/* 72500 */
struct PacketHandlerDispatcherInstance<ClientboundMapItemDataPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<CommandBlockUpdatePacket,false>
```cpp
/* 72509 */
struct PacketHandlerDispatcherInstance<CommandBlockUpdatePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<CommandOutputPacket,false>
```cpp
/* 72508 */
struct PacketHandlerDispatcherInstance<CommandOutputPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<CommandRequestPacket,false>
```cpp
/* 72507 */
struct PacketHandlerDispatcherInstance<CommandRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<CompletedUsingItemPacket,false>
```cpp
/* 72562 */
struct PacketHandlerDispatcherInstance<CompletedUsingItemPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ContainerClosePacket,false>
```cpp
/* 72474 */
struct PacketHandlerDispatcherInstance<ContainerClosePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ContainerOpenPacket,false>
```cpp
/* 72473 */
struct PacketHandlerDispatcherInstance<ContainerOpenPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ContainerSetDataPacket,false>
```cpp
/* 72475 */
struct PacketHandlerDispatcherInstance<ContainerSetDataPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<CraftingDataPacket,false>
```cpp
/* 72479 */
struct PacketHandlerDispatcherInstance<CraftingDataPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<CraftingEventPacket,false>
```cpp
/* 72480 */
struct PacketHandlerDispatcherInstance<CraftingEventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<DisconnectPacket,false>
```cpp
/* 72430 */
struct PacketHandlerDispatcherInstance<DisconnectPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<EducationSettingsPacket,false>
```cpp
/* 72554 */
struct PacketHandlerDispatcherInstance<EducationSettingsPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<EmotePacket,false>
```cpp
/* 72556 */
struct PacketHandlerDispatcherInstance<EmotePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<EventPacket,false>
```cpp
/* 72496 */
struct PacketHandlerDispatcherInstance<EventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<GameRulesChangedPacket,false>
```cpp
/* 72511 */
struct PacketHandlerDispatcherInstance<GameRulesChangedPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<GuiDataPickItemPacket,false>
```cpp
/* 72457 */
struct PacketHandlerDispatcherInstance<GuiDataPickItemPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<HurtArmorPacket,false>
```cpp
/* 72465 */
struct PacketHandlerDispatcherInstance<HurtArmorPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<InteractPacket,false>
```cpp
/* 72462 */
struct PacketHandlerDispatcherInstance<InteractPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<InventoryContentPacket,false>
```cpp
/* 72477 */
struct PacketHandlerDispatcherInstance<InventoryContentPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<InventorySlotPacket,false>
```cpp
/* 72478 */
struct PacketHandlerDispatcherInstance<InventorySlotPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<InventoryTransactionPacket,false>
```cpp
/* 72471 */
struct PacketHandlerDispatcherInstance<InventoryTransactionPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ItemFrameDropItemPacket,false>
```cpp
/* 72472 */
struct PacketHandlerDispatcherInstance<ItemFrameDropItemPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LabTablePacket,false>
```cpp
/* 72545 */
struct PacketHandlerDispatcherInstance<LabTablePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LecternUpdatePacket,false>
```cpp
/* 72552 */
struct PacketHandlerDispatcherInstance<LecternUpdatePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LevelChunkPacket,true>
```cpp
/* 72487 */
struct PacketHandlerDispatcherInstance<LevelChunkPacket,true>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LevelEventGenericPacket,false>
```cpp
/* 72453 */
struct PacketHandlerDispatcherInstance<LevelEventGenericPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LevelEventPacket,false>
```cpp
/* 72452 */
struct PacketHandlerDispatcherInstance<LevelEventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LevelSoundEventPacket,false>
```cpp
/* 72451 */
struct PacketHandlerDispatcherInstance<LevelSoundEventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LevelSoundEventPacketV1,false>
```cpp
/* 72450 */
struct PacketHandlerDispatcherInstance<LevelSoundEventPacketV1,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LevelSoundEventPacketV2,false>
```cpp
/* 72449 */
struct PacketHandlerDispatcherInstance<LevelSoundEventPacketV2,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<LoginPacket,false>
```cpp
/* 72419 */
struct PacketHandlerDispatcherInstance<LoginPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MapCreateLockedCopyPacket,false>
```cpp
/* 72501 */
struct PacketHandlerDispatcherInstance<MapCreateLockedCopyPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MapInfoRequestPacket,false>
```cpp
/* 72502 */
struct PacketHandlerDispatcherInstance<MapInfoRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MobArmorEquipmentPacket,false>
```cpp
/* 72461 */
struct PacketHandlerDispatcherInstance<MobArmorEquipmentPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MobEffectPacket,false>
```cpp
/* 72459 */
struct PacketHandlerDispatcherInstance<MobEffectPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MobEquipmentPacket,false>
```cpp
/* 72460 */
struct PacketHandlerDispatcherInstance<MobEquipmentPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ModalFormRequestPacket,false>
```cpp
/* 72538 */
struct PacketHandlerDispatcherInstance<ModalFormRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ModalFormResponsePacket,false>
```cpp
/* 72539 */
struct PacketHandlerDispatcherInstance<ModalFormResponsePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MoveActorAbsolutePacket,false>
```cpp
/* 72439 */
struct PacketHandlerDispatcherInstance<MoveActorAbsolutePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MoveActorDeltaPacket,false>
```cpp
/* 72440 */
struct PacketHandlerDispatcherInstance<MoveActorDeltaPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MovePlayerPacket,false>
```cpp
/* 72441 */
struct PacketHandlerDispatcherInstance<MovePlayerPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<MultiplayerSettingsPacket,false>
```cpp
/* 72557 */
struct PacketHandlerDispatcherInstance<MultiplayerSettingsPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<NetworkChunkPublisherUpdatePacket,false>
```cpp
/* 72516 */
struct PacketHandlerDispatcherInstance<NetworkChunkPublisherUpdatePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<NetworkSettingsPacket,false>
```cpp
/* 72560 */
struct PacketHandlerDispatcherInstance<NetworkSettingsPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<NetworkStackLatencyPacket,false>
```cpp
/* 72546 */
struct PacketHandlerDispatcherInstance<NetworkStackLatencyPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<NpcRequestPacket,false>
```cpp
/* 72535 */
struct PacketHandlerDispatcherInstance<NpcRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<OnScreenTextureAnimationPacket,false>
```cpp
/* 72540 */
struct PacketHandlerDispatcherInstance<OnScreenTextureAnimationPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PhotoTransferPacket,false>
```cpp
/* 72543 */
struct PacketHandlerDispatcherInstance<PhotoTransferPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PlaySoundPacket,false>
```cpp
/* 72523 */
struct PacketHandlerDispatcherInstance<PlaySoundPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PlayStatusPacket,false>
```cpp
/* 72421 */
struct PacketHandlerDispatcherInstance<PlayStatusPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PlayerActionPacket,false>
```cpp
/* 72463 */
struct PacketHandlerDispatcherInstance<PlayerActionPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PlayerAuthInputPacket,false>
```cpp
/* 72486 */
struct PacketHandlerDispatcherInstance<PlayerAuthInputPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PlayerHotbarPacket,false>
```cpp
/* 72476 */
struct PacketHandlerDispatcherInstance<PlayerHotbarPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PlayerInputPacket,false>
```cpp
/* 72485 */
struct PacketHandlerDispatcherInstance<PlayerInputPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PlayerListPacket,false>
```cpp
/* 72494 */
struct PacketHandlerDispatcherInstance<PlayerListPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PlayerSkinPacket,false>
```cpp
/* 72529 */
struct PacketHandlerDispatcherInstance<PlayerSkinPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<PurchaseReceiptPacket,false>
```cpp
/* 72528 */
struct PacketHandlerDispatcherInstance<PurchaseReceiptPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<RemoveActorPacket,false>
```cpp
/* 72444 */
struct PacketHandlerDispatcherInstance<RemoveActorPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<RemoveEntityPacket,false>
```cpp
/* 72445 */
struct PacketHandlerDispatcherInstance<RemoveEntityPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<RemoveObjectivePacket,false>
```cpp
/* 72526 */
struct PacketHandlerDispatcherInstance<RemoveObjectivePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<RequestChunkRadiusPacket,false>
```cpp
/* 72498 */
struct PacketHandlerDispatcherInstance<RequestChunkRadiusPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ResourcePackChunkDataPacket,false>
```cpp
/* 72514 */
struct PacketHandlerDispatcherInstance<ResourcePackChunkDataPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ResourcePackChunkRequestPacket,false>
```cpp
/* 72515 */
struct PacketHandlerDispatcherInstance<ResourcePackChunkRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ResourcePackClientResponsePacket,false>
```cpp
/* 72429 */
struct PacketHandlerDispatcherInstance<ResourcePackClientResponsePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ResourcePackDataInfoPacket,false>
```cpp
/* 72513 */
struct PacketHandlerDispatcherInstance<ResourcePackDataInfoPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ResourcePackStackPacket,false>
```cpp
/* 72428 */
struct PacketHandlerDispatcherInstance<ResourcePackStackPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ResourcePacksInfoPacket,false>
```cpp
/* 72427 */
struct PacketHandlerDispatcherInstance<ResourcePacksInfoPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<RespawnPacket,false>
```cpp
/* 72443 */
struct PacketHandlerDispatcherInstance<RespawnPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<RiderJumpPacket,false>
```cpp
/* 72442 */
struct PacketHandlerDispatcherInstance<RiderJumpPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ScriptCustomEventPacket,false>
```cpp
/* 72549 */
struct PacketHandlerDispatcherInstance<ScriptCustomEventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ServerSettingsRequestPacket,false>
```cpp
/* 72541 */
struct PacketHandlerDispatcherInstance<ServerSettingsRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ServerSettingsResponsePacket,false>
```cpp
/* 72542 */
struct PacketHandlerDispatcherInstance<ServerSettingsResponsePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ServerToClientHandshakePacket,false>
```cpp
/* 72422 */
struct PacketHandlerDispatcherInstance<ServerToClientHandshakePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetActorDataPacket,false>
```cpp
/* 72466 */
struct PacketHandlerDispatcherInstance<SetActorDataPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetActorLinkPacket,false>
```cpp
/* 72483 */
struct PacketHandlerDispatcherInstance<SetActorLinkPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetActorMotionPacket,false>
```cpp
/* 72467 */
struct PacketHandlerDispatcherInstance<SetActorMotionPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetCommandsEnabledPacket,false>
```cpp
/* 72488 */
struct PacketHandlerDispatcherInstance<SetCommandsEnabledPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetDefaultGameTypePacket,false>
```cpp
/* 72492 */
struct PacketHandlerDispatcherInstance<SetDefaultGameTypePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetDifficultyPacket,false>
```cpp
/* 72489 */
struct PacketHandlerDispatcherInstance<SetDifficultyPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetDisplayObjectivePacket,false>
```cpp
/* 72527 */
struct PacketHandlerDispatcherInstance<SetDisplayObjectivePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetHealthPacket,false>
```cpp
/* 72468 */
struct PacketHandlerDispatcherInstance<SetHealthPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetLastHurtByPacket,false>
```cpp
/* 72533 */
struct PacketHandlerDispatcherInstance<SetLastHurtByPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetLocalPlayerAsInitializedPacket,false>
```cpp
/* 72548 */
struct PacketHandlerDispatcherInstance<SetLocalPlayerAsInitializedPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetPlayerGameTypePacket,false>
```cpp
/* 72491 */
struct PacketHandlerDispatcherInstance<SetPlayerGameTypePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetScorePacket,false>
```cpp
/* 72530 */
struct PacketHandlerDispatcherInstance<SetScorePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetScoreboardIdentityPacket,false>
```cpp
/* 72531 */
struct PacketHandlerDispatcherInstance<SetScoreboardIdentityPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetSpawnPositionPacket,false>
```cpp
/* 72469 */
struct PacketHandlerDispatcherInstance<SetSpawnPositionPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetTimePacket,false>
```cpp
/* 72431 */
struct PacketHandlerDispatcherInstance<SetTimePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SetTitlePacket,false>
```cpp
/* 72522 */
struct PacketHandlerDispatcherInstance<SetTitlePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SettingsCommandPacket,false>
```cpp
/* 72555 */
struct PacketHandlerDispatcherInstance<SettingsCommandPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ShowCreditsPacket,false>
```cpp
/* 72512 */
struct PacketHandlerDispatcherInstance<ShowCreditsPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ShowProfilePacket,false>
```cpp
/* 72544 */
struct PacketHandlerDispatcherInstance<ShowProfilePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<ShowStoreOfferPacket,false>
```cpp
/* 72525 */
struct PacketHandlerDispatcherInstance<ShowStoreOfferPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SimpleEventPacket,false>
```cpp
/* 72495 */
struct PacketHandlerDispatcherInstance<SimpleEventPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SpawnExperienceOrbPacket,false>
```cpp
/* 72497 */
struct PacketHandlerDispatcherInstance<SpawnExperienceOrbPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SpawnParticleEffectPacket,false>
```cpp
/* 72448 */
struct PacketHandlerDispatcherInstance<SpawnParticleEffectPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<StartGamePacket,false>
```cpp
/* 72433 */
struct PacketHandlerDispatcherInstance<StartGamePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<StopSoundPacket,false>
```cpp
/* 72524 */
struct PacketHandlerDispatcherInstance<StopSoundPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<StructureBlockUpdatePacket,false>
```cpp
/* 72517 */
struct PacketHandlerDispatcherInstance<StructureBlockUpdatePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<StructureTemplateDataRequestPacket,false>
```cpp
/* 72518 */
struct PacketHandlerDispatcherInstance<StructureTemplateDataRequestPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<StructureTemplateDataResponsePacket,false>
```cpp
/* 72519 */
struct PacketHandlerDispatcherInstance<StructureTemplateDataResponsePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<SubClientLoginPacket,false>
```cpp
/* 72532 */
struct PacketHandlerDispatcherInstance<SubClientLoginPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<TakeItemActorPacket,false>
```cpp
/* 72437 */
struct PacketHandlerDispatcherInstance<TakeItemActorPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<TextPacket,false>
```cpp
/* 72432 */
struct PacketHandlerDispatcherInstance<TextPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<TickSyncPacket,false>
```cpp
/* 72559 */
struct PacketHandlerDispatcherInstance<TickSyncPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<TransferPacket,false>
```cpp
/* 72520 */
struct PacketHandlerDispatcherInstance<TransferPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<UpdateAttributesPacket,false>
```cpp
/* 72493 */
struct PacketHandlerDispatcherInstance<UpdateAttributesPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<UpdateBlockPacket,true>
```cpp
/* 72446 */
struct PacketHandlerDispatcherInstance<UpdateBlockPacket,true>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<UpdateBlockPropertiesPacket,false>
```cpp
/* 72553 */
struct PacketHandlerDispatcherInstance<UpdateBlockPropertiesPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<UpdateBlockSyncedPacket,true>
```cpp
/* 72447 */
struct PacketHandlerDispatcherInstance<UpdateBlockSyncedPacket,true>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<UpdateEquipPacket,false>
```cpp
/* 72504 */
struct PacketHandlerDispatcherInstance<UpdateEquipPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<UpdateSoftEnumPacket,false>
```cpp
/* 72547 */
struct PacketHandlerDispatcherInstance<UpdateSoftEnumPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<UpdateTradePacket,false>
```cpp
/* 72503 */
struct PacketHandlerDispatcherInstance<UpdateTradePacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHandlerDispatcherInstance<VideoStreamConnectPacket,false>
```cpp
/* 72537 */
struct PacketHandlerDispatcherInstance<VideoStreamConnectPacket,false>
{
__int8 baseclass_0[8];
};

```
#### PacketHeader
```cpp
/* 63705 */
struct PacketHeader
{
PacketHeader::$1CBC6A59FA6FE466C7E4A934B3AAA5AD mData;
};

```
#### PacketHeader::$1CBC6A59FA6FE466C7E4A934B3AAA5AD::$51D560F567CE4629B2B28E9C1CA63A03
```cpp
/* 63707 */
struct PacketHeader::$1CBC6A59FA6FE466C7E4A934B3AAA5AD::$51D560F567CE4629B2B28E9C1CA63A03
{
unsigned __int32 mPacketId : 10;
unsigned __int32 mSenderSubId : 2;
unsigned __int32 mClientSubId : 2;
};

```
#### PacketObserver
```cpp
/* 8632 */
struct PacketObserver
{
int (**_vptr$PacketObserver)(void);
};

```
#### PageContent
```cpp
/* 77462 */
struct PageContent
{
std::string mText;
std::string mParsedText;
std::string mPhotoName;
};

```
#### Palette
```cpp
/* 430572 */
struct Palette
{
__int8 gap0[1];
};

```
#### Parser
```cpp
/* 48705 */
struct Parser
{
__int8 gap0[1];
};

```
#### Particle;
```cpp
/* 35039 */
struct Particle;

```
#### ParticleTypeMap
```cpp
/* 452106 */
struct ParticleTypeMap
{
__int8 gap0[1];
};

```
#### ParticlesBlockExplosionEvent
```cpp
/* 457300 */
struct ParticlesBlockExplosionEvent
{
float mRadius;
Vec3 mOrigin;
std::vector<Vec3> mPositions;
};

```
#### ParticlesTeleportTrailEvent
```cpp
/* 420880 */
struct ParticlesTeleportTrailEvent
{
Vec3 mStart;
Vec3 mEnd;
Vec2 mVariation;
float mDirScale;
int mCount;
};

```
#### Path::Node
```cpp
/* 57492 */
struct Path::Node
{
BlockPos pos;
NodeType type;
};

```
#### PathFinder
```cpp
/* 290114 */
struct PathFinder
{
BlockSource *mRegion;
BinaryHeap mOpenSet;
std::unordered_map<BlockPos,PathfinderNode> mNodes;
std::array<PathfinderNode *,32> mNeighbors;
bool mCanPassDoors;
bool mCanOpenDoors;
bool mAvoidWater;
bool mAvoidDamageBlocks;
bool mCanFloat;
bool mIsAmphibious;
bool mAvoidPortals;
bool mCanBreach;
bool mCanJump;
bool mEntityIsSwimmer;
bool mEntityIsFlyer;
bool mEntityIsFireImmune;
bool mEntityIsOnHotBlock;
bool mEntityIsWalker;
bool mEntityIsDoorOpener;
bool mEntityIsDoorBreaker;
bool mAllowBlockBreaking;
const PreferredPathDescription *mPathPrefs;
};

```
#### PathNavigation
```cpp
/* 56589 */
struct PathNavigation
{
int (**_vptr$PathNavigation)(void);
};

```
#### PatternEntry
```cpp
/* 255085 */
struct PatternEntry
{
const Block *mBlock;
PatternEntry::BlockEntryTester mBlockEntryTester;
};

```
#### PeekComponent
```cpp
/* 57831 */
struct PeekComponent
{
bool mHadTarget;
int mDuration;
};

```
#### PeekDefinition
```cpp
/* 57887 */
struct PeekDefinition
{
DefinitionTrigger mOnOpen;
DefinitionTrigger mOnClose;
DefinitionTrigger mOnTargetOpen;
};

```
#### PerfTimer::Node
```cpp
/* 102418 */
struct PerfTimer::Node
{
const char *name;
const char *function;
int line;
unsigned __int16 elementCount;
double inclusiveTime;
double startTime;
PerfTimer::Node *elements;
};

```
#### PerlinNoise
```cpp
/* 36162 */
struct PerlinNoise
{
const int mLevels;
const int mMinLevel;
std::vector<ImprovedNoise> mNoiseLevels;
};

```
#### PermissionsFile
```cpp
/* 2796 */
struct PermissionsFile
{
const Core::HeapPathBuffer mFilePath;
std::unordered_map<std::string,PlayerPermissionLevel> mPermissions;
};

```
#### PermissionsHandler
```cpp
/* 3287 */
struct PermissionsHandler
{
CommandPermissionLevel mCommandPermissions;
PlayerPermissionLevel mPlayerPermissions;
};

```
#### PersistentFlag;
```cpp
/* 109106 */
struct PersistentFlag;

```
#### Phantom::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 170999 */
struct Phantom::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### PhotoStorage
```cpp
/* 87736 */
struct PhotoStorage
{
Core::HeapPathBuffer mBaseDir;
Core::HeapPathBuffer mBookDir;
Core::HeapPathBuffer mPhotoDir;
Core::HeapPathBuffer mManifestDir;
std::unordered_set<std::string> mChecksums;
};

```
#### PhysicsDefinition
```cpp
/* 412109 */
struct PhysicsDefinition
{
bool mHasGravity;
bool mHasCollision;
};

```
#### Pillager::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 171009 */
struct Pillager::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### PillagerOutpostPieces
```cpp
/* 42404 */
struct PillagerOutpostPieces
{
__int8 gap0[1];
};

```
#### PingedCompatibleServer
```cpp
/* 73271 */
struct PingedCompatibleServer
{
std::string name;
std::string worldName;
GameType gameType;
int protocol;
std::string version;
int players;
int maxPlayers;
std::string originalAddress;
RakNet::SystemAddress address;
RakNet::TimeMS pingTime;
float pingLatency;
RakNet::RakNetGUID hostGuid;
};

```
#### PistonArmBlock::neighborChanged::$20F33069935F666947F060F39ADB7AD4
```cpp
/* 459616 */
struct PistonArmBlock::neighborChanged::$20F33069935F666947F060F39ADB7AD4
{
const BlockActor *blockActor;
BlockPos *pistonBasePos;
BlockSource *region;
const BlockPos *pos;
};

```
#### Player::CachedSpawnData
```cpp
/* 88613 */
struct Player::CachedSpawnData
{
DimensionType mRespawnDimensionId;
Vec3 mTeleportDestPos;
BlockPos mRespawnPosition;
bool mHasRespawnPosition;
BlockPos mSharedSpawnPosition;
bool mRespawnReady;
Vec3 mPlayerPos;
bool mIsForcedRespawn;
bool mIsAdventure;
bool mIsFlyingOrNotOverworld;
bool mPositionLoadedFromSave;
};

```
#### Player::Player::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 173076 */
struct Player::Player::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### Player::checkNeedAutoJump::$6915C98F38B5DDADCE093124C9EFBE13
```cpp
/* 173079 */
struct Player::checkNeedAutoJump::$6915C98F38B5DDADCE093124C9EFBE13
{
BlockPos *obstacleBlockPos;
BlockSource *region;
AABB *bufferAABB;
Player *this;
float *obstacleHeight;
const AABB *playerAABB;
};

```
#### Player::checkNeedAutoJump::$B52B8B35601F6FAF57FCDEA392569712
```cpp
/* 173078 */
struct Player::checkNeedAutoJump::$B52B8B35601F6FAF57FCDEA392569712
{
BlockSource *region;
AABB *bufferAABB;
Player *this;
};

```
#### Player::take::$1BEE5056AEB754170F0D74900712D0BE
```cpp
/* 173077 */
struct Player::take::$1BEE5056AEB754170F0D74900712D0BE
{
Player *this;
};

```
#### Player::updateSkin::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 173080 */
struct Player::updateSkin::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### PlayerEventListener
```cpp
/* 10739 */
struct PlayerEventListener
{
int (**_vptr$PlayerEventListener)(void);
};

```
#### PlayerInteractionSystem
```cpp
/* 10282 */
struct PlayerInteractionSystem
{
std::vector<std::unique_ptr<PlayerInteractionSystem::InteractionMappingBase>> mInteractionMappings;
};

```
#### PlayerInteractionSystem::InteractionMappingBase
```cpp
/* 53893 */
struct PlayerInteractionSystem::InteractionMappingBase
{
int (**_vptr$InteractionMappingBase)(void);
};

```
#### PlayerInventoryProxy::SlotData
```cpp
/* 88614 */
struct PlayerInventoryProxy::SlotData
{
ContainerID mContainerId;
int mSlot;
};

```
#### PlayerListener;
```cpp
/* 88756 */
struct PlayerListener;

```
#### PlayerMovementTelemetryData
```cpp
/* 88583 */
struct PlayerMovementTelemetryData
{
int mCount;
float mTotalPosDelta;
float mMinPosDelta;
float mMaxPosDelta;
};

```
#### PlayerRespawnBlockRadiusRandomizer
```cpp
/* 88634 */
struct PlayerRespawnBlockRadiusRandomizer
{
uint32_t mSpawnRadius;
uint32_t mPossibleOrigins;
uint32_t mLargestPrime;
uint32_t mStartOrigin;
uint32_t mCurrentOrigin;
uint32_t mIterationCount;
};

```
#### PlayerRespawnRandomizer
```cpp
/* 88633 */
struct PlayerRespawnRandomizer
{
Random mRandom;
uint32_t mSpawnRadius;
uint32_t mSquaredRadius;
PlayerRespawnBlockRadiusRandomizer mPrimaryRandomizer;
PlayerRespawnBlockRadiusRandomizer mSecondaryRandomizer;
Vec3 mSpawnCenter;
Vec3 mPrimaryOffset;
Vec3 mPrimaryScale;
};

```
#### PlayerScoreboardId
```cpp
/* 70052 */
struct PlayerScoreboardId
{
int64_t mActorUniqueId;
};

```
#### PlayerStorageIds
```cpp
/* 77488 */
struct PlayerStorageIds
{
std::string MsaId;
std::string PlatformId;
std::string PlatformOnlineId;
std::string PlatformOfflineId;
std::string SelfSignedId;
std::string RandomClientId;
};

```
#### PortalBlock::animateTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 226772 */
struct PortalBlock::animateTick::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### PortalShape
```cpp
/* 190608 */
struct PortalShape
{
PortalAxis mAxis;
Facing::Name mRightDir;
Facing::Name mLeftDir;
int mNumPortalBlocks;
BlockPos mBottomLeft;
bool mBottomLeftValid;
int mHeight;
int mWidth;
};

```
#### Pos
```cpp
/* 5797 */
struct Pos
{
int x;
int y;
int z;
};

```
#### PostShoreEdgeTransformation;
```cpp
/* 40586 */
struct PostShoreEdgeTransformation;

```
#### PostprocessingManager
```cpp
/* 34355 */
struct PostprocessingManager
{
Bedrock::Threading::Mutex mManagerMutex;
std::unordered_set<ChunkPos> mAcquired;
};

```
#### PostprocessingManager::Owns
```cpp
/* 37056 */
struct PostprocessingManager::Owns
{
ChunkPos mPosition;
PostprocessingManager *mPpm;
};

```
#### PotionBrewing
```cpp
/* 77483 */
struct PotionBrewing
{
__int8 gap0[1];
};

```
#### PotionBrewing::Ingredient
```cpp
/* 76194 */
struct PotionBrewing::Ingredient
{
int mItemId;
int mData;
};

```
#### PotionBrewing::Mix<ItemInstance>
```cpp
/* 77484 */
struct PotionBrewing::Mix<ItemInstance>
{
ItemInstance mFrom;
PotionBrewing::Ingredient mIngredient;
ItemInstance mTo;
};

```
#### PotionBrewing::Mix<const Item &>
```cpp
/* 76229 */
struct PotionBrewing::Mix<const Item &>
{
const Item *mFrom;
PotionBrewing::Ingredient mIngredient;
const Item *mTo;
};

```
#### PotionMixDataEntry
```cpp
/* 75593 */
struct PotionMixDataEntry
{
int fromPotionId;
int reagentItemId;
int toPotionId;
};

```
#### PreHillsEdgeTransformation;
```cpp
/* 13150 */
struct PreHillsEdgeTransformation;

```
#### PrintStream;
```cpp
/* 61747 */
struct PrintStream;

```
#### ProfilerLite::NetworkStats
```cpp
/* 5538 */
struct ProfilerLite::NetworkStats
{
uint32_t sentPackets;
uint32_t sentBytes;
uint32_t receivedPackets;
uint32_t receivedBytes;
};

```
#### ProfilerLiteTelemetry
```cpp
/* 5516 */
struct ProfilerLiteTelemetry
{
float mAvgFps;
float mAvgServerSimTickTimeMS;
float mAvgClientSimTickTimeMS;
float mAvgBeginFrameTimeMS;
float mAvgInputTimeMS;
float mAvgRenderTimeMS;
float mAvgEndFrameTimeMS;
float mAvgRemainderTimePercent;
float mAvgUnaccountedTimePercent;
};

```
#### ProgressListener;
```cpp
/* 290484 */
struct ProgressListener;

```
#### ProjectileFactory
```cpp
/* 87903 */
struct ProjectileFactory
{
Level *mLevel;
};

```
#### PropertiesSettings
```cpp
/* 4777 */
struct PropertiesSettings
{
std::string mLevelSeed;
std::string mLevelName;
std::string mLevelType;
std::string mServerName;
NetworkAddress mRemoteServerCommunicationEndpoint;
NetworkAddress mClacksEndpoint;
uint16_t mServerPort;
uint16_t mServerPortv6;
int mMaxPlayers;
int mOpPermissionLevel;
std::string mDifficulty;
std::string mServerType;
std::string mGameMode;
std::string mLanguage;
std::string mServerId;
uint32_t mMaxThreads;
int mServerTickRange;
std::vector<std::string> mExtraTrustedKeys;
bool mUseWhitelist;
bool mIsOnlineMode;
bool mForceGameMode;
bool mAllowCheats;
bool mTexturePackRequired;
bool mUseMsaGamertagsOnly;
bool mIsContentLogFileEnabled;
int mMaxViewDistanceChunks;
std::chrono::minutes mMaxIdleTime;
std::string mDefaultPlayerPermissionLevel;
int mServerWakeupFrequency;
bool mServerAuthoritativeMovement;
float mPlayerMovementDistanceThreshold;
std::chrono::milliseconds mPlayerMovementDurationThreshold;
float mPlayerMovementScoreThreshold;
bool mShouldCorrectPlayerMovement;
float mWebsocketRetryTime;
bool mUseWebsocketEncryption;
uint16_t mCompressionThreshold;
std::unordered_map<std::string,std::string> mCustomProperties;
};

```
#### Pufferfish::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
```cpp
/* 124388 */
struct Pufferfish::updateEntitySpecificMolangVariables::$7EF7C94BEAB75C6CEF4ADFB99B570420
{
__int8 gap0[1];
};

```
#### PushNotificationMessage
```cpp
/* 45337 */
struct PushNotificationMessage
{
PushNotificationType m_Type;
std::string m_Title;
std::string m_Description;
Json::Value m_PropertyBag;
};

```
#### PushableComponent
```cpp
/* 59229 */
struct PushableComponent
{
bool mIsPushable;
bool mIsPushableByPiston;
float mPushthrough;
};

```
