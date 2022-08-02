#### lconv;
```cpp
/* 282 */
struct lconv;

```
#### linger
```cpp
/* 478103 */
struct linger
{
int l_onoff;
int l_linger;
};

```
#### link_map
```cpp
/* 486209 */
struct link_map
{
Elf64_Addr l_addr;
char *l_name;
Elf64_Dyn_0 *l_ld;
link_map *l_next;
link_map *l_prev;
};

```
#### linkedlist_data_s
```cpp
/* 485435 */
struct linkedlist_data_s
{
linkedlist_datablock_internal *first_block;
linkedlist_datablock_internal *last_block;
};

```
#### linkedlist_datablock_internal_s
```cpp
/* 485437 */
struct linkedlist_datablock_internal_s
{
linkedlist_datablock_internal_s *next_datablock;
uLong avail_in_this_block;
uLong filled_in_this_block;
uLong unused;
unsigned __int8 data[4080];
};

```
#### lldiv_t
```cpp
/* 236 */
struct lldiv_t
{
__int64 quot;
__int64 rem;
};

```
#### lconv;
```cpp
/* 282 */
struct lconv;

```
#### linger
```cpp
/* 478103 */
struct linger
{
int l_onoff;
int l_linger;
};

```
#### link_map
```cpp
/* 486209 */
struct link_map
{
Elf64_Addr l_addr;
char *l_name;
Elf64_Dyn_0 *l_ld;
link_map *l_next;
link_map *l_prev;
};

```
#### linkedlist_data_s
```cpp
/* 485435 */
struct linkedlist_data_s
{
linkedlist_datablock_internal *first_block;
linkedlist_datablock_internal *last_block;
};

```
#### linkedlist_datablock_internal_s
```cpp
/* 485437 */
struct linkedlist_datablock_internal_s
{
linkedlist_datablock_internal_s *next_datablock;
uLong avail_in_this_block;
uLong filled_in_this_block;
uLong unused;
unsigned __int8 data[4080];
};

```
#### lldiv_t
```cpp
/* 236 */
struct lldiv_t
{
__int64 quot;
__int64 rem;
};

```
