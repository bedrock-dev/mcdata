#### ucontext_t
```cpp
/* 485605 */
struct ucontext_t
{
unsigned __int64 uc_flags;
ucontext_t *uc_link;
stack_t uc_stack;
mcontext_t uc_mcontext;
sigset_t uc_sigmask;
_libc_fpstate __fpregs_mem;
};

```
#### uint128_struct
```cpp
/* 485789 */
struct uint128_struct
{
uint64_t high;
uint64_t low;
};

```
#### unz64_file_pos_s
```cpp
/* 485430 */
struct unz64_file_pos_s
{
ZPOS64_T pos_in_zip_directory;
ZPOS64_T num_of_file;
};

```
#### unz64_s
```cpp
/* 485420 */
struct unz64_s
{
zlib_filefunc64_32_def z_filefunc;
int is64bitOpenFunction;
voidpf filestream;
unz_global_info64 gi;
ZPOS64_T byte_before_the_zipfile;
ZPOS64_T num_file;
ZPOS64_T pos_in_central_dir;
ZPOS64_T current_file_ok;
ZPOS64_T central_pos;
ZPOS64_T size_central_dir;
ZPOS64_T offset_central_dir;
unz_file_info64 cur_file_info;
unz_file_info64_internal cur_file_info_internal;
file_in_zip64_read_info_s *pfile_in_zip_read;
int encrypted;
int isZip64;
};

```
#### unz_file_info64_internal_s
```cpp
/* 485425 */
struct unz_file_info64_internal_s
{
ZPOS64_T offset_curfile;
};

```
#### unz_file_info64_s
```cpp
/* 485423 */
struct unz_file_info64_s
{
uLong version;
uLong version_needed;
uLong flag;
uLong compression_method;
uLong dosDate;
uLong crc;
ZPOS64_T compressed_size;
ZPOS64_T uncompressed_size;
uLong size_filename;
uLong size_file_extra;
uLong size_file_comment;
uLong disk_num_start;
uLong internal_fa;
uLong external_fa;
tm_unz tmu_date;
};

```
#### unz_file_info_s
```cpp
/* 482955 */
struct unz_file_info_s
{
uLong version;
uLong version_needed;
uLong flag;
uLong compression_method;
uLong dosDate;
uLong crc;
uLong compressed_size;
uLong uncompressed_size;
uLong size_filename;
uLong size_file_extra;
uLong size_file_comment;
uLong disk_num_start;
uLong internal_fa;
uLong external_fa;
tm_unz tmu_date;
};

```
#### unz_file_pos_s
```cpp
/* 485432 */
struct unz_file_pos_s
{
uLong pos_in_zip_directory;
uLong num_of_file;
};

```
#### unz_global_info64_s
```cpp
/* 482959 */
struct unz_global_info64_s
{
ZPOS64_T number_entry;
uLong size_comment;
};

```
#### unz_global_info_s
```cpp
/* 483063 */
struct unz_global_info_s
{
uLong number_entry;
uLong size_comment;
};

```
#### user_fpregs_struct
```cpp
/* 485830 */
struct user_fpregs_struct
{
unsigned __int16 cwd;
unsigned __int16 swd;
unsigned __int16 ftw;
unsigned __int16 fop;
unsigned __int64 rip;
unsigned __int64 rdp;
unsigned int mxcsr;
unsigned int mxcr_mask;
unsigned int st_space[32];
unsigned int xmm_space[64];
unsigned int padding[24];
};

```
#### user_regs_struct
```cpp
/* 485829 */
struct user_regs_struct
{
unsigned __int64 r15;
unsigned __int64 r14;
unsigned __int64 r13;
unsigned __int64 r12;
unsigned __int64 rbp;
unsigned __int64 rbx;
unsigned __int64 r11;
unsigned __int64 r10;
unsigned __int64 r9;
unsigned __int64 r8;
unsigned __int64 rax;
unsigned __int64 rcx;
unsigned __int64 rdx;
unsigned __int64 rsi;
unsigned __int64 rdi;
unsigned __int64 orig_rax;
unsigned __int64 rip;
unsigned __int64 cs;
unsigned __int64 eflags;
unsigned __int64 rsp;
unsigned __int64 ss;
unsigned __int64 fs_base;
unsigned __int64 gs_base;
unsigned __int64 ds;
unsigned __int64 es;
unsigned __int64 fs;
unsigned __int64 gs;
};

```
#### utf8proc_property_struct
```cpp
/* 485136 */
struct utf8proc_property_struct
{
utf8proc_propval_t category;
utf8proc_propval_t combining_class;
utf8proc_propval_t bidi_class;
utf8proc_propval_t decomp_type;
const int32_t *decomp_mapping;
unsigned __int32 bidi_mirrored : 1;
int32_t uppercase_mapping;
int32_t lowercase_mapping;
int32_t titlecase_mapping;
int32_t comb1st_index;
int32_t comb2nd_index;
unsigned __int32 comp_exclusion : 1;
unsigned __int32 ignorable : 1;
unsigned __int32 control_boundary : 1;
unsigned __int32 extend : 1;
const int32_t *casefold_mapping;
};

```
#### utimbuf
```cpp
/* 483220 */
struct utimbuf
{
__time_t actime;
__time_t modtime;
};

```
#### ucontext_t
```cpp
/* 485605 */
struct ucontext_t
{
unsigned __int64 uc_flags;
ucontext_t *uc_link;
stack_t uc_stack;
mcontext_t uc_mcontext;
sigset_t uc_sigmask;
_libc_fpstate __fpregs_mem;
};

```
#### uint128_struct
```cpp
/* 485789 */
struct uint128_struct
{
uint64_t high;
uint64_t low;
};

```
#### unz64_file_pos_s
```cpp
/* 485430 */
struct unz64_file_pos_s
{
ZPOS64_T pos_in_zip_directory;
ZPOS64_T num_of_file;
};

```
#### unz64_s
```cpp
/* 485420 */
struct unz64_s
{
zlib_filefunc64_32_def z_filefunc;
int is64bitOpenFunction;
voidpf filestream;
unz_global_info64 gi;
ZPOS64_T byte_before_the_zipfile;
ZPOS64_T num_file;
ZPOS64_T pos_in_central_dir;
ZPOS64_T current_file_ok;
ZPOS64_T central_pos;
ZPOS64_T size_central_dir;
ZPOS64_T offset_central_dir;
unz_file_info64 cur_file_info;
unz_file_info64_internal cur_file_info_internal;
file_in_zip64_read_info_s *pfile_in_zip_read;
int encrypted;
int isZip64;
};

```
#### unz_file_info64_internal_s
```cpp
/* 485425 */
struct unz_file_info64_internal_s
{
ZPOS64_T offset_curfile;
};

```
#### unz_file_info64_s
```cpp
/* 485423 */
struct unz_file_info64_s
{
uLong version;
uLong version_needed;
uLong flag;
uLong compression_method;
uLong dosDate;
uLong crc;
ZPOS64_T compressed_size;
ZPOS64_T uncompressed_size;
uLong size_filename;
uLong size_file_extra;
uLong size_file_comment;
uLong disk_num_start;
uLong internal_fa;
uLong external_fa;
tm_unz tmu_date;
};

```
#### unz_file_info_s
```cpp
/* 482955 */
struct unz_file_info_s
{
uLong version;
uLong version_needed;
uLong flag;
uLong compression_method;
uLong dosDate;
uLong crc;
uLong compressed_size;
uLong uncompressed_size;
uLong size_filename;
uLong size_file_extra;
uLong size_file_comment;
uLong disk_num_start;
uLong internal_fa;
uLong external_fa;
tm_unz tmu_date;
};

```
#### unz_file_pos_s
```cpp
/* 485432 */
struct unz_file_pos_s
{
uLong pos_in_zip_directory;
uLong num_of_file;
};

```
#### unz_global_info64_s
```cpp
/* 482959 */
struct unz_global_info64_s
{
ZPOS64_T number_entry;
uLong size_comment;
};

```
#### unz_global_info_s
```cpp
/* 483063 */
struct unz_global_info_s
{
uLong number_entry;
uLong size_comment;
};

```
#### user_fpregs_struct
```cpp
/* 485830 */
struct user_fpregs_struct
{
unsigned __int16 cwd;
unsigned __int16 swd;
unsigned __int16 ftw;
unsigned __int16 fop;
unsigned __int64 rip;
unsigned __int64 rdp;
unsigned int mxcsr;
unsigned int mxcr_mask;
unsigned int st_space[32];
unsigned int xmm_space[64];
unsigned int padding[24];
};

```
#### user_regs_struct
```cpp
/* 485829 */
struct user_regs_struct
{
unsigned __int64 r15;
unsigned __int64 r14;
unsigned __int64 r13;
unsigned __int64 r12;
unsigned __int64 rbp;
unsigned __int64 rbx;
unsigned __int64 r11;
unsigned __int64 r10;
unsigned __int64 r9;
unsigned __int64 r8;
unsigned __int64 rax;
unsigned __int64 rcx;
unsigned __int64 rdx;
unsigned __int64 rsi;
unsigned __int64 rdi;
unsigned __int64 orig_rax;
unsigned __int64 rip;
unsigned __int64 cs;
unsigned __int64 eflags;
unsigned __int64 rsp;
unsigned __int64 ss;
unsigned __int64 fs_base;
unsigned __int64 gs_base;
unsigned __int64 ds;
unsigned __int64 es;
unsigned __int64 fs;
unsigned __int64 gs;
};

```
#### utf8proc_property_struct
```cpp
/* 485136 */
struct utf8proc_property_struct
{
utf8proc_propval_t category;
utf8proc_propval_t combining_class;
utf8proc_propval_t bidi_class;
utf8proc_propval_t decomp_type;
const int32_t *decomp_mapping;
unsigned __int32 bidi_mirrored : 1;
int32_t uppercase_mapping;
int32_t lowercase_mapping;
int32_t titlecase_mapping;
int32_t comb1st_index;
int32_t comb2nd_index;
unsigned __int32 comp_exclusion : 1;
unsigned __int32 ignorable : 1;
unsigned __int32 control_boundary : 1;
unsigned __int32 extend : 1;
const int32_t *casefold_mapping;
};

```
#### utimbuf
```cpp
/* 483220 */
struct utimbuf
{
__time_t actime;
__time_t modtime;
};

```
