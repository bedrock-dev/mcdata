#### z_stream_s
```cpp
/* 479214 */
struct z_stream_s
{
Bytef *next_in;
uInt avail_in;
uLong total_in;
Bytef *next_out;
uInt avail_out;
uLong total_out;
char *msg;
internal_state *state;
alloc_func zalloc;
free_func zfree;
voidpf opaque;
int data_type;
uLong adler;
uLong reserved;
};

```
#### zip64_internal
```cpp
/* 485433 */
struct zip64_internal
{
zlib_filefunc64_32_def z_filefunc;
voidpf filestream;
linkedlist_data central_dir;
int in_opened_file_inzip;
curfile64_info ci;
ZPOS64_T begin_pos;
ZPOS64_T add_position_when_writting_offset;
ZPOS64_T number_entry;
char *globalcomment;
};

```
#### zip_fileinfo
```cpp
/* 483059 */
struct zip_fileinfo
{
tm_zip tmz_date;
uLong dosDate;
uLong internal_fa;
uLong external_fa;
};

```
#### zlib_filefunc64_32_def_s
```cpp
/* 482225 */
struct zlib_filefunc64_32_def_s
{
zlib_filefunc64_def zfile_func64;
open_file_func zopen32_file;
tell_file_func ztell32_file;
seek_file_func zseek32_file;
};

```
#### zlib_filefunc_def_s
```cpp
/* 485428 */
struct zlib_filefunc_def_s
{
open_file_func zopen_file;
read_file_func zread_file;
write_file_func zwrite_file;
tell_file_func ztell_file;
seek_file_func zseek_file;
close_file_func zclose_file;
testerror_file_func zerror_file;
voidpf opaque;
};

```
#### zone;
```cpp
/* 486826 */
struct zone;

```
#### z_stream_s
```cpp
/* 479214 */
struct z_stream_s
{
Bytef *next_in;
uInt avail_in;
uLong total_in;
Bytef *next_out;
uInt avail_out;
uLong total_out;
char *msg;
internal_state *state;
alloc_func zalloc;
free_func zfree;
voidpf opaque;
int data_type;
uLong adler;
uLong reserved;
};

```
#### zip64_internal
```cpp
/* 485433 */
struct zip64_internal
{
zlib_filefunc64_32_def z_filefunc;
voidpf filestream;
linkedlist_data central_dir;
int in_opened_file_inzip;
curfile64_info ci;
ZPOS64_T begin_pos;
ZPOS64_T add_position_when_writting_offset;
ZPOS64_T number_entry;
char *globalcomment;
};

```
#### zip_fileinfo
```cpp
/* 483059 */
struct zip_fileinfo
{
tm_zip tmz_date;
uLong dosDate;
uLong internal_fa;
uLong external_fa;
};

```
#### zlib_filefunc64_32_def_s
```cpp
/* 482225 */
struct zlib_filefunc64_32_def_s
{
zlib_filefunc64_def zfile_func64;
open_file_func zopen32_file;
tell_file_func ztell32_file;
seek_file_func zseek32_file;
};

```
#### zlib_filefunc_def_s
```cpp
/* 485428 */
struct zlib_filefunc_def_s
{
open_file_func zopen_file;
read_file_func zread_file;
write_file_func zwrite_file;
tell_file_func ztell_file;
seek_file_func zseek_file;
close_file_func zclose_file;
testerror_file_func zerror_file;
voidpf opaque;
};

```
#### zone;
```cpp
/* 486826 */
struct zone;

```
