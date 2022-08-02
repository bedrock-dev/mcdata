#### sched_param
```cpp
/* 478091 */
struct sched_param
{
int sched_priority;
};

```
#### serialize<ActorLink>
```cpp
/* 77828 */
struct serialize<ActorLink>
{
__int8 gap0[1];
};

```
#### serialize<ActorRuntimeID>
```cpp
/* 77659 */
struct serialize<ActorRuntimeID>
{
__int8 gap0[1];
};

```
#### serialize<ActorUniqueID>
```cpp
/* 77824 */
struct serialize<ActorUniqueID>
{
__int8 gap0[1];
};

```
#### serialize<BaseGameVersion>
```cpp
/* 80298 */
struct serialize<BaseGameVersion>
{
__int8 gap0[1];
};

```
#### serialize<BlockPos>
```cpp
/* 78541 */
struct serialize<BlockPos>
{
__int8 gap0[1];
};

```
#### serialize<ChunkPos>
```cpp
/* 80004 */
struct serialize<ChunkPos>
{
__int8 gap0[1];
};

```
#### serialize<CommandOriginData>
```cpp
/* 78852 */
struct serialize<CommandOriginData>
{
__int8 gap0[1];
};

```
#### serialize<CompoundTag>
```cpp
/* 61748 */
struct serialize<CompoundTag>
{
__int8 gap0[1];
};

```
#### serialize<DataItem>
```cpp
/* 116856 */
struct serialize<DataItem>
{
__int8 gap0[1];
};

```
#### serialize<EducationLevelSettings>
```cpp
/* 79603 */
struct serialize<EducationLevelSettings>
{
__int8 gap0[1];
};

```
#### serialize<EducationLevelSettings>::write::$5D3ECE175654F4C4336B6523D3249746
```cpp
/* 186612 */
struct serialize<EducationLevelSettings>::write::$5D3ECE175654F4C4336B6523D3249746
{
const EducationLevelSettings *val;
};

```
#### serialize<EntityNetId>
```cpp
/* 79613 */
struct serialize<EntityNetId>
{
__int8 gap0[1];
};

```
#### serialize<GameRulesChangedPacketData>
```cpp
/* 79703 */
struct serialize<GameRulesChangedPacketData>
{
__int8 gap0[1];
};

```
#### serialize<IdentityDefinition::Type>
```cpp
/* 80475 */
struct serialize<IdentityDefinition::Type>
{
__int8 gap0[1];
};

```
#### serialize<InventoryAction>
```cpp
/* 79922 */
struct serialize<InventoryAction>
{
__int8 gap0[1];
};

```
#### serialize<InventorySource>
```cpp
/* 79923 */
struct serialize<InventorySource>
{
__int8 gap0[1];
};

```
#### serialize<InventoryTransaction>
```cpp
/* 79921 */
struct serialize<InventoryTransaction>
{
__int8 gap0[1];
};

```
#### serialize<ItemData>
```cpp
/* 80903 */
struct serialize<ItemData>
{
__int8 gap0[1];
};

```
#### serialize<ItemInstance>
```cpp
/* 81107 */
struct serialize<ItemInstance>
{
__int8 gap0[1];
};

```
#### serialize<ItemStack>
```cpp
/* 81106 */
struct serialize<ItemStack>
{
__int8 gap0[1];
};

```
#### serialize<LevelSettings>
```cpp
/* 80902 */
struct serialize<LevelSettings>
{
__int8 gap0[1];
};

```
#### serialize<MapDecoration>
```cpp
/* 78790 */
struct serialize<MapDecoration>
{
__int8 gap0[1];
};

```
#### serialize<MapItemTrackedActor::UniqueId>
```cpp
/* 78788 */
struct serialize<MapItemTrackedActor::UniqueId>
{
__int8 gap0[1];
};

```
#### serialize<MoveActorAbsoluteData>
```cpp
/* 80023 */
struct serialize<MoveActorAbsoluteData>
{
__int8 gap0[1];
};

```
#### serialize<MoveActorDeltaData>
```cpp
/* 80026 */
struct serialize<MoveActorDeltaData>
{
__int8 gap0[1];
};

```
#### serialize<NetworkBlockPosition>
```cpp
/* 77855 */
struct serialize<NetworkBlockPosition>
{
__int8 gap0[1];
};

```
#### serialize<RecipeIngredient>
```cpp
/* 184724 */
struct serialize<RecipeIngredient>
{
__int8 gap0[1];
};

```
#### serialize<ScoreboardId>
```cpp
/* 80474 */
struct serialize<ScoreboardId>
{
__int8 gap0[1];
};

```
#### serialize<ShapedChemistryRecipe>
```cpp
/* 79562 */
struct serialize<ShapedChemistryRecipe>
{
__int8 gap0[1];
};

```
#### serialize<ShapedRecipe>
```cpp
/* 79558 */
struct serialize<ShapedRecipe>
{
__int8 gap0[1];
};

```
#### serialize<ShapelessChemistryRecipe>
```cpp
/* 79561 */
struct serialize<ShapelessChemistryRecipe>
{
__int8 gap0[1];
};

```
#### serialize<ShapelessRecipe>
```cpp
/* 79559 */
struct serialize<ShapelessRecipe>
{
__int8 gap0[1];
};

```
#### serialize<ShulkerBoxRecipe>
```cpp
/* 79560 */
struct serialize<ShulkerBoxRecipe>
{
__int8 gap0[1];
};

```
#### serialize<StructureEditorData>
```cpp
/* 80912 */
struct serialize<StructureEditorData>
{
__int8 gap0[1];
};

```
#### serialize<StructureSettings>
```cpp
/* 80913 */
struct serialize<StructureSettings>
{
__int8 gap0[1];
};

```
#### serialize<Vec2>
```cpp
/* 77826 */
struct serialize<Vec2>
{
__int8 gap0[1];
};

```
#### serialize<Vec3>
```cpp
/* 77825 */
struct serialize<Vec3>
{
__int8 gap0[1];
};

```
#### serialize<mce::UUID>
```cpp
/* 77840 */
struct serialize<mce::UUID>
{
__int8 gap0[1];
};

```
#### sigaction
```cpp
/* 485724 */
struct sigaction
{
sigaction::$A264F945D93E77C42166F8517888D535 __sigaction_handler;
__sigset_t sa_mask;
int sa_flags;
void (*sa_restorer)(void);
};

```
#### siginfo_t
```cpp
/* 294326 */
struct siginfo_t
{
int si_signo;
int si_errno;
int si_code;
int __pad0;
siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A _sifields;
};

```
#### siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$1083567770C9944ECE9586E3D60D7164
```cpp
/* 294333 */
struct siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$1083567770C9944ECE9586E3D60D7164
{
__pid_t si_pid;
__uid_t si_uid;
__sigval_t si_sigval;
};

```
#### siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$269BD37B8033F496E0DA26224222815C
```cpp
/* 294334 */
struct siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$269BD37B8033F496E0DA26224222815C
{
__pid_t si_pid;
__uid_t si_uid;
int si_status;
__clock_t si_utime;
__clock_t si_stime;
};

```
#### siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$34A68472B6FD99AB74EBE1055AA656AE
```cpp
/* 294328 */
struct siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$34A68472B6FD99AB74EBE1055AA656AE
{
__pid_t si_pid;
__uid_t si_uid;
};

```
#### siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$5BF7061F11A02461448786E25380AC9A
```cpp
/* 294339 */
struct siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$5BF7061F11A02461448786E25380AC9A
{
void *_call_addr;
int _syscall;
unsigned int _arch;
};

```
#### siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$9E99AB014780417E3FB416F9C93D05FB
```cpp
/* 294335 */
struct siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$9E99AB014780417E3FB416F9C93D05FB
{
void *si_addr;
__int16 si_addr_lsb;
siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$9E99AB014780417E3FB416F9C93D05FB::$5BC825E6F32707B864090E1402CAE52B _bounds;
};

```
#### siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$9E99AB014780417E3FB416F9C93D05FB::$5BC825E6F32707B864090E1402CAE52B::$500E99076578AD283C95318D41ACB4BA
```cpp
/* 294337 */
struct siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$9E99AB014780417E3FB416F9C93D05FB::$5BC825E6F32707B864090E1402CAE52B::$500E99076578AD283C95318D41ACB4BA
{
void *_lower;
void *_upper;
};

```
#### siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$CCD53A48A999AABAD7234802D7894EC3
```cpp
/* 294330 */
struct siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$CCD53A48A999AABAD7234802D7894EC3
{
int si_tid;
int si_overrun;
__sigval_t si_sigval;
};

```
#### sockaddr
```cpp
/* 86249 */
struct sockaddr
{
sa_family_t sa_family;
char sa_data[14];
};

```
#### sockaddr_in
```cpp
/* 4275 */
struct sockaddr_in
{
sa_family_t sin_family;
in_port_t sin_port;
in_addr sin_addr;
unsigned __int8 sin_zero[8];
};

```
#### sockaddr_in6
```cpp
/* 4271 */
struct sockaddr_in6
{
sa_family_t sin6_family;
in_port_t sin6_port;
uint32_t sin6_flowinfo;
in6_addr sin6_addr;
uint32_t sin6_scope_id;
};

```
#### stack_t
```cpp
/* 485606 */
struct stack_t
{
void *ss_sp;
int ss_flags;
size_t ss_size;
};

```
#### start_timer_after_init_state;
```cpp
/* 486941 */
struct start_timer_after_init_state;

```
#### stat
```cpp
/* 483213 */
struct stat
{
__dev_t st_dev;
__ino_t st_ino;
__nlink_t st_nlink;
__mode_t st_mode;
__uid_t st_uid;
__gid_t st_gid;
int __pad0;
__dev_t st_rdev;
__off_t st_size;
__blksize_t st_blksize;
__blkcnt_t st_blocks;
timespec st_atim;
timespec st_mtim;
timespec st_ctim;
__syscall_slong_t __glibc_reserved[3];
};

```
#### static_vector<Actor *,1>
```cpp
/* 186241 */
struct static_vector<Actor *,1>
{
std::aligned_storage<8,8>::type mArray[1];
size_t mSize;
};

```
#### static_vector<Actor *,1>::const_iterator;
```cpp
/* 186243 */
struct static_vector<Actor *,1>::const_iterator;

```
#### static_vector<Actor *,1>::iterator;
```cpp
/* 186242 */
struct static_vector<Actor *,1>::iterator;

```
#### static_vector<const Block *,4096>
```cpp
/* 253608 */
struct static_vector<const Block *,4096>
{
std::aligned_storage<8,8>::type mArray[4096];
size_t mSize;
};

```
#### static_vector<const Block *,4096>::const_iterator;
```cpp
/* 253610 */
struct static_vector<const Block *,4096>::const_iterator;

```
#### static_vector<const Block *,4096>::iterator
```cpp
/* 253609 */
struct static_vector<const Block *,4096>::iterator
{
const Block **mPtr;
};

```
#### statvfs
```cpp
/* 42803 */
struct statvfs
{
unsigned __int64 f_bsize;
unsigned __int64 f_frsize;
__fsblkcnt_t f_blocks;
__fsblkcnt_t f_bfree;
__fsblkcnt_t f_bavail;
__fsfilcnt_t f_files;
__fsfilcnt_t f_ffree;
__fsfilcnt_t f_favail;
unsigned __int64 f_fsid;
unsigned __int64 f_flag;
unsigned __int64 f_namemax;
int __f_spare[6];
};

```
#### stdext::reference_wrapper<const Localization>
```cpp
/* 60810 */
struct stdext::reference_wrapper<const Localization>
{
const Localization *ptr;
};

```
#### stdext::reference_wrapper<int>;
```cpp
/* 5920 */
struct stdext::reference_wrapper<int>;

```
#### sched_param
```cpp
/* 478091 */
struct sched_param
{
int sched_priority;
};

```
#### serialize<ActorLink>
```cpp
/* 77828 */
struct serialize<ActorLink>
{
__int8 gap0[1];
};

```
#### serialize<ActorRuntimeID>
```cpp
/* 77659 */
struct serialize<ActorRuntimeID>
{
__int8 gap0[1];
};

```
#### serialize<ActorUniqueID>
```cpp
/* 77824 */
struct serialize<ActorUniqueID>
{
__int8 gap0[1];
};

```
#### serialize<BaseGameVersion>
```cpp
/* 80298 */
struct serialize<BaseGameVersion>
{
__int8 gap0[1];
};

```
#### serialize<BlockPos>
```cpp
/* 78541 */
struct serialize<BlockPos>
{
__int8 gap0[1];
};

```
#### serialize<ChunkPos>
```cpp
/* 80004 */
struct serialize<ChunkPos>
{
__int8 gap0[1];
};

```
#### serialize<CommandOriginData>
```cpp
/* 78852 */
struct serialize<CommandOriginData>
{
__int8 gap0[1];
};

```
#### serialize<CompoundTag>
```cpp
/* 61748 */
struct serialize<CompoundTag>
{
__int8 gap0[1];
};

```
#### serialize<DataItem>
```cpp
/* 116856 */
struct serialize<DataItem>
{
__int8 gap0[1];
};

```
#### serialize<EducationLevelSettings>
```cpp
/* 79603 */
struct serialize<EducationLevelSettings>
{
__int8 gap0[1];
};

```
#### serialize<EducationLevelSettings>::write::$5D3ECE175654F4C4336B6523D3249746
```cpp
/* 186612 */
struct serialize<EducationLevelSettings>::write::$5D3ECE175654F4C4336B6523D3249746
{
const EducationLevelSettings *val;
};

```
#### serialize<EntityNetId>
```cpp
/* 79613 */
struct serialize<EntityNetId>
{
__int8 gap0[1];
};

```
#### serialize<GameRulesChangedPacketData>
```cpp
/* 79703 */
struct serialize<GameRulesChangedPacketData>
{
__int8 gap0[1];
};

```
#### serialize<IdentityDefinition::Type>
```cpp
/* 80475 */
struct serialize<IdentityDefinition::Type>
{
__int8 gap0[1];
};

```
#### serialize<InventoryAction>
```cpp
/* 79922 */
struct serialize<InventoryAction>
{
__int8 gap0[1];
};

```
#### serialize<InventorySource>
```cpp
/* 79923 */
struct serialize<InventorySource>
{
__int8 gap0[1];
};

```
#### serialize<InventoryTransaction>
```cpp
/* 79921 */
struct serialize<InventoryTransaction>
{
__int8 gap0[1];
};

```
#### serialize<ItemData>
```cpp
/* 80903 */
struct serialize<ItemData>
{
__int8 gap0[1];
};

```
#### serialize<ItemInstance>
```cpp
/* 81107 */
struct serialize<ItemInstance>
{
__int8 gap0[1];
};

```
#### serialize<ItemStack>
```cpp
/* 81106 */
struct serialize<ItemStack>
{
__int8 gap0[1];
};

```
#### serialize<LevelSettings>
```cpp
/* 80902 */
struct serialize<LevelSettings>
{
__int8 gap0[1];
};

```
#### serialize<MapDecoration>
```cpp
/* 78790 */
struct serialize<MapDecoration>
{
__int8 gap0[1];
};

```
#### serialize<MapItemTrackedActor::UniqueId>
```cpp
/* 78788 */
struct serialize<MapItemTrackedActor::UniqueId>
{
__int8 gap0[1];
};

```
#### serialize<MoveActorAbsoluteData>
```cpp
/* 80023 */
struct serialize<MoveActorAbsoluteData>
{
__int8 gap0[1];
};

```
#### serialize<MoveActorDeltaData>
```cpp
/* 80026 */
struct serialize<MoveActorDeltaData>
{
__int8 gap0[1];
};

```
#### serialize<NetworkBlockPosition>
```cpp
/* 77855 */
struct serialize<NetworkBlockPosition>
{
__int8 gap0[1];
};

```
#### serialize<RecipeIngredient>
```cpp
/* 184724 */
struct serialize<RecipeIngredient>
{
__int8 gap0[1];
};

```
#### serialize<ScoreboardId>
```cpp
/* 80474 */
struct serialize<ScoreboardId>
{
__int8 gap0[1];
};

```
#### serialize<ShapedChemistryRecipe>
```cpp
/* 79562 */
struct serialize<ShapedChemistryRecipe>
{
__int8 gap0[1];
};

```
#### serialize<ShapedRecipe>
```cpp
/* 79558 */
struct serialize<ShapedRecipe>
{
__int8 gap0[1];
};

```
#### serialize<ShapelessChemistryRecipe>
```cpp
/* 79561 */
struct serialize<ShapelessChemistryRecipe>
{
__int8 gap0[1];
};

```
#### serialize<ShapelessRecipe>
```cpp
/* 79559 */
struct serialize<ShapelessRecipe>
{
__int8 gap0[1];
};

```
#### serialize<ShulkerBoxRecipe>
```cpp
/* 79560 */
struct serialize<ShulkerBoxRecipe>
{
__int8 gap0[1];
};

```
#### serialize<StructureEditorData>
```cpp
/* 80912 */
struct serialize<StructureEditorData>
{
__int8 gap0[1];
};

```
#### serialize<StructureSettings>
```cpp
/* 80913 */
struct serialize<StructureSettings>
{
__int8 gap0[1];
};

```
#### serialize<Vec2>
```cpp
/* 77826 */
struct serialize<Vec2>
{
__int8 gap0[1];
};

```
#### serialize<Vec3>
```cpp
/* 77825 */
struct serialize<Vec3>
{
__int8 gap0[1];
};

```
#### serialize<mce::UUID>
```cpp
/* 77840 */
struct serialize<mce::UUID>
{
__int8 gap0[1];
};

```
#### sigaction
```cpp
/* 485724 */
struct sigaction
{
sigaction::$A264F945D93E77C42166F8517888D535 __sigaction_handler;
__sigset_t sa_mask;
int sa_flags;
void (*sa_restorer)(void);
};

```
#### siginfo_t
```cpp
/* 294326 */
struct siginfo_t
{
int si_signo;
int si_errno;
int si_code;
int __pad0;
siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A _sifields;
};

```
#### siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$1083567770C9944ECE9586E3D60D7164
```cpp
/* 294333 */
struct siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$1083567770C9944ECE9586E3D60D7164
{
__pid_t si_pid;
__uid_t si_uid;
__sigval_t si_sigval;
};

```
#### siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$269BD37B8033F496E0DA26224222815C
```cpp
/* 294334 */
struct siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$269BD37B8033F496E0DA26224222815C
{
__pid_t si_pid;
__uid_t si_uid;
int si_status;
__clock_t si_utime;
__clock_t si_stime;
};

```
#### siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$34A68472B6FD99AB74EBE1055AA656AE
```cpp
/* 294328 */
struct siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$34A68472B6FD99AB74EBE1055AA656AE
{
__pid_t si_pid;
__uid_t si_uid;
};

```
#### siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$5BF7061F11A02461448786E25380AC9A
```cpp
/* 294339 */
struct siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$5BF7061F11A02461448786E25380AC9A
{
void *_call_addr;
int _syscall;
unsigned int _arch;
};

```
#### siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$9E99AB014780417E3FB416F9C93D05FB
```cpp
/* 294335 */
struct siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$9E99AB014780417E3FB416F9C93D05FB
{
void *si_addr;
__int16 si_addr_lsb;
siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$9E99AB014780417E3FB416F9C93D05FB::$5BC825E6F32707B864090E1402CAE52B _bounds;
};

```
#### siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$9E99AB014780417E3FB416F9C93D05FB::$5BC825E6F32707B864090E1402CAE52B::$500E99076578AD283C95318D41ACB4BA
```cpp
/* 294337 */
struct siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$9E99AB014780417E3FB416F9C93D05FB::$5BC825E6F32707B864090E1402CAE52B::$500E99076578AD283C95318D41ACB4BA
{
void *_lower;
void *_upper;
};

```
#### siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$CCD53A48A999AABAD7234802D7894EC3
```cpp
/* 294330 */
struct siginfo_t::$9514A1E9F77EB70C94BB89C64268A47A::$CCD53A48A999AABAD7234802D7894EC3
{
int si_tid;
int si_overrun;
__sigval_t si_sigval;
};

```
#### sockaddr
```cpp
/* 86249 */
struct sockaddr
{
sa_family_t sa_family;
char sa_data[14];
};

```
#### sockaddr_in
```cpp
/* 4275 */
struct sockaddr_in
{
sa_family_t sin_family;
in_port_t sin_port;
in_addr sin_addr;
unsigned __int8 sin_zero[8];
};

```
#### sockaddr_in6
```cpp
/* 4271 */
struct sockaddr_in6
{
sa_family_t sin6_family;
in_port_t sin6_port;
uint32_t sin6_flowinfo;
in6_addr sin6_addr;
uint32_t sin6_scope_id;
};

```
#### stack_t
```cpp
/* 485606 */
struct stack_t
{
void *ss_sp;
int ss_flags;
size_t ss_size;
};

```
#### start_timer_after_init_state;
```cpp
/* 486941 */
struct start_timer_after_init_state;

```
#### stat
```cpp
/* 483213 */
struct stat
{
__dev_t st_dev;
__ino_t st_ino;
__nlink_t st_nlink;
__mode_t st_mode;
__uid_t st_uid;
__gid_t st_gid;
int __pad0;
__dev_t st_rdev;
__off_t st_size;
__blksize_t st_blksize;
__blkcnt_t st_blocks;
timespec st_atim;
timespec st_mtim;
timespec st_ctim;
__syscall_slong_t __glibc_reserved[3];
};

```
#### static_vector<Actor *,1>
```cpp
/* 186241 */
struct static_vector<Actor *,1>
{
std::aligned_storage<8,8>::type mArray[1];
size_t mSize;
};

```
#### static_vector<Actor *,1>::const_iterator;
```cpp
/* 186243 */
struct static_vector<Actor *,1>::const_iterator;

```
#### static_vector<Actor *,1>::iterator;
```cpp
/* 186242 */
struct static_vector<Actor *,1>::iterator;

```
#### static_vector<const Block *,4096>
```cpp
/* 253608 */
struct static_vector<const Block *,4096>
{
std::aligned_storage<8,8>::type mArray[4096];
size_t mSize;
};

```
#### static_vector<const Block *,4096>::const_iterator;
```cpp
/* 253610 */
struct static_vector<const Block *,4096>::const_iterator;

```
#### static_vector<const Block *,4096>::iterator
```cpp
/* 253609 */
struct static_vector<const Block *,4096>::iterator
{
const Block **mPtr;
};

```
#### statvfs
```cpp
/* 42803 */
struct statvfs
{
unsigned __int64 f_bsize;
unsigned __int64 f_frsize;
__fsblkcnt_t f_blocks;
__fsblkcnt_t f_bfree;
__fsblkcnt_t f_bavail;
__fsfilcnt_t f_files;
__fsfilcnt_t f_ffree;
__fsfilcnt_t f_favail;
unsigned __int64 f_fsid;
unsigned __int64 f_flag;
unsigned __int64 f_namemax;
int __f_spare[6];
};

```
#### stdext::reference_wrapper<const Localization>
```cpp
/* 60810 */
struct stdext::reference_wrapper<const Localization>
{
const Localization *ptr;
};

```
#### stdext::reference_wrapper<int>;
```cpp
/* 5920 */
struct stdext::reference_wrapper<int>;

```
