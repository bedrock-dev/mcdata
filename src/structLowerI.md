#### ifaddrs
```cpp
/* 478104 */
struct ifaddrs
{
ifaddrs *ifa_next;
char *ifa_name;
unsigned int ifa_flags;
sockaddr *ifa_addr;
sockaddr *ifa_netmask;
ifaddrs::$84E426BE247030D232EE932B77F5CBF6 ifa_ifu;
void *ifa_data;
};

```
#### ifconf
```cpp
/* 294343 */
struct ifconf
{
int ifc_len;
ifconf::$CB4E2310AA03783056CB5D3719B31C2A ifc_ifcu;
};

```
#### ifreq
```cpp
/* 294346 */
struct ifreq
{
ifreq::$EC3FB77B1F5CBB3C6B6AB4B4CE5B261D ifr_ifrn;
ifreq::$3766CEB1D20AE6FB37CD7F05C4AF9C4E ifr_ifru;
};

```
#### in6_addr
```cpp
/* 4273 */
struct in6_addr
{
in6_addr::$FA2BBAF2C6BC03A9E0081A5D902744A5 __in6_u;
};

```
#### in_addr
```cpp
/* 4276 */
struct in_addr
{
in_addr_t s_addr;
};

```
#### internal_state;
```cpp
/* 479217 */
struct internal_state;

```
#### iovec
```cpp
/* 486228 */
struct iovec
{
void *iov_base;
size_t iov_len;
};

```
#### ipv6_mreq
```cpp
/* 478153 */
struct ipv6_mreq
{
in6_addr ipv6mr_multiaddr;
unsigned int ipv6mr_interface;
};

```
#### ifaddrs
```cpp
/* 478104 */
struct ifaddrs
{
ifaddrs *ifa_next;
char *ifa_name;
unsigned int ifa_flags;
sockaddr *ifa_addr;
sockaddr *ifa_netmask;
ifaddrs::$84E426BE247030D232EE932B77F5CBF6 ifa_ifu;
void *ifa_data;
};

```
#### ifconf
```cpp
/* 294343 */
struct ifconf
{
int ifc_len;
ifconf::$CB4E2310AA03783056CB5D3719B31C2A ifc_ifcu;
};

```
#### ifreq
```cpp
/* 294346 */
struct ifreq
{
ifreq::$EC3FB77B1F5CBB3C6B6AB4B4CE5B261D ifr_ifrn;
ifreq::$3766CEB1D20AE6FB37CD7F05C4AF9C4E ifr_ifru;
};

```
#### in6_addr
```cpp
/* 4273 */
struct in6_addr
{
in6_addr::$FA2BBAF2C6BC03A9E0081A5D902744A5 __in6_u;
};

```
#### in_addr
```cpp
/* 4276 */
struct in_addr
{
in_addr_t s_addr;
};

```
#### internal_state;
```cpp
/* 479217 */
struct internal_state;

```
#### iovec
```cpp
/* 486228 */
struct iovec
{
void *iov_base;
size_t iov_len;
};

```
#### ipv6_mreq
```cpp
/* 478153 */
struct ipv6_mreq
{
in6_addr ipv6mr_multiaddr;
unsigned int ipv6mr_interface;
};

```
