#### $1210F371E758421EF368DC19A231A6DA : __int32
```cpp
/* 478100 */
enum $1210F371E758421EF368DC19A231A6DA : __int32
{
IFF_UP = 0x1,
IFF_BROADCAST = 0x2,
IFF_DEBUG = 0x4,
IFF_LOOPBACK = 0x8,
IFF_POINTOPOINT = 0x10,
IFF_NOTRAILERS = 0x20,
IFF_RUNNING = 0x40,
IFF_NOARP = 0x80,
IFF_PROMISC = 0x100,
IFF_ALLMULTI = 0x200,
IFF_MASTER = 0x400,
IFF_SLAVE = 0x800,
IFF_MULTICAST = 0x1000,
IFF_PORTSEL = 0x2000,
IFF_AUTOMEDIA = 0x4000,
IFF_DYNAMIC = 0x8000,
};

```
#### $347C4AA96D10B0B03CED8E04011C7660 : __int32
```cpp
/* 486312 */
enum $347C4AA96D10B0B03CED8E04011C7660 : __int32
{
strictConversion = 0x0,
lenientConversion = 0x1,
};

```
#### $3D49817EA999CD8B3DC48DB74CFF9164 : __int32
```cpp
/* 486207 */
enum $3D49817EA999CD8B3DC48DB74CFF9164 : __int32
{
MD_OS_WIN32S = 0x0,
MD_OS_WIN32_WINDOWS = 0x1,
MD_OS_WIN32_NT = 0x2,
MD_OS_WIN32_CE = 0x3,
MD_OS_UNIX = 0x8000,
MD_OS_MAC_OS_X = 0x8101,
MD_OS_IOS = 0x8102,
MD_OS_LINUX = 0x8201,
MD_OS_SOLARIS = 0x8202,
MD_OS_ANDROID = 0x8203,
MD_OS_PS3 = 0x8204,
MD_OS_NACL = 0x8205,
};

```
#### $4AC4411A22C6C9FCB976BEA19FD29F1E : __int32
```cpp
/* 485728 */
enum $4AC4411A22C6C9FCB976BEA19FD29F1E : __int32
{
MD_EXCEPTION_CODE_LIN_SIGHUP = 0x1,
MD_EXCEPTION_CODE_LIN_SIGINT = 0x2,
MD_EXCEPTION_CODE_LIN_SIGQUIT = 0x3,
MD_EXCEPTION_CODE_LIN_SIGILL = 0x4,
MD_EXCEPTION_CODE_LIN_SIGTRAP = 0x5,
MD_EXCEPTION_CODE_LIN_SIGABRT = 0x6,
MD_EXCEPTION_CODE_LIN_SIGBUS = 0x7,
MD_EXCEPTION_CODE_LIN_SIGFPE = 0x8,
MD_EXCEPTION_CODE_LIN_SIGKILL = 0x9,
MD_EXCEPTION_CODE_LIN_SIGUSR1 = 0xA,
MD_EXCEPTION_CODE_LIN_SIGSEGV = 0xB,
MD_EXCEPTION_CODE_LIN_SIGUSR2 = 0xC,
MD_EXCEPTION_CODE_LIN_SIGPIPE = 0xD,
MD_EXCEPTION_CODE_LIN_SIGALRM = 0xE,
MD_EXCEPTION_CODE_LIN_SIGTERM = 0xF,
MD_EXCEPTION_CODE_LIN_SIGSTKFLT = 0x10,
MD_EXCEPTION_CODE_LIN_SIGCHLD = 0x11,
MD_EXCEPTION_CODE_LIN_SIGCONT = 0x12,
MD_EXCEPTION_CODE_LIN_SIGSTOP = 0x13,
MD_EXCEPTION_CODE_LIN_SIGTSTP = 0x14,
MD_EXCEPTION_CODE_LIN_SIGTTIN = 0x15,
MD_EXCEPTION_CODE_LIN_SIGTTOU = 0x16,
MD_EXCEPTION_CODE_LIN_SIGURG = 0x17,
MD_EXCEPTION_CODE_LIN_SIGXCPU = 0x18,
MD_EXCEPTION_CODE_LIN_SIGXFSZ = 0x19,
MD_EXCEPTION_CODE_LIN_SIGVTALRM = 0x1A,
MD_EXCEPTION_CODE_LIN_SIGPROF = 0x1B,
MD_EXCEPTION_CODE_LIN_SIGWINCH = 0x1C,
MD_EXCEPTION_CODE_LIN_SIGIO = 0x1D,
MD_EXCEPTION_CODE_LIN_SIGPWR = 0x1E,
MD_EXCEPTION_CODE_LIN_SIGSYS = 0x1F,
MD_EXCEPTION_CODE_LIN_DUMP_REQUESTED = 0xFFFFFFFF,
};

```
#### $56C97545D8191E8EE2F000856B97BA17 : __int32
```cpp
/* 485729 */
enum $56C97545D8191E8EE2F000856B97BA17 : __int32
{
REG_R8 = 0x0,
REG_R9 = 0x1,
REG_R10 = 0x2,
REG_R11 = 0x3,
REG_R12 = 0x4,
REG_R13 = 0x5,
REG_R14 = 0x6,
REG_R15 = 0x7,
REG_RDI = 0x8,
REG_RSI = 0x9,
REG_RBP = 0xA,
REG_RBX = 0xB,
REG_RDX = 0xC,
REG_RAX = 0xD,
REG_RCX = 0xE,
REG_RSP = 0xF,
REG_RIP = 0x10,
REG_EFL = 0x11,
REG_CSGSFS = 0x12,
REG_ERR = 0x13,
REG_TRAPNO = 0x14,
REG_OLDMASK = 0x15,
REG_CR2 = 0x16,
};

```
#### $7DA0ED1C510EB8BBF6F0B878F549FC50 : __int32
```cpp
/* 294341 */
enum $7DA0ED1C510EB8BBF6F0B878F549FC50 : __int32
{
IPPROTO_IP = 0x0,
IPPROTO_ICMP = 0x1,
IPPROTO_IGMP = 0x2,
IPPROTO_IPIP = 0x4,
IPPROTO_TCP = 0x6,
IPPROTO_EGP = 0x8,
IPPROTO_PUP = 0xC,
IPPROTO_UDP = 0x11,
IPPROTO_IDP = 0x16,
IPPROTO_TP = 0x1D,
IPPROTO_DCCP = 0x21,
IPPROTO_IPV6 = 0x29,
IPPROTO_RSVP = 0x2E,
IPPROTO_GRE = 0x2F,
IPPROTO_ESP = 0x32,
IPPROTO_AH = 0x33,
IPPROTO_MTP = 0x5C,
IPPROTO_BEETPH = 0x5E,
IPPROTO_ENCAP = 0x62,
IPPROTO_PIM = 0x67,
IPPROTO_COMP = 0x6C,
IPPROTO_SCTP = 0x84,
IPPROTO_UDPLITE = 0x88,
IPPROTO_MPLS = 0x89,
IPPROTO_RAW = 0xFF,
IPPROTO_MAX = 0x100,
};

```
#### $806B9BA87CC87D12CA732A028B794533 : __int32
```cpp
/* 42802 */
enum $806B9BA87CC87D12CA732A028B794533 : __int32
{
_SC_ARG_MAX = 0x0,
_SC_CHILD_MAX = 0x1,
_SC_CLK_TCK = 0x2,
_SC_NGROUPS_MAX = 0x3,
_SC_OPEN_MAX = 0x4,
_SC_STREAM_MAX = 0x5,
_SC_TZNAME_MAX = 0x6,
_SC_JOB_CONTROL = 0x7,
_SC_SAVED_IDS = 0x8,
_SC_REALTIME_SIGNALS = 0x9,
_SC_PRIORITY_SCHEDULING = 0xA,
_SC_TIMERS = 0xB,
_SC_ASYNCHRONOUS_IO = 0xC,
_SC_PRIORITIZED_IO = 0xD,
_SC_SYNCHRONIZED_IO = 0xE,
_SC_FSYNC = 0xF,
_SC_MAPPED_FILES = 0x10,
_SC_MEMLOCK = 0x11,
_SC_MEMLOCK_RANGE = 0x12,
_SC_MEMORY_PROTECTION = 0x13,
_SC_MESSAGE_PASSING = 0x14,
_SC_SEMAPHORES = 0x15,
_SC_SHARED_MEMORY_OBJECTS = 0x16,
_SC_AIO_LISTIO_MAX = 0x17,
_SC_AIO_MAX = 0x18,
_SC_AIO_PRIO_DELTA_MAX = 0x19,
_SC_DELAYTIMER_MAX = 0x1A,
_SC_MQ_OPEN_MAX = 0x1B,
_SC_MQ_PRIO_MAX = 0x1C,
_SC_VERSION = 0x1D,
_SC_PAGESIZE = 0x1E,
_SC_RTSIG_MAX = 0x1F,
_SC_SEM_NSEMS_MAX = 0x20,
_SC_SEM_VALUE_MAX = 0x21,
_SC_SIGQUEUE_MAX = 0x22,
_SC_TIMER_MAX = 0x23,
_SC_BC_BASE_MAX = 0x24,
_SC_BC_DIM_MAX = 0x25,
_SC_BC_SCALE_MAX = 0x26,
_SC_BC_STRING_MAX = 0x27,
_SC_COLL_WEIGHTS_MAX = 0x28,
_SC_EQUIV_CLASS_MAX = 0x29,
_SC_EXPR_NEST_MAX = 0x2A,
_SC_LINE_MAX = 0x2B,
_SC_RE_DUP_MAX = 0x2C,
_SC_CHARCLASS_NAME_MAX = 0x2D,
_SC_2_VERSION = 0x2E,
_SC_2_C_BIND = 0x2F,
_SC_2_C_DEV = 0x30,
_SC_2_FORT_DEV = 0x31,
_SC_2_FORT_RUN = 0x32,
_SC_2_SW_DEV = 0x33,
_SC_2_LOCALEDEF = 0x34,
_SC_PII = 0x35,
_SC_PII_XTI = 0x36,
_SC_PII_SOCKET = 0x37,
_SC_PII_INTERNET = 0x38,
_SC_PII_OSI = 0x39,
_SC_POLL = 0x3A,
_SC_SELECT = 0x3B,
_SC_UIO_MAXIOV = 0x3C,
_SC_IOV_MAX = 0x3C,
_SC_PII_INTERNET_STREAM = 0x3D,
_SC_PII_INTERNET_DGRAM = 0x3E,
_SC_PII_OSI_COTS = 0x3F,
_SC_PII_OSI_CLTS = 0x40,
_SC_PII_OSI_M = 0x41,
_SC_T_IOV_MAX = 0x42,
_SC_THREADS = 0x43,
_SC_THREAD_SAFE_FUNCTIONS = 0x44,
_SC_GETGR_R_SIZE_MAX = 0x45,
_SC_GETPW_R_SIZE_MAX = 0x46,
_SC_LOGIN_NAME_MAX = 0x47,
_SC_TTY_NAME_MAX = 0x48,
_SC_THREAD_DESTRUCTOR_ITERATIONS = 0x49,
_SC_THREAD_KEYS_MAX = 0x4A,
_SC_THREAD_STACK_MIN = 0x4B,
_SC_THREAD_THREADS_MAX = 0x4C,
_SC_THREAD_ATTR_STACKADDR = 0x4D,
_SC_THREAD_ATTR_STACKSIZE = 0x4E,
_SC_THREAD_PRIORITY_SCHEDULING = 0x4F,
_SC_THREAD_PRIO_INHERIT = 0x50,
_SC_THREAD_PRIO_PROTECT = 0x51,
_SC_THREAD_PROCESS_SHARED = 0x52,
_SC_NPROCESSORS_CONF = 0x53,
_SC_NPROCESSORS_ONLN = 0x54,
_SC_PHYS_PAGES = 0x55,
_SC_AVPHYS_PAGES = 0x56,
_SC_ATEXIT_MAX = 0x57,
_SC_PASS_MAX = 0x58,
_SC_XOPEN_VERSION = 0x59,
_SC_XOPEN_XCU_VERSION = 0x5A,
_SC_XOPEN_UNIX = 0x5B,
_SC_XOPEN_CRYPT = 0x5C,
_SC_XOPEN_ENH_I18N = 0x5D,
_SC_XOPEN_SHM = 0x5E,
_SC_2_CHAR_TERM = 0x5F,
_SC_2_C_VERSION = 0x60,
_SC_2_UPE = 0x61,
_SC_XOPEN_XPG2 = 0x62,
_SC_XOPEN_XPG3 = 0x63,
_SC_XOPEN_XPG4 = 0x64,
_SC_CHAR_BIT = 0x65,
_SC_CHAR_MAX = 0x66,
_SC_CHAR_MIN = 0x67,
_SC_INT_MAX = 0x68,
_SC_INT_MIN = 0x69,
_SC_LONG_BIT = 0x6A,
_SC_WORD_BIT = 0x6B,
_SC_MB_LEN_MAX = 0x6C,
_SC_NZERO = 0x6D,
_SC_SSIZE_MAX = 0x6E,
_SC_SCHAR_MAX = 0x6F,
_SC_SCHAR_MIN = 0x70,
_SC_SHRT_MAX = 0x71,
_SC_SHRT_MIN = 0x72,
_SC_UCHAR_MAX = 0x73,
_SC_UINT_MAX = 0x74,
_SC_ULONG_MAX = 0x75,
_SC_USHRT_MAX = 0x76,
_SC_NL_ARGMAX = 0x77,
_SC_NL_LANGMAX = 0x78,
_SC_NL_MSGMAX = 0x79,
_SC_NL_NMAX = 0x7A,
_SC_NL_SETMAX = 0x7B,
_SC_NL_TEXTMAX = 0x7C,
_SC_XBS5_ILP32_OFF32 = 0x7D,
_SC_XBS5_ILP32_OFFBIG = 0x7E,
_SC_XBS5_LP64_OFF64 = 0x7F,
_SC_XBS5_LPBIG_OFFBIG = 0x80,
_SC_XOPEN_LEGACY = 0x81,
_SC_XOPEN_REALTIME = 0x82,
_SC_XOPEN_REALTIME_THREADS = 0x83,
_SC_ADVISORY_INFO = 0x84,
_SC_BARRIERS = 0x85,
_SC_BASE = 0x86,
_SC_C_LANG_SUPPORT = 0x87,
_SC_C_LANG_SUPPORT_R = 0x88,
_SC_CLOCK_SELECTION = 0x89,
_SC_CPUTIME = 0x8A,
_SC_THREAD_CPUTIME = 0x8B,
_SC_DEVICE_IO = 0x8C,
_SC_DEVICE_SPECIFIC = 0x8D,
_SC_DEVICE_SPECIFIC_R = 0x8E,
_SC_FD_MGMT = 0x8F,
_SC_FIFO = 0x90,
_SC_PIPE = 0x91,
_SC_FILE_ATTRIBUTES = 0x92,
_SC_FILE_LOCKING = 0x93,
_SC_FILE_SYSTEM = 0x94,
_SC_MONOTONIC_CLOCK = 0x95,
_SC_MULTI_PROCESS = 0x96,
_SC_SINGLE_PROCESS = 0x97,
_SC_NETWORKING = 0x98,
_SC_READER_WRITER_LOCKS = 0x99,
_SC_SPIN_LOCKS = 0x9A,
_SC_REGEXP = 0x9B,
_SC_REGEX_VERSION = 0x9C,
_SC_SHELL = 0x9D,
_SC_SIGNALS = 0x9E,
_SC_SPAWN = 0x9F,
_SC_SPORADIC_SERVER = 0xA0,
_SC_THREAD_SPORADIC_SERVER = 0xA1,
_SC_SYSTEM_DATABASE = 0xA2,
_SC_SYSTEM_DATABASE_R = 0xA3,
_SC_TIMEOUTS = 0xA4,
_SC_TYPED_MEMORY_OBJECTS = 0xA5,
_SC_USER_GROUPS = 0xA6,
_SC_USER_GROUPS_R = 0xA7,
_SC_2_PBS = 0xA8,
_SC_2_PBS_ACCOUNTING = 0xA9,
_SC_2_PBS_LOCATE = 0xAA,
_SC_2_PBS_MESSAGE = 0xAB,
_SC_2_PBS_TRACK = 0xAC,
_SC_SYMLOOP_MAX = 0xAD,
_SC_STREAMS = 0xAE,
_SC_2_PBS_CHECKPOINT = 0xAF,
_SC_V6_ILP32_OFF32 = 0xB0,
_SC_V6_ILP32_OFFBIG = 0xB1,
_SC_V6_LP64_OFF64 = 0xB2,
_SC_V6_LPBIG_OFFBIG = 0xB3,
_SC_HOST_NAME_MAX = 0xB4,
_SC_TRACE = 0xB5,
_SC_TRACE_EVENT_FILTER = 0xB6,
_SC_TRACE_INHERIT = 0xB7,
_SC_TRACE_LOG = 0xB8,
_SC_LEVEL1_ICACHE_SIZE = 0xB9,
_SC_LEVEL1_ICACHE_ASSOC = 0xBA,
_SC_LEVEL1_ICACHE_LINESIZE = 0xBB,
_SC_LEVEL1_DCACHE_SIZE = 0xBC,
_SC_LEVEL1_DCACHE_ASSOC = 0xBD,
_SC_LEVEL1_DCACHE_LINESIZE = 0xBE,
_SC_LEVEL2_CACHE_SIZE = 0xBF,
_SC_LEVEL2_CACHE_ASSOC = 0xC0,
_SC_LEVEL2_CACHE_LINESIZE = 0xC1,
_SC_LEVEL3_CACHE_SIZE = 0xC2,
_SC_LEVEL3_CACHE_ASSOC = 0xC3,
_SC_LEVEL3_CACHE_LINESIZE = 0xC4,
_SC_LEVEL4_CACHE_SIZE = 0xC5,
_SC_LEVEL4_CACHE_ASSOC = 0xC6,
_SC_LEVEL4_CACHE_LINESIZE = 0xC7,
_SC_IPV6 = 0xEB,
_SC_RAW_SOCKETS = 0xEC,
_SC_V7_ILP32_OFF32 = 0xED,
_SC_V7_ILP32_OFFBIG = 0xEE,
_SC_V7_LP64_OFF64 = 0xEF,
_SC_V7_LPBIG_OFFBIG = 0xF0,
_SC_SS_REPL_MAX = 0xF1,
_SC_TRACE_EVENT_NAME_MAX = 0xF2,
_SC_TRACE_NAME_MAX = 0xF3,
_SC_TRACE_SYS_MAX = 0xF4,
_SC_TRACE_USER_EVENT_MAX = 0xF5,
_SC_XOPEN_STREAMS = 0xF6,
_SC_THREAD_ROBUST_PRIO_INHERIT = 0xF7,
_SC_THREAD_ROBUST_PRIO_PROTECT = 0xF8,
};

```
#### $8B0F52549CE761034392E15FD5290A77 : __int32
```cpp
/* 486205 */
enum $8B0F52549CE761034392E15FD5290A77 : __int32
{
MD_UNUSED_STREAM = 0x0,
MD_RESERVED_STREAM_0 = 0x1,
MD_RESERVED_STREAM_1 = 0x2,
MD_THREAD_LIST_STREAM = 0x3,
MD_MODULE_LIST_STREAM = 0x4,
MD_MEMORY_LIST_STREAM = 0x5,
MD_EXCEPTION_STREAM = 0x6,
MD_SYSTEM_INFO_STREAM = 0x7,
MD_THREAD_EX_LIST_STREAM = 0x8,
MD_MEMORY_64_LIST_STREAM = 0x9,
MD_COMMENT_STREAM_A = 0xA,
MD_COMMENT_STREAM_W = 0xB,
MD_HANDLE_DATA_STREAM = 0xC,
MD_FUNCTION_TABLE_STREAM = 0xD,
MD_UNLOADED_MODULE_LIST_STREAM = 0xE,
MD_MISC_INFO_STREAM = 0xF,
MD_MEMORY_INFO_LIST_STREAM = 0x10,
MD_THREAD_INFO_LIST_STREAM = 0x11,
MD_HANDLE_OPERATION_LIST_STREAM = 0x12,
MD_TOKEN_STREAM = 0x13,
MD_JAVASCRIPT_DATA_STREAM = 0x14,
MD_SYSTEM_MEMORY_INFO_STREAM = 0x15,
MD_PROCESS_VM_COUNTERS_STREAM = 0x16,
MD_LAST_RESERVED_STREAM = 0xFFFF,
MD_BREAKPAD_INFO_STREAM = 0x47670001,
MD_ASSERTION_INFO_STREAM = 0x47670002,
MD_LINUX_CPU_INFO = 0x47670003,
MD_LINUX_PROC_STATUS = 0x47670004,
MD_LINUX_LSB_RELEASE = 0x47670005,
MD_LINUX_CMD_LINE = 0x47670006,
MD_LINUX_ENVIRON = 0x47670007,
MD_LINUX_AUXV = 0x47670008,
MD_LINUX_MAPS = 0x47670009,
MD_LINUX_DSO_DEBUG = 0x4767000A,
};

```
#### $921DADCB212321B7AEB7DFA289997804 : __int32
```cpp
/* 486206 */
enum $921DADCB212321B7AEB7DFA289997804 : __int32
{
MD_CPU_ARCHITECTURE_X86 = 0x0,
MD_CPU_ARCHITECTURE_MIPS = 0x1,
MD_CPU_ARCHITECTURE_ALPHA = 0x2,
MD_CPU_ARCHITECTURE_PPC = 0x3,
MD_CPU_ARCHITECTURE_SHX = 0x4,
MD_CPU_ARCHITECTURE_ARM = 0x5,
MD_CPU_ARCHITECTURE_IA64 = 0x6,
MD_CPU_ARCHITECTURE_ALPHA64 = 0x7,
MD_CPU_ARCHITECTURE_MSIL = 0x8,
MD_CPU_ARCHITECTURE_AMD64 = 0x9,
MD_CPU_ARCHITECTURE_X86_WIN64 = 0xA,
MD_CPU_ARCHITECTURE_SPARC = 0x8001,
MD_CPU_ARCHITECTURE_PPC64 = 0x8002,
MD_CPU_ARCHITECTURE_ARM64 = 0x8003,
MD_CPU_ARCHITECTURE_MIPS64 = 0x8004,
MD_CPU_ARCHITECTURE_UNKNOWN = 0xFFFF,
};

```
#### $9C6F2EC01E3BBF5B0C7567BE63B52E63 : __int32
```cpp
/* 485737 */
enum $9C6F2EC01E3BBF5B0C7567BE63B52E63 : __int32
{
SCM_RIGHTS = 0x1,
SCM_CREDENTIALS = 0x2,
};

```
#### $ACDD07C6EE62D6CF0A2EDB2FA1B08CD2 : __int32
```cpp
/* 478120 */
enum $ACDD07C6EE62D6CF0A2EDB2FA1B08CD2 : __int32
{
SHUT_RD = 0x0,
SHUT_WR = 0x1,
SHUT_RDWR = 0x2,
};

```
#### $B829A033D76A0B72BA0F6DE5FA2A0558 : __int32
```cpp
/* 485727 */
enum $B829A033D76A0B72BA0F6DE5FA2A0558 : __int32
{
SI_ASYNCNL = 0xFFFFFFC4,
SI_TKILL = 0xFFFFFFFA,
SI_SIGIO = 0xFFFFFFFB,
SI_ASYNCIO = 0xFFFFFFFC,
SI_MESGQ = 0xFFFFFFFD,
SI_TIMER = 0xFFFFFFFE,
SI_QUEUE = 0xFFFFFFFF,
SI_USER = 0x0,
SI_KERNEL = 0x80,
};

```
#### $BF4FFC8FA3F69AC17F194B5C1C38DCD3 : __int32
```cpp
/* 478087 */
enum $BF4FFC8FA3F69AC17F194B5C1C38DCD3 : __int32
{
PTHREAD_CREATE_JOINABLE = 0x0,
PTHREAD_CREATE_DETACHED = 0x1,
};

```
#### $D8AD35139B05A1F2F34E4C9B32270E50 : __int32
```cpp
/* 485599 */
enum $D8AD35139B05A1F2F34E4C9B32270E50 : __int32
{
CURLFORM_NOTHING = 0x0,
CURLFORM_COPYNAME = 0x1,
CURLFORM_PTRNAME = 0x2,
CURLFORM_NAMELENGTH = 0x3,
CURLFORM_COPYCONTENTS = 0x4,
CURLFORM_PTRCONTENTS = 0x5,
CURLFORM_CONTENTSLENGTH = 0x6,
CURLFORM_FILECONTENT = 0x7,
CURLFORM_ARRAY = 0x8,
CURLFORM_OBSOLETE = 0x9,
CURLFORM_FILE = 0xA,
CURLFORM_BUFFER = 0xB,
CURLFORM_BUFFERPTR = 0xC,
CURLFORM_BUFFERLENGTH = 0xD,
CURLFORM_CONTENTTYPE = 0xE,
CURLFORM_CONTENTHEADER = 0xF,
CURLFORM_FILENAME = 0x10,
CURLFORM_END = 0x11,
CURLFORM_OBSOLETE2 = 0x12,
CURLFORM_STREAM = 0x13,
CURLFORM_LASTENTRY = 0x14,
};

```
#### $EF54F05406754BCF09CF1DEEDAE2A64A : __int64
```cpp
/* 430546 */
enum $EF54F05406754BCF09CF1DEEDAE2A64A : __int64
{
ExpressionOpFlag_LeftParenthesis = 0x1,
ExpressionOpFlag_RightParenthesis = 0x2,
ExpressionOpFlag_LeftBracket = 0x4,
ExpressionOpFlag_RightBracket = 0x8,
ExpressionOpFlag_Negate = 0x10,
ExpressionOpFlag_LogicalNot = 0x20,
ExpressionOpFlag_Abs = 0x40,
ExpressionOpFlag_Cos = 0x80,
ExpressionOpFlag_Sin = 0x100,
ExpressionOpFlag_Clamp = 0x200,
ExpressionOpFlag_Lerp = 0x400,
ExpressionOpFlag_LerpRotate = 0x800,
ExpressionOpFlag_Max = 0x1000,
ExpressionOpFlag_Min = 0x2000,
ExpressionOpFlag_Round = 0x4000,
ExpressionOpFlag_Trunc = 0x8000,
ExpressionOpFlag_Ceil = 0x10000,
ExpressionOpFlag_Floor = 0x20000,
ExpressionOpFlag_Mod = 0x40000,
ExpressionOpFlag_Add = 0x80000,
ExpressionOpFlag_Div = 0x100000,
ExpressionOpFlag_Mul = 0x200000,
ExpressionOpFlag_Exp = 0x400000,
ExpressionOpFlag_Ln = 0x800000,
ExpressionOpFlag_Sqrt = 0x1000000,
ExpressionOpFlag_Pow = 0x2000000,
ExpressionOpFlag_Random = 0x4000000,
ExpressionOpFlag_DieRoll = 0x8000000,
ExpressionOpFlag_QueryFunction = 0x10000000,
ExpressionOpFlag_GenericQueryFunction = 0x20000000,
ExpressionOpFlag_ArrayVariable = 0x40000000,
ExpressionOpFlag_EntityVariable = 0x80000000,
ExpressionOpFlag_TempVariable = 0x100000000,
ExpressionOpFlag_HashedString = 0x200000000,
ExpressionOpFlag_GeometryVariable = 0x400000000,
ExpressionOpFlag_MaterialVariable = 0x800000000,
ExpressionOpFlag_TextureVariable = 0x1000000000,
ExpressionOpFlag_LessThan = 0x2000000000,
ExpressionOpFlag_LessEqual = 0x4000000000,
ExpressionOpFlag_GreaterEqual = 0x8000000000,
ExpressionOpFlag_GreaterThan = 0x10000000000,
ExpressionOpFlag_LogicalEqual = 0x20000000000,
ExpressionOpFlag_LogicalNotEqual = 0x40000000000,
ExpressionOpFlag_LogicalOr = 0x80000000000,
ExpressionOpFlag_LogicalAnd = 0x100000000000,
ExpressionOpFlag_Conditional = 0x200000000000,
ExpressionOpFlag_ConditionalElse = 0x400000000000,
ExpressionOpFlag_Float = 0x800000000000,
ExpressionOpFlag_Pi = 0x1000000000000,
ExpressionOpFlag_Array = 0x2000000000000,
ExpressionOpFlag_Geometry = 0x4000000000000,
ExpressionOpFlag_ModelPart = 0x8000000000000,
ExpressionOpFlag_Material = 0x10000000000000,
ExpressionOpFlag_Texture = 0x20000000000000,
ExpressionOpFlag_Assignment = 0x40000000000000,
ExpressionOpFlag_Semicolon = 0x80000000000000,
ExpressionOpFlag_Return = 0x100000000000000,
ExpressionOpFlag_Comma = 0x200000000000000,
ExpressionOpFlag_This = 0x400000000000000,
};

```
#### $F32B689939CEA71C8E19C738C224B0DC : __int32
```cpp
/* 485730 */
enum $F32B689939CEA71C8E19C738C224B0DC : __int32
{
SS_ONSTACK = 0x1,
SS_DISABLE = 0x2,
};

```
#### $F74524F48CF4910B20371C911B765561 : __int32
```cpp
/* 483208 */
enum $F74524F48CF4910B20371C911B765561 : __int32
{
DT_UNKNOWN = 0x0,
DT_FIFO = 0x1,
DT_CHR = 0x2,
DT_DIR = 0x4,
DT_BLK = 0x6,
DT_REG = 0x8,
DT_LNK = 0xA,
DT_SOCK = 0xC,
DT_WHT = 0xE,
};

```
#### $FB2272BC94AC42AEC5E9EBA0E6473F05 : __int32
```cpp
/* 63713 */
enum $FB2272BC94AC42AEC5E9EBA0E6473F05 : __int32
{
PTHREAD_MUTEX_TIMED_NP = 0x0,
PTHREAD_MUTEX_RECURSIVE_NP = 0x1,
PTHREAD_MUTEX_ERRORCHECK_NP = 0x2,
PTHREAD_MUTEX_ADAPTIVE_NP = 0x3,
PTHREAD_MUTEX_NORMAL = 0x0,
PTHREAD_MUTEX_RECURSIVE = 0x1,
PTHREAD_MUTEX_ERRORCHECK = 0x2,
PTHREAD_MUTEX_DEFAULT = 0x0,
PTHREAD_MUTEX_FAST_NP = 0x0,
};

```
#### ADRole : __int8
```cpp
/* 44518 */
enum ADRole : __int8
{
};

```
#### ADRole_0 : __int8
```cpp
/* 77426 */
enum ADRole_0 : __int8
{
Student = 0x0,
Teacher = 0x1,
Unknown_28 = 0x2,
};

```
#### ARVRPlatform : __int32
```cpp
/* 6920 */
enum ARVRPlatform : __int32
{
ARVR_None = 0x0,
ARVR_Rift = 0x1,
ARVR_Holographic = 0x2,
ARVR_WindowsMR = 0x3,
ARVR_OrbisVR = 0x4,
};

```
#### AbilitiesIndex : __int16
```cpp
/* 5596 */
enum AbilitiesIndex : __int16
{
Invalid_3 = 0xFFFF,
Build = 0x0,
Mine = 0x1,
DoorsAndSwitches = 0x2,
OpenContainers = 0x3,
AttackPlayers = 0x4,
AttackMobs = 0x5,
OperatorCommands = 0x6,
Teleport = 0x7,
ExposedAbilityCount = 0x8,
Invulnerable = 0x8,
Flying = 0x9,
MayFly = 0xA,
Instabuild = 0xB,
Lightning = 0xC,
FlySpeed = 0xD,
WalkSpeed = 0xE,
Muted = 0xF,
WorldBuilder = 0x10,
NoClip = 0x11,
AbilityCount = 0x12,
};

```
#### Ability::Options : __int8
```cpp
/* 3305 */
enum Ability::Options : __int8
{
None_2 = 0x0,
NoSave = 0x1,
CommandExposed = 0x2,
PermissionsInterfaceExposed = 0x4,
WorldbuilderOverrides = 0x8,
};

```
#### Ability::Type : __int8
```cpp
/* 3303 */
enum Ability::Type : __int8
{
Invalid_2 = 0x0,
Unset = 0x1,
Bool_0 = 0x2,
Float_0 = 0x3,
};

```
#### AbstractArrow::Data : __int32
```cpp
/* 454238 */
enum AbstractArrow::Data : __int32
{
OwnerID = 0x11,
};

```
#### ActionEvent::$35A09F5CCAEB66D754D2523C4A0226F8 : __int32
```cpp
/* 454220 */
enum ActionEvent::$35A09F5CCAEB66D754D2523C4A0226F8 : __int32
{
ACTION_MOVE_LEFT = 0x1,
ACTION_MOVE_RIGHT = 0x2,
ACTION_MOVE_FORWARD = 0x3,
ACTION_MOVE_BACKWARD = 0x4,
ACTION_ASCEND = 0x5,
ACTION_DESCEND = 0x6,
ACTION_PADDLE_LEFT = 0x7,
ACTION_PADDLE_RIGHT = 0x8,
ACTION_SNEAK = 0xA,
ACTION_JUMP = 0xB,
ACTION_SPRINT = 0xC,
ACTION_DISMOUNT = 0xE,
ACTION_MOB_EFFECTS = 0x14,
ACTION_DROP = 0x15,
ACTION_INVENTORY = 0x16,
ACTION_BUILD = 0x17,
ACTION_DESTROY = 0x18,
ACTION_INTERACT = 0x19,
ACTION_ATTACK = 0x1A,
ACTION_PAUSE = 0x1E,
ACTION_CHAT = 0x1F,
ACTION_CONSOLE = 0x20,
ACTION_THIRD_PERSON_VIEW = 0x21,
ACTION_SCOREBOARD = 0x22,
ACTION_CODE_BUILDER = 0x23,
ACTION_SLOT_0 = 0x32,
ACTION_SLOT_1 = 0x33,
ACTION_SLOT_2 = 0x34,
ACTION_SLOT_3 = 0x35,
ACTION_SLOT_4 = 0x36,
ACTION_SLOT_5 = 0x37,
ACTION_SLOT_6 = 0x38,
ACTION_SLOT_7 = 0x39,
ACTION_SLOT_8 = 0x3A,
ACTION_SLOT_9 = 0x3B,
ACTION_MENU_UP = 0x64,
ACTION_MENU_DOWN = 0x65,
ACTION_MENU_LEFT = 0x66,
ACTION_MENU_RIGHT = 0x67,
ACTION_MENU_OK = 0x68,
ACTION_MENU_CANCEL = 0x69,
ACTION_MENU_INVENTORY_DROP = 0x6A,
ACTION_MENU_INVENTORY_CANCEL = 0x6B,
ACTION_POINTER_PRESSED = 0x78,
ACTION_BUILD_OR_INTERACT = 0x82,
ACTION_DESTROY_OR_ATTACK = 0x83,
ACTION_BUILD_OR_ATTACK = 0x8C,
ACTION_DESTROY_OR_INTERACT = 0x8D,
};

```
#### ActionEvent::ActionState : __int32
```cpp
/* 89286 */
enum ActionEvent::ActionState : __int32
{
Start_1 = 0x1,
Stop = 0x2,
};

```
#### ActiveDirectoryAction : __int8
```cpp
/* 45336 */
enum ActiveDirectoryAction : __int8
{
DismissAndStartGame = 0x1,
DismissAndExitGame = 0x2,
};

```
#### Actor::InitializationMethod : __int8
```cpp
/* 77418 */
enum Actor::InitializationMethod : __int8
{
INVALID_0 = 0x0,
LOADED = 0x1,
SPAWNED = 0x2,
BORN = 0x3,
TRANSFORMED = 0x4,
UPDATED = 0x5,
EVENT = 0x6,
LEGACY = 0x7,
};

```
#### ActorAnimationType : __int32
```cpp
/* 125119 */
enum ActorAnimationType : __int32
{
Empty_0 = 0xFFFFFFFF,
SkeletalAnimation = 0x0,
AnimationController = 0x1,
AnimationControllerState = 0x2,
};

```
#### ActorBlockSyncMessage::MessageId : __int32
```cpp
/* 77420 */
enum ActorBlockSyncMessage::MessageId : __int32
{
NONE_5 = 0x0,
CREATE = 0x1,
DESTROY = 0x2,
};

```
#### ActorCategory : __int32
```cpp
/* 45376 */
enum ActorCategory : __int32
{
None_21 = 0x0,
Player_1 = 0x1,
Mob_0 = 0x2,
Monster_0 = 0x4,
Humandoid = 0x8,
Animal_0 = 0x10,
WaterSpawning = 0x20,
Pathable = 0x40,
Tamable = 0x80,
Ridable = 0x100,
Item_0 = 0x400,
Ambient_1 = 0x800,
Villager_0 = 0x1000,
Arthropod_0 = 0x2000,
Undead = 0x4000,
Zombie_0 = 0x8000,
Minecart_0 = 0x10000,
Boat = 0x20000,
NonTargetable = 0x40000,
BoatRideable_0 = 0x20100,
MinecartRidable = 0x10100,
HumanoidMonster = 0xC,
WaterAnimal_0 = 0x30,
TamableAnimal_0 = 0x90,
UndeadMob_0 = 0x4004,
ZombieMonster_0 = 0x8004,
EvocationIllagerMonster = 0x100C,
};

```
#### ActorDamageCause : __int32
```cpp
/* 44530 */
enum ActorDamageCause : __int32
{
None_18 = 0xFFFFFFFF,
Override = 0x0,
Contact = 0x1,
EntityAttack = 0x2,
Projectile_0 = 0x3,
Suffocation = 0x4,
Fall_0 = 0x5,
Fire_1 = 0x6,
FireTick = 0x7,
Lava_2 = 0x8,
Drowning = 0x9,
BlockExplosion = 0xA,
EntityExplosion = 0xB,
Void = 0xC,
Suicide = 0xD,
Magic = 0xE,
Wither = 0xF,
Starve = 0x10,
Anvil_1 = 0x11,
Thorns_0 = 0x12,
FallingBlock_0 = 0x13,
Piston_0 = 0x14,
FlyIntoWall = 0x15,
Magma = 0x16,
Fireworks_0 = 0x17,
Lightning_0 = 0x18,
Charging = 0x19,
Temperature = 0x1A,
All_0 = 0x1F,
};

```
#### ActorDataIDs : __int8
```cpp
/* 45375 */
enum ActorDataIDs : __int8
{
FLAGS = 0x0,
STRUCTURAL_INTEGRITY = 0x1,
VARIANT = 0x2,
COLOR_INDEX = 0x3,
NAME = 0x4,
OWNER = 0x5,
TARGET = 0x6,
AIR_SUPPLY = 0x7,
EFFECT_COLOR = 0x8,
EFFECT_AMBIENCE = 0x9,
JUMP_DURATION = 0xA,
HURT = 0xB,
HURT_DIR = 0xC,
ROW_TIME_LEFT = 0xD,
ROW_TIME_RIGHT = 0xE,
VALUE = 0xF,
DISPLAY_TILE_RUNTIME_ID = 0x10,
DISPLAY_OFFSET = 0x11,
CUSTOM_DISPLAY = 0x12,
SWELL = 0x13,
OLD_SWELL = 0x14,
SWELL_DIR = 0x15,
CHARGE_AMOUNT = 0x16,
CARRY_BLOCK_RUNTIME_ID = 0x17,
CLIENT_EVENT = 0x18,
USING_ITEM = 0x19,
PLAYER_FLAGS = 0x1A,
PLAYER_INDEX = 0x1B,
BED_POSITION = 0x1C,
X_POWER = 0x1D,
Y_POWER = 0x1E,
Z_POWER = 0x1F,
AUX_POWER = 0x20,
FISHX = 0x21,
FISHZ = 0x22,
FISHANGLE = 0x23,
AUX_VALUE_DATA = 0x24,
LEASH_HOLDER = 0x25,
SCALE = 0x26,
HAS_NPC = 0x27,
NPC_DATA = 0x28,
ACTIONS = 0x29,
AIR_SUPPLY_MAX = 0x2A,
MARK_VARIANT = 0x2B,
CONTAINER_TYPE = 0x2C,
CONTAINER_SIZE = 0x2D,
CONTAINER_STRENGTH_MODIFIER = 0x2E,
BLOCK_TARGET = 0x2F,
INV = 0x30,
TARGET_A = 0x31,
TARGET_B = 0x32,
TARGET_C = 0x33,
AERIAL_ATTACK = 0x34,
WIDTH = 0x35,
HEIGHT = 0x36,
FUSE_TIME = 0x37,
SEAT_OFFSET = 0x38,
SEAT_LOCK_RIDER_ROTATION = 0x39,
SEAT_LOCK_RIDER_ROTATION_DEGREES = 0x3A,
SEAT_ROTATION_OFFSET = 0x3B,
DATA_RADIUS = 0x3C,
DATA_WAITING = 0x3D,
DATA_PARTICLE = 0x3E,
PEEK_ID = 0x3F,
ATTACH_FACE = 0x40,
ATTACHED = 0x41,
ATTACH_POS = 0x42,
TRADE_TARGET = 0x43,
CAREER = 0x44,
HAS_COMMAND_BLOCK = 0x45,
COMMAND_NAME = 0x46,
LAST_COMMAND_OUTPUT = 0x47,
TRACK_COMMAND_OUTPUT = 0x48,
CONTROLLING_SEAT_INDEX = 0x49,
STRENGTH = 0x4A,
STRENGTH_MAX = 0x4B,
DATA_SPELL_CASTING_COLOR = 0x4C,
DATA_LIFETIME_TICKS = 0x4D,
POSE_INDEX = 0x4E,
DATA_TICK_OFFSET = 0x4F,
NAMETAG_ALWAYS_SHOW = 0x50,
COLOR_2_INDEX = 0x51,
NAME_AUTHOR = 0x52,
SCORE = 0x53,
BALLOON_ANCHOR = 0x54,
PUFFED_STATE = 0x55,
BUBBLE_TIME = 0x56,
AGENT = 0x57,
SITTING_AMOUNT = 0x58,
SITTING_AMOUNT_PREVIOUS = 0x59,
EATING_COUNTER = 0x5A,
FLAGS2 = 0x5B,
LAYING_AMOUNT = 0x5C,
LAYING_AMOUNT_PREVIOUS = 0x5D,
DATA_DURATION = 0x5E,
DATA_SPAWN_TIME = 0x5F,
DATA_CHANGE_RATE = 0x60,
DATA_CHANGE_ON_PICKUP = 0x61,
DATA_PICKUP_COUNT = 0x62,
INTERACT_TEXT = 0x63,
TRADE_TIER = 0x64,
MAX_TRADE_TIER = 0x65,
TRADE_EXPERIENCE = 0x66,
SKIN_ID = 0x67,
SPAWNING_FRAMES = 0x68,
COMMAND_BLOCK_TICK_DELAY = 0x69,
COMMAND_BLOCK_EXECUTE_ON_FIRST_TICK = 0x6A,
AMBIENT_SOUND_INTERVAL = 0x6B,
AMBIENT_SOUND_INTERVAL_RANGE = 0x6C,
AMBIENT_SOUND_EVENT_NAME = 0x6D,
FALL_DAMAGE_MULTIPLIER = 0x6E,
NAME_RAW_TEXT = 0x6F,
CAN_RIDE_TARGET = 0x70,
};

```
#### ActorEvent : __int8
```cpp
/* 48670 */
enum ActorEvent : __int8
{
NONE_1 = 0x0,
JUMP = 0x1,
HURT_0 = 0x2,
DEATH = 0x3,
START_ATTACKING = 0x4,
STOP_ATTACKING = 0x5,
TAMING_FAILED = 0x6,
TAMING_SUCCEEDED = 0x7,
SHAKE_WETNESS = 0x8,
EAT_GRASS = 0xA,
FISHHOOK_BUBBLE = 0xB,
FISHHOOK_FISHPOS = 0xC,
FISHHOOK_HOOKTIME = 0xD,
FISHHOOK_TEASE = 0xE,
SQUID_FLEEING = 0xF,
ZOMBIE_CONVERTING = 0x10,
PLAY_AMBIENT = 0x11,
SPAWN_ALIVE = 0x12,
START_OFFER_FLOWER = 0x13,
STOP_OFFER_FLOWER = 0x14,
LOVE_HEARTS = 0x15,
VILLAGER_ANGRY = 0x16,
VILLAGER_HAPPY = 0x17,
WITCH_HAT_MAGIC = 0x18,
FIREWORKS_EXPLODE = 0x19,
IN_LOVE_HEARTS = 0x1A,
SILVERFISH_MERGE_ANIM = 0x1B,
GUARDIAN_ATTACK_SOUND = 0x1C,
DRINK_POTION = 0x1D,
THROW_POTION = 0x1E,
PRIME_TNTCART = 0x1F,
PRIME_CREEPER = 0x20,
AIR_SUPPLY_0 = 0x21,
ADD_PLAYER_LEVELS = 0x22,
GUARDIAN_MINING_FATIGUE = 0x23,
AGENT_SWING_ARM = 0x24,
DRAGON_START_DEATH_ANIM = 0x25,
GROUND_DUST = 0x26,
SHAKE = 0x27,
FEED = 0x39,
BABY_EAT = 0x3C,
INSTANT_DEATH = 0x3D,
NOTIFY_TRADE = 0x3E,
LEASH_DESTROYED = 0x3F,
CARAVAN_UPDATED = 0x40,
TALISMAN_ACTIVATE = 0x41,
UPDATE_STRUCTURE_FEATURE = 0x42,
PLAYER_SPAWNED_MOB = 0x43,
PUKE = 0x44,
UPDATE_STACK_SIZE = 0x45,
START_SWIMMING = 0x46,
BALLOON_POP = 0x47,
TREASURE_HUNT = 0x48,
SUMMON_AGENT = 0x49,
FINISHED_CHARGING_CROSSBOW = 0x4A,
};

```
#### ActorFilterGroup::Processing : __int32
```cpp
/* 114144 */
enum ActorFilterGroup::Processing : __int32
{
Default_11 = 0x0,
ReadValue = 0x1,
ReadString = 0x2,
Environment = 0x3,
Item_1 = 0x4,
Armor_1 = 0x5,
Equipment_0 = 0x6,
};

```
#### ActorFlags : __int32
```cpp
/* 49718 */
enum ActorFlags : __int32
{
Unknown_25 = 0xFFFFFFFF,
ONFIRE = 0x0,
SNEAKING = 0x1,
RIDING = 0x2,
SPRINTING = 0x3,
USINGITEM = 0x4,
INVISIBLE = 0x5,
TEMPTED = 0x6,
INLOVE = 0x7,
SADDLED = 0x8,
POWERED = 0x9,
IGNITED = 0xA,
BABY = 0xB,
CONVERTING = 0xC,
CRITICAL = 0xD,
CAN_SHOW_NAME = 0xE,
ALWAYS_SHOW_NAME = 0xF,
NOAI = 0x10,
SILENT = 0x11,
WALLCLIMBING = 0x12,
CANCLIMB = 0x13,
CANSWIM = 0x14,
CANFLY = 0x15,
CANWALK = 0x16,
RESTING = 0x17,
SITTING = 0x18,
ANGRY = 0x19,
INTERESTED = 0x1A,
CHARGED = 0x1B,
TAMED = 0x1C,
ORPHANED = 0x1D,
LEASHED = 0x1E,
SHEARED = 0x1F,
GLIDING = 0x20,
ELDER = 0x21,
MOVING = 0x22,
BREATHING = 0x23,
CHESTED = 0x24,
STACKABLE = 0x25,
SHOW_BOTTOM = 0x26,
STANDING = 0x27,
SHAKING = 0x28,
IDLING = 0x29,
CASTING = 0x2A,
CHARGING = 0x2B,
WASD_CONTROLLED = 0x2C,
CAN_POWER_JUMP = 0x2D,
LINGERING = 0x2E,
HAS_COLLISION = 0x2F,
HAS_GRAVITY = 0x30,
FIRE_IMMUNE = 0x31,
DANCING = 0x32,
ENCHANTED = 0x33,
RETURNTRIDENT = 0x34,
CONTAINER_IS_PRIVATE = 0x35,
IS_TRANSFORMING = 0x36,
DAMAGENEARBYMOBS = 0x37,
SWIMMING = 0x38,
BRIBED = 0x39,
IS_PREGNANT = 0x3A,
LAYING_EGG = 0x3B,
RIDER_CAN_PICK = 0x3C,
TRANSITION_SITTING = 0x3D,
EATING = 0x3E,
LAYING_DOWN = 0x3F,
SNEEZING = 0x40,
TRUSTING = 0x41,
ROLLING = 0x42,
SCARED = 0x43,
IN_SCAFFOLDING = 0x44,
OVER_SCAFFOLDING = 0x45,
FALL_THROUGH_SCAFFOLDING = 0x46,
BLOCKING = 0x47,
TRANSITION_BLOCKING = 0x48,
BLOCKED_USING_SHIELD = 0x49,
BLOCKED_USING_DAMAGED_SHIELD = 0x4A,
SLEEPING = 0x4B,
WANTS_TO_WAKE = 0x4C,
TRADE_INTEREST = 0x4D,
DOOR_BREAKER = 0x4E,
BREAKING_OBSTRUCTION = 0x4F,
DOOR_OPENER = 0x50,
IS_ILLAGER_CAPTAIN = 0x51,
STUNNED = 0x52,
ROARING = 0x53,
DELAYED_ATTACK = 0x54,
IS_AVOIDING_MOBS = 0x55,
FACING_TARGET_TO_RANGE_ATTACK = 0x56,
HIDDEN_WHEN_INVISIBLE = 0x57,
IS_IN_UI = 0x58,
STALKING = 0x59,
EMOTING = 0x5A,
CELEBRATING = 0x5B,
Count_7 = 0x5C,
};

```
#### ActorInWeatherTest::WeatherType : __int32
```cpp
/* 456915 */
enum ActorInWeatherTest::WeatherType : __int32
{
Undefined_14 = 0xFFFFFFFF,
Clear_4 = 0x0,
Rain_0 = 0x1,
Snow_3 = 0x2,
Thunderstorm = 0x3,
};

```
#### ActorLinkType : __int8
```cpp
/* 35036 */
enum ActorLinkType : __int8
{
None_13 = 0x0,
Riding = 0x1,
Passenger = 0x2,
};

```
#### ActorLocation : __int32
```cpp
/* 48667 */
enum ActorLocation : __int32
{
Feet_0 = 0x0,
Body = 0x1,
WeaponAttachPoint = 0x2,
Head_0 = 0x3,
DropAttachPoint = 0x4,
ExplosionPoint = 0x5,
Eyes = 0x6,
BreathingPoint = 0x7,
Mouth = 0x8,
};

```
#### ActorTarget : __int32
```cpp
/* 48673 */
enum ActorTarget : __int32
{
This_0 = 0x0,
Killer = 0x1,
KillerPlayer = 0x2,
};

```
#### ActorTerrainInterlockData::VisibilityState : __int8
```cpp
/* 89260 */
enum ActorTerrainInterlockData::VisibilityState : __int8
{
InitialNotVisible = 0x0,
Visible_0 = 0x1,
DelayedDestructionNotVisible = 0x2,
};

```
#### ActorType : __int32
```cpp
/* 13183 */
enum ActorType : __int32
{
Undefined_2 = 0x1,
TypeMask = 0xFF,
Mob = 0x100,
PathfinderMob = 0x300,
Monster = 0xB00,
Animal = 0x1300,
TamableAnimal = 0x5300,
Ambient = 0x8100,
UndeadMob = 0x10B00,
ZombieMonster = 0x30B00,
Arthropod = 0x40B00,
Minecart = 0x80000,
SkeletonMonster = 0x110B00,
EquineAnimal = 0x205300,
Projectile = 0x400000,
AbstractArrow = 0x800000,
WaterAnimal = 0x2300,
VillagerBase = 0x1000300,
Chicken = 0x130A,
Cow = 0x130B,
Pig = 0x130C,
Sheep = 0x130D,
Wolf = 0x530E,
Villager = 0x100030F,
MushroomCow = 0x1310,
Squid = 0x2311,
Rabbit = 0x1312,
Bat = 0x8113,
IronGolem = 0x314,
SnowGolem = 0x315,
Ocelot = 0x5316,
Horse = 0x205317,
PolarBear = 0x131C,
Llama = 0x131D,
Parrot = 0x531E,
Dolphin = 0x231F,
Donkey = 0x205318,
Mule = 0x205319,
SkeletonHorse = 0x215B1A,
ZombieHorse = 0x215B1B,
Zombie = 0x30B20,
Creeper = 0xB21,
Skeleton = 0x110B22,
Spider = 0x40B23,
PigZombie = 0x10B24,
Slime = 0xB25,
EnderMan = 0xB26,
Silverfish = 0x40B27,
CaveSpider = 0x40B28,
Ghast = 0xB29,
LavaSlime = 0xB2A,
Blaze = 0xB2B,
ZombieVillager = 0x30B2C,
Witch = 0xB2D,
Stray = 0x110B2E,
Husk = 0x30B2F,
WitherSkeleton = 0x110B30,
Guardian = 0xB31,
ElderGuardian = 0xB32,
Npc = 0x133,
WitherBoss = 0x10B34,
Dragon = 0xB35,
Shulker = 0xB36,
Endermite = 0x40B37,
Agent = 0x138,
Vindicator = 0xB39,
Phantom = 0x10B3A,
IllagerBeast = 0xB3B,
ArmorStand = 0x13D,
TripodCamera = 0x13E,
Player_0 = 0x13F,
ItemEntity = 0x40,
PrimedTnt = 0x41,
FallingBlock = 0x42,
MovingBlock = 0x43,
ExperiencePotion = 0x400044,
Experience = 0x45,
EyeOfEnder = 0x46,
EnderCrystal = 0x47,
FireworksRocket = 0x48,
Trident = 0xC00049,
Turtle = 0x134A,
Cat = 0x534B,
ShulkerBullet = 0x40004C,
FishingHook = 0x4D,
Chalkboard = 0x4E,
DragonFireball = 0x40004F,
Arrow = 0xC00050,
Snowball = 0x400051,
ThrownEgg = 0x400052,
Painting = 0x53,
LargeFireball = 0x400055,
ThrownPotion = 0x400056,
Enderpearl = 0x400057,
LeashKnot = 0x58,
WitherSkull = 0x400059,
BoatRideable = 0x5A,
WitherSkullDangerous = 0x40005B,
LightningBolt = 0x5D,
SmallFireball = 0x40005E,
AreaEffectCloud = 0x5F,
LingeringPotion = 0x400065,
LlamaSpit = 0x400066,
EvocationFang = 0x400067,
EvocationIllager = 0xB68,
Vex = 0xB69,
MinecartRideable = 0x80054,
MinecartHopper = 0x80060,
MinecartTNT = 0x80061,
MinecartChest = 0x80062,
MinecartFurnace = 0x80063,
MinecartCommandBlock = 0x80064,
IceBomb = 0x40006A,
Balloon = 0x6B,
Pufferfish = 0x236C,
Salmon = 0x236D,
Drowned = 0x30B6E,
Tropicalfish = 0x236F,
Fish = 0x2370,
Panda = 0x1371,
Pillager = 0xB72,
VillagerV2 = 0x1000373,
ZombieVillagerV2 = 0x30B74,
Shield = 0x75,
WanderingTrader = 0x376,
Lectern = 0x77,
ElderGuardianGhost = 0xB78,
Fox = 0x1379,
Bee = 0x17A,
};

```
#### ActorTypeNamespaceRules : __int32
```cpp
/* 109111 */
enum ActorTypeNamespaceRules : __int32
{
ReturnWithoutNamespace = 0x0,
ReturnWithNamespace = 0x1,
};

```
#### AddTickingAreaStatus : __int32
```cpp
/* 190219 */
enum AddTickingAreaStatus : __int32
{
ExceededChunkLimit = 0x0,
ExceededTickingAreaLimit = 0x1,
ConflictingName = 0x2,
Success_12 = 0x3,
};

```
#### AdventureSettingsPacket::Flags : __int32
```cpp
/* 77410 */
enum AdventureSettingsPacket::Flags : __int32
{
WorldImmutable = 0x1,
NoPvM = 0x2,
NoMvP = 0x4,
Unused = 0x8,
ShowNameTags = 0x10,
AutoJump = 0x20,
PlayerMayFly = 0x40,
PlayerNoClip = 0x80,
PlayerWorldBuilder = 0x100,
PlayerFlying = 0x200,
PlayerMuted = 0x400,
};

```
#### AdventureSettingsPacket::PermissionsFlags : __int32
```cpp
/* 77409 */
enum AdventureSettingsPacket::PermissionsFlags : __int32
{
Mine_0 = 0x1,
DoorsAndSwitches_0 = 0x2,
OpenContainers_0 = 0x4,
AttackPlayers_0 = 0x8,
AttackMobs_0 = 0x10,
OP = 0x20,
Teleport_2 = 0x80,
Build_0 = 0x100,
DefaultLevelPermissions = 0x200,
};

```
#### AgentCommand::Mode : __int32
```cpp
/* 475754 */
enum AgentCommand::Mode : __int32
{
Attack_3 = 0x0,
Collect = 0x1,
Create_0 = 0x2,
Destroy_2 = 0x3,
Detect_0 = 0x4,
DetectRedstone = 0x5,
Drop = 0x6,
DropAll = 0x7,
GetItemCount = 0x8,
GetItemDetail = 0x9,
GetItemSpace = 0xA,
GetPosition = 0xB,
Inspect = 0xC,
InspectData = 0xD,
Move_0 = 0xE,
Place_6 = 0xF,
SetItem = 0x10,
Till = 0x11,
TP = 0x12,
Transfer_0 = 0x13,
Turn = 0x14,
};

```
#### AgentCommands::CollectCommand::CollectionSpecification : __int32
```cpp
/* 475803 */
enum AgentCommands::CollectCommand::CollectionSpecification : __int32
{
SpecificItem = 0x0,
AllItems = 0x1,
None_59 = 0x2,
};

```
#### AgentCommands::Direction : __int8
```cpp
/* 475705 */
enum AgentCommands::Direction : __int8
{
Up_1 = 0x0,
Down_1 = 0x1,
Forward = 0x2,
Back_0 = 0x3,
Left_2 = 0x4,
Right_2 = 0x5,
Undefined_15 = 0x6,
};

```
#### AggregateFeature<PlaceType::Arbitrary>::EarlyOut : __int32
```cpp
/* 256069 */
enum AggregateFeature<PlaceType::Arbitrary>::EarlyOut : __int32
{
None_51 = 0x0,
FirstFailure = 0x1,
FirstSuccess = 0x2,
};

```
#### AggregateFeature<PlaceType::Sequential>::EarlyOut : __int32
```cpp
/* 257231 */
enum AggregateFeature<PlaceType::Sequential>::EarlyOut : __int32
{
None_52 = 0x0,
FirstFailure_0 = 0x1,
FirstSuccess_0 = 0x2,
};

```
#### AnimatePacket::Action : __int32
```cpp
/* 77848 */
enum AnimatePacket::Action : __int32
{
NoAction = 0x0,
Swing = 0x1,
WakeUp = 0x3,
CriticalHit = 0x4,
MagicCriticalHit = 0x5,
RowRight = 0x80,
RowLeft = 0x81,
};

```
#### AnimationComponentGroup : __int32
```cpp
/* 88739 */
enum AnimationComponentGroup : __int32
{
Client_1 = 0x0,
ClientHUD = 0x1,
Server_1 = 0x2,
};

```
#### AnvilDamage : __int32
```cpp
/* 75527 */
enum AnvilDamage : __int32
{
Undamaged = 0x0,
SlightlyDamaged = 0x1,
VeryDamaged = 0x2,
Broken = 0x3,
_count_16 = 0x4,
};

```
#### AppFocusState : __int32
```cpp
/* 6919 */
enum AppFocusState : __int32
{
Focused = 0x0,
Unfocused = 0x1,
};

```
#### ArmorItem::Tier : __int32
```cpp
/* 180689 */
enum ArmorItem::Tier : __int32
{
TIER_LEATHER = 0x0,
TIER_CHAIN = 0x1,
TIER_IRON = 0x2,
TIER_DIAMOND = 0x3,
TIER_GOLD = 0x4,
TIER_ELYTRA = 0x5,
TIER_TURTLE = 0x6,
};

```
#### ArmorMaterialType : __int32
```cpp
/* 109098 */
enum ArmorMaterialType : __int32
{
None_38 = 0xFFFFFFFF,
DefaultArmor = 0x0,
EnchantedArmor = 0x1,
LeatherArmor = 0x2,
EnchantedLeatherArmor = 0x3,
};

```
#### ArmorSlot : __int32
```cpp
/* 13189 */
enum ArmorSlot : __int32
{
Head = 0x0,
Torso = 0x1,
Legs = 0x2,
Feet = 0x3,
_count_1 = 0x4,
};

```
#### ArmorTextureType : __int32
```cpp
/* 109099 */
enum ArmorTextureType : __int32
{
None_39 = 0xFFFFFFFF,
Leather = 0x0,
Chain_0 = 0x1,
Iron = 0x2,
Diamond = 0x3,
Gold = 0x4,
Elytra = 0x5,
Turtle_0 = 0x6,
};

```
#### Arrow::Data : __int32
```cpp
/* 173210 */
enum Arrow::Data : __int32
{
IsCritical = 0x10,
TippedAuxValue = 0x12,
};

```
#### AttachableSlotIndex : __int32
```cpp
/* 109092 */
enum AttachableSlotIndex : __int32
{
Head_3 = 0x0,
Torso_1 = 0x1,
Legs_2 = 0x2,
Feet_3 = 0x3,
CarriedItem = 0x4,
OffhandItem = 0x5,
_Count_1 = 0x6,
};

```
#### AttachmentType : __int32
```cpp
/* 230116 */
enum AttachmentType : __int32
{
Standing = 0x0,
Hanging = 0x1,
Side = 0x2,
Multiple = 0x3,
_count_48 = 0x4,
};

```
#### AttributeBuffType : __int32
```cpp
/* 109101 */
enum AttributeBuffType : __int32
{
Hunger = 0x0,
Saturation = 0x1,
Regeneration = 0x2,
Heal = 0x3,
Harm = 0x4,
Magic_0 = 0x5,
Wither_0 = 0x6,
Poison = 0x7,
FatalPoison = 0x8,
SelfHeal = 0x9,
Unknown_37 = 0xA,
None_40 = 0xB,
};

```
#### AttributeMessageTypes::$D202BB380D96D518A6C41FAAD128A520 : __int32
```cpp
/* 174375 */
enum AttributeMessageTypes::$D202BB380D96D518A6C41FAAD128A520 : __int32
{
EXHAUSTION = 0x0,
COUNT_11 = 0x1,
};

```
#### AttributeModifierOperation : __int32
```cpp
/* 115729 */
enum AttributeModifierOperation : __int32
{
OPERATION_ADDITION = 0x0,
OPERATION_MULTIPLY_BASE = 0x1,
OPERATION_MULTIPLY_TOTAL = 0x2,
OPERATION_CAP = 0x3,
TOTAL_OPERATIONS = 0x4,
OPERATION_INVALID = 0x4,
};

```
#### AttributeOperands : __int32
```cpp
/* 100208 */
enum AttributeOperands : __int32
{
OPERAND_MIN = 0x0,
OPERAND_MAX = 0x1,
OPERAND_CURRENT = 0x2,
TOTAL_OPERANDS = 0x3,
OPERAND_INVALID = 0x3,
};

```
#### Automation::MessagePurpose : __int8
```cpp
/* 430899 */
enum Automation::MessagePurpose : __int8
{
None_57 = 0x0,
RequestCommand = 0x1,
RequestSubscribe = 0x2,
RequestUnsubscribe = 0x3,
ResponseCommand = 0x4,
ResponseError = 0x5,
ResponseEvent = 0x6,
};

```
#### Automation::Response::Type : __int8
```cpp
/* 424406 */
enum Automation::Response::Type : __int8
{
Command_4 = 0x0,
Event_0 = 0x1,
};

```
#### BackgroundTask::TaskRunResult : __int32
```cpp
/* 484283 */
enum BackgroundTask::TaskRunResult : __int32
{
Requeue = 0x0,
Done_3 = 0x1,
Noop = 0x2,
};

```
#### BackgroundTask::TaskStatus : __int32
```cpp
/* 484165 */
enum BackgroundTask::TaskStatus : __int32
{
WaitingForPredecessor = 0x0,
Pending_0 = 0x1,
Running_1 = 0x2,
CancelPending = 0x3,
Canceled_3 = 0x4,
Error_7 = 0x5,
Done_2 = 0x6,
};

```
#### BackgroundWorker::RunOneResult : __int32
```cpp
/* 485400 */
enum BackgroundWorker::RunOneResult : __int32
{
NoTasks = 0x0,
TaskExecuted = 0x1,
Retry_0 = 0x2,
};

```
#### BackgroundWorker::State : __int32
```cpp
/* 485254 */
enum BackgroundWorker::State : __int32
{
Initializing_0 = 0x0,
Off_0 = 0x1,
Running_3 = 0x2,
};

```
#### BannerBlockType : __int32
```cpp
/* 180700 */
enum BannerBlockType : __int32
{
Default_13 = 0x0,
IllagerCaptain = 0x1,
};

```
#### BannerPatternItem::Type : __int32
```cpp
/* 183739 */
enum BannerPatternItem::Type : __int32
{
Creeper_0 = 0x0,
Skull_0 = 0x1,
Flower_0 = 0x2,
Thing = 0x3,
Bricks = 0x4,
Vines = 0x5,
_count_39 = 0x6,
};

```
#### BaseRailTransporter::RailType : __int32
```cpp
/* 223108 */
enum BaseRailTransporter::RailType : __int32
{
Activator = 0x0,
Power = 0x1,
};

```
#### BedSleepingResult : __int32
```cpp
/* 173069 */
enum BedSleepingResult : __int32
{
OK_2 = 0x0,
NOT_POSSIBLE_HERE = 0x1,
NOT_POSSIBLE_NOW = 0x2,
TOO_FAR_AWAY = 0x3,
OTHER_PROBLEM = 0x4,
NOT_SAFE = 0x5,
};

```
#### Bedrock::Threading::AsyncErrc : __int32
```cpp
/* 484153 */
enum Bedrock::Threading::AsyncErrc : __int32
{
operation_in_progress_0 = 0x1,
operation_canceled_0 = 0x2,
operation_threw_exception = 0x3,
unexpected_error = 0x4,
invalid_state = 0x5,
};

```
#### Bedrock::Threading::AsyncStatus : __int32
```cpp
/* 63702 */
enum Bedrock::Threading::AsyncStatus : __int32
{
Started_1 = 0x0,
Completed_1 = 0x1,
Canceled_2 = 0x2,
Error_2 = 0x3,
};

```
#### Bedrock::Threading::OSThreadPriority : __int32
```cpp
/* 5512 */
enum Bedrock::Threading::OSThreadPriority : __int32
{
High = 0x0,
Elevated = 0x1,
Normal = 0x2,
Low = 0x3,
};

```
#### BedrockLog::LogCategory : __int32
```cpp
/* 5582 */
enum BedrockLog::LogCategory : __int32
{
LogArea = 0x0,
LogWorldGen = 0x1,
LogLoot = 0x2,
LogRender = 0x3,
LogStructure = 0x4,
LogUI = 0x5,
LogOnline = 0x6,
NumLogCategories = 0x7,
};

```
#### BedrockLog::LogChannel : __int32
```cpp
/* 480294 */
enum BedrockLog::LogChannel : __int32
{
Global_0 = 0x0,
ClientSide = 0x1,
ServerSide = 0x2,
NumLogChannels = 0x3,
};

```
#### BedrockLog::LogRule : __int32
```cpp
/* 5583 */
enum BedrockLog::LogRule : __int32
{
DefaultRules = 0x0,
ClientAndServer = 0x1,
};

```
#### BehaviorData::DataType : __int8
```cpp
/* 50657 */
enum BehaviorData::DataType : __int8
{
BlockPosition = 0x0,
Boolean = 0x1,
Float_4 = 0x2,
Int_3 = 0x3,
String_2 = 0x4,
Vector3 = 0x5,
VoidPointer = 0x6,
};

```
#### BehaviorStatus : __int32
```cpp
/* 454219 */
enum BehaviorStatus : __int32
{
Success_14 = 0x0,
Running_0 = 0x1,
Failure_0 = 0x2,
Error_6 = 0x3,
Undefined_13 = 0x4,
};

```
#### Biome::BiomeTempCategory : __int32
```cpp
/* 177354 */
enum Biome::BiomeTempCategory : __int32
{
OCEAN = 0x0,
COLD_0 = 0x1,
MEDIUM = 0x2,
WARM_0 = 0x3,
};

```
#### BiomeComponentFactory::ComponentScope : __int32
```cpp
/* 190210 */
enum BiomeComponentFactory::ComponentScope : __int32
{
Client_3 = 0x0,
Server_3 = 0x1,
ClientAndServer_0 = 0x2,
};

```
#### BiomeComponentFactory::FactoryScope : __int32
```cpp
/* 88412 */
enum BiomeComponentFactory::FactoryScope : __int32
{
Client_0 = 0x0,
Server_0 = 0x1,
};

```
#### BiomeTemperatureCategory : __int8
```cpp
/* 39255 */
enum BiomeTemperatureCategory : __int8
{
Medium_0 = 0x0,
Warm = 0x1,
Lukewarm = 0x2,
Cold = 0x3,
Frozen = 0x4,
Count_4 = 0x5,
};

```
#### Blacklist::Duration : __int32
```cpp
/* 74634 */
enum Blacklist::Duration : __int32
{
Session = 0x0,
OneTime = 0x1,
Invalid_15 = 0x2,
};

```
#### BlockActorRendererId : __int32
```cpp
/* 235085 */
enum BlockActorRendererId : __int32
{
TR_DEFAULT_RENDERER = 0x0,
TR_CHEST_RENDERER = 0x1,
TR_SIGN_RENDERER = 0x2,
TR_MOBSPAWNER_RENDERER = 0x3,
TR_SKULL_RENDERER = 0x4,
TR_ENCHANTER_RENDERER = 0x5,
TR_PISTONARM_RENDERER = 0x6,
TR_ITEMFRAME_RENDERER = 0x7,
TR_MOVINGBLOCK_RENDERER = 0x8,
TR_CHALKBOARD_RENDERER = 0x9,
TR_BEACON_RENDERER = 0xA,
TR_ENDGATEWAY_RENDERER = 0xB,
TR_ENDERCHEST_RENDERER = 0xC,
TR_SHULKERBOX_RENDERER = 0xD,
TR_COMMANDBLOCK_RENDERER = 0xE,
TR_BED_RENDERER = 0xF,
TR_BANNER_RENDERER = 0x10,
TR_CONDUIT_RENDERER = 0x11,
TR_LECTERN_RENDERER = 0x12,
TR_BELL_RENDERER = 0x13,
TR_CAMPFIRE_RENDERER = 0x14,
};

```
#### BlockActorType : __int32
```cpp
/* 40864 */
enum BlockActorType : __int32
{
Undefined_6 = 0x0,
Furnace = 0x1,
Chest = 0x2,
NetherReactor = 0x3,
Sign = 0x4,
MobSpawner = 0x5,
Skull = 0x6,
FlowerPot = 0x7,
BrewingStand = 0x8,
EnchantingTable_0 = 0x9,
DaylightDetector = 0xA,
Music = 0xB,
Comparator = 0xC,
Dispenser = 0xD,
Dropper = 0xE,
Hopper = 0xF,
Cauldron = 0x10,
ItemFrame = 0x11,
PistonArm = 0x12,
MovingBlock_0 = 0x13,
Chalkboard_0 = 0x14,
Beacon = 0x15,
EndPortal = 0x16,
EnderChest = 0x17,
EndGateway = 0x18,
ShulkerBox = 0x19,
CommandBlock = 0x1A,
Bed_0 = 0x1B,
Banner = 0x1C,
StructureBlock = 0x20,
Jukebox = 0x21,
ChemistryTable = 0x22,
Conduit_0 = 0x23,
JigsawBlock = 0x24,
Lectern_0 = 0x25,
BlastFurnace = 0x26,
Smoker = 0x27,
Bell_0 = 0x28,
Campfire = 0x29,
BarrelBlock = 0x2A,
Beehive = 0x2B,
_count_14 = 0x2C,
};

```
#### BlockColor : __int8
```cpp
/* 35876 */
enum BlockColor : __int8
{
White = 0x0,
Orange = 0x1,
Magenta = 0x2,
Light_blue = 0x3,
Yellow = 0x4,
Lime = 0x5,
Pink = 0x6,
Gray = 0x7,
Silver = 0x8,
Cyan = 0x9,
Purple = 0xA,
Blue = 0xB,
Brown = 0xC,
Green = 0xD,
Red = 0xE,
Black = 0xF,
_count_11 = 0x10,
};

```
#### BlockProperty : __int64
```cpp
/* 115630 */
enum BlockProperty : __int64
{
None_43 = 0x0,
Stair = 0x1,
HalfSlab = 0x2,
Hopper_0 = 0x4,
TopSnow_0 = 0x8,
FenceGate = 0x10,
Leaf = 0x20,
ThinConnects2D = 0x40,
Connects2D = 0x80,
Carpet_0 = 0x100,
Button_0 = 0x200,
Door = 0x400,
Portal_3 = 0x800,
Heavy = 0x1000,
Snow_1 = 0x2000,
Trap = 0x4000,
Sign_0 = 0x8000,
Walkable = 0x10000,
PressurePlate = 0x20000,
PistonBlockGrabber = 0x40000,
TopSolidBlocking = 0x80000,
SolidBlocking = 0x100000,
CubeShaped = 0x200000,
Power_NO = 0x400000,
Power_BlockDown = 0x800000,
Immovable = 0x1000000,
BreakOnPush = 0x2000000,
Piston_1 = 0x4000000,
InfiniBurn = 0x8000000,
RequiresWorldBuilder = 0x10000000,
CausesDamage = 0x20000000,
BreaksWhenFallenOnByHeavy = 0x40000000,
OnlyPistonPush = 0x80000000,
Liquid_0 = 0x100000000,
CanBeBuiltOver = 0x200000000,
SnowRecoverable = 0x400000000,
Scaffolding = 0x800000000,
CanSupportCenterHangingBlock = 0x1000000000,
BreaksWhenHitByArrow = 0x2000000000,
Unwalkable = 0x4000000000,
Impenetrable = 0x8000000000,
Hollow = 0x10000000000,
OperatorBlock = 0x20000000000,
SupportedByFlowerPot = 0x40000000000,
PreventsJumping = 0x80000000000,
ContainsHoney = 0x100000000000,
Slime_2 = 0x200000000000,
};

```
#### BlockRenderLayer : __int32
```cpp
/* 223089 */
enum BlockRenderLayer : __int32
{
RENDERLAYER_DOUBLE_SIDED = 0x0,
RENDERLAYER_BLEND = 0x1,
RENDERLAYER_OPAQUE = 0x2,
RENDERLAYER_OPTIONAL_ALPHATEST = 0x3,
RENDERLAYER_ALPHATEST = 0x4,
RENDERLAYER_SEASONS_OPAQUE = 0x5,
RENDERLAYER_SEASONS_OPTIONAL_ALPHATEST = 0x6,
RENDERLAYER_ALPHATEST_SINGLE_SIDE = 0x7,
RENDERLAYER_ENDPORTAL = 0x8,
RENDERLAYER_BARRIER = 0x9,
RENDERLAYER_STRUCTURE_VOID = 0xA,
_RENDERLAYER_COUNT = 0xB,
};

```
#### BlockShape : __int32
```cpp
/* 116676 */
enum BlockShape : __int32
{
INVISIBLE_0 = 0xFFFFFFFF,
BLOCK = 0x0,
CROSS_TEXTURE = 0x1,
TORCH = 0x2,
FIRE_0 = 0x3,
WATER_0 = 0x4,
RED_DUST = 0x5,
ROWS = 0x6,
DOOR_0 = 0x7,
LADDER = 0x8,
RAIL = 0x9,
STAIRS = 0xA,
FENCE_0 = 0xB,
LEVER = 0xC,
CACTUS = 0xD,
BED = 0xE,
DIODE = 0xF,
IRON_FENCE = 0x12,
STEM = 0x13,
VINE = 0x14,
FENCE_GATE = 0x15,
CHEST = 0x16,
LILYPAD = 0x17,
BREWING_STAND_0 = 0x19,
PORTAL_FRAME = 0x1A,
COCOA = 0x1C,
TREE = 0x1F,
WALL = 0x20,
DOUBLE_PLANT = 0x28,
FLOWER_POT = 0x2A,
ANVIL_0 = 0x2B,
DRAGON_EGG = 0x2C,
STRUCTURE_VOID = 0x30,
BLOCK_HALF = 0x43,
TOP_SNOW = 0x44,
TRIPWIRE = 0x45,
TRIPWIRE_HOOK = 0x46,
CAULDRON_0 = 0x47,
REPEATER = 0x48,
COMPARATOR = 0x49,
HOPPER_0 = 0x4A,
SLIME_BLOCK = 0x4B,
PISTON = 0x4C,
BEACON_0 = 0x4D,
CHORUS_PLANT = 0x4E,
CHORUS_FLOWER = 0x4F,
END_PORTAL = 0x50,
END_ROD = 0x51,
END_GATEWAY = 0x52,
SKULL = 0x53,
FACING_BLOCK = 0x54,
COMMAND_BLOCK_0 = 0x55,
TERRACOTTA = 0x56,
DOUBLE_SIDE_FENCE = 0x57,
ITEM_FRAME = 0x58,
SHULKER_BOX = 0x59,
DOUBLESIDED_CROSS_TEXTURE = 0x5A,
DOUBLESIDED_DOUBLE_PLANT = 0x5B,
DOUBLESIDED_ROWS = 0x5C,
ELEMENT_BLOCK = 0x5D,
CHEMISTRY_TABLE = 0x5E,
CORAL_FAN = 0x60,
SEAGRASS = 0x61,
KELP = 0x62,
TRAPDOOR = 0x63,
SEA_PICKLE = 0x64,
CONDUIT = 0x65,
TURTLE_EGG = 0x66,
BUBBLE_COLUMN = 0x69,
BARRIER = 0x6A,
SIGN = 0x6B,
BAMBOO = 0x6C,
BAMBOO_SAPLING = 0x6D,
SCAFFOLDING = 0x6E,
GRINDSTONE_0 = 0x6F,
BELL = 0x70,
LANTERN = 0x71,
CAMPFIRE = 0x72,
LECTERN_0 = 0x73,
SWEET_BERRY_BUSH = 0x74,
CARTOGRAPHY_TABLE = 0x75,
COMPOSTER = 0x76,
STONE_CUTTER = 0x77,
HONEY_BLOCK = 0x78,
};

```
#### BlockSlot : __int32
```cpp
/* 426365 */
enum BlockSlot : __int32
{
None_56 = 0xFFFFFFFF,
Container_0 = 0x0,
_count_53 = 0x1,
};

```
#### BlockSoundType : __int32
```cpp
/* 294374 */
enum BlockSoundType : __int32
{
Normal_14 = 0x0,
Gravel = 0x1,
Wood_1 = 0x2,
Grass_0 = 0x3,
Metal_0 = 0x4,
Stone_3 = 0x5,
Cloth_0 = 0x6,
Glass_1 = 0x7,
Sand_0 = 0x8,
Snow_2 = 0x9,
Ladder = 0xA,
Anvil_2 = 0xB,
Slime_3 = 0xC,
Silent_0 = 0xD,
ItemFrame_1 = 0xE,
TurtleEgg = 0xF,
Bamboo = 0x10,
BambooSapling = 0x11,
Lantern = 0x12,
Scaffolding_0 = 0x13,
SweetBerryBush = 0x14,
Default_19 = 0x15,
Undefined_11 = 0x16,
};

```
#### BlockSupportType : __int32
```cpp
/* 173073 */
enum BlockSupportType : __int32
{
Center_0 = 0x0,
Edge = 0x1,
Any_3 = 0x2,
};

```
#### BoneAnimationRelativeMode : __int32
```cpp
/* 124453 */
enum BoneAnimationRelativeMode : __int32
{
Parent_0 = 0x0,
Entity_5 = 0x1,
};

```
#### BoneTransformType : __int32
```cpp
/* 124547 */
enum BoneTransformType : __int32
{
Position_0 = 0x0,
Rotation = 0x1,
Scale = 0x2,
_Count_2 = 0x3,
};

```
#### BookEditAction : __int8
```cpp
/* 76957 */
enum BookEditAction : __int8
{
ReplacePage = 0x0,
AddPage = 0x1,
DeletePage = 0x2,
SwapPages = 0x3,
Finalize = 0x4,
};

```
#### BossBarColor : __int32
```cpp
/* 51301 */
enum BossBarColor : __int32
{
PINK = 0x0,
BLUE = 0x1,
RED = 0x2,
GREEN = 0x3,
YELLOW = 0x4,
PURPLE = 0x5,
WHITE = 0x6,
};

```
#### BossBarOverlay : __int32
```cpp
/* 51302 */
enum BossBarOverlay : __int32
{
PROGRESS = 0x0,
NOTCHED_6 = 0x1,
NOTCHED_10 = 0x2,
NOTCHED_12 = 0x3,
NOTCHED_20 = 0x4,
};

```
#### BossEventUpdateType : __int32
```cpp
/* 51423 */
enum BossEventUpdateType : __int32
{
Add_0 = 0x0,
PlayerAdded = 0x1,
Remove = 0x2,
PlayerRemoved = 0x3,
Update_Percent = 0x4,
Update_Name = 0x5,
Update_Properties = 0x6,
Update_Style = 0x7,
};

```
#### Bounds::Option : __int32
```cpp
/* 37043 */
enum Bounds::Option : __int32
{
Default_5 = 0x0,
Flatten = 0x1,
};

```
#### BreathableComponent::BreathableState : __int32
```cpp
/* 51699 */
enum BreathableComponent::BreathableState : __int32
{
InAir = 0x0,
InWater = 0x1,
InLava = 0x2,
InSolids = 0x3,
InBreathableOverrideBlock = 0x4,
InNonBreathableOverrideBlock = 0x5,
};

```
#### BrewingStandBlockActor::$68235EB771568274AB23F364CDF33A71 : __int32
```cpp
/* 175306 */
enum BrewingStandBlockActor::$68235EB771568274AB23F364CDF33A71 : __int32
{
SLOT_INGREDIENT = 0x0,
SLOT_POTION1 = 0x1,
SLOT_POTION2 = 0x2,
SLOT_POTION3 = 0x3,
SLOT_FUEL = 0x4,
};

```
#### BrewingStandContainerData : __int32
```cpp
/* 175236 */
enum BrewingStandContainerData : __int32
{
SetBrewTime = 0x0,
SetFuelAmount = 0x1,
SetFuelTotal = 0x2,
};

```
#### BucketFillType : __int16
```cpp
/* 182771 */
enum BucketFillType : __int16
{
Unknown_43 = 0xFFFF,
Empty_1 = 0x0,
Milk_0 = 0x1,
Fish_0 = 0x2,
Salmon_0 = 0x3,
Tropicalfish_0 = 0x4,
Pufferfish_0 = 0x5,
Water_4 = 0x8,
Lava_5 = 0xA,
};

```
#### BuildPlatform : __int32
```cpp
/* 44652 */
enum BuildPlatform : __int32
{
Google = 0x1,
iOS = 0x2,
OSX = 0x3,
Amazon = 0x4,
GearVR_0 = 0x5,
UWP = 0x7,
Win32 = 0x8,
Dedicated = 0x9,
Orbis = 0xB,
Nx = 0xC,
Xbox_0 = 0xD,
WindowsPhone = 0xE,
Unknown_13 = 0xFFFFFFFF,
};

```
#### CSHA1::REPORT_TYPE : __int32
```cpp
/* 478098 */
enum CSHA1::REPORT_TYPE : __int32
{
REPORT_HEX = 0x0,
REPORT_DIGIT = 0x1,
REPORT_HEX_SHORT = 0x2,
};

```
#### CURLFORMcode : __int32
```cpp
/* 485598 */
enum CURLFORMcode : __int32
{
CURL_FORMADD_OK = 0x0,
CURL_FORMADD_MEMORY = 0x1,
CURL_FORMADD_OPTION_TWICE = 0x2,
CURL_FORMADD_NULL = 0x3,
CURL_FORMADD_UNKNOWN_OPTION = 0x4,
CURL_FORMADD_INCOMPLETE = 0x5,
CURL_FORMADD_ILLEGAL_ARRAY = 0x6,
CURL_FORMADD_DISABLED = 0x7,
CURL_FORMADD_LAST = 0x8,
};

```
#### CURLINFO : __int32
```cpp
/* 485600 */
enum CURLINFO : __int32
{
CURLINFO_NONE = 0x0,
CURLINFO_EFFECTIVE_URL = 0x100001,
CURLINFO_RESPONSE_CODE = 0x200002,
CURLINFO_TOTAL_TIME = 0x300003,
CURLINFO_NAMELOOKUP_TIME = 0x300004,
CURLINFO_CONNECT_TIME = 0x300005,
CURLINFO_PRETRANSFER_TIME = 0x300006,
CURLINFO_SIZE_UPLOAD = 0x300007,
CURLINFO_SIZE_DOWNLOAD = 0x300008,
CURLINFO_SPEED_DOWNLOAD = 0x300009,
CURLINFO_SPEED_UPLOAD = 0x30000A,
CURLINFO_HEADER_SIZE = 0x20000B,
CURLINFO_REQUEST_SIZE = 0x20000C,
CURLINFO_SSL_VERIFYRESULT = 0x20000D,
CURLINFO_FILETIME = 0x20000E,
CURLINFO_CONTENT_LENGTH_DOWNLOAD = 0x30000F,
CURLINFO_CONTENT_LENGTH_UPLOAD = 0x300010,
CURLINFO_STARTTRANSFER_TIME = 0x300011,
CURLINFO_CONTENT_TYPE = 0x100012,
CURLINFO_REDIRECT_TIME = 0x300013,
CURLINFO_REDIRECT_COUNT = 0x200014,
CURLINFO_PRIVATE = 0x100015,
CURLINFO_HTTP_CONNECTCODE = 0x200016,
CURLINFO_HTTPAUTH_AVAIL = 0x200017,
CURLINFO_PROXYAUTH_AVAIL = 0x200018,
CURLINFO_OS_ERRNO = 0x200019,
CURLINFO_NUM_CONNECTS = 0x20001A,
CURLINFO_SSL_ENGINES = 0x40001B,
CURLINFO_COOKIELIST = 0x40001C,
CURLINFO_LASTSOCKET = 0x20001D,
CURLINFO_FTP_ENTRY_PATH = 0x10001E,
CURLINFO_REDIRECT_URL = 0x10001F,
CURLINFO_PRIMARY_IP = 0x100020,
CURLINFO_APPCONNECT_TIME = 0x300021,
CURLINFO_CERTINFO = 0x400022,
CURLINFO_CONDITION_UNMET = 0x200023,
CURLINFO_LASTONE = 0x23,
};

```
#### CURLcode : __int32
```cpp
/* 485596 */
enum CURLcode : __int32
{
CURLE_OK = 0x0,
CURLE_UNSUPPORTED_PROTOCOL = 0x1,
CURLE_FAILED_INIT = 0x2,
CURLE_URL_MALFORMAT = 0x3,
CURLE_OBSOLETE4 = 0x4,
CURLE_COULDNT_RESOLVE_PROXY = 0x5,
CURLE_COULDNT_RESOLVE_HOST = 0x6,
CURLE_COULDNT_CONNECT = 0x7,
CURLE_FTP_WEIRD_SERVER_REPLY = 0x8,
CURLE_REMOTE_ACCESS_DENIED = 0x9,
CURLE_OBSOLETE10 = 0xA,
CURLE_FTP_WEIRD_PASS_REPLY = 0xB,
CURLE_OBSOLETE12 = 0xC,
CURLE_FTP_WEIRD_PASV_REPLY = 0xD,
CURLE_FTP_WEIRD_227_FORMAT = 0xE,
CURLE_FTP_CANT_GET_HOST = 0xF,
CURLE_OBSOLETE16 = 0x10,
CURLE_FTP_COULDNT_SET_TYPE = 0x11,
CURLE_PARTIAL_FILE = 0x12,
CURLE_FTP_COULDNT_RETR_FILE = 0x13,
CURLE_OBSOLETE20 = 0x14,
CURLE_QUOTE_ERROR = 0x15,
CURLE_HTTP_RETURNED_ERROR = 0x16,
CURLE_WRITE_ERROR = 0x17,
CURLE_OBSOLETE24 = 0x18,
CURLE_UPLOAD_FAILED = 0x19,
CURLE_READ_ERROR = 0x1A,
CURLE_OUT_OF_MEMORY = 0x1B,
CURLE_OPERATION_TIMEDOUT = 0x1C,
CURLE_OBSOLETE29 = 0x1D,
CURLE_FTP_PORT_FAILED = 0x1E,
CURLE_FTP_COULDNT_USE_REST = 0x1F,
CURLE_OBSOLETE32 = 0x20,
CURLE_RANGE_ERROR = 0x21,
CURLE_HTTP_POST_ERROR = 0x22,
CURLE_SSL_CONNECT_ERROR = 0x23,
CURLE_BAD_DOWNLOAD_RESUME = 0x24,
CURLE_FILE_COULDNT_READ_FILE = 0x25,
CURLE_LDAP_CANNOT_BIND = 0x26,
CURLE_LDAP_SEARCH_FAILED = 0x27,
CURLE_OBSOLETE40 = 0x28,
CURLE_FUNCTION_NOT_FOUND = 0x29,
CURLE_ABORTED_BY_CALLBACK = 0x2A,
CURLE_BAD_FUNCTION_ARGUMENT = 0x2B,
CURLE_OBSOLETE44 = 0x2C,
CURLE_INTERFACE_FAILED = 0x2D,
CURLE_OBSOLETE46 = 0x2E,
CURLE_TOO_MANY_REDIRECTS = 0x2F,
CURLE_UNKNOWN_TELNET_OPTION = 0x30,
CURLE_TELNET_OPTION_SYNTAX = 0x31,
CURLE_OBSOLETE50 = 0x32,
CURLE_PEER_FAILED_VERIFICATION = 0x33,
CURLE_GOT_NOTHING = 0x34,
CURLE_SSL_ENGINE_NOTFOUND = 0x35,
CURLE_SSL_ENGINE_SETFAILED = 0x36,
CURLE_SEND_ERROR = 0x37,
CURLE_RECV_ERROR = 0x38,
CURLE_OBSOLETE57 = 0x39,
CURLE_SSL_CERTPROBLEM = 0x3A,
CURLE_SSL_CIPHER = 0x3B,
CURLE_SSL_CACERT = 0x3C,
CURLE_BAD_CONTENT_ENCODING = 0x3D,
CURLE_LDAP_INVALID_URL = 0x3E,
CURLE_FILESIZE_EXCEEDED = 0x3F,
CURLE_USE_SSL_FAILED = 0x40,
CURLE_SEND_FAIL_REWIND = 0x41,
CURLE_SSL_ENGINE_INITFAILED = 0x42,
CURLE_LOGIN_DENIED = 0x43,
CURLE_TFTP_NOTFOUND = 0x44,
CURLE_TFTP_PERM = 0x45,
CURLE_REMOTE_DISK_FULL = 0x46,
CURLE_TFTP_ILLEGAL = 0x47,
CURLE_TFTP_UNKNOWNID = 0x48,
CURLE_REMOTE_FILE_EXISTS = 0x49,
CURLE_TFTP_NOSUCHUSER = 0x4A,
CURLE_CONV_FAILED = 0x4B,
CURLE_CONV_REQD = 0x4C,
CURLE_SSL_CACERT_BADFILE = 0x4D,
CURLE_REMOTE_FILE_NOT_FOUND = 0x4E,
CURLE_SSH = 0x4F,
CURLE_SSL_SHUTDOWN_FAILED = 0x50,
CURLE_AGAIN = 0x51,
CURLE_SSL_CRL_BADFILE = 0x52,
CURLE_SSL_ISSUER_ERROR = 0x53,
CURL_LAST = 0x54,
};

```
#### CURLoption : __int32
```cpp
/* 485597 */
enum CURLoption : __int32
{
CURLOPT_FILE = 0x2711,
CURLOPT_URL = 0x2712,
CURLOPT_PORT = 0x3,
CURLOPT_PROXY = 0x2714,
CURLOPT_USERPWD = 0x2715,
CURLOPT_PROXYUSERPWD = 0x2716,
CURLOPT_RANGE = 0x2717,
CURLOPT_INFILE = 0x2719,
CURLOPT_ERRORBUFFER = 0x271A,
CURLOPT_WRITEFUNCTION = 0x4E2B,
CURLOPT_READFUNCTION = 0x4E2C,
CURLOPT_TIMEOUT = 0xD,
CURLOPT_INFILESIZE = 0xE,
CURLOPT_POSTFIELDS = 0x271F,
CURLOPT_REFERER = 0x2720,
CURLOPT_FTPPORT = 0x2721,
CURLOPT_USERAGENT = 0x2722,
CURLOPT_LOW_SPEED_LIMIT = 0x13,
CURLOPT_LOW_SPEED_TIME = 0x14,
CURLOPT_RESUME_FROM = 0x15,
CURLOPT_COOKIE = 0x2726,
CURLOPT_HTTPHEADER = 0x2727,
CURLOPT_HTTPPOST = 0x2728,
CURLOPT_SSLCERT = 0x2729,
CURLOPT_KEYPASSWD = 0x272A,
CURLOPT_CRLF = 0x1B,
CURLOPT_QUOTE = 0x272C,
CURLOPT_WRITEHEADER = 0x272D,
CURLOPT_COOKIEFILE = 0x272F,
CURLOPT_SSLVERSION = 0x20,
CURLOPT_TIMECONDITION = 0x21,
CURLOPT_TIMEVALUE = 0x22,
CURLOPT_CUSTOMREQUEST = 0x2734,
CURLOPT_STDERR = 0x2735,
CURLOPT_POSTQUOTE = 0x2737,
CURLOPT_WRITEINFO = 0x2738,
CURLOPT_VERBOSE = 0x29,
CURLOPT_HEADER = 0x2A,
CURLOPT_NOPROGRESS = 0x2B,
CURLOPT_NOBODY = 0x2C,
CURLOPT_FAILONERROR = 0x2D,
CURLOPT_UPLOAD = 0x2E,
CURLOPT_POST = 0x2F,
CURLOPT_DIRLISTONLY = 0x30,
CURLOPT_APPEND = 0x32,
CURLOPT_NETRC = 0x33,
CURLOPT_FOLLOWLOCATION = 0x34,
CURLOPT_TRANSFERTEXT = 0x35,
CURLOPT_PUT = 0x36,
CURLOPT_PROGRESSFUNCTION = 0x4E58,
CURLOPT_PROGRESSDATA = 0x2749,
CURLOPT_AUTOREFERER = 0x3A,
CURLOPT_PROXYPORT = 0x3B,
CURLOPT_POSTFIELDSIZE = 0x3C,
CURLOPT_HTTPPROXYTUNNEL = 0x3D,
CURLOPT_INTERFACE = 0x274E,
CURLOPT_KRBLEVEL = 0x274F,
CURLOPT_SSL_VERIFYPEER = 0x40,
CURLOPT_CAINFO = 0x2751,
CURLOPT_MAXREDIRS = 0x44,
CURLOPT_FILETIME = 0x45,
CURLOPT_TELNETOPTIONS = 0x2756,
CURLOPT_MAXCONNECTS = 0x47,
CURLOPT_CLOSEPOLICY = 0x48,
CURLOPT_FRESH_CONNECT = 0x4A,
CURLOPT_FORBID_REUSE = 0x4B,
CURLOPT_RANDOM_FILE = 0x275C,
CURLOPT_EGDSOCKET = 0x275D,
CURLOPT_CONNECTTIMEOUT = 0x4E,
CURLOPT_HEADERFUNCTION = 0x4E6F,
CURLOPT_HTTPGET = 0x50,
CURLOPT_SSL_VERIFYHOST = 0x51,
CURLOPT_COOKIEJAR = 0x2762,
CURLOPT_SSL_CIPHER_LIST = 0x2763,
CURLOPT_HTTP_VERSION = 0x54,
CURLOPT_FTP_USE_EPSV = 0x55,
CURLOPT_SSLCERTTYPE = 0x2766,
CURLOPT_SSLKEY = 0x2767,
CURLOPT_SSLKEYTYPE = 0x2768,
CURLOPT_SSLENGINE = 0x2769,
CURLOPT_SSLENGINE_DEFAULT = 0x5A,
CURLOPT_DNS_USE_GLOBAL_CACHE = 0x5B,
CURLOPT_DNS_CACHE_TIMEOUT = 0x5C,
CURLOPT_PREQUOTE = 0x276D,
CURLOPT_DEBUGFUNCTION = 0x4E7E,
CURLOPT_DEBUGDATA = 0x276F,
CURLOPT_COOKIESESSION = 0x60,
CURLOPT_CAPATH = 0x2771,
CURLOPT_BUFFERSIZE = 0x62,
CURLOPT_NOSIGNAL = 0x63,
CURLOPT_SHARE = 0x2774,
CURLOPT_PROXYTYPE = 0x65,
CURLOPT_ENCODING = 0x2776,
CURLOPT_PRIVATE = 0x2777,
CURLOPT_HTTP200ALIASES = 0x2778,
CURLOPT_UNRESTRICTED_AUTH = 0x69,
CURLOPT_FTP_USE_EPRT = 0x6A,
CURLOPT_HTTPAUTH = 0x6B,
CURLOPT_SSL_CTX_FUNCTION = 0x4E8C,
CURLOPT_SSL_CTX_DATA = 0x277D,
CURLOPT_FTP_CREATE_MISSING_DIRS = 0x6E,
CURLOPT_PROXYAUTH = 0x6F,
CURLOPT_FTP_RESPONSE_TIMEOUT = 0x70,
CURLOPT_IPRESOLVE = 0x71,
CURLOPT_MAXFILESIZE = 0x72,
CURLOPT_INFILESIZE_LARGE = 0x75A3,
CURLOPT_RESUME_FROM_LARGE = 0x75A4,
CURLOPT_MAXFILESIZE_LARGE = 0x75A5,
CURLOPT_NETRC_FILE = 0x2786,
CURLOPT_USE_SSL = 0x77,
CURLOPT_POSTFIELDSIZE_LARGE = 0x75A8,
CURLOPT_TCP_NODELAY = 0x79,
CURLOPT_FTPSSLAUTH = 0x81,
CURLOPT_IOCTLFUNCTION = 0x4EA2,
CURLOPT_IOCTLDATA = 0x2793,
CURLOPT_FTP_ACCOUNT = 0x2796,
CURLOPT_COOKIELIST = 0x2797,
CURLOPT_IGNORE_CONTENT_LENGTH = 0x88,
CURLOPT_FTP_SKIP_PASV_IP = 0x89,
CURLOPT_FTP_FILEMETHOD = 0x8A,
CURLOPT_LOCALPORT = 0x8B,
CURLOPT_LOCALPORTRANGE = 0x8C,
CURLOPT_CONNECT_ONLY = 0x8D,
CURLOPT_CONV_FROM_NETWORK_FUNCTION = 0x4EAE,
CURLOPT_CONV_TO_NETWORK_FUNCTION = 0x4EAF,
CURLOPT_CONV_FROM_UTF8_FUNCTION = 0x4EB0,
CURLOPT_MAX_SEND_SPEED_LARGE = 0x75C1,
CURLOPT_MAX_RECV_SPEED_LARGE = 0x75C2,
CURLOPT_FTP_ALTERNATIVE_TO_USER = 0x27A3,
CURLOPT_SOCKOPTFUNCTION = 0x4EB4,
CURLOPT_SOCKOPTDATA = 0x27A5,
CURLOPT_SSL_SESSIONID_CACHE = 0x96,
CURLOPT_SSH_AUTH_TYPES = 0x97,
CURLOPT_SSH_PUBLIC_KEYFILE = 0x27A8,
CURLOPT_SSH_PRIVATE_KEYFILE = 0x27A9,
CURLOPT_FTP_SSL_CCC = 0x9A,
CURLOPT_TIMEOUT_MS = 0x9B,
CURLOPT_CONNECTTIMEOUT_MS = 0x9C,
CURLOPT_HTTP_TRANSFER_DECODING = 0x9D,
CURLOPT_HTTP_CONTENT_DECODING = 0x9E,
CURLOPT_NEW_FILE_PERMS = 0x9F,
CURLOPT_NEW_DIRECTORY_PERMS = 0xA0,
CURLOPT_POSTREDIR = 0xA1,
CURLOPT_SSH_HOST_PUBLIC_KEY_MD5 = 0x27B2,
CURLOPT_OPENSOCKETFUNCTION = 0x4EC3,
CURLOPT_OPENSOCKETDATA = 0x27B4,
CURLOPT_COPYPOSTFIELDS = 0x27B5,
CURLOPT_PROXY_TRANSFER_MODE = 0xA6,
CURLOPT_SEEKFUNCTION = 0x4EC7,
CURLOPT_SEEKDATA = 0x27B8,
CURLOPT_CRLFILE = 0x27B9,
CURLOPT_ISSUERCERT = 0x27BA,
CURLOPT_ADDRESS_SCOPE = 0xAB,
CURLOPT_CERTINFO = 0xAC,
CURLOPT_USERNAME = 0x27BD,
CURLOPT_PASSWORD = 0x27BE,
CURLOPT_PROXYUSERNAME = 0x27BF,
CURLOPT_PROXYPASSWORD = 0x27C0,
CURLOPT_NOPROXY = 0x27C1,
CURLOPT_TFTP_BLKSIZE = 0xB2,
CURLOPT_SOCKS5_GSSAPI_SERVICE = 0x27C3,
CURLOPT_SOCKS5_GSSAPI_NEC = 0xB4,
CURLOPT_PROTOCOLS = 0xB5,
CURLOPT_REDIR_PROTOCOLS = 0xB6,
CURLOPT_SSH_KNOWNHOSTS = 0x27C7,
CURLOPT_SSH_KEYFUNCTION = 0x4ED8,
CURLOPT_SSH_KEYDATA = 0x27C9,
CURLOPT_LASTENTRY = 0x27CA,
};

```
#### CameraItemComponent::UseAction : __int8
```cpp
/* 457057 */
enum CameraItemComponent::UseAction : __int8
{
None_58 = 0x0,
Place_5 = 0x1,
Use_2 = 0x2,
};

```
#### CauldronLiquidType : __int32
```cpp
/* 109113 */
enum CauldronLiquidType : __int32
{
Water_1 = 0x0,
Lava_3 = 0x1,
_count_22 = 0x2,
};

```
#### ChalkboardSize : __int8
```cpp
/* 44598 */
enum ChalkboardSize : __int8
{
OnebyOne = 0x0,
TwobyOne = 0x1,
ThreebyTwo = 0x2,
Invalid_11 = 0x3,
};

```
#### ChangeDimensionRequest::State : __int32
```cpp
/* 89835 */
enum ChangeDimensionRequest::State : __int32
{
PrepareRegion = 0x0,
WaitingForChunks = 0x1,
WaitingForRespawn = 0x2,
};

```
#### ChangeSettingCommand::Setting : __int32
```cpp
/* 6170 */
enum ChangeSettingCommand::Setting : __int32
{
AllowCheats = 0x0,
Difficulty = 0x1,
};

```
#### ChannelTransformAxisType : __int32
```cpp
/* 124575 */
enum ChannelTransformAxisType : __int32
{
Uniform = 0x0,
XYZ = 0x1,
Arbitrary = 0x2,
_Count_3 = 0x3,
};

```
#### ChemistryTableType : __int32
```cpp
/* 175329 */
enum ChemistryTableType : __int32
{
CompoundCreator = 0x0,
MaterialReducer = 0x1,
ElementConstructor = 0x2,
LabTable_0 = 0x3,
_count_25 = 0x4,
};

```
#### ChestBlock::ChestType : __int32
```cpp
/* 251038 */
enum ChestBlock::ChestType : __int32
{
TYPE_BASIC = 0x0,
TYPE_TRAP = 0x1,
TYPE_ENDER = 0x2,
};

```
#### ChiselType : __int32
```cpp
/* 183665 */
enum ChiselType : __int32
{
Default_14 = 0x0,
Chiseled_0 = 0x1,
Lines = 0x2,
Smooth_0 = 0x3,
_count_30 = 0x4,
};

```
#### ChunkCachedDataState : __int8
```cpp
/* 34996 */
enum ChunkCachedDataState : __int8
{
NotGenerated = 0x0,
Generating_0 = 0x1,
Generated_2 = 0x2,
};

```
#### ChunkDebugDisplaySavedState : __int8
```cpp
/* 34995 */
enum ChunkDebugDisplaySavedState : __int8
{
Generated_1 = 0x0,
Saved = 0x1,
};

```
#### ChunkSource::LoadMode : __int32
```cpp
/* 172975 */
enum ChunkSource::LoadMode : __int32
{
None_47 = 0x0,
Deferred = 0x1,
};

```
#### ChunkState : __int8
```cpp
/* 33525 */
enum ChunkState : __int8
{
Unloaded = 0x0,
Generating = 0x1,
Generated = 0x2,
PostProcessing = 0x3,
PostProcessed = 0x4,
CheckingForReplacementData = 0x5,
NeedsLighting = 0x6,
Lighting_0 = 0x7,
Loaded = 0x8,
};

```
#### ChunkTerrainDataState : __int8
```cpp
/* 34994 */
enum ChunkTerrainDataState : __int8
{
NoData_0 = 0x0,
NeedsFixup = 0x1,
ReadyForGeneration = 0x2,
Generated_0 = 0x3,
PostProcessed_0 = 0x4,
Ready = 0x5,
};

```
#### ClientPlayMode : __int32
```cpp
/* 80052 */
enum ClientPlayMode : __int32
{
Normal_5 = 0x0,
Teaser = 0x1,
Screen = 0x2,
Viewer = 0x3,
Reality = 0x4,
Placement = 0x5,
LivingRoom = 0x6,
ExitLevel = 0x7,
ExitLevelLivingRoom = 0x8,
NumModes = 0x9,
};

```
#### ClientboundMapItemDataPacket::Type : __int32
```cpp
/* 78627 */
enum ClientboundMapItemDataPacket::Type : __int32
{
Invalid_16 = 0x0,
TextureUpdate = 0x2,
DecorationUpdate = 0x4,
Creation = 0x8,
};

```
#### CloneCommand::CloneMode : __int32
```cpp
/* 424801 */
enum CloneCommand::CloneMode : __int32
{
Normal_15 = 0x0,
Force = 0x1,
Move = 0x2,
};

```
#### CloneCommand::MaskMode : __int32
```cpp
/* 424752 */
enum CloneCommand::MaskMode : __int32
{
Replace_0 = 0x0,
Filtered = 0x1,
Masked = 0x2,
};

```
#### ColorFormat::ColorEnum::AvailableColors : __int32
```cpp
/* 101397 */
enum ColorFormat::ColorEnum::AvailableColors : __int32
{
BLACK = 0x0,
DARK_BLUE = 0x1,
DARK_GREEN = 0x2,
DARK_AQUA = 0x3,
DARK_RED = 0x4,
DARK_PURPLE = 0x5,
GOLD = 0x6,
GRAY = 0x7,
DARK_GRAY = 0x8,
BLUE_0 = 0x9,
GREEN_0 = 0xA,
AQUA = 0xB,
RED_0 = 0xC,
LIGHT_PURPLE = 0xD,
YELLOW_0 = 0xE,
WHITE_0 = 0xF,
MINECOIN_GOLD = 0x10,
COUNT_6 = 0x11,
};

```
#### ColoredTorchColor : __int8
```cpp
/* 251041 */
enum ColoredTorchColor : __int8
{
Red_7 = 0x0,
Green_2 = 0x1,
Blue_3 = 0x2,
Purple_3 = 0x3,
Invalid_27 = 0x4,
};

```
#### CommandBlockMode : __int16
```cpp
/* 44536 */
enum CommandBlockMode : __int16
{
Normal_3 = 0x0,
Repeating = 0x1,
Chain = 0x2,
};

```
#### CommandCheatFlag : __int8
```cpp
/* 5653 */
enum CommandCheatFlag : __int8
{
Cheat = 0x0,
NotCheat = 0x40,
};

```
#### CommandExecuteFlag : __int8
```cpp
/* 5651 */
enum CommandExecuteFlag : __int8
{
Allowed = 0x0,
Disallowed = 0x10,
};

```
#### CommandLexer::TokenType : __int32
```cpp
/* 5667 */
enum CommandLexer::TokenType : __int32
{
Error_0 = 0x0,
Integer = 0x1,
NInteger = 0x2,
Identifier = 0x3,
Selector = 0x4,
Slash = 0x5,
Value = 0x6,
RValue = 0x7,
LValue = 0x8,
Equals = 0x9,
Comma = 0xA,
Colon = 0xB,
Not = 0xC,
Asterisk = 0xD,
Hash = 0xE,
OpenBracket = 0xF,
CloseBracket = 0x10,
OpenBrace = 0x11,
CloseBrace = 0x12,
String = 0x13,
Range = 0x14,
LessThan = 0x15,
GreaterThan = 0x16,
PlusEquals = 0x17,
MinusEquals = 0x18,
TimesEquals = 0x19,
DivideEquals = 0x1A,
ModEquals = 0x1B,
GreaterThanLessThan = 0x1C,
Unknown_1 = 0x1D,
End = 0x1E,
};

```
#### CommandOperator : __int8
```cpp
/* 5684 */
enum CommandOperator : __int8
{
};

```
#### CommandOperator_0 : __int8
```cpp
/* 92672 */
enum CommandOperator_0 : __int8
{
Invalid_19 = 0x0,
Equals_0 = 0x1,
PlusEquals_0 = 0x2,
MinusEquals_0 = 0x3,
TimesEquals_0 = 0x4,
DivideEquals_0 = 0x5,
ModEquals_0 = 0x6,
MinEquals = 0x7,
MaxEquals = 0x8,
Swap = 0x9,
};

```
#### CommandOriginSystem : __int32
```cpp
/* 88548 */
enum CommandOriginSystem : __int32
{
AnimationTimelineSystem = 0x0,
};

```
#### CommandOriginType : __int8
```cpp
/* 78801 */
enum CommandOriginType : __int8
{
Player_4 = 0x0,
CommandBlock_0 = 0x1,
MinecartCommandBlock_0 = 0x2,
DevConsole = 0x3,
Test_0 = 0x4,
AutomationPlayer = 0x5,
ClientAutomation = 0x6,
DedicatedServer = 0x7,
Entity_4 = 0x8,
Virtual = 0x9,
GameArgument = 0xA,
EntityServer = 0xB,
Precompiled = 0xC,
GameMasterEntityServer = 0xD,
Scripting_1 = 0xE,
};

```
#### CommandOutputMessageType : __int32
```cpp
/* 6318 */
enum CommandOutputMessageType : __int32
{
Success_0 = 0x0,
Error_1 = 0x1,
};

```
#### CommandOutputParameter::NoCountType : __int32
```cpp
/* 6315 */
enum CommandOutputParameter::NoCountType : __int32
{
NoCount = 0x0,
};

```
#### CommandOutputType : __int32
```cpp
/* 5687 */
enum CommandOutputType : __int32
{
None_7 = 0x0,
LastOutput = 0x1,
Silent = 0x2,
AllOutput = 0x3,
DataSet = 0x4,
};

```
#### CommandParameterDataType : __int32
```cpp
/* 1617 */
enum CommandParameterDataType : __int32
{
Basic = 0x0,
Enum = 0x1,
SoftEnum = 0x2,
Postfix = 0x3,
};

```
#### CommandParameterOption : __int8
```cpp
/* 1618 */
enum CommandParameterOption : __int8
{
None_1 = 0x0,
EnumAutocompleteExpansion = 0x1,
HasSemanticConstraint = 0x2,
};

```
#### CommandPermissionLevel : __int8
```cpp
/* 1619 */
enum CommandPermissionLevel : __int8
{
Any = 0x0,
GameMasters = 0x1,
Admin = 0x2,
Host = 0x3,
Owner = 0x4,
Internal = 0x5,
};

```
#### CommandRegistry::HardNonTerminal : __int32
```cpp
/* 5669 */
enum CommandRegistry::HardNonTerminal : __int32
{
Epsilon = 0x100000,
Int_0 = 0x100001,
Val = 0x100002,
RVal = 0x100003,
WildcardInt = 0x100004,
Operator_0 = 0x100005,
Selection = 0x100006,
WildcardSelection = 0x100007,
NonIdSelector = 0x100008,
ScoresArg = 0x100009,
ScoresArgs = 0x10000A,
ScoreSelectParam = 0x10000B,
ScoreSelector = 0x10000C,
TagSelector = 0x10000D,
FilePath = 0x10000E,
FilePathVal = 0x10000F,
FilePathCont = 0x100010,
IntegerRangeVal = 0x100011,
IntegerRangePostVal = 0x100012,
IntegerRange = 0x100013,
FullIntegerRange = 0x100014,
SelArgs = 0x100015,
Args = 0x100016,
Arg = 0x100017,
MArg = 0x100018,
MValue = 0x100019,
NameArg = 0x10001A,
TypeArg = 0x10001B,
TagArg = 0x10001C,
Id = 0x10001D,
IdCont = 0x10001E,
CoordXInt = 0x10001F,
CoordYInt = 0x100020,
CoordZInt = 0x100021,
CoordXFloat = 0x100022,
CoordYFloat = 0x100023,
CoordZFloat = 0x100024,
Position = 0x100025,
PositionFloat = 0x100026,
MessageExp = 0x100027,
Message_0 = 0x100028,
MessageRoot = 0x100029,
PostSelector = 0x10002A,
RawText = 0x10002B,
RawTextCont = 0x10002C,
JsonValue = 0x10002D,
JsonField = 0x10002E,
JsonObject = 0x10002F,
JsonObjectFields = 0x100030,
JsonObjectCont = 0x100031,
JsonArray = 0x100032,
JsonArrayValues = 0x100033,
JsonArrayCont = 0x100034,
Command = 0x100035,
SlashCommand = 0x100036,
};

```
#### CommandSelectionOrder : __int32
```cpp
/* 33043 */
enum CommandSelectionOrder : __int32
{
Sorted = 0x0,
InverseSorted = 0x1,
Random = 0x2,
};

```
#### CommandSelectionType : __int32
```cpp
/* 33042 */
enum CommandSelectionType : __int32
{
Self_0 = 0x0,
Entities = 0x1,
Players = 0x2,
DefaultPlayers = 0x3,
OwnedAgent = 0x4,
Agents = 0x5,
};

```
#### CommandStatus : __int32
```cpp
/* 5680 */
enum CommandStatus : __int32
{
Invalid_6 = 0x0,
Local_0 = 0x1,
Remote = 0x2,
};

```
#### CommandSyncFlag : __int8
```cpp
/* 5650 */
enum CommandSyncFlag : __int8
{
Synced = 0x0,
Local = 0x8,
};

```
#### CommandTypeFlag : __int8
```cpp
/* 5652 */
enum CommandTypeFlag : __int8
{
None_5 = 0x0,
Message = 0x20,
};

```
#### CommandUsageFlag : __int8
```cpp
/* 5648 */
enum CommandUsageFlag : __int8
{
Normal_1 = 0x0,
Test = 0x1,
};

```
#### CommandVisibilityFlag : __int8
```cpp
/* 5649 */
enum CommandVisibilityFlag : __int8
{
Visible = 0x0,
HiddenFromCommandBlockOrigin = 0x2,
HiddenFromPlayerOrigin = 0x4,
Hidden = 0x6,
};

```
#### CommonDirection : __int32
```cpp
/* 296633 */
enum CommonDirection : __int32
{
North_2 = 0x0,
East_2 = 0x1,
South_2 = 0x2,
West_2 = 0x3,
DownNorthSouth_0 = 0x4,
DownEastWest_0 = 0x5,
UpNorthSouth_0 = 0x6,
UpEastWest_0 = 0x7,
AscendingEast = 0x8,
AscendingWest = 0x9,
AscendingNorth = 0xA,
AscendingSouth = 0xB,
SouthEast = 0xC,
SouthWest = 0xD,
NorthWest = 0xE,
NorthEast = 0xF,
None_54 = 0x10,
};

```
#### CompactionStatus : __int32
```cpp
/* 86748 */
enum CompactionStatus : __int32
{
Starting_0 = 0x0,
Finished_1 = 0x1,
};

```
#### ComparatorCapacitor::Mode : __int32
```cpp
/* 292524 */
enum ComparatorCapacitor::Mode : __int32
{
COMPARE_MODE = 0x0,
SUBTRACT_MODE = 0x1,
};

```
#### ComplexInventoryTransaction::Type : __int32
```cpp
/* 79779 */
enum ComplexInventoryTransaction::Type : __int32
{
NormalTransaction = 0x0,
InventoryMismatch_0 = 0x1,
ItemUseTransaction = 0x2,
ItemUseOnEntityTransaction = 0x3,
ItemReleaseTransaction = 0x4,
};

```
#### CompoundContainerType : __int8
```cpp
/* 181065 */
enum CompoundContainerType : __int8
{
Jar = 0x0,
Beaker = 0x1,
Flask = 0x2,
Invalid_22 = 0x3,
};

```
#### CompoundTagUpdaterResult : __int32
```cpp
/* 13572 */
enum CompoundTagUpdaterResult : __int32
{
Success_2 = 0x0,
NoUpdateNeeded = 0x1,
Failed_0 = 0x2,
};

```
#### CompoundType : __int8
```cpp
/* 181066 */
enum CompoundType : __int8
{
Salt = 0x0,
SodiumOxide = 0x1,
SodiumHydroxide = 0x2,
MagnesiumNitrate = 0x3,
IronSulfide = 0x4,
LithiumHydride = 0x5,
SodiumHydride = 0x6,
CalciumBromide = 0x7,
MagnesiumOxide = 0x8,
SodiumAcetate = 0x9,
Luminol = 0xA,
Charcoal = 0xB,
Sugar = 0xC,
AluminumOxide = 0xD,
BoronTrioxide = 0xE,
Soap = 0xF,
Polyethylene = 0x10,
Garbage = 0x11,
MagnesiumSalts_0 = 0x12,
Sulfate = 0x13,
BariumSulfate = 0x14,
PotassiumChloride = 0x15,
MercuricChloride = 0x16,
CeriumChloride = 0x17,
TungstenChloride = 0x18,
CalciumChloride = 0x19,
Water_3 = 0x1A,
Glue = 0x1B,
Hypochlorite = 0x1C,
CrudeOil = 0x1D,
Latex = 0x1E,
PotassiumIodide = 0x1F,
SodiumFluoride = 0x20,
Benzene = 0x21,
Ink_0 = 0x22,
HydrogenPeroxide = 0x23,
Ammonia = 0x24,
SodiumHypochlorite = 0x25,
Invalid_23 = 0x26,
};

```
#### Compressibility : __int32
```cpp
/* 63714 */
enum Compressibility : __int32
{
Compressible = 0x0,
Incompressible = 0x1,
};

```
#### ConnectionDefinition::PortBusyFallbackPolicy : __int32
```cpp
/* 5664 */
enum ConnectionDefinition::PortBusyFallbackPolicy : __int32
{
UseRandom = 0x0,
Fail = 0x1,
};

```
#### ContainerBackgroundStyle : __int32
```cpp
/* 174665 */
enum ContainerBackgroundStyle : __int32
{
Classic = 0x0,
Normal_10 = 0x1,
Invert = 0x2,
Red_2 = 0x3,
Selected = 0x4,
RedButton = 0x5,
Hint = 0x6,
Count_25 = 0x7,
};

```
#### ContainerCategory : __int32
```cpp
/* 174694 */
enum ContainerCategory : __int32
{
Default_12 = 0x0,
PlayerInventory = 0x1,
Intermediary = 0x2,
Output_0 = 0x3,
Unknown_42 = 0x4,
};

```
#### ContainerEnumName : __int32
```cpp
/* 174780 */
enum ContainerEnumName : __int32
{
AnvilInputContainer = 0x0,
AnvilMaterialContainer = 0x1,
AnvilResultPreviewContainer = 0x2,
ArmorContainer = 0x3,
LevelEntityContainer = 0x4,
BeaconPaymentContainer = 0x5,
BrewingStandInputContainer = 0x6,
BrewingStandResultContainer = 0x7,
BrewingStandFuelContainer = 0x8,
CombinedHotbarAndInventoryContainer = 0x9,
CraftingInputContainer = 0xA,
CraftingOutputPreviewContainer = 0xB,
RecipeConstructionContainer = 0xC,
RecipeNatureContainer = 0xD,
RecipeItemsContainer = 0xE,
RecipeSearchContainer = 0xF,
RecipeSearchBarContainer = 0x10,
RecipeEquipmentContainer = 0x11,
EnchantingInputContainer = 0x12,
EnchantingMaterialContainer = 0x13,
FurnaceFuelContainer = 0x14,
FurnaceIngredientContainer = 0x15,
FurnaceResultContainer = 0x16,
HorseEquipContainer = 0x17,
HotbarContainer = 0x18,
HudContainer = 0x19,
InventoryContainer = 0x1A,
ShulkerBoxContainer = 0x1B,
TradeIngredient1Container = 0x1C,
TradeIngredient2Container = 0x1D,
TradeResultPreviewContainer = 0x1E,
OffhandContainer = 0x1F,
CompoundCreatorInput = 0x20,
CompoundCreatorOutputPreview = 0x21,
ElementConstructorOutputPreview = 0x22,
MaterialReducerInput_0 = 0x23,
MaterialReducerOutput = 0x24,
LabTableInput = 0x25,
LoomInputContainer = 0x26,
LoomDyeContainer = 0x27,
LoomMaterialContainer = 0x28,
LoomResultPreviewContainer = 0x29,
BlastFurnaceIngredientContainer = 0x2A,
SmokerIngredientContainer = 0x2B,
Trade2Ingredient1Container = 0x2C,
Trade2Ingredient2Container = 0x2D,
Trade2ResultPreviewContainer = 0x2E,
GrindstoneInputContainer = 0x2F,
GrindstoneAdditionalContainer = 0x30,
GrindstoneResultPreviewContainer = 0x31,
StonecutterInputContainer = 0x32,
StonecutterResultPreviewContainer = 0x33,
CartographyInputContainer = 0x34,
CartographyAdditionalContainer = 0x35,
CartographyResultPreviewContainer = 0x36,
BarrelContainer = 0x37,
CursorContainer = 0x38,
CreatedOutputContainer = 0x39,
};

```
#### ContainerExpandStatus : __int32
```cpp
/* 174693 */
enum ContainerExpandStatus : __int32
{
Normal_11 = 0x0,
Expanded_0 = 0x1,
Contracted = 0x2,
Child = 0x3,
Count_26 = 0x4,
};

```
#### ContainerID : __int8
```cpp
/* 33267 */
enum ContainerID : __int8
{
CONTAINER_ID_NONE = 0xFF,
CONTAINER_ID_INVENTORY = 0x0,
CONTAINER_ID_FIRST = 0x1,
CONTAINER_ID_LAST = 0x64,
CONTAINER_ID_OFFHAND = 0x77,
CONTAINER_ID_ARMOR = 0x78,
CONTAINER_ID_CREATIVE = 0x79,
CONTAINER_ID_SELECTION_SLOTS = 0x7A,
CONTAINER_ID_PLAYER_ONLY_UI = 0x7C,
};

```
#### ContainerType : __int8
```cpp
/* 48672 */
enum ContainerType : __int8
{
NONE_2 = 0xF7,
INVENTORY = 0xFF,
CONTAINER = 0x0,
WORKBENCH = 0x1,
FURNACE = 0x2,
ENCHANTMENT = 0x3,
BREWING_STAND = 0x4,
ANVIL = 0x5,
DISPENSER = 0x6,
DROPPER = 0x7,
HOPPER = 0x8,
CAULDRON = 0x9,
MINECART_CHEST = 0xA,
MINECART_HOPPER = 0xB,
HORSE = 0xC,
BEACON = 0xD,
STRUCTURE_EDITOR = 0xE,
TRADE = 0xF,
COMMAND_BLOCK = 0x10,
JUKEBOX = 0x11,
ARMOR = 0x12,
HAND = 0x13,
COMPOUND_CREATOR = 0x14,
ELEMENT_CONSTRUCTOR = 0x15,
MATERIAL_REDUCER = 0x16,
LAB_TABLE = 0x17,
LOOM = 0x18,
LECTERN = 0x19,
GRINDSTONE = 0x1A,
BLAST_FURNACE = 0x1B,
SMOKER = 0x1C,
STONECUTTER = 0x1D,
CARTOGRAPHY = 0x1E,
};

```
#### ContentTierIncompatibleReason : __int32
```cpp
/* 5784 */
enum ContentTierIncompatibleReason : __int32
{
};

```
#### ContentTierIncompatibleReason_0 : __int32
```cpp
/* 83332 */
enum ContentTierIncompatibleReason_0 : __int32
{
None_32 = 0x0,
Memory = 0x1,
};

```
#### ConversionFlags : __int32
```cpp
/* 486336 */
enum ConversionFlags : __int32
{
strictConversion_0 = 0x0,
lenientConversion_0 = 0x1,
};

```
#### ConversionResult : __int32
```cpp
/* 486311 */
enum ConversionResult : __int32
{
conversionOK = 0x0,
sourceExhausted = 0x1,
targetExhausted = 0x2,
sourceIllegal = 0x3,
};

```
#### CooldownType : __int32
```cpp
/* 172502 */
enum CooldownType : __int32
{
TypeNone = 0xFFFFFFFF,
ChorusFruit_0 = 0x0,
EnderPearl = 0x1,
IceBomb_1 = 0x2,
Count_24 = 0x3,
};

```
#### CoralColor : __int32
```cpp
/* 183705 */
enum CoralColor : __int32
{
Blue_2 = 0x0,
Pink_2 = 0x1,
Purple_2 = 0x2,
Red_4 = 0x3,
Yellow_2 = 0x4,
_count_35 = 0x5,
};

```
#### CoralDirection : __int32
```cpp
/* 460494 */
enum CoralDirection : __int32
{
West_3 = 0x0,
East_3 = 0x1,
North_3 = 0x2,
South_3 = 0x3,
};

```
#### Core::CrossStorageCopyMode : __int32
```cpp
/* 482463 */
enum Core::CrossStorageCopyMode : __int32
{
Buffered_0 = 0x0,
FullCopy = 0x1,
};

```
#### Core::DirectoryIterationFlags : __int64
```cpp
/* 84123 */
enum Core::DirectoryIterationFlags : __int64
{
None_34 = 0x1,
FullPathName = 0x2,
Name = 0x4,
FileSize = 0x8,
Type = 0x10,
CreateTime = 0x20,
ModifyTime = 0x40,
CreateAndModifyTime = 0x60,
Files = 0x80,
Directories = 0x100,
FilesAndDirectories = 0x180,
Recursive = 0x200,
TreatFlatFileAsFile = 0x400,
FileSizeAllocationOnDisk = 0x800,
};

```
#### Core::FileAccessType : __int32
```cpp
/* 463111 */
enum Core::FileAccessType : __int32
{
ReadOnly = 0x0,
ReadWrite = 0x1,
Flush = 0x2,
};

```
#### Core::FileBufferingMode : __int32
```cpp
/* 5544 */
enum Core::FileBufferingMode : __int32
{
Buffered = 0x0,
Unbuffered = 0x1,
};

```
#### Core::FileStorageArea::FlushableLevelDbEnvType : __int32
```cpp
/* 480043 */
enum Core::FileStorageArea::FlushableLevelDbEnvType : __int32
{
None_60 = 0x0,
InMemory = 0x1,
StorageArea = 0x2,
};

```
#### Core::FileType : __int32
```cpp
/* 83873 */
enum Core::FileType : __int32
{
File = 0x0,
Directory_1 = 0x1,
None_33 = 0x2,
};

```
#### Core::FlatFileManifestInfo::FlatFileManifestInfoFlags : __int8
```cpp
/* 482746 */
enum Core::FlatFileManifestInfo::FlatFileManifestInfoFlags : __int8
{
File_0 = 0x1,
Deleted = 0x80,
};

```
#### Core::LevelStorageState : __int32
```cpp
/* 87048 */
enum Core::LevelStorageState : __int32
{
Open_0 = 0x0,
Corrupted = 0x1,
NotFound = 0x2,
IOError = 0x3,
NotSupported = 0x4,
InvalidArguments = 0x5,
Unknown_31 = 0x6,
};

```
#### Core::Profile::CounterFlags : __int32
```cpp
/* 485590 */
enum Core::Profile::CounterFlags : __int32
{
None_62 = 0x0,
Detailed = 0x1,
DetailedGraph = 0x2,
};

```
#### Core::Profile::CounterFormat : __int32
```cpp
/* 64250 */
enum Core::Profile::CounterFormat : __int32
{
Default_8 = 0x0,
Bytes = 0x1,
};

```
#### Core::Profile::FileExtension : __int8
```cpp
/* 485591 */
enum Core::Profile::FileExtension : __int8
{
HTML = 0x0,
CSV = 0x1,
BOTH = 0x2,
};

```
#### Core::ZipUtils::UnzipResult : __int32
```cpp
/* 84117 */
enum Core::ZipUtils::UnzipResult : __int32
{
OK_0 = 0x0,
UnzipError = 0x1,
ParamError = 0x2,
BadZipFile = 0x3,
InternalError = 0x4,
CRCError = 0x5,
};

```
#### Core::ZipUtils::ZipCompressionLevel : __int32
```cpp
/* 84118 */
enum Core::ZipUtils::ZipCompressionLevel : __int32
{
Default_10 = 0x0,
NoCompression = 0x1,
BestSpeed = 0x2,
BestCompression = 0x3,
};

```
#### Core::ZipUtils::ZipResult : __int32
```cpp
/* 84119 */
enum Core::ZipUtils::ZipResult : __int32
{
OK_1 = 0x0,
ZipError = 0x1,
ParamError_0 = 0x2,
BadZipFile_0 = 0x3,
InternalError_0 = 0x4,
};

```
#### CraftingDataEntryType : __int32
```cpp
/* 75621 */
enum CraftingDataEntryType : __int32
{
ShapelessRecipe = 0x0,
ShapedRecipe = 0x1,
FurnaceRecipe = 0x2,
FurnaceAuxRecipe = 0x3,
MultiRecipe = 0x4,
ShulkerBoxRecipe = 0x5,
ShapelessChemistryRecipe = 0x6,
ShapedChemistryRecipe = 0x7,
};

```
#### CrashDumpLogStringID : __int16
```cpp
/* 480121 */
enum CrashDumpLogStringID : __int16
{
None_61 = 0x0,
HandleBuildAction = 0x1,
EnterScope = 0x2,
ExitScope = 0x3,
AppPlatform_initialize = 0x4,
MinecraftGame_update = 0x5,
DataDrivenRenderer_renderModel = 0x6,
KillMinecraft = 0x7,
StartMinecraft = 0x8,
Main = 0x9,
MakeMinecraftGame = 0xA,
MainLoop = 0xB,
AppResetRequested = 0xC,
Shutdown = 0xD,
ActorRenderDisplatcher_Render = 0xE,
AppMain_updateAndRender = 0xF,
AppPlatformWinrt_Update = 0x10,
AppView_run = 0x11,
MinecraftGame_initStep = 0x12,
MinecraftGame_suspendStep = 0x13,
MinecraftGame_resumeStep = 0x14,
AbortedScope = 0x15,
SaveData_mount = 0x16,
SaveData_unmount = 0x17,
SaveData_remount = 0x18,
SaveData_watchdog = 0x19,
_count_54 = 0x1A,
};

```
#### CreativeItemCategory : __int32
```cpp
/* 94506 */
enum CreativeItemCategory : __int32
{
All_3 = 0x0,
Construction = 0x1,
Nature = 0x2,
Equipment = 0x3,
Items = 0x4,
ItemCommandOnly = 0x5,
Undefined_10 = 0x6,
NUM_CATEGORIES = 0x7,
};

```
#### Crypto::Asymmetric::System : __int32
```cpp
/* 45580 */
enum Crypto::Asymmetric::System : __int32
{
RSA_1024 = 0x0,
RSA_2048 = 0x1,
RSA_4096 = 0x2,
EC_prime256v1 = 0x3,
EC_secp256k1 = 0x4,
EC_secp384r1 = 0x5,
EC_secp521r1 = 0x6,
};

```
#### Crypto::Hash::HashType : __int32
```cpp
/* 45581 */
enum Crypto::Hash::HashType : __int32
{
MD5 = 0x0,
SHA1 = 0x1,
SHA256 = 0x2,
SHA384 = 0x3,
SHA512 = 0x4,
};

```
#### Crypto::Symmetric::OperationMode : __int32
```cpp
/* 421421 */
enum Crypto::Symmetric::OperationMode : __int32
{
ECB = 0x0,
CBC = 0x1,
CFB = 0x2,
OFB = 0x3,
};

```
#### Crypto::Symmetric::System : __int32
```cpp
/* 421418 */
enum Crypto::Symmetric::System : __int32
{
AES_128 = 0x0,
AES_256 = 0x1,
};

```
#### CurrentCmdVersion : __int32
```cpp
/* 5678 */
enum CurrentCmdVersion : __int32
{
Invalid_5 = 0xFFFFFFFF,
Initial = 0x1,
TpRotationClamping = 0x2,
NewBedrockCmdSystem = 0x3,
ExecuteUsesVec3 = 0x4,
CloneFixes = 0x5,
UpdateAquatic = 0x6,
EntitySelectorUsesVec3 = 0x7,
ContainersDontDropItemsAnymore = 0x8,
FiltersObeyDimensions = 0x9,
ExecuteAndBlockCommandAndSelfSelectorFixes = 0xA,
};

```
#### DBChunkStorage::ChunkCacheStatus : __int32
```cpp
/* 476899 */
enum DBChunkStorage::ChunkCacheStatus : __int32
{
Missing = 0x0,
Available_0 = 0x1,
DontCache = 0x2,
};

```
#### DataItemType : __int8
```cpp
/* 47292 */
enum DataItemType : __int8
{
Byte = 0x0,
Short = 0x1,
Int_1 = 0x2,
Float_1 = 0x3,
String_0 = 0x4,
CompoundTag = 0x5,
Pos = 0x6,
Int64 = 0x7,
Vec3 = 0x8,
Unknown_23 = 0x9,
};

```
#### DataLoadHelperType : __int32
```cpp
/* 77438 */
enum DataLoadHelperType : __int32
{
Default_9 = 0x0,
Structure_0 = 0x1,
};

```
#### DateManager::TimeZoneType : __int32
```cpp
/* 82681 */
enum DateManager::TimeZoneType : __int32
{
UTC = 0x0,
Local_4 = 0x1,
};

```
#### DedicatedServer::StartResult : __int32
```cpp
/* 5508 */
enum DedicatedServer::StartResult : __int32
{
Success = 0x0,
PortOccupied = 0x1,
InvalidSettings = 0x2,
};

```
#### DefaultMessageIDTypes : __int32
```cpp
/* 73242 */
enum DefaultMessageIDTypes : __int32
{
ID_CONNECTED_PING = 0x0,
ID_UNCONNECTED_PING = 0x1,
ID_UNCONNECTED_PING_OPEN_CONNECTIONS = 0x2,
ID_CONNECTED_PONG = 0x3,
ID_DETECT_LOST_CONNECTIONS = 0x4,
ID_OPEN_CONNECTION_REQUEST_1 = 0x5,
ID_OPEN_CONNECTION_REPLY_1 = 0x6,
ID_OPEN_CONNECTION_REQUEST_2 = 0x7,
ID_OPEN_CONNECTION_REPLY_2 = 0x8,
ID_CONNECTION_REQUEST = 0x9,
ID_REMOTE_SYSTEM_REQUIRES_PUBLIC_KEY = 0xA,
ID_OUR_SYSTEM_REQUIRES_SECURITY = 0xB,
ID_PUBLIC_KEY_MISMATCH = 0xC,
ID_OUT_OF_BAND_INTERNAL = 0xD,
ID_SND_RECEIPT_ACKED = 0xE,
ID_SND_RECEIPT_LOSS = 0xF,
ID_CONNECTION_REQUEST_ACCEPTED = 0x10,
ID_CONNECTION_ATTEMPT_FAILED = 0x11,
ID_ALREADY_CONNECTED = 0x12,
ID_NEW_INCOMING_CONNECTION = 0x13,
ID_NO_FREE_INCOMING_CONNECTIONS = 0x14,
ID_DISCONNECTION_NOTIFICATION = 0x15,
ID_CONNECTION_LOST = 0x16,
ID_CONNECTION_BANNED = 0x17,
ID_INVALID_PASSWORD = 0x18,
ID_INCOMPATIBLE_PROTOCOL_VERSION = 0x19,
ID_IP_RECENTLY_CONNECTED = 0x1A,
ID_TIMESTAMP = 0x1B,
ID_UNCONNECTED_PONG = 0x1C,
ID_ADVERTISE_SYSTEM = 0x1D,
ID_DOWNLOAD_PROGRESS = 0x1E,
ID_REMOTE_DISCONNECTION_NOTIFICATION = 0x1F,
ID_REMOTE_CONNECTION_LOST = 0x20,
ID_REMOTE_NEW_INCOMING_CONNECTION = 0x21,
ID_FILE_LIST_TRANSFER_HEADER = 0x22,
ID_FILE_LIST_TRANSFER_FILE = 0x23,
ID_FILE_LIST_REFERENCE_PUSH_ACK = 0x24,
ID_DDT_DOWNLOAD_REQUEST = 0x25,
ID_TRANSPORT_STRING = 0x26,
ID_REPLICA_MANAGER_CONSTRUCTION = 0x27,
ID_REPLICA_MANAGER_SCOPE_CHANGE = 0x28,
ID_REPLICA_MANAGER_SERIALIZE = 0x29,
ID_REPLICA_MANAGER_DOWNLOAD_STARTED = 0x2A,
ID_REPLICA_MANAGER_DOWNLOAD_COMPLETE = 0x2B,
ID_RAKVOICE_OPEN_CHANNEL_REQUEST = 0x2C,
ID_RAKVOICE_OPEN_CHANNEL_REPLY = 0x2D,
ID_RAKVOICE_CLOSE_CHANNEL = 0x2E,
ID_RAKVOICE_DATA = 0x2F,
ID_AUTOPATCHER_GET_CHANGELIST_SINCE_DATE = 0x30,
ID_AUTOPATCHER_CREATION_LIST = 0x31,
ID_AUTOPATCHER_DELETION_LIST = 0x32,
ID_AUTOPATCHER_GET_PATCH = 0x33,
ID_AUTOPATCHER_PATCH_LIST = 0x34,
ID_AUTOPATCHER_REPOSITORY_FATAL_ERROR = 0x35,
ID_AUTOPATCHER_CANNOT_DOWNLOAD_ORIGINAL_UNMODIFIED_FILES = 0x36,
ID_AUTOPATCHER_FINISHED_INTERNAL = 0x37,
ID_AUTOPATCHER_FINISHED = 0x38,
ID_AUTOPATCHER_RESTART_APPLICATION = 0x39,
ID_NAT_PUNCHTHROUGH_REQUEST = 0x3A,
ID_NAT_CONNECT_AT_TIME = 0x3B,
ID_NAT_GET_MOST_RECENT_PORT = 0x3C,
ID_NAT_CLIENT_READY = 0x3D,
ID_NAT_TARGET_NOT_CONNECTED = 0x3E,
ID_NAT_TARGET_UNRESPONSIVE = 0x3F,
ID_NAT_CONNECTION_TO_TARGET_LOST = 0x40,
ID_NAT_ALREADY_IN_PROGRESS = 0x41,
ID_NAT_PUNCHTHROUGH_FAILED = 0x42,
ID_NAT_PUNCHTHROUGH_SUCCEEDED = 0x43,
ID_READY_EVENT_SET = 0x44,
ID_READY_EVENT_UNSET = 0x45,
ID_READY_EVENT_ALL_SET = 0x46,
ID_READY_EVENT_QUERY = 0x47,
ID_LOBBY_GENERAL = 0x48,
ID_RPC_REMOTE_ERROR = 0x49,
ID_RPC_PLUGIN = 0x4A,
ID_FILE_LIST_REFERENCE_PUSH = 0x4B,
ID_READY_EVENT_FORCE_ALL_SET = 0x4C,
ID_ROOMS_EXECUTE_FUNC = 0x4D,
ID_ROOMS_LOGON_STATUS = 0x4E,
ID_ROOMS_HANDLE_CHANGE = 0x4F,
ID_LOBBY2_SEND_MESSAGE = 0x50,
ID_LOBBY2_SERVER_ERROR = 0x51,
ID_FCM2_NEW_HOST = 0x52,
ID_FCM2_REQUEST_FCMGUID = 0x53,
ID_FCM2_RESPOND_CONNECTION_COUNT = 0x54,
ID_FCM2_INFORM_FCMGUID = 0x55,
ID_FCM2_UPDATE_MIN_TOTAL_CONNECTION_COUNT = 0x56,
ID_FCM2_VERIFIED_JOIN_START = 0x57,
ID_FCM2_VERIFIED_JOIN_CAPABLE = 0x58,
ID_FCM2_VERIFIED_JOIN_FAILED = 0x59,
ID_FCM2_VERIFIED_JOIN_ACCEPTED = 0x5A,
ID_FCM2_VERIFIED_JOIN_REJECTED = 0x5B,
ID_UDP_PROXY_GENERAL = 0x5C,
ID_SQLite3_EXEC = 0x5D,
ID_SQLite3_UNKNOWN_DB = 0x5E,
ID_SQLLITE_LOGGER = 0x5F,
ID_NAT_TYPE_DETECTION_REQUEST = 0x60,
ID_NAT_TYPE_DETECTION_RESULT = 0x61,
ID_ROUTER_2_INTERNAL = 0x62,
ID_ROUTER_2_FORWARDING_NO_PATH = 0x63,
ID_ROUTER_2_FORWARDING_ESTABLISHED = 0x64,
ID_ROUTER_2_REROUTED = 0x65,
ID_TEAM_BALANCER_INTERNAL = 0x66,
ID_TEAM_BALANCER_REQUESTED_TEAM_FULL = 0x67,
ID_TEAM_BALANCER_REQUESTED_TEAM_LOCKED = 0x68,
ID_TEAM_BALANCER_TEAM_REQUESTED_CANCELLED = 0x69,
ID_TEAM_BALANCER_TEAM_ASSIGNED = 0x6A,
ID_LIGHTSPEED_INTEGRATION = 0x6B,
ID_XBOX_LOBBY = 0x6C,
ID_TWO_WAY_AUTHENTICATION_INCOMING_CHALLENGE_SUCCESS = 0x6D,
ID_TWO_WAY_AUTHENTICATION_OUTGOING_CHALLENGE_SUCCESS = 0x6E,
ID_TWO_WAY_AUTHENTICATION_INCOMING_CHALLENGE_FAILURE = 0x6F,
ID_TWO_WAY_AUTHENTICATION_OUTGOING_CHALLENGE_FAILURE = 0x70,
ID_TWO_WAY_AUTHENTICATION_OUTGOING_CHALLENGE_TIMEOUT = 0x71,
ID_TWO_WAY_AUTHENTICATION_NEGOTIATION = 0x72,
ID_CLOUD_POST_REQUEST = 0x73,
ID_CLOUD_RELEASE_REQUEST = 0x74,
ID_CLOUD_GET_REQUEST = 0x75,
ID_CLOUD_GET_RESPONSE = 0x76,
ID_CLOUD_UNSUBSCRIBE_REQUEST = 0x77,
ID_CLOUD_SERVER_TO_SERVER_COMMAND = 0x78,
ID_CLOUD_SUBSCRIPTION_NOTIFICATION = 0x79,
ID_LIB_VOICE = 0x7A,
ID_RELAY_PLUGIN = 0x7B,
ID_NAT_REQUEST_BOUND_ADDRESSES = 0x7C,
ID_NAT_RESPOND_BOUND_ADDRESSES = 0x7D,
ID_FCM2_UPDATE_USER_CONTEXT = 0x7E,
ID_RESERVED_3 = 0x7F,
ID_RESERVED_4 = 0x80,
ID_RESERVED_5 = 0x81,
ID_RESERVED_6 = 0x82,
ID_RESERVED_7 = 0x83,
ID_RESERVED_8 = 0x84,
ID_RESERVED_9 = 0x85,
ID_PONG_ADDRESS_INFO = 0x86,
ID_NAT_TRAVERSAL_PING = 0x87,
ID_NAT_TRAVERSAL_PONG = 0x88,
ID_REQUEST_WEBSOCKET_CONNECTION = 0x89,
ID_ACK_FAILED_WEBSOCKET_REQUEST = 0x8A,
ID_AVAILABLE_5 = 0x8B,
ID_AVAILABLE_6 = 0x8C,
ID_AVAILABLE_7 = 0x8D,
ID_USER_PACKET_ENUM = 0x8E,
};

```
#### DefinitionEventType : __int32
```cpp
/* 46262 */
enum DefinitionEventType : __int32
{
LEAF = 0x0,
SEQUENCE = 0x1,
RANDOM = 0x2,
NONE_0 = 0x3,
};

```
#### Difficulty : __int32
```cpp
/* 5592 */
enum Difficulty : __int32
{
Peaceful = 0x0,
Easy = 0x1,
Normal_0 = 0x2,
Hard = 0x3,
Count_1 = 0x4,
Unknown = 0x5,
};

```
#### Direction::Type : __int8
```cpp
/* 31927 */
enum Direction::Type : __int8
{
SOUTH = 0x0,
WEST = 0x1,
NORTH = 0x2,
EAST = 0x3,
UNDEFINED = 0xFF,
};

```
#### DirtType : __int32
```cpp
/* 183671 */
enum DirtType : __int32
{
Normal_12 = 0x0,
Coarse = 0x1,
_count_31 = 0x2,
};

```
#### DisplayOrientation : __int32
```cpp
/* 6934 */
enum DisplayOrientation : __int32
{
None_8 = 0x0,
Landscape = 0x1,
Portrait = 0x2,
LandscapeFlipped = 0x3,
PortraitFlipped = 0x4,
};

```
#### DlcPerformanceTier : __int32
```cpp
/* 82545 */
enum DlcPerformanceTier : __int32
{
};

```
#### DoorBlock::DoorType : __int32
```cpp
/* 183756 */
enum DoorBlock::DoorType : __int32
{
OAK = 0x0,
SPRUCE = 0x1,
BIRCH = 0x2,
JUNGLE = 0x3,
ACACIA = 0x4,
DARKOAK = 0x5,
IRON = 0x6,
COUNT_13 = 0x7,
};

```
#### DoublePlantType : __int32
```cpp
/* 35199 */
enum DoublePlantType : __int32
{
Sunflower = 0x0,
Syringa = 0x1,
Grass = 0x2,
Fern_0 = 0x3,
Rose = 0x4,
Paeonia = 0x5,
_count_10 = 0x6,
};

```
#### DwellerComponent::DwellingType : __int32
```cpp
/* 53495 */
enum DwellerComponent::DwellingType : __int32
{
VillageDwelling = 0x0,
COUNT_2 = 0x1,
};

```
#### DwellerRole : __int32
```cpp
/* 53496 */
enum DwellerRole : __int32
{
DwellingInhabitant = 0x0,
DwellingDefender = 0x1,
DwellingHostile = 0x2,
DwellingPassive = 0x3,
COUNT_3 = 0x4,
};

```
#### EducationEditionOffer : __int32
```cpp
/* 5597 */
enum EducationEditionOffer : __int32
{
None_3 = 0x0,
RestOfWorld = 0x1,
China = 0x2,
};

```
#### EducationFeature : __int8
```cpp
/* 81159 */
enum EducationFeature : __int8
{
None_29 = 0x0,
Chemistry = 0x1,
Education = 0x2,
CodeBuilder = 0x4,
BaseCodeBuilder = 0x8,
};

```
#### EducationMetadata::ContentType : __int32
```cpp
/* 83526 */
enum EducationMetadata::ContentType : __int32
{
Invalid_18 = 0x0,
WorldLesson = 0x1,
NonWorldLesson = 0x2,
Count_18 = 0x3,
};

```
#### EducationMetadata::UserType : __int32
```cpp
/* 83527 */
enum EducationMetadata::UserType : __int32
{
Unknown_30 = 0x0,
StudentAndTeacher = 0x1,
Teacher_0 = 0x2,
Count_19 = 0x3,
};

```
#### EffectCommand::Mode : __int32
```cpp
/* 425152 */
enum EffectCommand::Mode : __int32
{
Add_6 = 0x0,
Clear_0 = 0x1,
};

```
#### EggCount : __int32
```cpp
/* 122545 */
enum EggCount : __int32
{
OneEgg = 0x0,
TwoEgg = 0x1,
ThreeEgg = 0x2,
FourEgg = 0x3,
_count_23 = 0x4,
};

```
#### ElementCategory : __int8
```cpp
/* 226409 */
enum ElementCategory : __int8
{
AlkaliMetal = 0x0,
AlkalineEarth = 0x1,
TransitionMetal = 0x2,
BasicMetal = 0x3,
Semimetal = 0x4,
Nonmetal = 0x5,
Halogen = 0x6,
NobleGas = 0x7,
Lanthanide = 0x8,
Actinide = 0x9,
Unknown_45 = 0xA,
};

```
#### ElementType : __int8
```cpp
/* 183769 */
enum ElementType : __int8
{
Unknown_44 = 0x0,
H = 0x1,
He = 0x2,
Li = 0x3,
Be = 0x4,
B = 0x5,
C = 0x6,
N = 0x7,
O = 0x8,
F = 0x9,
Ne = 0xA,
Na = 0xB,
Mg = 0xC,
Al = 0xD,
Si = 0xE,
P = 0xF,
S = 0x10,
Cl = 0x11,
Ar = 0x12,
K = 0x13,
Ca = 0x14,
Sc = 0x15,
Ti = 0x16,
V = 0x17,
Cr = 0x18,
Mn = 0x19,
Fe = 0x1A,
Co = 0x1B,
Ni = 0x1C,
Cu = 0x1D,
Zn = 0x1E,
Ga = 0x1F,
Ge = 0x20,
As = 0x21,
Se = 0x22,
Br = 0x23,
Kr = 0x24,
Rb = 0x25,
Sr = 0x26,
Y_0 = 0x27,
Zr = 0x28,
Nb = 0x29,
Mo = 0x2A,
Tc = 0x2B,
Ru = 0x2C,
Rh = 0x2D,
Pd = 0x2E,
Ag = 0x2F,
Cd = 0x30,
In = 0x31,
Sn = 0x32,
Sb = 0x33,
Te = 0x34,
I = 0x35,
Xe = 0x36,
Cs = 0x37,
Ba = 0x38,
La = 0x39,
Ce = 0x3A,
Pr = 0x3B,
Nd = 0x3C,
Pm = 0x3D,
Sm = 0x3E,
Eu = 0x3F,
Gd = 0x40,
Tb = 0x41,
Dy = 0x42,
Ho = 0x43,
Er = 0x44,
Tm = 0x45,
Yb = 0x46,
Lu = 0x47,
Hf = 0x48,
Ta = 0x49,
W = 0x4A,
Re = 0x4B,
Os = 0x4C,
Ir = 0x4D,
Pt = 0x4E,
Au = 0x4F,
Hg = 0x50,
Tl = 0x51,
Pb = 0x52,
Bi = 0x53,
Po = 0x54,
At = 0x55,
Rn = 0x56,
Fr = 0x57,
Ra = 0x58,
Ac = 0x59,
Th = 0x5A,
Pa = 0x5B,
U = 0x5C,
Np = 0x5D,
Pu = 0x5E,
Am = 0x5F,
Cm = 0x60,
Bk = 0x61,
Cf = 0x62,
Es = 0x63,
Fm = 0x64,
Md = 0x65,
No = 0x66,
Lr = 0x67,
Rf = 0x68,
Db = 0x69,
Sg = 0x6A,
Bh = 0x6B,
Hs = 0x6C,
Mt = 0x6D,
Ds = 0x6E,
Rg = 0x6F,
Cn = 0x70,
Nh = 0x71,
Fl = 0x72,
Mc = 0x73,
Lv = 0x74,
Ts = 0x75,
Og = 0x76,
Invalid_24 = 0x77,
};

```
#### EmotePacket::Flags : __int8
```cpp
/* 79606 */
enum EmotePacket::Flags : __int8
{
SERVER_SIDE = 0x1,
};

```
#### Enchant::Activation : __int32
```cpp
/* 116675 */
enum Enchant::Activation : __int32
{
EQUIPPED = 0x0,
HELD = 0x1,
SELF = 0x2,
_num_activations = 0x3,
_invalid = 0x4,
};

```
#### Enchant::CompatibilityID : __int32
```cpp
/* 185711 */
enum Enchant::CompatibilityID : __int32
{
NON_CONFLICT = 0x0,
DAMAGE = 0x1,
GATHERING = 0x2,
PROTECTION = 0x3,
FROSTSTRIDER = 0x4,
MENDFINITY = 0x5,
LOYALRIPTIDE = 0x6,
};

```
#### Enchant::Frequency : __int32
```cpp
/* 185265 */
enum Enchant::Frequency : __int32
{
Common_0 = 0x1E,
Uncommon_0 = 0xA,
Rare_0 = 0x3,
VeryRare = 0x1,
};

```
#### Enchant::Slot : __int32
```cpp
/* 180699 */
enum Enchant::Slot : __int32
{
NONE_12 = 0x0,
All_8 = 0xFFFFFFFF,
G_ARMOR = 0xF,
ARMOR_HEAD = 0x1,
ARMOR_TORSO = 0x2,
ARMOR_FEET = 0x4,
ARMOR_LEGS = 0x8,
SWORD = 0x10,
BOW = 0x20,
SPEAR = 0x8000,
CROSSBOW = 0x10000,
G_TOOL = 0x201C0,
HOE = 0x40,
SHEARS = 0x80,
FLINTSTEEL = 0x100,
SHIELD = 0x20000,
G_DIGGING = 0xE00,
AXE = 0x200,
PICKAXE = 0x400,
SHOVEL = 0x800,
FISHING_ROD = 0x1000,
CARROT_STICK = 0x2000,
ELYTRA = 0x4000,
};

```
#### Enchant::Type : __int32
```cpp
/* 33011 */
enum Enchant::Type : __int32
{
ArmorAll = 0x0,
ArmorFire = 0x1,
ArmorFall = 0x2,
ArmorExplosive = 0x3,
ArmorProjectile = 0x4,
ArmorThorns = 0x5,
WaterBreath = 0x6,
WaterSpeed = 0x7,
WaterAffinity = 0x8,
WeaponDamage = 0x9,
WeaponUndead = 0xA,
WeaponArthropod = 0xB,
WeaponKnockback = 0xC,
WeaponFire = 0xD,
WeaponLoot = 0xE,
MiningEfficiency = 0xF,
MiningSilkTouch = 0x10,
MiningDurability = 0x11,
MiningLoot = 0x12,
BowDamage = 0x13,
BowKnockback = 0x14,
BowFire = 0x15,
BowInfinity = 0x16,
FishingLoot = 0x17,
FishingLure = 0x18,
FrostWalker = 0x19,
Mending = 0x1A,
CurseBinding = 0x1B,
CurseVanishing = 0x1C,
TridentImpaling = 0x1D,
TridentRiptide = 0x1E,
TridentLoyalty = 0x1F,
TridentChanneling = 0x20,
CrossbowMultishot = 0x21,
CrossbowPiercing = 0x22,
CrossbowQuickCharge = 0x23,
NumEnchantments = 0x24,
InvalidEnchantment = 0x25,
};

```
#### EnchantResultType : __int8
```cpp
/* 33511 */
enum EnchantResultType : __int8
{
Fail_0 = 0x0,
Conflict = 0x1,
Increment = 0x2,
Enchant = 0x3,
};

```
#### EndCityPieces::SectionType : __int32
```cpp
/* 461977 */
enum EndCityPieces::SectionType : __int32
{
SectionTower = 0x0,
SectionFatTower = 0x1,
SectionBridge = 0x2,
SectionHouse = 0x3,
};

```
#### EndDragonFight::GatewayTask : __int8
```cpp
/* 169789 */
enum EndDragonFight::GatewayTask : __int8
{
GENERATE_PAIR = 0x0,
VERIFY_PAIR = 0x1,
NO_TASK = 0x2,
};

```
#### EndDragonFightVersion : __int8
```cpp
/* 169787 */
enum EndDragonFightVersion : __int8
{
Unknown_39 = 0x0,
v1_9_0_0 = 0x1,
};

```
#### EndPortalFrameBlock::CreateEndPortalResults : __int32
```cpp
/* 459394 */
enum EndPortalFrameBlock::CreateEndPortalResults : __int32
{
Success_15 = 0x0,
InvalidShape = 0x1,
Blocked = 0x2,
Count_28 = 0x3,
};

```
#### EquipmentFilter : __int32
```cpp
/* 51809 */
enum EquipmentFilter : __int32
{
MainHand = 0x0,
OffHand = 0x1,
Hands = 0x2,
Armor_0 = 0x3,
All_1 = 0x4,
Count_8 = 0x5,
};

```
#### EquipmentLocation : __int32
```cpp
/* 114311 */
enum EquipmentLocation : __int32
{
Any_2 = 0x0,
Hand = 0x1,
AnyArmor = 0x2,
HeadArmor = 0x3,
TorsoArmor = 0x4,
LegArmor = 0x5,
FeetArmor = 0x6,
};

```
#### EquipmentSlot : __int32
```cpp
/* 89151 */
enum EquipmentSlot : __int32
{
_none = 0xFFFFFFFF,
_begin = 0x0,
_handSlot = 0x0,
Mainhand_0 = 0x0,
Offhand_0 = 0x1,
_armorSlot = 0x2,
Head_2 = 0x2,
Torso_0 = 0x3,
Legs_1 = 0x4,
Feet_2 = 0x5,
_containerSlot = 0x6,
Hotbar = 0x6,
Inventory = 0x7,
EnderChest_0 = 0x8,
Saddle_0 = 0x9,
EntityArmor = 0xA,
Chest_0 = 0xB,
_count_19 = 0xC,
};

```
#### EventPacket::AgentResult : __int32
```cpp
/* 79629 */
enum EventPacket::AgentResult : __int32
{
ActionFail = 0x0,
ActionSuccess = 0x1,
QueryResultFalse = 0x2,
QueryResultTrue = 0x3,
};

```
#### EventPacket::Type : __int32
```cpp
/* 13309 */
enum EventPacket::Type : __int32
{
Achievement = 0x0,
Interaction = 0x1,
PortalCreated = 0x2,
PortalUsed = 0x3,
MobKilled = 0x4,
CauldronUsed = 0x5,
PlayerDied = 0x6,
BossKilled = 0x7,
AgentCommand = 0x8,
AgentCreated = 0x9,
PatternRemoved = 0xA,
SlashCommand_0 = 0xB,
FishBucketed = 0xC,
MobBorn = 0xD,
PetDied = 0xE,
POICauldronUsed = 0xF,
ComposterUsed = 0x10,
BellUsed = 0x11,
ActorDefinition = 0x12,
RaidUpdate = 0x13,
PlayerMovementAnomaly = 0x14,
PlayerMovementCorrected = 0x15,
HoneyHarvested = 0x16,
};

```
#### EventResult : __int32
```cpp
/* 475 */
enum EventResult : __int32
{
StopProcessing = 0x0,
KeepGoing = 0x1,
};

```
#### ExecuteCommand::Mode : __int32
```cpp
/* 425338 */
enum ExecuteCommand::Mode : __int32
{
Execute = 0x0,
Detect = 0x1,
};

```
#### ExperienceOrb::DropType : __int8
```cpp
/* 48669 */
enum ExperienceOrb::DropType : __int8
{
NoType = 0x0,
FromBlock = 0x1,
FromMob = 0x2,
FromPlayer = 0x3,
};

```
#### ExpressionOp : __int32
```cpp
/* 47717 */
enum ExpressionOp : __int32
{
Unknown_24 = 0xFFFFFFFF,
LeftParenthesis = 0x0,
RightParenthesis = 0x1,
LeftBracket = 0x2,
RightBracket = 0x3,
Negate = 0x4,
LogicalNot = 0x5,
Abs = 0x6,
Cos = 0x7,
Sin = 0x8,
Clamp = 0x9,
Lerp = 0xA,
LerpRotate = 0xB,
Max_1 = 0xC,
Min_1 = 0xD,
Round = 0xE,
Trunc = 0xF,
Ceil = 0x10,
Floor = 0x11,
Mod = 0x12,
Add = 0x13,
Div = 0x14,
Mul = 0x15,
Exp = 0x16,
Ln = 0x17,
Sqrt = 0x18,
Pow = 0x19,
Random_1 = 0x1A,
DieRoll = 0x1B,
QueryFunction = 0x1C,
GenericQueryFunction = 0x1D,
ArrayVariable = 0x1E,
EntityVariable = 0x1F,
TempVariable = 0x20,
HashedString = 0x21,
GeometryVariable = 0x22,
MaterialVariable = 0x23,
TextureVariable = 0x24,
LessThan_1 = 0x25,
LessEqual = 0x26,
GreaterEqual = 0x27,
GreaterThan_1 = 0x28,
LogicalEqual = 0x29,
LogicalNotEqual = 0x2A,
LogicalOr = 0x2B,
LogicalAnd = 0x2C,
Conditional = 0x2D,
ConditionalElse = 0x2E,
Float_2 = 0x2F,
Pi = 0x30,
Array = 0x31,
Geometry_0 = 0x32,
ModelPart = 0x33,
Material = 0x34,
Texture = 0x35,
Assignment = 0x36,
Semicolon = 0x37,
Return = 0x38,
Comma_0 = 0x39,
This = 0x3A,
Count_6 = 0x3B,
};

```
#### ExternalApp : __int32
```cpp
/* 480113 */
enum ExternalApp : __int32
{
};

```
#### Facing::Name : __int8
```cpp
/* 31929 */
enum Facing::Name : __int8
{
DOWN = 0x0,
UP = 0x1,
NORTH_0 = 0x2,
SOUTH_0 = 0x3,
WEST_0 = 0x4,
EAST_0 = 0x5,
MAX = 0x6,
NOT_DEFINED = 0x6,
NUM_CULLING_IDS = 0x7,
};

```
#### Facing::Rotation : __int32
```cpp
/* 31930 */
enum Facing::Rotation : __int32
{
NONE = 0x0,
CCW = 0x1,
OPP = 0x2,
CW = 0x3,
};

```
#### FallingBlock::State : __int32
```cpp
/* 170704 */
enum FallingBlock::State : __int32
{
Falling = 0x0,
WaitRemoval = 0x1,
};

```
#### FeatureOptionID : __int32
```cpp
/* 77444 */
enum FeatureOptionID : __int32
{
None_25 = 0x0,
NetworkLogAllPackets = 0x1,
Scoreboards = 0x2,
Functions = 0x3,
UIAsyncLoadingAndAnimations = 0x4,
Allow3rdPartyServerSplitscreen = 0x5,
ExperimentalGameplayInAllWorlds = 0x6,
Hummingbird = 0x7,
HummingbirdDebugging = 0x8,
UIRefresh = 0x9,
Scripting_0 = 0xA,
Realms_1 = 0xB,
RealmsContent = 0xC,
EnableLoadTimer = 0xD,
ExternalWorldTemplatePackSources = 0xE,
Win10Subscriptions = 0xF,
PlayerRenaming = 0x10,
PersonaBackend = 0x11,
PersonaSkin = 0x12,
PlayFabInsightsTelemetry = 0x13,
PersonaEnabled = 0x14,
PersonaServiceEnabled = 0x15,
PersonaTestCatalog = 0x16,
PersonaCape = 0x17,
PersonaEmotes = 0x18,
StorefrontTestLayouts = 0x19,
RenderDragonRenderPath = 0x1A,
BaseGameVersioniningTestPacks = 0x1B,
LevelStoragePerfLog = 0x1C,
TrueTypeFontLoading = 0x1D,
PauseMenuOnFocusLost = 0x1E,
Count_14 = 0x1F,
};

```
#### FertilizerType : __int8
```cpp
/* 181089 */
enum FertilizerType : __int8
{
Bonemeal = 0x0,
Rapid = 0x1,
};

```
#### FileArchiver::ExportType : __int32
```cpp
/* 103133 */
enum FileArchiver::ExportType : __int32
{
Level_0 = 0x0,
Template = 0x1,
};

```
#### FileArchiver::Outcome : __int32
```cpp
/* 103115 */
enum FileArchiver::Outcome : __int32
{
Success_11 = 0x0,
FailureUnknown = 0x1,
FailureNoFile = 0x2,
FailureZipError = 0x3,
FailurePremiumContent = 0x4,
FailureEditionMismatch = 0x5,
};

```
#### FileArchiver::State : __int32
```cpp
/* 103074 */
enum FileArchiver::State : __int32
{
Idle_0 = 0x0,
Importing = 0x1,
Exporting_0 = 0x2,
};

```
#### FilePickerSettings::PickerType : __int32
```cpp
/* 186676 */
enum FilePickerSettings::PickerType : __int32
{
Invalid_26 = 0x0,
Open_1 = 0x1,
Save_1 = 0x2,
};

```
#### FileReadResult : __int32
```cpp
/* 5594 */
enum FileReadResult : __int32
{
SUCCESS = 0x0,
FAILED_TO_OPEN_FILE = 0x1,
MALFORMED = 0x2,
};

```
#### FileSystemMode : __int32
```cpp
/* 480026 */
enum FileSystemMode : __int32
{
ReadWrite_0 = 0x0,
ReadOnly_0 = 0x1,
};

```
#### FileType : __int32
```cpp
/* 422546 */
enum FileType : __int32
{
Invalid_28 = 0x0,
Zip_0 = 0x1,
EncryptedZip = 0x2,
Other_2 = 0x3,
};

```
#### FillCommand::FillMode : __int32
```cpp
/* 425433 */
enum FillCommand::FillMode : __int32
{
Replace_1 = 0x0,
Destroy_0 = 0x1,
Hollow_0 = 0x2,
Outline = 0x3,
Keep = 0x4,
};

```
#### FilterGroup::CollectionType : __int32
```cpp
/* 9578 */
enum FilterGroup::CollectionType : __int32
{
AND = 0x0,
OR = 0x1,
NOT = 0x2,
};

```
#### FilterOperator : __int16
```cpp
/* 9615 */
enum FilterOperator : __int16
{
Equal = 0x0,
NotEqual = 0x1,
GreaterThan_0 = 0x2,
LessThan_0 = 0x3,
GreaterThanOrEqual = 0x4,
LessThanOrEqual = 0x5,
};

```
#### FilterParamOption : __int8
```cpp
/* 114140 */
enum FilterParamOption : __int8
{
None_42 = 0x0,
EmptyDefaultString = 0x1,
};

```
#### FilterParamRequirement : __int32
```cpp
/* 114115 */
enum FilterParamRequirement : __int32
{
Required = 0x0,
Optional = 0x1,
};

```
#### FilterParamType : __int32
```cpp
/* 114114 */
enum FilterParamType : __int32
{
Bool_1 = 0x0,
Int_5 = 0x1,
Float_6 = 0x2,
String_4 = 0x3,
};

```
#### FilterResult : __int32
```cpp
/* 175608 */
enum FilterResult : __int32
{
ShowPrioritized = 0x0,
Show = 0x1,
Disable = 0x2,
Hide = 0x3,
};

```
#### FilterSubject : __int16
```cpp
/* 9614 */
enum FilterSubject : __int16
{
Self = 0x0,
Other = 0x1,
Player = 0x2,
Target = 0x3,
Parent = 0x4,
Baby = 0x5,
Block = 0x6,
COUNT_1 = 0x7,
};

```
#### FireworkChargeItem::Shape : __int32
```cpp
/* 170712 */
enum FireworkChargeItem::Shape : __int32
{
SHAPE_NONE = 0x0,
SHAPE_LARGE_BALL = 0x1,
SHAPE_STAR = 0x2,
SHAPE_HEAD_CREEPER = 0x3,
SHAPE_BURST = 0x4,
SHAPE_COUNT = 0x5,
};

```
#### FishPattern : __int32
```cpp
/* 124442 */
enum FishPattern : __int32
{
PATTERN_1 = 0x0,
PATTERN_2 = 0x1,
PATTERN_3 = 0x2,
PATTERN_4 = 0x3,
PATTERN_5 = 0x4,
PATTERN_6 = 0x5,
COUNT_8 = 0x6,
};

```
#### Flip : __int32
```cpp
/* 223287 */
enum Flip : __int32
{
None_50 = 0x0,
RotateCW = 0x1,
RotateCCW = 0x2,
Rotate180_0 = 0x3,
MirrorX = 0x4,
DontRotate = 0x5,
};

```
#### FlowerBlock::Type : __int32
```cpp
/* 251029 */
enum FlowerBlock::Type : __int32
{
Yellow_3 = 0x0,
Red_5 = 0x1,
WitherRose_0 = 0x2,
};

```
#### FlowerType : __int32
```cpp
/* 183717 */
enum FlowerType : __int32
{
Poppy_0 = 0x0,
Orchid = 0x1,
Allium_0 = 0x2,
Houstonia = 0x3,
TulipRed = 0x4,
TulipOrange = 0x5,
TulipWhite = 0x6,
TulipPink = 0x7,
Oxeye = 0x8,
Cornflower_0 = 0x9,
LilyOfTheValley_0 = 0xA,
_count_37 = 0xB,
};

```
#### FocusImpact : __int8
```cpp
/* 89287 */
enum FocusImpact : __int8
{
Neutral = 0x0,
ActivateFocus = 0x1,
DeactivateFocus = 0x2,
};

```
#### FoodItemComponent::OnUseAction : __int32
```cpp
/* 173072 */
enum FoodItemComponent::OnUseAction : __int32
{
NONE_11 = 0xFFFFFFFF,
CHORUS_TELEPORT = 0x0,
SUSPICIOUS_STEW_EFFECT = 0x1,
};

```
#### FreezeOnHitSubcomponent::Shape : __int8
```cpp
/* 174011 */
enum FreezeOnHitSubcomponent::Shape : __int8
{
Cube = 0x0,
Sphere = 0x1,
};

```
#### FullscreenMode : __int32
```cpp
/* 480114 */
enum FullscreenMode : __int32
{
Windowed = 0x0,
Fullscreen = 0x1,
};

```
#### FunctionState : __int8
```cpp
/* 95066 */
enum FunctionState : __int8
{
Uninitialized_0 = 0x1,
EngineVersionNotInitialized = 0x2,
Valid_1 = 0x3,
};

```
#### FurnaceBlockActor::$78D9F25919EA3E1AC07246132E3A6E19 : __int32
```cpp
/* 175423 */
enum FurnaceBlockActor::$78D9F25919EA3E1AC07246132E3A6E19 : __int32
{
SLOT_INGREDIENT_0 = 0x0,
SLOT_FUEL_0 = 0x1,
SLOT_RESULT = 0x2,
NUM_ITEMS = 0x3,
};

```
#### FurnaceContainerData : __int32
```cpp
/* 175422 */
enum FurnaceContainerData : __int32
{
SetTickCount = 0x0,
SetLitTime = 0x1,
SetLitDuration = 0x2,
SetStoredXP = 0x3,
};

```
#### GameRule::Type : __int8
```cpp
/* 946 */
enum GameRule::Type : __int8
{
Invalid = 0x0,
Bool = 0x1,
Int = 0x2,
Float = 0x3,
};

```
#### GameRules::GameRulesIndex : __int32
```cpp
/* 13184 */
enum GameRules::GameRulesIndex : __int32
{
INVALID_GAME_RULE = 0xFFFFFFFF,
COMMAND_BLOCK_OUTPUT = 0x0,
DO_DAYLIGHT_CYCLE = 0x1,
DO_ENTITY_DROPS = 0x2,
DO_FIRE_TICK = 0x3,
DO_MOB_LOOT = 0x4,
DO_MOB_SPAWNING = 0x5,
DO_TILE_DROPS = 0x6,
DO_WEATHER_CYCLE = 0x7,
DROWNING_DAMAGE = 0x8,
FALL_DAMAGE = 0x9,
FIRE_DAMAGE = 0xA,
KEEP_INVENTORY = 0xB,
MOB_GRIEFING = 0xC,
PVP = 0xD,
SHOW_COORDINATES = 0xE,
DO_NATURAL_REGENERATION = 0xF,
DO_TNT_EXPLODE = 0x10,
SEND_COMMAND_FEEDBACK = 0x11,
EXPERIMENTAL_GAMEPLAY = 0x12,
MAX_COMMAND_CHAIN_LENGTH = 0x13,
DO_INSOMNIA = 0x14,
COMMAND_BLOCKS_ENABLED = 0x15,
RANDOM_TICK_SPEED = 0x16,
DO_IMMEDIATE_RESPAWN = 0x17,
SHOW_DEATH_MESSAGES = 0x18,
FUNCTION_COMMAND_LIMIT = 0x19,
PLAYER_SPAWN_RADIUS = 0x1A,
SHOW_TAGS = 0x1B,
VANILLA_GAME_RULE_COUNT = 0x1C,
GLOBAL_MUTE = 0x1C,
ALLOW_DESTRUCTIVE_OBJECTS = 0x1D,
ALLOW_MOBS = 0x1E,
CODE_BUILDER = 0x1F,
EDU_GAME_RULE_COUNT = 0x20,
};

```
#### GameType : __int32
```cpp
/* 5593 */
enum GameType : __int32
{
Undefined = 0xFFFFFFFF,
Survival = 0x0,
Creative = 0x1,
Adventure = 0x2,
SurvivalViewer = 0x3,
CreativeViewer = 0x4,
Default = 0x5,
WorldDefault = 0x0,
};

```
#### GameVersion::Octet : __int32
```cpp
/* 5655 */
enum GameVersion::Octet : __int32
{
MAJOR = 0x0,
MINOR = 0x1,
PATCH = 0x2,
REVISION = 0x3,
BETA = 0x4,
NUM_OCTETS = 0x5,
INVALID = 0x5,
};

```
#### GeneratorType : __int32
```cpp
/* 5595 */
enum GeneratorType : __int32
{
Legacy = 0x0,
Overworld = 0x1,
Flat = 0x2,
Nether = 0x3,
TheEnd = 0x4,
Undefined_0 = 0x5,
};

```
#### HandSlot : __int32
```cpp
/* 13188 */
enum HandSlot : __int32
{
Mainhand = 0x0,
Offhand = 0x1,
_count_0 = 0x2,
};

```
#### HardcodedSpawnAreaType : __int8
```cpp
/* 34079 */
enum HardcodedSpawnAreaType : __int8
{
None_11 = 0x0,
NetherFortress = 0x1,
WitchHut_0 = 0x2,
OceanMonument = 0x3,
Village_Deprecated = 0x4,
PillagerOutpost = 0x5,
NewVillage_Deprecated = 0x6,
_Count = 0x7,
};

```
#### HarvestFarmBlockGoal::Task : __int32
```cpp
/* 122533 */
enum HarvestFarmBlockGoal::Task : __int32
{
NONE_9 = 0xFFFFFFFF,
REAP = 0x0,
SOW = 0x1,
};

```
#### HatchLevel : __int32
```cpp
/* 227743 */
enum HatchLevel : __int32
{
NoCracks = 0x0,
Cracked_0 = 0x1,
MaxCracked = 0x2,
_count_45 = 0x3,
};

```
#### HitResultType : __int32
```cpp
/* 13187 */
enum HitResultType : __int32
{
TILE = 0x0,
ENTITY = 0x1,
ENTITY_OUT_OF_RANGE = 0x2,
NO_HIT = 0x3,
};

```
#### HorseArmorItem::HorseArmorTier : __int32
```cpp
/* 183761 */
enum HorseArmorItem::HorseArmorTier : __int32
{
TIER_NONE = 0x0,
TIER_LEATHER_0 = 0x1,
TIER_IRON_0 = 0x2,
TIER_GOLD_0 = 0x3,
TIER_DIAMOND_0 = 0x4,
};

```
#### HorseEquipContainerController::EquipSlot : __int32
```cpp
/* 456093 */
enum HorseEquipContainerController::EquipSlot : __int32
{
SLOT_SADDLE = 0x0,
SLOT_ARMOR = 0x1,
};

```
#### HorseFlags : __int32
```cpp
/* 124180 */
enum HorseFlags : __int32
{
FLAG_SADDLE = 0x4,
FLAG_BRED = 0x10,
FLAG_EATING = 0x20,
FLAG_STANDING = 0x40,
FLAG_OPEN_MOUTH = 0x80,
};

```
#### HorseIds : __int32
```cpp
/* 124181 */
enum HorseIds : __int32
{
DATA_ID_HORSE_FLAGS = 0x10,
DATA_ID_TYPE = 0x13,
DATA_ID_TYPE_VARIANT = 0x14,
DATA_ID_OWNER_UUID = 0x15,
};

```
#### HorseInventoryEnum : __int32
```cpp
/* 114716 */
enum HorseInventoryEnum : __int32
{
INV_SLOT_SADDLE = 0x0,
INV_SLOT_ARMOR = 0x1,
INV_BASE_COUNT = 0x2,
};

```
#### HorseMarkings : __int32
```cpp
/* 124183 */
enum HorseMarkings : __int32
{
MARKING_NONE = 0x0,
MARKING_WHITE_DETAILS = 0x1,
MARKING_WHITE_FIELDS = 0x2,
MARKING_WHITE_DOTS = 0x3,
MARKING_BLACK_DOTS = 0x4,
MARKING_COUNT = 0x5,
};

```
#### HorseType : __int32
```cpp
/* 114715 */
enum HorseType : __int32
{
TYPE_UNSET = 0xFFFFFFFF,
TYPE_HORSE = 0x0,
TYPE_DONKEY = 0x1,
TYPE_MULE = 0x2,
TYPE_UNDEAD = 0x3,
TYPE_SKELETON = 0x4,
TYPE_COUNT = 0x5,
};

```
#### HorseVariant : __int32
```cpp
/* 124182 */
enum HorseVariant : __int32
{
VARIANT_WHITE = 0x0,
VARIANT_CREAMY = 0x1,
VARIANT_CHESTNUT = 0x2,
VARIANT_BROWN = 0x3,
VARIANT_BLACK = 0x4,
VARIANT_GRAY = 0x5,
VARIANT_DARKBROWN = 0x6,
VARIANT_COUNT = 0x7,
};

```
#### HugeMushroomBlock::Type : __int32
```cpp
/* 251035 */
enum HugeMushroomBlock::Type : __int32
{
Brown_2 = 0x0,
Red_6 = 0x1,
};

```
#### HurtByType : __int32
```cpp
/* 100821 */
enum HurtByType : __int32
{
UNDEFINED_0 = 0x0,
HURT_BY_ACTOR = 0x1,
HURT_BY_PROJECTILE = 0x2,
HURT_BY_BLOCK = 0x3,
HurtByType_Count = 0x4,
};

```
#### IFileChunkUploader::UploadStreamResult : __int32
```cpp
/* 101568 */
enum IFileChunkUploader::UploadStreamResult : __int32
{
Success_10 = 0x0,
Failure = 0x1,
FailureForbidden = 0x2,
None_37 = 0x3,
};

```
#### IMinecraftEventing::ClubsEngagementAction : __int32
```cpp
/* 44640 */
enum IMinecraftEventing::ClubsEngagementAction : __int32
{
Like = 0x0,
Unlike = 0x1,
Post = 0x2,
Delete = 0x3,
Report = 0x4,
Comment = 0x5,
};

```
#### IMinecraftEventing::ClubsEngagementTargetType : __int32
```cpp
/* 44646 */
enum IMinecraftEventing::ClubsEngagementTargetType : __int32
{
Unknown_12 = 0x0,
ImageFeedPost = 0x1,
TextFeedPost = 0x2,
Comment_0 = 0x3,
};

```
#### IMinecraftEventing::ClubsFeedScreenSource : __int32
```cpp
/* 44634 */
enum IMinecraftEventing::ClubsFeedScreenSource : __int32
{
PlayScreen = 0x0,
PauseScreen = 0x1,
};

```
#### IMinecraftEventing::ConnectionFailureReason : __int32
```cpp
/* 45298 */
enum IMinecraftEventing::ConnectionFailureReason : __int32
{
Unknown_19 = 0xFFFFFFFF,
MismatchedMinecraftProtocol = 0x1,
MismatchedRaknetVersion = 0x2,
};

```
#### IMinecraftEventing::DayOneExperienceState : __int32
```cpp
/* 44628 */
enum IMinecraftEventing::DayOneExperienceState : __int32
{
Started = 0x0,
CompletedWithoutWorlds = 0x1,
CompletedWithImportSkipped = 0x2,
CompletedWithImport = 0x3,
};

```
#### IMinecraftEventing::DeviceAccountFailurePhase : __int32
```cpp
/* 45295 */
enum IMinecraftEventing::DeviceAccountFailurePhase : __int32
{
Unknown_18 = 0x0,
SignIn = 0x1,
LoadCredentials = 0x2,
TitleKey = 0x3,
StoreVerify = 0x4,
PlayFabCreate_Configured = 0x5,
PlayFabCreate = 0x6,
};

```
#### IMinecraftEventing::EduSignInStage : __int32
```cpp
/* 45301 */
enum IMinecraftEventing::EduSignInStage : __int32
{
Unknown_20 = 0x0,
AttemptingActiveDirectory = 0x1,
FailedActiveDirectory = 0x2,
AttemptingMuts = 0x3,
FailedMuts = 0x4,
PresentingingEula = 0x5,
Success_7 = 0x6,
RefreshingActiveDirectory = 0x7,
RefreshActiveDirectorySuccess = 0x8,
RefreshActiveDirectoryFailed = 0x9,
};

```
#### IMinecraftEventing::EducationLessonAction : __int32
```cpp
/* 44616 */
enum IMinecraftEventing::EducationLessonAction : __int32
{
Start = 0x0,
Continue = 0x1,
Restart = 0x2,
Host_0 = 0x3,
Join = 0x4,
Finish = 0x5,
};

```
#### IMinecraftEventing::ElementConstructorUseType : __int32
```cpp
/* 45291 */
enum IMinecraftEventing::ElementConstructorUseType : __int32
{
Created = 0x0,
Entered = 0x1,
};

```
#### IMinecraftEventing::ExportOutcome : __int32
```cpp
/* 44622 */
enum IMinecraftEventing::ExportOutcome : __int32
{
Failed_1 = 0x0,
Success_3 = 0x1,
};

```
#### IMinecraftEventing::ExportStage : __int32
```cpp
/* 45300 */
enum IMinecraftEventing::ExportStage : __int32
{
Initiated = 0x0,
Completed_0 = 0x1,
};

```
#### IMinecraftEventing::FileTransmissionDirection : __int32
```cpp
/* 45292 */
enum IMinecraftEventing::FileTransmissionDirection : __int32
{
Download = 0x0,
Upload = 0x1,
};

```
#### IMinecraftEventing::FileTransmissionState : __int32
```cpp
/* 45293 */
enum IMinecraftEventing::FileTransmissionState : __int32
{
Failed_4 = 0x0,
Started_0 = 0x1,
Completed = 0x2,
Resumed = 0x3,
Canceled_0 = 0xFFFFFFFF,
};

```
#### IMinecraftEventing::FileTransmissionType : __int32
```cpp
/* 45294 */
enum IMinecraftEventing::FileTransmissionType : __int32
{
Realm_file = 0x1,
Dlc = 0x2,
Remix3D_DEPRECATED = 0x3,
DlcUpdate_Auto = 0x4,
DlcUpdate_User = 0x5,
};

```
#### IMinecraftEventing::NetworkType : __int32
```cpp
/* 45285 */
enum IMinecraftEventing::NetworkType : __int32
{
Local_2 = 0x0,
LAN = 0x1,
External = 0x2,
Friend = 0x3,
Realm = 0x4,
ThirdParty = 0x5,
};

```
#### IMinecraftEventing::OpenCodeMethod : __int32
```cpp
/* 44604 */
enum IMinecraftEventing::OpenCodeMethod : __int32
{
TouchHUD = 0x0,
Keypress = 0x1,
Command_1 = 0x2,
};

```
#### IMinecraftEventing::PetDeathContext : __int32
```cpp
/* 44658 */
enum IMinecraftEventing::PetDeathContext : __int32
{
DiedOfOtherCause = 0x0,
PlayerMurdered = 0x1,
OwnerMurdered = 0x2,
MobMurdered = 0x3,
};

```
#### IMinecraftEventing::PromotionType : __int32
```cpp
/* 45303 */
enum IMinecraftEventing::PromotionType : __int32
{
Featured = 0x0,
Default_6 = 0x1,
None_19 = 0x2,
};

```
#### IMinecraftEventing::PurchaseResult : __int32
```cpp
/* 45296 */
enum IMinecraftEventing::PurchaseResult : __int32
{
Success_6 = 0x1,
Canceled_1 = 0x0,
Failed_5 = 0xFFFFFFFF,
};

```
#### IMinecraftEventing::RealmConnectionFlow : __int32
```cpp
/* 45288 */
enum IMinecraftEventing::RealmConnectionFlow : __int32
{
PlayScreen_0 = 0x0,
SettingsScreen = 0x1,
InviteLink = 0x2,
WhiteList = 0x3,
Marketplace = 0x4,
CreateScreen = 0x5,
};

```
#### IMinecraftEventing::RealmConnectionLambda : __int32
```cpp
/* 45289 */
enum IMinecraftEventing::RealmConnectionLambda : __int32
{
CompletedCallback = 0x0,
RetryCallback = 0x1,
ProgressScreenTickCallback = 0x2,
ProgressScreenOnCancelCallback = 0x3,
GameServerConnectProgressCallback = 0x4,
};

```
#### IMinecraftEventing::RealmConnectionResult : __int32
```cpp
/* 45290 */
enum IMinecraftEventing::RealmConnectionResult : __int32
{
Success_5 = 0x0,
SuccessWithWarning = 0x1,
FailWithUnnassignedDevVersion = 0x2,
Fail_1 = 0x3,
Retry = 0x4,
CancelByUser = 0x5,
InvalidCallback = 0x6,
Unknown_17 = 0x7,
TimedOut = 0x8,
};

```
#### IMinecraftEventing::ServerConnectionOutcome : __int32
```cpp
/* 45286 */
enum IMinecraftEventing::ServerConnectionOutcome : __int32
{
Success_4 = 0x0,
Failed_2 = 0x1,
Failed_UserOffline = 0x2,
Failed_ServerFull = 0x3,
Failed_ServerOffline = 0x4,
};

```
#### IMinecraftEventing::ShareMode : __int32
```cpp
/* 45299 */
enum IMinecraftEventing::ShareMode : __int32
{
Share = 0x1,
Copy = 0x2,
};

```
#### IMinecraftEventing::SignInStage : __int32
```cpp
/* 45287 */
enum IMinecraftEventing::SignInStage : __int32
{
Unknown_16 = 0x0,
Starting = 0x1,
Failed_3 = 0x2,
Canceled = 0x3,
Succeeded = 0x4,
Succeeded_New_Account = 0x5,
Failed_Create = 0x6,
};

```
#### IMinecraftEventing::StoreType : __int32
```cpp
/* 45297 */
enum IMinecraftEventing::StoreType : __int32
{
Store = 0x0,
DressingRoom = 0x1,
};

```
#### IMinecraftEventing::StructureBlockActionType : __int32
```cpp
/* 44542 */
enum IMinecraftEventing::StructureBlockActionType : __int32
{
Unknown_11 = 0xFFFFFFFF,
Save = 0x0,
Load = 0x1,
Export = 0x2,
Export3D = 0x3,
LeaveScreen = 0x4,
};

```
#### IdentityDefinition::Type : __int8
```cpp
/* 70053 */
enum IdentityDefinition::Type : __int8
{
Invalid_14 = 0x0,
Player_2 = 0x1,
Entity_2 = 0x2,
FakePlayer = 0x3,
};

```
#### InHandUpdateType : __int8
```cpp
/* 181498 */
enum InHandUpdateType : __int8
{
NONE_13 = 0x0,
UPDATE = 0x1,
SWAP = 0x2,
};

```
#### InMemoryAccessMode : __int32
```cpp
/* 463110 */
enum InMemoryAccessMode : __int32
{
Read = 0x0,
Write = 0x1,
};

```
#### InputMode : __int32
```cpp
/* 44576 */
enum InputMode : __int32
{
Undefined_7 = 0x0,
Mouse = 0x1,
Touch = 0x2,
GamePad = 0x3,
MotionController_0 = 0x4,
Count_5 = 0x5,
};

```
#### IntellisenseUtils::MatcherOptions : __int8
```cpp
/* 93423 */
enum IntellisenseUtils::MatcherOptions : __int8
{
NONE_7 = 0x0,
HIGHLIGHT = 0x1,
CASE_SENSITIVE = 0x2,
};

```
#### InteractPacket::Action : __int8
```cpp
/* 79706 */
enum InteractPacket::Action : __int8
{
StopRiding = 0x3,
InteractUpdate = 0x4,
NpcOpen = 0x5,
OpenInventory = 0x6,
};

```
#### InventorySource::InventorySourceFlags : __int32
```cpp
/* 33268 */
enum InventorySource::InventorySourceFlags : __int32
{
NoFlag = 0x0,
WorldInteraction_Random = 0x1,
};

```
#### InventorySourceType : __int32
```cpp
/* 33266 */
enum InventorySourceType : __int32
{
InvalidInventory = 0xFFFFFFFF,
ContainerInventory = 0x0,
GlobalInventory = 0x1,
WorldInteraction = 0x2,
CreativeInventory = 0x3,
UntrackedInteractionUI = 0x64,
NonImplementedFeatureTODO = 0x1869F,
};

```
#### InventoryTransactionError : __int32
```cpp
/* 33512 */
enum InventoryTransactionError : __int32
{
Unknown_4 = 0x0,
NoError = 0x1,
BalanceMismatch = 0x2,
SourceItemMismatch = 0x3,
InventoryMismatch = 0x4,
SizeMismatch = 0x5,
AuthorityMismatch = 0x6,
StateMismatch = 0x7,
ApiDenied = 0x8,
};

```
#### ItemAcquisitionMethod : __int32
```cpp
/* 13214 */
enum ItemAcquisitionMethod : __int32
{
};

```
#### ItemAcquisitionMethod_0 : __int32
```cpp
/* 43301 */
enum ItemAcquisitionMethod_0 : __int32
{
Unknown_8 = 0xFFFFFFFF,
None_16 = 0x0,
PickedUp = 0x1,
Crafted_0 = 0x2,
TakenFromChest = 0x3,
TakenFromEnderchest = 0x4,
Bought = 0x5,
Anvil = 0x6,
Smelted = 0x7,
Brewed = 0x8,
Filled_0 = 0x9,
Trading_0 = 0xA,
Fishing = 0xB,
Container = 0xD,
};

```
#### ItemAddType : __int32
```cpp
/* 174692 */
enum ItemAddType : __int32
{
All_7 = 0x0,
Partial_0 = 0x1,
None_49 = 0x2,
};

```
#### ItemColor : __int8
```cpp
/* 181069 */
enum ItemColor : __int8
{
Black_1 = 0x0,
Red_3 = 0x1,
Green_1 = 0x2,
Brown_1 = 0x3,
Blue_1 = 0x4,
Purple_1 = 0x5,
Cyan_1 = 0x6,
Silver_1 = 0x7,
Gray_1 = 0x8,
Pink_1 = 0x9,
Lime_0 = 0xA,
Yellow_1 = 0xB,
LightBlue_0 = 0xC,
Magenta_1 = 0xD,
Orange_1 = 0xE,
White_1 = 0xF,
_count_26 = 0x10,
};

```
#### ItemPlaceType : __int32
```cpp
/* 174690 */
enum ItemPlaceType : __int32
{
All_6 = 0x0,
One_0 = 0x1,
};

```
#### ItemReleaseInventoryTransaction::ActionType : __int32
```cpp
/* 173074 */
enum ItemReleaseInventoryTransaction::ActionType : __int32
{
Release_0 = 0x0,
Use_0 = 0x1,
};

```
#### ItemSetType : __int32
```cpp
/* 174691 */
enum ItemSetType : __int32
{
Place_3 = 0x0,
Swap_0 = 0x1,
Add_5 = 0x2,
None_48 = 0x3,
};

```
#### ItemTakeType : __int32
```cpp
/* 174689 */
enum ItemTakeType : __int32
{
All_5 = 0x0,
Half = 0x1,
One = 0x2,
};

```
#### ItemTransferAmount::ItemTransferAmountTag : __int32
```cpp
/* 174687 */
enum ItemTransferAmount::ItemTransferAmountTag : __int32
{
RequestAmount = 0x0,
TakeType = 0x1,
PlaceType = 0x2,
};

```
#### ItemUseInventoryTransaction::ActionType : __int32
```cpp
/* 180450 */
enum ItemUseInventoryTransaction::ActionType : __int32
{
Place_4 = 0x0,
Use_1 = 0x1,
Destroy = 0x2,
};

```
#### ItemUseMethod : __int32
```cpp
/* 13212 */
enum ItemUseMethod : __int32
{
};

```
#### ItemUseMethod_0 : __int32
```cpp
/* 43215 */
enum ItemUseMethod_0 : __int32
{
Unknown_6 = 0xFFFFFFFF,
EquipArmor = 0x0,
Eat_1 = 0x1,
Attack_0 = 0x2,
Consume = 0x3,
Throw_0 = 0x4,
Shoot_0 = 0x5,
Place_0 = 0x6,
FillBottle = 0x7,
FillBucket = 0x8,
PourBucket = 0x9,
UseTool = 0xA,
Interact = 0xB,
Retrieved = 0xC,
Dyed = 0xD,
Traded = 0xE,
_Count_0 = 0xF,
};

```
#### ItemUseOnActorInventoryTransaction::ActionType : __int32
```cpp
/* 180449 */
enum ItemUseOnActorInventoryTransaction::ActionType : __int32
{
Interact_1 = 0x0,
Attack_2 = 0x1,
ItemInteract = 0x2,
};

```
#### JournaledFile::Progression : __int32
```cpp
/* 290436 */
enum JournaledFile::Progression : __int32
{
NeverWritten = 0x0,
WriteFailed = 0x1,
WriteSuccess = 0x2,
};

```
#### JumpType : __int32
```cpp
/* 56477 */
enum JumpType : __int32
{
NONE_3 = 0x0,
HOP = 0x1,
STEP = 0x2,
SPRINT = 0x3,
_COUNT = 0x4,
};

```
#### KeyFrameLerpStyle : __int32
```cpp
/* 124577 */
enum KeyFrameLerpStyle : __int32
{
Linear = 0x0,
CatmullRom = 0x1,
_Count_4 = 0x2,
};

```
#### KeyFrameTransformPrePostSplitState : __int64
```cpp
/* 125121 */
enum KeyFrameTransformPrePostSplitState : __int64
{
Auto = 0x0,
Single = 0x1,
ForcedSplit = 0x2,
_Count_5 = 0x3,
};

```
#### KnownPackType : __int32
```cpp
/* 5661 */
enum KnownPackType : __int32
{
Valid = 0x0,
Invalid_4 = 0x1,
};

```
#### LabTablePacket::Type : __int8
```cpp
/* 79927 */
enum LabTablePacket::Type : __int8
{
StartCombine = 0x0,
StartReaction = 0x1,
Reset = 0x2,
};

```
#### LabTableReactionType : __int8
```cpp
/* 79933 */
enum LabTableReactionType : __int8
{
None_28 = 0x0,
IceBomb_0 = 0x1,
Bleach_0 = 0x2,
ElephantToothpaste = 0x3,
Fertilizer = 0x4,
HeatBlock = 0x5,
MagnesiumSalts = 0x6,
MiscFire = 0x7,
MiscExplosion = 0x8,
MiscLava = 0x9,
MiscMystical = 0xA,
MiscSmoke = 0xB,
MiscLargeSmoke = 0xC,
};

```
#### LayerValues::Terrain : __int8
```cpp
/* 39129 */
enum LayerValues::Terrain : __int8
{
Ocean = 0x0,
Land_0 = 0x1,
SpecialLand_1 = 0x2,
SpecialLand_2 = 0x3,
SpecialLand_3 = 0x4,
SpecialLand_4 = 0x5,
SpecialLand_5 = 0x6,
SpecialLand_6 = 0x7,
SpecialLand_7 = 0x8,
SpecialLand_8 = 0x9,
SpecialLand_9 = 0xA,
SpecialLand_10 = 0xB,
SpecialLand_11 = 0xC,
SpecialLand_12 = 0xD,
SpecialLand_13 = 0xE,
SpecialLand_14 = 0xF,
SpecialLand_15 = 0x10,
SpecialLand_16 = 0x11,
};

```
#### LayerZooms::Alignment : __int32
```cpp
/* 40588 */
enum LayerZooms::Alignment : __int32
{
Min = 0x0,
Center = 0x1,
Max = 0x2,
};

```
#### LeafSize : __int32
```cpp
/* 227982 */
enum LeafSize : __int32
{
NoLeaves = 0x0,
SmallLeaves = 0x1,
LargeLeaves = 0x2,
_count_47 = 0x3,
};

```
#### LegacyFlowerFeature::Type : __int32
```cpp
/* 29834 */
enum LegacyFlowerFeature::Type : __int32
{
FlowerForest_0 = 0x0,
Forest_0 = 0x1,
Overworld_0 = 0x2,
Plains_0 = 0x3,
Swamp = 0x4,
};

```
#### LegacyForestFoliageFeature::Type : __int32
```cpp
/* 29826 */
enum LegacyForestFoliageFeature::Type : __int32
{
Flower = 0x0,
Normal_2 = 0x1,
Roofed = 0x2,
};

```
#### LegacyTreeFeature::Type : __int32
```cpp
/* 29831 */
enum LegacyTreeFeature::Type : __int32
{
BambooJungle = 0x0,
BirchForest = 0x1,
BirchForestMutated = 0x2,
ExtremeHillsPlusTrees = 0x3,
FlowerForest = 0x4,
Forest = 0x5,
Ice = 0x6,
Jungle_1 = 0x7,
JungleEdge = 0x8,
MesaForest = 0x9,
Plains = 0xA,
Savanna = 0xB,
SavannaMutated = 0xC,
Taiga = 0xD,
TaigaMega = 0xE,
TaigaMegaSpruce = 0xF,
};

```
#### LevelChunk::Finalization : __int32
```cpp
/* 35001 */
enum LevelChunk::Finalization : __int32
{
NeedsInstaticking = 0x0,
NeedsPopulation = 0x1,
Done = 0x2,
};

```
#### LevelChunk::Tag : __int8
```cpp
/* 252819 */
enum LevelChunk::Tag : __int8
{
Data2D = 0x2D,
Data2DLegacy = 0x2E,
SubChunkPrefix = 0x2F,
LegacyTerrain = 0x30,
BlockEntity_1 = 0x31,
Entity_6 = 0x32,
PendingTicks_0 = 0x33,
LegacyBlockExtraData = 0x34,
BiomeState_0 = 0x35,
FinalizedState = 0x36,
ConversionData = 0x37,
BorderBlocks_0 = 0x38,
HardcodedSpawners = 0x39,
RandomTicks_0 = 0x3A,
Version = 0x76,
};

```
#### LevelChunkDataField : __int32
```cpp
/* 35031 */
enum LevelChunkDataField : __int32
{
BiomeState = 0x0,
BlockEntity = 0x1,
Entity_0 = 0x2,
PendingTicks = 0x3,
BorderBlocks = 0x4,
RandomTicks = 0x5,
_count_9 = 0x6,
};

```
#### LevelChunkFormat : __int8
```cpp
/* 34993 */
enum LevelChunkFormat : __int8
{
v9_00 = 0x0,
v9_02 = 0x1,
v9_05 = 0x2,
v17_0 = 0x3,
v18_0 = 0x4,
vConsole1_to_v18_0 = 0x5,
v1_2_0 = 0x6,
v1_2_0_bis = 0x7,
v1_3_0 = 0x8,
v1_8_0 = 0x9,
v1_9_0 = 0xA,
v1_10_0 = 0xB,
v1_11_0 = 0xC,
v1_11_1 = 0xD,
v1_11_2 = 0xE,
v1_12_0 = 0xF,
v1_14_0 = 0x10,
Count_3 = 0x11,
};

```
#### LevelEvent : __int16
```cpp
/* 35037 */
enum LevelEvent : __int16
{
Undefined_4 = 0x0,
SoundClick = 0x3E8,
SoundClickFail = 0x3E9,
SoundLaunch = 0x3EA,
SoundOpenDoor = 0x3EB,
SoundFizz = 0x3EC,
SoundFuse = 0x3ED,
SoundPlayRecording = 0x3EE,
SoundGhastWarning = 0x3EF,
SoundGhastFireball = 0x3F0,
SoundBlazeFireball = 0x3F1,
SoundZombieWoodenDoor = 0x3F2,
SoundZombieDoorCrash = 0x3F4,
SoundZombieInfected = 0x3F8,
SoundZombieConverted = 0x3F9,
SoundEndermanTeleport = 0x3FA,
SoundAnvilBroken = 0x3FC,
SoundAnvilUsed = 0x3FD,
SoundAnvilLand = 0x3FE,
SoundInfinityArrowPickup = 0x406,
SoundTeleportEnderPearl = 0x408,
SoundAddItem = 0x410,
SoundItemFrameBreak = 0x411,
SoundItemFramePlace = 0x412,
SoundItemFrameRemoveItem = 0x413,
SoundItemFrameRotateItem = 0x414,
SoundExperienceOrbPickup = 0x41B,
SoundTotemUsed = 0x41C,
SoundArmorStandBreak = 0x424,
SoundArmorStandHit = 0x425,
SoundArmorStandLand = 0x426,
SoundArmorStandPlace = 0x427,
ParticlesShoot = 0x7D0,
ParticlesDestroyBlock = 0x7D1,
ParticlesPotionSplash = 0x7D2,
ParticlesEyeOfEnderDeath = 0x7D3,
ParticlesMobBlockSpawn = 0x7D4,
ParticleCropGrowth = 0x7D5,
ParticleSoundGuardianGhost = 0x7D6,
ParticleDeathSmoke = 0x7D7,
ParticleDenyBlock = 0x7D8,
ParticleGenericSpawn = 0x7D9,
ParticlesDragonEgg = 0x7DA,
ParticlesCropEaten = 0x7DB,
ParticlesCrit = 0x7DC,
ParticlesTeleport = 0x7DD,
ParticlesCrackBlock = 0x7DE,
ParticlesBubble = 0x7DF,
ParticlesEvaporate = 0x7E0,
ParticlesDestroyArmorStand = 0x7E1,
ParticlesBreakingEgg = 0x7E2,
ParticleDestroyEgg = 0x7E3,
ParticlesEvaporateWater = 0x7E4,
ParticlesDestroyBlockNoSound = 0x7E5,
ParticlesKnockbackRoar = 0x7E6,
ParticlesTeleportTrail = 0x7E7,
ParticlesPointCloud = 0x7E8,
ParticlesExplosion = 0x7E9,
ParticlesBlockExplosion = 0x7EA,
StartRaining = 0xBB9,
StartThunderstorm = 0xBBA,
StopRaining = 0xBBB,
StopThunderstorm = 0xBBC,
GlobalPause = 0xBBD,
SimTimeStep = 0xBBE,
SimTimeScale = 0xBBF,
ActivateBlock = 0xDAC,
CauldronExplode = 0xDAD,
CauldronDyeArmor = 0xDAE,
CauldronCleanArmor = 0xDAF,
CauldronFillPotion = 0xDB0,
CauldronTakePotion = 0xDB1,
CauldronFillWater = 0xDB2,
CauldronTakeWater = 0xDB3,
CauldronAddDye = 0xDB4,
CauldronCleanBanner = 0xDB5,
CauldronFlush = 0xDB6,
AgentSpawnEffect = 0xDB7,
CauldronFillLava = 0xDB8,
CauldronTakeLava = 0xDB9,
StartBlockCracking = 0xE10,
StopBlockCracking = 0xE11,
UpdateBlockCracking = 0xE12,
AllPlayersSleeping = 0x2648,
JumpPrevented = 0x2652,
ParticleLegacyEvent = 0x4000,
};

```
#### LevelSoundEvent : __int32
```cpp
/* 35038 */
enum LevelSoundEvent : __int32
{
ItemUseOn = 0x0,
Hit = 0x1,
Step = 0x2,
Fly = 0x3,
Jump = 0x4,
Break = 0x5,
Place = 0x6,
HeavyStep = 0x7,
Gallop = 0x8,
Fall = 0x9,
Ambient_0 = 0xA,
AmbientBaby = 0xB,
AmbientInWater = 0xC,
Breathe = 0xD,
Death = 0xE,
DeathInWater = 0xF,
DeathToZombie = 0x10,
Hurt = 0x11,
HurtInWater = 0x12,
Mad = 0x13,
Boost = 0x14,
Bow_0 = 0x15,
SquishBig = 0x16,
SquishSmall = 0x17,
FallBig = 0x18,
FallSmall = 0x19,
Splash = 0x1A,
Fizz = 0x1B,
Flap = 0x1C,
Swim = 0x1D,
Drink_0 = 0x1E,
Eat_0 = 0x1F,
Takeoff = 0x20,
Shake = 0x21,
Plop = 0x22,
Land = 0x23,
Saddle = 0x24,
Armor = 0x25,
ArmorPlace = 0x26,
AddChest = 0x27,
Throw = 0x28,
Attack = 0x29,
AttackNoDamage = 0x2A,
AttackStrong = 0x2B,
Warn = 0x2C,
Shear = 0x2D,
Milk = 0x2E,
Thunder = 0x2F,
Explode_0 = 0x30,
Fire = 0x31,
Ignite = 0x32,
Fuse = 0x33,
Stare = 0x34,
Spawn = 0x35,
Shoot = 0x36,
BreakBlock = 0x37,
Launch = 0x38,
Blast = 0x39,
LargeBlast = 0x3A,
Twinkle = 0x3B,
Remedy = 0x3C,
Unfect = 0x3D,
LevelUp = 0x3E,
BowHit = 0x3F,
BulletHit = 0x40,
ExtinguishFire = 0x41,
ItemFizz = 0x42,
ChestOpen = 0x43,
ChestClosed = 0x44,
ShulkerBoxOpen = 0x45,
ShulkerBoxClosed = 0x46,
EnderChestOpen = 0x47,
EnderChestClosed = 0x48,
PowerOn = 0x49,
PowerOff = 0x4A,
Attach = 0x4B,
Detach = 0x4C,
Deny = 0x4D,
Tripod = 0x4E,
Pop = 0x4F,
DropSlot = 0x50,
Note_0 = 0x51,
Thorns = 0x52,
PistonIn = 0x53,
PistonOut = 0x54,
Portal_0 = 0x55,
Water = 0x56,
LavaPop = 0x57,
Lava_0 = 0x58,
Burp = 0x59,
BucketFillWater = 0x5A,
BucketFillLava = 0x5B,
BucketEmptyWater = 0x5C,
BucketEmptyLava = 0x5D,
EquipChain = 0x5E,
EquipDiamond = 0x5F,
EquipGeneric = 0x60,
EquipGold = 0x61,
EquipIron = 0x62,
EquipLeather = 0x63,
EquipElytra = 0x64,
Record13 = 0x65,
RecordCat = 0x66,
RecordBlocks = 0x67,
RecordChirp = 0x68,
RecordFar = 0x69,
RecordMall = 0x6A,
RecordMellohi = 0x6B,
RecordStal = 0x6C,
RecordStrad = 0x6D,
RecordWard = 0x6E,
Record11 = 0x6F,
RecordWait = 0x70,
RecordNull = 0x71,
Flop = 0x72,
GuardianCurse = 0x73,
MobWarning = 0x74,
MobWarningBaby = 0x75,
Teleport_0 = 0x76,
ShulkerOpen = 0x77,
ShulkerClose = 0x78,
Haggle = 0x79,
HaggleYes = 0x7A,
HaggleNo = 0x7B,
HaggleIdle = 0x7C,
ChorusGrow = 0x7D,
ChorusDeath = 0x7E,
Glass = 0x7F,
PotionBrewed = 0x80,
CastSpell = 0x81,
PrepareAttackSpell = 0x82,
PrepareSummon = 0x83,
PrepareWololo = 0x84,
Fang = 0x85,
Charge = 0x86,
TakePicture = 0x87,
PlaceLeashKnot = 0x88,
BreakLeashKnot = 0x89,
AmbientGrowl = 0x8A,
AmbientWhine = 0x8B,
AmbientPant = 0x8C,
AmbientPurr = 0x8D,
AmbientPurreow = 0x8E,
DeathMinVolume = 0x8F,
DeathMidVolume = 0x90,
ImitateBlaze = 0x91,
ImitateCaveSpider = 0x92,
ImitateCreeper = 0x93,
ImitateElderGuardian = 0x94,
ImitateEnderDragon = 0x95,
ImitateEnderman = 0x96,
ImitateEndermite = 0x97,
ImitateEvocationIllager = 0x98,
ImitateGhast = 0x99,
ImitateHusk = 0x9A,
ImitateIllusionIllager = 0x9B,
ImitateMagmaCube = 0x9C,
ImitatePolarBear = 0x9D,
ImitateShulker = 0x9E,
ImitateSilverfish = 0x9F,
ImitateSkeleton = 0xA0,
ImitateSlime = 0xA1,
ImitateSpider = 0xA2,
ImitateStray = 0xA3,
ImitateVex = 0xA4,
ImitateVindicationIllager = 0xA5,
ImitateWitch = 0xA6,
ImitateWither = 0xA7,
ImitateWitherSkeleton = 0xA8,
ImitateWolf = 0xA9,
ImitateZombie = 0xAA,
ImitateZombiePigman = 0xAB,
ImitateZombieVillager = 0xAC,
EnderEyePlaced = 0xAD,
EndPortalCreated = 0xAE,
AnvilUse = 0xAF,
BottleDragonBreath = 0xB0,
PortalTravel = 0xB1,
TridentHit = 0xB2,
TridentReturn = 0xB3,
TridentRiptide_1 = 0xB4,
TridentRiptide_2 = 0xB5,
TridentRiptide_3 = 0xB6,
TridentThrow = 0xB7,
TridentThunder = 0xB8,
TridentHitGround = 0xB9,
Default_4 = 0xBA,
FletchingTableUse = 0xBB,
ElemConstructOpen = 0xBC,
IceBombHit = 0xBD,
BalloonPop = 0xBE,
LTReactionIceBomb = 0xBF,
LTReactionBleach = 0xC0,
LTReactionElephantToothpaste = 0xC1,
LTReactionElephantToothpaste2 = 0xC2,
LTReactionGlowStick = 0xC3,
LTReactionGlowStick2 = 0xC4,
LTReactionLuminol = 0xC5,
LTReactionSalt = 0xC6,
LTReactionFertilizer = 0xC7,
LTReactionFireball = 0xC8,
LTReactionMagnesiumSalt = 0xC9,
LTReactionMiscFire = 0xCA,
LTReactionFire = 0xCB,
LTReactionMiscExplosion = 0xCC,
LTReactionMiscMystical = 0xCD,
LTReactionMiscMystical2 = 0xCE,
LTReactionProduct = 0xCF,
SparklerUse = 0xD0,
GlowStickUse = 0xD1,
SparklerActive = 0xD2,
ConvertToDrowned = 0xD3,
BucketFillFish = 0xD4,
BucketEmptyFish = 0xD5,
BubbleColumnUpwards = 0xD6,
BubbleColumnDownwards = 0xD7,
BubblePop = 0xD8,
BubbleUpInside = 0xD9,
BubbleDownInside = 0xDA,
HurtBaby = 0xDB,
DeathBaby = 0xDC,
StepBaby = 0xDD,
SpawnBaby = 0xDE,
Born = 0xDF,
TurtleEggBreak = 0xE0,
TurtleEggCrack = 0xE1,
TurtleEggHatched = 0xE2,
LayEgg = 0xE3,
TurtleEggAttacked = 0xE4,
BeaconActivate = 0xE5,
BeaconAmbient = 0xE6,
BeaconDeactivate = 0xE7,
BeaconPower = 0xE8,
ConduitActivate = 0xE9,
ConduitAmbient = 0xEA,
ConduitAttack = 0xEB,
ConduitDeactivate = 0xEC,
ConduitShort = 0xED,
Swoop = 0xEE,
BambooSaplingPlace = 0xEF,
PreSneeze = 0xF0,
Sneeze_0 = 0xF1,
AmbientTame = 0xF2,
Scared = 0xF3,
ScaffoldingClimb = 0xF4,
CrossbowLoadingStart = 0xF5,
CrossbowLoadingMiddle = 0xF6,
CrossbowLoadingEnd = 0xF7,
CrossbowShoot = 0xF8,
CrossbowQuickChargeStart = 0xF9,
CrossbowQuickChargeMiddle = 0xFA,
CrossbowQuickChargeEnd = 0xFB,
AmbientAggressive = 0xFC,
AmbientWorried = 0xFD,
CantBreed = 0xFE,
ShieldBlock = 0xFF,
LecternBookPlace = 0x100,
GrindstoneUse = 0x101,
Bell = 0x102,
CampfireCrackle = 0x103,
SweetBerryBushHurt = 0x106,
SweetBerryBushPick = 0x107,
Roar = 0x104,
Stun = 0x105,
CartographyTableUse = 0x108,
StonecutterUse = 0x109,
ComposterEmpty = 0x10A,
ComposterFill = 0x10B,
ComposterFillLayer = 0x10C,
ComposterReady = 0x10D,
BarrelOpen = 0x10E,
BarrelClose = 0x10F,
RaidHorn = 0x110,
LoomUse = 0x111,
AmbientInRaid = 0x112,
UICartographyTableUse = 0x113,
UIStonecutterUse = 0x114,
UILoomUse = 0x115,
SmokerUse = 0x116,
BlastFurnaceUse = 0x117,
SmithingTableUse = 0x118,
Screech = 0x119,
Sleep = 0x11A,
FurnaceUse = 0x11B,
MooshroomConvert = 0x11C,
MilkSuspiciously = 0x11D,
Celebrate = 0x11E,
JumpPrevent = 0x11F,
AmbientPollinate = 0x120,
BeehiveDrip = 0x121,
BeehiveEnter = 0x122,
BeehiveExit = 0x123,
BeehiveWork = 0x124,
BeehiveShear = 0x125,
HoneybottleDrink = 0x126,
Undefined_5 = 0x127,
};

```
#### LeverDirection : __int32
```cpp
/* 230355 */
enum LeverDirection : __int32
{
DownEastWest = 0x0,
East_1 = 0x1,
West_1 = 0x2,
South_1 = 0x3,
North_1 = 0x4,
UpNorthSouth = 0x5,
UpEastWest = 0x6,
DownNorthSouth = 0x7,
_count_50 = 0x8,
};

```
#### LimboEntitiesVersion : __int8
```cpp
/* 254192 */
enum LimboEntitiesVersion : __int8
{
v0 = 0x0,
v1_8_0_0 = 0x1,
v1_10_0_0 = 0x2,
v1_12_0_0 = 0x3,
};

```
#### ListDCommand::DetailMode : __int32
```cpp
/* 425893 */
enum ListDCommand::DetailMode : __int32
{
None_55 = 0x0,
IDs = 0x1,
UUIDs = 0x2,
Stats = 0x3,
};

```
#### LoadingState : __int32
```cpp
/* 45311 */
enum LoadingState : __int32
{
};

```
#### Localization::appendTranslations::LangLineState : __int32
```cpp
/* 60934 */
enum Localization::appendTranslations::LangLineState : __int32
{
LeadingWhitespace = 0x0,
Key = 0x1,
Value_0 = 0x2,
PostValueWhitespaceOrComment = 0x3,
};

```
#### Lockless::MemoryOrder : __int32
```cpp
/* 226 */
enum Lockless::MemoryOrder : __int32
{
Relaxed = 0x0,
Acquire = 0x1,
Release = 0x2,
AcqRel = 0x3,
SeqCst = 0x4,
Sync = 0x4,
};

```
#### LogArea : __int32
```cpp
/* 5589 */
enum LogArea : __int32
{
Actor = 0x0,
Addon_0 = 0x1,
AI = 0x2,
Animation = 0x3,
AutomatedTests = 0x4,
BiomeRegistry = 0x5,
Blocks = 0x6,
Camera = 0x7,
Commands = 0x8,
Components = 0x9,
Effects = 0xA,
Entity = 0xB,
FeatureRegistry = 0xC,
Geometry = 0xD,
Item = 0xE,
Json = 0xF,
LevelStorage = 0x10,
Log = 0x11,
Molang = 0x12,
Recipes = 0x13,
Rendering = 0x14,
Scripting = 0x15,
Sound = 0x16,
Structure = 0x17,
UI = 0x18,
COUNT_0 = 0x19,
};

```
#### LogAreaID : __int32
```cpp
/* 5591 */
enum LogAreaID : __int32
{
LOG_AREA_ALL = 0x0,
LOG_AREA_PLATFORM = 0x1,
LOG_AREA_ENTITY = 0x2,
LOG_AREA_DATABASE = 0x3,
LOG_AREA_GUI = 0x4,
LOG_AREA_SYSTEM = 0x5,
LOG_AREA_NETWORK = 0x6,
LOG_AREA_RENDER = 0x7,
LOG_AREA_MEMORY = 0x8,
LOG_AREA_ANIMATION = 0x9,
LOG_AREA_INPUT = 0xA,
LOG_AREA_LEVEL = 0xB,
LOG_AREA_SERVER = 0xC,
LOG_AREA_DLC = 0xD,
LOG_AREA_PHYSICS = 0xE,
LOG_AREA_FILE = 0xF,
LOG_AREA_STORAGE = 0x10,
LOG_AREA_REALMS = 0x11,
LOG_AREA_REALMSAPI = 0x12,
LOG_AREA_XBOXLIVE = 0x13,
LOG_AREA_USERMANAGER = 0x14,
LOG_AREA_XSAPI = 0x15,
LOG_AREA_PERF = 0x16,
LOG_AREA_TELEMETRY = 0x17,
LOG_AREA_BLOCKS = 0x18,
LOG_AREA_RAKNET = 0x19,
LOG_AREA_GAMEFACE = 0x1A,
LOG_AREA_SOUND = 0x1B,
LOG_AREA_INTERACTIVE = 0x1C,
LOG_AREA_SCRIPTING = 0x1D,
LOG_AREA_PLAYFAB = 0x1E,
LOG_AREA_AUTOMATION = 0x1F,
LOG_AREA_PERSONA = 0x20,
LOG_AREA_UNKNOWN = 0x21,
NUM_LOG_AREAS = 0x22,
};

```
#### LogLevel : __int32
```cpp
/* 5588 */
enum LogLevel : __int32
{
Verbose = 0x0,
Inform = 0x1,
Warning = 0x2,
Error = 0x3,
COUNT = 0x4,
};

```
#### MCCATEGORY : __int8
```cpp
/* 94507 */
enum MCCATEGORY : __int8
{
Minecraft = 0x0,
AutomationProtocol = 0x1,
MinecraftCommand = 0x2,
};

```
#### ManifestOrigin : __int8
```cpp
/* 5772 */
enum ManifestOrigin : __int8
{
Directory = 0x0,
Archive = 0x1,
Realms = 0x2,
Catalog = 0x3,
WorldHistory = 0x4,
Invalid_8 = 0x5,
};

```
#### ManifestType : __int8
```cpp
/* 5773 */
enum ManifestType : __int8
{
Pack = 0x0,
WorldTemplate_1 = 0x1,
Catalog_0 = 0x2,
};

```
#### MapDecoration::Type : __int8
```cpp
/* 75313 */
enum MapDecoration::Type : __int8
{
MarkerWhite = 0x0,
MarkerGreen = 0x1,
MarkerRed = 0x2,
MarkerBlue = 0x3,
XWhite = 0x4,
TriangleRed = 0x5,
SquareWhite = 0x6,
MarkerSign = 0x7,
MarkerPink = 0x8,
MarkerOrange = 0x9,
MarkerYellow = 0xA,
MarkerTeal = 0xB,
TriangleGreen = 0xC,
SmallSquareWhite = 0xD,
Mansion = 0xE,
Monument_0 = 0xF,
NoDraw = 0x10,
Count_13 = 0x11,
Player_3 = 0x0,
PlayerOffMap = 0x6,
PlayerOffLimits = 0xD,
PlayerHidden = 0x10,
ItemFrame_0 = 0x1,
};

```
#### MapItemTrackedActor::Type : __int32
```cpp
/* 75354 */
enum MapItemTrackedActor::Type : __int32
{
Entity_3 = 0x0,
BlockEntity_0 = 0x1,
Other_1 = 0x2,
};

```
#### MapOutputType : __int32
```cpp
/* 45353 */
enum MapOutputType : __int32
{
None_20 = 0x0,
RenameMap = 0x1,
BasicMap = 0x2,
LocatorMap = 0x3,
ExtendAndClearMap = 0x4,
CloneMap = 0x5,
LockMap = 0x6,
};

```
#### MapType : __int32
```cpp
/* 93974 */
enum MapType : __int32
{
Empty = 0x0,
Basic_0 = 0x1,
Enhanced = 0x2,
OceanExplorer = 0x3,
WoodlandExplorer = 0x4,
TreasureExplorer = 0x5,
Locked = 0x6,
};

```
#### Material::Settings : __int32
```cpp
/* 109110 */
enum Material::Settings : __int32
{
Normal_6 = 0x0,
Gas = 0x1,
Liquid = 0x2,
Decoration_0 = 0x3,
Portal_2 = 0x4,
};

```
#### MaterialType : __int32
```cpp
/* 40752 */
enum MaterialType : __int32
{
Air = 0x0,
Dirt = 0x1,
Wood_0 = 0x2,
Stone_0 = 0x3,
Metal = 0x4,
Water_0 = 0x5,
Lava_1 = 0x6,
Leaves = 0x7,
Plant = 0x8,
ReplaceablePlant = 0x9,
Sponge = 0xA,
Cloth = 0xB,
Bed = 0xC,
Fire_0 = 0xD,
Sand = 0xE,
Decoration = 0xF,
Glass_0 = 0x10,
Explosive = 0x11,
Ice_0 = 0x12,
PackedIce = 0x13,
TopSnow = 0x14,
Snow_0 = 0x15,
Cactus = 0x16,
Clay = 0x17,
Vegetable = 0x18,
Portal_1 = 0x19,
Cake = 0x1A,
Web = 0x1B,
RedstoneWire = 0x1C,
Carpet = 0x1D,
BuildableGlass = 0x1E,
Slime_1 = 0x1F,
Piston = 0x20,
Allow = 0x21,
Deny_0 = 0x22,
Netherwart = 0x23,
StoneDecoration = 0x24,
Bubble_0 = 0x25,
Egg = 0x26,
Barrier = 0x27,
DecorationFlammable = 0x28,
SurfaceTypeTotal = 0x29,
Any_1 = 0x2A,
};

```
#### MedicineType : __int8
```cpp
/* 184481 */
enum MedicineType : __int8
{
Blindness = 0x0,
Nausea = 0x1,
Poison_0 = 0x2,
Weakness = 0x3,
Invalid_25 = 0x4,
};

```
#### MinecartType : __int32
```cpp
/* 170745 */
enum MinecartType : __int32
{
Rideable = 0x0,
Chest_1 = 0x1,
Furnace_0 = 0x2,
TNT = 0x3,
Spawner_0 = 0x4,
Hopper_1 = 0x5,
CommandBlock_1 = 0x6,
};

```
#### MinecraftEventing::AccountType : __int32
```cpp
/* 45283 */
enum MinecraftEventing::AccountType : __int32
{
Xbl = 0x1,
Guest = 0x2,
Other_0 = 0x3,
};

```
#### MinecraftEventing::AchievementIds : __int32
```cpp
/* 13191 */
enum MinecraftEventing::AchievementIds : __int32
{
ChestFullOfCobblestone = 0x7,
DiamondForYou = 0xA,
IronBelly = 0x14,
IronMan = 0x15,
OnARail = 0x1D,
Overkill = 0x1E,
ReturnToSender = 0x25,
SniperDuel = 0x26,
StayinFrosty = 0x27,
TakeInventory = 0x28,
MapRoom = 0x32,
FreightStation = 0x34,
SmeltEverything = 0x35,
TasteOfYourOwnMedicine = 0x36,
WhenPigsFly = 0x38,
Inception = 0x3A,
ArtificialSelection = 0x3C,
FreeDiver = 0x3D,
SpawnTheWither = 0x3E,
Beaconator = 0x3F,
GreatView = 0x40,
SuperSonic = 0x41,
TheEndAgain = 0x42,
TreasureHunter = 0x43,
ShootingStar = 0x44,
FashionShow = 0x45,
Brilliance = 0x46,
SelfPublishedAuthor = 0x47,
AlternativeFuel = 0x48,
SleepWithTheFishes = 0x49,
Castaway = 0x4A,
ImAMarineBiologist = 0x4B,
SailThe7Seas = 0x4C,
MeGold = 0x4D,
Ahoy = 0x4E,
Atlantis = 0x4F,
OnePickleTwoPickleSeaPickleFour = 0x50,
DoaBarrelRoll = 0x51,
Moskstraumen = 0x52,
Echolocation = 0x53,
WhereHaveYouBeen = 0x54,
TopOfTheWorld = 0x55,
FruitOnTheLoom = 0x56,
SoundTheAlarm = 0x57,
BuyLowSellHigh = 0x58,
Disenchanted = 0x59,
TimeForStew = 0x5A,
BeeOurGuest = 0x5B,
TotalBeeLocation = 0x5C,
StickySituation = 0x5D,
};

```
#### MinecraftEventing::AcquisitionMethod : __int32
```cpp
/* 43312 */
enum MinecraftEventing::AcquisitionMethod : __int32
{
Unknown_9 = 0xFFFFFFFF,
None_17 = 0x0,
PickedUp_0 = 0x1,
Crafted_1 = 0x2,
TakenFromChest_0 = 0x3,
TakenFromEnderchest_0 = 0x4,
Bought_0 = 0x5,
Anvil_0 = 0x6,
Smelted_0 = 0x7,
Brewed_0 = 0x8,
Bottle = 0x9,
Trading_1 = 0xA,
Fishing_0 = 0xB,
};

```
#### MinecraftEventing::BlockPlacementMethod : __int32
```cpp
/* 44512 */
enum MinecraftEventing::BlockPlacementMethod : __int32
{
Entity_1 = 0x0,
Command_0 = 0x1,
};

```
#### MinecraftEventing::ChangeType : __int32
```cpp
/* 44524 */
enum MinecraftEventing::ChangeType : __int32
{
Unknown_10 = 0x0,
Added = 0x1,
Removed = 0x2,
Updated = 0x3,
};

```
#### MinecraftEventing::InteractionType : __int32
```cpp
/* 13190 */
enum MinecraftEventing::InteractionType : __int32
{
Breeding = 0x1,
Taming = 0x2,
Curing = 0x3,
Crafted = 0x4,
Shearing = 0x5,
Milking = 0x6,
Trading = 0x7,
Feeding = 0x8,
Igniting = 0x9,
Coloring = 0xA,
Naming = 0xB,
Leashing = 0xC,
Unleashing = 0xD,
PetSleep = 0xE,
Trusting = 0xF,
Commanding = 0x10,
};

```
#### MinecraftEventing::ItemInteractMethod : __int32
```cpp
/* 44582 */
enum MinecraftEventing::ItemInteractMethod : __int32
{
Use = 0x0,
Place_2 = 0x1,
};

```
#### MinecraftEventing::POIBlockInteractionType : __int32
```cpp
/* 13306 */
enum MinecraftEventing::POIBlockInteractionType : __int32
{
None_9 = 0x0,
Extend = 0x1,
Clone = 0x2,
Lock = 0x3,
Create = 0x4,
CreateLocator = 0x5,
Rename = 0x6,
ItemPlaced = 0x7,
ItemRemoved = 0x8,
Cooking = 0x9,
Dousing = 0xA,
Lighting = 0xB,
Haystack = 0xC,
Filled = 0xD,
Emptied = 0xE,
AddDye = 0xF,
DyeItem = 0x10,
ClearItem = 0x11,
EnchantArrow = 0x12,
CompostItemPlaced = 0x13,
RecoveredBonemeal = 0x14,
BookPlaced = 0x15,
BookOpened = 0x16,
Disenchant = 0x17,
Repair = 0x18,
DisenchantAndRepair = 0x19,
};

```
#### MinecraftEventing::PoiEventBlockType : __int32
```cpp
/* 44501 */
enum MinecraftEventing::PoiEventBlockType : __int32
{
BlastFurnace_0 = 0x0,
BrewingStand_0 = 0x1,
CartographyTable = 0x2,
Grindstone = 0x3,
Loom = 0x4,
Smoker_0 = 0x5,
Stonecutter = 0x6,
Barrel = 0x7,
Bell_1 = 0x8,
Campfire_0 = 0x9,
Cauldron_0 = 0xA,
Composter = 0xB,
Lectern_1 = 0xC,
};

```
#### MinecraftEventing::TeleportationCause : __int32
```cpp
/* 45282 */
enum MinecraftEventing::TeleportationCause : __int32
{
Unknown_14 = 0x0,
Projectile_1 = 0x1,
ChorusFruit = 0x2,
Command_2 = 0x3,
Behavior_0 = 0x4,
TeleportationCause_Count = 0x5,
};

```
#### MinecraftEventing::TravelMethod : __int32
```cpp
/* 45284 */
enum MinecraftEventing::TravelMethod : __int32
{
Unknown_15 = 0xFFFFFFFF,
Walk = 0x0,
SwimWater = 0x1,
Fall_1 = 0x2,
Climb = 0x3,
SwimLava = 0x4,
Fly_0 = 0x5,
Riding_0 = 0x6,
Sneak = 0x7,
Sprint = 0x8,
Bounce = 0x9,
FrostWalk = 0xA,
};

```
#### MinecraftEventing::UseMethod : __int32
```cpp
/* 43226 */
enum MinecraftEventing::UseMethod : __int32
{
Unknown_7 = 0xFFFFFFFF,
EquipArmor_0 = 0x0,
Eat_2 = 0x1,
Attack_1 = 0x2,
Consume_0 = 0x3,
Throw_1 = 0x4,
Shoot_1 = 0x5,
Place_1 = 0x6,
FillBottle_0 = 0x7,
FillBucket_0 = 0x8,
PourBucket_0 = 0x9,
UseTool_0 = 0xA,
};

```
#### MinecraftPacketIds : __int32
```cpp
/* 63708 */
enum MinecraftPacketIds : __int32
{
KeepAlive = 0x0,
Login = 0x1,
PlayStatus = 0x2,
ServerToClientHandshake = 0x3,
ClientToServerHandshake = 0x4,
Disconnect = 0x5,
ResourcePacksInfo = 0x6,
ResourcePackStack = 0x7,
ResourcePackClientResponse = 0x8,
Text = 0x9,
SetTime = 0xA,
StartGame = 0xB,
AddPlayer = 0xC,
AddActor = 0xD,
RemoveActor = 0xE,
AddItemActor = 0xF,
UNUSED_PLS_USE_ME = 0x10,
TakeItemActor = 0x11,
MoveAbsoluteActor = 0x12,
MovePlayer = 0x13,
RiderJump = 0x14,
UpdateBlock = 0x15,
AddPainting = 0x16,
TickSync = 0x17,
LevelSoundEventV1 = 0x18,
LevelEvent = 0x19,
TileEvent = 0x1A,
ActorEvent = 0x1B,
MobEffect = 0x1C,
UpdateAttributes = 0x1D,
InventoryTransaction = 0x1E,
PlayerEquipment = 0x1F,
MobArmorEquipment = 0x20,
Interact_0 = 0x21,
BlockPickRequest = 0x22,
ActorPickRequest = 0x23,
PlayerAction = 0x24,
ActorFall = 0x25,
HurtArmor = 0x26,
SetActorData = 0x27,
SetActorMotion = 0x28,
SetActorLink = 0x29,
SetHealth = 0x2A,
SetSpawnPosition = 0x2B,
Animate = 0x2C,
Respawn = 0x2D,
ContainerOpen = 0x2E,
ContainerClose = 0x2F,
PlayerHotbar = 0x30,
InventoryContent = 0x31,
InventorySlot = 0x32,
ContainerSetData = 0x33,
CraftingData = 0x34,
CraftingEvent = 0x35,
GuiDataPickItem = 0x36,
AdventureSettings = 0x37,
BlockActorData = 0x38,
PlayerInput = 0x39,
FullChunkData = 0x3A,
SetCommandsEnabled = 0x3B,
SetDifficulty = 0x3C,
ChangeDimension = 0x3D,
SetPlayerGameType = 0x3E,
PlayerList = 0x3F,
SimpleEvent = 0x40,
Event = 0x41,
SpawnExperienceOrb = 0x42,
MapData = 0x43,
MapInfoRequest = 0x44,
RequestChunkRadius = 0x45,
ChunkRadiusUpdated = 0x46,
ItemFrameDropItem = 0x47,
GameRulesChanged = 0x48,
Camera_1 = 0x49,
BossEvent = 0x4A,
ShowCredits = 0x4B,
AvailableCommands = 0x4C,
CommandRequest = 0x4D,
CommandBlockUpdate = 0x4E,
CommandOutput = 0x4F,
UpdateTrade = 0x50,
UpdateEquip = 0x51,
ResourcePackDataInfo = 0x52,
ResourcePackChunkData = 0x53,
ResourcePackChunkRequest = 0x54,
Transfer = 0x55,
PlaySound = 0x56,
StopSound = 0x57,
SetTitle = 0x58,
AddBehaviorTree = 0x59,
StructureBlockUpdate = 0x5A,
ShowStoreOffer = 0x5B,
PurchaseReceipt = 0x5C,
PlayerSkin = 0x5D,
SubclientLogin = 0x5E,
AutomationClientConnect = 0x5F,
SetLastHurtBy = 0x60,
BookEdit = 0x61,
NPCRequest = 0x62,
PhotoTransfer = 0x63,
ShowModalForm = 0x64,
ModalFormResponse = 0x65,
ServerSettingsRequest = 0x66,
ServerSettingsResponse = 0x67,
ShowProfile = 0x68,
SetDefaultGameType = 0x69,
RemoveObjective = 0x6A,
SetDisplayObjective = 0x6B,
SetScore = 0x6C,
LabTable = 0x6D,
UpdateBlockSynced = 0x6E,
MoveDeltaActor = 0x6F,
SetScoreboardIdentity = 0x70,
SetLocalPlayerAsInit = 0x71,
UpdateSoftEnum = 0x72,
Ping = 0x73,
BlockPalette = 0x74,
SciptCustomEvent = 0x75,
SpawnParticleEffect = 0x76,
AvailableActorIDList = 0x77,
LevelSoundEventV2 = 0x78,
NetworkChunkPublisherUpdate = 0x79,
BiomeDefinitionList = 0x7A,
LevelSoundEvent = 0x7B,
LevelEventGeneric = 0x7C,
LecternUpdate = 0x7D,
VideoStreamConnect = 0x7E,
AddEntity = 0x7F,
RemoveEntity = 0x80,
ClientCacheStatus = 0x81,
OnScreenTextureAnimation = 0x82,
MapCreateLockedCopy = 0x83,
StructureTemplateDataExportRequest = 0x84,
StructureTemplateDataExportResponse = 0x85,
UpdateBlockProperties = 0x86,
ClientCacheBlobStatusPacket = 0x87,
ClientCacheMissResponsePacket = 0x88,
EducationSettingsPacket = 0x89,
Emote = 0x8A,
MultiplayerSettingsPacket = 0x8B,
SettingsCommandPacket = 0x8C,
AnvilDamage = 0x8D,
CompletedUsingItem = 0x8E,
NetworkSettings = 0x8F,
PlayerAuthInputPacket = 0x90,
EndId = 0x91,
};

```
#### MingleComponent::MingleState : __int32
```cpp
/* 122581 */
enum MingleComponent::MingleState : __int32
{
Unavailable = 0x0,
Available = 0x1,
PartneredActive = 0x2,
PartneredPassive = 0x3,
Mingling = 0x4,
};

```
#### Mirror : __int8
```cpp
/* 5804 */
enum Mirror : __int8
{
};

```
#### Mirror_0 : __int8
```cpp
/* 35194 */
enum Mirror_0 : __int8
{
None_15 = 0x0,
X = 0x1,
Z = 0x2,
XZ = 0x3,
};

```
#### Mob::TravelType : __int32
```cpp
/* 116607 */
enum Mob::TravelType : __int32
{
Water_2 = 0x0,
Lava_4 = 0x1,
Ground = 0x2,
Air_0 = 0x3,
};

```
#### MobEffectPacket::Event : __int8
```cpp
/* 80017 */
enum MobEffectPacket::Event : __int8
{
Add_1 = 0x1,
Update = 0x2,
Remove_0 = 0x3,
};

```
#### MobEventsIndex : __int16
```cpp
/* 124039 */
enum MobEventsIndex : __int16
{
Invalid_21 = 0xFFFF,
PillagerPatrolsEvent = 0x0,
WanderingTraderEvent = 0x1,
EventCount = 0x2,
};

```
#### MobGoals : __int32
```cpp
/* 452192 */
enum MobGoals : __int32
{
GO_TO_MOB = 0x0,
GO_IN_MOB_DIRECTION = 0x1,
};

```
#### MobSpawnMethod : __int32
```cpp
/* 88768 */
enum MobSpawnMethod : __int32
{
Unknown_32 = 0x0,
SpawnEgg = 0x1,
Command_3 = 0x2,
Dispenser_0 = 0x3,
Spawner = 0x4,
SpawnMethod_Count = 0x5,
};

```
#### MonsterEggStoneType : __int32
```cpp
/* 31917 */
enum MonsterEggStoneType : __int32
{
Stone = 0x0,
Cobblestone_0 = 0x1,
StoneBrick_0 = 0x2,
MossyStoneBrick = 0x3,
CrackedStoneBrick = 0x4,
ChiseledStoneBrick = 0x5,
_count_7 = 0x6,
};

```
#### MoonPhases : __int32
```cpp
/* 254723 */
enum MoonPhases : __int32
{
FULL_MOON = 0x0,
WANING_GIBBOUS = 0x1,
FIRST_QUARTER = 0x2,
WANING_CRESCENT = 0x3,
NEW_MOON = 0x4,
WAXING_CRESCENT = 0x5,
LAST_QUARTER = 0x6,
WAXING_GIBBOUS = 0x7,
COUNT_14 = 0x8,
};

```
#### MoveInputHandler::LookDirection : __int8
```cpp
/* 475158 */
enum MoveInputHandler::LookDirection : __int8
{
Up_0 = 0x1,
Down_0 = 0x0,
Left_1 = 0x4,
Right_1 = 0x5,
Count_29 = 0x4,
};

```
#### MovementEventType : __int8
```cpp
/* 13307 */
enum MovementEventType : __int8
{
PositionCorrected = 0x0,
BackInSync = 0x1,
};

```
#### MultiplayerSettingsPacketType : __int32
```cpp
/* 77446 */
enum MultiplayerSettingsPacketType : __int32
{
EnableMultiplayer = 0x0,
DisableMultiplayer = 0x1,
RefreshJoincode = 0x2,
};

```
#### MushroomOuterType : __int32
```cpp
/* 183774 */
enum MushroomOuterType : __int32
{
AllPores = 0x0,
VerticalStem = 0xA,
AllCap = 0xE,
AllStem = 0xF,
};

```
#### NetworkHandler::Connection::Type : __int32
```cpp
/* 8336 */
enum NetworkHandler::Connection::Type : __int32
{
Remote_0 = 0x0,
Local_1 = 0x1,
};

```
#### NetworkHandler::NetworkStatisticsConfig : __int32
```cpp
/* 63569 */
enum NetworkHandler::NetworkStatisticsConfig : __int32
{
None_23 = 0x0,
Client = 0x1,
Server = 0x2,
};

```
#### NetworkIdentifier::Type : __int32
```cpp
/* 8097 */
enum NetworkIdentifier::Type : __int32
{
RakNet = 0x0,
Address = 0x1,
Address6 = 0x2,
Generic = 0x3,
};

```
#### NetworkPeer::DataStatus : __int32
```cpp
/* 8628 */
enum NetworkPeer::DataStatus : __int32
{
HasData = 0x0,
NoData = 0x1,
BrokenData = 0x2,
};

```
#### NetworkPeer::NetworkLoad : __int32
```cpp
/* 8629 */
enum NetworkPeer::NetworkLoad : __int32
{
Unrestricted = 0x0,
Low_0 = 0x1,
Medium = 0x2,
High_0 = 0x3,
};

```
#### NetworkPeer::Reliability : __int32
```cpp
/* 63696 */
enum NetworkPeer::Reliability : __int32
{
Reliable = 0x0,
ReliableOrdered = 0x1,
Unreliable = 0x2,
UnreliableSequenced = 0x3,
};

```
#### NewLeafType : __int32
```cpp
/* 183699 */
enum NewLeafType : __int32
{
Acacia_1 = 0x0,
DarkOak_1 = 0x1,
_count_34 = 0x2,
};

```
#### NewLogType : __int32
```cpp
/* 183688 */
enum NewLogType : __int32
{
Acacia_0 = 0x0,
DarkOak_0 = 0x1,
_count_33 = 0x2,
};

```
#### NodeType : __int32
```cpp
/* 57607 */
enum NodeType : __int32
{
HONEYBLOCK = 0xFFFFFFF8,
UNWALKABLE = 0xFFFFFFF9,
HOTBLOCK = 0xFFFFFFFA,
FIRE = 0xFFFFFFFB,
TRAP = 0xFFFFFFFC,
FENCE = 0xFFFFFFFD,
LAVA = 0xFFFFFFFE,
WATER = 0xFFFFFFFF,
BLOCKED = 0x0,
BREAKABLE = 0x1,
OPEN = 0x2,
WALKABLE = 0x3,
SWIMMABLE = 0x4,
BREACHABLE = 0x5,
FLYABLE = 0x6,
DOOR = 0x7,
OPEN_TYPE_COUNT = 0x9,
};

```
#### NpcActionMode : __int8
```cpp
/* 49177 */
enum NpcActionMode : __int8
{
Button = 0x0,
OnClose = 0x1,
};

```
#### NpcActionType : __int8
```cpp
/* 49178 */
enum NpcActionType : __int8
{
UrlAction = 0x0,
CommandAction = 0x1,
InvalidAction = 0x2,
};

```
#### NpcRequestPacket::RequestType : __int8
```cpp
/* 80037 */
enum NpcRequestPacket::RequestType : __int8
{
SetActions = 0x0,
ExecuteAction = 0x1,
ExecuteClosingCommands = 0x2,
SetName = 0x3,
SetSkin = 0x4,
SetInteractText = 0x5,
};

```
#### ObjectiveRenderType : __int8
```cpp
/* 80246 */
enum ObjectiveRenderType : __int8
{
};

```
#### ObjectiveRenderType_0 : __int8
```cpp
/* 80473 */
enum ObjectiveRenderType_0 : __int8
{
Integer_0 = 0x0,
Hearts = 0x1,
};

```
#### ObjectiveSortOrder : __int8
```cpp
/* 80416 */
enum ObjectiveSortOrder : __int8
{
Ascending = 0x0,
Descending = 0x1,
};

```
#### OceanTempCategory : __int32
```cpp
/* 41639 */
enum OceanTempCategory : __int32
{
COLD = 0x0,
WARM = 0x1,
};

```
#### OldLeafType : __int32
```cpp
/* 19619 */
enum OldLeafType : __int32
{
Oak_0 = 0x0,
Spruce_0 = 0x1,
Birch_0 = 0x2,
Jungle_0 = 0x3,
_count_3 = 0x4,
};

```
#### OldLogType : __int32
```cpp
/* 19613 */
enum OldLogType : __int32
{
Oak = 0x0,
Spruce = 0x1,
Birch = 0x2,
Jungle = 0x3,
_count_2 = 0x4,
};

```
#### OperationMode : __int32
```cpp
/* 87056 */
enum OperationMode : __int32
{
Handheld = 0x0,
Console_1 = 0x1,
};

```
#### OptionID : __int32
```cpp
/* 81323 */
enum OptionID : __int32
{
NAME_0 = 0x0,
DIFFICULTY = 0x1,
THIRD_PERSON = 0x2,
DPAD_SCALE = 0x3,
SERVER_VISIBLE = 0x4,
XBOX_LIVE_VISIBLE = 0x5,
NEX_VISIBLE = 0x6,
PSN_VISIBLE = 0x7,
LIMIT_WORLD_SIZE = 0x8,
LANGUAGE = 0x9,
SKIN_ID_0 = 0xA,
LAST_CUSTOM_SKIN_ID = 0xB,
RECENT_SKIN_ID_1 = 0xC,
RECENT_SKIN_ID_2 = 0xD,
RECENT_SKIN_ID_3 = 0xE,
LOGGED_INTO_XB1 = 0xF,
CHOSEN_NOT_SIGN_IN_XB1 = 0x10,
STORAGE_LOCATION = 0x11,
LEFT_HANDED = 0x12,
SPLIT_CONTROLS = 0x13,
SWAP_JUMP_AND_SNEAK = 0x14,
VIEW_DISTANCE = 0x15,
PARTICLE_VIEW_DISTANCE = 0x16,
VIEW_BOBBING = 0x17,
GRAPHICS = 0x18,
TRANSPARENTLEAVES = 0x19,
VR_TRANSPARENTLEAVES = 0x1A,
SMOOTH_LIGHTING = 0x1B,
VR_SMOOTH_LIGHTING = 0x1C,
FORCE_USE_UNSORTED_POLYS = 0x1D,
FANCY_SKIES = 0x1E,
FIXED_CAMERA = 0x1F,
HIDE_SCREENS = 0x20,
HIDE_ITEM_IN_HAND = 0x21,
FIELD_OF_VIEW = 0x22,
MSAA = 0x23,
TEXEL_AA = 0x24,
GAMMA = 0x25,
MULTITHREADED_RENDERER = 0x26,
VSYNC = 0x27,
ASYNC_TEXTURE_LOADS = 0x28,
ASYNC_TEXTURE_SHOW_MISSING_TEXTURE = 0x29,
ASYNC_TEXTURE_MAX_DEQUED_PER_FRAME = 0x2A,
ASYNC_TEXTURE_TEXTURE_LOAD_DELAY_MS = 0x2B,
FILE_WATCHER = 0x2C,
METAL_MASK = 0x2D,
FOLIAGE_LIGHT_WRAP = 0x2E,
LIGHT_WRAP_ENABLED = 0x2F,
ENVIRONMENT_LIGHT_SCALE = 0x30,
EMISSIVE_SCALE = 0x31,
METAL_COLOR_SCALE = 0x32,
LIGHT_SCALE = 0x33,
OPPOSING_LIGHT_SCALE = 0x34,
LIGHT_OFFSET = 0x35,
LENS_FLARE_ANGLE_APPEAR = 0x36,
DEPTH_OF_FIELD_NEAR_END_DEPTH = 0x37,
DEPTH_OF_FIELD_NEAR_START_BLUR_SIZE = 0x38,
DEPTH_OF_FIELD_FAR_START_DEPTH = 0x39,
DEPTH_OF_FIELD_FAR_END_DEPTH = 0x3A,
DEPTH_OF_FIELD_FAR_END_BLUR_SIZE = 0x3B,
MOTION_BLUR_ENABLE = 0x3C,
MOTION_BLUR_THRESHOLD = 0x3D,
LIGHT_COLOR = 0x3E,
BLOCK_LIGHT_COLOR = 0x3F,
BLOCK_LIGHT_SCALE = 0x40,
SKY_COLOR = 0x41,
RAYLEIGH_BETA = 0x42,
MIE_BETA = 0x43,
RAYLEIGH_HEIGHT_FALLOFF = 0x44,
RAYLEIGH_DIST_SCALE = 0x45,
AIR_SCATTER_SCALE = 0x46,
GROUND_SCATTER_COLOR = 0x47,
SKY_SCATTER_COLOR = 0x48,
SUN_SCATTER_INNER_COLOR = 0x49,
SUN_SCATTER_OUTER_COLOR = 0x4A,
GROUND_SCATTER_BETA = 0x4B,
GROUND_SCATTER_HEIGHT_FALLOFF = 0x4C,
GROUND_SCATTER_SCALE = 0x4D,
GROUND_SCATTER_DIST_SCALE = 0x4E,
SMOOTHNESS = 0x4F,
REFLECTANCE = 0x50,
RENDER_CHUNK_EDGE_BRIGHTNESS = 0x51,
RENDER_CHUNK_EDGE_TIGHTNESS = 0x52,
RENDER_CHUNK_EDGE_SHARPNESS = 0x53,
RENDER_CHUNK_EDGE_LOD_SCALAR = 0x54,
ITEM_IN_HAND_EDGE_BRIGHTNESS = 0x55,
ITEM_IN_HAND_EDGE_TIGHTNESS = 0x56,
ITEM_IN_HAND_EDGE_SHARPNESS = 0x57,
ENTITY_EDGE_BRIGHTNESS = 0x58,
ENTITY_EDGE_TIGHTNESS = 0x59,
ENTITY_EDGE_SHARPNESS = 0x5A,
ENTITY_EDGE_LOD_SCALAR = 0x5B,
PARALLAX_HEIGHT_SCALE = 0x5C,
REFL_DISTORT_MIN = 0x5D,
REFL_DISTORT_MAX = 0x5E,
WAVE_REFL_DISTORT_NEAR = 0x5F,
WAVE_REFL_DISTORT_FAR = 0x60,
WAVE_REFR_DISTORT = 0x61,
DIFFUSE_TINT = 0x62,
FOG_MIN_DEPTH = 0x63,
FOG_MAX_DEPTH = 0x64,
SPEC_COLOR_WATER = 0x65,
SHININESS = 0x66,
BLOOM_THRESHOLD = 0x67,
BLOOM_MAGNITUDE = 0x68,
BLOOM_BLUR_SIZE = 0x69,
ADAPTATION_RATE = 0x6A,
TONEMAP_TECHNIQUE = 0x6B,
EXPOSURE = 0x6C,
AUTO_EXPOSURE = 0x6D,
AUTO_EXPOSURE_KEY_VALUE = 0x6E,
SHOULDER_STRENGTH = 0x6F,
LINEAR_STRENGTH = 0x70,
LINEAR_ANGLE = 0x71,
TOE_STRENGTH = 0x72,
TOE_NUMERATOR = 0x73,
TOE_DENOMINATOR = 0x74,
HABLE_WHITE_LEVEL = 0x75,
EXPONENTIAL_WHITE_LEVEL = 0x76,
LOGARITHMIC_WHITE_LEVEL = 0x77,
REINHARD_MODIFIED_WHITE_LEVEL = 0x78,
DRAGO_WHITE_LEVEL = 0x79,
LUMINANCE_SATURATION = 0x7A,
LUM_MAP_MIP_LEVEL = 0x7B,
BIAS = 0x7C,
SHADOW_COVERAGE_DISTANCE_SCALE = 0x7D,
SHADOW_HIGH_DETAIL_DISTANCE_SCALE = 0x7E,
SHADOW_INTENSITY = 0x7F,
CLOUD_INTERIOR_FOG_DEPTH_START = 0x80,
CLOUD_INTERIOR_FOG_DEPTH_END = 0x81,
CLOUD_INTERIOR_FOG_MAX = 0x82,
CLOUD_INTERIOR_FOG_OUTER_SHELL_OPACITY_FACTOR = 0x83,
CLOUD_INTERIOR_FOG_OPACITY_FACTOR = 0x84,
CLOUD_INTERIOR_FOG_COLOR_DEBUG = 0x85,
CLOUD_INTERIOR_FOG_NEARBY_TRANSITION_THRESHOLD = 0x86,
CLOUD_FRESNEL_DISTANCE_START = 0x87,
CLOUD_FRESNEL_DISTANCE_END = 0x88,
CLOUD_LIGHT_FALLOFF_START = 0x89,
CLOUD_LIGHT_FALLOFF_END = 0x8A,
CLOUD_LIGHT_SPOT_POWER = 0x8B,
CLOUD_RENDER_NORMALS = 0x8C,
CLOUDS0_ENABLED = 0x8D,
CLOUDS0_COLOR = 0x8E,
CLOUDS0_OPACITY = 0x8F,
CLOUDS0_EMISSIVE_STRENGTH = 0x90,
CLOUDS0_LIGHT_WRAP_STRENGTH = 0x91,
CLOUDS0_TRANSMISSION_STRENGTH = 0x92,
CLOUDS0_EDGE_HIGHLIGHT_COLOR = 0x93,
CLOUDS0_EDGE_HIGHLIGHT_TIGHTNESS = 0x94,
CLOUDS0_NORMAL_BEND_TIGHTNESS = 0x95,
CLOUDS0_ALTITUDE = 0x96,
CLOUDS0_THICKNESS = 0x97,
CLOUDS0_BOUNDS = 0x98,
CLOUDS0_DRIFT_VELOCITY = 0x99,
CLOUDS0_ANIMATION_SPEED = 0x9A,
CLOUDS0_ANIMATION_PAUSE = 0x9B,
CLOUDS1_ENABLED = 0x9C,
CLOUDS1_COLOR = 0x9D,
CLOUDS1_OPACITY = 0x9E,
CLOUDS1_EMISSIVE_STRENGTH = 0x9F,
CLOUDS1_LIGHT_WRAP_STRENGTH = 0xA0,
CLOUDS1_TRANSMISSION_STRENGTH = 0xA1,
CLOUDS1_EDGE_HIGHLIGHT_COLOR = 0xA2,
CLOUDS1_EDGE_HIGHLIGHT_TIGHTNESS = 0xA3,
CLOUDS1_NORMAL_BEND_TIGHTNESS = 0xA4,
CLOUDS1_ALTITUDE = 0xA5,
CLOUDS1_THICKNESS = 0xA6,
CLOUDS1_BOUNDS = 0xA7,
CLOUDS1_DRIFT_VELOCITY = 0xA8,
CLOUDS1_ANIMATION_SPEED = 0xA9,
CLOUDS1_ANIMATION_PAUSE = 0xAA,
CLOUDS2_ENABLED = 0xAB,
CLOUDS2_COLOR = 0xAC,
CLOUDS2_OPACITY = 0xAD,
CLOUDS2_EMISSIVE_STRENGTH = 0xAE,
CLOUDS2_LIGHT_WRAP_STRENGTH = 0xAF,
CLOUDS2_TRANSMISSION_STRENGTH = 0xB0,
CLOUDS2_EDGE_HIGHLIGHT_COLOR = 0xB1,
CLOUDS2_EDGE_HIGHLIGHT_TIGHTNESS = 0xB2,
CLOUDS2_NORMAL_BEND_TIGHTNESS = 0xB3,
CLOUDS2_ALTITUDE = 0xB4,
CLOUDS2_THICKNESS = 0xB5,
CLOUDS2_BOUNDS = 0xB6,
CLOUDS2_DRIFT_VELOCITY = 0xB7,
CLOUDS2_ANIMATION_SPEED = 0xB8,
CLOUDS2_ANIMATION_PAUSE = 0xB9,
CLOUDS3_ENABLED = 0xBA,
CLOUDS3_COLOR = 0xBB,
CLOUDS3_OPACITY = 0xBC,
CLOUDS3_EMISSIVE_STRENGTH = 0xBD,
CLOUDS3_LIGHT_WRAP_STRENGTH = 0xBE,
CLOUDS3_TRANSMISSION_STRENGTH = 0xBF,
CLOUDS3_EDGE_HIGHLIGHT_COLOR = 0xC0,
CLOUDS3_EDGE_HIGHLIGHT_TIGHTNESS = 0xC1,
CLOUDS3_NORMAL_BEND_TIGHTNESS = 0xC2,
CLOUDS3_ALTITUDE = 0xC3,
CLOUDS3_THICKNESS = 0xC4,
CLOUDS3_BOUNDS = 0xC5,
CLOUDS3_DRIFT_VELOCITY = 0xC6,
CLOUDS3_ANIMATION_SPEED = 0xC7,
CLOUDS3_ANIMATION_PAUSE = 0xC8,
CLOUDS4_ENABLED = 0xC9,
CLOUDS4_COLOR = 0xCA,
CLOUDS4_OPACITY = 0xCB,
CLOUDS4_EMISSIVE_STRENGTH = 0xCC,
CLOUDS4_LIGHT_WRAP_STRENGTH = 0xCD,
CLOUDS4_TRANSMISSION_STRENGTH = 0xCE,
CLOUDS4_EDGE_HIGHLIGHT_COLOR = 0xCF,
CLOUDS4_EDGE_HIGHLIGHT_TIGHTNESS = 0xD0,
CLOUDS4_NORMAL_BEND_TIGHTNESS = 0xD1,
CLOUDS4_ALTITUDE = 0xD2,
CLOUDS4_THICKNESS = 0xD3,
CLOUDS4_BOUNDS = 0xD4,
CLOUDS4_DRIFT_VELOCITY = 0xD5,
CLOUDS4_ANIMATION_SPEED = 0xD6,
CLOUDS4_ANIMATION_PAUSE = 0xD7,
RAYS_ENABLE_DEBUG_TEXTURES = 0xD8,
RAYS_NUMBER_OF_SLICES = 0xD9,
RAYS_NUMBER_OF_SAMPLES_PER_SLICE = 0xDA,
RAYS_EPIPOLAR_STEP_WIDTH = 0xDB,
RAYS_DEPTH_BREAK_THRESHOLD = 0xDC,
RAYS_FIX_UP_TRESHOLD = 0xDD,
RAYS_RAY_CASTING_DISTANCE = 0xDE,
RAYS_RAY_CASTING_STEP_WIDTH = 0xDF,
WIND_ANGLE = 0xE0,
WIND_SPEED = 0xE1,
WIND_OCTAVE_1_AMPLITUDE = 0xE2,
WIND_OCTAVE_1_FREQUENCY = 0xE3,
WIND_OCTAVE_2_AMPLITUDE = 0xE4,
WIND_OCTAVE_2_FREQUENCY = 0xE5,
WIND_OCTAVE_3_AMPLITUDE = 0xE6,
WIND_OCTAVE_3_FREQUENCY = 0xE7,
GRASS_FLEXIBILITY = 0xE8,
TALL_GRASS_FLEXIBILITY = 0xE9,
CROPS_FLEXIBILITY = 0xEA,
LEAVES_FLEXIBILITY = 0xEB,
FLOWERS_FLEXIBILITY = 0xEC,
MAX_FRAMERATE = 0xED,
FULLSCREEN = 0xEE,
SHOW_ADVANCED_VIDEO_SETTINGS = 0xEF,
SHOW_TONEMAP_SETTINGS = 0xF0,
GUI_SCALE = 0xF1,
SPLIT_SCREEN_GUI_SCALE = 0xF2,
SAFE_ZONE_X = 0xF3,
SAFE_ZONE_Y = 0xF4,
SCREEN_POSITION_X = 0xF5,
SCREEN_POSITION_Y = 0xF6,
UI_PROFILE = 0xF7,
SOUND = 0xF8,
MUSIC = 0xF9,
VR_SENSITIVITY = 0xFA,
VR_GAMMA = 0xFB,
RESET_PLAYER_ALIGNMENT = 0xFC,
VR_PARTICLE_VIEW_DISTANCE = 0xFD,
STUTTER_TURN = 0xFE,
STUTTER_TURN_SOUND = 0xFF,
HMD_POSITION_DISPLACEMENT = 0x100,
VR_VIEW_DISTANCE = 0x101,
VR_AUTO_JUMP = 0x102,
VR_HEAD_STEERING = 0x103,
STUTTER_CONSTANT_TIME_MODE = 0x104,
STEREO_RENDERING = 0x105,
VR_HUD_AT_TOP = 0x106,
VR_USES_NORMAL_HIT_FX = 0x107,
VR_USES_RED_FLASH_FOR_HIT = 0x108,
VR_RIGHTSTICK_PITCHASSIST = 0x109,
VR_RIGHTSTICK_DEADBAND = 0x10A,
VR_RIGHTSTICK_GAZEADJUST = 0x10B,
VR_GAZE_PITCH_BOOST = 0x10C,
VR_HUD_DRIFTS = 0x10D,
VR_LIVING_ROOM_CURSOR_CENTERED = 0x10E,
VR_LINEAR_JUMP = 0x10F,
VR_LINEAR_MOTION = 0x110,
VR_STICKY_MINING = 0x111,
VR_STICKY_MINING_HAND_POINTER = 0x112,
VR_TAP_TURN = 0x113,
VR_TAP_TURN_SENSITIVITY = 0x114,
VR_ROLL_TURN_SENSITIVITY = 0x115,
VR_ROLL_TURNING = 0x116,
VR_180_TURNING = 0x117,
VR_OPTIONS_COMFORT_CONTROLS = 0x118,
VR_SHOW_OPTIONS_SELECT_SCREEN = 0x119,
VR_LVR_HINT_TIME = 0x11A,
VR_MIRROR_TEXTURE = 0x11B,
VR_HAND_CONTROLS_ITEM = 0x11C,
VR_HAND_CONTROLS_HUD = 0x11D,
VR_HAND_POINTER = 0x11E,
VR_HANDS_VISIBLE = 0x11F,
VR_UI_MOUSE_SENSITIVITY = 0x120,
VR_MSAA = 0x121,
VR_LIVING_ROOM_MODE = 0x122,
VR_JOYSTICKAIM = 0x123,
VR_JOYSTICKAIM_SENSITIVITY = 0x124,
VR_RIGHTSTICK_PITCH_MAXANGLE = 0x125,
VR_RIGHTSTICK_PITCHASSIST_STEPPINGS = 0x126,
STORE_HAS_PURCHASED_COINS = 0x127,
SWITCH_DEBUG_COINS = 0x128,
SHOW_CHUNK_MAP = 0x129,
SHOW_SERVER_CHUNK_MAP = 0x12A,
DEBUG_DISABLE_RENDER_TERRAIN = 0x12B,
DEBUG_DISABLE_RENDER_ENTITIES = 0x12C,
DEBUG_DISABLE_RENDER_BLOCKENTITIES = 0x12D,
DEBUG_DISABLE_RENDER_PARTICLES = 0x12E,
DEBUG_DISABLE_RENDER_SKY = 0x12F,
DEBUG_DISABLE_RENDER_WEATHER = 0x130,
DEBUG_DISABLE_RENDER_HUD = 0x131,
DEBUG_DISABLE_RENDER_ITEM_IN_HAND = 0x132,
ENABLE_PROFILER_OUTPUT = 0x133,
SILENT_ADD_USER = 0x134,
BENCHMARK_MODE_TIME = 0x135,
DISABLE_CLIENT_BLOB_CACHE = 0x136,
FORCE_CLIENT_BLOB_CACHE = 0x137,
CONNECTION_QUALITY = 0x138,
SHOW_LATENCY_GRAPH = 0x139,
RENDER_BOUNDING_BOXES = 0x13A,
RENDER_PATHS = 0x13B,
RENDER_GOAL_STATE = 0x13C,
RENDER_COORDINATE_SYSTEM = 0x13D,
NEW_PARTICLE_SYSTEM = 0x13E,
DISABLE_RAIN = 0x13F,
AUTO_LOAD_LEVEL = 0x140,
ACHIEVEMENTS_ALWAYS_ENABLED = 0x141,
REALM_CREATE_WITHOUT_PURCHASE = 0x142,
USE_IPV6_ONLY = 0x143,
USE_RETAIL_XBOX_SANDBOX = 0x144,
USE_OVERRIDE_DATE = 0x145,
DISPLAY_OVERRIDE_DATETIME = 0x146,
LOAD_OVERRIDE_DATE = 0x147,
OVERRIDE_DATE = 0x148,
OVERRIDE_TIME_SCALE = 0x149,
OVERRIDE_DATE_TYPE = 0x14A,
DISPLAY_MARKETPLACE_DOCUMENT_ID = 0x14B,
MARKETPLACE_DOCUMENT_ID = 0x14C,
REALMS_ENVIRONMENT = 0x14D,
REALMS_ENDPOINT = 0x14E,
REALMS_ENDPOINT_PAYMENT = 0x14F,
REALMS_RELYING_PARTY = 0x150,
REALMS_RELYING_PARTY_PAYMENT = 0x151,
STORE_OFFER_QUERY_REQUIRES_XBL = 0x152,
RESET_CLIENT_ID = 0x153,
LOG_FLUSH_IMMEDIATE = 0x154,
LOG_TIMESTAMP = 0x155,
LOG_TRACE = 0x156,
LOG_APPEND = 0x157,
LOG_AREA = 0x158,
LOG_PRIORITY = 0x159,
LOG_THREAD = 0x15A,
LOG_PROCESS_ID = 0x15B,
LOG_MESSAGE_ID = 0x15C,
LOG_SILENT = 0x15D,
LOG_PRIORITY_FILTER = 0x15E,
LOG_AREA_FILTER_STRING = 0x15F,
LOG_CATEGORY_WORLD_GEN = 0x160,
LOG_CATEGORY_LOOT = 0x161,
LOG_CATEGORY_RENDER = 0x162,
LOG_CATEGORY_STRUCTURE = 0x163,
LOG_CATEGORY_UI = 0x164,
LOG_CATEGORY_ONLINE = 0x165,
DEBUG_HUD = 0x166,
SHOW_BUILD_INFO = 0x167,
LAST_GAME_VERSION_MAJOR = 0x168,
LAST_GAME_VERSION_MINOR = 0x169,
LAST_GAME_VERSION_PATCH = 0x16A,
LAST_GAME_VERSION_REVISION = 0x16B,
LAST_GAME_VERSION_BETA = 0x16C,
USE_OVERRIDE_PATCHNOTES_CLIENT_VERSION = 0x16D,
REALMS_SHOW_FRIEND_INVITES_ONLY = 0x16E,
REALMS_NUMBER_OF_OWNED_REALMS = 0x16F,
REALMS_NUMBER_OF_FRIENDS_REALMS = 0x170,
REALMS_VIEW_UPSELL_SCREEN_COUNT = 0x171,
SHOWN_RATINGS_PROMPT = 0x172,
SAVE_AND_QUIT_COUNT = 0x173,
REALMS_SHOW_REALMS_TRIAL_ON_PLAY_SCREEN = 0x174,
ALLOW_CELLULAR_DATA = 0x175,
AUTO_UPDATE_MODE = 0x176,
AUTO_UPDATE_ENABLED = 0x177,
WEBSOCKET_ENCRYPTION = 0x178,
TEXT_TO_SPEECH_DISCOVERED = 0x179,
TEXT_TO_SPEECH_AUTO_ENABLE = 0x17A,
CHAT_TEXT_TO_SPEECH = 0x17B,
UI_TEXT_TO_SPEECH = 0x17C,
OPEN_CHAT_MESSAGE = 0x17D,
SENSITIVITY = 0x17E,
SMOOTH_ROTATION_SPEED = 0x17F,
INVERT_MOUSE = 0x180,
AUTO_JUMP = 0x181,
FULL_KEYBOARD_GAMEPLAY = 0x182,
DESTROY_VIBRATION = 0x183,
RENDER_CLOUDS = 0x184,
TOGGLE_CROUCH = 0x185,
GAME_SENSITIVITY = 0x186,
VR_GAME_SENSITIVITY = 0x187,
MULTIPLAYER_GAME = 0x188,
CROSSPLATFORM_GAME = 0x189,
LAST_XUID = 0x18A,
HIDE_PAPERDOLL = 0x18B,
ASSERTIONS_DEBUG_BREAK = 0x18C,
ASSERTIONS_SHOW_DIALOG = 0x18D,
SHOW_DEV_CONSOLE_BUTTON = 0x18E,
DISPLAY_TREATMENTS_PANEL = 0x18F,
HIDE_KEYBOARD_TOOLTIPS = 0x190,
HIDE_KEYBOARD_TOOLTIPS_OVERRIDDEN = 0x191,
HIDE_TOOLTIPS = 0x192,
CLASSIC_BOX_SELECTION = 0x193,
VR_CLASSIC_BOX_SELECTION = 0x194,
DEBUG_ATTACH_POS = 0x195,
DEBUG_SHOW_MINECRAFT_TCUI_REPLACEMENT = 0x196,
SPLIT_SCREEN = 0x197,
HIDE_HUD = 0x198,
HIDE_HAND = 0x199,
VR_HIDE_HUD = 0x19A,
VR_HIDE_HAND = 0x19B,
INGAME_PLAYER_NAMES = 0x19C,
SPLITSCREEN_INGAME_PLAYER_NAMES = 0x19D,
INTERFACE_OPACITY = 0x19E,
SPLITSCREEN_INTERFACE_OPACITY = 0x19F,
ACK_AUTO_SAVE = 0x1A0,
REALMSPLUS_UPGRADENOTICE_STATE = 0x1A1,
SHOW_AUTO_SAVE_ICON = 0x1A2,
HAS_SET_SAFE_ZONE = 0x1A3,
FIND_MOBS = 0x1A4,
FIELD_OF_VIEW_TOGGLE = 0x1A5,
HIDE_GAMEPAD_CURSOR = 0x1A6,
ENABLE_MIXER_INTERACTIVE = 0x1A7,
AUTOMATION_UPLOAD_TOKEN = 0x1A8,
AUTOMATION_UPLOAD_LOGS = 0x1A9,
AUTOMATION_LOG_FLUSH_DELAY = 0x1AA,
AUTOMATION_FILE_UPLOAD_ENDPOINT = 0x1AB,
AUTOMATION_APPEND_DEBUGLOG_TIMESTAMP = 0x1AC,
AUTOMATION_UNIT_TEST_TAGS = 0x1AD,
AUTOMATION_FUNCTIONAL_TEST_TAGS = 0x1AE,
AUTOMATION_UNIT_BLACKLIST_TEST_TAGS = 0x1AF,
AUTOMATION_FUNCTIONAL_BLACKLIST_TEST_TAGS = 0x1B0,
AUTOMATION_TESTRUN_TIMED_OUT = 0x1B1,
AUTOMATION_TESTRUN_ID = 0x1B2,
AUTOMATION_REPEAT_COUNT = 0x1B3,
AUTOMATION_REPEAT_FAILURES_ONLY = 0x1B4,
AUTOMATION_PER_TESTCASE_TIMEOUT = 0x1B5,
AUTOMATION_QUIT_APP = 0x1B6,
LIGHTING_ADJUSTMENT_VALUE = 0x1B7,
HAS_SET_LIGHTING_ADJUSTMENT_VALUE = 0x1B8,
DEBUG_DISABLE_CONNECTED_STORAGE_PULL = 0x1B9,
DEBUG_DISABLE_CONNECTED_STORAGE_PUSH = 0x1BA,
HOTBAR_ONLY_TOUCH = 0x1BB,
TEST_ASSETS_AZURE_SAS = 0x1BC,
TEST_ASSETS_AZURE_URL = 0x1BD,
TEST_ASSETS_LOCAL_PATH = 0x1BE,
GAMEPAD_CURSOR_SENSITIVITY = 0x1BF,
SHOWN_PATCH_NOTICE = 0x1C0,
LAST_SHOWN_REALMS_ENDED_DATE = 0x1C1,
IGNORE_USER_INPUT = 0x1C2,
SHOWN_PLATFORM_NETWORK_CONNECT_CONFIRMATION = 0x1C3,
SCREEN_ANIMATIONS = 0x1C4,
GAMEPAD_SWAP_AB_BUTTONS = 0x1C5,
GAMEPAD_SWAP_XY_BUTTONS = 0x1C6,
FANCY_BUBBLES = 0x1C7,
SHOWN_PLATFORM_PREMIUM_UPSELL = 0x1C8,
TEST_TAGS_SERVICE_URL = 0x1C9,
EDU_FIRST_LOGIN = 0x1CA,
TEST_BRANCH_NAME = 0x1CB,
FUNCTIONAL_TEST_BLOCK_INPUT = 0x1CC,
FUNCTIONAL_TEST_BLOCKING_INPUT = 0x1CD,
AUTOMATION_MARKETPLACE_BOOT_TEST_BATCH = 0x1CE,
AUTOMATION_MARKETPLACE_BOOT_TEST_RUN_BATCH_COUNT = 0x1CF,
DEV_CONSOLE_PREVIOUS_MESSAGES = 0x1D0,
CODE_SCREEN_VIEW = 0x1D1,
CODE_SCREEN_FIRST_TIME = 0x1D2,
CODE_SCREEN_IDE = 0x1D3,
CHAT_COLOR_CODE = 0x1D4,
CHAT_FONT_SIZE = 0x1D5,
CHAT_LINE_SPACING = 0x1D6,
CHAT_MENTIONS_COLOR_CODE = 0x1D7,
CHAT_TYPEFACE = 0x1D8,
LIBRARY_WELCOME = 0x1D9,
CONTENT_LOG_FILE = 0x1DA,
CONTENT_LOG_GUI = 0x1DB,
PERF_TURTLE = 0x1DC,
GAMEPLAY_TIPS_ENABLED = 0x1DD,
GAMEPLAY_TIPS_SHOULD_BE_SHOWN = 0x1DE,
IAP_OWNING_ACCOUNT = 0x1DF,
LAST_PLAYFAB_ID = 0x1E0,
CONTROL_TIPS_SHOULD_BE_SHOWN = 0x1E1,
PLAYFAB_ENVIRONMENT = 0x1E2,
AD_STAY_SIGNED_IN = 0x1E3,
AD_USE_SINGLE_SIGN_ON = 0x1E4,
AD_SHOW_DEBUG_PANEL = 0x1E5,
AD_TOKEN_REFRESH_THRESHOLD = 0x1E6,
AD_DEV_CONFIG = 0x1E7,
RENDER_SCHEDULER_INFO = 0x1E8,
WINDOWS_STORE_MODE = 0x1E9,
INVENTORY_TIPS_SHOULD_BE_SHOWN = 0x1EA,
TREE_TIPS_SHOULD_BE_SHOWN = 0x1EB,
OPEN_INVENTORY_TIPS_SHOULD_BE_SHOWN = 0x1EC,
USE_DEFAULT_FONT_OVERRIDES = 0x1ED,
DAY_ONE_EXPERIENCE_COMPLETED = 0x1EE,
SELECT_CRAFTTABLE_TIPS_SHOULD_BE_SHOWN = 0x1EF,
PLACE_CRAFTTABLE_TIPS_SHOULD_BE_SHOWN = 0x1F0,
USE_CRAFTTABLE_TIPS_SHOULD_BE_SHOWN = 0x1F1,
MAKE_CRAFTTABLE_TIPS_SHOULD_BE_SHOWN = 0x1F2,
NEED_MORE_MATERIALS_TIPS_SHOULD_BE_SHOWN = 0x1F3,
IS_LEGACY_PLAYER = 0x1F4,
PLAYFAB_COMMERCE = 0x1F5,
DO_NOT_SHOW_MULTIPLAYER_ONLINE_SAFETY_WARNING = 0x1F6,
ONLY_TRUSTED_SKINS_ALLOWED = 0x1F7,
COUNT_5 = 0x1F8,
};

```
#### OptionOwnerType : __int32
```cpp
/* 81326 */
enum OptionOwnerType : __int32
{
User_0 = 0x0,
Machine = 0x1,
};

```
#### OptionResetFlags : __int32
```cpp
/* 81329 */
enum OptionResetFlags : __int32
{
None_30 = 0x1,
KeyboardMouse = 0x2,
Controller = 0x4,
Touch_0 = 0x8,
Video = 0x10,
Audio = 0x20,
Chat_0 = 0x40,
Accessibility = 0x80,
Controls = 0xE,
};

```
#### OptionType : __int32
```cpp
/* 81341 */
enum OptionType : __int32
{
Boolean_0 = 0x0,
InputModeBoolean = 0x1,
Float_5 = 0x2,
InputModeFloat = 0x3,
String_3 = 0x4,
Int_4 = 0x5,
Enum_0 = 0x6,
Vec3_0 = 0x7,
};

```
#### OsVersion : __int32
```cpp
/* 480115 */
enum OsVersion : __int32
{
Unspecified_0 = 0x0,
Windows10 = 0x1,
Windows8_1 = 0x2,
Windows7 = 0x3,
};

```
#### OwnerStorageEntity::EmptyInit : __int32
```cpp
/* 13178 */
enum OwnerStorageEntity::EmptyInit : __int32
{
NoValue_0 = 0x0,
};

```
#### OwnerStorageEntity::VariadicInit : __int32
```cpp
/* 13179 */
enum OwnerStorageEntity::VariadicInit : __int32
{
NonAmbiguous_0 = 0x0,
};

```
#### OwnerStorageFeature::EmptyInit : __int32
```cpp
/* 31074 */
enum OwnerStorageFeature::EmptyInit : __int32
{
NoValue_1 = 0x0,
};

```
#### OwnerStorageFeature::VariadicInit : __int32
```cpp
/* 31075 */
enum OwnerStorageFeature::VariadicInit : __int32
{
NonAmbiguous_1 = 0x0,
};

```
#### OwnerStorageSharePtr<EntityRegistryOwned>::EmptyInit : __int32
```cpp
/* 13168 */
enum OwnerStorageSharePtr<EntityRegistryOwned>::EmptyInit : __int32
{
};

```
#### OwnerStorageSharePtr<EntityRegistryOwned>::VariadicInit : __int32
```cpp
/* 104380 */
enum OwnerStorageSharePtr<EntityRegistryOwned>::VariadicInit : __int32
{
NonAmbiguous_3 = 0x0,
};

```
#### OwnerStorageSharePtr<PerlinSimplexNoise>::EmptyInit : __int32
```cpp
/* 191526 */
enum OwnerStorageSharePtr<PerlinSimplexNoise>::EmptyInit : __int32
{
};

```
#### OwnerStorageSharePtr<PerlinSimplexNoise>::VariadicInit : __int32
```cpp
/* 191527 */
enum OwnerStorageSharePtr<PerlinSimplexNoise>::VariadicInit : __int32
{
NonAmbiguous_4 = 0x0,
};

```
#### POIType : __int32
```cpp
/* 53670 */
enum POIType : __int32
{
InvalidPOI = 0xFFFFFFFF,
Bed_1 = 0x0,
MeetingArea = 0x1,
Jobsite = 0x2,
Count_9 = 0x3,
};

```
#### PackAccessAssetGenerationResult : __int32
```cpp
/* 422544 */
enum PackAccessAssetGenerationResult : __int32
{
ReadContentsFile = 0x0,
IteratedThroughDirectory = 0x1,
Failed_7 = 0x2,
AlreadyGenerated = 0x3,
};

```
#### PackAccessStrategyType : __int32
```cpp
/* 83334 */
enum PackAccessStrategyType : __int32
{
Directory_0 = 0x0,
Zip = 0x1,
DirectoryAndZip = 0x2,
Invalid_17 = 0x3,
};

```
#### PackCategory : __int32
```cpp
/* 5659 */
enum PackCategory : __int32
{
_Unknown_0 = 0x0,
_RealmsUnknown_0 = 0x1,
Standard = 0x2,
Premium = 0x3,
Custom_0 = 0x4,
Subpack = 0x5,
};

```
#### PackErrorType : __int32
```cpp
/* 5657 */
enum PackErrorType : __int32
{
None_6 = 0x0,
IncompletePackError = 0x1,
PackParseError = 0x2,
PackLoadError = 0x3,
UIError = 0x4,
PackSettingsError = 0x5,
};

```
#### PackIconType : __int32
```cpp
/* 5660 */
enum PackIconType : __int32
{
Default_0 = 0x0,
Bugged = 0x1,
};

```
#### PackManifest::PackRedownloadableState : __int32
```cpp
/* 5776 */
enum PackManifest::PackRedownloadableState : __int32
{
Redownloadable = 0x0,
NotRedownloadable = 0x1,
Unknown_2 = 0x2,
};

```
#### PackManifestFormat : __int8
```cpp
/* 5777 */
enum PackManifestFormat : __int8
{
V0 = 0x0,
V1 = 0x1,
V2 = 0x2,
};

```
#### PackOrigin : __int32
```cpp
/* 5658 */
enum PackOrigin : __int32
{
_Unknown = 0x0,
_RealmsUnknown = 0x1,
Package = 0x2,
Treatment = 0x3,
Dev = 0x4,
World = 0x5,
User = 0x6,
TempCache = 0x7,
PremiumCache = 0x8,
PremiumTempCache = 0x9,
};

```
#### PackParseErrorType : __int32
```cpp
/* 83185 */
enum PackParseErrorType : __int32
{
None_31 = 0x0,
NoPackAccess = 0x1,
UnsupportedFileFormat = 0x2,
IncompletePack = 0x3,
NoManifest = 0x4,
ParseError = 0x5,
MissingProperty = 0x6,
MissingPropertyUpgraded = 0x7,
WrongTypeProperty = 0x8,
EmptyProperty = 0x9,
EmptyPropertyUpgraded = 0xA,
InvalidProperty = 0xB,
MalformedPropertyUUID = 0xC,
MalformedPropertyUUIDUpgraded = 0xD,
MalformedPropertyVERSION = 0xE,
MalformedPropertyVERSIONUpgraded = 0xF,
DuplicateUUIDUpgraded = 0x10,
DuplicateUUID = 0x11,
InvalidPackTypeUpgraded = 0x12,
MissingModules = 0x13,
MissingDependency = 0x14,
MultipleModules = 0x15,
MultipleModulesUpgraded = 0x16,
UnsupportedFormatVersion = 0x17,
PackUpgraded = 0x18,
InvalidCapability = 0x19,
UnsupportedBaseGameVersionPatch = 0x1A,
IgnoredProperty = 0x1B,
VersionTooHigh = 0x1C,
VersionTooLow = 0x1D,
MinEngineVersionCapFormatVersion1 = 0x1E,
Count_17 = 0x1F,
};

```
#### PackScope : __int8
```cpp
/* 5775 */
enum PackScope : __int8
{
Global = 0x1,
AddOn = 0x2,
Level = 0x4,
World_0 = 0x6,
Any_0 = 0x7,
Default_1 = 0x7,
};

```
#### PackType : __int8
```cpp
/* 2176 */
enum PackType : __int8
{
Invalid_0 = 0x0,
Addon = 0x1,
Cached = 0x2,
CopyProtected = 0x3,
Behavior = 0x4,
PersonaPiece = 0x5,
Resources = 0x6,
Skins = 0x7,
WorldTemplate = 0x8,
Count = 0x9,
};

```
#### PacketPriority : __int32
```cpp
/* 64314 */
enum PacketPriority : __int32
{
IMMEDIATE_PRIORITY = 0x0,
HIGH_PRIORITY = 0x1,
MEDIUM_PRIORITY = 0x2,
LOW_PRIORITY = 0x3,
NUMBER_OF_PRIORITIES = 0x4,
};

```
#### PacketReadResult : __int32
```cpp
/* 72420 */
enum PacketReadResult : __int32
{
Valid_0 = 0x0,
Malformed = 0x1,
Fixed = 0x2,
};

```
#### PacketReliability : __int32
```cpp
/* 73241 */
enum PacketReliability : __int32
{
UNRELIABLE = 0x0,
UNRELIABLE_SEQUENCED = 0x1,
RELIABLE = 0x2,
RELIABLE_ORDERED = 0x3,
RELIABLE_SEQUENCED = 0x4,
UNRELIABLE_WITH_ACK_RECEIPT = 0x5,
RELIABLE_WITH_ACK_RECEIPT = 0x6,
RELIABLE_ORDERED_WITH_ACK_RECEIPT = 0x7,
NUMBER_OF_RELIABILITIES = 0x8,
};

```
#### PageContent::PageType : __int8
```cpp
/* 77463 */
enum PageContent::PageType : __int8
{
Text_0 = 0x0,
Photo = 0x1,
Count_15 = 0x2,
};

```
#### PaletteColor : __int8
```cpp
/* 79623 */
enum PaletteColor : __int8
{
White_0 = 0x0,
Orange_0 = 0x1,
Magenta_0 = 0x2,
LightBlue = 0x3,
Yellow_0 = 0x4,
LightGreen = 0x5,
Pink_0 = 0x6,
Gray_0 = 0x7,
Silver_0 = 0x8,
Cyan_0 = 0x9,
Purple_0 = 0xA,
Blue_0 = 0xB,
Brown_0 = 0xC,
Green_0 = 0xD,
Red_0 = 0xE,
Black_0 = 0xF,
Count_16 = 0x10,
};

```
#### PandaVariant : __int32
```cpp
/* 124192 */
enum PandaVariant : __int32
{
DEFAULT_0 = 0x0,
LAZY = 0x1,
WORRIED = 0x2,
PLAYFUL = 0x3,
BROWN = 0x4,
WEAK = 0x5,
AGGRESSIVE = 0x6,
COUNT_7 = 0x7,
};

```
#### ParticleType : __int32
```cpp
/* 34992 */
enum ParticleType : __int32
{
Undefined_3 = 0x0,
Bubble = 0x1,
BubbleManual = 0x2,
Crit = 0x3,
BlockForceField = 0x4,
Smoke = 0x5,
Explode = 0x6,
Evaporation = 0x7,
Flame = 0x8,
Lava = 0x9,
LargeSmoke = 0xA,
RedDust = 0xB,
RisingBorderDust = 0xC,
IconCrack = 0xD,
SnowballPoof = 0xE,
LargeExplode = 0xF,
HugeExplosion = 0x10,
MobFlame = 0x11,
Heart = 0x12,
Terrain = 0x13,
TownAura = 0x14,
Portal = 0x15,
MobPortal = 0x16,
WaterSplash = 0x17,
WaterSplashManual = 0x18,
WaterWake = 0x19,
DripWater = 0x1A,
DripLava = 0x1B,
DripHoney = 0x1C,
FallingDust = 0x1D,
MobSpell = 0x1E,
MobSpellAmbient = 0x1F,
MobSpellInstantaneous = 0x20,
Ink = 0x21,
Slime_0 = 0x22,
RainSplash = 0x23,
VillagerAngry = 0x24,
VillagerHappy = 0x25,
EnchantingTable = 0x26,
TrackingEmitter = 0x27,
Note = 0x28,
WitchSpell = 0x29,
CarrotBoost = 0x2A,
MobAppearance = 0x2B,
EndRod = 0x2C,
DragonBreath = 0x2D,
Spit = 0x2E,
Totem = 0x2F,
Food = 0x30,
FireworksStarter = 0x31,
Fireworks = 0x32,
FireworksOverlay = 0x33,
BalloonGas = 0x34,
ColoredFlame = 0x35,
Sparkler_0 = 0x36,
Conduit = 0x37,
BubbleColumnUp = 0x38,
BubbleColumnDown = 0x39,
Sneeze = 0x3A,
ShulkerBullet_0 = 0x3B,
Bleach = 0x3C,
DragonDestroyBlock = 0x3D,
MyceliumDust = 0x3E,
FallingBorderDust = 0x3F,
CampfireSmoke = 0x40,
CampfireSmokeTall = 0x41,
DragonBreathFire = 0x42,
DragonBreathTrail = 0x43,
_count_8 = 0x44,
};

```
#### PathCompletionType : __int8
```cpp
/* 57493 */
enum PathCompletionType : __int8
{
EMPTY = 0x0,
PARTIAL = 0x1,
FULL = 0x2,
};

```
#### PermissionCommand::Action : __int32
```cpp
/* 426142 */
enum PermissionCommand::Action : __int32
{
List_1 = 0x0,
Reload_0 = 0x1,
Set_0 = 0x2,
};

```
#### PermissionCommand::AvailableCommandPermissionPresets : __int32
```cpp
/* 426191 */
enum PermissionCommand::AvailableCommandPermissionPresets : __int32
{
Visitor_0 = 0x0,
Member_0 = 0x1,
Operator_1 = 0x2,
Undefined_12 = 0x3,
};

```
#### Pillager::State : __int32
```cpp
/* 171005 */
enum Pillager::State : __int32
{
Normal_8 = 0x0,
Hold_0 = 0x1,
Charging_0 = 0x2,
};

```
#### PillarAxis : __int32
```cpp
/* 230435 */
enum PillarAxis : __int32
{
Y_1 = 0x0,
X_2 = 0x1,
Z_2 = 0x2,
_count_51 = 0x3,
};

```
#### PistonBlock::Type : __int32
```cpp
/* 251026 */
enum PistonBlock::Type : __int32
{
Normal_13 = 0x0,
Sticky = 0x1,
};

```
#### PistonBlockActor::PistonState : __int8
```cpp
/* 13193 */
enum PistonBlockActor::PistonState : __int8
{
Retracted = 0x0,
Expanding = 0x1,
Expanded = 0x2,
Retracting = 0x3,
};

```
#### PlaceType : __int32
```cpp
/* 258224 */
enum PlaceType : __int32
{
Arbitrary_0 = 0x0,
Sequential = 0x1,
};

```
#### PlatformType : __int32
```cpp
/* 6933 */
enum PlatformType : __int32
{
Desktop_0 = 0x0,
Pocket = 0x1,
Console_0 = 0x2,
SetTopBox = 0x3,
};

```
#### PlayStatus : __int32
```cpp
/* 77455 */
enum PlayStatus : __int32
{
LoginSuccess = 0x0,
LoginFailed_ClientOld = 0x1,
LoginFailed_ServerOld = 0x2,
PlayerSpawn = 0x3,
LoginFailed_InvalidTenant = 0x4,
LoginFailed_EditionMismatchEduToVanilla = 0x5,
LoginFailed_EditionMismatchVanillaToEdu = 0x6,
LoginFailed_ServerFullSubClient = 0x7,
};

```
#### Player::DimensionState : __int32
```cpp
/* 77066 */
enum Player::DimensionState : __int32
{
Ready_0 = 0x0,
Pending = 0x1,
WaitingServerResponse = 0x2,
WaitingArea = 0x3,
WaitingRespawn = 0x4,
};

```
#### Player::PositionMode : __int8
```cpp
/* 77067 */
enum Player::PositionMode : __int8
{
Normal_4 = 0x0,
Respawn_0 = 0x1,
Teleport_1 = 0x2,
OnlyHeadRot = 0x3,
};

```
#### Player::SpawnPositionSource : __int32
```cpp
/* 88612 */
enum Player::SpawnPositionSource : __int32
{
Randomizer = 0x0,
Respawn_2 = 0x1,
Teleport_3 = 0x2,
Static = 0x3,
};

```
#### Player::SpawnPositionState : __int32
```cpp
/* 88611 */
enum Player::SpawnPositionState : __int32
{
InitializeSpawnPositionRandomizer = 0x0,
WaitForClientAck = 0x1,
ChangeDimension_0 = 0x2,
WaitForDimension = 0x3,
ChooseSpawnArea = 0x4,
CheckLoadedChunk = 0x5,
ChooseSpawnPosition = 0x6,
SpawnComplete = 0x7,
};

```
#### PlayerActionType : __int32
```cpp
/* 13195 */
enum PlayerActionType : __int32
{
};

```
#### PlayerActionType_0 : __int32
```cpp
/* 77458 */
enum PlayerActionType_0 : __int32
{
Unknown_29 = 0xFFFFFFFF,
StartDestroyBlock = 0x0,
AbortDestroyBlock = 0x1,
StopDestroyBlock = 0x2,
GetUpdatedBlock = 0x3,
DropItem = 0x4,
StartSleeping = 0x5,
StopSleeping = 0x6,
Respawn_1 = 0x7,
StartJump = 0x8,
StartSprinting = 0x9,
StopSprinting = 0xA,
StartSneaking = 0xB,
StopSneaking = 0xC,
DEPRECATED_ChangeDimension = 0xD,
ChangeDimensionAck = 0xE,
StartGliding = 0xF,
StopGliding = 0x10,
DenyDestroyBlock = 0x11,
CrackBlock = 0x12,
ChangeSkin = 0x13,
UpdatedEnchantingSeed = 0x14,
StartSwimming = 0x15,
StopSwimming = 0x16,
StartSpinAttack = 0x17,
StopSpinAttack = 0x18,
StartBuildingBlock = 0x19,
};

```
#### PlayerAuthInputPacket::InputData : __int32
```cpp
/* 80058 */
enum PlayerAuthInputPacket::InputData : __int32
{
Ascend = 0x0,
Descend = 0x1,
NorthJump = 0x2,
JumpDown = 0x3,
SprintDown = 0x4,
ChangeHeight = 0x5,
Jumping = 0x6,
AutoJumpingInWater = 0x7,
Sneaking = 0x8,
SneakDown = 0x9,
Up = 0xA,
Down = 0xB,
Left_0 = 0xC,
Right_0 = 0xD,
UpLeft = 0xE,
UpRight = 0xF,
WantUp = 0x10,
WantDown = 0x11,
WantDownSlow = 0x12,
WantUpSlow = 0x13,
Sprinting = 0x14,
AscendScaffolding = 0x15,
DescendScaffolding = 0x16,
SneakToggleDown = 0x17,
PersistSneak = 0x18,
INPUT_NUM = 0x19,
};

```
#### PlayerListPacketType : __int8
```cpp
/* 80065 */
enum PlayerListPacketType : __int8
{
Add_2 = 0x0,
Remove_1 = 0x1,
};

```
#### PlayerPermissionLevel : __int8
```cpp
/* 2411 */
enum PlayerPermissionLevel : __int8
{
Visitor = 0x0,
Member = 0x1,
Operator = 0x2,
Custom = 0x3,
};

```
#### PlayerRespawnState : __int8
```cpp
/* 77454 */
enum PlayerRespawnState : __int8
{
SearchingForSpawn = 0x0,
ReadyToSpawn = 0x1,
ClientReadyToSpawn = 0x2,
};

```
#### PlayerScoreSetFunction : __int8
```cpp
/* 80243 */
enum PlayerScoreSetFunction : __int8
{
Set = 0x0,
Add_3 = 0x1,
Subtract = 0x2,
};

```
#### PlayerSuspension::State : __int32
```cpp
/* 87673 */
enum PlayerSuspension::State : __int32
{
Suspend = 0x0,
Resume_0 = 0x1,
};

```
#### PlayerUISlot : __int32
```cpp
/* 79714 */
enum PlayerUISlot : __int32
{
CursorSelected = 0x0,
AnvilInput = 0x1,
AnvilMaterial = 0x2,
StoneCutterInput = 0x3,
Trade2Ingredient1 = 0x4,
Trade2Ingredient2 = 0x5,
TradeIngredient1 = 0x6,
TradeIngredient2 = 0x7,
MaterialReducerInput = 0x8,
LoomInput = 0x9,
LoomDye = 0xA,
LoomMaterial = 0xB,
CartographyInput = 0xC,
CartographyAdditional = 0xD,
EnchantingInput = 0xE,
EnchantingMaterial = 0xF,
GrindstoneInput = 0x10,
GrindstoneAdditional = 0x11,
CompoundCreatorInput1 = 0x12,
CompoundCreatorInput2 = 0x13,
CompoundCreatorInput3 = 0x14,
CompoundCreatorInput4 = 0x15,
CompoundCreatorInput5 = 0x16,
CompoundCreatorInput6 = 0x17,
CompoundCreatorInput7 = 0x18,
CompoundCreatorInput8 = 0x19,
CompoundCreatorInput9 = 0x1A,
BeaconPayment = 0x1B,
Crafting2x2Input1 = 0x1C,
Crafting2x2Input2 = 0x1D,
Crafting2x2Input3 = 0x1E,
Crafting2x2Input4 = 0x1F,
Crafting3x3Input1 = 0x20,
Crafting3x3Input2 = 0x21,
Crafting3x3Input3 = 0x22,
Crafting3x3Input4 = 0x23,
Crafting3x3Input5 = 0x24,
Crafting3x3Input6 = 0x25,
Crafting3x3Input7 = 0x26,
Crafting3x3Input8 = 0x27,
Crafting3x3Input9 = 0x28,
MaterialReducerOutput1 = 0x29,
MaterialReducerOutput2 = 0x2A,
MaterialReducerOutput3 = 0x2B,
MaterialReducerOutput4 = 0x2C,
MaterialReducerOutput5 = 0x2D,
MaterialReducerOutput6 = 0x2E,
MaterialReducerOutput7 = 0x2F,
MaterialReducerOutput8 = 0x30,
MaterialReducerOutput9 = 0x31,
CreatedItemOutput = 0x32,
_count_17 = 0x33,
};

```
#### PortalAxis : __int32
```cpp
/* 88949 */
enum PortalAxis : __int32
{
Unknown_33 = 0x0,
X_1 = 0x1,
Z_1 = 0x2,
_count_18 = 0x3,
};

```
#### Potion::PotionType : __int32
```cpp
/* 77460 */
enum Potion::PotionType : __int32
{
Undefined_9 = 0xFFFFFFFF,
Regular = 0x0,
Splash_0 = 0x1,
Lingering = 0x2,
};

```
#### Potion::PotionVariant : __int32
```cpp
/* 75384 */
enum Potion::PotionVariant : __int32
{
MOVESLOW = 0x0,
MOVESPEED = 0x1,
DIGSLOW = 0x2,
DIGSPEED = 0x3,
DAMAGEBOOST = 0x4,
HEAL = 0x5,
HARM = 0x6,
JUMP_0 = 0x7,
CONFUSION = 0x8,
REGEN = 0x9,
RESISTANCE = 0xA,
FIRERESISTANCE = 0xB,
WATERBREATH = 0xC,
INVISIBILITY = 0xD,
BLINDNESS = 0xE,
NIGHTVISION = 0xF,
HUNGER = 0x10,
WEAKNESS = 0x11,
POISON = 0x12,
WITHER = 0x13,
HEALTHBOOST = 0x14,
ABSORPTION = 0x15,
SATURATION = 0x16,
LEVITATION = 0x17,
TURTLEMASTER = 0x18,
SLOWFALL = 0x19,
BASE = 0x1A,
};

```
#### PressurePlateBlock::Sensitivity : __int32
```cpp
/* 251032 */
enum PressurePlateBlock::Sensitivity : __int32
{
EVERYTHING = 0x0,
MOBS = 0x1,
PLAYERS = 0x2,
};

```
#### PrismarineBlockType : __int32
```cpp
/* 183771 */
enum PrismarineBlockType : __int32
{
Default_16 = 0x0,
Dark = 0x1,
Bricks_0 = 0x2,
_count_41 = 0x3,
};

```
#### ProfanityFilterContext : __int32
```cpp
/* 109112 */
enum ProfanityFilterContext : __int32
{
None_41 = 0x0,
UIFrontEnd = 0x1,
UIInGame = 0x2,
AllUI = 0x3,
InGameChat = 0x4,
InGameItems = 0x8,
InGameName = 0x10,
All_4 = 0x1F,
};

```
#### Profession : __int32
```cpp
/* 171074 */
enum Profession : __int32
{
};

```
#### ProfilerLite::ScopeTag : __int32
```cpp
/* 603 */
enum ProfilerLite::ScopeTag : __int32
{
None = 0x0,
Root = 0x1,
BeginFrame = 0x2,
ClientInstance = 0x3,
EndFrame = 0x4,
Present = 0x5,
Input = 0x6,
ClientSimTick = 0x7,
ClientRealTick = 0x8,
ServerInstance = 0x9,
ServerSimTick = 0xA,
ServerRealTick = 0xB,
Render = 0xC,
RenderLevel = 0xD,
TickAndRenderUI = 0xE,
Last = 0xE,
SimTickFirst = 0x7,
SimTickLast = 0xB,
RenderTickFirst = 0xC,
RenderTickLast = 0xE,
};

```
#### ProjectileAnchor : __int32
```cpp
/* 58004 */
enum ProjectileAnchor : __int32
{
Origin = 0x0,
EyeHeight = 0x1,
Middle = 0x2,
Count_10 = 0x3,
};

```
#### ProjectileComponent::EAxis : __int32
```cpp
/* 58005 */
enum ProjectileComponent::EAxis : __int32
{
NONE_4 = 0xFFFFFFFF,
X_0 = 0x0,
Y = 0x1,
Z_0 = 0x2,
};

```
#### Projection : __int32
```cpp
/* 36134 */
enum Projection : __int32
{
Rigid = 0x0,
TerrainMatching = 0x1,
Invalid_9 = 0x2,
};

```
#### PurchasePath : __int32
```cpp
/* 45318 */
enum PurchasePath : __int32
{
Unknown_21 = 0xFFFFFFFF,
MinecoinScreen = 0x0,
InsufficientFunds = 0x1,
RealMoneyButton = 0x2,
Redeemed5x5 = 0x3,
Realms_0 = 0x4,
DurableCatalogOffer = 0x5,
};

```
#### PushNotificationType : __int32
```cpp
/* 45338 */
enum PushNotificationType : __int32
{
Achievement_0 = 0x0,
MultiplayerInvite = 0x1,
MultiplayerInviteRaw = 0x2,
FocusLost = 0x3,
BrazeModalDialog = 0x4,
BrazeToast = 0x5,
Toast = 0x6,
DeepLink = 0x7,
RemoveRequest = 0x8,
Unknown_22 = 0x63,
};

```
#### Raid::RaidState : __int32
```cpp
/* 52780 */
enum Raid::RaidState : __int32
{
PreparingGroup = 0x0,
PickingSpawnPoint = 0x1,
SpawningGroup = 0x2,
GroupInPlay = 0x3,
AwardingRewards = 0x4,
Finished = 0x5,
};

```
#### RailDirection : __int32
```cpp
/* 460187 */
enum RailDirection : __int32
{
NorthSouth = 0x0,
EastWest = 0x1,
AscendingEast_0 = 0x2,
AscendingWest_0 = 0x3,
AscendingNorth_0 = 0x4,
AscendingSouth_0 = 0x5,
SouthEast_0 = 0x6,
SouthWest_0 = 0x7,
NorthWest_0 = 0x8,
NorthEast_0 = 0x9,
};

```
#### RakNet::AdapterAttributes : __int32
```cpp
/* 73239 */
enum RakNet::AdapterAttributes : __int32
{
NO_ATTRIBUTES = 0x0,
IS_MULTICAST = 0x1,
IS_LOOPBACK = 0x2,
HAS_NO_GATEWAY = 0x4,
};

```
#### RakNet::ConnectionAttemptResult : __int32
```cpp
/* 73238 */
enum RakNet::ConnectionAttemptResult : __int32
{
CONNECTION_ATTEMPT_STARTED = 0x0,
INVALID_PARAMETER = 0x1,
CANNOT_RESOLVE_DOMAIN_NAME = 0x2,
ALREADY_CONNECTED_TO_ENDPOINT = 0x3,
CONNECTION_ATTEMPT_ALREADY_IN_PROGRESS = 0x4,
SECURITY_INITIALIZATION_FAILED = 0x5,
};

```
#### RakNet::ConnectionState : __int32
```cpp
/* 478071 */
enum RakNet::ConnectionState : __int32
{
IS_PENDING = 0x0,
IS_CONNECTING = 0x1,
IS_CONNECTED = 0x2,
IS_DISCONNECTING = 0x3,
IS_SILENTLY_DISCONNECTING = 0x4,
IS_DISCONNECTED = 0x5,
IS_NOT_CONNECTED = 0x6,
};

```
#### RakNet::InternalPacket::AllocationScheme : __int32
```cpp
/* 477995 */
enum RakNet::InternalPacket::AllocationScheme : __int32
{
NORMAL_0 = 0x0,
REF_COUNTED = 0x1,
STACK = 0x2,
};

```
#### RakNet::PI2_FailedConnectionAttemptReason : __int32
```cpp
/* 478076 */
enum RakNet::PI2_FailedConnectionAttemptReason : __int32
{
FCAR_CONNECTION_ATTEMPT_FAILED = 0x0,
FCAR_ALREADY_CONNECTED = 0x1,
FCAR_NO_FREE_INCOMING_CONNECTIONS = 0x2,
FCAR_SECURITY_PUBLIC_KEY_MISMATCH = 0x3,
FCAR_CONNECTION_BANNED = 0x4,
FCAR_INVALID_PASSWORD = 0x5,
FCAR_INCOMPATIBLE_PROTOCOL = 0x6,
FCAR_IP_RECENTLY_CONNECTED = 0x7,
FCAR_REMOTE_SYSTEM_REQUIRES_PUBLIC_KEY = 0x8,
FCAR_OUR_SYSTEM_REQUIRES_SECURITY = 0x9,
FCAR_PUBLIC_KEY_MISMATCH = 0xA,
};

```
#### RakNet::PI2_LostConnectionReason : __int32
```cpp
/* 478075 */
enum RakNet::PI2_LostConnectionReason : __int32
{
LCR_CLOSED_BY_USER = 0x0,
LCR_DISCONNECTION_NOTIFICATION = 0x1,
LCR_CONNECTION_LOST = 0x2,
};

```
#### RakNet::PluginReceiveResult : __int32
```cpp
/* 478074 */
enum RakNet::PluginReceiveResult : __int32
{
RR_STOP_PROCESSING_AND_DEALLOCATE = 0x0,
RR_CONTINUE_PROCESSING = 0x1,
RR_STOP_PROCESSING = 0x2,
};

```
#### RakNet::PublicKeyMode : __int32
```cpp
/* 478042 */
enum RakNet::PublicKeyMode : __int32
{
PKM_INSECURE_CONNECTION = 0x0,
PKM_ACCEPT_ANY_PUBLIC_KEY = 0x1,
PKM_USE_KNOWN_PUBLIC_KEY = 0x2,
PKM_USE_TWO_WAY_AUTHENTICATION = 0x3,
};

```
#### RakNet::RNS2BindResult : __int32
```cpp
/* 478073 */
enum RakNet::RNS2BindResult : __int32
{
BR_SUCCESS = 0x0,
BR_REQUIRES_RAKNET_SUPPORT_IPV6_DEFINE = 0x1,
BR_FAILED_TO_BIND_SOCKET = 0x2,
BR_FAILED_SEND_TEST = 0x3,
};

```
#### RakNet::RNS2Type : __int32
```cpp
/* 478145 */
enum RakNet::RNS2Type : __int32
{
RNS2T_WINDOWS_STORE_8 = 0x0,
RNS2T_PS3 = 0x1,
RNS2T_PS4 = 0x2,
RNS2T_CHROME = 0x3,
RNS2T_VITA = 0x4,
RNS2T_XBOX_360 = 0x5,
RNS2T_XBOX_720 = 0x6,
RNS2T_WINDOWS = 0x7,
RNS2T_LINUX = 0x8,
};

```
#### RakNet::RNSPerSecondMetrics : __int32
```cpp
/* 64311 */
enum RakNet::RNSPerSecondMetrics : __int32
{
USER_MESSAGE_BYTES_PUSHED = 0x0,
USER_MESSAGE_BYTES_SENT = 0x1,
USER_MESSAGE_BYTES_RESENT = 0x2,
USER_MESSAGE_BYTES_RECEIVED_PROCESSED = 0x3,
USER_MESSAGE_BYTES_RECEIVED_IGNORED = 0x4,
ACTUAL_BYTES_SENT = 0x5,
ACTUAL_BYTES_RECEIVED = 0x6,
RNS_PER_SECOND_METRICS_COUNT = 0x7,
};

```
#### RakNet::RakPeer::$1054D3269989E0175094BA1B08A2EDA8 : __int32
```cpp
/* 478069 */
enum RakNet::RakPeer::$1054D3269989E0175094BA1B08A2EDA8 : __int32
{
requestedConnectionList_Mutex = 0x0,
offlinePingResponse_Mutex = 0x1,
NUMBER_OF_RAKPEER_MUTEXES = 0x2,
};

```
#### RakNet::RakPeer::BufferedCommandStruct::$D8D77DCE4D37D1D6016B84EB664ECA65 : __int32
```cpp
/* 478050 */
enum RakNet::RakPeer::BufferedCommandStruct::$D8D77DCE4D37D1D6016B84EB664ECA65 : __int32
{
BCS_SEND = 0x0,
BCS_CLOSE_CONNECTION = 0x1,
BCS_GET_SOCKET = 0x2,
BCS_CHANGE_SYSTEM_ADDRESS = 0x3,
BCS_DO_NOTHING = 0x4,
};

```
#### RakNet::RakPeer::RemoteSystemStruct::ConnectMode : __int32
```cpp
/* 478031 */
enum RakNet::RakPeer::RemoteSystemStruct::ConnectMode : __int32
{
NO_ACTION = 0x0,
DISCONNECT_ASAP = 0x1,
DISCONNECT_ASAP_SILENTLY = 0x2,
DISCONNECT_ON_NO_ACK = 0x3,
REQUESTED_CONNECTION = 0x4,
HANDLING_CONNECTION_REQUEST = 0x5,
UNVERIFIED_SENDER = 0x6,
CONNECTED = 0x7,
};

```
#### RakNet::RakPeer::RequestedConnectionStruct::$FD3B22BB7AF8A0ABB9D04D1A9E595697 : __int32
```cpp
/* 478043 */
enum RakNet::RakPeer::RequestedConnectionStruct::$FD3B22BB7AF8A0ABB9D04D1A9E595697 : __int32
{
CONNECT = 0x1,
};

```
#### RakNet::StartupResult : __int32
```cpp
/* 63570 */
enum RakNet::StartupResult : __int32
{
RAKNET_STARTED = 0x0,
RAKNET_ALREADY_STARTED = 0x1,
INVALID_SOCKET_DESCRIPTORS = 0x2,
INVALID_MAX_CONNECTIONS = 0x3,
SOCKET_FAMILY_NOT_SUPPORTED = 0x4,
SOCKET_PORT_ALREADY_IN_USE = 0x5,
SOCKET_FAILED_TO_BIND = 0x6,
SOCKET_FAILED_TEST_SEND = 0x7,
PORT_CANNOT_BE_ZERO = 0x8,
FAILED_TO_CREATE_NETWORK_THREAD = 0x9,
COULD_NOT_GENERATE_GUID = 0xA,
STARTUP_OTHER_FAILURE = 0xB,
};

```
#### RakNetInstance::NATState : __int32
```cpp
/* 73237 */
enum RakNetInstance::NATState : __int32
{
NotStarted = 0x0,
PunchRequested = 0x1,
PunchStarted = 0x2,
PunchAddressRegistered = 0x3,
SendingPunchPings = 0x4,
PunchSucceeded = 0x5,
PunchFailed = 0x6,
};

```
#### RakNetServerLocator::protocolVersion : __int32
```cpp
/* 73588 */
enum RakNetServerLocator::protocolVersion : __int32
{
ipv4 = 0x4,
ipv6 = 0x6,
};

```
#### RakPeerHelper::IPVersion : __int32
```cpp
/* 73593 */
enum RakPeerHelper::IPVersion : __int32
{
IPv4_0 = 0x0,
IPv6_0 = 0x1,
COUNT_4 = 0x2,
};

```
#### RawInputType : __int8
```cpp
/* 44570 */
enum RawInputType : __int8
{
};

```
#### Realms::World::State : __int32
```cpp
/* 45316 */
enum Realms::World::State : __int32
{
Uninitialized = 0x0,
Closed = 0x1,
Open = 0x2,
End_0 = 0x3,
};

```
#### RecipeContainerBackgroundStyle : __int32
```cpp
/* 456085 */
enum RecipeContainerBackgroundStyle : __int32
{
Default_20 = 0x0,
GroupHeadCollapsed = 0x1,
GroupHeadExpanded = 0x2,
GroupItem = 0x3,
GroupItemRed = 0x4,
Count_27 = 0x5,
};

```
#### RedefinitionMode : __int8
```cpp
/* 74149 */
enum RedefinitionMode : __int8
{
KeepCurrent = 0x0,
UpdateToNewDefault = 0x1,
};

```
#### RegistrationType : __int32
```cpp
/* 99881 */
enum RegistrationType : __int32
{
MINECRAFT = 0x0,
CUSTOM = 0x1,
NONE_8 = 0x2,
};

```
#### RenderCapability : __int32
```cpp
/* 483788 */
enum RenderCapability : __int32
{
SuperFancyShading = 0x0,
LushLeaves = 0x1,
Atmospherics = 0x2,
EdgeHighlighting = 0x3,
Bloom = 0x4,
TerrainShadows = 0x5,
SuperDuperClouds = 0x6,
LightRays = 0x7,
DepthOfField = 0x8,
SuperDuperWater = 0x9,
CloudFog = 0xA,
FoliageWind = 0xB,
SkyTexture = 0xC,
ToneMap = 0xD,
COUNT_15 = 0xE,
};

```
#### RenderParam : __int32
```cpp
/* 115735 */
enum RenderParam : __int32
{
Unknown_38 = 0xFFFFFFFF,
FrameAlpha = 0x0,
Bob = 0x1,
ModelScale = 0x2,
AnimTime = 0x3,
DeltaTime = 0x4,
KeyFrameLerpTime = 0x5,
LifeTime = 0x6,
IsFirstPerson = 0x7,
NumRenderParams = 0x8,
};

```
#### RepeaterCapacitor::States : __int32
```cpp
/* 464259 */
enum RepeaterCapacitor::States : __int32
{
OFF = 0x0,
ON = 0x1,
OFF_LOCKED = 0x2,
ON_LOCKED = 0x3,
};

```
#### ReplaceItemCommand::TargetType : __int32
```cpp
/* 426462 */
enum ReplaceItemCommand::TargetType : __int32
{
Block_1 = 0x0,
Entity_7 = 0x1,
};

```
#### ResourceFileSystem : __int32
```cpp
/* 2550 */
enum ResourceFileSystem : __int32
{
UserPackage = 0x0,
AppPackage = 0x1,
Raw = 0x2,
RawPersistent = 0x3,
SettingsDir = 0x4,
ExternalDir = 0x5,
ServerPackage = 0x6,
DataDir = 0x7,
UserDir = 0x8,
ScreenshotsDir = 0x9,
StoreCache = 0xA,
Invalid_1 = 0xB,
};

```
#### ResourceInformation::ResourceType : __int32
```cpp
/* 5757 */
enum ResourceInformation::ResourceType : __int32
{
Invalid_7 = 0x0,
Resources_0 = 0x1,
DataAddOn = 0x2,
ScriptAddOn = 0x3,
ClientData = 0x4,
Interface = 0x5,
Mandatory = 0x6,
WorldTemplate_0 = 0x7,
Count_2 = 0x8,
};

```
#### ResourceLoadType : __int32
```cpp
/* 60434 */
enum ResourceLoadType : __int32
{
None_22 = 0x0,
Texture_0 = 0x1,
Sound_0 = 0x2,
MusicDefinition = 0x3,
Localization = 0x4,
Geometry_1 = 0x5,
TerrainAtlas = 0x6,
ItemAtlas = 0x7,
AnimatedAtlas = 0x8,
FontGlyph = 0x9,
BlockGraphics = 0xA,
Tessellator = 0xB,
Material_0 = 0xC,
Seasons = 0xD,
ActorResourceDefinition = 0xE,
UIDefinitions = 0xF,
UIDefinitionReferences = 0x10,
UIDefinitionReports = 0x11,
UIDefinitionResults = 0x12,
ActorSkeletalAnimation = 0x13,
ActorAnimationController = 0x14,
RenderController = 0x15,
ClientInstanceLoadResources = 0x16,
ItemRenderer = 0x17,
DynamicTextures = 0x18,
LevelRenderer = 0x19,
ParticleStaticResources = 0x1A,
FoliageColors = 0x1B,
ClearAndResetFontData = 0x1C,
FinalizeLoad = 0x1D,
ParticleEffect = 0x1E,
All_2 = 0x1F,
Count_11 = 0x1F,
};

```
#### ResourcePackResponse : __int8
```cpp
/* 77456 */
enum ResourcePackResponse : __int8
{
Cancel = 0x1,
Downloading = 0x2,
DownloadingFinished = 0x3,
ResourcePackStackFinished = 0x4,
};

```
#### ResourcePackStackType : __int32
```cpp
/* 5662 */
enum ResourcePackStackType : __int32
{
LEVEL = 0x0,
ADDON = 0x1,
GLOBAL = 0x2,
TREATMENT = 0x3,
BASE_GAME = 0x4,
SIZE = 0x5,
};

```
#### RespawnAnimation : __int32
```cpp
/* 169786 */
enum RespawnAnimation : __int32
{
NONE_10 = 0x0,
START = 0x1,
PREPARING_TO_SUMMON_PILLARS = 0x2,
SUMMONING_PILLARS = 0x3,
SUMMONING_DRAGON = 0x4,
END = 0x5,
};

```
#### RopeParams::Flags : __int32
```cpp
/* 291989 */
enum RopeParams::Flags : __int32
{
None_53 = 0x0,
DynamicResize = 0x2,
DynamicStretch = 0x4,
CollisionEnabled = 0x8,
};

```
#### RopeWave::Direction : __int32
```cpp
/* 88926 */
enum RopeWave::Direction : __int32
{
StartToEnd = 0x0,
EndToStart = 0x1,
};

```
#### Rotation : __int8
```cpp
/* 5803 */
enum Rotation : __int8
{
};

```
#### Rotation_0 : __int8
```cpp
/* 35193 */
enum Rotation_0 : __int8
{
None_14 = 0x0,
Rotate90 = 0x1,
Rotate180 = 0x2,
Rotate270 = 0x3,
Total = 0x4,
};

```
#### SPSCQueue<BatchedNetworkPeer::DataCallback,512>::AllocationMode : __int32
```cpp
/* 421278 */
enum SPSCQueue<BatchedNetworkPeer::DataCallback,512>::AllocationMode : __int32
{
CanAlloc_4 = 0x0,
CannotAlloc_4 = 0x1,
};

```
#### SandStoneType : __int32
```cpp
/* 183772 */
enum SandStoneType : __int32
{
Default_17 = 0x0,
Heiroglyphs = 0x1,
Cut = 0x2,
Smooth_1 = 0x3,
_count_42 = 0x4,
};

```
#### SandType : __int32
```cpp
/* 170973 */
enum SandType : __int32
{
Normal_7 = 0x0,
Red_1 = 0x1,
_count_24 = 0x2,
};

```
#### SaplingType : __int32
```cpp
/* 183773 */
enum SaplingType : __int32
{
Default_18 = 0x0,
Evergreen = 0x1,
Birch_3 = 0x2,
Jungle_5 = 0x3,
Acacia_3 = 0x4,
RoofedOak = 0x5,
_count_43 = 0x6,
};

```
#### SaveCommand::Mode : __int32
```cpp
/* 6500 */
enum SaveCommand::Mode : __int32
{
Hold = 0x0,
Resume = 0x1,
Query = 0x2,
};

```
#### SaveCommand::State : __int32
```cpp
/* 6615 */
enum SaveCommand::State : __int32
{
Idle = 0x0,
Saving = 0x1,
Complete = 0x2,
};

```
#### ScatterParams::CoordinateEvaluationOrder : __int32
```cpp
/* 192994 */
enum ScatterParams::CoordinateEvaluationOrder : __int32
{
XYZ_0 = 0x0,
XZY = 0x1,
YXZ = 0x2,
YZX = 0x3,
ZXY = 0x4,
ZYX = 0x5,
};

```
#### ScatterParams::RandomDistributionType : __int32
```cpp
/* 192993 */
enum ScatterParams::RandomDistributionType : __int32
{
SingleValued = 0x0,
Uniform_0 = 0x1,
Gaussian = 0x2,
Grid = 0x3,
};

```
#### ScorePacketType : __int8
```cpp
/* 80433 */
enum ScorePacketType : __int8
{
Change = 0x0,
Remove_2 = 0x1,
};

```
#### ScoreboardCommand::Action : __int32
```cpp
/* 426673 */
enum ScoreboardCommand::Action : __int32
{
Invalid_29 = 0x0,
Add_7 = 0x1,
List_2 = 0x2,
Operation = 0x3,
Random_3 = 0x4,
Remove_5 = 0x5,
Reset_1 = 0x6,
Set_1 = 0x7,
SetDisplay = 0x8,
Test_1 = 0x9,
};

```
#### ScoreboardCommand::Category : __int32
```cpp
/* 426624 */
enum ScoreboardCommand::Category : __int32
{
Objectives = 0x0,
Players_0 = 0x1,
};

```
#### ScoreboardIdentityPacketType : __int8
```cpp
/* 80489 */
enum ScoreboardIdentityPacketType : __int8
{
Update_0 = 0x0,
Remove_3 = 0x1,
};

```
#### ScriptApi::ApiScriptType : __int32
```cpp
/* 99154 */
enum ScriptApi::ApiScriptType : __int32
{
Server_2 = 0x0,
Client_2 = 0x1,
};

```
#### ScriptApi::ScriptObjectType : __int32
```cpp
/* 100495 */
enum ScriptApi::ScriptObjectType : __int32
{
UndefinedType = 0x0,
NullType = 0x1,
NumberType = 0x2,
StringType = 0x3,
BooleanType = 0x4,
ObjectType = 0x5,
ArrayType = 0x6,
FunctionType = 0x7,
};

```
#### ScriptApi::ScriptReportItemType : __int32
```cpp
/* 95270 */
enum ScriptApi::ScriptReportItemType : __int32
{
Error_3 = 0x0,
Warning_0 = 0x1,
_count_20 = 0x2,
};

```
#### ScriptLogType : __int32
```cpp
/* 99882 */
enum ScriptLogType : __int32
{
Error_4 = 0x0,
Warning_1 = 0x1,
Information = 0x2,
_count_21 = 0x3,
};

```
#### ScriptQueryComponent::ViewType : __int32
```cpp
/* 423827 */
enum ScriptQueryComponent::ViewType : __int32
{
Plain_0 = 0x0,
Spatial = 0x1,
};

```
#### SeaGrassType : __int32
```cpp
/* 183711 */
enum SeaGrassType : __int32
{
Default_15 = 0x0,
DoubleTop = 0x1,
DoubleBot = 0x2,
_count_36 = 0x3,
};

```
#### SeaPickleCount : __int32
```cpp
/* 232934 */
enum SeaPickleCount : __int32
{
One_Pickle = 0x0,
Two_Pickle = 0x1,
Three_Pickle = 0x2,
Four_Pickle = 0x3,
_count_52 = 0x4,
};

```
#### SemVersion::MatchType : __int32
```cpp
/* 5624 */
enum SemVersion::MatchType : __int32
{
Full = 0x0,
Partial = 0x1,
None_4 = 0x2,
};

```
#### SemVersion::ParseOption : __int32
```cpp
/* 5625 */
enum SemVersion::ParseOption : __int32
{
AllowAnyVersion = 0x0,
NoAnyVersion = 0x1,
};

```
#### SemanticConstraint : __int8
```cpp
/* 1541 */
enum SemanticConstraint : __int8
{
None_0 = 0x0,
RequiresCheatsEnabled = 0x1,
RequiresElevatedPermissions = 0x2,
RequiresHostPermissions = 0x4,
VALUE_MASK = 0x7,
};

```
#### SensibleDirections : __int32
```cpp
/* 288528 */
enum SensibleDirections : __int32
{
NORTH_1 = 0x0,
EAST_1 = 0x1,
SOUTH_1 = 0x2,
WEST_1 = 0x3,
};

```
#### ServerInstance::InstanceState : __int32
```cpp
/* 86445 */
enum ServerInstance::InstanceState : __int32
{
Running = 0x0,
Suspended = 0x1,
WaitingLeaveGame = 0x2,
Stopped = 0x3,
NotStarted_0 = 0x4,
};

```
#### ServerPlayer::NearbyActor::State : __int32
```cpp
/* 89357 */
enum ServerPlayer::NearbyActor::State : __int32
{
Unknown_34 = 0x0,
New_1 = 0x1,
Exist = 0x2,
DidExist = 0x3,
};

```
#### SetBlockCommand::SetBlockMode : __int32
```cpp
/* 426891 */
enum SetBlockCommand::SetBlockMode : __int32
{
Replace_2 = 0x0,
Destroy_1 = 0x1,
Keep_0 = 0x2,
};

```
#### SetTitlePacket::TitleType : __int32
```cpp
/* 80526 */
enum SetTitlePacket::TitleType : __int32
{
Clear = 0x0,
Reset_0 = 0x1,
Title = 0x2,
Subtitle = 0x3,
Actionbar = 0x4,
Times = 0x5,
TitleTextObject = 0x6,
SubtitleTextObject = 0x7,
ActionbarTextObject = 0x8,
};

```
#### ShowCreditsPacket::CreditsState : __int32
```cpp
/* 77413 */
enum ShowCreditsPacket::CreditsState : __int32
{
Start_0 = 0x0,
Finished_0 = 0x1,
};

```
#### Side : __int32
```cpp
/* 77457 */
enum Side : __int32
{
Left = 0x0,
Right = 0x1,
};

```
#### SignBlockActor::SignType : __int32
```cpp
/* 183753 */
enum SignBlockActor::SignType : __int32
{
Oak_2 = 0x0,
Spruce_2 = 0x1,
Birch_2 = 0x2,
Jungle_4 = 0x3,
Acacia_2 = 0x4,
DarkOak_2 = 0x5,
};

```
#### SimpleEventPacket::Subtype : __int32
```cpp
/* 77411 */
enum SimpleEventPacket::Subtype : __int32
{
UninitializedSubtype = 0x0,
EnableCommands = 0x1,
DisableCommands = 0x2,
UnlockWorldTemplateSettings = 0x3,
};

```
#### SkeletalHierarchyIndex : __int32
```cpp
/* 104582 */
enum SkeletalHierarchyIndex : __int32
{
Unknown_36 = 0xFFFFFFFF,
};

```
#### Skeleton::SkeletonType : __int32
```cpp
/* 114714 */
enum Skeleton::SkeletonType : __int32
{
DEFAULT = 0x0,
WITHER_0 = 0x1,
STRAY = 0x2,
};

```
#### SkullBlockActor::SkullType : __int32
```cpp
/* 170804 */
enum SkullBlockActor::SkullType : __int32
{
UNSET = 0xFFFFFFFF,
SKELETON = 0x0,
WITHER_1 = 0x1,
ZOMBIE = 0x2,
CHAR = 0x3,
CREEPER = 0x4,
DRAGON = 0x5,
COUNT_9 = 0x6,
};

```
#### SlabBlock::SlabType : __int32
```cpp
/* 460042 */
enum SlabBlock::SlabType : __int32
{
WoodSlab = 0x0,
StoneSlab = 0x1,
};

```
#### Slime::ClientEvent : __int8
```cpp
/* 171023 */
enum Slime::ClientEvent : __int8
{
None_44 = 0x0,
JustLanded = 0x1,
JustJumped = 0x2,
};

```
#### Social::ConnectionType : __int16
```cpp
/* 63699 */
enum Social::ConnectionType : __int16
{
Undefined_8 = 0xFFFF,
Local_3 = 0x0,
IPv4 = 0x1,
IPv6 = 0x2,
NAT = 0x3,
UPNP = 0x4,
UnknownIP = 0x5,
};

```
#### Social::Events::Measurement::AggregationType : __int32
```cpp
/* 43075 */
enum Social::Events::Measurement::AggregationType : __int32
{
Increment_0 = 0x0,
Sum = 0x1,
Min_0 = 0x2,
Max_0 = 0x3,
Average = 0x4,
};

```
#### Social::GamePublishSetting : __int32
```cpp
/* 5598 */
enum Social::GamePublishSetting : __int32
{
NoMultiPlay = 0x0,
InviteOnly = 0x1,
FriendsOnly = 0x2,
FriendsOfFriends = 0x3,
Public = 0x4,
};

```
#### Social::MultiplayerServiceIdentifier : __int32
```cpp
/* 45092 */
enum Social::MultiplayerServiceIdentifier : __int32
{
XboxLive = 0x0,
Nintendo = 0x1,
AdHoc = 0x2,
Playstation = 0x3,
EDU = 0x4,
Mock = 0x5,
Invalid_12 = 0xFFFFFFFF,
};

```
#### SoftEnumUpdateType : __int8
```cpp
/* 81090 */
enum SoftEnumUpdateType : __int8
{
Add_4 = 0x0,
Remove_4 = 0x1,
Replace = 0x2,
};

```
#### SolidityCheckType : __int8
```cpp
/* 123024 */
enum SolidityCheckType : __int8
{
CheckSolidBlocking = 0x0,
CheckCollisionShape = 0x1,
};

```
#### SpawnPositionType : __int32
```cpp
/* 77459 */
enum SpawnPositionType : __int32
{
PlayerRespawn = 0x0,
WorldSpawn = 0x1,
};

```
#### Spider::Type : __int32
```cpp
/* 171024 */
enum Spider::Type : __int32
{
Normal_9 = 0x0,
Cave = 0x1,
};

```
#### SpongeType : __int32
```cpp
/* 183728 */
enum SpongeType : __int32
{
Dry = 0x0,
Wet = 0x1,
_count_38 = 0x2,
};

```
#### StalkAndPounceOnTargetGoal::StalkAndPounceState : __int8
```cpp
/* 122839 */
enum StalkAndPounceOnTargetGoal::StalkAndPounceState : __int8
{
Stalking = 0x0,
Interested = 0x1,
Pouncing = 0x2,
Stuck = 0x3,
Done_1 = 0x4,
};

```
#### StalkThickness : __int32
```cpp
/* 227902 */
enum StalkThickness : __int32
{
Thin = 0x0,
Thick = 0x1,
_count_46 = 0x2,
};

```
#### StateTransitionEvent : __int32
```cpp
/* 452323 */
enum StateTransitionEvent : __int32
{
Entry = 0x0,
Exit = 0x1,
NumCategories = 0x2,
};

```
#### StoneBrickType : __int32
```cpp
/* 31916 */
enum StoneBrickType : __int32
{
Default_3 = 0x0,
Mossy = 0x1,
Cracked = 0x2,
Chiseled = 0x3,
Smooth = 0x4,
_count_6 = 0x5,
};

```
#### StoneSlabType : __int32
```cpp
/* 31472 */
enum StoneSlabType : __int32
{
SmoothStone = 0x0,
Sandstone = 0x1,
Wood = 0x2,
Cobblestone = 0x3,
Brick = 0x4,
StoneBrick = 0x5,
Quartz = 0x6,
NetherBrick = 0x7,
_count_5 = 0x8,
};

```
#### StoneSlabType2 : __int32
```cpp
/* 183653 */
enum StoneSlabType2 : __int32
{
RedSandstone = 0x0,
Purpur = 0x1,
PrismarineRough = 0x2,
PrismarineDark = 0x3,
PrismarineBrick = 0x4,
MossyCobblestone = 0x5,
SmoothSandstone = 0x6,
RedNetherBrick = 0x7,
_count_28 = 0x8,
};

```
#### StoneSlabType3 : __int32
```cpp
/* 183659 */
enum StoneSlabType3 : __int32
{
EndStoneBrick = 0x0,
SmoothRedSandstone = 0x1,
PolishedAndesite = 0x2,
Andesite = 0x3,
Diorite = 0x4,
PolishedDiorite = 0x5,
Granite = 0x6,
PolishedGranite = 0x7,
_count_29 = 0x8,
};

```
#### StoneSlabType4 : __int32
```cpp
/* 183647 */
enum StoneSlabType4 : __int32
{
MossyStoneBrick_0 = 0x0,
SmoothQuartz = 0x1,
Stone_1 = 0x2,
CutSandstone = 0x3,
CutRedSandstone = 0x4,
_count_27 = 0x5,
};

```
#### StoneType : __int32
```cpp
/* 183677 */
enum StoneType : __int32
{
Stone_2 = 0x0,
Granite_0 = 0x1,
GraniteSmooth = 0x2,
Diorite_0 = 0x3,
DioriteSmooth = 0x4,
Andesite_0 = 0x5,
AndesiteSmooth = 0x6,
_count_32 = 0x7,
};

```
#### StoragePermissionResult : __int8
```cpp
/* 6917 */
enum StoragePermissionResult : __int8
{
PermissionGranted = 0x0,
PermissionDenied = 0x1,
};

```
#### StorageVersion : __int32
```cpp
/* 5656 */
enum StorageVersion : __int32
{
Unknown_0 = 0x0,
OldV1 = 0x1,
OldV2 = 0x2,
OldV3 = 0x3,
LevelDB1 = 0x4,
LevelDBSubChunks = 0x5,
LevelDBSubChunkRawZip = 0x6,
LevelDBPaletted1 = 0x7,
LevelDBPalettedMultiBlockStorage = 0x8,
};

```
#### StrongholdPiece::SmallDoorType : __int32
```cpp
/* 31370 */
enum StrongholdPiece::SmallDoorType : __int32
{
OPENING = 0x0,
WOOD_DOOR = 0x1,
GRATES = 0x2,
IRON_DOOR = 0x3,
};

```
#### StructureBlockPaletteLoadResult : __int32
```cpp
/* 77452 */
enum StructureBlockPaletteLoadResult : __int32
{
Success_8 = 0x0,
MissingBlockPaletteField = 0x1,
ExpectedCompoundTagInBlockList = 0x2,
MissingBlockPositionDataField = 0x3,
ExpectedNumberAsStringWhenParsingBlockPositionData = 0x4,
ExpectedCompoundForBlockPositionData = 0x5,
ExpectedCompoundTagForBlockEntityData = 0x6,
ExpectedListTagForTickQueueData = 0x7,
ExpectedCompoundTagInTickQueueData = 0x8,
};

```
#### StructureBlockType : __int32
```cpp
/* 44548 */
enum StructureBlockType : __int32
{
Data = 0x0,
Save_0 = 0x1,
Load_0 = 0x2,
Corner = 0x3,
Invalid_10 = 0x4,
Export_0 = 0x5,
_count_15 = 0x6,
};

```
#### StructureFeatureType : __int8
```cpp
/* 37036 */
enum StructureFeatureType : __int8
{
Unknown_5 = 0x0,
EndCity = 0x1,
Fortress = 0x2,
Mineshaft = 0x3,
Monument = 0x4,
Stronghold = 0x5,
Temple = 0x6,
Village = 0x7,
WoodlandMansion = 0x8,
Shipwreck_0 = 0x9,
BuriedTreasure_0 = 0xA,
Ruins = 0xB,
PillagerOutpost_0 = 0xC,
_count_13 = 0xD,
};

```
#### StructureLoadResult : __int32
```cpp
/* 288522 */
enum StructureLoadResult : __int32
{
Success_13 = 0x0,
MissingFormatVersionField = 0x1,
InvalidFormatVersion = 0x2,
MissingSizeField = 0x3,
SizeIsNot3Elements = 0x4,
NegativeSize = 0x5,
MissingWorldOriginField = 0x6,
WorldOriginIsNot3Elements = 0x7,
MissingBlockIndicesField = 0x8,
BlockIndicesNot2Arrays = 0x9,
BlockIndicesIsNotAList = 0xA,
BlockIndicesListsNotSameSize = 0xB,
MismatchedSizeAndBlockIndicesSize = 0xC,
MissingPaletteField = 0xD,
FailedToLoadPalette = 0xE,
ExpectedCompoundTagInPaletteList = 0xF,
MissingEntitiesField = 0x10,
ExpectedCompoundTagInEntitiesList = 0x11,
};

```
#### StructurePieceType : __int32
```cpp
/* 31924 */
enum StructurePieceType : __int32
{
Unknown_3 = 0x0,
EndCityPiece = 0x45435450,
MineshaftRoom = 0x4D53524D,
MineshaftCorridor = 0x4D53434F,
MineshaftCrossing = 0x4D534352,
MineshaftStairs = 0x4D535354,
NetherFortressCrossing = 0x4E424352,
NetherFortressStartPiece = 0x4E425350,
NetherFortressStraight = 0x4E425354,
NetherFortressEndFiller = 0x4E424546,
NetherFortressRoomCrossing = 0x4E425243,
NetherFortressStairsRoom = 0x4E425352,
NetherFortressMonsterThrone = 0x4E424D54,
NetherCastleEntrance = 0x4E43454E,
NetherCastleStalkRoom = 0x4E435352,
NetherCastleSmallCorridor = 0x4E435343,
NetherCastleSmallCorridorCrossing = 0x4E434343,
NetherCastleSmallCorridorRightTurn = 0x4E435254,
NetherCastleSmallCorridorLeftTurn = 0x4E434C54,
NetherCastleCorridorStairs = 0x4E435354,
NetherCastleCorridorTBalcony = 0x4E434241,
OceanMonumentBuilding = 0x4F4D4255,
OceanMonumentEntryRoom = 0x4F4D4552,
OceanMonumentSimpleRoom = 0x4F4D5352,
OceanMonumentSimpleTopRoom = 0x4F4D5452,
OceanMonumentDoubleXRoom = 0x4F4D3258,
OceanMonumentDoubleYRoom = 0x4F4D3259,
OceanMonumentDoubleZRoom = 0x4F4D325A,
OceanMonumentDoubleXYRoom = 0x4F4D5859,
OceanMonumentDoubleYZRoom = 0x4F4D595A,
OceanMonumentCoreRoom = 0x4F4D4352,
OceanMonumentWingRoom = 0x4F4D5752,
OceanMonumentPenthouse = 0x4F4D5048,
DesertPyramid = 0x44535254,
Igloo = 0x49474C4F,
JunglePyramid = 0x4A4E474C,
WitchHut = 0x57544348,
StrongholdStairsDown = 0x53485344,
StrongholdStartPiece = 0x53485350,
StrongholdChestCorridor = 0x53484348,
StrongholdFillerCorridor = 0x53484649,
StrongholdFiveCrossing = 0x53483543,
StrongholdLeftTurn = 0x53484C54,
StrongholdRightTurn = 0x53485254,
StrongholdLibrary = 0x53484C49,
StrongholdPortalRoom = 0x53485052,
StrongholdPrisonHall = 0x53485048,
StrongholdRoomCrossing = 0x53485243,
StrongholdStraight = 0x53485354,
StrongholdStraightStairsDown = 0x53485353,
VillageWell = 0x56495745,
VillageStartPiece = 0x56495350,
VillageSimpleHouse = 0x56495348,
VillageSmallTemple = 0x56495354,
VillageBookHouse = 0x56494248,
VillageSmallHut = 0x56494854,
VillagePigHouse = 0x56495047,
VillageDoubleFarmland = 0x56494446,
VillageFarmland = 0x5649464C,
VillageSmithy = 0x5649534D,
VillageTwoRoomHouse = 0x56493252,
VillageLightPost = 0x56494C50,
VillageStraightRoad = 0x56495352,
WoodlandMansionPiece = 0x574C4D50,
Shipwreck = 0x53505752,
BuriedTreasure = 0x42525452,
OceanRuinsPiece = 0x4F435250,
};

```
#### StructureRedstoneSaveMode : __int8
```cpp
/* 44554 */
enum StructureRedstoneSaveMode : __int8
{
SavesToMemory = 0x0,
SavesToDisk = 0x1,
};

```
#### StructureTemplateRequestOperation : __int8
```cpp
/* 77451 */
enum StructureTemplateRequestOperation : __int8
{
None_26 = 0x0,
ExportFromSaveMode = 0x1,
ExportFromLoadMode = 0x2,
QuerySavedStructure = 0x3,
};

```
#### StructureTemplateResponseType : __int8
```cpp
/* 42308 */
enum StructureTemplateResponseType : __int8
{
};

```
#### StructureTemplateResponseType_0 : __int8
```cpp
/* 77453 */
enum StructureTemplateResponseType_0 : __int8
{
None_27 = 0x0,
Export_1 = 0x1,
Query_0 = 0x2,
};

```
#### StructureVoidType : __int32
```cpp
/* 230196 */
enum StructureVoidType : __int32
{
Void_0 = 0x0,
Air_1 = 0x1,
_count_49 = 0x2,
};

```
#### SubChunkBlockStorage::Type : __int8
```cpp
/* 253606 */
enum SubChunkBlockStorage::Type : __int8
{
Paletted1 = 0x1,
Paletted2 = 0x2,
Paletted3 = 0x3,
Paletted4 = 0x4,
Paletted5 = 0x5,
Paletted6 = 0x6,
Paletted8 = 0x8,
Paletted16 = 0x10,
};

```
#### SubChunkFormat : __int8
```cpp
/* 45384 */
enum SubChunkFormat : __int8
{
v17_0_0 = 0x0,
v1_3_0_0 = 0x1,
v17_0_badly_converted1 = 0x2,
v17_0_badly_converted2 = 0x3,
v17_0_badly_converted3 = 0x4,
v17_0_badly_converted4 = 0x5,
v17_0_badly_converted5 = 0x6,
v17_0_badly_converted6 = 0x7,
v1_3_0_2 = 0x8,
};

```
#### SubChunkInitMode : __int32
```cpp
/* 35032 */
enum SubChunkInitMode : __int32
{
All = 0x0,
AllButLast = 0x1,
None_12 = 0x2,
};

```
#### SubChunkRelighter::SubChunkToDoBitsClearMode : __int32
```cpp
/* 252864 */
enum SubChunkRelighter::SubChunkToDoBitsClearMode : __int32
{
AllSubChunkBorderBitsExceptTheOuterEdgeOfComputationBits = 0x0,
SetOuterEdgeOfComputationBits = 0x1,
};

```
#### SummonShape : __int32
```cpp
/* 88812 */
enum SummonShape : __int32
{
Circle = 0x0,
Line = 0x1,
Count_20 = 0x2,
};

```
#### SummonTarget : __int32
```cpp
/* 88813 */
enum SummonTarget : __int32
{
Self_1 = 0x0,
Target_0 = 0x1,
Count_21 = 0x2,
};

```
#### SuspiciousStewItem::SuspiciousStewType : __int32
```cpp
/* 183451 */
enum SuspiciousStewItem::SuspiciousStewType : __int32
{
Poppy = 0x0,
Cornflower = 0x1,
Tulip = 0x2,
AzureBluet = 0x3,
LilyOfTheValley = 0x4,
Dandelion = 0x5,
BlueOrchid = 0x6,
Allium = 0x7,
OxeyeDaisy = 0x8,
WitherRose = 0x9,
COUNT_12 = 0xA,
};

```
#### SweetBerryBushBlock::BerryStage : __int32
```cpp
/* 460045 */
enum SweetBerryBushBlock::BerryStage : __int32
{
Sapling = 0x0,
NoBerries = 0x1,
SomeBerries = 0x2,
FullBerries = 0x3,
};

```
#### Tag::Type : __int8
```cpp
/* 48666 */
enum Tag::Type : __int8
{
End_1 = 0x0,
Byte_0 = 0x1,
Short_0 = 0x2,
Int_2 = 0x3,
Int64_0 = 0x4,
Float_3 = 0x5,
Double = 0x6,
ByteArray = 0x7,
String_1 = 0x8,
List_0 = 0x9,
Compound = 0xA,
IntArray = 0xB,
};

```
#### TagCommand::Action : __int8
```cpp
/* 427273 */
enum TagCommand::Action : __int8
{
Add_8 = 0x0,
Remove_6 = 0x1,
List_3 = 0x2,
};

```
#### TallGrassType : __int32
```cpp
/* 31090 */
enum TallGrassType : __int32
{
Default_2 = 0x0,
Tall = 0x1,
Fern = 0x2,
Snow = 0x3,
_count_4 = 0x4,
};

```
#### TargetSelectionMethod : __int8
```cpp
/* 88785 */
enum TargetSelectionMethod : __int8
{
};

```
#### TargetSelectionMethod_0 : __int8
```cpp
/* 117056 */
enum TargetSelectionMethod_0 : __int8
{
Nearest = 0x0,
Random_2 = 0x1,
};

```
#### TaskGroupState : __int32
```cpp
/* 484303 */
enum TaskGroupState : __int32
{
Running_2 = 0x0,
Paused = 0x1,
Flush_0 = 0x2,
Sync_0 = 0x3,
};

```
#### TaskOptions : __int32
```cpp
/* 63712 */
enum TaskOptions : __int32
{
Default_7 = 0x0,
TaskProfiled = 0x1,
LinkPredecessor = 0x2,
};

```
#### TaskType : __int32
```cpp
/* 484374 */
enum TaskType : __int32
{
Flushable = 0x0,
};

```
#### TeleportCommand::FacingResult : __int32
```cpp
/* 427393 */
enum TeleportCommand::FacingResult : __int32
{
HaveFacing = 0x0,
NoFacing = 0x1,
Error_5 = 0x2,
};

```
#### TeleportCommand::TeleportAnalysis : __int32
```cpp
/* 427464 */
enum TeleportCommand::TeleportAnalysis : __int32
{
WontClip = 0x0,
WillClip = 0x1,
ChunksUnloaded = 0x2,
};

```
#### TemperatureCategory : __int32
```cpp
/* 191331 */
enum TemperatureCategory : __int32
{
Frozen_0 = 0x0,
};

```
#### TemplateLockState : __int8
```cpp
/* 5774 */
enum TemplateLockState : __int8
{
Undefined_1 = 0x0,
Enabled = 0x1,
Disabled = 0x2,
};

```
#### TestForBlocksCommand::Mode : __int32
```cpp
/* 427579 */
enum TestForBlocksCommand::Mode : __int32
{
All_9 = 0x0,
Masked_0 = 0x1,
};

```
#### TextPacketType : __int8
```cpp
/* 77445 */
enum TextPacketType : __int8
{
Raw_0 = 0x0,
Chat = 0x1,
Translate = 0x2,
Popup = 0x3,
JukeboxPopup = 0x4,
Tip = 0x5,
SystemMessage = 0x6,
Whisper = 0x7,
Announcement = 0x8,
TextObject = 0x9,
};

```
#### TickingAreaCommand::AddAreaType : __int32
```cpp
/* 427758 */
enum TickingAreaCommand::AddAreaType : __int32
{
Bounds = 0x0,
Circle_0 = 0x1,
};

```
#### TickingAreaCommand::Mode : __int32
```cpp
/* 427709 */
enum TickingAreaCommand::Mode : __int32
{
Add_9 = 0x0,
Remove_7 = 0x1,
RemoveAll = 0x2,
List_4 = 0x3,
};

```
#### TickingAreaCommand::TargetDimensions : __int32
```cpp
/* 427807 */
enum TickingAreaCommand::TargetDimensions : __int32
{
CurrentDimension = 0x0,
AllDimensions = 0x1,
};

```
#### TickingQueueType : __int8
```cpp
/* 36326 */
enum TickingQueueType : __int8
{
Internal_0 = 0x0,
Random_0 = 0x1,
};

```
#### TimeCommand::Mode : __int32
```cpp
/* 427946 */
enum TimeCommand::Mode : __int32
{
Set_2 = 0x0,
Add_10 = 0x1,
Query_1 = 0x2,
};

```
#### TimeCommand::Query : __int32
```cpp
/* 427995 */
enum TimeCommand::Query : __int32
{
DayTime = 0x0,
GameTime = 0x1,
Day = 0x2,
};

```
#### TimeCommand::TimeSpec : __int32
```cpp
/* 428044 */
enum TimeCommand::TimeSpec : __int32
{
Sunrise = 0x0,
Day_0 = 0x1,
Noon = 0x2,
Sunset = 0x3,
Night = 0x4,
Midnight = 0x5,
Unspecified = 0x6,
};

```
#### TitleCommand::Mode : __int32
```cpp
/* 428171 */
enum TitleCommand::Mode : __int32
{
Clear_1 = 0x0,
Reset_2 = 0x1,
Title_0 = 0x2,
Subtitle_0 = 0x3,
ActionBar = 0x4,
Times_0 = 0x5,
};

```
#### TitleRawCommand::Mode : __int32
```cpp
/* 428299 */
enum TitleRawCommand::Mode : __int32
{
Clear_2 = 0x0,
Reset_3 = 0x1,
Title_1 = 0x2,
Subtitle_1 = 0x3,
ActionBar_0 = 0x4,
Times_1 = 0x5,
};

```
#### Token::Type : __int32
```cpp
/* 117551 */
enum Token::Type : __int32
{
String_5 = 0x0,
Number = 0x1,
Bool_2 = 0x2,
};

```
#### Token::tokenize::$663C034D90AC1D8D8F9A30B68A82B4D9 : __int32
```cpp
/* 430694 */
enum Token::tokenize::$663C034D90AC1D8D8F9A30B68A82B4D9 : __int32
{
S_NONE = 0x0,
S_TOKEN = 0x1,
S_QUOTES = 0x2,
};

```
#### TorchFacing : __int32
```cpp
/* 227584 */
enum TorchFacing : __int32
{
Unknown_46 = 0x0,
West_0 = 0x1,
East_0 = 0x2,
North_0 = 0x3,
South_0 = 0x4,
Top_0 = 0x5,
_count_44 = 0x6,
};

```
#### TrackerType : __int32
```cpp
/* 5581 */
enum TrackerType : __int32
{
ClientPackets = 0x0,
ServerPackets = 0x1,
Xbox = 0x2,
HttpMisc = 0x3,
Count_0 = 0x4,
};

```
#### TransactionStatus : __int32
```cpp
/* 44610 */
enum TransactionStatus : __int32
{
};

```
#### TransferState : __int32
```cpp
/* 44669 */
enum TransferState : __int32
{
};

```
#### TrapDoorBlock::TrapDoorDir : __int8
```cpp
/* 460049 */
enum TrapDoorBlock::TrapDoorDir : __int8
{
DIR_EAST = 0x0,
DIR_WEST = 0x1,
DIR_SOUTH = 0x2,
DIR_NORTH = 0x3,
};

```
#### TrustedSkinFlag : __int8
```cpp
/* 74259 */
enum TrustedSkinFlag : __int8
{
Unset_0 = 0x0,
False = 0x1,
True = 0x2,
};

```
#### UIPackErrorType : __int32
```cpp
/* 85849 */
enum UIPackErrorType : __int32
{
None_35 = 0x0,
InvalidChildNames = 0x1,
ParseError_0 = 0x2,
MissingControl = 0x3,
MissingControlTarget = 0x4,
MissingArrayName = 0x5,
MissingCondition = 0x6,
MissingValue = 0x7,
MissingOperation = 0x8,
InvalidOperationName = 0x9,
};

```
#### UIProfile : __int32
```cpp
/* 480116 */
enum UIProfile : __int32
{
Classic_0 = 0x0,
Pocket_0 = 0x1,
Count_30 = 0x2,
};

```
#### UIScalingRules : __int32
```cpp
/* 6931 */
enum UIScalingRules : __int32
{
Desktop = 0x0,
PocketApple = 0x1,
PocketAndroid = 0x2,
PocketWindows = 0x3,
Console = 0x4,
HandheldConsole = 0x5,
};

```
#### UploadError : __int32
```cpp
/* 101407 */
enum UploadError : __int32
{
None_36 = 0x0,
ForbiddenContent = 0x1,
Unknown_35 = 0x2,
};

```
#### UploadState : __int32
```cpp
/* 101406 */
enum UploadState : __int32
{
Uninitialized_1 = 0x0,
Initializing = 0x1,
Progress = 0x2,
Exporting = 0x3,
Done_0 = 0x4,
Failed_6 = 0x5,
};

```
#### UpnpState : __int32
```cpp
/* 62643 */
enum UpnpState : __int32
{
Startup = 0x0,
UpnpRequested = 0x1,
UpnpStarted = 0x2,
UpnpSucceeded = 0x3,
UpnpFailed = 0x4,
Invalid_13 = 0x5,
};

```
#### UseAnimation : __int8
```cpp
/* 33513 */
enum UseAnimation : __int8
{
None_10 = 0x0,
Eat = 0x1,
Drink = 0x2,
Block_0 = 0x3,
Bow = 0x4,
Camera_0 = 0x5,
Spear = 0x6,
GlowStick = 0x7,
Sparkler = 0x8,
Crossbow = 0x9,
};

```
#### Util::NumberConversionResult : __int32
```cpp
/* 93422 */
enum Util::NumberConversionResult : __int32
{
Succeed = 0x0,
Invalid_20 = 0x1,
TooSmall = 0x2,
TooLarge = 0x3,
Count_22 = 0x4,
};

```
#### Util::removeAllColorCodes::RemoveAllColorCodesState : __int32
```cpp
/* 103850 */
enum Util::removeAllColorCodes::RemoveAllColorCodesState : __int32
{
Output = 0x0,
SawCodeByte1 = 0x1,
SawCodeByte2 = 0x2,
};

```
#### VRControllerType : __int64
```cpp
/* 6884 */
enum VRControllerType : __int64
{
Standard_0 = 0x0,
SingleTriggerGearVR = 0x1,
GearVR = 0x2,
MotionController = 0x3,
_count = 0x4,
};

```
#### VanillaBiomeTypes : __int32
```cpp
/* 42752 */
enum VanillaBiomeTypes : __int32
{
};

```
#### VanillaBiomeTypes_0 : __int32
```cpp
/* 115604 */
enum VanillaBiomeTypes_0 : __int32
{
Beach = 0x0,
Desert = 0x1,
ExtremeHills = 0x2,
Flat_0 = 0x3,
Forest_1 = 0x4,
Hell = 0x5,
Ice_1 = 0x6,
Jungle_3 = 0x7,
Mesa = 0x8,
MushroomIsland = 0x9,
Ocean_0 = 0xA,
Plain = 0xB,
River = 0xC,
Savanna_0 = 0xD,
StoneBeach = 0xE,
Swamp_0 = 0xF,
Taiga_0 = 0x10,
TheEnd_0 = 0x11,
DataDriven = 0x12,
};

```
#### VideoStreamConnectPacket::Action : __int8
```cpp
/* 81105 */
enum VideoStreamConnectPacket::Action : __int8
{
NONE_6 = 0x0,
CLOSE = 0x1,
};

```
#### WSConnectionResult : __int8
```cpp
/* 6406 */
enum WSConnectionResult : __int8
{
Failed = 0x0,
InvalidUri = 0x1,
ConnectionInProgress = 0x2,
Success_1 = 0x3,
};

```
#### WallBlockType : __int32
```cpp
/* 183770 */
enum WallBlockType : __int32
{
Cobblestone_1 = 0x0,
MossyCobblestone_0 = 0x1,
Granite_1 = 0x2,
Diorite_1 = 0x3,
Andesite_1 = 0x4,
Sandstone_0 = 0x5,
Brick_0 = 0x6,
StoneBrick_1 = 0x7,
MossyStoneBrick_1 = 0x8,
NetherBrick_0 = 0x9,
EndBrick = 0xA,
Prismarine = 0xB,
RedSandstone_0 = 0xC,
RedNetherBrick_0 = 0xD,
_count_40 = 0xE,
};

```
#### WeakStorageEntity::EmptyInit : __int32
```cpp
/* 13156 */
enum WeakStorageEntity::EmptyInit : __int32
{
NoValue = 0x0,
};

```
#### WeakStorageEntity::VariadicInit : __int32
```cpp
/* 13157 */
enum WeakStorageEntity::VariadicInit : __int32
{
NonAmbiguous = 0x0,
};

```
#### WeakStorageFeature::EmptyInit : __int32
```cpp
/* 31085 */
enum WeakStorageFeature::EmptyInit : __int32
{
NoValue_2 = 0x0,
};

```
#### WeakStorageFeature::VariadicInit : __int32
```cpp
/* 31086 */
enum WeakStorageFeature::VariadicInit : __int32
{
NonAmbiguous_2 = 0x0,
};

```
#### WeakStorageSharePtr<EntityRegistry>::EmptyInit : __int32
```cpp
/* 13162 */
enum WeakStorageSharePtr<EntityRegistry>::EmptyInit : __int32
{
};

```
#### WeakStorageSharePtr<EntityRegistry>::VariadicInit : __int32
```cpp
/* 13163 */
enum WeakStorageSharePtr<EntityRegistry>::VariadicInit : __int32
{
};

```
#### WeakStorageSharePtr<PerlinSimplexNoise>::EmptyInit : __int32
```cpp
/* 191529 */
enum WeakStorageSharePtr<PerlinSimplexNoise>::EmptyInit : __int32
{
};

```
#### WeakStorageSharePtr<PerlinSimplexNoise>::VariadicInit : __int32
```cpp
/* 191530 */
enum WeakStorageSharePtr<PerlinSimplexNoise>::VariadicInit : __int32
{
};

```
#### WeatherCommand::WeatherRequest : __int32
```cpp
/* 428598 */
enum WeatherCommand::WeatherRequest : __int32
{
Set_3 = 0x0,
Query_2 = 0x1,
};

```
#### WeatherCommand::WeatherType : __int32
```cpp
/* 428549 */
enum WeatherCommand::WeatherType : __int32
{
Clear_3 = 0x0,
Rain = 0x1,
Thunder_0 = 0x2,
};

```
#### WeirdoDirection : __int32
```cpp
/* 31931 */
enum WeirdoDirection : __int32
{
East = 0x0,
West = 0x1,
South = 0x2,
North = 0x3,
};

```
#### WhitelistCommand::Action : __int32
```cpp
/* 6683 */
enum WhitelistCommand::Action : __int32
{
List = 0x0,
On = 0x1,
Off = 0x2,
AddName = 0x3,
RemoveName = 0x4,
Reload = 0x5,
};

```
#### WoodType : __int32
```cpp
/* 35877 */
enum WoodType : __int32
{
Oak_1 = 0x0,
Spruce_1 = 0x1,
Birch_1 = 0x2,
Jungle_2 = 0x3,
Acacia = 0x4,
DarkOak = 0x5,
_count_12 = 0x6,
};

```
#### WoodlandMansionPieces::WoodlandMansionPiece::_addChest::SensibleDirections : __int32
```cpp
/* 288547 */
enum WoodlandMansionPieces::WoodlandMansionPiece::_addChest::SensibleDirections : __int32
{
NORTH_2 = 0x0,
EAST_2 = 0x1,
SOUTH_2 = 0x2,
WEST_2 = 0x3,
};

```
#### WorldConversionError : __int32
```cpp
/* 45327 */
enum WorldConversionError : __int32
{
};

```
#### WorldPacksHistoryFile::ParseResult : __int32
```cpp
/* 85907 */
enum WorldPacksHistoryFile::ParseResult : __int32
{
InvalidArrayOfPacks = 0x0,
InvalidPack = 0x1,
Success_9 = 0x2,
};

```
#### XXH_alignment : __int32
```cpp
/* 424367 */
enum XXH_alignment : __int32
{
XXH_aligned = 0x0,
XXH_unaligned = 0x1,
};

```
#### XXH_endianess : __int32
```cpp
/* 424366 */
enum XXH_endianess : __int32
{
XXH_bigEndian = 0x0,
XXH_littleEndian = 0x1,
};

```
#### Zombie::ZombieType : __int32
```cpp
/* 171000 */
enum Zombie::ZombieType : __int32
{
DEFAULT_1 = 0x0,
VILLAGER = 0x1,
HUSK = 0x2,
PIGZOMBIE = 0x3,
DROWNED = 0x4,
};

```
#### __ptrace_request : __int32
```cpp
/* 486223 */
enum __ptrace_request : __int32
{
PTRACE_TRACEME = 0x0,
PTRACE_PEEKTEXT = 0x1,
PTRACE_PEEKDATA = 0x2,
PTRACE_PEEKUSER = 0x3,
PTRACE_POKETEXT = 0x4,
PTRACE_POKEDATA = 0x5,
PTRACE_POKEUSER = 0x6,
PTRACE_CONT = 0x7,
PTRACE_KILL = 0x8,
PTRACE_SINGLESTEP = 0x9,
PTRACE_GETREGS = 0xC,
PTRACE_SETREGS = 0xD,
PTRACE_GETFPREGS = 0xE,
PTRACE_SETFPREGS = 0xF,
PTRACE_ATTACH = 0x10,
PTRACE_DETACH = 0x11,
PTRACE_GETFPXREGS = 0x12,
PTRACE_SETFPXREGS = 0x13,
PTRACE_SYSCALL = 0x18,
PTRACE_GET_THREAD_AREA = 0x19,
PTRACE_SET_THREAD_AREA = 0x1A,
PTRACE_ARCH_PRCTL = 0x1E,
PTRACE_SYSEMU = 0x1F,
PTRACE_SYSEMU_SINGLESTEP = 0x20,
PTRACE_SINGLEBLOCK = 0x21,
PTRACE_SETOPTIONS = 0x4200,
PTRACE_GETEVENTMSG = 0x4201,
PTRACE_GETSIGINFO = 0x4202,
PTRACE_SETSIGINFO = 0x4203,
PTRACE_GETREGSET = 0x4204,
PTRACE_SETREGSET = 0x4205,
PTRACE_SEIZE = 0x4206,
PTRACE_INTERRUPT = 0x4207,
PTRACE_LISTEN = 0x4208,
PTRACE_PEEKSIGINFO = 0x4209,
PTRACE_GETSIGMASK = 0x420A,
PTRACE_SETSIGMASK = 0x420B,
PTRACE_SECCOMP_GET_FILTER = 0x420C,
};

```
#### __socket_type : __int32
```cpp
/* 294340 */
enum __socket_type : __int32
{
SOCK_STREAM = 0x1,
SOCK_DGRAM = 0x2,
SOCK_RAW = 0x3,
SOCK_RDM = 0x4,
SOCK_SEQPACKET = 0x5,
SOCK_DCCP = 0x6,
SOCK_PACKET = 0xA,
SOCK_CLOEXEC = 0x80000,
SOCK_NONBLOCK = 0x800,
};

```
#### `anonymous namespace'::PriorityBucket : __int32
```cpp
/* 258294 */
enum `anonymous namespace'::PriorityBucket : __int32
{
BeforeUndergroundPass = 0x0,
UndergroundPass = 0x1,
BeforeSurfacePass = 0x2,
SurfacePass = 0x3,
BeforeSkyPass = 0x4,
SkyPass = 0x5,
FinalPass = 0x6,
_Count_6 = 0x7,
};

```
#### cg::ColorSpace : __int8
```cpp
/* 457059 */
enum cg::ColorSpace : __int8
{
Unknown_47 = 0x0,
sRGB_0 = 0x1,
Linear_0 = 0x2,
};

```
#### com::mojang::clacks::protocol::CheatsSetting : __int32
```cpp
/* 7924 */
enum com::mojang::clacks::protocol::CheatsSetting : __int32
{
ALLOW = 0x0,
DISALLOW = 0x1,
CheatsSetting_INT_MIN_SENTINEL_DO_NOT_USE_ = 0x80000000,
CheatsSetting_INT_MAX_SENTINEL_DO_NOT_USE_ = 0x7FFFFFFF,
};

```
#### com::mojang::clacks::protocol::DifficultySetting : __int32
```cpp
/* 7923 */
enum com::mojang::clacks::protocol::DifficultySetting : __int32
{
PEACEFUL = 0x0,
EASY = 0x1,
NORMAL = 0x2,
HARD = 0x3,
DifficultySetting_INT_MIN_SENTINEL_DO_NOT_USE_ = 0x80000000,
DifficultySetting_INT_MAX_SENTINEL_DO_NOT_USE_ = 0x7FFFFFFF,
};

```
#### com::mojang::clacks::protocol::MetricReport::MetricCase : __int32
```cpp
/* 8627 */
enum com::mojang::clacks::protocol::MetricReport::MetricCase : __int32
{
kBandwith = 0x1,
kLatency = 0x2,
kTickTime = 0x3,
METRIC_NOT_SET = 0x0,
};

```
#### com::mojang::clacks::protocol::PlayerType : __int32
```cpp
/* 7921 */
enum com::mojang::clacks::protocol::PlayerType : __int32
{
PRIMARY_PLAYER = 0x0,
SPLIT_SCREEN_PLAYER = 0x1,
PlayerType_INT_MIN_SENTINEL_DO_NOT_USE_ = 0x80000000,
PlayerType_INT_MAX_SENTINEL_DO_NOT_USE_ = 0x7FFFFFFF,
};

```
#### com::mojang::clacks::protocol::SaveState : __int32
```cpp
/* 7402 */
enum com::mojang::clacks::protocol::SaveState : __int32
{
IDLE = 0x0,
SAVING = 0x1,
COMPLETE = 0x2,
SaveState_INT_MIN_SENTINEL_DO_NOT_USE_ = 0x80000000,
SaveState_INT_MAX_SENTINEL_DO_NOT_USE_ = 0x7FFFFFFF,
};

```
#### com::mojang::clacks::protocol::Settings::SettingsCase : __int32
```cpp
/* 7922 */
enum com::mojang::clacks::protocol::Settings::SettingsCase : __int32
{
kDifficultySetting = 0x1,
kCheatsSetting = 0x2,
SETTINGS_NOT_SET = 0x0,
};

```
#### glm::ctor : __int32
```cpp
/* 5600 */
enum glm::ctor : __int32
{
uninitialize = 0x0,
};

```
#### glm::precision : __int32
```cpp
/* 5599 */
enum glm::precision : __int32
{
packed_highp = 0x0,
packed_mediump = 0x1,
packed_lowp = 0x2,
aligned_highp = 0x3,
aligned_mediump = 0x4,
aligned_lowp = 0x5,
aligned = 0x3,
highp = 0x0,
mediump = 0x1,
lowp = 0x2,
packed = 0x0,
defaultp = 0x0,
};

```
#### google_breakpad::MinidumpDescriptor::DumpMode : __int32
```cpp
/* 294187 */
enum google_breakpad::MinidumpDescriptor::DumpMode : __int32
{
kUninitialized = 0x0,
kWriteMinidumpToFile = 0x1,
kWriteMinidumpToFd = 0x2,
kWriteMicrodumpToConsole = 0x3,
};

```
#### google_breakpad::TypedMDRVA<MDRawContextAMD64>::AllocationState : __int32
```cpp
/* 485791 */
enum google_breakpad::TypedMDRVA<MDRawContextAMD64>::AllocationState : __int32
{
UNALLOCATED_2 = 0x0,
SINGLE_OBJECT_2 = 0x1,
ARRAY_2 = 0x2,
SINGLE_OBJECT_WITH_ARRAY_2 = 0x3,
};

```
#### google_breakpad::TypedMDRVA<MDRawDebug64>::AllocationState : __int32
```cpp
/* 485807 */
enum google_breakpad::TypedMDRVA<MDRawDebug64>::AllocationState : __int32
{
UNALLOCATED_6 = 0x0,
SINGLE_OBJECT_6 = 0x1,
ARRAY_6 = 0x2,
SINGLE_OBJECT_WITH_ARRAY_6 = 0x3,
};

```
#### google_breakpad::TypedMDRVA<MDRawDirectory>::AllocationState : __int32
```cpp
/* 485779 */
enum google_breakpad::TypedMDRVA<MDRawDirectory>::AllocationState : __int32
{
UNALLOCATED = 0x0,
SINGLE_OBJECT = 0x1,
ARRAY = 0x2,
SINGLE_OBJECT_WITH_ARRAY = 0x3,
};

```
#### google_breakpad::TypedMDRVA<MDRawExceptionStream>::AllocationState : __int32
```cpp
/* 485795 */
enum google_breakpad::TypedMDRVA<MDRawExceptionStream>::AllocationState : __int32
{
UNALLOCATED_3 = 0x0,
SINGLE_OBJECT_3 = 0x1,
ARRAY_3 = 0x2,
SINGLE_OBJECT_WITH_ARRAY_3 = 0x3,
};

```
#### google_breakpad::TypedMDRVA<MDRawHeader>::AllocationState : __int32
```cpp
/* 485782 */
enum google_breakpad::TypedMDRVA<MDRawHeader>::AllocationState : __int32
{
UNALLOCATED_0 = 0x0,
SINGLE_OBJECT_0 = 0x1,
ARRAY_0 = 0x2,
SINGLE_OBJECT_WITH_ARRAY_0 = 0x3,
};

```
#### google_breakpad::TypedMDRVA<MDRawLinkMap64>::AllocationState : __int32
```cpp
/* 485804 */
enum google_breakpad::TypedMDRVA<MDRawLinkMap64>::AllocationState : __int32
{
UNALLOCATED_5 = 0x0,
SINGLE_OBJECT_5 = 0x1,
ARRAY_5 = 0x2,
SINGLE_OBJECT_WITH_ARRAY_5 = 0x3,
};

```
#### google_breakpad::TypedMDRVA<MDRawSystemInfo>::AllocationState : __int32
```cpp
/* 485802 */
enum google_breakpad::TypedMDRVA<MDRawSystemInfo>::AllocationState : __int32
{
UNALLOCATED_4 = 0x0,
SINGLE_OBJECT_4 = 0x1,
ARRAY_4 = 0x2,
SINGLE_OBJECT_WITH_ARRAY_4 = 0x3,
};

```
#### google_breakpad::TypedMDRVA<MDString>::AllocationState : __int32
```cpp
/* 486268 */
enum google_breakpad::TypedMDRVA<MDString>::AllocationState : __int32
{
UNALLOCATED_7 = 0x0,
SINGLE_OBJECT_7 = 0x1,
ARRAY_7 = 0x2,
SINGLE_OBJECT_WITH_ARRAY_7 = 0x3,
};

```
#### google_breakpad::TypedMDRVA<unsigned int>::AllocationState : __int32
```cpp
/* 485784 */
enum google_breakpad::TypedMDRVA<unsigned int>::AllocationState : __int32
{
UNALLOCATED_1 = 0x0,
SINGLE_OBJECT_1 = 0x1,
ARRAY_1 = 0x2,
SINGLE_OBJECT_WITH_ARRAY_1 = 0x3,
};

```
#### gpr_clock_type : __int32
```cpp
/* 7946 */
enum gpr_clock_type : __int32
{
GPR_CLOCK_MONOTONIC = 0x0,
GPR_CLOCK_REALTIME = 0x1,
GPR_CLOCK_PRECISE = 0x2,
GPR_TIMESPAN = 0x3,
};

```
#### grpc_byte_buffer_type : __int32
```cpp
/* 8926 */
enum grpc_byte_buffer_type : __int32
{
GRPC_BB_RAW = 0x0,
};

```
#### grpc_call_error : __int32
```cpp
/* 9432 */
enum grpc_call_error : __int32
{
GRPC_CALL_OK = 0x0,
GRPC_CALL_ERROR = 0x1,
GRPC_CALL_ERROR_NOT_ON_SERVER = 0x2,
GRPC_CALL_ERROR_NOT_ON_CLIENT = 0x3,
GRPC_CALL_ERROR_ALREADY_ACCEPTED = 0x4,
GRPC_CALL_ERROR_ALREADY_INVOKED = 0x5,
GRPC_CALL_ERROR_NOT_INVOKED = 0x6,
GRPC_CALL_ERROR_ALREADY_FINISHED = 0x7,
GRPC_CALL_ERROR_TOO_MANY_OPERATIONS = 0x8,
GRPC_CALL_ERROR_INVALID_FLAGS = 0x9,
GRPC_CALL_ERROR_INVALID_METADATA = 0xA,
GRPC_CALL_ERROR_INVALID_MESSAGE = 0xB,
GRPC_CALL_ERROR_NOT_SERVER_COMPLETION_QUEUE = 0xC,
GRPC_CALL_ERROR_BATCH_TOO_BIG = 0xD,
GRPC_CALL_ERROR_PAYLOAD_TYPE_MISMATCH = 0xE,
GRPC_CALL_ERROR_COMPLETION_QUEUE_SHUTDOWN = 0xF,
};

```
#### grpc_completion_type : __int32
```cpp
/* 9433 */
enum grpc_completion_type : __int32
{
GRPC_QUEUE_SHUTDOWN = 0x0,
GRPC_QUEUE_TIMEOUT = 0x1,
GRPC_OP_COMPLETE = 0x2,
};

```
#### grpc_compression_algorithm : __int32
```cpp
/* 7960 */
enum grpc_compression_algorithm : __int32
{
GRPC_COMPRESS_NONE = 0x0,
GRPC_COMPRESS_DEFLATE = 0x1,
GRPC_COMPRESS_GZIP = 0x2,
GRPC_COMPRESS_STREAM_GZIP = 0x3,
GRPC_COMPRESS_ALGORITHMS_COUNT = 0x4,
};

```
#### grpc_compression_level : __int32
```cpp
/* 7959 */
enum grpc_compression_level : __int32
{
GRPC_COMPRESS_LEVEL_NONE = 0x0,
GRPC_COMPRESS_LEVEL_LOW = 0x1,
GRPC_COMPRESS_LEVEL_MED = 0x2,
GRPC_COMPRESS_LEVEL_HIGH = 0x3,
GRPC_COMPRESS_LEVEL_COUNT = 0x4,
};

```
#### grpc_connectivity_state : __int32
```cpp
/* 9418 */
enum grpc_connectivity_state : __int32
{
GRPC_CHANNEL_IDLE = 0x0,
GRPC_CHANNEL_CONNECTING = 0x1,
GRPC_CHANNEL_READY = 0x2,
GRPC_CHANNEL_TRANSIENT_FAILURE = 0x3,
GRPC_CHANNEL_SHUTDOWN = 0x4,
};

```
#### grpc_cq_completion_type : __int32
```cpp
/* 9404 */
enum grpc_cq_completion_type : __int32
{
GRPC_CQ_NEXT = 0x0,
GRPC_CQ_PLUCK = 0x1,
GRPC_CQ_CALLBACK = 0x2,
};

```
#### grpc_cq_polling_type : __int32
```cpp
/* 9405 */
enum grpc_cq_polling_type : __int32
{
GRPC_CQ_DEFAULT_POLLING = 0x0,
GRPC_CQ_NON_LISTENING = 0x1,
GRPC_CQ_NON_POLLING = 0x2,
};

```
#### grpc_op_type : __int32
```cpp
/* 9421 */
enum grpc_op_type : __int32
{
GRPC_OP_SEND_INITIAL_METADATA = 0x0,
GRPC_OP_SEND_MESSAGE = 0x1,
GRPC_OP_SEND_CLOSE_FROM_CLIENT = 0x2,
GRPC_OP_SEND_STATUS_FROM_SERVER = 0x3,
GRPC_OP_RECV_INITIAL_METADATA = 0x4,
GRPC_OP_RECV_MESSAGE = 0x5,
GRPC_OP_RECV_STATUS_ON_CLIENT = 0x6,
GRPC_OP_RECV_CLOSE_ON_SERVER = 0x7,
};

```
#### grpc_status_code : __int32
```cpp
/* 8936 */
enum grpc_status_code : __int32
{
GRPC_STATUS_OK = 0x0,
GRPC_STATUS_CANCELLED = 0x1,
GRPC_STATUS_UNKNOWN = 0x2,
GRPC_STATUS_INVALID_ARGUMENT = 0x3,
GRPC_STATUS_DEADLINE_EXCEEDED = 0x4,
GRPC_STATUS_NOT_FOUND = 0x5,
GRPC_STATUS_ALREADY_EXISTS = 0x6,
GRPC_STATUS_PERMISSION_DENIED = 0x7,
GRPC_STATUS_UNAUTHENTICATED = 0x10,
GRPC_STATUS_RESOURCE_EXHAUSTED = 0x8,
GRPC_STATUS_FAILED_PRECONDITION = 0x9,
GRPC_STATUS_ABORTED = 0xA,
GRPC_STATUS_OUT_OF_RANGE = 0xB,
GRPC_STATUS_UNIMPLEMENTED = 0xC,
GRPC_STATUS_INTERNAL = 0xD,
GRPC_STATUS_UNAVAILABLE = 0xE,
GRPC_STATUS_DATA_LOSS = 0xF,
GRPC_STATUS__DO_NOT_USE = 0xFFFFFFFF,
};

```
#### mce::ImageFormat : __int32
```cpp
/* 74241 */
enum mce::ImageFormat : __int32
{
Unknown_27 = 0x0,
RGB8Unorm = 0x1,
RGBA8Unorm = 0x2,
};

```
#### mce::ImageUsage : __int8
```cpp
/* 74242 */
enum mce::ImageUsage : __int8
{
};

```
#### mce::ImageUsage_0 : __int8
```cpp
/* 173108 */
enum mce::ImageUsage_0 : __int8
{
Unknown_41 = 0x0,
sRGB = 0x1,
Data_0 = 0x2,
};

```
#### mce::TextureFormat : __int32
```cpp
/* 457061 */
enum mce::TextureFormat : __int32
{
};

```
#### persona::AnimatedTextureType : __int32
```cpp
/* 74258 */
enum persona::AnimatedTextureType : __int32
{
None_24 = 0x0,
Face = 0x1,
Body32x32 = 0x2,
Body128x128 = 0x3,
};

```
#### persona::PersonaError : __int32
```cpp
/* 171755 */
enum persona::PersonaError : __int32
{
NoError_0 = 0x0,
ItemSelection = 0x1,
InvalidPersona = 0x3,
LoadingAppearanceTimeOut = 0x4,
};

```
#### persona::PieceSubType : __int32
```cpp
/* 171595 */
enum persona::PieceSubType : __int32
{
Unknown_40 = 0x0,
None_45 = 0x1,
Cape = 0x2,
Complexion = 0x3,
Count_23 = 0x4,
};

```
#### persona::PieceType : __int32
```cpp
/* 73850 */
enum persona::PieceType : __int32
{
Unknown_26 = 0x0,
Skeleton_0 = 0x1,
Body_0 = 0x2,
Skin = 0x3,
Bottom = 0x4,
Feet_1 = 0x5,
Dress = 0x6,
Top = 0x7,
High_Pants = 0x8,
Hands_0 = 0x9,
Outerwear = 0xA,
Back = 0xB,
FacialHair = 0xC,
Mouth_0 = 0xD,
Eyes_0 = 0xE,
Hair = 0xF,
FaceAccessory = 0x10,
Head_1 = 0x11,
Legs_0 = 0x12,
LeftLeg = 0x13,
RightLeg = 0x14,
Arms = 0x15,
LeftArm = 0x16,
RightArm = 0x17,
Capes = 0x18,
ClassicSkin = 0x19,
Count_12 = 0x1A,
};

```
#### persona::ProfileType : __int32
```cpp
/* 171437 */
enum persona::ProfileType : __int32
{
Legacy_0 = 0x0,
Persona1 = 0x1,
Persona2 = 0x2,
Persona3 = 0x3,
Persona4 = 0x4,
Persona5 = 0x5,
COUNT_10 = 0x6,
NOT_FOUND_0 = 0x7,
CUSTOM_0 = 0x8,
};

```
#### persona::Rarity : __int8
```cpp
/* 171675 */
enum persona::Rarity : __int8
{
None_46 = 0x0,
Common = 0x1,
Uncommon = 0x2,
Rare = 0x3,
Epic = 0x4,
Legendary = 0x5,
};

```
#### r_debug::$779A3ED0FCC279D8F3DE0A4A7B5F9A6A : __int32
```cpp
/* 486215 */
enum r_debug::$779A3ED0FCC279D8F3DE0A4A7B5F9A6A : __int32
{
RT_CONSISTENT = 0x0,
RT_ADD = 0x1,
RT_DELETE = 0x2,
};

```
#### typeid_t<CommandRegistry>::NewIDType : __int32
```cpp
/* 5679 */
enum typeid_t<CommandRegistry>::NewIDType : __int32
{
New = 0x0,
};

```
#### typeid_t<ContextAccessor>::NewIDType : __int32
```cpp
/* 421008 */
enum typeid_t<ContextAccessor>::NewIDType : __int32
{
New_3 = 0x0,
};

```
#### typeid_t<IDefinitionInstance>::NewIDType : __int32
```cpp
/* 48665 */
enum typeid_t<IDefinitionInstance>::NewIDType : __int32
{
New_0 = 0x0,
};

```
#### typeid_t<ScriptBinderComponent>::NewIDType : __int32
```cpp
/* 99879 */
enum typeid_t<ScriptBinderComponent>::NewIDType : __int32
{
New_2 = 0x0,
};

```
#### $1210F371E758421EF368DC19A231A6DA : __int32
```cpp
/* 478100 */
enum $1210F371E758421EF368DC19A231A6DA : __int32
{
IFF_UP = 0x1,
IFF_BROADCAST = 0x2,
IFF_DEBUG = 0x4,
IFF_LOOPBACK = 0x8,
IFF_POINTOPOINT = 0x10,
IFF_NOTRAILERS = 0x20,
IFF_RUNNING = 0x40,
IFF_NOARP = 0x80,
IFF_PROMISC = 0x100,
IFF_ALLMULTI = 0x200,
IFF_MASTER = 0x400,
IFF_SLAVE = 0x800,
IFF_MULTICAST = 0x1000,
IFF_PORTSEL = 0x2000,
IFF_AUTOMEDIA = 0x4000,
IFF_DYNAMIC = 0x8000,
};

```
#### $347C4AA96D10B0B03CED8E04011C7660 : __int32
```cpp
/* 486312 */
enum $347C4AA96D10B0B03CED8E04011C7660 : __int32
{
strictConversion = 0x0,
lenientConversion = 0x1,
};

```
#### $3D49817EA999CD8B3DC48DB74CFF9164 : __int32
```cpp
/* 486207 */
enum $3D49817EA999CD8B3DC48DB74CFF9164 : __int32
{
MD_OS_WIN32S = 0x0,
MD_OS_WIN32_WINDOWS = 0x1,
MD_OS_WIN32_NT = 0x2,
MD_OS_WIN32_CE = 0x3,
MD_OS_UNIX = 0x8000,
MD_OS_MAC_OS_X = 0x8101,
MD_OS_IOS = 0x8102,
MD_OS_LINUX = 0x8201,
MD_OS_SOLARIS = 0x8202,
MD_OS_ANDROID = 0x8203,
MD_OS_PS3 = 0x8204,
MD_OS_NACL = 0x8205,
};

```
#### $4AC4411A22C6C9FCB976BEA19FD29F1E : __int32
```cpp
/* 485728 */
enum $4AC4411A22C6C9FCB976BEA19FD29F1E : __int32
{
MD_EXCEPTION_CODE_LIN_SIGHUP = 0x1,
MD_EXCEPTION_CODE_LIN_SIGINT = 0x2,
MD_EXCEPTION_CODE_LIN_SIGQUIT = 0x3,
MD_EXCEPTION_CODE_LIN_SIGILL = 0x4,
MD_EXCEPTION_CODE_LIN_SIGTRAP = 0x5,
MD_EXCEPTION_CODE_LIN_SIGABRT = 0x6,
MD_EXCEPTION_CODE_LIN_SIGBUS = 0x7,
MD_EXCEPTION_CODE_LIN_SIGFPE = 0x8,
MD_EXCEPTION_CODE_LIN_SIGKILL = 0x9,
MD_EXCEPTION_CODE_LIN_SIGUSR1 = 0xA,
MD_EXCEPTION_CODE_LIN_SIGSEGV = 0xB,
MD_EXCEPTION_CODE_LIN_SIGUSR2 = 0xC,
MD_EXCEPTION_CODE_LIN_SIGPIPE = 0xD,
MD_EXCEPTION_CODE_LIN_SIGALRM = 0xE,
MD_EXCEPTION_CODE_LIN_SIGTERM = 0xF,
MD_EXCEPTION_CODE_LIN_SIGSTKFLT = 0x10,
MD_EXCEPTION_CODE_LIN_SIGCHLD = 0x11,
MD_EXCEPTION_CODE_LIN_SIGCONT = 0x12,
MD_EXCEPTION_CODE_LIN_SIGSTOP = 0x13,
MD_EXCEPTION_CODE_LIN_SIGTSTP = 0x14,
MD_EXCEPTION_CODE_LIN_SIGTTIN = 0x15,
MD_EXCEPTION_CODE_LIN_SIGTTOU = 0x16,
MD_EXCEPTION_CODE_LIN_SIGURG = 0x17,
MD_EXCEPTION_CODE_LIN_SIGXCPU = 0x18,
MD_EXCEPTION_CODE_LIN_SIGXFSZ = 0x19,
MD_EXCEPTION_CODE_LIN_SIGVTALRM = 0x1A,
MD_EXCEPTION_CODE_LIN_SIGPROF = 0x1B,
MD_EXCEPTION_CODE_LIN_SIGWINCH = 0x1C,
MD_EXCEPTION_CODE_LIN_SIGIO = 0x1D,
MD_EXCEPTION_CODE_LIN_SIGPWR = 0x1E,
MD_EXCEPTION_CODE_LIN_SIGSYS = 0x1F,
MD_EXCEPTION_CODE_LIN_DUMP_REQUESTED = 0xFFFFFFFF,
};

```
#### $56C97545D8191E8EE2F000856B97BA17 : __int32
```cpp
/* 485729 */
enum $56C97545D8191E8EE2F000856B97BA17 : __int32
{
REG_R8 = 0x0,
REG_R9 = 0x1,
REG_R10 = 0x2,
REG_R11 = 0x3,
REG_R12 = 0x4,
REG_R13 = 0x5,
REG_R14 = 0x6,
REG_R15 = 0x7,
REG_RDI = 0x8,
REG_RSI = 0x9,
REG_RBP = 0xA,
REG_RBX = 0xB,
REG_RDX = 0xC,
REG_RAX = 0xD,
REG_RCX = 0xE,
REG_RSP = 0xF,
REG_RIP = 0x10,
REG_EFL = 0x11,
REG_CSGSFS = 0x12,
REG_ERR = 0x13,
REG_TRAPNO = 0x14,
REG_OLDMASK = 0x15,
REG_CR2 = 0x16,
};

```
#### $7DA0ED1C510EB8BBF6F0B878F549FC50 : __int32
```cpp
/* 294341 */
enum $7DA0ED1C510EB8BBF6F0B878F549FC50 : __int32
{
IPPROTO_IP = 0x0,
IPPROTO_ICMP = 0x1,
IPPROTO_IGMP = 0x2,
IPPROTO_IPIP = 0x4,
IPPROTO_TCP = 0x6,
IPPROTO_EGP = 0x8,
IPPROTO_PUP = 0xC,
IPPROTO_UDP = 0x11,
IPPROTO_IDP = 0x16,
IPPROTO_TP = 0x1D,
IPPROTO_DCCP = 0x21,
IPPROTO_IPV6 = 0x29,
IPPROTO_RSVP = 0x2E,
IPPROTO_GRE = 0x2F,
IPPROTO_ESP = 0x32,
IPPROTO_AH = 0x33,
IPPROTO_MTP = 0x5C,
IPPROTO_BEETPH = 0x5E,
IPPROTO_ENCAP = 0x62,
IPPROTO_PIM = 0x67,
IPPROTO_COMP = 0x6C,
IPPROTO_SCTP = 0x84,
IPPROTO_UDPLITE = 0x88,
IPPROTO_MPLS = 0x89,
IPPROTO_RAW = 0xFF,
IPPROTO_MAX = 0x100,
};

```
#### $806B9BA87CC87D12CA732A028B794533 : __int32
```cpp
/* 42802 */
enum $806B9BA87CC87D12CA732A028B794533 : __int32
{
_SC_ARG_MAX = 0x0,
_SC_CHILD_MAX = 0x1,
_SC_CLK_TCK = 0x2,
_SC_NGROUPS_MAX = 0x3,
_SC_OPEN_MAX = 0x4,
_SC_STREAM_MAX = 0x5,
_SC_TZNAME_MAX = 0x6,
_SC_JOB_CONTROL = 0x7,
_SC_SAVED_IDS = 0x8,
_SC_REALTIME_SIGNALS = 0x9,
_SC_PRIORITY_SCHEDULING = 0xA,
_SC_TIMERS = 0xB,
_SC_ASYNCHRONOUS_IO = 0xC,
_SC_PRIORITIZED_IO = 0xD,
_SC_SYNCHRONIZED_IO = 0xE,
_SC_FSYNC = 0xF,
_SC_MAPPED_FILES = 0x10,
_SC_MEMLOCK = 0x11,
_SC_MEMLOCK_RANGE = 0x12,
_SC_MEMORY_PROTECTION = 0x13,
_SC_MESSAGE_PASSING = 0x14,
_SC_SEMAPHORES = 0x15,
_SC_SHARED_MEMORY_OBJECTS = 0x16,
_SC_AIO_LISTIO_MAX = 0x17,
_SC_AIO_MAX = 0x18,
_SC_AIO_PRIO_DELTA_MAX = 0x19,
_SC_DELAYTIMER_MAX = 0x1A,
_SC_MQ_OPEN_MAX = 0x1B,
_SC_MQ_PRIO_MAX = 0x1C,
_SC_VERSION = 0x1D,
_SC_PAGESIZE = 0x1E,
_SC_RTSIG_MAX = 0x1F,
_SC_SEM_NSEMS_MAX = 0x20,
_SC_SEM_VALUE_MAX = 0x21,
_SC_SIGQUEUE_MAX = 0x22,
_SC_TIMER_MAX = 0x23,
_SC_BC_BASE_MAX = 0x24,
_SC_BC_DIM_MAX = 0x25,
_SC_BC_SCALE_MAX = 0x26,
_SC_BC_STRING_MAX = 0x27,
_SC_COLL_WEIGHTS_MAX = 0x28,
_SC_EQUIV_CLASS_MAX = 0x29,
_SC_EXPR_NEST_MAX = 0x2A,
_SC_LINE_MAX = 0x2B,
_SC_RE_DUP_MAX = 0x2C,
_SC_CHARCLASS_NAME_MAX = 0x2D,
_SC_2_VERSION = 0x2E,
_SC_2_C_BIND = 0x2F,
_SC_2_C_DEV = 0x30,
_SC_2_FORT_DEV = 0x31,
_SC_2_FORT_RUN = 0x32,
_SC_2_SW_DEV = 0x33,
_SC_2_LOCALEDEF = 0x34,
_SC_PII = 0x35,
_SC_PII_XTI = 0x36,
_SC_PII_SOCKET = 0x37,
_SC_PII_INTERNET = 0x38,
_SC_PII_OSI = 0x39,
_SC_POLL = 0x3A,
_SC_SELECT = 0x3B,
_SC_UIO_MAXIOV = 0x3C,
_SC_IOV_MAX = 0x3C,
_SC_PII_INTERNET_STREAM = 0x3D,
_SC_PII_INTERNET_DGRAM = 0x3E,
_SC_PII_OSI_COTS = 0x3F,
_SC_PII_OSI_CLTS = 0x40,
_SC_PII_OSI_M = 0x41,
_SC_T_IOV_MAX = 0x42,
_SC_THREADS = 0x43,
_SC_THREAD_SAFE_FUNCTIONS = 0x44,
_SC_GETGR_R_SIZE_MAX = 0x45,
_SC_GETPW_R_SIZE_MAX = 0x46,
_SC_LOGIN_NAME_MAX = 0x47,
_SC_TTY_NAME_MAX = 0x48,
_SC_THREAD_DESTRUCTOR_ITERATIONS = 0x49,
_SC_THREAD_KEYS_MAX = 0x4A,
_SC_THREAD_STACK_MIN = 0x4B,
_SC_THREAD_THREADS_MAX = 0x4C,
_SC_THREAD_ATTR_STACKADDR = 0x4D,
_SC_THREAD_ATTR_STACKSIZE = 0x4E,
_SC_THREAD_PRIORITY_SCHEDULING = 0x4F,
_SC_THREAD_PRIO_INHERIT = 0x50,
_SC_THREAD_PRIO_PROTECT = 0x51,
_SC_THREAD_PROCESS_SHARED = 0x52,
_SC_NPROCESSORS_CONF = 0x53,
_SC_NPROCESSORS_ONLN = 0x54,
_SC_PHYS_PAGES = 0x55,
_SC_AVPHYS_PAGES = 0x56,
_SC_ATEXIT_MAX = 0x57,
_SC_PASS_MAX = 0x58,
_SC_XOPEN_VERSION = 0x59,
_SC_XOPEN_XCU_VERSION = 0x5A,
_SC_XOPEN_UNIX = 0x5B,
_SC_XOPEN_CRYPT = 0x5C,
_SC_XOPEN_ENH_I18N = 0x5D,
_SC_XOPEN_SHM = 0x5E,
_SC_2_CHAR_TERM = 0x5F,
_SC_2_C_VERSION = 0x60,
_SC_2_UPE = 0x61,
_SC_XOPEN_XPG2 = 0x62,
_SC_XOPEN_XPG3 = 0x63,
_SC_XOPEN_XPG4 = 0x64,
_SC_CHAR_BIT = 0x65,
_SC_CHAR_MAX = 0x66,
_SC_CHAR_MIN = 0x67,
_SC_INT_MAX = 0x68,
_SC_INT_MIN = 0x69,
_SC_LONG_BIT = 0x6A,
_SC_WORD_BIT = 0x6B,
_SC_MB_LEN_MAX = 0x6C,
_SC_NZERO = 0x6D,
_SC_SSIZE_MAX = 0x6E,
_SC_SCHAR_MAX = 0x6F,
_SC_SCHAR_MIN = 0x70,
_SC_SHRT_MAX = 0x71,
_SC_SHRT_MIN = 0x72,
_SC_UCHAR_MAX = 0x73,
_SC_UINT_MAX = 0x74,
_SC_ULONG_MAX = 0x75,
_SC_USHRT_MAX = 0x76,
_SC_NL_ARGMAX = 0x77,
_SC_NL_LANGMAX = 0x78,
_SC_NL_MSGMAX = 0x79,
_SC_NL_NMAX = 0x7A,
_SC_NL_SETMAX = 0x7B,
_SC_NL_TEXTMAX = 0x7C,
_SC_XBS5_ILP32_OFF32 = 0x7D,
_SC_XBS5_ILP32_OFFBIG = 0x7E,
_SC_XBS5_LP64_OFF64 = 0x7F,
_SC_XBS5_LPBIG_OFFBIG = 0x80,
_SC_XOPEN_LEGACY = 0x81,
_SC_XOPEN_REALTIME = 0x82,
_SC_XOPEN_REALTIME_THREADS = 0x83,
_SC_ADVISORY_INFO = 0x84,
_SC_BARRIERS = 0x85,
_SC_BASE = 0x86,
_SC_C_LANG_SUPPORT = 0x87,
_SC_C_LANG_SUPPORT_R = 0x88,
_SC_CLOCK_SELECTION = 0x89,
_SC_CPUTIME = 0x8A,
_SC_THREAD_CPUTIME = 0x8B,
_SC_DEVICE_IO = 0x8C,
_SC_DEVICE_SPECIFIC = 0x8D,
_SC_DEVICE_SPECIFIC_R = 0x8E,
_SC_FD_MGMT = 0x8F,
_SC_FIFO = 0x90,
_SC_PIPE = 0x91,
_SC_FILE_ATTRIBUTES = 0x92,
_SC_FILE_LOCKING = 0x93,
_SC_FILE_SYSTEM = 0x94,
_SC_MONOTONIC_CLOCK = 0x95,
_SC_MULTI_PROCESS = 0x96,
_SC_SINGLE_PROCESS = 0x97,
_SC_NETWORKING = 0x98,
_SC_READER_WRITER_LOCKS = 0x99,
_SC_SPIN_LOCKS = 0x9A,
_SC_REGEXP = 0x9B,
_SC_REGEX_VERSION = 0x9C,
_SC_SHELL = 0x9D,
_SC_SIGNALS = 0x9E,
_SC_SPAWN = 0x9F,
_SC_SPORADIC_SERVER = 0xA0,
_SC_THREAD_SPORADIC_SERVER = 0xA1,
_SC_SYSTEM_DATABASE = 0xA2,
_SC_SYSTEM_DATABASE_R = 0xA3,
_SC_TIMEOUTS = 0xA4,
_SC_TYPED_MEMORY_OBJECTS = 0xA5,
_SC_USER_GROUPS = 0xA6,
_SC_USER_GROUPS_R = 0xA7,
_SC_2_PBS = 0xA8,
_SC_2_PBS_ACCOUNTING = 0xA9,
_SC_2_PBS_LOCATE = 0xAA,
_SC_2_PBS_MESSAGE = 0xAB,
_SC_2_PBS_TRACK = 0xAC,
_SC_SYMLOOP_MAX = 0xAD,
_SC_STREAMS = 0xAE,
_SC_2_PBS_CHECKPOINT = 0xAF,
_SC_V6_ILP32_OFF32 = 0xB0,
_SC_V6_ILP32_OFFBIG = 0xB1,
_SC_V6_LP64_OFF64 = 0xB2,
_SC_V6_LPBIG_OFFBIG = 0xB3,
_SC_HOST_NAME_MAX = 0xB4,
_SC_TRACE = 0xB5,
_SC_TRACE_EVENT_FILTER = 0xB6,
_SC_TRACE_INHERIT = 0xB7,
_SC_TRACE_LOG = 0xB8,
_SC_LEVEL1_ICACHE_SIZE = 0xB9,
_SC_LEVEL1_ICACHE_ASSOC = 0xBA,
_SC_LEVEL1_ICACHE_LINESIZE = 0xBB,
_SC_LEVEL1_DCACHE_SIZE = 0xBC,
_SC_LEVEL1_DCACHE_ASSOC = 0xBD,
_SC_LEVEL1_DCACHE_LINESIZE = 0xBE,
_SC_LEVEL2_CACHE_SIZE = 0xBF,
_SC_LEVEL2_CACHE_ASSOC = 0xC0,
_SC_LEVEL2_CACHE_LINESIZE = 0xC1,
_SC_LEVEL3_CACHE_SIZE = 0xC2,
_SC_LEVEL3_CACHE_ASSOC = 0xC3,
_SC_LEVEL3_CACHE_LINESIZE = 0xC4,
_SC_LEVEL4_CACHE_SIZE = 0xC5,
_SC_LEVEL4_CACHE_ASSOC = 0xC6,
_SC_LEVEL4_CACHE_LINESIZE = 0xC7,
_SC_IPV6 = 0xEB,
_SC_RAW_SOCKETS = 0xEC,
_SC_V7_ILP32_OFF32 = 0xED,
_SC_V7_ILP32_OFFBIG = 0xEE,
_SC_V7_LP64_OFF64 = 0xEF,
_SC_V7_LPBIG_OFFBIG = 0xF0,
_SC_SS_REPL_MAX = 0xF1,
_SC_TRACE_EVENT_NAME_MAX = 0xF2,
_SC_TRACE_NAME_MAX = 0xF3,
_SC_TRACE_SYS_MAX = 0xF4,
_SC_TRACE_USER_EVENT_MAX = 0xF5,
_SC_XOPEN_STREAMS = 0xF6,
_SC_THREAD_ROBUST_PRIO_INHERIT = 0xF7,
_SC_THREAD_ROBUST_PRIO_PROTECT = 0xF8,
};

```
#### $8B0F52549CE761034392E15FD5290A77 : __int32
```cpp
/* 486205 */
enum $8B0F52549CE761034392E15FD5290A77 : __int32
{
MD_UNUSED_STREAM = 0x0,
MD_RESERVED_STREAM_0 = 0x1,
MD_RESERVED_STREAM_1 = 0x2,
MD_THREAD_LIST_STREAM = 0x3,
MD_MODULE_LIST_STREAM = 0x4,
MD_MEMORY_LIST_STREAM = 0x5,
MD_EXCEPTION_STREAM = 0x6,
MD_SYSTEM_INFO_STREAM = 0x7,
MD_THREAD_EX_LIST_STREAM = 0x8,
MD_MEMORY_64_LIST_STREAM = 0x9,
MD_COMMENT_STREAM_A = 0xA,
MD_COMMENT_STREAM_W = 0xB,
MD_HANDLE_DATA_STREAM = 0xC,
MD_FUNCTION_TABLE_STREAM = 0xD,
MD_UNLOADED_MODULE_LIST_STREAM = 0xE,
MD_MISC_INFO_STREAM = 0xF,
MD_MEMORY_INFO_LIST_STREAM = 0x10,
MD_THREAD_INFO_LIST_STREAM = 0x11,
MD_HANDLE_OPERATION_LIST_STREAM = 0x12,
MD_TOKEN_STREAM = 0x13,
MD_JAVASCRIPT_DATA_STREAM = 0x14,
MD_SYSTEM_MEMORY_INFO_STREAM = 0x15,
MD_PROCESS_VM_COUNTERS_STREAM = 0x16,
MD_LAST_RESERVED_STREAM = 0xFFFF,
MD_BREAKPAD_INFO_STREAM = 0x47670001,
MD_ASSERTION_INFO_STREAM = 0x47670002,
MD_LINUX_CPU_INFO = 0x47670003,
MD_LINUX_PROC_STATUS = 0x47670004,
MD_LINUX_LSB_RELEASE = 0x47670005,
MD_LINUX_CMD_LINE = 0x47670006,
MD_LINUX_ENVIRON = 0x47670007,
MD_LINUX_AUXV = 0x47670008,
MD_LINUX_MAPS = 0x47670009,
MD_LINUX_DSO_DEBUG = 0x4767000A,
};

```
#### $921DADCB212321B7AEB7DFA289997804 : __int32
```cpp
/* 486206 */
enum $921DADCB212321B7AEB7DFA289997804 : __int32
{
MD_CPU_ARCHITECTURE_X86 = 0x0,
MD_CPU_ARCHITECTURE_MIPS = 0x1,
MD_CPU_ARCHITECTURE_ALPHA = 0x2,
MD_CPU_ARCHITECTURE_PPC = 0x3,
MD_CPU_ARCHITECTURE_SHX = 0x4,
MD_CPU_ARCHITECTURE_ARM = 0x5,
MD_CPU_ARCHITECTURE_IA64 = 0x6,
MD_CPU_ARCHITECTURE_ALPHA64 = 0x7,
MD_CPU_ARCHITECTURE_MSIL = 0x8,
MD_CPU_ARCHITECTURE_AMD64 = 0x9,
MD_CPU_ARCHITECTURE_X86_WIN64 = 0xA,
MD_CPU_ARCHITECTURE_SPARC = 0x8001,
MD_CPU_ARCHITECTURE_PPC64 = 0x8002,
MD_CPU_ARCHITECTURE_ARM64 = 0x8003,
MD_CPU_ARCHITECTURE_MIPS64 = 0x8004,
MD_CPU_ARCHITECTURE_UNKNOWN = 0xFFFF,
};

```
#### $9C6F2EC01E3BBF5B0C7567BE63B52E63 : __int32
```cpp
/* 485737 */
enum $9C6F2EC01E3BBF5B0C7567BE63B52E63 : __int32
{
SCM_RIGHTS = 0x1,
SCM_CREDENTIALS = 0x2,
};

```
#### $ACDD07C6EE62D6CF0A2EDB2FA1B08CD2 : __int32
```cpp
/* 478120 */
enum $ACDD07C6EE62D6CF0A2EDB2FA1B08CD2 : __int32
{
SHUT_RD = 0x0,
SHUT_WR = 0x1,
SHUT_RDWR = 0x2,
};

```
#### $B829A033D76A0B72BA0F6DE5FA2A0558 : __int32
```cpp
/* 485727 */
enum $B829A033D76A0B72BA0F6DE5FA2A0558 : __int32
{
SI_ASYNCNL = 0xFFFFFFC4,
SI_TKILL = 0xFFFFFFFA,
SI_SIGIO = 0xFFFFFFFB,
SI_ASYNCIO = 0xFFFFFFFC,
SI_MESGQ = 0xFFFFFFFD,
SI_TIMER = 0xFFFFFFFE,
SI_QUEUE = 0xFFFFFFFF,
SI_USER = 0x0,
SI_KERNEL = 0x80,
};

```
#### $BF4FFC8FA3F69AC17F194B5C1C38DCD3 : __int32
```cpp
/* 478087 */
enum $BF4FFC8FA3F69AC17F194B5C1C38DCD3 : __int32
{
PTHREAD_CREATE_JOINABLE = 0x0,
PTHREAD_CREATE_DETACHED = 0x1,
};

```
#### $D8AD35139B05A1F2F34E4C9B32270E50 : __int32
```cpp
/* 485599 */
enum $D8AD35139B05A1F2F34E4C9B32270E50 : __int32
{
CURLFORM_NOTHING = 0x0,
CURLFORM_COPYNAME = 0x1,
CURLFORM_PTRNAME = 0x2,
CURLFORM_NAMELENGTH = 0x3,
CURLFORM_COPYCONTENTS = 0x4,
CURLFORM_PTRCONTENTS = 0x5,
CURLFORM_CONTENTSLENGTH = 0x6,
CURLFORM_FILECONTENT = 0x7,
CURLFORM_ARRAY = 0x8,
CURLFORM_OBSOLETE = 0x9,
CURLFORM_FILE = 0xA,
CURLFORM_BUFFER = 0xB,
CURLFORM_BUFFERPTR = 0xC,
CURLFORM_BUFFERLENGTH = 0xD,
CURLFORM_CONTENTTYPE = 0xE,
CURLFORM_CONTENTHEADER = 0xF,
CURLFORM_FILENAME = 0x10,
CURLFORM_END = 0x11,
CURLFORM_OBSOLETE2 = 0x12,
CURLFORM_STREAM = 0x13,
CURLFORM_LASTENTRY = 0x14,
};

```
#### $EF54F05406754BCF09CF1DEEDAE2A64A : __int64
```cpp
/* 430546 */
enum $EF54F05406754BCF09CF1DEEDAE2A64A : __int64
{
ExpressionOpFlag_LeftParenthesis = 0x1,
ExpressionOpFlag_RightParenthesis = 0x2,
ExpressionOpFlag_LeftBracket = 0x4,
ExpressionOpFlag_RightBracket = 0x8,
ExpressionOpFlag_Negate = 0x10,
ExpressionOpFlag_LogicalNot = 0x20,
ExpressionOpFlag_Abs = 0x40,
ExpressionOpFlag_Cos = 0x80,
ExpressionOpFlag_Sin = 0x100,
ExpressionOpFlag_Clamp = 0x200,
ExpressionOpFlag_Lerp = 0x400,
ExpressionOpFlag_LerpRotate = 0x800,
ExpressionOpFlag_Max = 0x1000,
ExpressionOpFlag_Min = 0x2000,
ExpressionOpFlag_Round = 0x4000,
ExpressionOpFlag_Trunc = 0x8000,
ExpressionOpFlag_Ceil = 0x10000,
ExpressionOpFlag_Floor = 0x20000,
ExpressionOpFlag_Mod = 0x40000,
ExpressionOpFlag_Add = 0x80000,
ExpressionOpFlag_Div = 0x100000,
ExpressionOpFlag_Mul = 0x200000,
ExpressionOpFlag_Exp = 0x400000,
ExpressionOpFlag_Ln = 0x800000,
ExpressionOpFlag_Sqrt = 0x1000000,
ExpressionOpFlag_Pow = 0x2000000,
ExpressionOpFlag_Random = 0x4000000,
ExpressionOpFlag_DieRoll = 0x8000000,
ExpressionOpFlag_QueryFunction = 0x10000000,
ExpressionOpFlag_GenericQueryFunction = 0x20000000,
ExpressionOpFlag_ArrayVariable = 0x40000000,
ExpressionOpFlag_EntityVariable = 0x80000000,
ExpressionOpFlag_TempVariable = 0x100000000,
ExpressionOpFlag_HashedString = 0x200000000,
ExpressionOpFlag_GeometryVariable = 0x400000000,
ExpressionOpFlag_MaterialVariable = 0x800000000,
ExpressionOpFlag_TextureVariable = 0x1000000000,
ExpressionOpFlag_LessThan = 0x2000000000,
ExpressionOpFlag_LessEqual = 0x4000000000,
ExpressionOpFlag_GreaterEqual = 0x8000000000,
ExpressionOpFlag_GreaterThan = 0x10000000000,
ExpressionOpFlag_LogicalEqual = 0x20000000000,
ExpressionOpFlag_LogicalNotEqual = 0x40000000000,
ExpressionOpFlag_LogicalOr = 0x80000000000,
ExpressionOpFlag_LogicalAnd = 0x100000000000,
ExpressionOpFlag_Conditional = 0x200000000000,
ExpressionOpFlag_ConditionalElse = 0x400000000000,
ExpressionOpFlag_Float = 0x800000000000,
ExpressionOpFlag_Pi = 0x1000000000000,
ExpressionOpFlag_Array = 0x2000000000000,
ExpressionOpFlag_Geometry = 0x4000000000000,
ExpressionOpFlag_ModelPart = 0x8000000000000,
ExpressionOpFlag_Material = 0x10000000000000,
ExpressionOpFlag_Texture = 0x20000000000000,
ExpressionOpFlag_Assignment = 0x40000000000000,
ExpressionOpFlag_Semicolon = 0x80000000000000,
ExpressionOpFlag_Return = 0x100000000000000,
ExpressionOpFlag_Comma = 0x200000000000000,
ExpressionOpFlag_This = 0x400000000000000,
};

```
#### $F32B689939CEA71C8E19C738C224B0DC : __int32
```cpp
/* 485730 */
enum $F32B689939CEA71C8E19C738C224B0DC : __int32
{
SS_ONSTACK = 0x1,
SS_DISABLE = 0x2,
};

```
#### $F74524F48CF4910B20371C911B765561 : __int32
```cpp
/* 483208 */
enum $F74524F48CF4910B20371C911B765561 : __int32
{
DT_UNKNOWN = 0x0,
DT_FIFO = 0x1,
DT_CHR = 0x2,
DT_DIR = 0x4,
DT_BLK = 0x6,
DT_REG = 0x8,
DT_LNK = 0xA,
DT_SOCK = 0xC,
DT_WHT = 0xE,
};

```
#### $FB2272BC94AC42AEC5E9EBA0E6473F05 : __int32
```cpp
/* 63713 */
enum $FB2272BC94AC42AEC5E9EBA0E6473F05 : __int32
{
PTHREAD_MUTEX_TIMED_NP = 0x0,
PTHREAD_MUTEX_RECURSIVE_NP = 0x1,
PTHREAD_MUTEX_ERRORCHECK_NP = 0x2,
PTHREAD_MUTEX_ADAPTIVE_NP = 0x3,
PTHREAD_MUTEX_NORMAL = 0x0,
PTHREAD_MUTEX_RECURSIVE = 0x1,
PTHREAD_MUTEX_ERRORCHECK = 0x2,
PTHREAD_MUTEX_DEFAULT = 0x0,
PTHREAD_MUTEX_FAST_NP = 0x0,
};

```
#### ADRole : __int8
```cpp
/* 44518 */
enum ADRole : __int8
{
};

```
#### ADRole_0 : __int8
```cpp
/* 77426 */
enum ADRole_0 : __int8
{
Student = 0x0,
Teacher = 0x1,
Unknown_28 = 0x2,
};

```
#### ARVRPlatform : __int32
```cpp
/* 6920 */
enum ARVRPlatform : __int32
{
ARVR_None = 0x0,
ARVR_Rift = 0x1,
ARVR_Holographic = 0x2,
ARVR_WindowsMR = 0x3,
ARVR_OrbisVR = 0x4,
};

```
#### AbilitiesIndex : __int16
```cpp
/* 5596 */
enum AbilitiesIndex : __int16
{
Invalid_3 = 0xFFFF,
Build = 0x0,
Mine = 0x1,
DoorsAndSwitches = 0x2,
OpenContainers = 0x3,
AttackPlayers = 0x4,
AttackMobs = 0x5,
OperatorCommands = 0x6,
Teleport = 0x7,
ExposedAbilityCount = 0x8,
Invulnerable = 0x8,
Flying = 0x9,
MayFly = 0xA,
Instabuild = 0xB,
Lightning = 0xC,
FlySpeed = 0xD,
WalkSpeed = 0xE,
Muted = 0xF,
WorldBuilder = 0x10,
NoClip = 0x11,
AbilityCount = 0x12,
};

```
#### Ability::Options : __int8
```cpp
/* 3305 */
enum Ability::Options : __int8
{
None_2 = 0x0,
NoSave = 0x1,
CommandExposed = 0x2,
PermissionsInterfaceExposed = 0x4,
WorldbuilderOverrides = 0x8,
};

```
#### Ability::Type : __int8
```cpp
/* 3303 */
enum Ability::Type : __int8
{
Invalid_2 = 0x0,
Unset = 0x1,
Bool_0 = 0x2,
Float_0 = 0x3,
};

```
#### AbstractArrow::Data : __int32
```cpp
/* 454238 */
enum AbstractArrow::Data : __int32
{
OwnerID = 0x11,
};

```
#### ActionEvent::$35A09F5CCAEB66D754D2523C4A0226F8 : __int32
```cpp
/* 454220 */
enum ActionEvent::$35A09F5CCAEB66D754D2523C4A0226F8 : __int32
{
ACTION_MOVE_LEFT = 0x1,
ACTION_MOVE_RIGHT = 0x2,
ACTION_MOVE_FORWARD = 0x3,
ACTION_MOVE_BACKWARD = 0x4,
ACTION_ASCEND = 0x5,
ACTION_DESCEND = 0x6,
ACTION_PADDLE_LEFT = 0x7,
ACTION_PADDLE_RIGHT = 0x8,
ACTION_SNEAK = 0xA,
ACTION_JUMP = 0xB,
ACTION_SPRINT = 0xC,
ACTION_DISMOUNT = 0xE,
ACTION_MOB_EFFECTS = 0x14,
ACTION_DROP = 0x15,
ACTION_INVENTORY = 0x16,
ACTION_BUILD = 0x17,
ACTION_DESTROY = 0x18,
ACTION_INTERACT = 0x19,
ACTION_ATTACK = 0x1A,
ACTION_PAUSE = 0x1E,
ACTION_CHAT = 0x1F,
ACTION_CONSOLE = 0x20,
ACTION_THIRD_PERSON_VIEW = 0x21,
ACTION_SCOREBOARD = 0x22,
ACTION_CODE_BUILDER = 0x23,
ACTION_SLOT_0 = 0x32,
ACTION_SLOT_1 = 0x33,
ACTION_SLOT_2 = 0x34,
ACTION_SLOT_3 = 0x35,
ACTION_SLOT_4 = 0x36,
ACTION_SLOT_5 = 0x37,
ACTION_SLOT_6 = 0x38,
ACTION_SLOT_7 = 0x39,
ACTION_SLOT_8 = 0x3A,
ACTION_SLOT_9 = 0x3B,
ACTION_MENU_UP = 0x64,
ACTION_MENU_DOWN = 0x65,
ACTION_MENU_LEFT = 0x66,
ACTION_MENU_RIGHT = 0x67,
ACTION_MENU_OK = 0x68,
ACTION_MENU_CANCEL = 0x69,
ACTION_MENU_INVENTORY_DROP = 0x6A,
ACTION_MENU_INVENTORY_CANCEL = 0x6B,
ACTION_POINTER_PRESSED = 0x78,
ACTION_BUILD_OR_INTERACT = 0x82,
ACTION_DESTROY_OR_ATTACK = 0x83,
ACTION_BUILD_OR_ATTACK = 0x8C,
ACTION_DESTROY_OR_INTERACT = 0x8D,
};

```
#### ActionEvent::ActionState : __int32
```cpp
/* 89286 */
enum ActionEvent::ActionState : __int32
{
Start_1 = 0x1,
Stop = 0x2,
};

```
#### ActiveDirectoryAction : __int8
```cpp
/* 45336 */
enum ActiveDirectoryAction : __int8
{
DismissAndStartGame = 0x1,
DismissAndExitGame = 0x2,
};

```
#### Actor::InitializationMethod : __int8
```cpp
/* 77418 */
enum Actor::InitializationMethod : __int8
{
INVALID_0 = 0x0,
LOADED = 0x1,
SPAWNED = 0x2,
BORN = 0x3,
TRANSFORMED = 0x4,
UPDATED = 0x5,
EVENT = 0x6,
LEGACY = 0x7,
};

```
#### ActorAnimationType : __int32
```cpp
/* 125119 */
enum ActorAnimationType : __int32
{
Empty_0 = 0xFFFFFFFF,
SkeletalAnimation = 0x0,
AnimationController = 0x1,
AnimationControllerState = 0x2,
};

```
#### ActorBlockSyncMessage::MessageId : __int32
```cpp
/* 77420 */
enum ActorBlockSyncMessage::MessageId : __int32
{
NONE_5 = 0x0,
CREATE = 0x1,
DESTROY = 0x2,
};

```
#### ActorCategory : __int32
```cpp
/* 45376 */
enum ActorCategory : __int32
{
None_21 = 0x0,
Player_1 = 0x1,
Mob_0 = 0x2,
Monster_0 = 0x4,
Humandoid = 0x8,
Animal_0 = 0x10,
WaterSpawning = 0x20,
Pathable = 0x40,
Tamable = 0x80,
Ridable = 0x100,
Item_0 = 0x400,
Ambient_1 = 0x800,
Villager_0 = 0x1000,
Arthropod_0 = 0x2000,
Undead = 0x4000,
Zombie_0 = 0x8000,
Minecart_0 = 0x10000,
Boat = 0x20000,
NonTargetable = 0x40000,
BoatRideable_0 = 0x20100,
MinecartRidable = 0x10100,
HumanoidMonster = 0xC,
WaterAnimal_0 = 0x30,
TamableAnimal_0 = 0x90,
UndeadMob_0 = 0x4004,
ZombieMonster_0 = 0x8004,
EvocationIllagerMonster = 0x100C,
};

```
#### ActorDamageCause : __int32
```cpp
/* 44530 */
enum ActorDamageCause : __int32
{
None_18 = 0xFFFFFFFF,
Override = 0x0,
Contact = 0x1,
EntityAttack = 0x2,
Projectile_0 = 0x3,
Suffocation = 0x4,
Fall_0 = 0x5,
Fire_1 = 0x6,
FireTick = 0x7,
Lava_2 = 0x8,
Drowning = 0x9,
BlockExplosion = 0xA,
EntityExplosion = 0xB,
Void = 0xC,
Suicide = 0xD,
Magic = 0xE,
Wither = 0xF,
Starve = 0x10,
Anvil_1 = 0x11,
Thorns_0 = 0x12,
FallingBlock_0 = 0x13,
Piston_0 = 0x14,
FlyIntoWall = 0x15,
Magma = 0x16,
Fireworks_0 = 0x17,
Lightning_0 = 0x18,
Charging = 0x19,
Temperature = 0x1A,
All_0 = 0x1F,
};

```
#### ActorDataIDs : __int8
```cpp
/* 45375 */
enum ActorDataIDs : __int8
{
FLAGS = 0x0,
STRUCTURAL_INTEGRITY = 0x1,
VARIANT = 0x2,
COLOR_INDEX = 0x3,
NAME = 0x4,
OWNER = 0x5,
TARGET = 0x6,
AIR_SUPPLY = 0x7,
EFFECT_COLOR = 0x8,
EFFECT_AMBIENCE = 0x9,
JUMP_DURATION = 0xA,
HURT = 0xB,
HURT_DIR = 0xC,
ROW_TIME_LEFT = 0xD,
ROW_TIME_RIGHT = 0xE,
VALUE = 0xF,
DISPLAY_TILE_RUNTIME_ID = 0x10,
DISPLAY_OFFSET = 0x11,
CUSTOM_DISPLAY = 0x12,
SWELL = 0x13,
OLD_SWELL = 0x14,
SWELL_DIR = 0x15,
CHARGE_AMOUNT = 0x16,
CARRY_BLOCK_RUNTIME_ID = 0x17,
CLIENT_EVENT = 0x18,
USING_ITEM = 0x19,
PLAYER_FLAGS = 0x1A,
PLAYER_INDEX = 0x1B,
BED_POSITION = 0x1C,
X_POWER = 0x1D,
Y_POWER = 0x1E,
Z_POWER = 0x1F,
AUX_POWER = 0x20,
FISHX = 0x21,
FISHZ = 0x22,
FISHANGLE = 0x23,
AUX_VALUE_DATA = 0x24,
LEASH_HOLDER = 0x25,
SCALE = 0x26,
HAS_NPC = 0x27,
NPC_DATA = 0x28,
ACTIONS = 0x29,
AIR_SUPPLY_MAX = 0x2A,
MARK_VARIANT = 0x2B,
CONTAINER_TYPE = 0x2C,
CONTAINER_SIZE = 0x2D,
CONTAINER_STRENGTH_MODIFIER = 0x2E,
BLOCK_TARGET = 0x2F,
INV = 0x30,
TARGET_A = 0x31,
TARGET_B = 0x32,
TARGET_C = 0x33,
AERIAL_ATTACK = 0x34,
WIDTH = 0x35,
HEIGHT = 0x36,
FUSE_TIME = 0x37,
SEAT_OFFSET = 0x38,
SEAT_LOCK_RIDER_ROTATION = 0x39,
SEAT_LOCK_RIDER_ROTATION_DEGREES = 0x3A,
SEAT_ROTATION_OFFSET = 0x3B,
DATA_RADIUS = 0x3C,
DATA_WAITING = 0x3D,
DATA_PARTICLE = 0x3E,
PEEK_ID = 0x3F,
ATTACH_FACE = 0x40,
ATTACHED = 0x41,
ATTACH_POS = 0x42,
TRADE_TARGET = 0x43,
CAREER = 0x44,
HAS_COMMAND_BLOCK = 0x45,
COMMAND_NAME = 0x46,
LAST_COMMAND_OUTPUT = 0x47,
TRACK_COMMAND_OUTPUT = 0x48,
CONTROLLING_SEAT_INDEX = 0x49,
STRENGTH = 0x4A,
STRENGTH_MAX = 0x4B,
DATA_SPELL_CASTING_COLOR = 0x4C,
DATA_LIFETIME_TICKS = 0x4D,
POSE_INDEX = 0x4E,
DATA_TICK_OFFSET = 0x4F,
NAMETAG_ALWAYS_SHOW = 0x50,
COLOR_2_INDEX = 0x51,
NAME_AUTHOR = 0x52,
SCORE = 0x53,
BALLOON_ANCHOR = 0x54,
PUFFED_STATE = 0x55,
BUBBLE_TIME = 0x56,
AGENT = 0x57,
SITTING_AMOUNT = 0x58,
SITTING_AMOUNT_PREVIOUS = 0x59,
EATING_COUNTER = 0x5A,
FLAGS2 = 0x5B,
LAYING_AMOUNT = 0x5C,
LAYING_AMOUNT_PREVIOUS = 0x5D,
DATA_DURATION = 0x5E,
DATA_SPAWN_TIME = 0x5F,
DATA_CHANGE_RATE = 0x60,
DATA_CHANGE_ON_PICKUP = 0x61,
DATA_PICKUP_COUNT = 0x62,
INTERACT_TEXT = 0x63,
TRADE_TIER = 0x64,
MAX_TRADE_TIER = 0x65,
TRADE_EXPERIENCE = 0x66,
SKIN_ID = 0x67,
SPAWNING_FRAMES = 0x68,
COMMAND_BLOCK_TICK_DELAY = 0x69,
COMMAND_BLOCK_EXECUTE_ON_FIRST_TICK = 0x6A,
AMBIENT_SOUND_INTERVAL = 0x6B,
AMBIENT_SOUND_INTERVAL_RANGE = 0x6C,
AMBIENT_SOUND_EVENT_NAME = 0x6D,
FALL_DAMAGE_MULTIPLIER = 0x6E,
NAME_RAW_TEXT = 0x6F,
CAN_RIDE_TARGET = 0x70,
};

```
#### ActorEvent : __int8
```cpp
/* 48670 */
enum ActorEvent : __int8
{
NONE_1 = 0x0,
JUMP = 0x1,
HURT_0 = 0x2,
DEATH = 0x3,
START_ATTACKING = 0x4,
STOP_ATTACKING = 0x5,
TAMING_FAILED = 0x6,
TAMING_SUCCEEDED = 0x7,
SHAKE_WETNESS = 0x8,
EAT_GRASS = 0xA,
FISHHOOK_BUBBLE = 0xB,
FISHHOOK_FISHPOS = 0xC,
FISHHOOK_HOOKTIME = 0xD,
FISHHOOK_TEASE = 0xE,
SQUID_FLEEING = 0xF,
ZOMBIE_CONVERTING = 0x10,
PLAY_AMBIENT = 0x11,
SPAWN_ALIVE = 0x12,
START_OFFER_FLOWER = 0x13,
STOP_OFFER_FLOWER = 0x14,
LOVE_HEARTS = 0x15,
VILLAGER_ANGRY = 0x16,
VILLAGER_HAPPY = 0x17,
WITCH_HAT_MAGIC = 0x18,
FIREWORKS_EXPLODE = 0x19,
IN_LOVE_HEARTS = 0x1A,
SILVERFISH_MERGE_ANIM = 0x1B,
GUARDIAN_ATTACK_SOUND = 0x1C,
DRINK_POTION = 0x1D,
THROW_POTION = 0x1E,
PRIME_TNTCART = 0x1F,
PRIME_CREEPER = 0x20,
AIR_SUPPLY_0 = 0x21,
ADD_PLAYER_LEVELS = 0x22,
GUARDIAN_MINING_FATIGUE = 0x23,
AGENT_SWING_ARM = 0x24,
DRAGON_START_DEATH_ANIM = 0x25,
GROUND_DUST = 0x26,
SHAKE = 0x27,
FEED = 0x39,
BABY_EAT = 0x3C,
INSTANT_DEATH = 0x3D,
NOTIFY_TRADE = 0x3E,
LEASH_DESTROYED = 0x3F,
CARAVAN_UPDATED = 0x40,
TALISMAN_ACTIVATE = 0x41,
UPDATE_STRUCTURE_FEATURE = 0x42,
PLAYER_SPAWNED_MOB = 0x43,
PUKE = 0x44,
UPDATE_STACK_SIZE = 0x45,
START_SWIMMING = 0x46,
BALLOON_POP = 0x47,
TREASURE_HUNT = 0x48,
SUMMON_AGENT = 0x49,
FINISHED_CHARGING_CROSSBOW = 0x4A,
};

```
#### ActorFilterGroup::Processing : __int32
```cpp
/* 114144 */
enum ActorFilterGroup::Processing : __int32
{
Default_11 = 0x0,
ReadValue = 0x1,
ReadString = 0x2,
Environment = 0x3,
Item_1 = 0x4,
Armor_1 = 0x5,
Equipment_0 = 0x6,
};

```
#### ActorFlags : __int32
```cpp
/* 49718 */
enum ActorFlags : __int32
{
Unknown_25 = 0xFFFFFFFF,
ONFIRE = 0x0,
SNEAKING = 0x1,
RIDING = 0x2,
SPRINTING = 0x3,
USINGITEM = 0x4,
INVISIBLE = 0x5,
TEMPTED = 0x6,
INLOVE = 0x7,
SADDLED = 0x8,
POWERED = 0x9,
IGNITED = 0xA,
BABY = 0xB,
CONVERTING = 0xC,
CRITICAL = 0xD,
CAN_SHOW_NAME = 0xE,
ALWAYS_SHOW_NAME = 0xF,
NOAI = 0x10,
SILENT = 0x11,
WALLCLIMBING = 0x12,
CANCLIMB = 0x13,
CANSWIM = 0x14,
CANFLY = 0x15,
CANWALK = 0x16,
RESTING = 0x17,
SITTING = 0x18,
ANGRY = 0x19,
INTERESTED = 0x1A,
CHARGED = 0x1B,
TAMED = 0x1C,
ORPHANED = 0x1D,
LEASHED = 0x1E,
SHEARED = 0x1F,
GLIDING = 0x20,
ELDER = 0x21,
MOVING = 0x22,
BREATHING = 0x23,
CHESTED = 0x24,
STACKABLE = 0x25,
SHOW_BOTTOM = 0x26,
STANDING = 0x27,
SHAKING = 0x28,
IDLING = 0x29,
CASTING = 0x2A,
CHARGING = 0x2B,
WASD_CONTROLLED = 0x2C,
CAN_POWER_JUMP = 0x2D,
LINGERING = 0x2E,
HAS_COLLISION = 0x2F,
HAS_GRAVITY = 0x30,
FIRE_IMMUNE = 0x31,
DANCING = 0x32,
ENCHANTED = 0x33,
RETURNTRIDENT = 0x34,
CONTAINER_IS_PRIVATE = 0x35,
IS_TRANSFORMING = 0x36,
DAMAGENEARBYMOBS = 0x37,
SWIMMING = 0x38,
BRIBED = 0x39,
IS_PREGNANT = 0x3A,
LAYING_EGG = 0x3B,
RIDER_CAN_PICK = 0x3C,
TRANSITION_SITTING = 0x3D,
EATING = 0x3E,
LAYING_DOWN = 0x3F,
SNEEZING = 0x40,
TRUSTING = 0x41,
ROLLING = 0x42,
SCARED = 0x43,
IN_SCAFFOLDING = 0x44,
OVER_SCAFFOLDING = 0x45,
FALL_THROUGH_SCAFFOLDING = 0x46,
BLOCKING = 0x47,
TRANSITION_BLOCKING = 0x48,
BLOCKED_USING_SHIELD = 0x49,
BLOCKED_USING_DAMAGED_SHIELD = 0x4A,
SLEEPING = 0x4B,
WANTS_TO_WAKE = 0x4C,
TRADE_INTEREST = 0x4D,
DOOR_BREAKER = 0x4E,
BREAKING_OBSTRUCTION = 0x4F,
DOOR_OPENER = 0x50,
IS_ILLAGER_CAPTAIN = 0x51,
STUNNED = 0x52,
ROARING = 0x53,
DELAYED_ATTACK = 0x54,
IS_AVOIDING_MOBS = 0x55,
FACING_TARGET_TO_RANGE_ATTACK = 0x56,
HIDDEN_WHEN_INVISIBLE = 0x57,
IS_IN_UI = 0x58,
STALKING = 0x59,
EMOTING = 0x5A,
CELEBRATING = 0x5B,
Count_7 = 0x5C,
};

```
#### ActorInWeatherTest::WeatherType : __int32
```cpp
/* 456915 */
enum ActorInWeatherTest::WeatherType : __int32
{
Undefined_14 = 0xFFFFFFFF,
Clear_4 = 0x0,
Rain_0 = 0x1,
Snow_3 = 0x2,
Thunderstorm = 0x3,
};

```
#### ActorLinkType : __int8
```cpp
/* 35036 */
enum ActorLinkType : __int8
{
None_13 = 0x0,
Riding = 0x1,
Passenger = 0x2,
};

```
#### ActorLocation : __int32
```cpp
/* 48667 */
enum ActorLocation : __int32
{
Feet_0 = 0x0,
Body = 0x1,
WeaponAttachPoint = 0x2,
Head_0 = 0x3,
DropAttachPoint = 0x4,
ExplosionPoint = 0x5,
Eyes = 0x6,
BreathingPoint = 0x7,
Mouth = 0x8,
};

```
#### ActorTarget : __int32
```cpp
/* 48673 */
enum ActorTarget : __int32
{
This_0 = 0x0,
Killer = 0x1,
KillerPlayer = 0x2,
};

```
#### ActorTerrainInterlockData::VisibilityState : __int8
```cpp
/* 89260 */
enum ActorTerrainInterlockData::VisibilityState : __int8
{
InitialNotVisible = 0x0,
Visible_0 = 0x1,
DelayedDestructionNotVisible = 0x2,
};

```
#### ActorType : __int32
```cpp
/* 13183 */
enum ActorType : __int32
{
Undefined_2 = 0x1,
TypeMask = 0xFF,
Mob = 0x100,
PathfinderMob = 0x300,
Monster = 0xB00,
Animal = 0x1300,
TamableAnimal = 0x5300,
Ambient = 0x8100,
UndeadMob = 0x10B00,
ZombieMonster = 0x30B00,
Arthropod = 0x40B00,
Minecart = 0x80000,
SkeletonMonster = 0x110B00,
EquineAnimal = 0x205300,
Projectile = 0x400000,
AbstractArrow = 0x800000,
WaterAnimal = 0x2300,
VillagerBase = 0x1000300,
Chicken = 0x130A,
Cow = 0x130B,
Pig = 0x130C,
Sheep = 0x130D,
Wolf = 0x530E,
Villager = 0x100030F,
MushroomCow = 0x1310,
Squid = 0x2311,
Rabbit = 0x1312,
Bat = 0x8113,
IronGolem = 0x314,
SnowGolem = 0x315,
Ocelot = 0x5316,
Horse = 0x205317,
PolarBear = 0x131C,
Llama = 0x131D,
Parrot = 0x531E,
Dolphin = 0x231F,
Donkey = 0x205318,
Mule = 0x205319,
SkeletonHorse = 0x215B1A,
ZombieHorse = 0x215B1B,
Zombie = 0x30B20,
Creeper = 0xB21,
Skeleton = 0x110B22,
Spider = 0x40B23,
PigZombie = 0x10B24,
Slime = 0xB25,
EnderMan = 0xB26,
Silverfish = 0x40B27,
CaveSpider = 0x40B28,
Ghast = 0xB29,
LavaSlime = 0xB2A,
Blaze = 0xB2B,
ZombieVillager = 0x30B2C,
Witch = 0xB2D,
Stray = 0x110B2E,
Husk = 0x30B2F,
WitherSkeleton = 0x110B30,
Guardian = 0xB31,
ElderGuardian = 0xB32,
Npc = 0x133,
WitherBoss = 0x10B34,
Dragon = 0xB35,
Shulker = 0xB36,
Endermite = 0x40B37,
Agent = 0x138,
Vindicator = 0xB39,
Phantom = 0x10B3A,
IllagerBeast = 0xB3B,
ArmorStand = 0x13D,
TripodCamera = 0x13E,
Player_0 = 0x13F,
ItemEntity = 0x40,
PrimedTnt = 0x41,
FallingBlock = 0x42,
MovingBlock = 0x43,
ExperiencePotion = 0x400044,
Experience = 0x45,
EyeOfEnder = 0x46,
EnderCrystal = 0x47,
FireworksRocket = 0x48,
Trident = 0xC00049,
Turtle = 0x134A,
Cat = 0x534B,
ShulkerBullet = 0x40004C,
FishingHook = 0x4D,
Chalkboard = 0x4E,
DragonFireball = 0x40004F,
Arrow = 0xC00050,
Snowball = 0x400051,
ThrownEgg = 0x400052,
Painting = 0x53,
LargeFireball = 0x400055,
ThrownPotion = 0x400056,
Enderpearl = 0x400057,
LeashKnot = 0x58,
WitherSkull = 0x400059,
BoatRideable = 0x5A,
WitherSkullDangerous = 0x40005B,
LightningBolt = 0x5D,
SmallFireball = 0x40005E,
AreaEffectCloud = 0x5F,
LingeringPotion = 0x400065,
LlamaSpit = 0x400066,
EvocationFang = 0x400067,
EvocationIllager = 0xB68,
Vex = 0xB69,
MinecartRideable = 0x80054,
MinecartHopper = 0x80060,
MinecartTNT = 0x80061,
MinecartChest = 0x80062,
MinecartFurnace = 0x80063,
MinecartCommandBlock = 0x80064,
IceBomb = 0x40006A,
Balloon = 0x6B,
Pufferfish = 0x236C,
Salmon = 0x236D,
Drowned = 0x30B6E,
Tropicalfish = 0x236F,
Fish = 0x2370,
Panda = 0x1371,
Pillager = 0xB72,
VillagerV2 = 0x1000373,
ZombieVillagerV2 = 0x30B74,
Shield = 0x75,
WanderingTrader = 0x376,
Lectern = 0x77,
ElderGuardianGhost = 0xB78,
Fox = 0x1379,
Bee = 0x17A,
};

```
#### ActorTypeNamespaceRules : __int32
```cpp
/* 109111 */
enum ActorTypeNamespaceRules : __int32
{
ReturnWithoutNamespace = 0x0,
ReturnWithNamespace = 0x1,
};

```
#### AddTickingAreaStatus : __int32
```cpp
/* 190219 */
enum AddTickingAreaStatus : __int32
{
ExceededChunkLimit = 0x0,
ExceededTickingAreaLimit = 0x1,
ConflictingName = 0x2,
Success_12 = 0x3,
};

```
#### AdventureSettingsPacket::Flags : __int32
```cpp
/* 77410 */
enum AdventureSettingsPacket::Flags : __int32
{
WorldImmutable = 0x1,
NoPvM = 0x2,
NoMvP = 0x4,
Unused = 0x8,
ShowNameTags = 0x10,
AutoJump = 0x20,
PlayerMayFly = 0x40,
PlayerNoClip = 0x80,
PlayerWorldBuilder = 0x100,
PlayerFlying = 0x200,
PlayerMuted = 0x400,
};

```
#### AdventureSettingsPacket::PermissionsFlags : __int32
```cpp
/* 77409 */
enum AdventureSettingsPacket::PermissionsFlags : __int32
{
Mine_0 = 0x1,
DoorsAndSwitches_0 = 0x2,
OpenContainers_0 = 0x4,
AttackPlayers_0 = 0x8,
AttackMobs_0 = 0x10,
OP = 0x20,
Teleport_2 = 0x80,
Build_0 = 0x100,
DefaultLevelPermissions = 0x200,
};

```
#### AgentCommand::Mode : __int32
```cpp
/* 475754 */
enum AgentCommand::Mode : __int32
{
Attack_3 = 0x0,
Collect = 0x1,
Create_0 = 0x2,
Destroy_2 = 0x3,
Detect_0 = 0x4,
DetectRedstone = 0x5,
Drop = 0x6,
DropAll = 0x7,
GetItemCount = 0x8,
GetItemDetail = 0x9,
GetItemSpace = 0xA,
GetPosition = 0xB,
Inspect = 0xC,
InspectData = 0xD,
Move_0 = 0xE,
Place_6 = 0xF,
SetItem = 0x10,
Till = 0x11,
TP = 0x12,
Transfer_0 = 0x13,
Turn = 0x14,
};

```
#### AgentCommands::CollectCommand::CollectionSpecification : __int32
```cpp
/* 475803 */
enum AgentCommands::CollectCommand::CollectionSpecification : __int32
{
SpecificItem = 0x0,
AllItems = 0x1,
None_59 = 0x2,
};

```
#### AgentCommands::Direction : __int8
```cpp
/* 475705 */
enum AgentCommands::Direction : __int8
{
Up_1 = 0x0,
Down_1 = 0x1,
Forward = 0x2,
Back_0 = 0x3,
Left_2 = 0x4,
Right_2 = 0x5,
Undefined_15 = 0x6,
};

```
#### AggregateFeature<PlaceType::Arbitrary>::EarlyOut : __int32
```cpp
/* 256069 */
enum AggregateFeature<PlaceType::Arbitrary>::EarlyOut : __int32
{
None_51 = 0x0,
FirstFailure = 0x1,
FirstSuccess = 0x2,
};

```
#### AggregateFeature<PlaceType::Sequential>::EarlyOut : __int32
```cpp
/* 257231 */
enum AggregateFeature<PlaceType::Sequential>::EarlyOut : __int32
{
None_52 = 0x0,
FirstFailure_0 = 0x1,
FirstSuccess_0 = 0x2,
};

```
#### AnimatePacket::Action : __int32
```cpp
/* 77848 */
enum AnimatePacket::Action : __int32
{
NoAction = 0x0,
Swing = 0x1,
WakeUp = 0x3,
CriticalHit = 0x4,
MagicCriticalHit = 0x5,
RowRight = 0x80,
RowLeft = 0x81,
};

```
#### AnimationComponentGroup : __int32
```cpp
/* 88739 */
enum AnimationComponentGroup : __int32
{
Client_1 = 0x0,
ClientHUD = 0x1,
Server_1 = 0x2,
};

```
#### AnvilDamage : __int32
```cpp
/* 75527 */
enum AnvilDamage : __int32
{
Undamaged = 0x0,
SlightlyDamaged = 0x1,
VeryDamaged = 0x2,
Broken = 0x3,
_count_16 = 0x4,
};

```
#### AppFocusState : __int32
```cpp
/* 6919 */
enum AppFocusState : __int32
{
Focused = 0x0,
Unfocused = 0x1,
};

```
#### ArmorItem::Tier : __int32
```cpp
/* 180689 */
enum ArmorItem::Tier : __int32
{
TIER_LEATHER = 0x0,
TIER_CHAIN = 0x1,
TIER_IRON = 0x2,
TIER_DIAMOND = 0x3,
TIER_GOLD = 0x4,
TIER_ELYTRA = 0x5,
TIER_TURTLE = 0x6,
};

```
#### ArmorMaterialType : __int32
```cpp
/* 109098 */
enum ArmorMaterialType : __int32
{
None_38 = 0xFFFFFFFF,
DefaultArmor = 0x0,
EnchantedArmor = 0x1,
LeatherArmor = 0x2,
EnchantedLeatherArmor = 0x3,
};

```
#### ArmorSlot : __int32
```cpp
/* 13189 */
enum ArmorSlot : __int32
{
Head = 0x0,
Torso = 0x1,
Legs = 0x2,
Feet = 0x3,
_count_1 = 0x4,
};

```
#### ArmorTextureType : __int32
```cpp
/* 109099 */
enum ArmorTextureType : __int32
{
None_39 = 0xFFFFFFFF,
Leather = 0x0,
Chain_0 = 0x1,
Iron = 0x2,
Diamond = 0x3,
Gold = 0x4,
Elytra = 0x5,
Turtle_0 = 0x6,
};

```
#### Arrow::Data : __int32
```cpp
/* 173210 */
enum Arrow::Data : __int32
{
IsCritical = 0x10,
TippedAuxValue = 0x12,
};

```
#### AttachableSlotIndex : __int32
```cpp
/* 109092 */
enum AttachableSlotIndex : __int32
{
Head_3 = 0x0,
Torso_1 = 0x1,
Legs_2 = 0x2,
Feet_3 = 0x3,
CarriedItem = 0x4,
OffhandItem = 0x5,
_Count_1 = 0x6,
};

```
#### AttachmentType : __int32
```cpp
/* 230116 */
enum AttachmentType : __int32
{
Standing = 0x0,
Hanging = 0x1,
Side = 0x2,
Multiple = 0x3,
_count_48 = 0x4,
};

```
#### AttributeBuffType : __int32
```cpp
/* 109101 */
enum AttributeBuffType : __int32
{
Hunger = 0x0,
Saturation = 0x1,
Regeneration = 0x2,
Heal = 0x3,
Harm = 0x4,
Magic_0 = 0x5,
Wither_0 = 0x6,
Poison = 0x7,
FatalPoison = 0x8,
SelfHeal = 0x9,
Unknown_37 = 0xA,
None_40 = 0xB,
};

```
#### AttributeMessageTypes::$D202BB380D96D518A6C41FAAD128A520 : __int32
```cpp
/* 174375 */
enum AttributeMessageTypes::$D202BB380D96D518A6C41FAAD128A520 : __int32
{
EXHAUSTION = 0x0,
COUNT_11 = 0x1,
};

```
#### AttributeModifierOperation : __int32
```cpp
/* 115729 */
enum AttributeModifierOperation : __int32
{
OPERATION_ADDITION = 0x0,
OPERATION_MULTIPLY_BASE = 0x1,
OPERATION_MULTIPLY_TOTAL = 0x2,
OPERATION_CAP = 0x3,
TOTAL_OPERATIONS = 0x4,
OPERATION_INVALID = 0x4,
};

```
#### AttributeOperands : __int32
```cpp
/* 100208 */
enum AttributeOperands : __int32
{
OPERAND_MIN = 0x0,
OPERAND_MAX = 0x1,
OPERAND_CURRENT = 0x2,
TOTAL_OPERANDS = 0x3,
OPERAND_INVALID = 0x3,
};

```
#### Automation::MessagePurpose : __int8
```cpp
/* 430899 */
enum Automation::MessagePurpose : __int8
{
None_57 = 0x0,
RequestCommand = 0x1,
RequestSubscribe = 0x2,
RequestUnsubscribe = 0x3,
ResponseCommand = 0x4,
ResponseError = 0x5,
ResponseEvent = 0x6,
};

```
#### Automation::Response::Type : __int8
```cpp
/* 424406 */
enum Automation::Response::Type : __int8
{
Command_4 = 0x0,
Event_0 = 0x1,
};

```
#### BackgroundTask::TaskRunResult : __int32
```cpp
/* 484283 */
enum BackgroundTask::TaskRunResult : __int32
{
Requeue = 0x0,
Done_3 = 0x1,
Noop = 0x2,
};

```
#### BackgroundTask::TaskStatus : __int32
```cpp
/* 484165 */
enum BackgroundTask::TaskStatus : __int32
{
WaitingForPredecessor = 0x0,
Pending_0 = 0x1,
Running_1 = 0x2,
CancelPending = 0x3,
Canceled_3 = 0x4,
Error_7 = 0x5,
Done_2 = 0x6,
};

```
#### BackgroundWorker::RunOneResult : __int32
```cpp
/* 485400 */
enum BackgroundWorker::RunOneResult : __int32
{
NoTasks = 0x0,
TaskExecuted = 0x1,
Retry_0 = 0x2,
};

```
#### BackgroundWorker::State : __int32
```cpp
/* 485254 */
enum BackgroundWorker::State : __int32
{
Initializing_0 = 0x0,
Off_0 = 0x1,
Running_3 = 0x2,
};

```
#### BannerBlockType : __int32
```cpp
/* 180700 */
enum BannerBlockType : __int32
{
Default_13 = 0x0,
IllagerCaptain = 0x1,
};

```
#### BannerPatternItem::Type : __int32
```cpp
/* 183739 */
enum BannerPatternItem::Type : __int32
{
Creeper_0 = 0x0,
Skull_0 = 0x1,
Flower_0 = 0x2,
Thing = 0x3,
Bricks = 0x4,
Vines = 0x5,
_count_39 = 0x6,
};

```
#### BaseRailTransporter::RailType : __int32
```cpp
/* 223108 */
enum BaseRailTransporter::RailType : __int32
{
Activator = 0x0,
Power = 0x1,
};

```
#### BedSleepingResult : __int32
```cpp
/* 173069 */
enum BedSleepingResult : __int32
{
OK_2 = 0x0,
NOT_POSSIBLE_HERE = 0x1,
NOT_POSSIBLE_NOW = 0x2,
TOO_FAR_AWAY = 0x3,
OTHER_PROBLEM = 0x4,
NOT_SAFE = 0x5,
};

```
#### Bedrock::Threading::AsyncErrc : __int32
```cpp
/* 484153 */
enum Bedrock::Threading::AsyncErrc : __int32
{
operation_in_progress_0 = 0x1,
operation_canceled_0 = 0x2,
operation_threw_exception = 0x3,
unexpected_error = 0x4,
invalid_state = 0x5,
};

```
#### Bedrock::Threading::AsyncStatus : __int32
```cpp
/* 63702 */
enum Bedrock::Threading::AsyncStatus : __int32
{
Started_1 = 0x0,
Completed_1 = 0x1,
Canceled_2 = 0x2,
Error_2 = 0x3,
};

```
#### Bedrock::Threading::OSThreadPriority : __int32
```cpp
/* 5512 */
enum Bedrock::Threading::OSThreadPriority : __int32
{
High = 0x0,
Elevated = 0x1,
Normal = 0x2,
Low = 0x3,
};

```
#### BedrockLog::LogCategory : __int32
```cpp
/* 5582 */
enum BedrockLog::LogCategory : __int32
{
LogArea = 0x0,
LogWorldGen = 0x1,
LogLoot = 0x2,
LogRender = 0x3,
LogStructure = 0x4,
LogUI = 0x5,
LogOnline = 0x6,
NumLogCategories = 0x7,
};

```
#### BedrockLog::LogChannel : __int32
```cpp
/* 480294 */
enum BedrockLog::LogChannel : __int32
{
Global_0 = 0x0,
ClientSide = 0x1,
ServerSide = 0x2,
NumLogChannels = 0x3,
};

```
#### BedrockLog::LogRule : __int32
```cpp
/* 5583 */
enum BedrockLog::LogRule : __int32
{
DefaultRules = 0x0,
ClientAndServer = 0x1,
};

```
#### BehaviorData::DataType : __int8
```cpp
/* 50657 */
enum BehaviorData::DataType : __int8
{
BlockPosition = 0x0,
Boolean = 0x1,
Float_4 = 0x2,
Int_3 = 0x3,
String_2 = 0x4,
Vector3 = 0x5,
VoidPointer = 0x6,
};

```
#### BehaviorStatus : __int32
```cpp
/* 454219 */
enum BehaviorStatus : __int32
{
Success_14 = 0x0,
Running_0 = 0x1,
Failure_0 = 0x2,
Error_6 = 0x3,
Undefined_13 = 0x4,
};

```
#### Biome::BiomeTempCategory : __int32
```cpp
/* 177354 */
enum Biome::BiomeTempCategory : __int32
{
OCEAN = 0x0,
COLD_0 = 0x1,
MEDIUM = 0x2,
WARM_0 = 0x3,
};

```
#### BiomeComponentFactory::ComponentScope : __int32
```cpp
/* 190210 */
enum BiomeComponentFactory::ComponentScope : __int32
{
Client_3 = 0x0,
Server_3 = 0x1,
ClientAndServer_0 = 0x2,
};

```
#### BiomeComponentFactory::FactoryScope : __int32
```cpp
/* 88412 */
enum BiomeComponentFactory::FactoryScope : __int32
{
Client_0 = 0x0,
Server_0 = 0x1,
};

```
#### BiomeTemperatureCategory : __int8
```cpp
/* 39255 */
enum BiomeTemperatureCategory : __int8
{
Medium_0 = 0x0,
Warm = 0x1,
Lukewarm = 0x2,
Cold = 0x3,
Frozen = 0x4,
Count_4 = 0x5,
};

```
#### Blacklist::Duration : __int32
```cpp
/* 74634 */
enum Blacklist::Duration : __int32
{
Session = 0x0,
OneTime = 0x1,
Invalid_15 = 0x2,
};

```
#### BlockActorRendererId : __int32
```cpp
/* 235085 */
enum BlockActorRendererId : __int32
{
TR_DEFAULT_RENDERER = 0x0,
TR_CHEST_RENDERER = 0x1,
TR_SIGN_RENDERER = 0x2,
TR_MOBSPAWNER_RENDERER = 0x3,
TR_SKULL_RENDERER = 0x4,
TR_ENCHANTER_RENDERER = 0x5,
TR_PISTONARM_RENDERER = 0x6,
TR_ITEMFRAME_RENDERER = 0x7,
TR_MOVINGBLOCK_RENDERER = 0x8,
TR_CHALKBOARD_RENDERER = 0x9,
TR_BEACON_RENDERER = 0xA,
TR_ENDGATEWAY_RENDERER = 0xB,
TR_ENDERCHEST_RENDERER = 0xC,
TR_SHULKERBOX_RENDERER = 0xD,
TR_COMMANDBLOCK_RENDERER = 0xE,
TR_BED_RENDERER = 0xF,
TR_BANNER_RENDERER = 0x10,
TR_CONDUIT_RENDERER = 0x11,
TR_LECTERN_RENDERER = 0x12,
TR_BELL_RENDERER = 0x13,
TR_CAMPFIRE_RENDERER = 0x14,
};

```
#### BlockActorType : __int32
```cpp
/* 40864 */
enum BlockActorType : __int32
{
Undefined_6 = 0x0,
Furnace = 0x1,
Chest = 0x2,
NetherReactor = 0x3,
Sign = 0x4,
MobSpawner = 0x5,
Skull = 0x6,
FlowerPot = 0x7,
BrewingStand = 0x8,
EnchantingTable_0 = 0x9,
DaylightDetector = 0xA,
Music = 0xB,
Comparator = 0xC,
Dispenser = 0xD,
Dropper = 0xE,
Hopper = 0xF,
Cauldron = 0x10,
ItemFrame = 0x11,
PistonArm = 0x12,
MovingBlock_0 = 0x13,
Chalkboard_0 = 0x14,
Beacon = 0x15,
EndPortal = 0x16,
EnderChest = 0x17,
EndGateway = 0x18,
ShulkerBox = 0x19,
CommandBlock = 0x1A,
Bed_0 = 0x1B,
Banner = 0x1C,
StructureBlock = 0x20,
Jukebox = 0x21,
ChemistryTable = 0x22,
Conduit_0 = 0x23,
JigsawBlock = 0x24,
Lectern_0 = 0x25,
BlastFurnace = 0x26,
Smoker = 0x27,
Bell_0 = 0x28,
Campfire = 0x29,
BarrelBlock = 0x2A,
Beehive = 0x2B,
_count_14 = 0x2C,
};

```
#### BlockColor : __int8
```cpp
/* 35876 */
enum BlockColor : __int8
{
White = 0x0,
Orange = 0x1,
Magenta = 0x2,
Light_blue = 0x3,
Yellow = 0x4,
Lime = 0x5,
Pink = 0x6,
Gray = 0x7,
Silver = 0x8,
Cyan = 0x9,
Purple = 0xA,
Blue = 0xB,
Brown = 0xC,
Green = 0xD,
Red = 0xE,
Black = 0xF,
_count_11 = 0x10,
};

```
#### BlockProperty : __int64
```cpp
/* 115630 */
enum BlockProperty : __int64
{
None_43 = 0x0,
Stair = 0x1,
HalfSlab = 0x2,
Hopper_0 = 0x4,
TopSnow_0 = 0x8,
FenceGate = 0x10,
Leaf = 0x20,
ThinConnects2D = 0x40,
Connects2D = 0x80,
Carpet_0 = 0x100,
Button_0 = 0x200,
Door = 0x400,
Portal_3 = 0x800,
Heavy = 0x1000,
Snow_1 = 0x2000,
Trap = 0x4000,
Sign_0 = 0x8000,
Walkable = 0x10000,
PressurePlate = 0x20000,
PistonBlockGrabber = 0x40000,
TopSolidBlocking = 0x80000,
SolidBlocking = 0x100000,
CubeShaped = 0x200000,
Power_NO = 0x400000,
Power_BlockDown = 0x800000,
Immovable = 0x1000000,
BreakOnPush = 0x2000000,
Piston_1 = 0x4000000,
InfiniBurn = 0x8000000,
RequiresWorldBuilder = 0x10000000,
CausesDamage = 0x20000000,
BreaksWhenFallenOnByHeavy = 0x40000000,
OnlyPistonPush = 0x80000000,
Liquid_0 = 0x100000000,
CanBeBuiltOver = 0x200000000,
SnowRecoverable = 0x400000000,
Scaffolding = 0x800000000,
CanSupportCenterHangingBlock = 0x1000000000,
BreaksWhenHitByArrow = 0x2000000000,
Unwalkable = 0x4000000000,
Impenetrable = 0x8000000000,
Hollow = 0x10000000000,
OperatorBlock = 0x20000000000,
SupportedByFlowerPot = 0x40000000000,
PreventsJumping = 0x80000000000,
ContainsHoney = 0x100000000000,
Slime_2 = 0x200000000000,
};

```
#### BlockRenderLayer : __int32
```cpp
/* 223089 */
enum BlockRenderLayer : __int32
{
RENDERLAYER_DOUBLE_SIDED = 0x0,
RENDERLAYER_BLEND = 0x1,
RENDERLAYER_OPAQUE = 0x2,
RENDERLAYER_OPTIONAL_ALPHATEST = 0x3,
RENDERLAYER_ALPHATEST = 0x4,
RENDERLAYER_SEASONS_OPAQUE = 0x5,
RENDERLAYER_SEASONS_OPTIONAL_ALPHATEST = 0x6,
RENDERLAYER_ALPHATEST_SINGLE_SIDE = 0x7,
RENDERLAYER_ENDPORTAL = 0x8,
RENDERLAYER_BARRIER = 0x9,
RENDERLAYER_STRUCTURE_VOID = 0xA,
_RENDERLAYER_COUNT = 0xB,
};

```
#### BlockShape : __int32
```cpp
/* 116676 */
enum BlockShape : __int32
{
INVISIBLE_0 = 0xFFFFFFFF,
BLOCK = 0x0,
CROSS_TEXTURE = 0x1,
TORCH = 0x2,
FIRE_0 = 0x3,
WATER_0 = 0x4,
RED_DUST = 0x5,
ROWS = 0x6,
DOOR_0 = 0x7,
LADDER = 0x8,
RAIL = 0x9,
STAIRS = 0xA,
FENCE_0 = 0xB,
LEVER = 0xC,
CACTUS = 0xD,
BED = 0xE,
DIODE = 0xF,
IRON_FENCE = 0x12,
STEM = 0x13,
VINE = 0x14,
FENCE_GATE = 0x15,
CHEST = 0x16,
LILYPAD = 0x17,
BREWING_STAND_0 = 0x19,
PORTAL_FRAME = 0x1A,
COCOA = 0x1C,
TREE = 0x1F,
WALL = 0x20,
DOUBLE_PLANT = 0x28,
FLOWER_POT = 0x2A,
ANVIL_0 = 0x2B,
DRAGON_EGG = 0x2C,
STRUCTURE_VOID = 0x30,
BLOCK_HALF = 0x43,
TOP_SNOW = 0x44,
TRIPWIRE = 0x45,
TRIPWIRE_HOOK = 0x46,
CAULDRON_0 = 0x47,
REPEATER = 0x48,
COMPARATOR = 0x49,
HOPPER_0 = 0x4A,
SLIME_BLOCK = 0x4B,
PISTON = 0x4C,
BEACON_0 = 0x4D,
CHORUS_PLANT = 0x4E,
CHORUS_FLOWER = 0x4F,
END_PORTAL = 0x50,
END_ROD = 0x51,
END_GATEWAY = 0x52,
SKULL = 0x53,
FACING_BLOCK = 0x54,
COMMAND_BLOCK_0 = 0x55,
TERRACOTTA = 0x56,
DOUBLE_SIDE_FENCE = 0x57,
ITEM_FRAME = 0x58,
SHULKER_BOX = 0x59,
DOUBLESIDED_CROSS_TEXTURE = 0x5A,
DOUBLESIDED_DOUBLE_PLANT = 0x5B,
DOUBLESIDED_ROWS = 0x5C,
ELEMENT_BLOCK = 0x5D,
CHEMISTRY_TABLE = 0x5E,
CORAL_FAN = 0x60,
SEAGRASS = 0x61,
KELP = 0x62,
TRAPDOOR = 0x63,
SEA_PICKLE = 0x64,
CONDUIT = 0x65,
TURTLE_EGG = 0x66,
BUBBLE_COLUMN = 0x69,
BARRIER = 0x6A,
SIGN = 0x6B,
BAMBOO = 0x6C,
BAMBOO_SAPLING = 0x6D,
SCAFFOLDING = 0x6E,
GRINDSTONE_0 = 0x6F,
BELL = 0x70,
LANTERN = 0x71,
CAMPFIRE = 0x72,
LECTERN_0 = 0x73,
SWEET_BERRY_BUSH = 0x74,
CARTOGRAPHY_TABLE = 0x75,
COMPOSTER = 0x76,
STONE_CUTTER = 0x77,
HONEY_BLOCK = 0x78,
};

```
#### BlockSlot : __int32
```cpp
/* 426365 */
enum BlockSlot : __int32
{
None_56 = 0xFFFFFFFF,
Container_0 = 0x0,
_count_53 = 0x1,
};

```
#### BlockSoundType : __int32
```cpp
/* 294374 */
enum BlockSoundType : __int32
{
Normal_14 = 0x0,
Gravel = 0x1,
Wood_1 = 0x2,
Grass_0 = 0x3,
Metal_0 = 0x4,
Stone_3 = 0x5,
Cloth_0 = 0x6,
Glass_1 = 0x7,
Sand_0 = 0x8,
Snow_2 = 0x9,
Ladder = 0xA,
Anvil_2 = 0xB,
Slime_3 = 0xC,
Silent_0 = 0xD,
ItemFrame_1 = 0xE,
TurtleEgg = 0xF,
Bamboo = 0x10,
BambooSapling = 0x11,
Lantern = 0x12,
Scaffolding_0 = 0x13,
SweetBerryBush = 0x14,
Default_19 = 0x15,
Undefined_11 = 0x16,
};

```
#### BlockSupportType : __int32
```cpp
/* 173073 */
enum BlockSupportType : __int32
{
Center_0 = 0x0,
Edge = 0x1,
Any_3 = 0x2,
};

```
#### BoneAnimationRelativeMode : __int32
```cpp
/* 124453 */
enum BoneAnimationRelativeMode : __int32
{
Parent_0 = 0x0,
Entity_5 = 0x1,
};

```
#### BoneTransformType : __int32
```cpp
/* 124547 */
enum BoneTransformType : __int32
{
Position_0 = 0x0,
Rotation = 0x1,
Scale = 0x2,
_Count_2 = 0x3,
};

```
#### BookEditAction : __int8
```cpp
/* 76957 */
enum BookEditAction : __int8
{
ReplacePage = 0x0,
AddPage = 0x1,
DeletePage = 0x2,
SwapPages = 0x3,
Finalize = 0x4,
};

```
#### BossBarColor : __int32
```cpp
/* 51301 */
enum BossBarColor : __int32
{
PINK = 0x0,
BLUE = 0x1,
RED = 0x2,
GREEN = 0x3,
YELLOW = 0x4,
PURPLE = 0x5,
WHITE = 0x6,
};

```
#### BossBarOverlay : __int32
```cpp
/* 51302 */
enum BossBarOverlay : __int32
{
PROGRESS = 0x0,
NOTCHED_6 = 0x1,
NOTCHED_10 = 0x2,
NOTCHED_12 = 0x3,
NOTCHED_20 = 0x4,
};

```
#### BossEventUpdateType : __int32
```cpp
/* 51423 */
enum BossEventUpdateType : __int32
{
Add_0 = 0x0,
PlayerAdded = 0x1,
Remove = 0x2,
PlayerRemoved = 0x3,
Update_Percent = 0x4,
Update_Name = 0x5,
Update_Properties = 0x6,
Update_Style = 0x7,
};

```
#### Bounds::Option : __int32
```cpp
/* 37043 */
enum Bounds::Option : __int32
{
Default_5 = 0x0,
Flatten = 0x1,
};

```
#### BreathableComponent::BreathableState : __int32
```cpp
/* 51699 */
enum BreathableComponent::BreathableState : __int32
{
InAir = 0x0,
InWater = 0x1,
InLava = 0x2,
InSolids = 0x3,
InBreathableOverrideBlock = 0x4,
InNonBreathableOverrideBlock = 0x5,
};

```
#### BrewingStandBlockActor::$68235EB771568274AB23F364CDF33A71 : __int32
```cpp
/* 175306 */
enum BrewingStandBlockActor::$68235EB771568274AB23F364CDF33A71 : __int32
{
SLOT_INGREDIENT = 0x0,
SLOT_POTION1 = 0x1,
SLOT_POTION2 = 0x2,
SLOT_POTION3 = 0x3,
SLOT_FUEL = 0x4,
};

```
#### BrewingStandContainerData : __int32
```cpp
/* 175236 */
enum BrewingStandContainerData : __int32
{
SetBrewTime = 0x0,
SetFuelAmount = 0x1,
SetFuelTotal = 0x2,
};

```
#### BucketFillType : __int16
```cpp
/* 182771 */
enum BucketFillType : __int16
{
Unknown_43 = 0xFFFF,
Empty_1 = 0x0,
Milk_0 = 0x1,
Fish_0 = 0x2,
Salmon_0 = 0x3,
Tropicalfish_0 = 0x4,
Pufferfish_0 = 0x5,
Water_4 = 0x8,
Lava_5 = 0xA,
};

```
#### BuildPlatform : __int32
```cpp
/* 44652 */
enum BuildPlatform : __int32
{
Google = 0x1,
iOS = 0x2,
OSX = 0x3,
Amazon = 0x4,
GearVR_0 = 0x5,
UWP = 0x7,
Win32 = 0x8,
Dedicated = 0x9,
Orbis = 0xB,
Nx = 0xC,
Xbox_0 = 0xD,
WindowsPhone = 0xE,
Unknown_13 = 0xFFFFFFFF,
};

```
#### CSHA1::REPORT_TYPE : __int32
```cpp
/* 478098 */
enum CSHA1::REPORT_TYPE : __int32
{
REPORT_HEX = 0x0,
REPORT_DIGIT = 0x1,
REPORT_HEX_SHORT = 0x2,
};

```
#### CURLFORMcode : __int32
```cpp
/* 485598 */
enum CURLFORMcode : __int32
{
CURL_FORMADD_OK = 0x0,
CURL_FORMADD_MEMORY = 0x1,
CURL_FORMADD_OPTION_TWICE = 0x2,
CURL_FORMADD_NULL = 0x3,
CURL_FORMADD_UNKNOWN_OPTION = 0x4,
CURL_FORMADD_INCOMPLETE = 0x5,
CURL_FORMADD_ILLEGAL_ARRAY = 0x6,
CURL_FORMADD_DISABLED = 0x7,
CURL_FORMADD_LAST = 0x8,
};

```
#### CURLINFO : __int32
```cpp
/* 485600 */
enum CURLINFO : __int32
{
CURLINFO_NONE = 0x0,
CURLINFO_EFFECTIVE_URL = 0x100001,
CURLINFO_RESPONSE_CODE = 0x200002,
CURLINFO_TOTAL_TIME = 0x300003,
CURLINFO_NAMELOOKUP_TIME = 0x300004,
CURLINFO_CONNECT_TIME = 0x300005,
CURLINFO_PRETRANSFER_TIME = 0x300006,
CURLINFO_SIZE_UPLOAD = 0x300007,
CURLINFO_SIZE_DOWNLOAD = 0x300008,
CURLINFO_SPEED_DOWNLOAD = 0x300009,
CURLINFO_SPEED_UPLOAD = 0x30000A,
CURLINFO_HEADER_SIZE = 0x20000B,
CURLINFO_REQUEST_SIZE = 0x20000C,
CURLINFO_SSL_VERIFYRESULT = 0x20000D,
CURLINFO_FILETIME = 0x20000E,
CURLINFO_CONTENT_LENGTH_DOWNLOAD = 0x30000F,
CURLINFO_CONTENT_LENGTH_UPLOAD = 0x300010,
CURLINFO_STARTTRANSFER_TIME = 0x300011,
CURLINFO_CONTENT_TYPE = 0x100012,
CURLINFO_REDIRECT_TIME = 0x300013,
CURLINFO_REDIRECT_COUNT = 0x200014,
CURLINFO_PRIVATE = 0x100015,
CURLINFO_HTTP_CONNECTCODE = 0x200016,
CURLINFO_HTTPAUTH_AVAIL = 0x200017,
CURLINFO_PROXYAUTH_AVAIL = 0x200018,
CURLINFO_OS_ERRNO = 0x200019,
CURLINFO_NUM_CONNECTS = 0x20001A,
CURLINFO_SSL_ENGINES = 0x40001B,
CURLINFO_COOKIELIST = 0x40001C,
CURLINFO_LASTSOCKET = 0x20001D,
CURLINFO_FTP_ENTRY_PATH = 0x10001E,
CURLINFO_REDIRECT_URL = 0x10001F,
CURLINFO_PRIMARY_IP = 0x100020,
CURLINFO_APPCONNECT_TIME = 0x300021,
CURLINFO_CERTINFO = 0x400022,
CURLINFO_CONDITION_UNMET = 0x200023,
CURLINFO_LASTONE = 0x23,
};

```
#### CURLcode : __int32
```cpp
/* 485596 */
enum CURLcode : __int32
{
CURLE_OK = 0x0,
CURLE_UNSUPPORTED_PROTOCOL = 0x1,
CURLE_FAILED_INIT = 0x2,
CURLE_URL_MALFORMAT = 0x3,
CURLE_OBSOLETE4 = 0x4,
CURLE_COULDNT_RESOLVE_PROXY = 0x5,
CURLE_COULDNT_RESOLVE_HOST = 0x6,
CURLE_COULDNT_CONNECT = 0x7,
CURLE_FTP_WEIRD_SERVER_REPLY = 0x8,
CURLE_REMOTE_ACCESS_DENIED = 0x9,
CURLE_OBSOLETE10 = 0xA,
CURLE_FTP_WEIRD_PASS_REPLY = 0xB,
CURLE_OBSOLETE12 = 0xC,
CURLE_FTP_WEIRD_PASV_REPLY = 0xD,
CURLE_FTP_WEIRD_227_FORMAT = 0xE,
CURLE_FTP_CANT_GET_HOST = 0xF,
CURLE_OBSOLETE16 = 0x10,
CURLE_FTP_COULDNT_SET_TYPE = 0x11,
CURLE_PARTIAL_FILE = 0x12,
CURLE_FTP_COULDNT_RETR_FILE = 0x13,
CURLE_OBSOLETE20 = 0x14,
CURLE_QUOTE_ERROR = 0x15,
CURLE_HTTP_RETURNED_ERROR = 0x16,
CURLE_WRITE_ERROR = 0x17,
CURLE_OBSOLETE24 = 0x18,
CURLE_UPLOAD_FAILED = 0x19,
CURLE_READ_ERROR = 0x1A,
CURLE_OUT_OF_MEMORY = 0x1B,
CURLE_OPERATION_TIMEDOUT = 0x1C,
CURLE_OBSOLETE29 = 0x1D,
CURLE_FTP_PORT_FAILED = 0x1E,
CURLE_FTP_COULDNT_USE_REST = 0x1F,
CURLE_OBSOLETE32 = 0x20,
CURLE_RANGE_ERROR = 0x21,
CURLE_HTTP_POST_ERROR = 0x22,
CURLE_SSL_CONNECT_ERROR = 0x23,
CURLE_BAD_DOWNLOAD_RESUME = 0x24,
CURLE_FILE_COULDNT_READ_FILE = 0x25,
CURLE_LDAP_CANNOT_BIND = 0x26,
CURLE_LDAP_SEARCH_FAILED = 0x27,
CURLE_OBSOLETE40 = 0x28,
CURLE_FUNCTION_NOT_FOUND = 0x29,
CURLE_ABORTED_BY_CALLBACK = 0x2A,
CURLE_BAD_FUNCTION_ARGUMENT = 0x2B,
CURLE_OBSOLETE44 = 0x2C,
CURLE_INTERFACE_FAILED = 0x2D,
CURLE_OBSOLETE46 = 0x2E,
CURLE_TOO_MANY_REDIRECTS = 0x2F,
CURLE_UNKNOWN_TELNET_OPTION = 0x30,
CURLE_TELNET_OPTION_SYNTAX = 0x31,
CURLE_OBSOLETE50 = 0x32,
CURLE_PEER_FAILED_VERIFICATION = 0x33,
CURLE_GOT_NOTHING = 0x34,
CURLE_SSL_ENGINE_NOTFOUND = 0x35,
CURLE_SSL_ENGINE_SETFAILED = 0x36,
CURLE_SEND_ERROR = 0x37,
CURLE_RECV_ERROR = 0x38,
CURLE_OBSOLETE57 = 0x39,
CURLE_SSL_CERTPROBLEM = 0x3A,
CURLE_SSL_CIPHER = 0x3B,
CURLE_SSL_CACERT = 0x3C,
CURLE_BAD_CONTENT_ENCODING = 0x3D,
CURLE_LDAP_INVALID_URL = 0x3E,
CURLE_FILESIZE_EXCEEDED = 0x3F,
CURLE_USE_SSL_FAILED = 0x40,
CURLE_SEND_FAIL_REWIND = 0x41,
CURLE_SSL_ENGINE_INITFAILED = 0x42,
CURLE_LOGIN_DENIED = 0x43,
CURLE_TFTP_NOTFOUND = 0x44,
CURLE_TFTP_PERM = 0x45,
CURLE_REMOTE_DISK_FULL = 0x46,
CURLE_TFTP_ILLEGAL = 0x47,
CURLE_TFTP_UNKNOWNID = 0x48,
CURLE_REMOTE_FILE_EXISTS = 0x49,
CURLE_TFTP_NOSUCHUSER = 0x4A,
CURLE_CONV_FAILED = 0x4B,
CURLE_CONV_REQD = 0x4C,
CURLE_SSL_CACERT_BADFILE = 0x4D,
CURLE_REMOTE_FILE_NOT_FOUND = 0x4E,
CURLE_SSH = 0x4F,
CURLE_SSL_SHUTDOWN_FAILED = 0x50,
CURLE_AGAIN = 0x51,
CURLE_SSL_CRL_BADFILE = 0x52,
CURLE_SSL_ISSUER_ERROR = 0x53,
CURL_LAST = 0x54,
};

```
#### CURLoption : __int32
```cpp
/* 485597 */
enum CURLoption : __int32
{
CURLOPT_FILE = 0x2711,
CURLOPT_URL = 0x2712,
CURLOPT_PORT = 0x3,
CURLOPT_PROXY = 0x2714,
CURLOPT_USERPWD = 0x2715,
CURLOPT_PROXYUSERPWD = 0x2716,
CURLOPT_RANGE = 0x2717,
CURLOPT_INFILE = 0x2719,
CURLOPT_ERRORBUFFER = 0x271A,
CURLOPT_WRITEFUNCTION = 0x4E2B,
CURLOPT_READFUNCTION = 0x4E2C,
CURLOPT_TIMEOUT = 0xD,
CURLOPT_INFILESIZE = 0xE,
CURLOPT_POSTFIELDS = 0x271F,
CURLOPT_REFERER = 0x2720,
CURLOPT_FTPPORT = 0x2721,
CURLOPT_USERAGENT = 0x2722,
CURLOPT_LOW_SPEED_LIMIT = 0x13,
CURLOPT_LOW_SPEED_TIME = 0x14,
CURLOPT_RESUME_FROM = 0x15,
CURLOPT_COOKIE = 0x2726,
CURLOPT_HTTPHEADER = 0x2727,
CURLOPT_HTTPPOST = 0x2728,
CURLOPT_SSLCERT = 0x2729,
CURLOPT_KEYPASSWD = 0x272A,
CURLOPT_CRLF = 0x1B,
CURLOPT_QUOTE = 0x272C,
CURLOPT_WRITEHEADER = 0x272D,
CURLOPT_COOKIEFILE = 0x272F,
CURLOPT_SSLVERSION = 0x20,
CURLOPT_TIMECONDITION = 0x21,
CURLOPT_TIMEVALUE = 0x22,
CURLOPT_CUSTOMREQUEST = 0x2734,
CURLOPT_STDERR = 0x2735,
CURLOPT_POSTQUOTE = 0x2737,
CURLOPT_WRITEINFO = 0x2738,
CURLOPT_VERBOSE = 0x29,
CURLOPT_HEADER = 0x2A,
CURLOPT_NOPROGRESS = 0x2B,
CURLOPT_NOBODY = 0x2C,
CURLOPT_FAILONERROR = 0x2D,
CURLOPT_UPLOAD = 0x2E,
CURLOPT_POST = 0x2F,
CURLOPT_DIRLISTONLY = 0x30,
CURLOPT_APPEND = 0x32,
CURLOPT_NETRC = 0x33,
CURLOPT_FOLLOWLOCATION = 0x34,
CURLOPT_TRANSFERTEXT = 0x35,
CURLOPT_PUT = 0x36,
CURLOPT_PROGRESSFUNCTION = 0x4E58,
CURLOPT_PROGRESSDATA = 0x2749,
CURLOPT_AUTOREFERER = 0x3A,
CURLOPT_PROXYPORT = 0x3B,
CURLOPT_POSTFIELDSIZE = 0x3C,
CURLOPT_HTTPPROXYTUNNEL = 0x3D,
CURLOPT_INTERFACE = 0x274E,
CURLOPT_KRBLEVEL = 0x274F,
CURLOPT_SSL_VERIFYPEER = 0x40,
CURLOPT_CAINFO = 0x2751,
CURLOPT_MAXREDIRS = 0x44,
CURLOPT_FILETIME = 0x45,
CURLOPT_TELNETOPTIONS = 0x2756,
CURLOPT_MAXCONNECTS = 0x47,
CURLOPT_CLOSEPOLICY = 0x48,
CURLOPT_FRESH_CONNECT = 0x4A,
CURLOPT_FORBID_REUSE = 0x4B,
CURLOPT_RANDOM_FILE = 0x275C,
CURLOPT_EGDSOCKET = 0x275D,
CURLOPT_CONNECTTIMEOUT = 0x4E,
CURLOPT_HEADERFUNCTION = 0x4E6F,
CURLOPT_HTTPGET = 0x50,
CURLOPT_SSL_VERIFYHOST = 0x51,
CURLOPT_COOKIEJAR = 0x2762,
CURLOPT_SSL_CIPHER_LIST = 0x2763,
CURLOPT_HTTP_VERSION = 0x54,
CURLOPT_FTP_USE_EPSV = 0x55,
CURLOPT_SSLCERTTYPE = 0x2766,
CURLOPT_SSLKEY = 0x2767,
CURLOPT_SSLKEYTYPE = 0x2768,
CURLOPT_SSLENGINE = 0x2769,
CURLOPT_SSLENGINE_DEFAULT = 0x5A,
CURLOPT_DNS_USE_GLOBAL_CACHE = 0x5B,
CURLOPT_DNS_CACHE_TIMEOUT = 0x5C,
CURLOPT_PREQUOTE = 0x276D,
CURLOPT_DEBUGFUNCTION = 0x4E7E,
CURLOPT_DEBUGDATA = 0x276F,
CURLOPT_COOKIESESSION = 0x60,
CURLOPT_CAPATH = 0x2771,
CURLOPT_BUFFERSIZE = 0x62,
CURLOPT_NOSIGNAL = 0x63,
CURLOPT_SHARE = 0x2774,
CURLOPT_PROXYTYPE = 0x65,
CURLOPT_ENCODING = 0x2776,
CURLOPT_PRIVATE = 0x2777,
CURLOPT_HTTP200ALIASES = 0x2778,
CURLOPT_UNRESTRICTED_AUTH = 0x69,
CURLOPT_FTP_USE_EPRT = 0x6A,
CURLOPT_HTTPAUTH = 0x6B,
CURLOPT_SSL_CTX_FUNCTION = 0x4E8C,
CURLOPT_SSL_CTX_DATA = 0x277D,
CURLOPT_FTP_CREATE_MISSING_DIRS = 0x6E,
CURLOPT_PROXYAUTH = 0x6F,
CURLOPT_FTP_RESPONSE_TIMEOUT = 0x70,
CURLOPT_IPRESOLVE = 0x71,
CURLOPT_MAXFILESIZE = 0x72,
CURLOPT_INFILESIZE_LARGE = 0x75A3,
CURLOPT_RESUME_FROM_LARGE = 0x75A4,
CURLOPT_MAXFILESIZE_LARGE = 0x75A5,
CURLOPT_NETRC_FILE = 0x2786,
CURLOPT_USE_SSL = 0x77,
CURLOPT_POSTFIELDSIZE_LARGE = 0x75A8,
CURLOPT_TCP_NODELAY = 0x79,
CURLOPT_FTPSSLAUTH = 0x81,
CURLOPT_IOCTLFUNCTION = 0x4EA2,
CURLOPT_IOCTLDATA = 0x2793,
CURLOPT_FTP_ACCOUNT = 0x2796,
CURLOPT_COOKIELIST = 0x2797,
CURLOPT_IGNORE_CONTENT_LENGTH = 0x88,
CURLOPT_FTP_SKIP_PASV_IP = 0x89,
CURLOPT_FTP_FILEMETHOD = 0x8A,
CURLOPT_LOCALPORT = 0x8B,
CURLOPT_LOCALPORTRANGE = 0x8C,
CURLOPT_CONNECT_ONLY = 0x8D,
CURLOPT_CONV_FROM_NETWORK_FUNCTION = 0x4EAE,
CURLOPT_CONV_TO_NETWORK_FUNCTION = 0x4EAF,
CURLOPT_CONV_FROM_UTF8_FUNCTION = 0x4EB0,
CURLOPT_MAX_SEND_SPEED_LARGE = 0x75C1,
CURLOPT_MAX_RECV_SPEED_LARGE = 0x75C2,
CURLOPT_FTP_ALTERNATIVE_TO_USER = 0x27A3,
CURLOPT_SOCKOPTFUNCTION = 0x4EB4,
CURLOPT_SOCKOPTDATA = 0x27A5,
CURLOPT_SSL_SESSIONID_CACHE = 0x96,
CURLOPT_SSH_AUTH_TYPES = 0x97,
CURLOPT_SSH_PUBLIC_KEYFILE = 0x27A8,
CURLOPT_SSH_PRIVATE_KEYFILE = 0x27A9,
CURLOPT_FTP_SSL_CCC = 0x9A,
CURLOPT_TIMEOUT_MS = 0x9B,
CURLOPT_CONNECTTIMEOUT_MS = 0x9C,
CURLOPT_HTTP_TRANSFER_DECODING = 0x9D,
CURLOPT_HTTP_CONTENT_DECODING = 0x9E,
CURLOPT_NEW_FILE_PERMS = 0x9F,
CURLOPT_NEW_DIRECTORY_PERMS = 0xA0,
CURLOPT_POSTREDIR = 0xA1,
CURLOPT_SSH_HOST_PUBLIC_KEY_MD5 = 0x27B2,
CURLOPT_OPENSOCKETFUNCTION = 0x4EC3,
CURLOPT_OPENSOCKETDATA = 0x27B4,
CURLOPT_COPYPOSTFIELDS = 0x27B5,
CURLOPT_PROXY_TRANSFER_MODE = 0xA6,
CURLOPT_SEEKFUNCTION = 0x4EC7,
CURLOPT_SEEKDATA = 0x27B8,
CURLOPT_CRLFILE = 0x27B9,
CURLOPT_ISSUERCERT = 0x27BA,
CURLOPT_ADDRESS_SCOPE = 0xAB,
CURLOPT_CERTINFO = 0xAC,
CURLOPT_USERNAME = 0x27BD,
CURLOPT_PASSWORD = 0x27BE,
CURLOPT_PROXYUSERNAME = 0x27BF,
CURLOPT_PROXYPASSWORD = 0x27C0,
CURLOPT_NOPROXY = 0x27C1,
CURLOPT_TFTP_BLKSIZE = 0xB2,
CURLOPT_SOCKS5_GSSAPI_SERVICE = 0x27C3,
CURLOPT_SOCKS5_GSSAPI_NEC = 0xB4,
CURLOPT_PROTOCOLS = 0xB5,
CURLOPT_REDIR_PROTOCOLS = 0xB6,
CURLOPT_SSH_KNOWNHOSTS = 0x27C7,
CURLOPT_SSH_KEYFUNCTION = 0x4ED8,
CURLOPT_SSH_KEYDATA = 0x27C9,
CURLOPT_LASTENTRY = 0x27CA,
};

```
#### CameraItemComponent::UseAction : __int8
```cpp
/* 457057 */
enum CameraItemComponent::UseAction : __int8
{
None_58 = 0x0,
Place_5 = 0x1,
Use_2 = 0x2,
};

```
#### CauldronLiquidType : __int32
```cpp
/* 109113 */
enum CauldronLiquidType : __int32
{
Water_1 = 0x0,
Lava_3 = 0x1,
_count_22 = 0x2,
};

```
#### ChalkboardSize : __int8
```cpp
/* 44598 */
enum ChalkboardSize : __int8
{
OnebyOne = 0x0,
TwobyOne = 0x1,
ThreebyTwo = 0x2,
Invalid_11 = 0x3,
};

```
#### ChangeDimensionRequest::State : __int32
```cpp
/* 89835 */
enum ChangeDimensionRequest::State : __int32
{
PrepareRegion = 0x0,
WaitingForChunks = 0x1,
WaitingForRespawn = 0x2,
};

```
#### ChangeSettingCommand::Setting : __int32
```cpp
/* 6170 */
enum ChangeSettingCommand::Setting : __int32
{
AllowCheats = 0x0,
Difficulty = 0x1,
};

```
#### ChannelTransformAxisType : __int32
```cpp
/* 124575 */
enum ChannelTransformAxisType : __int32
{
Uniform = 0x0,
XYZ = 0x1,
Arbitrary = 0x2,
_Count_3 = 0x3,
};

```
#### ChemistryTableType : __int32
```cpp
/* 175329 */
enum ChemistryTableType : __int32
{
CompoundCreator = 0x0,
MaterialReducer = 0x1,
ElementConstructor = 0x2,
LabTable_0 = 0x3,
_count_25 = 0x4,
};

```
#### ChestBlock::ChestType : __int32
```cpp
/* 251038 */
enum ChestBlock::ChestType : __int32
{
TYPE_BASIC = 0x0,
TYPE_TRAP = 0x1,
TYPE_ENDER = 0x2,
};

```
#### ChiselType : __int32
```cpp
/* 183665 */
enum ChiselType : __int32
{
Default_14 = 0x0,
Chiseled_0 = 0x1,
Lines = 0x2,
Smooth_0 = 0x3,
_count_30 = 0x4,
};

```
#### ChunkCachedDataState : __int8
```cpp
/* 34996 */
enum ChunkCachedDataState : __int8
{
NotGenerated = 0x0,
Generating_0 = 0x1,
Generated_2 = 0x2,
};

```
#### ChunkDebugDisplaySavedState : __int8
```cpp
/* 34995 */
enum ChunkDebugDisplaySavedState : __int8
{
Generated_1 = 0x0,
Saved = 0x1,
};

```
#### ChunkSource::LoadMode : __int32
```cpp
/* 172975 */
enum ChunkSource::LoadMode : __int32
{
None_47 = 0x0,
Deferred = 0x1,
};

```
#### ChunkState : __int8
```cpp
/* 33525 */
enum ChunkState : __int8
{
Unloaded = 0x0,
Generating = 0x1,
Generated = 0x2,
PostProcessing = 0x3,
PostProcessed = 0x4,
CheckingForReplacementData = 0x5,
NeedsLighting = 0x6,
Lighting_0 = 0x7,
Loaded = 0x8,
};

```
#### ChunkTerrainDataState : __int8
```cpp
/* 34994 */
enum ChunkTerrainDataState : __int8
{
NoData_0 = 0x0,
NeedsFixup = 0x1,
ReadyForGeneration = 0x2,
Generated_0 = 0x3,
PostProcessed_0 = 0x4,
Ready = 0x5,
};

```
#### ClientPlayMode : __int32
```cpp
/* 80052 */
enum ClientPlayMode : __int32
{
Normal_5 = 0x0,
Teaser = 0x1,
Screen = 0x2,
Viewer = 0x3,
Reality = 0x4,
Placement = 0x5,
LivingRoom = 0x6,
ExitLevel = 0x7,
ExitLevelLivingRoom = 0x8,
NumModes = 0x9,
};

```
#### ClientboundMapItemDataPacket::Type : __int32
```cpp
/* 78627 */
enum ClientboundMapItemDataPacket::Type : __int32
{
Invalid_16 = 0x0,
TextureUpdate = 0x2,
DecorationUpdate = 0x4,
Creation = 0x8,
};

```
#### CloneCommand::CloneMode : __int32
```cpp
/* 424801 */
enum CloneCommand::CloneMode : __int32
{
Normal_15 = 0x0,
Force = 0x1,
Move = 0x2,
};

```
#### CloneCommand::MaskMode : __int32
```cpp
/* 424752 */
enum CloneCommand::MaskMode : __int32
{
Replace_0 = 0x0,
Filtered = 0x1,
Masked = 0x2,
};

```
#### ColorFormat::ColorEnum::AvailableColors : __int32
```cpp
/* 101397 */
enum ColorFormat::ColorEnum::AvailableColors : __int32
{
BLACK = 0x0,
DARK_BLUE = 0x1,
DARK_GREEN = 0x2,
DARK_AQUA = 0x3,
DARK_RED = 0x4,
DARK_PURPLE = 0x5,
GOLD = 0x6,
GRAY = 0x7,
DARK_GRAY = 0x8,
BLUE_0 = 0x9,
GREEN_0 = 0xA,
AQUA = 0xB,
RED_0 = 0xC,
LIGHT_PURPLE = 0xD,
YELLOW_0 = 0xE,
WHITE_0 = 0xF,
MINECOIN_GOLD = 0x10,
COUNT_6 = 0x11,
};

```
#### ColoredTorchColor : __int8
```cpp
/* 251041 */
enum ColoredTorchColor : __int8
{
Red_7 = 0x0,
Green_2 = 0x1,
Blue_3 = 0x2,
Purple_3 = 0x3,
Invalid_27 = 0x4,
};

```
#### CommandBlockMode : __int16
```cpp
/* 44536 */
enum CommandBlockMode : __int16
{
Normal_3 = 0x0,
Repeating = 0x1,
Chain = 0x2,
};

```
#### CommandCheatFlag : __int8
```cpp
/* 5653 */
enum CommandCheatFlag : __int8
{
Cheat = 0x0,
NotCheat = 0x40,
};

```
#### CommandExecuteFlag : __int8
```cpp
/* 5651 */
enum CommandExecuteFlag : __int8
{
Allowed = 0x0,
Disallowed = 0x10,
};

```
#### CommandLexer::TokenType : __int32
```cpp
/* 5667 */
enum CommandLexer::TokenType : __int32
{
Error_0 = 0x0,
Integer = 0x1,
NInteger = 0x2,
Identifier = 0x3,
Selector = 0x4,
Slash = 0x5,
Value = 0x6,
RValue = 0x7,
LValue = 0x8,
Equals = 0x9,
Comma = 0xA,
Colon = 0xB,
Not = 0xC,
Asterisk = 0xD,
Hash = 0xE,
OpenBracket = 0xF,
CloseBracket = 0x10,
OpenBrace = 0x11,
CloseBrace = 0x12,
String = 0x13,
Range = 0x14,
LessThan = 0x15,
GreaterThan = 0x16,
PlusEquals = 0x17,
MinusEquals = 0x18,
TimesEquals = 0x19,
DivideEquals = 0x1A,
ModEquals = 0x1B,
GreaterThanLessThan = 0x1C,
Unknown_1 = 0x1D,
End = 0x1E,
};

```
#### CommandOperator : __int8
```cpp
/* 5684 */
enum CommandOperator : __int8
{
};

```
#### CommandOperator_0 : __int8
```cpp
/* 92672 */
enum CommandOperator_0 : __int8
{
Invalid_19 = 0x0,
Equals_0 = 0x1,
PlusEquals_0 = 0x2,
MinusEquals_0 = 0x3,
TimesEquals_0 = 0x4,
DivideEquals_0 = 0x5,
ModEquals_0 = 0x6,
MinEquals = 0x7,
MaxEquals = 0x8,
Swap = 0x9,
};

```
#### CommandOriginSystem : __int32
```cpp
/* 88548 */
enum CommandOriginSystem : __int32
{
AnimationTimelineSystem = 0x0,
};

```
#### CommandOriginType : __int8
```cpp
/* 78801 */
enum CommandOriginType : __int8
{
Player_4 = 0x0,
CommandBlock_0 = 0x1,
MinecartCommandBlock_0 = 0x2,
DevConsole = 0x3,
Test_0 = 0x4,
AutomationPlayer = 0x5,
ClientAutomation = 0x6,
DedicatedServer = 0x7,
Entity_4 = 0x8,
Virtual = 0x9,
GameArgument = 0xA,
EntityServer = 0xB,
Precompiled = 0xC,
GameMasterEntityServer = 0xD,
Scripting_1 = 0xE,
};

```
#### CommandOutputMessageType : __int32
```cpp
/* 6318 */
enum CommandOutputMessageType : __int32
{
Success_0 = 0x0,
Error_1 = 0x1,
};

```
#### CommandOutputParameter::NoCountType : __int32
```cpp
/* 6315 */
enum CommandOutputParameter::NoCountType : __int32
{
NoCount = 0x0,
};

```
#### CommandOutputType : __int32
```cpp
/* 5687 */
enum CommandOutputType : __int32
{
None_7 = 0x0,
LastOutput = 0x1,
Silent = 0x2,
AllOutput = 0x3,
DataSet = 0x4,
};

```
#### CommandParameterDataType : __int32
```cpp
/* 1617 */
enum CommandParameterDataType : __int32
{
Basic = 0x0,
Enum = 0x1,
SoftEnum = 0x2,
Postfix = 0x3,
};

```
#### CommandParameterOption : __int8
```cpp
/* 1618 */
enum CommandParameterOption : __int8
{
None_1 = 0x0,
EnumAutocompleteExpansion = 0x1,
HasSemanticConstraint = 0x2,
};

```
#### CommandPermissionLevel : __int8
```cpp
/* 1619 */
enum CommandPermissionLevel : __int8
{
Any = 0x0,
GameMasters = 0x1,
Admin = 0x2,
Host = 0x3,
Owner = 0x4,
Internal = 0x5,
};

```
#### CommandRegistry::HardNonTerminal : __int32
```cpp
/* 5669 */
enum CommandRegistry::HardNonTerminal : __int32
{
Epsilon = 0x100000,
Int_0 = 0x100001,
Val = 0x100002,
RVal = 0x100003,
WildcardInt = 0x100004,
Operator_0 = 0x100005,
Selection = 0x100006,
WildcardSelection = 0x100007,
NonIdSelector = 0x100008,
ScoresArg = 0x100009,
ScoresArgs = 0x10000A,
ScoreSelectParam = 0x10000B,
ScoreSelector = 0x10000C,
TagSelector = 0x10000D,
FilePath = 0x10000E,
FilePathVal = 0x10000F,
FilePathCont = 0x100010,
IntegerRangeVal = 0x100011,
IntegerRangePostVal = 0x100012,
IntegerRange = 0x100013,
FullIntegerRange = 0x100014,
SelArgs = 0x100015,
Args = 0x100016,
Arg = 0x100017,
MArg = 0x100018,
MValue = 0x100019,
NameArg = 0x10001A,
TypeArg = 0x10001B,
TagArg = 0x10001C,
Id = 0x10001D,
IdCont = 0x10001E,
CoordXInt = 0x10001F,
CoordYInt = 0x100020,
CoordZInt = 0x100021,
CoordXFloat = 0x100022,
CoordYFloat = 0x100023,
CoordZFloat = 0x100024,
Position = 0x100025,
PositionFloat = 0x100026,
MessageExp = 0x100027,
Message_0 = 0x100028,
MessageRoot = 0x100029,
PostSelector = 0x10002A,
RawText = 0x10002B,
RawTextCont = 0x10002C,
JsonValue = 0x10002D,
JsonField = 0x10002E,
JsonObject = 0x10002F,
JsonObjectFields = 0x100030,
JsonObjectCont = 0x100031,
JsonArray = 0x100032,
JsonArrayValues = 0x100033,
JsonArrayCont = 0x100034,
Command = 0x100035,
SlashCommand = 0x100036,
};

```
#### CommandSelectionOrder : __int32
```cpp
/* 33043 */
enum CommandSelectionOrder : __int32
{
Sorted = 0x0,
InverseSorted = 0x1,
Random = 0x2,
};

```
#### CommandSelectionType : __int32
```cpp
/* 33042 */
enum CommandSelectionType : __int32
{
Self_0 = 0x0,
Entities = 0x1,
Players = 0x2,
DefaultPlayers = 0x3,
OwnedAgent = 0x4,
Agents = 0x5,
};

```
#### CommandStatus : __int32
```cpp
/* 5680 */
enum CommandStatus : __int32
{
Invalid_6 = 0x0,
Local_0 = 0x1,
Remote = 0x2,
};

```
#### CommandSyncFlag : __int8
```cpp
/* 5650 */
enum CommandSyncFlag : __int8
{
Synced = 0x0,
Local = 0x8,
};

```
#### CommandTypeFlag : __int8
```cpp
/* 5652 */
enum CommandTypeFlag : __int8
{
None_5 = 0x0,
Message = 0x20,
};

```
#### CommandUsageFlag : __int8
```cpp
/* 5648 */
enum CommandUsageFlag : __int8
{
Normal_1 = 0x0,
Test = 0x1,
};

```
#### CommandVisibilityFlag : __int8
```cpp
/* 5649 */
enum CommandVisibilityFlag : __int8
{
Visible = 0x0,
HiddenFromCommandBlockOrigin = 0x2,
HiddenFromPlayerOrigin = 0x4,
Hidden = 0x6,
};

```
#### CommonDirection : __int32
```cpp
/* 296633 */
enum CommonDirection : __int32
{
North_2 = 0x0,
East_2 = 0x1,
South_2 = 0x2,
West_2 = 0x3,
DownNorthSouth_0 = 0x4,
DownEastWest_0 = 0x5,
UpNorthSouth_0 = 0x6,
UpEastWest_0 = 0x7,
AscendingEast = 0x8,
AscendingWest = 0x9,
AscendingNorth = 0xA,
AscendingSouth = 0xB,
SouthEast = 0xC,
SouthWest = 0xD,
NorthWest = 0xE,
NorthEast = 0xF,
None_54 = 0x10,
};

```
#### CompactionStatus : __int32
```cpp
/* 86748 */
enum CompactionStatus : __int32
{
Starting_0 = 0x0,
Finished_1 = 0x1,
};

```
#### ComparatorCapacitor::Mode : __int32
```cpp
/* 292524 */
enum ComparatorCapacitor::Mode : __int32
{
COMPARE_MODE = 0x0,
SUBTRACT_MODE = 0x1,
};

```
#### ComplexInventoryTransaction::Type : __int32
```cpp
/* 79779 */
enum ComplexInventoryTransaction::Type : __int32
{
NormalTransaction = 0x0,
InventoryMismatch_0 = 0x1,
ItemUseTransaction = 0x2,
ItemUseOnEntityTransaction = 0x3,
ItemReleaseTransaction = 0x4,
};

```
#### CompoundContainerType : __int8
```cpp
/* 181065 */
enum CompoundContainerType : __int8
{
Jar = 0x0,
Beaker = 0x1,
Flask = 0x2,
Invalid_22 = 0x3,
};

```
#### CompoundTagUpdaterResult : __int32
```cpp
/* 13572 */
enum CompoundTagUpdaterResult : __int32
{
Success_2 = 0x0,
NoUpdateNeeded = 0x1,
Failed_0 = 0x2,
};

```
#### CompoundType : __int8
```cpp
/* 181066 */
enum CompoundType : __int8
{
Salt = 0x0,
SodiumOxide = 0x1,
SodiumHydroxide = 0x2,
MagnesiumNitrate = 0x3,
IronSulfide = 0x4,
LithiumHydride = 0x5,
SodiumHydride = 0x6,
CalciumBromide = 0x7,
MagnesiumOxide = 0x8,
SodiumAcetate = 0x9,
Luminol = 0xA,
Charcoal = 0xB,
Sugar = 0xC,
AluminumOxide = 0xD,
BoronTrioxide = 0xE,
Soap = 0xF,
Polyethylene = 0x10,
Garbage = 0x11,
MagnesiumSalts_0 = 0x12,
Sulfate = 0x13,
BariumSulfate = 0x14,
PotassiumChloride = 0x15,
MercuricChloride = 0x16,
CeriumChloride = 0x17,
TungstenChloride = 0x18,
CalciumChloride = 0x19,
Water_3 = 0x1A,
Glue = 0x1B,
Hypochlorite = 0x1C,
CrudeOil = 0x1D,
Latex = 0x1E,
PotassiumIodide = 0x1F,
SodiumFluoride = 0x20,
Benzene = 0x21,
Ink_0 = 0x22,
HydrogenPeroxide = 0x23,
Ammonia = 0x24,
SodiumHypochlorite = 0x25,
Invalid_23 = 0x26,
};

```
#### Compressibility : __int32
```cpp
/* 63714 */
enum Compressibility : __int32
{
Compressible = 0x0,
Incompressible = 0x1,
};

```
#### ConnectionDefinition::PortBusyFallbackPolicy : __int32
```cpp
/* 5664 */
enum ConnectionDefinition::PortBusyFallbackPolicy : __int32
{
UseRandom = 0x0,
Fail = 0x1,
};

```
#### ContainerBackgroundStyle : __int32
```cpp
/* 174665 */
enum ContainerBackgroundStyle : __int32
{
Classic = 0x0,
Normal_10 = 0x1,
Invert = 0x2,
Red_2 = 0x3,
Selected = 0x4,
RedButton = 0x5,
Hint = 0x6,
Count_25 = 0x7,
};

```
#### ContainerCategory : __int32
```cpp
/* 174694 */
enum ContainerCategory : __int32
{
Default_12 = 0x0,
PlayerInventory = 0x1,
Intermediary = 0x2,
Output_0 = 0x3,
Unknown_42 = 0x4,
};

```
#### ContainerEnumName : __int32
```cpp
/* 174780 */
enum ContainerEnumName : __int32
{
AnvilInputContainer = 0x0,
AnvilMaterialContainer = 0x1,
AnvilResultPreviewContainer = 0x2,
ArmorContainer = 0x3,
LevelEntityContainer = 0x4,
BeaconPaymentContainer = 0x5,
BrewingStandInputContainer = 0x6,
BrewingStandResultContainer = 0x7,
BrewingStandFuelContainer = 0x8,
CombinedHotbarAndInventoryContainer = 0x9,
CraftingInputContainer = 0xA,
CraftingOutputPreviewContainer = 0xB,
RecipeConstructionContainer = 0xC,
RecipeNatureContainer = 0xD,
RecipeItemsContainer = 0xE,
RecipeSearchContainer = 0xF,
RecipeSearchBarContainer = 0x10,
RecipeEquipmentContainer = 0x11,
EnchantingInputContainer = 0x12,
EnchantingMaterialContainer = 0x13,
FurnaceFuelContainer = 0x14,
FurnaceIngredientContainer = 0x15,
FurnaceResultContainer = 0x16,
HorseEquipContainer = 0x17,
HotbarContainer = 0x18,
HudContainer = 0x19,
InventoryContainer = 0x1A,
ShulkerBoxContainer = 0x1B,
TradeIngredient1Container = 0x1C,
TradeIngredient2Container = 0x1D,
TradeResultPreviewContainer = 0x1E,
OffhandContainer = 0x1F,
CompoundCreatorInput = 0x20,
CompoundCreatorOutputPreview = 0x21,
ElementConstructorOutputPreview = 0x22,
MaterialReducerInput_0 = 0x23,
MaterialReducerOutput = 0x24,
LabTableInput = 0x25,
LoomInputContainer = 0x26,
LoomDyeContainer = 0x27,
LoomMaterialContainer = 0x28,
LoomResultPreviewContainer = 0x29,
BlastFurnaceIngredientContainer = 0x2A,
SmokerIngredientContainer = 0x2B,
Trade2Ingredient1Container = 0x2C,
Trade2Ingredient2Container = 0x2D,
Trade2ResultPreviewContainer = 0x2E,
GrindstoneInputContainer = 0x2F,
GrindstoneAdditionalContainer = 0x30,
GrindstoneResultPreviewContainer = 0x31,
StonecutterInputContainer = 0x32,
StonecutterResultPreviewContainer = 0x33,
CartographyInputContainer = 0x34,
CartographyAdditionalContainer = 0x35,
CartographyResultPreviewContainer = 0x36,
BarrelContainer = 0x37,
CursorContainer = 0x38,
CreatedOutputContainer = 0x39,
};

```
#### ContainerExpandStatus : __int32
```cpp
/* 174693 */
enum ContainerExpandStatus : __int32
{
Normal_11 = 0x0,
Expanded_0 = 0x1,
Contracted = 0x2,
Child = 0x3,
Count_26 = 0x4,
};

```
#### ContainerID : __int8
```cpp
/* 33267 */
enum ContainerID : __int8
{
CONTAINER_ID_NONE = 0xFF,
CONTAINER_ID_INVENTORY = 0x0,
CONTAINER_ID_FIRST = 0x1,
CONTAINER_ID_LAST = 0x64,
CONTAINER_ID_OFFHAND = 0x77,
CONTAINER_ID_ARMOR = 0x78,
CONTAINER_ID_CREATIVE = 0x79,
CONTAINER_ID_SELECTION_SLOTS = 0x7A,
CONTAINER_ID_PLAYER_ONLY_UI = 0x7C,
};

```
#### ContainerType : __int8
```cpp
/* 48672 */
enum ContainerType : __int8
{
NONE_2 = 0xF7,
INVENTORY = 0xFF,
CONTAINER = 0x0,
WORKBENCH = 0x1,
FURNACE = 0x2,
ENCHANTMENT = 0x3,
BREWING_STAND = 0x4,
ANVIL = 0x5,
DISPENSER = 0x6,
DROPPER = 0x7,
HOPPER = 0x8,
CAULDRON = 0x9,
MINECART_CHEST = 0xA,
MINECART_HOPPER = 0xB,
HORSE = 0xC,
BEACON = 0xD,
STRUCTURE_EDITOR = 0xE,
TRADE = 0xF,
COMMAND_BLOCK = 0x10,
JUKEBOX = 0x11,
ARMOR = 0x12,
HAND = 0x13,
COMPOUND_CREATOR = 0x14,
ELEMENT_CONSTRUCTOR = 0x15,
MATERIAL_REDUCER = 0x16,
LAB_TABLE = 0x17,
LOOM = 0x18,
LECTERN = 0x19,
GRINDSTONE = 0x1A,
BLAST_FURNACE = 0x1B,
SMOKER = 0x1C,
STONECUTTER = 0x1D,
CARTOGRAPHY = 0x1E,
};

```
#### ContentTierIncompatibleReason : __int32
```cpp
/* 5784 */
enum ContentTierIncompatibleReason : __int32
{
};

```
#### ContentTierIncompatibleReason_0 : __int32
```cpp
/* 83332 */
enum ContentTierIncompatibleReason_0 : __int32
{
None_32 = 0x0,
Memory = 0x1,
};

```
#### ConversionFlags : __int32
```cpp
/* 486336 */
enum ConversionFlags : __int32
{
strictConversion_0 = 0x0,
lenientConversion_0 = 0x1,
};

```
#### ConversionResult : __int32
```cpp
/* 486311 */
enum ConversionResult : __int32
{
conversionOK = 0x0,
sourceExhausted = 0x1,
targetExhausted = 0x2,
sourceIllegal = 0x3,
};

```
#### CooldownType : __int32
```cpp
/* 172502 */
enum CooldownType : __int32
{
TypeNone = 0xFFFFFFFF,
ChorusFruit_0 = 0x0,
EnderPearl = 0x1,
IceBomb_1 = 0x2,
Count_24 = 0x3,
};

```
#### CoralColor : __int32
```cpp
/* 183705 */
enum CoralColor : __int32
{
Blue_2 = 0x0,
Pink_2 = 0x1,
Purple_2 = 0x2,
Red_4 = 0x3,
Yellow_2 = 0x4,
_count_35 = 0x5,
};

```
#### CoralDirection : __int32
```cpp
/* 460494 */
enum CoralDirection : __int32
{
West_3 = 0x0,
East_3 = 0x1,
North_3 = 0x2,
South_3 = 0x3,
};

```
#### Core::CrossStorageCopyMode : __int32
```cpp
/* 482463 */
enum Core::CrossStorageCopyMode : __int32
{
Buffered_0 = 0x0,
FullCopy = 0x1,
};

```
#### Core::DirectoryIterationFlags : __int64
```cpp
/* 84123 */
enum Core::DirectoryIterationFlags : __int64
{
None_34 = 0x1,
FullPathName = 0x2,
Name = 0x4,
FileSize = 0x8,
Type = 0x10,
CreateTime = 0x20,
ModifyTime = 0x40,
CreateAndModifyTime = 0x60,
Files = 0x80,
Directories = 0x100,
FilesAndDirectories = 0x180,
Recursive = 0x200,
TreatFlatFileAsFile = 0x400,
FileSizeAllocationOnDisk = 0x800,
};

```
#### Core::FileAccessType : __int32
```cpp
/* 463111 */
enum Core::FileAccessType : __int32
{
ReadOnly = 0x0,
ReadWrite = 0x1,
Flush = 0x2,
};

```
#### Core::FileBufferingMode : __int32
```cpp
/* 5544 */
enum Core::FileBufferingMode : __int32
{
Buffered = 0x0,
Unbuffered = 0x1,
};

```
#### Core::FileStorageArea::FlushableLevelDbEnvType : __int32
```cpp
/* 480043 */
enum Core::FileStorageArea::FlushableLevelDbEnvType : __int32
{
None_60 = 0x0,
InMemory = 0x1,
StorageArea = 0x2,
};

```
#### Core::FileType : __int32
```cpp
/* 83873 */
enum Core::FileType : __int32
{
File = 0x0,
Directory_1 = 0x1,
None_33 = 0x2,
};

```
#### Core::FlatFileManifestInfo::FlatFileManifestInfoFlags : __int8
```cpp
/* 482746 */
enum Core::FlatFileManifestInfo::FlatFileManifestInfoFlags : __int8
{
File_0 = 0x1,
Deleted = 0x80,
};

```
#### Core::LevelStorageState : __int32
```cpp
/* 87048 */
enum Core::LevelStorageState : __int32
{
Open_0 = 0x0,
Corrupted = 0x1,
NotFound = 0x2,
IOError = 0x3,
NotSupported = 0x4,
InvalidArguments = 0x5,
Unknown_31 = 0x6,
};

```
#### Core::Profile::CounterFlags : __int32
```cpp
/* 485590 */
enum Core::Profile::CounterFlags : __int32
{
None_62 = 0x0,
Detailed = 0x1,
DetailedGraph = 0x2,
};

```
#### Core::Profile::CounterFormat : __int32
```cpp
/* 64250 */
enum Core::Profile::CounterFormat : __int32
{
Default_8 = 0x0,
Bytes = 0x1,
};

```
#### Core::Profile::FileExtension : __int8
```cpp
/* 485591 */
enum Core::Profile::FileExtension : __int8
{
HTML = 0x0,
CSV = 0x1,
BOTH = 0x2,
};

```
#### Core::ZipUtils::UnzipResult : __int32
```cpp
/* 84117 */
enum Core::ZipUtils::UnzipResult : __int32
{
OK_0 = 0x0,
UnzipError = 0x1,
ParamError = 0x2,
BadZipFile = 0x3,
InternalError = 0x4,
CRCError = 0x5,
};

```
#### Core::ZipUtils::ZipCompressionLevel : __int32
```cpp
/* 84118 */
enum Core::ZipUtils::ZipCompressionLevel : __int32
{
Default_10 = 0x0,
NoCompression = 0x1,
BestSpeed = 0x2,
BestCompression = 0x3,
};

```
#### Core::ZipUtils::ZipResult : __int32
```cpp
/* 84119 */
enum Core::ZipUtils::ZipResult : __int32
{
OK_1 = 0x0,
ZipError = 0x1,
ParamError_0 = 0x2,
BadZipFile_0 = 0x3,
InternalError_0 = 0x4,
};

```
#### CraftingDataEntryType : __int32
```cpp
/* 75621 */
enum CraftingDataEntryType : __int32
{
ShapelessRecipe = 0x0,
ShapedRecipe = 0x1,
FurnaceRecipe = 0x2,
FurnaceAuxRecipe = 0x3,
MultiRecipe = 0x4,
ShulkerBoxRecipe = 0x5,
ShapelessChemistryRecipe = 0x6,
ShapedChemistryRecipe = 0x7,
};

```
#### CrashDumpLogStringID : __int16
```cpp
/* 480121 */
enum CrashDumpLogStringID : __int16
{
None_61 = 0x0,
HandleBuildAction = 0x1,
EnterScope = 0x2,
ExitScope = 0x3,
AppPlatform_initialize = 0x4,
MinecraftGame_update = 0x5,
DataDrivenRenderer_renderModel = 0x6,
KillMinecraft = 0x7,
StartMinecraft = 0x8,
Main = 0x9,
MakeMinecraftGame = 0xA,
MainLoop = 0xB,
AppResetRequested = 0xC,
Shutdown = 0xD,
ActorRenderDisplatcher_Render = 0xE,
AppMain_updateAndRender = 0xF,
AppPlatformWinrt_Update = 0x10,
AppView_run = 0x11,
MinecraftGame_initStep = 0x12,
MinecraftGame_suspendStep = 0x13,
MinecraftGame_resumeStep = 0x14,
AbortedScope = 0x15,
SaveData_mount = 0x16,
SaveData_unmount = 0x17,
SaveData_remount = 0x18,
SaveData_watchdog = 0x19,
_count_54 = 0x1A,
};

```
#### CreativeItemCategory : __int32
```cpp
/* 94506 */
enum CreativeItemCategory : __int32
{
All_3 = 0x0,
Construction = 0x1,
Nature = 0x2,
Equipment = 0x3,
Items = 0x4,
ItemCommandOnly = 0x5,
Undefined_10 = 0x6,
NUM_CATEGORIES = 0x7,
};

```
#### Crypto::Asymmetric::System : __int32
```cpp
/* 45580 */
enum Crypto::Asymmetric::System : __int32
{
RSA_1024 = 0x0,
RSA_2048 = 0x1,
RSA_4096 = 0x2,
EC_prime256v1 = 0x3,
EC_secp256k1 = 0x4,
EC_secp384r1 = 0x5,
EC_secp521r1 = 0x6,
};

```
#### Crypto::Hash::HashType : __int32
```cpp
/* 45581 */
enum Crypto::Hash::HashType : __int32
{
MD5 = 0x0,
SHA1 = 0x1,
SHA256 = 0x2,
SHA384 = 0x3,
SHA512 = 0x4,
};

```
#### Crypto::Symmetric::OperationMode : __int32
```cpp
/* 421421 */
enum Crypto::Symmetric::OperationMode : __int32
{
ECB = 0x0,
CBC = 0x1,
CFB = 0x2,
OFB = 0x3,
};

```
#### Crypto::Symmetric::System : __int32
```cpp
/* 421418 */
enum Crypto::Symmetric::System : __int32
{
AES_128 = 0x0,
AES_256 = 0x1,
};

```
#### CurrentCmdVersion : __int32
```cpp
/* 5678 */
enum CurrentCmdVersion : __int32
{
Invalid_5 = 0xFFFFFFFF,
Initial = 0x1,
TpRotationClamping = 0x2,
NewBedrockCmdSystem = 0x3,
ExecuteUsesVec3 = 0x4,
CloneFixes = 0x5,
UpdateAquatic = 0x6,
EntitySelectorUsesVec3 = 0x7,
ContainersDontDropItemsAnymore = 0x8,
FiltersObeyDimensions = 0x9,
ExecuteAndBlockCommandAndSelfSelectorFixes = 0xA,
};

```
#### DBChunkStorage::ChunkCacheStatus : __int32
```cpp
/* 476899 */
enum DBChunkStorage::ChunkCacheStatus : __int32
{
Missing = 0x0,
Available_0 = 0x1,
DontCache = 0x2,
};

```
#### DataItemType : __int8
```cpp
/* 47292 */
enum DataItemType : __int8
{
Byte = 0x0,
Short = 0x1,
Int_1 = 0x2,
Float_1 = 0x3,
String_0 = 0x4,
CompoundTag = 0x5,
Pos = 0x6,
Int64 = 0x7,
Vec3 = 0x8,
Unknown_23 = 0x9,
};

```
#### DataLoadHelperType : __int32
```cpp
/* 77438 */
enum DataLoadHelperType : __int32
{
Default_9 = 0x0,
Structure_0 = 0x1,
};

```
#### DateManager::TimeZoneType : __int32
```cpp
/* 82681 */
enum DateManager::TimeZoneType : __int32
{
UTC = 0x0,
Local_4 = 0x1,
};

```
#### DedicatedServer::StartResult : __int32
```cpp
/* 5508 */
enum DedicatedServer::StartResult : __int32
{
Success = 0x0,
PortOccupied = 0x1,
InvalidSettings = 0x2,
};

```
#### DefaultMessageIDTypes : __int32
```cpp
/* 73242 */
enum DefaultMessageIDTypes : __int32
{
ID_CONNECTED_PING = 0x0,
ID_UNCONNECTED_PING = 0x1,
ID_UNCONNECTED_PING_OPEN_CONNECTIONS = 0x2,
ID_CONNECTED_PONG = 0x3,
ID_DETECT_LOST_CONNECTIONS = 0x4,
ID_OPEN_CONNECTION_REQUEST_1 = 0x5,
ID_OPEN_CONNECTION_REPLY_1 = 0x6,
ID_OPEN_CONNECTION_REQUEST_2 = 0x7,
ID_OPEN_CONNECTION_REPLY_2 = 0x8,
ID_CONNECTION_REQUEST = 0x9,
ID_REMOTE_SYSTEM_REQUIRES_PUBLIC_KEY = 0xA,
ID_OUR_SYSTEM_REQUIRES_SECURITY = 0xB,
ID_PUBLIC_KEY_MISMATCH = 0xC,
ID_OUT_OF_BAND_INTERNAL = 0xD,
ID_SND_RECEIPT_ACKED = 0xE,
ID_SND_RECEIPT_LOSS = 0xF,
ID_CONNECTION_REQUEST_ACCEPTED = 0x10,
ID_CONNECTION_ATTEMPT_FAILED = 0x11,
ID_ALREADY_CONNECTED = 0x12,
ID_NEW_INCOMING_CONNECTION = 0x13,
ID_NO_FREE_INCOMING_CONNECTIONS = 0x14,
ID_DISCONNECTION_NOTIFICATION = 0x15,
ID_CONNECTION_LOST = 0x16,
ID_CONNECTION_BANNED = 0x17,
ID_INVALID_PASSWORD = 0x18,
ID_INCOMPATIBLE_PROTOCOL_VERSION = 0x19,
ID_IP_RECENTLY_CONNECTED = 0x1A,
ID_TIMESTAMP = 0x1B,
ID_UNCONNECTED_PONG = 0x1C,
ID_ADVERTISE_SYSTEM = 0x1D,
ID_DOWNLOAD_PROGRESS = 0x1E,
ID_REMOTE_DISCONNECTION_NOTIFICATION = 0x1F,
ID_REMOTE_CONNECTION_LOST = 0x20,
ID_REMOTE_NEW_INCOMING_CONNECTION = 0x21,
ID_FILE_LIST_TRANSFER_HEADER = 0x22,
ID_FILE_LIST_TRANSFER_FILE = 0x23,
ID_FILE_LIST_REFERENCE_PUSH_ACK = 0x24,
ID_DDT_DOWNLOAD_REQUEST = 0x25,
ID_TRANSPORT_STRING = 0x26,
ID_REPLICA_MANAGER_CONSTRUCTION = 0x27,
ID_REPLICA_MANAGER_SCOPE_CHANGE = 0x28,
ID_REPLICA_MANAGER_SERIALIZE = 0x29,
ID_REPLICA_MANAGER_DOWNLOAD_STARTED = 0x2A,
ID_REPLICA_MANAGER_DOWNLOAD_COMPLETE = 0x2B,
ID_RAKVOICE_OPEN_CHANNEL_REQUEST = 0x2C,
ID_RAKVOICE_OPEN_CHANNEL_REPLY = 0x2D,
ID_RAKVOICE_CLOSE_CHANNEL = 0x2E,
ID_RAKVOICE_DATA = 0x2F,
ID_AUTOPATCHER_GET_CHANGELIST_SINCE_DATE = 0x30,
ID_AUTOPATCHER_CREATION_LIST = 0x31,
ID_AUTOPATCHER_DELETION_LIST = 0x32,
ID_AUTOPATCHER_GET_PATCH = 0x33,
ID_AUTOPATCHER_PATCH_LIST = 0x34,
ID_AUTOPATCHER_REPOSITORY_FATAL_ERROR = 0x35,
ID_AUTOPATCHER_CANNOT_DOWNLOAD_ORIGINAL_UNMODIFIED_FILES = 0x36,
ID_AUTOPATCHER_FINISHED_INTERNAL = 0x37,
ID_AUTOPATCHER_FINISHED = 0x38,
ID_AUTOPATCHER_RESTART_APPLICATION = 0x39,
ID_NAT_PUNCHTHROUGH_REQUEST = 0x3A,
ID_NAT_CONNECT_AT_TIME = 0x3B,
ID_NAT_GET_MOST_RECENT_PORT = 0x3C,
ID_NAT_CLIENT_READY = 0x3D,
ID_NAT_TARGET_NOT_CONNECTED = 0x3E,
ID_NAT_TARGET_UNRESPONSIVE = 0x3F,
ID_NAT_CONNECTION_TO_TARGET_LOST = 0x40,
ID_NAT_ALREADY_IN_PROGRESS = 0x41,
ID_NAT_PUNCHTHROUGH_FAILED = 0x42,
ID_NAT_PUNCHTHROUGH_SUCCEEDED = 0x43,
ID_READY_EVENT_SET = 0x44,
ID_READY_EVENT_UNSET = 0x45,
ID_READY_EVENT_ALL_SET = 0x46,
ID_READY_EVENT_QUERY = 0x47,
ID_LOBBY_GENERAL = 0x48,
ID_RPC_REMOTE_ERROR = 0x49,
ID_RPC_PLUGIN = 0x4A,
ID_FILE_LIST_REFERENCE_PUSH = 0x4B,
ID_READY_EVENT_FORCE_ALL_SET = 0x4C,
ID_ROOMS_EXECUTE_FUNC = 0x4D,
ID_ROOMS_LOGON_STATUS = 0x4E,
ID_ROOMS_HANDLE_CHANGE = 0x4F,
ID_LOBBY2_SEND_MESSAGE = 0x50,
ID_LOBBY2_SERVER_ERROR = 0x51,
ID_FCM2_NEW_HOST = 0x52,
ID_FCM2_REQUEST_FCMGUID = 0x53,
ID_FCM2_RESPOND_CONNECTION_COUNT = 0x54,
ID_FCM2_INFORM_FCMGUID = 0x55,
ID_FCM2_UPDATE_MIN_TOTAL_CONNECTION_COUNT = 0x56,
ID_FCM2_VERIFIED_JOIN_START = 0x57,
ID_FCM2_VERIFIED_JOIN_CAPABLE = 0x58,
ID_FCM2_VERIFIED_JOIN_FAILED = 0x59,
ID_FCM2_VERIFIED_JOIN_ACCEPTED = 0x5A,
ID_FCM2_VERIFIED_JOIN_REJECTED = 0x5B,
ID_UDP_PROXY_GENERAL = 0x5C,
ID_SQLite3_EXEC = 0x5D,
ID_SQLite3_UNKNOWN_DB = 0x5E,
ID_SQLLITE_LOGGER = 0x5F,
ID_NAT_TYPE_DETECTION_REQUEST = 0x60,
ID_NAT_TYPE_DETECTION_RESULT = 0x61,
ID_ROUTER_2_INTERNAL = 0x62,
ID_ROUTER_2_FORWARDING_NO_PATH = 0x63,
ID_ROUTER_2_FORWARDING_ESTABLISHED = 0x64,
ID_ROUTER_2_REROUTED = 0x65,
ID_TEAM_BALANCER_INTERNAL = 0x66,
ID_TEAM_BALANCER_REQUESTED_TEAM_FULL = 0x67,
ID_TEAM_BALANCER_REQUESTED_TEAM_LOCKED = 0x68,
ID_TEAM_BALANCER_TEAM_REQUESTED_CANCELLED = 0x69,
ID_TEAM_BALANCER_TEAM_ASSIGNED = 0x6A,
ID_LIGHTSPEED_INTEGRATION = 0x6B,
ID_XBOX_LOBBY = 0x6C,
ID_TWO_WAY_AUTHENTICATION_INCOMING_CHALLENGE_SUCCESS = 0x6D,
ID_TWO_WAY_AUTHENTICATION_OUTGOING_CHALLENGE_SUCCESS = 0x6E,
ID_TWO_WAY_AUTHENTICATION_INCOMING_CHALLENGE_FAILURE = 0x6F,
ID_TWO_WAY_AUTHENTICATION_OUTGOING_CHALLENGE_FAILURE = 0x70,
ID_TWO_WAY_AUTHENTICATION_OUTGOING_CHALLENGE_TIMEOUT = 0x71,
ID_TWO_WAY_AUTHENTICATION_NEGOTIATION = 0x72,
ID_CLOUD_POST_REQUEST = 0x73,
ID_CLOUD_RELEASE_REQUEST = 0x74,
ID_CLOUD_GET_REQUEST = 0x75,
ID_CLOUD_GET_RESPONSE = 0x76,
ID_CLOUD_UNSUBSCRIBE_REQUEST = 0x77,
ID_CLOUD_SERVER_TO_SERVER_COMMAND = 0x78,
ID_CLOUD_SUBSCRIPTION_NOTIFICATION = 0x79,
ID_LIB_VOICE = 0x7A,
ID_RELAY_PLUGIN = 0x7B,
ID_NAT_REQUEST_BOUND_ADDRESSES = 0x7C,
ID_NAT_RESPOND_BOUND_ADDRESSES = 0x7D,
ID_FCM2_UPDATE_USER_CONTEXT = 0x7E,
ID_RESERVED_3 = 0x7F,
ID_RESERVED_4 = 0x80,
ID_RESERVED_5 = 0x81,
ID_RESERVED_6 = 0x82,
ID_RESERVED_7 = 0x83,
ID_RESERVED_8 = 0x84,
ID_RESERVED_9 = 0x85,
ID_PONG_ADDRESS_INFO = 0x86,
ID_NAT_TRAVERSAL_PING = 0x87,
ID_NAT_TRAVERSAL_PONG = 0x88,
ID_REQUEST_WEBSOCKET_CONNECTION = 0x89,
ID_ACK_FAILED_WEBSOCKET_REQUEST = 0x8A,
ID_AVAILABLE_5 = 0x8B,
ID_AVAILABLE_6 = 0x8C,
ID_AVAILABLE_7 = 0x8D,
ID_USER_PACKET_ENUM = 0x8E,
};

```
#### DefinitionEventType : __int32
```cpp
/* 46262 */
enum DefinitionEventType : __int32
{
LEAF = 0x0,
SEQUENCE = 0x1,
RANDOM = 0x2,
NONE_0 = 0x3,
};

```
#### Difficulty : __int32
```cpp
/* 5592 */
enum Difficulty : __int32
{
Peaceful = 0x0,
Easy = 0x1,
Normal_0 = 0x2,
Hard = 0x3,
Count_1 = 0x4,
Unknown = 0x5,
};

```
#### Direction::Type : __int8
```cpp
/* 31927 */
enum Direction::Type : __int8
{
SOUTH = 0x0,
WEST = 0x1,
NORTH = 0x2,
EAST = 0x3,
UNDEFINED = 0xFF,
};

```
#### DirtType : __int32
```cpp
/* 183671 */
enum DirtType : __int32
{
Normal_12 = 0x0,
Coarse = 0x1,
_count_31 = 0x2,
};

```
#### DisplayOrientation : __int32
```cpp
/* 6934 */
enum DisplayOrientation : __int32
{
None_8 = 0x0,
Landscape = 0x1,
Portrait = 0x2,
LandscapeFlipped = 0x3,
PortraitFlipped = 0x4,
};

```
#### DlcPerformanceTier : __int32
```cpp
/* 82545 */
enum DlcPerformanceTier : __int32
{
};

```
#### DoorBlock::DoorType : __int32
```cpp
/* 183756 */
enum DoorBlock::DoorType : __int32
{
OAK = 0x0,
SPRUCE = 0x1,
BIRCH = 0x2,
JUNGLE = 0x3,
ACACIA = 0x4,
DARKOAK = 0x5,
IRON = 0x6,
COUNT_13 = 0x7,
};

```
#### DoublePlantType : __int32
```cpp
/* 35199 */
enum DoublePlantType : __int32
{
Sunflower = 0x0,
Syringa = 0x1,
Grass = 0x2,
Fern_0 = 0x3,
Rose = 0x4,
Paeonia = 0x5,
_count_10 = 0x6,
};

```
#### DwellerComponent::DwellingType : __int32
```cpp
/* 53495 */
enum DwellerComponent::DwellingType : __int32
{
VillageDwelling = 0x0,
COUNT_2 = 0x1,
};

```
#### DwellerRole : __int32
```cpp
/* 53496 */
enum DwellerRole : __int32
{
DwellingInhabitant = 0x0,
DwellingDefender = 0x1,
DwellingHostile = 0x2,
DwellingPassive = 0x3,
COUNT_3 = 0x4,
};

```
#### EducationEditionOffer : __int32
```cpp
/* 5597 */
enum EducationEditionOffer : __int32
{
None_3 = 0x0,
RestOfWorld = 0x1,
China = 0x2,
};

```
#### EducationFeature : __int8
```cpp
/* 81159 */
enum EducationFeature : __int8
{
None_29 = 0x0,
Chemistry = 0x1,
Education = 0x2,
CodeBuilder = 0x4,
BaseCodeBuilder = 0x8,
};

```
#### EducationMetadata::ContentType : __int32
```cpp
/* 83526 */
enum EducationMetadata::ContentType : __int32
{
Invalid_18 = 0x0,
WorldLesson = 0x1,
NonWorldLesson = 0x2,
Count_18 = 0x3,
};

```
#### EducationMetadata::UserType : __int32
```cpp
/* 83527 */
enum EducationMetadata::UserType : __int32
{
Unknown_30 = 0x0,
StudentAndTeacher = 0x1,
Teacher_0 = 0x2,
Count_19 = 0x3,
};

```
#### EffectCommand::Mode : __int32
```cpp
/* 425152 */
enum EffectCommand::Mode : __int32
{
Add_6 = 0x0,
Clear_0 = 0x1,
};

```
#### EggCount : __int32
```cpp
/* 122545 */
enum EggCount : __int32
{
OneEgg = 0x0,
TwoEgg = 0x1,
ThreeEgg = 0x2,
FourEgg = 0x3,
_count_23 = 0x4,
};

```
#### ElementCategory : __int8
```cpp
/* 226409 */
enum ElementCategory : __int8
{
AlkaliMetal = 0x0,
AlkalineEarth = 0x1,
TransitionMetal = 0x2,
BasicMetal = 0x3,
Semimetal = 0x4,
Nonmetal = 0x5,
Halogen = 0x6,
NobleGas = 0x7,
Lanthanide = 0x8,
Actinide = 0x9,
Unknown_45 = 0xA,
};

```
#### ElementType : __int8
```cpp
/* 183769 */
enum ElementType : __int8
{
Unknown_44 = 0x0,
H = 0x1,
He = 0x2,
Li = 0x3,
Be = 0x4,
B = 0x5,
C = 0x6,
N = 0x7,
O = 0x8,
F = 0x9,
Ne = 0xA,
Na = 0xB,
Mg = 0xC,
Al = 0xD,
Si = 0xE,
P = 0xF,
S = 0x10,
Cl = 0x11,
Ar = 0x12,
K = 0x13,
Ca = 0x14,
Sc = 0x15,
Ti = 0x16,
V = 0x17,
Cr = 0x18,
Mn = 0x19,
Fe = 0x1A,
Co = 0x1B,
Ni = 0x1C,
Cu = 0x1D,
Zn = 0x1E,
Ga = 0x1F,
Ge = 0x20,
As = 0x21,
Se = 0x22,
Br = 0x23,
Kr = 0x24,
Rb = 0x25,
Sr = 0x26,
Y_0 = 0x27,
Zr = 0x28,
Nb = 0x29,
Mo = 0x2A,
Tc = 0x2B,
Ru = 0x2C,
Rh = 0x2D,
Pd = 0x2E,
Ag = 0x2F,
Cd = 0x30,
In = 0x31,
Sn = 0x32,
Sb = 0x33,
Te = 0x34,
I = 0x35,
Xe = 0x36,
Cs = 0x37,
Ba = 0x38,
La = 0x39,
Ce = 0x3A,
Pr = 0x3B,
Nd = 0x3C,
Pm = 0x3D,
Sm = 0x3E,
Eu = 0x3F,
Gd = 0x40,
Tb = 0x41,
Dy = 0x42,
Ho = 0x43,
Er = 0x44,
Tm = 0x45,
Yb = 0x46,
Lu = 0x47,
Hf = 0x48,
Ta = 0x49,
W = 0x4A,
Re = 0x4B,
Os = 0x4C,
Ir = 0x4D,
Pt = 0x4E,
Au = 0x4F,
Hg = 0x50,
Tl = 0x51,
Pb = 0x52,
Bi = 0x53,
Po = 0x54,
At = 0x55,
Rn = 0x56,
Fr = 0x57,
Ra = 0x58,
Ac = 0x59,
Th = 0x5A,
Pa = 0x5B,
U = 0x5C,
Np = 0x5D,
Pu = 0x5E,
Am = 0x5F,
Cm = 0x60,
Bk = 0x61,
Cf = 0x62,
Es = 0x63,
Fm = 0x64,
Md = 0x65,
No = 0x66,
Lr = 0x67,
Rf = 0x68,
Db = 0x69,
Sg = 0x6A,
Bh = 0x6B,
Hs = 0x6C,
Mt = 0x6D,
Ds = 0x6E,
Rg = 0x6F,
Cn = 0x70,
Nh = 0x71,
Fl = 0x72,
Mc = 0x73,
Lv = 0x74,
Ts = 0x75,
Og = 0x76,
Invalid_24 = 0x77,
};

```
#### EmotePacket::Flags : __int8
```cpp
/* 79606 */
enum EmotePacket::Flags : __int8
{
SERVER_SIDE = 0x1,
};

```
#### Enchant::Activation : __int32
```cpp
/* 116675 */
enum Enchant::Activation : __int32
{
EQUIPPED = 0x0,
HELD = 0x1,
SELF = 0x2,
_num_activations = 0x3,
_invalid = 0x4,
};

```
#### Enchant::CompatibilityID : __int32
```cpp
/* 185711 */
enum Enchant::CompatibilityID : __int32
{
NON_CONFLICT = 0x0,
DAMAGE = 0x1,
GATHERING = 0x2,
PROTECTION = 0x3,
FROSTSTRIDER = 0x4,
MENDFINITY = 0x5,
LOYALRIPTIDE = 0x6,
};

```
#### Enchant::Frequency : __int32
```cpp
/* 185265 */
enum Enchant::Frequency : __int32
{
Common_0 = 0x1E,
Uncommon_0 = 0xA,
Rare_0 = 0x3,
VeryRare = 0x1,
};

```
#### Enchant::Slot : __int32
```cpp
/* 180699 */
enum Enchant::Slot : __int32
{
NONE_12 = 0x0,
All_8 = 0xFFFFFFFF,
G_ARMOR = 0xF,
ARMOR_HEAD = 0x1,
ARMOR_TORSO = 0x2,
ARMOR_FEET = 0x4,
ARMOR_LEGS = 0x8,
SWORD = 0x10,
BOW = 0x20,
SPEAR = 0x8000,
CROSSBOW = 0x10000,
G_TOOL = 0x201C0,
HOE = 0x40,
SHEARS = 0x80,
FLINTSTEEL = 0x100,
SHIELD = 0x20000,
G_DIGGING = 0xE00,
AXE = 0x200,
PICKAXE = 0x400,
SHOVEL = 0x800,
FISHING_ROD = 0x1000,
CARROT_STICK = 0x2000,
ELYTRA = 0x4000,
};

```
#### Enchant::Type : __int32
```cpp
/* 33011 */
enum Enchant::Type : __int32
{
ArmorAll = 0x0,
ArmorFire = 0x1,
ArmorFall = 0x2,
ArmorExplosive = 0x3,
ArmorProjectile = 0x4,
ArmorThorns = 0x5,
WaterBreath = 0x6,
WaterSpeed = 0x7,
WaterAffinity = 0x8,
WeaponDamage = 0x9,
WeaponUndead = 0xA,
WeaponArthropod = 0xB,
WeaponKnockback = 0xC,
WeaponFire = 0xD,
WeaponLoot = 0xE,
MiningEfficiency = 0xF,
MiningSilkTouch = 0x10,
MiningDurability = 0x11,
MiningLoot = 0x12,
BowDamage = 0x13,
BowKnockback = 0x14,
BowFire = 0x15,
BowInfinity = 0x16,
FishingLoot = 0x17,
FishingLure = 0x18,
FrostWalker = 0x19,
Mending = 0x1A,
CurseBinding = 0x1B,
CurseVanishing = 0x1C,
TridentImpaling = 0x1D,
TridentRiptide = 0x1E,
TridentLoyalty = 0x1F,
TridentChanneling = 0x20,
CrossbowMultishot = 0x21,
CrossbowPiercing = 0x22,
CrossbowQuickCharge = 0x23,
NumEnchantments = 0x24,
InvalidEnchantment = 0x25,
};

```
#### EnchantResultType : __int8
```cpp
/* 33511 */
enum EnchantResultType : __int8
{
Fail_0 = 0x0,
Conflict = 0x1,
Increment = 0x2,
Enchant = 0x3,
};

```
#### EndCityPieces::SectionType : __int32
```cpp
/* 461977 */
enum EndCityPieces::SectionType : __int32
{
SectionTower = 0x0,
SectionFatTower = 0x1,
SectionBridge = 0x2,
SectionHouse = 0x3,
};

```
#### EndDragonFight::GatewayTask : __int8
```cpp
/* 169789 */
enum EndDragonFight::GatewayTask : __int8
{
GENERATE_PAIR = 0x0,
VERIFY_PAIR = 0x1,
NO_TASK = 0x2,
};

```
#### EndDragonFightVersion : __int8
```cpp
/* 169787 */
enum EndDragonFightVersion : __int8
{
Unknown_39 = 0x0,
v1_9_0_0 = 0x1,
};

```
#### EndPortalFrameBlock::CreateEndPortalResults : __int32
```cpp
/* 459394 */
enum EndPortalFrameBlock::CreateEndPortalResults : __int32
{
Success_15 = 0x0,
InvalidShape = 0x1,
Blocked = 0x2,
Count_28 = 0x3,
};

```
#### EquipmentFilter : __int32
```cpp
/* 51809 */
enum EquipmentFilter : __int32
{
MainHand = 0x0,
OffHand = 0x1,
Hands = 0x2,
Armor_0 = 0x3,
All_1 = 0x4,
Count_8 = 0x5,
};

```
#### EquipmentLocation : __int32
```cpp
/* 114311 */
enum EquipmentLocation : __int32
{
Any_2 = 0x0,
Hand = 0x1,
AnyArmor = 0x2,
HeadArmor = 0x3,
TorsoArmor = 0x4,
LegArmor = 0x5,
FeetArmor = 0x6,
};

```
#### EquipmentSlot : __int32
```cpp
/* 89151 */
enum EquipmentSlot : __int32
{
_none = 0xFFFFFFFF,
_begin = 0x0,
_handSlot = 0x0,
Mainhand_0 = 0x0,
Offhand_0 = 0x1,
_armorSlot = 0x2,
Head_2 = 0x2,
Torso_0 = 0x3,
Legs_1 = 0x4,
Feet_2 = 0x5,
_containerSlot = 0x6,
Hotbar = 0x6,
Inventory = 0x7,
EnderChest_0 = 0x8,
Saddle_0 = 0x9,
EntityArmor = 0xA,
Chest_0 = 0xB,
_count_19 = 0xC,
};

```
#### EventPacket::AgentResult : __int32
```cpp
/* 79629 */
enum EventPacket::AgentResult : __int32
{
ActionFail = 0x0,
ActionSuccess = 0x1,
QueryResultFalse = 0x2,
QueryResultTrue = 0x3,
};

```
#### EventPacket::Type : __int32
```cpp
/* 13309 */
enum EventPacket::Type : __int32
{
Achievement = 0x0,
Interaction = 0x1,
PortalCreated = 0x2,
PortalUsed = 0x3,
MobKilled = 0x4,
CauldronUsed = 0x5,
PlayerDied = 0x6,
BossKilled = 0x7,
AgentCommand = 0x8,
AgentCreated = 0x9,
PatternRemoved = 0xA,
SlashCommand_0 = 0xB,
FishBucketed = 0xC,
MobBorn = 0xD,
PetDied = 0xE,
POICauldronUsed = 0xF,
ComposterUsed = 0x10,
BellUsed = 0x11,
ActorDefinition = 0x12,
RaidUpdate = 0x13,
PlayerMovementAnomaly = 0x14,
PlayerMovementCorrected = 0x15,
HoneyHarvested = 0x16,
};

```
#### EventResult : __int32
```cpp
/* 475 */
enum EventResult : __int32
{
StopProcessing = 0x0,
KeepGoing = 0x1,
};

```
#### ExecuteCommand::Mode : __int32
```cpp
/* 425338 */
enum ExecuteCommand::Mode : __int32
{
Execute = 0x0,
Detect = 0x1,
};

```
#### ExperienceOrb::DropType : __int8
```cpp
/* 48669 */
enum ExperienceOrb::DropType : __int8
{
NoType = 0x0,
FromBlock = 0x1,
FromMob = 0x2,
FromPlayer = 0x3,
};

```
#### ExpressionOp : __int32
```cpp
/* 47717 */
enum ExpressionOp : __int32
{
Unknown_24 = 0xFFFFFFFF,
LeftParenthesis = 0x0,
RightParenthesis = 0x1,
LeftBracket = 0x2,
RightBracket = 0x3,
Negate = 0x4,
LogicalNot = 0x5,
Abs = 0x6,
Cos = 0x7,
Sin = 0x8,
Clamp = 0x9,
Lerp = 0xA,
LerpRotate = 0xB,
Max_1 = 0xC,
Min_1 = 0xD,
Round = 0xE,
Trunc = 0xF,
Ceil = 0x10,
Floor = 0x11,
Mod = 0x12,
Add = 0x13,
Div = 0x14,
Mul = 0x15,
Exp = 0x16,
Ln = 0x17,
Sqrt = 0x18,
Pow = 0x19,
Random_1 = 0x1A,
DieRoll = 0x1B,
QueryFunction = 0x1C,
GenericQueryFunction = 0x1D,
ArrayVariable = 0x1E,
EntityVariable = 0x1F,
TempVariable = 0x20,
HashedString = 0x21,
GeometryVariable = 0x22,
MaterialVariable = 0x23,
TextureVariable = 0x24,
LessThan_1 = 0x25,
LessEqual = 0x26,
GreaterEqual = 0x27,
GreaterThan_1 = 0x28,
LogicalEqual = 0x29,
LogicalNotEqual = 0x2A,
LogicalOr = 0x2B,
LogicalAnd = 0x2C,
Conditional = 0x2D,
ConditionalElse = 0x2E,
Float_2 = 0x2F,
Pi = 0x30,
Array = 0x31,
Geometry_0 = 0x32,
ModelPart = 0x33,
Material = 0x34,
Texture = 0x35,
Assignment = 0x36,
Semicolon = 0x37,
Return = 0x38,
Comma_0 = 0x39,
This = 0x3A,
Count_6 = 0x3B,
};

```
#### ExternalApp : __int32
```cpp
/* 480113 */
enum ExternalApp : __int32
{
};

```
#### Facing::Name : __int8
```cpp
/* 31929 */
enum Facing::Name : __int8
{
DOWN = 0x0,
UP = 0x1,
NORTH_0 = 0x2,
SOUTH_0 = 0x3,
WEST_0 = 0x4,
EAST_0 = 0x5,
MAX = 0x6,
NOT_DEFINED = 0x6,
NUM_CULLING_IDS = 0x7,
};

```
#### Facing::Rotation : __int32
```cpp
/* 31930 */
enum Facing::Rotation : __int32
{
NONE = 0x0,
CCW = 0x1,
OPP = 0x2,
CW = 0x3,
};

```
#### FallingBlock::State : __int32
```cpp
/* 170704 */
enum FallingBlock::State : __int32
{
Falling = 0x0,
WaitRemoval = 0x1,
};

```
#### FeatureOptionID : __int32
```cpp
/* 77444 */
enum FeatureOptionID : __int32
{
None_25 = 0x0,
NetworkLogAllPackets = 0x1,
Scoreboards = 0x2,
Functions = 0x3,
UIAsyncLoadingAndAnimations = 0x4,
Allow3rdPartyServerSplitscreen = 0x5,
ExperimentalGameplayInAllWorlds = 0x6,
Hummingbird = 0x7,
HummingbirdDebugging = 0x8,
UIRefresh = 0x9,
Scripting_0 = 0xA,
Realms_1 = 0xB,
RealmsContent = 0xC,
EnableLoadTimer = 0xD,
ExternalWorldTemplatePackSources = 0xE,
Win10Subscriptions = 0xF,
PlayerRenaming = 0x10,
PersonaBackend = 0x11,
PersonaSkin = 0x12,
PlayFabInsightsTelemetry = 0x13,
PersonaEnabled = 0x14,
PersonaServiceEnabled = 0x15,
PersonaTestCatalog = 0x16,
PersonaCape = 0x17,
PersonaEmotes = 0x18,
StorefrontTestLayouts = 0x19,
RenderDragonRenderPath = 0x1A,
BaseGameVersioniningTestPacks = 0x1B,
LevelStoragePerfLog = 0x1C,
TrueTypeFontLoading = 0x1D,
PauseMenuOnFocusLost = 0x1E,
Count_14 = 0x1F,
};

```
#### FertilizerType : __int8
```cpp
/* 181089 */
enum FertilizerType : __int8
{
Bonemeal = 0x0,
Rapid = 0x1,
};

```
#### FileArchiver::ExportType : __int32
```cpp
/* 103133 */
enum FileArchiver::ExportType : __int32
{
Level_0 = 0x0,
Template = 0x1,
};

```
#### FileArchiver::Outcome : __int32
```cpp
/* 103115 */
enum FileArchiver::Outcome : __int32
{
Success_11 = 0x0,
FailureUnknown = 0x1,
FailureNoFile = 0x2,
FailureZipError = 0x3,
FailurePremiumContent = 0x4,
FailureEditionMismatch = 0x5,
};

```
#### FileArchiver::State : __int32
```cpp
/* 103074 */
enum FileArchiver::State : __int32
{
Idle_0 = 0x0,
Importing = 0x1,
Exporting_0 = 0x2,
};

```
#### FilePickerSettings::PickerType : __int32
```cpp
/* 186676 */
enum FilePickerSettings::PickerType : __int32
{
Invalid_26 = 0x0,
Open_1 = 0x1,
Save_1 = 0x2,
};

```
#### FileReadResult : __int32
```cpp
/* 5594 */
enum FileReadResult : __int32
{
SUCCESS = 0x0,
FAILED_TO_OPEN_FILE = 0x1,
MALFORMED = 0x2,
};

```
#### FileSystemMode : __int32
```cpp
/* 480026 */
enum FileSystemMode : __int32
{
ReadWrite_0 = 0x0,
ReadOnly_0 = 0x1,
};

```
#### FileType : __int32
```cpp
/* 422546 */
enum FileType : __int32
{
Invalid_28 = 0x0,
Zip_0 = 0x1,
EncryptedZip = 0x2,
Other_2 = 0x3,
};

```
#### FillCommand::FillMode : __int32
```cpp
/* 425433 */
enum FillCommand::FillMode : __int32
{
Replace_1 = 0x0,
Destroy_0 = 0x1,
Hollow_0 = 0x2,
Outline = 0x3,
Keep = 0x4,
};

```
#### FilterGroup::CollectionType : __int32
```cpp
/* 9578 */
enum FilterGroup::CollectionType : __int32
{
AND = 0x0,
OR = 0x1,
NOT = 0x2,
};

```
#### FilterOperator : __int16
```cpp
/* 9615 */
enum FilterOperator : __int16
{
Equal = 0x0,
NotEqual = 0x1,
GreaterThan_0 = 0x2,
LessThan_0 = 0x3,
GreaterThanOrEqual = 0x4,
LessThanOrEqual = 0x5,
};

```
#### FilterParamOption : __int8
```cpp
/* 114140 */
enum FilterParamOption : __int8
{
None_42 = 0x0,
EmptyDefaultString = 0x1,
};

```
#### FilterParamRequirement : __int32
```cpp
/* 114115 */
enum FilterParamRequirement : __int32
{
Required = 0x0,
Optional = 0x1,
};

```
#### FilterParamType : __int32
```cpp
/* 114114 */
enum FilterParamType : __int32
{
Bool_1 = 0x0,
Int_5 = 0x1,
Float_6 = 0x2,
String_4 = 0x3,
};

```
#### FilterResult : __int32
```cpp
/* 175608 */
enum FilterResult : __int32
{
ShowPrioritized = 0x0,
Show = 0x1,
Disable = 0x2,
Hide = 0x3,
};

```
#### FilterSubject : __int16
```cpp
/* 9614 */
enum FilterSubject : __int16
{
Self = 0x0,
Other = 0x1,
Player = 0x2,
Target = 0x3,
Parent = 0x4,
Baby = 0x5,
Block = 0x6,
COUNT_1 = 0x7,
};

```
#### FireworkChargeItem::Shape : __int32
```cpp
/* 170712 */
enum FireworkChargeItem::Shape : __int32
{
SHAPE_NONE = 0x0,
SHAPE_LARGE_BALL = 0x1,
SHAPE_STAR = 0x2,
SHAPE_HEAD_CREEPER = 0x3,
SHAPE_BURST = 0x4,
SHAPE_COUNT = 0x5,
};

```
#### FishPattern : __int32
```cpp
/* 124442 */
enum FishPattern : __int32
{
PATTERN_1 = 0x0,
PATTERN_2 = 0x1,
PATTERN_3 = 0x2,
PATTERN_4 = 0x3,
PATTERN_5 = 0x4,
PATTERN_6 = 0x5,
COUNT_8 = 0x6,
};

```
#### Flip : __int32
```cpp
/* 223287 */
enum Flip : __int32
{
None_50 = 0x0,
RotateCW = 0x1,
RotateCCW = 0x2,
Rotate180_0 = 0x3,
MirrorX = 0x4,
DontRotate = 0x5,
};

```
#### FlowerBlock::Type : __int32
```cpp
/* 251029 */
enum FlowerBlock::Type : __int32
{
Yellow_3 = 0x0,
Red_5 = 0x1,
WitherRose_0 = 0x2,
};

```
#### FlowerType : __int32
```cpp
/* 183717 */
enum FlowerType : __int32
{
Poppy_0 = 0x0,
Orchid = 0x1,
Allium_0 = 0x2,
Houstonia = 0x3,
TulipRed = 0x4,
TulipOrange = 0x5,
TulipWhite = 0x6,
TulipPink = 0x7,
Oxeye = 0x8,
Cornflower_0 = 0x9,
LilyOfTheValley_0 = 0xA,
_count_37 = 0xB,
};

```
#### FocusImpact : __int8
```cpp
/* 89287 */
enum FocusImpact : __int8
{
Neutral = 0x0,
ActivateFocus = 0x1,
DeactivateFocus = 0x2,
};

```
#### FoodItemComponent::OnUseAction : __int32
```cpp
/* 173072 */
enum FoodItemComponent::OnUseAction : __int32
{
NONE_11 = 0xFFFFFFFF,
CHORUS_TELEPORT = 0x0,
SUSPICIOUS_STEW_EFFECT = 0x1,
};

```
#### FreezeOnHitSubcomponent::Shape : __int8
```cpp
/* 174011 */
enum FreezeOnHitSubcomponent::Shape : __int8
{
Cube = 0x0,
Sphere = 0x1,
};

```
#### FullscreenMode : __int32
```cpp
/* 480114 */
enum FullscreenMode : __int32
{
Windowed = 0x0,
Fullscreen = 0x1,
};

```
#### FunctionState : __int8
```cpp
/* 95066 */
enum FunctionState : __int8
{
Uninitialized_0 = 0x1,
EngineVersionNotInitialized = 0x2,
Valid_1 = 0x3,
};

```
#### FurnaceBlockActor::$78D9F25919EA3E1AC07246132E3A6E19 : __int32
```cpp
/* 175423 */
enum FurnaceBlockActor::$78D9F25919EA3E1AC07246132E3A6E19 : __int32
{
SLOT_INGREDIENT_0 = 0x0,
SLOT_FUEL_0 = 0x1,
SLOT_RESULT = 0x2,
NUM_ITEMS = 0x3,
};

```
#### FurnaceContainerData : __int32
```cpp
/* 175422 */
enum FurnaceContainerData : __int32
{
SetTickCount = 0x0,
SetLitTime = 0x1,
SetLitDuration = 0x2,
SetStoredXP = 0x3,
};

```
#### GameRule::Type : __int8
```cpp
/* 946 */
enum GameRule::Type : __int8
{
Invalid = 0x0,
Bool = 0x1,
Int = 0x2,
Float = 0x3,
};

```
#### GameRules::GameRulesIndex : __int32
```cpp
/* 13184 */
enum GameRules::GameRulesIndex : __int32
{
INVALID_GAME_RULE = 0xFFFFFFFF,
COMMAND_BLOCK_OUTPUT = 0x0,
DO_DAYLIGHT_CYCLE = 0x1,
DO_ENTITY_DROPS = 0x2,
DO_FIRE_TICK = 0x3,
DO_MOB_LOOT = 0x4,
DO_MOB_SPAWNING = 0x5,
DO_TILE_DROPS = 0x6,
DO_WEATHER_CYCLE = 0x7,
DROWNING_DAMAGE = 0x8,
FALL_DAMAGE = 0x9,
FIRE_DAMAGE = 0xA,
KEEP_INVENTORY = 0xB,
MOB_GRIEFING = 0xC,
PVP = 0xD,
SHOW_COORDINATES = 0xE,
DO_NATURAL_REGENERATION = 0xF,
DO_TNT_EXPLODE = 0x10,
SEND_COMMAND_FEEDBACK = 0x11,
EXPERIMENTAL_GAMEPLAY = 0x12,
MAX_COMMAND_CHAIN_LENGTH = 0x13,
DO_INSOMNIA = 0x14,
COMMAND_BLOCKS_ENABLED = 0x15,
RANDOM_TICK_SPEED = 0x16,
DO_IMMEDIATE_RESPAWN = 0x17,
SHOW_DEATH_MESSAGES = 0x18,
FUNCTION_COMMAND_LIMIT = 0x19,
PLAYER_SPAWN_RADIUS = 0x1A,
SHOW_TAGS = 0x1B,
VANILLA_GAME_RULE_COUNT = 0x1C,
GLOBAL_MUTE = 0x1C,
ALLOW_DESTRUCTIVE_OBJECTS = 0x1D,
ALLOW_MOBS = 0x1E,
CODE_BUILDER = 0x1F,
EDU_GAME_RULE_COUNT = 0x20,
};

```
#### GameType : __int32
```cpp
/* 5593 */
enum GameType : __int32
{
Undefined = 0xFFFFFFFF,
Survival = 0x0,
Creative = 0x1,
Adventure = 0x2,
SurvivalViewer = 0x3,
CreativeViewer = 0x4,
Default = 0x5,
WorldDefault = 0x0,
};

```
#### GameVersion::Octet : __int32
```cpp
/* 5655 */
enum GameVersion::Octet : __int32
{
MAJOR = 0x0,
MINOR = 0x1,
PATCH = 0x2,
REVISION = 0x3,
BETA = 0x4,
NUM_OCTETS = 0x5,
INVALID = 0x5,
};

```
#### GeneratorType : __int32
```cpp
/* 5595 */
enum GeneratorType : __int32
{
Legacy = 0x0,
Overworld = 0x1,
Flat = 0x2,
Nether = 0x3,
TheEnd = 0x4,
Undefined_0 = 0x5,
};

```
#### HandSlot : __int32
```cpp
/* 13188 */
enum HandSlot : __int32
{
Mainhand = 0x0,
Offhand = 0x1,
_count_0 = 0x2,
};

```
#### HardcodedSpawnAreaType : __int8
```cpp
/* 34079 */
enum HardcodedSpawnAreaType : __int8
{
None_11 = 0x0,
NetherFortress = 0x1,
WitchHut_0 = 0x2,
OceanMonument = 0x3,
Village_Deprecated = 0x4,
PillagerOutpost = 0x5,
NewVillage_Deprecated = 0x6,
_Count = 0x7,
};

```
#### HarvestFarmBlockGoal::Task : __int32
```cpp
/* 122533 */
enum HarvestFarmBlockGoal::Task : __int32
{
NONE_9 = 0xFFFFFFFF,
REAP = 0x0,
SOW = 0x1,
};

```
#### HatchLevel : __int32
```cpp
/* 227743 */
enum HatchLevel : __int32
{
NoCracks = 0x0,
Cracked_0 = 0x1,
MaxCracked = 0x2,
_count_45 = 0x3,
};

```
#### HitResultType : __int32
```cpp
/* 13187 */
enum HitResultType : __int32
{
TILE = 0x0,
ENTITY = 0x1,
ENTITY_OUT_OF_RANGE = 0x2,
NO_HIT = 0x3,
};

```
#### HorseArmorItem::HorseArmorTier : __int32
```cpp
/* 183761 */
enum HorseArmorItem::HorseArmorTier : __int32
{
TIER_NONE = 0x0,
TIER_LEATHER_0 = 0x1,
TIER_IRON_0 = 0x2,
TIER_GOLD_0 = 0x3,
TIER_DIAMOND_0 = 0x4,
};

```
#### HorseEquipContainerController::EquipSlot : __int32
```cpp
/* 456093 */
enum HorseEquipContainerController::EquipSlot : __int32
{
SLOT_SADDLE = 0x0,
SLOT_ARMOR = 0x1,
};

```
#### HorseFlags : __int32
```cpp
/* 124180 */
enum HorseFlags : __int32
{
FLAG_SADDLE = 0x4,
FLAG_BRED = 0x10,
FLAG_EATING = 0x20,
FLAG_STANDING = 0x40,
FLAG_OPEN_MOUTH = 0x80,
};

```
#### HorseIds : __int32
```cpp
/* 124181 */
enum HorseIds : __int32
{
DATA_ID_HORSE_FLAGS = 0x10,
DATA_ID_TYPE = 0x13,
DATA_ID_TYPE_VARIANT = 0x14,
DATA_ID_OWNER_UUID = 0x15,
};

```
#### HorseInventoryEnum : __int32
```cpp
/* 114716 */
enum HorseInventoryEnum : __int32
{
INV_SLOT_SADDLE = 0x0,
INV_SLOT_ARMOR = 0x1,
INV_BASE_COUNT = 0x2,
};

```
#### HorseMarkings : __int32
```cpp
/* 124183 */
enum HorseMarkings : __int32
{
MARKING_NONE = 0x0,
MARKING_WHITE_DETAILS = 0x1,
MARKING_WHITE_FIELDS = 0x2,
MARKING_WHITE_DOTS = 0x3,
MARKING_BLACK_DOTS = 0x4,
MARKING_COUNT = 0x5,
};

```
#### HorseType : __int32
```cpp
/* 114715 */
enum HorseType : __int32
{
TYPE_UNSET = 0xFFFFFFFF,
TYPE_HORSE = 0x0,
TYPE_DONKEY = 0x1,
TYPE_MULE = 0x2,
TYPE_UNDEAD = 0x3,
TYPE_SKELETON = 0x4,
TYPE_COUNT = 0x5,
};

```
#### HorseVariant : __int32
```cpp
/* 124182 */
enum HorseVariant : __int32
{
VARIANT_WHITE = 0x0,
VARIANT_CREAMY = 0x1,
VARIANT_CHESTNUT = 0x2,
VARIANT_BROWN = 0x3,
VARIANT_BLACK = 0x4,
VARIANT_GRAY = 0x5,
VARIANT_DARKBROWN = 0x6,
VARIANT_COUNT = 0x7,
};

```
#### HugeMushroomBlock::Type : __int32
```cpp
/* 251035 */
enum HugeMushroomBlock::Type : __int32
{
Brown_2 = 0x0,
Red_6 = 0x1,
};

```
#### HurtByType : __int32
```cpp
/* 100821 */
enum HurtByType : __int32
{
UNDEFINED_0 = 0x0,
HURT_BY_ACTOR = 0x1,
HURT_BY_PROJECTILE = 0x2,
HURT_BY_BLOCK = 0x3,
HurtByType_Count = 0x4,
};

```
#### IFileChunkUploader::UploadStreamResult : __int32
```cpp
/* 101568 */
enum IFileChunkUploader::UploadStreamResult : __int32
{
Success_10 = 0x0,
Failure = 0x1,
FailureForbidden = 0x2,
None_37 = 0x3,
};

```
#### IMinecraftEventing::ClubsEngagementAction : __int32
```cpp
/* 44640 */
enum IMinecraftEventing::ClubsEngagementAction : __int32
{
Like = 0x0,
Unlike = 0x1,
Post = 0x2,
Delete = 0x3,
Report = 0x4,
Comment = 0x5,
};

```
#### IMinecraftEventing::ClubsEngagementTargetType : __int32
```cpp
/* 44646 */
enum IMinecraftEventing::ClubsEngagementTargetType : __int32
{
Unknown_12 = 0x0,
ImageFeedPost = 0x1,
TextFeedPost = 0x2,
Comment_0 = 0x3,
};

```
#### IMinecraftEventing::ClubsFeedScreenSource : __int32
```cpp
/* 44634 */
enum IMinecraftEventing::ClubsFeedScreenSource : __int32
{
PlayScreen = 0x0,
PauseScreen = 0x1,
};

```
#### IMinecraftEventing::ConnectionFailureReason : __int32
```cpp
/* 45298 */
enum IMinecraftEventing::ConnectionFailureReason : __int32
{
Unknown_19 = 0xFFFFFFFF,
MismatchedMinecraftProtocol = 0x1,
MismatchedRaknetVersion = 0x2,
};

```
#### IMinecraftEventing::DayOneExperienceState : __int32
```cpp
/* 44628 */
enum IMinecraftEventing::DayOneExperienceState : __int32
{
Started = 0x0,
CompletedWithoutWorlds = 0x1,
CompletedWithImportSkipped = 0x2,
CompletedWithImport = 0x3,
};

```
#### IMinecraftEventing::DeviceAccountFailurePhase : __int32
```cpp
/* 45295 */
enum IMinecraftEventing::DeviceAccountFailurePhase : __int32
{
Unknown_18 = 0x0,
SignIn = 0x1,
LoadCredentials = 0x2,
TitleKey = 0x3,
StoreVerify = 0x4,
PlayFabCreate_Configured = 0x5,
PlayFabCreate = 0x6,
};

```
#### IMinecraftEventing::EduSignInStage : __int32
```cpp
/* 45301 */
enum IMinecraftEventing::EduSignInStage : __int32
{
Unknown_20 = 0x0,
AttemptingActiveDirectory = 0x1,
FailedActiveDirectory = 0x2,
AttemptingMuts = 0x3,
FailedMuts = 0x4,
PresentingingEula = 0x5,
Success_7 = 0x6,
RefreshingActiveDirectory = 0x7,
RefreshActiveDirectorySuccess = 0x8,
RefreshActiveDirectoryFailed = 0x9,
};

```
#### IMinecraftEventing::EducationLessonAction : __int32
```cpp
/* 44616 */
enum IMinecraftEventing::EducationLessonAction : __int32
{
Start = 0x0,
Continue = 0x1,
Restart = 0x2,
Host_0 = 0x3,
Join = 0x4,
Finish = 0x5,
};

```
#### IMinecraftEventing::ElementConstructorUseType : __int32
```cpp
/* 45291 */
enum IMinecraftEventing::ElementConstructorUseType : __int32
{
Created = 0x0,
Entered = 0x1,
};

```
#### IMinecraftEventing::ExportOutcome : __int32
```cpp
/* 44622 */
enum IMinecraftEventing::ExportOutcome : __int32
{
Failed_1 = 0x0,
Success_3 = 0x1,
};

```
#### IMinecraftEventing::ExportStage : __int32
```cpp
/* 45300 */
enum IMinecraftEventing::ExportStage : __int32
{
Initiated = 0x0,
Completed_0 = 0x1,
};

```
#### IMinecraftEventing::FileTransmissionDirection : __int32
```cpp
/* 45292 */
enum IMinecraftEventing::FileTransmissionDirection : __int32
{
Download = 0x0,
Upload = 0x1,
};

```
#### IMinecraftEventing::FileTransmissionState : __int32
```cpp
/* 45293 */
enum IMinecraftEventing::FileTransmissionState : __int32
{
Failed_4 = 0x0,
Started_0 = 0x1,
Completed = 0x2,
Resumed = 0x3,
Canceled_0 = 0xFFFFFFFF,
};

```
#### IMinecraftEventing::FileTransmissionType : __int32
```cpp
/* 45294 */
enum IMinecraftEventing::FileTransmissionType : __int32
{
Realm_file = 0x1,
Dlc = 0x2,
Remix3D_DEPRECATED = 0x3,
DlcUpdate_Auto = 0x4,
DlcUpdate_User = 0x5,
};

```
#### IMinecraftEventing::NetworkType : __int32
```cpp
/* 45285 */
enum IMinecraftEventing::NetworkType : __int32
{
Local_2 = 0x0,
LAN = 0x1,
External = 0x2,
Friend = 0x3,
Realm = 0x4,
ThirdParty = 0x5,
};

```
#### IMinecraftEventing::OpenCodeMethod : __int32
```cpp
/* 44604 */
enum IMinecraftEventing::OpenCodeMethod : __int32
{
TouchHUD = 0x0,
Keypress = 0x1,
Command_1 = 0x2,
};

```
#### IMinecraftEventing::PetDeathContext : __int32
```cpp
/* 44658 */
enum IMinecraftEventing::PetDeathContext : __int32
{
DiedOfOtherCause = 0x0,
PlayerMurdered = 0x1,
OwnerMurdered = 0x2,
MobMurdered = 0x3,
};

```
#### IMinecraftEventing::PromotionType : __int32
```cpp
/* 45303 */
enum IMinecraftEventing::PromotionType : __int32
{
Featured = 0x0,
Default_6 = 0x1,
None_19 = 0x2,
};

```
#### IMinecraftEventing::PurchaseResult : __int32
```cpp
/* 45296 */
enum IMinecraftEventing::PurchaseResult : __int32
{
Success_6 = 0x1,
Canceled_1 = 0x0,
Failed_5 = 0xFFFFFFFF,
};

```
#### IMinecraftEventing::RealmConnectionFlow : __int32
```cpp
/* 45288 */
enum IMinecraftEventing::RealmConnectionFlow : __int32
{
PlayScreen_0 = 0x0,
SettingsScreen = 0x1,
InviteLink = 0x2,
WhiteList = 0x3,
Marketplace = 0x4,
CreateScreen = 0x5,
};

```
#### IMinecraftEventing::RealmConnectionLambda : __int32
```cpp
/* 45289 */
enum IMinecraftEventing::RealmConnectionLambda : __int32
{
CompletedCallback = 0x0,
RetryCallback = 0x1,
ProgressScreenTickCallback = 0x2,
ProgressScreenOnCancelCallback = 0x3,
GameServerConnectProgressCallback = 0x4,
};

```
#### IMinecraftEventing::RealmConnectionResult : __int32
```cpp
/* 45290 */
enum IMinecraftEventing::RealmConnectionResult : __int32
{
Success_5 = 0x0,
SuccessWithWarning = 0x1,
FailWithUnnassignedDevVersion = 0x2,
Fail_1 = 0x3,
Retry = 0x4,
CancelByUser = 0x5,
InvalidCallback = 0x6,
Unknown_17 = 0x7,
TimedOut = 0x8,
};

```
#### IMinecraftEventing::ServerConnectionOutcome : __int32
```cpp
/* 45286 */
enum IMinecraftEventing::ServerConnectionOutcome : __int32
{
Success_4 = 0x0,
Failed_2 = 0x1,
Failed_UserOffline = 0x2,
Failed_ServerFull = 0x3,
Failed_ServerOffline = 0x4,
};

```
#### IMinecraftEventing::ShareMode : __int32
```cpp
/* 45299 */
enum IMinecraftEventing::ShareMode : __int32
{
Share = 0x1,
Copy = 0x2,
};

```
#### IMinecraftEventing::SignInStage : __int32
```cpp
/* 45287 */
enum IMinecraftEventing::SignInStage : __int32
{
Unknown_16 = 0x0,
Starting = 0x1,
Failed_3 = 0x2,
Canceled = 0x3,
Succeeded = 0x4,
Succeeded_New_Account = 0x5,
Failed_Create = 0x6,
};

```
#### IMinecraftEventing::StoreType : __int32
```cpp
/* 45297 */
enum IMinecraftEventing::StoreType : __int32
{
Store = 0x0,
DressingRoom = 0x1,
};

```
#### IMinecraftEventing::StructureBlockActionType : __int32
```cpp
/* 44542 */
enum IMinecraftEventing::StructureBlockActionType : __int32
{
Unknown_11 = 0xFFFFFFFF,
Save = 0x0,
Load = 0x1,
Export = 0x2,
Export3D = 0x3,
LeaveScreen = 0x4,
};

```
#### IdentityDefinition::Type : __int8
```cpp
/* 70053 */
enum IdentityDefinition::Type : __int8
{
Invalid_14 = 0x0,
Player_2 = 0x1,
Entity_2 = 0x2,
FakePlayer = 0x3,
};

```
#### InHandUpdateType : __int8
```cpp
/* 181498 */
enum InHandUpdateType : __int8
{
NONE_13 = 0x0,
UPDATE = 0x1,
SWAP = 0x2,
};

```
#### InMemoryAccessMode : __int32
```cpp
/* 463110 */
enum InMemoryAccessMode : __int32
{
Read = 0x0,
Write = 0x1,
};

```
#### InputMode : __int32
```cpp
/* 44576 */
enum InputMode : __int32
{
Undefined_7 = 0x0,
Mouse = 0x1,
Touch = 0x2,
GamePad = 0x3,
MotionController_0 = 0x4,
Count_5 = 0x5,
};

```
#### IntellisenseUtils::MatcherOptions : __int8
```cpp
/* 93423 */
enum IntellisenseUtils::MatcherOptions : __int8
{
NONE_7 = 0x0,
HIGHLIGHT = 0x1,
CASE_SENSITIVE = 0x2,
};

```
#### InteractPacket::Action : __int8
```cpp
/* 79706 */
enum InteractPacket::Action : __int8
{
StopRiding = 0x3,
InteractUpdate = 0x4,
NpcOpen = 0x5,
OpenInventory = 0x6,
};

```
#### InventorySource::InventorySourceFlags : __int32
```cpp
/* 33268 */
enum InventorySource::InventorySourceFlags : __int32
{
NoFlag = 0x0,
WorldInteraction_Random = 0x1,
};

```
#### InventorySourceType : __int32
```cpp
/* 33266 */
enum InventorySourceType : __int32
{
InvalidInventory = 0xFFFFFFFF,
ContainerInventory = 0x0,
GlobalInventory = 0x1,
WorldInteraction = 0x2,
CreativeInventory = 0x3,
UntrackedInteractionUI = 0x64,
NonImplementedFeatureTODO = 0x1869F,
};

```
#### InventoryTransactionError : __int32
```cpp
/* 33512 */
enum InventoryTransactionError : __int32
{
Unknown_4 = 0x0,
NoError = 0x1,
BalanceMismatch = 0x2,
SourceItemMismatch = 0x3,
InventoryMismatch = 0x4,
SizeMismatch = 0x5,
AuthorityMismatch = 0x6,
StateMismatch = 0x7,
ApiDenied = 0x8,
};

```
#### ItemAcquisitionMethod : __int32
```cpp
/* 13214 */
enum ItemAcquisitionMethod : __int32
{
};

```
#### ItemAcquisitionMethod_0 : __int32
```cpp
/* 43301 */
enum ItemAcquisitionMethod_0 : __int32
{
Unknown_8 = 0xFFFFFFFF,
None_16 = 0x0,
PickedUp = 0x1,
Crafted_0 = 0x2,
TakenFromChest = 0x3,
TakenFromEnderchest = 0x4,
Bought = 0x5,
Anvil = 0x6,
Smelted = 0x7,
Brewed = 0x8,
Filled_0 = 0x9,
Trading_0 = 0xA,
Fishing = 0xB,
Container = 0xD,
};

```
#### ItemAddType : __int32
```cpp
/* 174692 */
enum ItemAddType : __int32
{
All_7 = 0x0,
Partial_0 = 0x1,
None_49 = 0x2,
};

```
#### ItemColor : __int8
```cpp
/* 181069 */
enum ItemColor : __int8
{
Black_1 = 0x0,
Red_3 = 0x1,
Green_1 = 0x2,
Brown_1 = 0x3,
Blue_1 = 0x4,
Purple_1 = 0x5,
Cyan_1 = 0x6,
Silver_1 = 0x7,
Gray_1 = 0x8,
Pink_1 = 0x9,
Lime_0 = 0xA,
Yellow_1 = 0xB,
LightBlue_0 = 0xC,
Magenta_1 = 0xD,
Orange_1 = 0xE,
White_1 = 0xF,
_count_26 = 0x10,
};

```
#### ItemPlaceType : __int32
```cpp
/* 174690 */
enum ItemPlaceType : __int32
{
All_6 = 0x0,
One_0 = 0x1,
};

```
#### ItemReleaseInventoryTransaction::ActionType : __int32
```cpp
/* 173074 */
enum ItemReleaseInventoryTransaction::ActionType : __int32
{
Release_0 = 0x0,
Use_0 = 0x1,
};

```
#### ItemSetType : __int32
```cpp
/* 174691 */
enum ItemSetType : __int32
{
Place_3 = 0x0,
Swap_0 = 0x1,
Add_5 = 0x2,
None_48 = 0x3,
};

```
#### ItemTakeType : __int32
```cpp
/* 174689 */
enum ItemTakeType : __int32
{
All_5 = 0x0,
Half = 0x1,
One = 0x2,
};

```
#### ItemTransferAmount::ItemTransferAmountTag : __int32
```cpp
/* 174687 */
enum ItemTransferAmount::ItemTransferAmountTag : __int32
{
RequestAmount = 0x0,
TakeType = 0x1,
PlaceType = 0x2,
};

```
#### ItemUseInventoryTransaction::ActionType : __int32
```cpp
/* 180450 */
enum ItemUseInventoryTransaction::ActionType : __int32
{
Place_4 = 0x0,
Use_1 = 0x1,
Destroy = 0x2,
};

```
#### ItemUseMethod : __int32
```cpp
/* 13212 */
enum ItemUseMethod : __int32
{
};

```
#### ItemUseMethod_0 : __int32
```cpp
/* 43215 */
enum ItemUseMethod_0 : __int32
{
Unknown_6 = 0xFFFFFFFF,
EquipArmor = 0x0,
Eat_1 = 0x1,
Attack_0 = 0x2,
Consume = 0x3,
Throw_0 = 0x4,
Shoot_0 = 0x5,
Place_0 = 0x6,
FillBottle = 0x7,
FillBucket = 0x8,
PourBucket = 0x9,
UseTool = 0xA,
Interact = 0xB,
Retrieved = 0xC,
Dyed = 0xD,
Traded = 0xE,
_Count_0 = 0xF,
};

```
#### ItemUseOnActorInventoryTransaction::ActionType : __int32
```cpp
/* 180449 */
enum ItemUseOnActorInventoryTransaction::ActionType : __int32
{
Interact_1 = 0x0,
Attack_2 = 0x1,
ItemInteract = 0x2,
};

```
#### JournaledFile::Progression : __int32
```cpp
/* 290436 */
enum JournaledFile::Progression : __int32
{
NeverWritten = 0x0,
WriteFailed = 0x1,
WriteSuccess = 0x2,
};

```
#### JumpType : __int32
```cpp
/* 56477 */
enum JumpType : __int32
{
NONE_3 = 0x0,
HOP = 0x1,
STEP = 0x2,
SPRINT = 0x3,
_COUNT = 0x4,
};

```
#### KeyFrameLerpStyle : __int32
```cpp
/* 124577 */
enum KeyFrameLerpStyle : __int32
{
Linear = 0x0,
CatmullRom = 0x1,
_Count_4 = 0x2,
};

```
#### KeyFrameTransformPrePostSplitState : __int64
```cpp
/* 125121 */
enum KeyFrameTransformPrePostSplitState : __int64
{
Auto = 0x0,
Single = 0x1,
ForcedSplit = 0x2,
_Count_5 = 0x3,
};

```
#### KnownPackType : __int32
```cpp
/* 5661 */
enum KnownPackType : __int32
{
Valid = 0x0,
Invalid_4 = 0x1,
};

```
#### LabTablePacket::Type : __int8
```cpp
/* 79927 */
enum LabTablePacket::Type : __int8
{
StartCombine = 0x0,
StartReaction = 0x1,
Reset = 0x2,
};

```
#### LabTableReactionType : __int8
```cpp
/* 79933 */
enum LabTableReactionType : __int8
{
None_28 = 0x0,
IceBomb_0 = 0x1,
Bleach_0 = 0x2,
ElephantToothpaste = 0x3,
Fertilizer = 0x4,
HeatBlock = 0x5,
MagnesiumSalts = 0x6,
MiscFire = 0x7,
MiscExplosion = 0x8,
MiscLava = 0x9,
MiscMystical = 0xA,
MiscSmoke = 0xB,
MiscLargeSmoke = 0xC,
};

```
#### LayerValues::Terrain : __int8
```cpp
/* 39129 */
enum LayerValues::Terrain : __int8
{
Ocean = 0x0,
Land_0 = 0x1,
SpecialLand_1 = 0x2,
SpecialLand_2 = 0x3,
SpecialLand_3 = 0x4,
SpecialLand_4 = 0x5,
SpecialLand_5 = 0x6,
SpecialLand_6 = 0x7,
SpecialLand_7 = 0x8,
SpecialLand_8 = 0x9,
SpecialLand_9 = 0xA,
SpecialLand_10 = 0xB,
SpecialLand_11 = 0xC,
SpecialLand_12 = 0xD,
SpecialLand_13 = 0xE,
SpecialLand_14 = 0xF,
SpecialLand_15 = 0x10,
SpecialLand_16 = 0x11,
};

```
#### LayerZooms::Alignment : __int32
```cpp
/* 40588 */
enum LayerZooms::Alignment : __int32
{
Min = 0x0,
Center = 0x1,
Max = 0x2,
};

```
#### LeafSize : __int32
```cpp
/* 227982 */
enum LeafSize : __int32
{
NoLeaves = 0x0,
SmallLeaves = 0x1,
LargeLeaves = 0x2,
_count_47 = 0x3,
};

```
#### LegacyFlowerFeature::Type : __int32
```cpp
/* 29834 */
enum LegacyFlowerFeature::Type : __int32
{
FlowerForest_0 = 0x0,
Forest_0 = 0x1,
Overworld_0 = 0x2,
Plains_0 = 0x3,
Swamp = 0x4,
};

```
#### LegacyForestFoliageFeature::Type : __int32
```cpp
/* 29826 */
enum LegacyForestFoliageFeature::Type : __int32
{
Flower = 0x0,
Normal_2 = 0x1,
Roofed = 0x2,
};

```
#### LegacyTreeFeature::Type : __int32
```cpp
/* 29831 */
enum LegacyTreeFeature::Type : __int32
{
BambooJungle = 0x0,
BirchForest = 0x1,
BirchForestMutated = 0x2,
ExtremeHillsPlusTrees = 0x3,
FlowerForest = 0x4,
Forest = 0x5,
Ice = 0x6,
Jungle_1 = 0x7,
JungleEdge = 0x8,
MesaForest = 0x9,
Plains = 0xA,
Savanna = 0xB,
SavannaMutated = 0xC,
Taiga = 0xD,
TaigaMega = 0xE,
TaigaMegaSpruce = 0xF,
};

```
#### LevelChunk::Finalization : __int32
```cpp
/* 35001 */
enum LevelChunk::Finalization : __int32
{
NeedsInstaticking = 0x0,
NeedsPopulation = 0x1,
Done = 0x2,
};

```
#### LevelChunk::Tag : __int8
```cpp
/* 252819 */
enum LevelChunk::Tag : __int8
{
Data2D = 0x2D,
Data2DLegacy = 0x2E,
SubChunkPrefix = 0x2F,
LegacyTerrain = 0x30,
BlockEntity_1 = 0x31,
Entity_6 = 0x32,
PendingTicks_0 = 0x33,
LegacyBlockExtraData = 0x34,
BiomeState_0 = 0x35,
FinalizedState = 0x36,
ConversionData = 0x37,
BorderBlocks_0 = 0x38,
HardcodedSpawners = 0x39,
RandomTicks_0 = 0x3A,
Version = 0x76,
};

```
#### LevelChunkDataField : __int32
```cpp
/* 35031 */
enum LevelChunkDataField : __int32
{
BiomeState = 0x0,
BlockEntity = 0x1,
Entity_0 = 0x2,
PendingTicks = 0x3,
BorderBlocks = 0x4,
RandomTicks = 0x5,
_count_9 = 0x6,
};

```
#### LevelChunkFormat : __int8
```cpp
/* 34993 */
enum LevelChunkFormat : __int8
{
v9_00 = 0x0,
v9_02 = 0x1,
v9_05 = 0x2,
v17_0 = 0x3,
v18_0 = 0x4,
vConsole1_to_v18_0 = 0x5,
v1_2_0 = 0x6,
v1_2_0_bis = 0x7,
v1_3_0 = 0x8,
v1_8_0 = 0x9,
v1_9_0 = 0xA,
v1_10_0 = 0xB,
v1_11_0 = 0xC,
v1_11_1 = 0xD,
v1_11_2 = 0xE,
v1_12_0 = 0xF,
v1_14_0 = 0x10,
Count_3 = 0x11,
};

```
#### LevelEvent : __int16
```cpp
/* 35037 */
enum LevelEvent : __int16
{
Undefined_4 = 0x0,
SoundClick = 0x3E8,
SoundClickFail = 0x3E9,
SoundLaunch = 0x3EA,
SoundOpenDoor = 0x3EB,
SoundFizz = 0x3EC,
SoundFuse = 0x3ED,
SoundPlayRecording = 0x3EE,
SoundGhastWarning = 0x3EF,
SoundGhastFireball = 0x3F0,
SoundBlazeFireball = 0x3F1,
SoundZombieWoodenDoor = 0x3F2,
SoundZombieDoorCrash = 0x3F4,
SoundZombieInfected = 0x3F8,
SoundZombieConverted = 0x3F9,
SoundEndermanTeleport = 0x3FA,
SoundAnvilBroken = 0x3FC,
SoundAnvilUsed = 0x3FD,
SoundAnvilLand = 0x3FE,
SoundInfinityArrowPickup = 0x406,
SoundTeleportEnderPearl = 0x408,
SoundAddItem = 0x410,
SoundItemFrameBreak = 0x411,
SoundItemFramePlace = 0x412,
SoundItemFrameRemoveItem = 0x413,
SoundItemFrameRotateItem = 0x414,
SoundExperienceOrbPickup = 0x41B,
SoundTotemUsed = 0x41C,
SoundArmorStandBreak = 0x424,
SoundArmorStandHit = 0x425,
SoundArmorStandLand = 0x426,
SoundArmorStandPlace = 0x427,
ParticlesShoot = 0x7D0,
ParticlesDestroyBlock = 0x7D1,
ParticlesPotionSplash = 0x7D2,
ParticlesEyeOfEnderDeath = 0x7D3,
ParticlesMobBlockSpawn = 0x7D4,
ParticleCropGrowth = 0x7D5,
ParticleSoundGuardianGhost = 0x7D6,
ParticleDeathSmoke = 0x7D7,
ParticleDenyBlock = 0x7D8,
ParticleGenericSpawn = 0x7D9,
ParticlesDragonEgg = 0x7DA,
ParticlesCropEaten = 0x7DB,
ParticlesCrit = 0x7DC,
ParticlesTeleport = 0x7DD,
ParticlesCrackBlock = 0x7DE,
ParticlesBubble = 0x7DF,
ParticlesEvaporate = 0x7E0,
ParticlesDestroyArmorStand = 0x7E1,
ParticlesBreakingEgg = 0x7E2,
ParticleDestroyEgg = 0x7E3,
ParticlesEvaporateWater = 0x7E4,
ParticlesDestroyBlockNoSound = 0x7E5,
ParticlesKnockbackRoar = 0x7E6,
ParticlesTeleportTrail = 0x7E7,
ParticlesPointCloud = 0x7E8,
ParticlesExplosion = 0x7E9,
ParticlesBlockExplosion = 0x7EA,
StartRaining = 0xBB9,
StartThunderstorm = 0xBBA,
StopRaining = 0xBBB,
StopThunderstorm = 0xBBC,
GlobalPause = 0xBBD,
SimTimeStep = 0xBBE,
SimTimeScale = 0xBBF,
ActivateBlock = 0xDAC,
CauldronExplode = 0xDAD,
CauldronDyeArmor = 0xDAE,
CauldronCleanArmor = 0xDAF,
CauldronFillPotion = 0xDB0,
CauldronTakePotion = 0xDB1,
CauldronFillWater = 0xDB2,
CauldronTakeWater = 0xDB3,
CauldronAddDye = 0xDB4,
CauldronCleanBanner = 0xDB5,
CauldronFlush = 0xDB6,
AgentSpawnEffect = 0xDB7,
CauldronFillLava = 0xDB8,
CauldronTakeLava = 0xDB9,
StartBlockCracking = 0xE10,
StopBlockCracking = 0xE11,
UpdateBlockCracking = 0xE12,
AllPlayersSleeping = 0x2648,
JumpPrevented = 0x2652,
ParticleLegacyEvent = 0x4000,
};

```
#### LevelSoundEvent : __int32
```cpp
/* 35038 */
enum LevelSoundEvent : __int32
{
ItemUseOn = 0x0,
Hit = 0x1,
Step = 0x2,
Fly = 0x3,
Jump = 0x4,
Break = 0x5,
Place = 0x6,
HeavyStep = 0x7,
Gallop = 0x8,
Fall = 0x9,
Ambient_0 = 0xA,
AmbientBaby = 0xB,
AmbientInWater = 0xC,
Breathe = 0xD,
Death = 0xE,
DeathInWater = 0xF,
DeathToZombie = 0x10,
Hurt = 0x11,
HurtInWater = 0x12,
Mad = 0x13,
Boost = 0x14,
Bow_0 = 0x15,
SquishBig = 0x16,
SquishSmall = 0x17,
FallBig = 0x18,
FallSmall = 0x19,
Splash = 0x1A,
Fizz = 0x1B,
Flap = 0x1C,
Swim = 0x1D,
Drink_0 = 0x1E,
Eat_0 = 0x1F,
Takeoff = 0x20,
Shake = 0x21,
Plop = 0x22,
Land = 0x23,
Saddle = 0x24,
Armor = 0x25,
ArmorPlace = 0x26,
AddChest = 0x27,
Throw = 0x28,
Attack = 0x29,
AttackNoDamage = 0x2A,
AttackStrong = 0x2B,
Warn = 0x2C,
Shear = 0x2D,
Milk = 0x2E,
Thunder = 0x2F,
Explode_0 = 0x30,
Fire = 0x31,
Ignite = 0x32,
Fuse = 0x33,
Stare = 0x34,
Spawn = 0x35,
Shoot = 0x36,
BreakBlock = 0x37,
Launch = 0x38,
Blast = 0x39,
LargeBlast = 0x3A,
Twinkle = 0x3B,
Remedy = 0x3C,
Unfect = 0x3D,
LevelUp = 0x3E,
BowHit = 0x3F,
BulletHit = 0x40,
ExtinguishFire = 0x41,
ItemFizz = 0x42,
ChestOpen = 0x43,
ChestClosed = 0x44,
ShulkerBoxOpen = 0x45,
ShulkerBoxClosed = 0x46,
EnderChestOpen = 0x47,
EnderChestClosed = 0x48,
PowerOn = 0x49,
PowerOff = 0x4A,
Attach = 0x4B,
Detach = 0x4C,
Deny = 0x4D,
Tripod = 0x4E,
Pop = 0x4F,
DropSlot = 0x50,
Note_0 = 0x51,
Thorns = 0x52,
PistonIn = 0x53,
PistonOut = 0x54,
Portal_0 = 0x55,
Water = 0x56,
LavaPop = 0x57,
Lava_0 = 0x58,
Burp = 0x59,
BucketFillWater = 0x5A,
BucketFillLava = 0x5B,
BucketEmptyWater = 0x5C,
BucketEmptyLava = 0x5D,
EquipChain = 0x5E,
EquipDiamond = 0x5F,
EquipGeneric = 0x60,
EquipGold = 0x61,
EquipIron = 0x62,
EquipLeather = 0x63,
EquipElytra = 0x64,
Record13 = 0x65,
RecordCat = 0x66,
RecordBlocks = 0x67,
RecordChirp = 0x68,
RecordFar = 0x69,
RecordMall = 0x6A,
RecordMellohi = 0x6B,
RecordStal = 0x6C,
RecordStrad = 0x6D,
RecordWard = 0x6E,
Record11 = 0x6F,
RecordWait = 0x70,
RecordNull = 0x71,
Flop = 0x72,
GuardianCurse = 0x73,
MobWarning = 0x74,
MobWarningBaby = 0x75,
Teleport_0 = 0x76,
ShulkerOpen = 0x77,
ShulkerClose = 0x78,
Haggle = 0x79,
HaggleYes = 0x7A,
HaggleNo = 0x7B,
HaggleIdle = 0x7C,
ChorusGrow = 0x7D,
ChorusDeath = 0x7E,
Glass = 0x7F,
PotionBrewed = 0x80,
CastSpell = 0x81,
PrepareAttackSpell = 0x82,
PrepareSummon = 0x83,
PrepareWololo = 0x84,
Fang = 0x85,
Charge = 0x86,
TakePicture = 0x87,
PlaceLeashKnot = 0x88,
BreakLeashKnot = 0x89,
AmbientGrowl = 0x8A,
AmbientWhine = 0x8B,
AmbientPant = 0x8C,
AmbientPurr = 0x8D,
AmbientPurreow = 0x8E,
DeathMinVolume = 0x8F,
DeathMidVolume = 0x90,
ImitateBlaze = 0x91,
ImitateCaveSpider = 0x92,
ImitateCreeper = 0x93,
ImitateElderGuardian = 0x94,
ImitateEnderDragon = 0x95,
ImitateEnderman = 0x96,
ImitateEndermite = 0x97,
ImitateEvocationIllager = 0x98,
ImitateGhast = 0x99,
ImitateHusk = 0x9A,
ImitateIllusionIllager = 0x9B,
ImitateMagmaCube = 0x9C,
ImitatePolarBear = 0x9D,
ImitateShulker = 0x9E,
ImitateSilverfish = 0x9F,
ImitateSkeleton = 0xA0,
ImitateSlime = 0xA1,
ImitateSpider = 0xA2,
ImitateStray = 0xA3,
ImitateVex = 0xA4,
ImitateVindicationIllager = 0xA5,
ImitateWitch = 0xA6,
ImitateWither = 0xA7,
ImitateWitherSkeleton = 0xA8,
ImitateWolf = 0xA9,
ImitateZombie = 0xAA,
ImitateZombiePigman = 0xAB,
ImitateZombieVillager = 0xAC,
EnderEyePlaced = 0xAD,
EndPortalCreated = 0xAE,
AnvilUse = 0xAF,
BottleDragonBreath = 0xB0,
PortalTravel = 0xB1,
TridentHit = 0xB2,
TridentReturn = 0xB3,
TridentRiptide_1 = 0xB4,
TridentRiptide_2 = 0xB5,
TridentRiptide_3 = 0xB6,
TridentThrow = 0xB7,
TridentThunder = 0xB8,
TridentHitGround = 0xB9,
Default_4 = 0xBA,
FletchingTableUse = 0xBB,
ElemConstructOpen = 0xBC,
IceBombHit = 0xBD,
BalloonPop = 0xBE,
LTReactionIceBomb = 0xBF,
LTReactionBleach = 0xC0,
LTReactionElephantToothpaste = 0xC1,
LTReactionElephantToothpaste2 = 0xC2,
LTReactionGlowStick = 0xC3,
LTReactionGlowStick2 = 0xC4,
LTReactionLuminol = 0xC5,
LTReactionSalt = 0xC6,
LTReactionFertilizer = 0xC7,
LTReactionFireball = 0xC8,
LTReactionMagnesiumSalt = 0xC9,
LTReactionMiscFire = 0xCA,
LTReactionFire = 0xCB,
LTReactionMiscExplosion = 0xCC,
LTReactionMiscMystical = 0xCD,
LTReactionMiscMystical2 = 0xCE,
LTReactionProduct = 0xCF,
SparklerUse = 0xD0,
GlowStickUse = 0xD1,
SparklerActive = 0xD2,
ConvertToDrowned = 0xD3,
BucketFillFish = 0xD4,
BucketEmptyFish = 0xD5,
BubbleColumnUpwards = 0xD6,
BubbleColumnDownwards = 0xD7,
BubblePop = 0xD8,
BubbleUpInside = 0xD9,
BubbleDownInside = 0xDA,
HurtBaby = 0xDB,
DeathBaby = 0xDC,
StepBaby = 0xDD,
SpawnBaby = 0xDE,
Born = 0xDF,
TurtleEggBreak = 0xE0,
TurtleEggCrack = 0xE1,
TurtleEggHatched = 0xE2,
LayEgg = 0xE3,
TurtleEggAttacked = 0xE4,
BeaconActivate = 0xE5,
BeaconAmbient = 0xE6,
BeaconDeactivate = 0xE7,
BeaconPower = 0xE8,
ConduitActivate = 0xE9,
ConduitAmbient = 0xEA,
ConduitAttack = 0xEB,
ConduitDeactivate = 0xEC,
ConduitShort = 0xED,
Swoop = 0xEE,
BambooSaplingPlace = 0xEF,
PreSneeze = 0xF0,
Sneeze_0 = 0xF1,
AmbientTame = 0xF2,
Scared = 0xF3,
ScaffoldingClimb = 0xF4,
CrossbowLoadingStart = 0xF5,
CrossbowLoadingMiddle = 0xF6,
CrossbowLoadingEnd = 0xF7,
CrossbowShoot = 0xF8,
CrossbowQuickChargeStart = 0xF9,
CrossbowQuickChargeMiddle = 0xFA,
CrossbowQuickChargeEnd = 0xFB,
AmbientAggressive = 0xFC,
AmbientWorried = 0xFD,
CantBreed = 0xFE,
ShieldBlock = 0xFF,
LecternBookPlace = 0x100,
GrindstoneUse = 0x101,
Bell = 0x102,
CampfireCrackle = 0x103,
SweetBerryBushHurt = 0x106,
SweetBerryBushPick = 0x107,
Roar = 0x104,
Stun = 0x105,
CartographyTableUse = 0x108,
StonecutterUse = 0x109,
ComposterEmpty = 0x10A,
ComposterFill = 0x10B,
ComposterFillLayer = 0x10C,
ComposterReady = 0x10D,
BarrelOpen = 0x10E,
BarrelClose = 0x10F,
RaidHorn = 0x110,
LoomUse = 0x111,
AmbientInRaid = 0x112,
UICartographyTableUse = 0x113,
UIStonecutterUse = 0x114,
UILoomUse = 0x115,
SmokerUse = 0x116,
BlastFurnaceUse = 0x117,
SmithingTableUse = 0x118,
Screech = 0x119,
Sleep = 0x11A,
FurnaceUse = 0x11B,
MooshroomConvert = 0x11C,
MilkSuspiciously = 0x11D,
Celebrate = 0x11E,
JumpPrevent = 0x11F,
AmbientPollinate = 0x120,
BeehiveDrip = 0x121,
BeehiveEnter = 0x122,
BeehiveExit = 0x123,
BeehiveWork = 0x124,
BeehiveShear = 0x125,
HoneybottleDrink = 0x126,
Undefined_5 = 0x127,
};

```
#### LeverDirection : __int32
```cpp
/* 230355 */
enum LeverDirection : __int32
{
DownEastWest = 0x0,
East_1 = 0x1,
West_1 = 0x2,
South_1 = 0x3,
North_1 = 0x4,
UpNorthSouth = 0x5,
UpEastWest = 0x6,
DownNorthSouth = 0x7,
_count_50 = 0x8,
};

```
#### LimboEntitiesVersion : __int8
```cpp
/* 254192 */
enum LimboEntitiesVersion : __int8
{
v0 = 0x0,
v1_8_0_0 = 0x1,
v1_10_0_0 = 0x2,
v1_12_0_0 = 0x3,
};

```
#### ListDCommand::DetailMode : __int32
```cpp
/* 425893 */
enum ListDCommand::DetailMode : __int32
{
None_55 = 0x0,
IDs = 0x1,
UUIDs = 0x2,
Stats = 0x3,
};

```
#### LoadingState : __int32
```cpp
/* 45311 */
enum LoadingState : __int32
{
};

```
#### Localization::appendTranslations::LangLineState : __int32
```cpp
/* 60934 */
enum Localization::appendTranslations::LangLineState : __int32
{
LeadingWhitespace = 0x0,
Key = 0x1,
Value_0 = 0x2,
PostValueWhitespaceOrComment = 0x3,
};

```
#### Lockless::MemoryOrder : __int32
```cpp
/* 226 */
enum Lockless::MemoryOrder : __int32
{
Relaxed = 0x0,
Acquire = 0x1,
Release = 0x2,
AcqRel = 0x3,
SeqCst = 0x4,
Sync = 0x4,
};

```
#### LogArea : __int32
```cpp
/* 5589 */
enum LogArea : __int32
{
Actor = 0x0,
Addon_0 = 0x1,
AI = 0x2,
Animation = 0x3,
AutomatedTests = 0x4,
BiomeRegistry = 0x5,
Blocks = 0x6,
Camera = 0x7,
Commands = 0x8,
Components = 0x9,
Effects = 0xA,
Entity = 0xB,
FeatureRegistry = 0xC,
Geometry = 0xD,
Item = 0xE,
Json = 0xF,
LevelStorage = 0x10,
Log = 0x11,
Molang = 0x12,
Recipes = 0x13,
Rendering = 0x14,
Scripting = 0x15,
Sound = 0x16,
Structure = 0x17,
UI = 0x18,
COUNT_0 = 0x19,
};

```
#### LogAreaID : __int32
```cpp
/* 5591 */
enum LogAreaID : __int32
{
LOG_AREA_ALL = 0x0,
LOG_AREA_PLATFORM = 0x1,
LOG_AREA_ENTITY = 0x2,
LOG_AREA_DATABASE = 0x3,
LOG_AREA_GUI = 0x4,
LOG_AREA_SYSTEM = 0x5,
LOG_AREA_NETWORK = 0x6,
LOG_AREA_RENDER = 0x7,
LOG_AREA_MEMORY = 0x8,
LOG_AREA_ANIMATION = 0x9,
LOG_AREA_INPUT = 0xA,
LOG_AREA_LEVEL = 0xB,
LOG_AREA_SERVER = 0xC,
LOG_AREA_DLC = 0xD,
LOG_AREA_PHYSICS = 0xE,
LOG_AREA_FILE = 0xF,
LOG_AREA_STORAGE = 0x10,
LOG_AREA_REALMS = 0x11,
LOG_AREA_REALMSAPI = 0x12,
LOG_AREA_XBOXLIVE = 0x13,
LOG_AREA_USERMANAGER = 0x14,
LOG_AREA_XSAPI = 0x15,
LOG_AREA_PERF = 0x16,
LOG_AREA_TELEMETRY = 0x17,
LOG_AREA_BLOCKS = 0x18,
LOG_AREA_RAKNET = 0x19,
LOG_AREA_GAMEFACE = 0x1A,
LOG_AREA_SOUND = 0x1B,
LOG_AREA_INTERACTIVE = 0x1C,
LOG_AREA_SCRIPTING = 0x1D,
LOG_AREA_PLAYFAB = 0x1E,
LOG_AREA_AUTOMATION = 0x1F,
LOG_AREA_PERSONA = 0x20,
LOG_AREA_UNKNOWN = 0x21,
NUM_LOG_AREAS = 0x22,
};

```
#### LogLevel : __int32
```cpp
/* 5588 */
enum LogLevel : __int32
{
Verbose = 0x0,
Inform = 0x1,
Warning = 0x2,
Error = 0x3,
COUNT = 0x4,
};

```
#### MCCATEGORY : __int8
```cpp
/* 94507 */
enum MCCATEGORY : __int8
{
Minecraft = 0x0,
AutomationProtocol = 0x1,
MinecraftCommand = 0x2,
};

```
#### ManifestOrigin : __int8
```cpp
/* 5772 */
enum ManifestOrigin : __int8
{
Directory = 0x0,
Archive = 0x1,
Realms = 0x2,
Catalog = 0x3,
WorldHistory = 0x4,
Invalid_8 = 0x5,
};

```
#### ManifestType : __int8
```cpp
/* 5773 */
enum ManifestType : __int8
{
Pack = 0x0,
WorldTemplate_1 = 0x1,
Catalog_0 = 0x2,
};

```
#### MapDecoration::Type : __int8
```cpp
/* 75313 */
enum MapDecoration::Type : __int8
{
MarkerWhite = 0x0,
MarkerGreen = 0x1,
MarkerRed = 0x2,
MarkerBlue = 0x3,
XWhite = 0x4,
TriangleRed = 0x5,
SquareWhite = 0x6,
MarkerSign = 0x7,
MarkerPink = 0x8,
MarkerOrange = 0x9,
MarkerYellow = 0xA,
MarkerTeal = 0xB,
TriangleGreen = 0xC,
SmallSquareWhite = 0xD,
Mansion = 0xE,
Monument_0 = 0xF,
NoDraw = 0x10,
Count_13 = 0x11,
Player_3 = 0x0,
PlayerOffMap = 0x6,
PlayerOffLimits = 0xD,
PlayerHidden = 0x10,
ItemFrame_0 = 0x1,
};

```
#### MapItemTrackedActor::Type : __int32
```cpp
/* 75354 */
enum MapItemTrackedActor::Type : __int32
{
Entity_3 = 0x0,
BlockEntity_0 = 0x1,
Other_1 = 0x2,
};

```
#### MapOutputType : __int32
```cpp
/* 45353 */
enum MapOutputType : __int32
{
None_20 = 0x0,
RenameMap = 0x1,
BasicMap = 0x2,
LocatorMap = 0x3,
ExtendAndClearMap = 0x4,
CloneMap = 0x5,
LockMap = 0x6,
};

```
#### MapType : __int32
```cpp
/* 93974 */
enum MapType : __int32
{
Empty = 0x0,
Basic_0 = 0x1,
Enhanced = 0x2,
OceanExplorer = 0x3,
WoodlandExplorer = 0x4,
TreasureExplorer = 0x5,
Locked = 0x6,
};

```
#### Material::Settings : __int32
```cpp
/* 109110 */
enum Material::Settings : __int32
{
Normal_6 = 0x0,
Gas = 0x1,
Liquid = 0x2,
Decoration_0 = 0x3,
Portal_2 = 0x4,
};

```
#### MaterialType : __int32
```cpp
/* 40752 */
enum MaterialType : __int32
{
Air = 0x0,
Dirt = 0x1,
Wood_0 = 0x2,
Stone_0 = 0x3,
Metal = 0x4,
Water_0 = 0x5,
Lava_1 = 0x6,
Leaves = 0x7,
Plant = 0x8,
ReplaceablePlant = 0x9,
Sponge = 0xA,
Cloth = 0xB,
Bed = 0xC,
Fire_0 = 0xD,
Sand = 0xE,
Decoration = 0xF,
Glass_0 = 0x10,
Explosive = 0x11,
Ice_0 = 0x12,
PackedIce = 0x13,
TopSnow = 0x14,
Snow_0 = 0x15,
Cactus = 0x16,
Clay = 0x17,
Vegetable = 0x18,
Portal_1 = 0x19,
Cake = 0x1A,
Web = 0x1B,
RedstoneWire = 0x1C,
Carpet = 0x1D,
BuildableGlass = 0x1E,
Slime_1 = 0x1F,
Piston = 0x20,
Allow = 0x21,
Deny_0 = 0x22,
Netherwart = 0x23,
StoneDecoration = 0x24,
Bubble_0 = 0x25,
Egg = 0x26,
Barrier = 0x27,
DecorationFlammable = 0x28,
SurfaceTypeTotal = 0x29,
Any_1 = 0x2A,
};

```
#### MedicineType : __int8
```cpp
/* 184481 */
enum MedicineType : __int8
{
Blindness = 0x0,
Nausea = 0x1,
Poison_0 = 0x2,
Weakness = 0x3,
Invalid_25 = 0x4,
};

```
#### MinecartType : __int32
```cpp
/* 170745 */
enum MinecartType : __int32
{
Rideable = 0x0,
Chest_1 = 0x1,
Furnace_0 = 0x2,
TNT = 0x3,
Spawner_0 = 0x4,
Hopper_1 = 0x5,
CommandBlock_1 = 0x6,
};

```
#### MinecraftEventing::AccountType : __int32
```cpp
/* 45283 */
enum MinecraftEventing::AccountType : __int32
{
Xbl = 0x1,
Guest = 0x2,
Other_0 = 0x3,
};

```
#### MinecraftEventing::AchievementIds : __int32
```cpp
/* 13191 */
enum MinecraftEventing::AchievementIds : __int32
{
ChestFullOfCobblestone = 0x7,
DiamondForYou = 0xA,
IronBelly = 0x14,
IronMan = 0x15,
OnARail = 0x1D,
Overkill = 0x1E,
ReturnToSender = 0x25,
SniperDuel = 0x26,
StayinFrosty = 0x27,
TakeInventory = 0x28,
MapRoom = 0x32,
FreightStation = 0x34,
SmeltEverything = 0x35,
TasteOfYourOwnMedicine = 0x36,
WhenPigsFly = 0x38,
Inception = 0x3A,
ArtificialSelection = 0x3C,
FreeDiver = 0x3D,
SpawnTheWither = 0x3E,
Beaconator = 0x3F,
GreatView = 0x40,
SuperSonic = 0x41,
TheEndAgain = 0x42,
TreasureHunter = 0x43,
ShootingStar = 0x44,
FashionShow = 0x45,
Brilliance = 0x46,
SelfPublishedAuthor = 0x47,
AlternativeFuel = 0x48,
SleepWithTheFishes = 0x49,
Castaway = 0x4A,
ImAMarineBiologist = 0x4B,
SailThe7Seas = 0x4C,
MeGold = 0x4D,
Ahoy = 0x4E,
Atlantis = 0x4F,
OnePickleTwoPickleSeaPickleFour = 0x50,
DoaBarrelRoll = 0x51,
Moskstraumen = 0x52,
Echolocation = 0x53,
WhereHaveYouBeen = 0x54,
TopOfTheWorld = 0x55,
FruitOnTheLoom = 0x56,
SoundTheAlarm = 0x57,
BuyLowSellHigh = 0x58,
Disenchanted = 0x59,
TimeForStew = 0x5A,
BeeOurGuest = 0x5B,
TotalBeeLocation = 0x5C,
StickySituation = 0x5D,
};

```
#### MinecraftEventing::AcquisitionMethod : __int32
```cpp
/* 43312 */
enum MinecraftEventing::AcquisitionMethod : __int32
{
Unknown_9 = 0xFFFFFFFF,
None_17 = 0x0,
PickedUp_0 = 0x1,
Crafted_1 = 0x2,
TakenFromChest_0 = 0x3,
TakenFromEnderchest_0 = 0x4,
Bought_0 = 0x5,
Anvil_0 = 0x6,
Smelted_0 = 0x7,
Brewed_0 = 0x8,
Bottle = 0x9,
Trading_1 = 0xA,
Fishing_0 = 0xB,
};

```
#### MinecraftEventing::BlockPlacementMethod : __int32
```cpp
/* 44512 */
enum MinecraftEventing::BlockPlacementMethod : __int32
{
Entity_1 = 0x0,
Command_0 = 0x1,
};

```
#### MinecraftEventing::ChangeType : __int32
```cpp
/* 44524 */
enum MinecraftEventing::ChangeType : __int32
{
Unknown_10 = 0x0,
Added = 0x1,
Removed = 0x2,
Updated = 0x3,
};

```
#### MinecraftEventing::InteractionType : __int32
```cpp
/* 13190 */
enum MinecraftEventing::InteractionType : __int32
{
Breeding = 0x1,
Taming = 0x2,
Curing = 0x3,
Crafted = 0x4,
Shearing = 0x5,
Milking = 0x6,
Trading = 0x7,
Feeding = 0x8,
Igniting = 0x9,
Coloring = 0xA,
Naming = 0xB,
Leashing = 0xC,
Unleashing = 0xD,
PetSleep = 0xE,
Trusting = 0xF,
Commanding = 0x10,
};

```
#### MinecraftEventing::ItemInteractMethod : __int32
```cpp
/* 44582 */
enum MinecraftEventing::ItemInteractMethod : __int32
{
Use = 0x0,
Place_2 = 0x1,
};

```
#### MinecraftEventing::POIBlockInteractionType : __int32
```cpp
/* 13306 */
enum MinecraftEventing::POIBlockInteractionType : __int32
{
None_9 = 0x0,
Extend = 0x1,
Clone = 0x2,
Lock = 0x3,
Create = 0x4,
CreateLocator = 0x5,
Rename = 0x6,
ItemPlaced = 0x7,
ItemRemoved = 0x8,
Cooking = 0x9,
Dousing = 0xA,
Lighting = 0xB,
Haystack = 0xC,
Filled = 0xD,
Emptied = 0xE,
AddDye = 0xF,
DyeItem = 0x10,
ClearItem = 0x11,
EnchantArrow = 0x12,
CompostItemPlaced = 0x13,
RecoveredBonemeal = 0x14,
BookPlaced = 0x15,
BookOpened = 0x16,
Disenchant = 0x17,
Repair = 0x18,
DisenchantAndRepair = 0x19,
};

```
#### MinecraftEventing::PoiEventBlockType : __int32
```cpp
/* 44501 */
enum MinecraftEventing::PoiEventBlockType : __int32
{
BlastFurnace_0 = 0x0,
BrewingStand_0 = 0x1,
CartographyTable = 0x2,
Grindstone = 0x3,
Loom = 0x4,
Smoker_0 = 0x5,
Stonecutter = 0x6,
Barrel = 0x7,
Bell_1 = 0x8,
Campfire_0 = 0x9,
Cauldron_0 = 0xA,
Composter = 0xB,
Lectern_1 = 0xC,
};

```
#### MinecraftEventing::TeleportationCause : __int32
```cpp
/* 45282 */
enum MinecraftEventing::TeleportationCause : __int32
{
Unknown_14 = 0x0,
Projectile_1 = 0x1,
ChorusFruit = 0x2,
Command_2 = 0x3,
Behavior_0 = 0x4,
TeleportationCause_Count = 0x5,
};

```
#### MinecraftEventing::TravelMethod : __int32
```cpp
/* 45284 */
enum MinecraftEventing::TravelMethod : __int32
{
Unknown_15 = 0xFFFFFFFF,
Walk = 0x0,
SwimWater = 0x1,
Fall_1 = 0x2,
Climb = 0x3,
SwimLava = 0x4,
Fly_0 = 0x5,
Riding_0 = 0x6,
Sneak = 0x7,
Sprint = 0x8,
Bounce = 0x9,
FrostWalk = 0xA,
};

```
#### MinecraftEventing::UseMethod : __int32
```cpp
/* 43226 */
enum MinecraftEventing::UseMethod : __int32
{
Unknown_7 = 0xFFFFFFFF,
EquipArmor_0 = 0x0,
Eat_2 = 0x1,
Attack_1 = 0x2,
Consume_0 = 0x3,
Throw_1 = 0x4,
Shoot_1 = 0x5,
Place_1 = 0x6,
FillBottle_0 = 0x7,
FillBucket_0 = 0x8,
PourBucket_0 = 0x9,
UseTool_0 = 0xA,
};

```
#### MinecraftPacketIds : __int32
```cpp
/* 63708 */
enum MinecraftPacketIds : __int32
{
KeepAlive = 0x0,
Login = 0x1,
PlayStatus = 0x2,
ServerToClientHandshake = 0x3,
ClientToServerHandshake = 0x4,
Disconnect = 0x5,
ResourcePacksInfo = 0x6,
ResourcePackStack = 0x7,
ResourcePackClientResponse = 0x8,
Text = 0x9,
SetTime = 0xA,
StartGame = 0xB,
AddPlayer = 0xC,
AddActor = 0xD,
RemoveActor = 0xE,
AddItemActor = 0xF,
UNUSED_PLS_USE_ME = 0x10,
TakeItemActor = 0x11,
MoveAbsoluteActor = 0x12,
MovePlayer = 0x13,
RiderJump = 0x14,
UpdateBlock = 0x15,
AddPainting = 0x16,
TickSync = 0x17,
LevelSoundEventV1 = 0x18,
LevelEvent = 0x19,
TileEvent = 0x1A,
ActorEvent = 0x1B,
MobEffect = 0x1C,
UpdateAttributes = 0x1D,
InventoryTransaction = 0x1E,
PlayerEquipment = 0x1F,
MobArmorEquipment = 0x20,
Interact_0 = 0x21,
BlockPickRequest = 0x22,
ActorPickRequest = 0x23,
PlayerAction = 0x24,
ActorFall = 0x25,
HurtArmor = 0x26,
SetActorData = 0x27,
SetActorMotion = 0x28,
SetActorLink = 0x29,
SetHealth = 0x2A,
SetSpawnPosition = 0x2B,
Animate = 0x2C,
Respawn = 0x2D,
ContainerOpen = 0x2E,
ContainerClose = 0x2F,
PlayerHotbar = 0x30,
InventoryContent = 0x31,
InventorySlot = 0x32,
ContainerSetData = 0x33,
CraftingData = 0x34,
CraftingEvent = 0x35,
GuiDataPickItem = 0x36,
AdventureSettings = 0x37,
BlockActorData = 0x38,
PlayerInput = 0x39,
FullChunkData = 0x3A,
SetCommandsEnabled = 0x3B,
SetDifficulty = 0x3C,
ChangeDimension = 0x3D,
SetPlayerGameType = 0x3E,
PlayerList = 0x3F,
SimpleEvent = 0x40,
Event = 0x41,
SpawnExperienceOrb = 0x42,
MapData = 0x43,
MapInfoRequest = 0x44,
RequestChunkRadius = 0x45,
ChunkRadiusUpdated = 0x46,
ItemFrameDropItem = 0x47,
GameRulesChanged = 0x48,
Camera_1 = 0x49,
BossEvent = 0x4A,
ShowCredits = 0x4B,
AvailableCommands = 0x4C,
CommandRequest = 0x4D,
CommandBlockUpdate = 0x4E,
CommandOutput = 0x4F,
UpdateTrade = 0x50,
UpdateEquip = 0x51,
ResourcePackDataInfo = 0x52,
ResourcePackChunkData = 0x53,
ResourcePackChunkRequest = 0x54,
Transfer = 0x55,
PlaySound = 0x56,
StopSound = 0x57,
SetTitle = 0x58,
AddBehaviorTree = 0x59,
StructureBlockUpdate = 0x5A,
ShowStoreOffer = 0x5B,
PurchaseReceipt = 0x5C,
PlayerSkin = 0x5D,
SubclientLogin = 0x5E,
AutomationClientConnect = 0x5F,
SetLastHurtBy = 0x60,
BookEdit = 0x61,
NPCRequest = 0x62,
PhotoTransfer = 0x63,
ShowModalForm = 0x64,
ModalFormResponse = 0x65,
ServerSettingsRequest = 0x66,
ServerSettingsResponse = 0x67,
ShowProfile = 0x68,
SetDefaultGameType = 0x69,
RemoveObjective = 0x6A,
SetDisplayObjective = 0x6B,
SetScore = 0x6C,
LabTable = 0x6D,
UpdateBlockSynced = 0x6E,
MoveDeltaActor = 0x6F,
SetScoreboardIdentity = 0x70,
SetLocalPlayerAsInit = 0x71,
UpdateSoftEnum = 0x72,
Ping = 0x73,
BlockPalette = 0x74,
SciptCustomEvent = 0x75,
SpawnParticleEffect = 0x76,
AvailableActorIDList = 0x77,
LevelSoundEventV2 = 0x78,
NetworkChunkPublisherUpdate = 0x79,
BiomeDefinitionList = 0x7A,
LevelSoundEvent = 0x7B,
LevelEventGeneric = 0x7C,
LecternUpdate = 0x7D,
VideoStreamConnect = 0x7E,
AddEntity = 0x7F,
RemoveEntity = 0x80,
ClientCacheStatus = 0x81,
OnScreenTextureAnimation = 0x82,
MapCreateLockedCopy = 0x83,
StructureTemplateDataExportRequest = 0x84,
StructureTemplateDataExportResponse = 0x85,
UpdateBlockProperties = 0x86,
ClientCacheBlobStatusPacket = 0x87,
ClientCacheMissResponsePacket = 0x88,
EducationSettingsPacket = 0x89,
Emote = 0x8A,
MultiplayerSettingsPacket = 0x8B,
SettingsCommandPacket = 0x8C,
AnvilDamage = 0x8D,
CompletedUsingItem = 0x8E,
NetworkSettings = 0x8F,
PlayerAuthInputPacket = 0x90,
EndId = 0x91,
};

```
#### MingleComponent::MingleState : __int32
```cpp
/* 122581 */
enum MingleComponent::MingleState : __int32
{
Unavailable = 0x0,
Available = 0x1,
PartneredActive = 0x2,
PartneredPassive = 0x3,
Mingling = 0x4,
};

```
#### Mirror : __int8
```cpp
/* 5804 */
enum Mirror : __int8
{
};

```
#### Mirror_0 : __int8
```cpp
/* 35194 */
enum Mirror_0 : __int8
{
None_15 = 0x0,
X = 0x1,
Z = 0x2,
XZ = 0x3,
};

```
#### Mob::TravelType : __int32
```cpp
/* 116607 */
enum Mob::TravelType : __int32
{
Water_2 = 0x0,
Lava_4 = 0x1,
Ground = 0x2,
Air_0 = 0x3,
};

```
#### MobEffectPacket::Event : __int8
```cpp
/* 80017 */
enum MobEffectPacket::Event : __int8
{
Add_1 = 0x1,
Update = 0x2,
Remove_0 = 0x3,
};

```
#### MobEventsIndex : __int16
```cpp
/* 124039 */
enum MobEventsIndex : __int16
{
Invalid_21 = 0xFFFF,
PillagerPatrolsEvent = 0x0,
WanderingTraderEvent = 0x1,
EventCount = 0x2,
};

```
#### MobGoals : __int32
```cpp
/* 452192 */
enum MobGoals : __int32
{
GO_TO_MOB = 0x0,
GO_IN_MOB_DIRECTION = 0x1,
};

```
#### MobSpawnMethod : __int32
```cpp
/* 88768 */
enum MobSpawnMethod : __int32
{
Unknown_32 = 0x0,
SpawnEgg = 0x1,
Command_3 = 0x2,
Dispenser_0 = 0x3,
Spawner = 0x4,
SpawnMethod_Count = 0x5,
};

```
#### MonsterEggStoneType : __int32
```cpp
/* 31917 */
enum MonsterEggStoneType : __int32
{
Stone = 0x0,
Cobblestone_0 = 0x1,
StoneBrick_0 = 0x2,
MossyStoneBrick = 0x3,
CrackedStoneBrick = 0x4,
ChiseledStoneBrick = 0x5,
_count_7 = 0x6,
};

```
#### MoonPhases : __int32
```cpp
/* 254723 */
enum MoonPhases : __int32
{
FULL_MOON = 0x0,
WANING_GIBBOUS = 0x1,
FIRST_QUARTER = 0x2,
WANING_CRESCENT = 0x3,
NEW_MOON = 0x4,
WAXING_CRESCENT = 0x5,
LAST_QUARTER = 0x6,
WAXING_GIBBOUS = 0x7,
COUNT_14 = 0x8,
};

```
#### MoveInputHandler::LookDirection : __int8
```cpp
/* 475158 */
enum MoveInputHandler::LookDirection : __int8
{
Up_0 = 0x1,
Down_0 = 0x0,
Left_1 = 0x4,
Right_1 = 0x5,
Count_29 = 0x4,
};

```
#### MovementEventType : __int8
```cpp
/* 13307 */
enum MovementEventType : __int8
{
PositionCorrected = 0x0,
BackInSync = 0x1,
};

```
#### MultiplayerSettingsPacketType : __int32
```cpp
/* 77446 */
enum MultiplayerSettingsPacketType : __int32
{
EnableMultiplayer = 0x0,
DisableMultiplayer = 0x1,
RefreshJoincode = 0x2,
};

```
#### MushroomOuterType : __int32
```cpp
/* 183774 */
enum MushroomOuterType : __int32
{
AllPores = 0x0,
VerticalStem = 0xA,
AllCap = 0xE,
AllStem = 0xF,
};

```
#### NetworkHandler::Connection::Type : __int32
```cpp
/* 8336 */
enum NetworkHandler::Connection::Type : __int32
{
Remote_0 = 0x0,
Local_1 = 0x1,
};

```
#### NetworkHandler::NetworkStatisticsConfig : __int32
```cpp
/* 63569 */
enum NetworkHandler::NetworkStatisticsConfig : __int32
{
None_23 = 0x0,
Client = 0x1,
Server = 0x2,
};

```
#### NetworkIdentifier::Type : __int32
```cpp
/* 8097 */
enum NetworkIdentifier::Type : __int32
{
RakNet = 0x0,
Address = 0x1,
Address6 = 0x2,
Generic = 0x3,
};

```
#### NetworkPeer::DataStatus : __int32
```cpp
/* 8628 */
enum NetworkPeer::DataStatus : __int32
{
HasData = 0x0,
NoData = 0x1,
BrokenData = 0x2,
};

```
#### NetworkPeer::NetworkLoad : __int32
```cpp
/* 8629 */
enum NetworkPeer::NetworkLoad : __int32
{
Unrestricted = 0x0,
Low_0 = 0x1,
Medium = 0x2,
High_0 = 0x3,
};

```
#### NetworkPeer::Reliability : __int32
```cpp
/* 63696 */
enum NetworkPeer::Reliability : __int32
{
Reliable = 0x0,
ReliableOrdered = 0x1,
Unreliable = 0x2,
UnreliableSequenced = 0x3,
};

```
#### NewLeafType : __int32
```cpp
/* 183699 */
enum NewLeafType : __int32
{
Acacia_1 = 0x0,
DarkOak_1 = 0x1,
_count_34 = 0x2,
};

```
#### NewLogType : __int32
```cpp
/* 183688 */
enum NewLogType : __int32
{
Acacia_0 = 0x0,
DarkOak_0 = 0x1,
_count_33 = 0x2,
};

```
#### NodeType : __int32
```cpp
/* 57607 */
enum NodeType : __int32
{
HONEYBLOCK = 0xFFFFFFF8,
UNWALKABLE = 0xFFFFFFF9,
HOTBLOCK = 0xFFFFFFFA,
FIRE = 0xFFFFFFFB,
TRAP = 0xFFFFFFFC,
FENCE = 0xFFFFFFFD,
LAVA = 0xFFFFFFFE,
WATER = 0xFFFFFFFF,
BLOCKED = 0x0,
BREAKABLE = 0x1,
OPEN = 0x2,
WALKABLE = 0x3,
SWIMMABLE = 0x4,
BREACHABLE = 0x5,
FLYABLE = 0x6,
DOOR = 0x7,
OPEN_TYPE_COUNT = 0x9,
};

```
#### NpcActionMode : __int8
```cpp
/* 49177 */
enum NpcActionMode : __int8
{
Button = 0x0,
OnClose = 0x1,
};

```
#### NpcActionType : __int8
```cpp
/* 49178 */
enum NpcActionType : __int8
{
UrlAction = 0x0,
CommandAction = 0x1,
InvalidAction = 0x2,
};

```
#### NpcRequestPacket::RequestType : __int8
```cpp
/* 80037 */
enum NpcRequestPacket::RequestType : __int8
{
SetActions = 0x0,
ExecuteAction = 0x1,
ExecuteClosingCommands = 0x2,
SetName = 0x3,
SetSkin = 0x4,
SetInteractText = 0x5,
};

```
#### ObjectiveRenderType : __int8
```cpp
/* 80246 */
enum ObjectiveRenderType : __int8
{
};

```
#### ObjectiveRenderType_0 : __int8
```cpp
/* 80473 */
enum ObjectiveRenderType_0 : __int8
{
Integer_0 = 0x0,
Hearts = 0x1,
};

```
#### ObjectiveSortOrder : __int8
```cpp
/* 80416 */
enum ObjectiveSortOrder : __int8
{
Ascending = 0x0,
Descending = 0x1,
};

```
#### OceanTempCategory : __int32
```cpp
/* 41639 */
enum OceanTempCategory : __int32
{
COLD = 0x0,
WARM = 0x1,
};

```
#### OldLeafType : __int32
```cpp
/* 19619 */
enum OldLeafType : __int32
{
Oak_0 = 0x0,
Spruce_0 = 0x1,
Birch_0 = 0x2,
Jungle_0 = 0x3,
_count_3 = 0x4,
};

```
#### OldLogType : __int32
```cpp
/* 19613 */
enum OldLogType : __int32
{
Oak = 0x0,
Spruce = 0x1,
Birch = 0x2,
Jungle = 0x3,
_count_2 = 0x4,
};

```
#### OperationMode : __int32
```cpp
/* 87056 */
enum OperationMode : __int32
{
Handheld = 0x0,
Console_1 = 0x1,
};

```
#### OptionID : __int32
```cpp
/* 81323 */
enum OptionID : __int32
{
NAME_0 = 0x0,
DIFFICULTY = 0x1,
THIRD_PERSON = 0x2,
DPAD_SCALE = 0x3,
SERVER_VISIBLE = 0x4,
XBOX_LIVE_VISIBLE = 0x5,
NEX_VISIBLE = 0x6,
PSN_VISIBLE = 0x7,
LIMIT_WORLD_SIZE = 0x8,
LANGUAGE = 0x9,
SKIN_ID_0 = 0xA,
LAST_CUSTOM_SKIN_ID = 0xB,
RECENT_SKIN_ID_1 = 0xC,
RECENT_SKIN_ID_2 = 0xD,
RECENT_SKIN_ID_3 = 0xE,
LOGGED_INTO_XB1 = 0xF,
CHOSEN_NOT_SIGN_IN_XB1 = 0x10,
STORAGE_LOCATION = 0x11,
LEFT_HANDED = 0x12,
SPLIT_CONTROLS = 0x13,
SWAP_JUMP_AND_SNEAK = 0x14,
VIEW_DISTANCE = 0x15,
PARTICLE_VIEW_DISTANCE = 0x16,
VIEW_BOBBING = 0x17,
GRAPHICS = 0x18,
TRANSPARENTLEAVES = 0x19,
VR_TRANSPARENTLEAVES = 0x1A,
SMOOTH_LIGHTING = 0x1B,
VR_SMOOTH_LIGHTING = 0x1C,
FORCE_USE_UNSORTED_POLYS = 0x1D,
FANCY_SKIES = 0x1E,
FIXED_CAMERA = 0x1F,
HIDE_SCREENS = 0x20,
HIDE_ITEM_IN_HAND = 0x21,
FIELD_OF_VIEW = 0x22,
MSAA = 0x23,
TEXEL_AA = 0x24,
GAMMA = 0x25,
MULTITHREADED_RENDERER = 0x26,
VSYNC = 0x27,
ASYNC_TEXTURE_LOADS = 0x28,
ASYNC_TEXTURE_SHOW_MISSING_TEXTURE = 0x29,
ASYNC_TEXTURE_MAX_DEQUED_PER_FRAME = 0x2A,
ASYNC_TEXTURE_TEXTURE_LOAD_DELAY_MS = 0x2B,
FILE_WATCHER = 0x2C,
METAL_MASK = 0x2D,
FOLIAGE_LIGHT_WRAP = 0x2E,
LIGHT_WRAP_ENABLED = 0x2F,
ENVIRONMENT_LIGHT_SCALE = 0x30,
EMISSIVE_SCALE = 0x31,
METAL_COLOR_SCALE = 0x32,
LIGHT_SCALE = 0x33,
OPPOSING_LIGHT_SCALE = 0x34,
LIGHT_OFFSET = 0x35,
LENS_FLARE_ANGLE_APPEAR = 0x36,
DEPTH_OF_FIELD_NEAR_END_DEPTH = 0x37,
DEPTH_OF_FIELD_NEAR_START_BLUR_SIZE = 0x38,
DEPTH_OF_FIELD_FAR_START_DEPTH = 0x39,
DEPTH_OF_FIELD_FAR_END_DEPTH = 0x3A,
DEPTH_OF_FIELD_FAR_END_BLUR_SIZE = 0x3B,
MOTION_BLUR_ENABLE = 0x3C,
MOTION_BLUR_THRESHOLD = 0x3D,
LIGHT_COLOR = 0x3E,
BLOCK_LIGHT_COLOR = 0x3F,
BLOCK_LIGHT_SCALE = 0x40,
SKY_COLOR = 0x41,
RAYLEIGH_BETA = 0x42,
MIE_BETA = 0x43,
RAYLEIGH_HEIGHT_FALLOFF = 0x44,
RAYLEIGH_DIST_SCALE = 0x45,
AIR_SCATTER_SCALE = 0x46,
GROUND_SCATTER_COLOR = 0x47,
SKY_SCATTER_COLOR = 0x48,
SUN_SCATTER_INNER_COLOR = 0x49,
SUN_SCATTER_OUTER_COLOR = 0x4A,
GROUND_SCATTER_BETA = 0x4B,
GROUND_SCATTER_HEIGHT_FALLOFF = 0x4C,
GROUND_SCATTER_SCALE = 0x4D,
GROUND_SCATTER_DIST_SCALE = 0x4E,
SMOOTHNESS = 0x4F,
REFLECTANCE = 0x50,
RENDER_CHUNK_EDGE_BRIGHTNESS = 0x51,
RENDER_CHUNK_EDGE_TIGHTNESS = 0x52,
RENDER_CHUNK_EDGE_SHARPNESS = 0x53,
RENDER_CHUNK_EDGE_LOD_SCALAR = 0x54,
ITEM_IN_HAND_EDGE_BRIGHTNESS = 0x55,
ITEM_IN_HAND_EDGE_TIGHTNESS = 0x56,
ITEM_IN_HAND_EDGE_SHARPNESS = 0x57,
ENTITY_EDGE_BRIGHTNESS = 0x58,
ENTITY_EDGE_TIGHTNESS = 0x59,
ENTITY_EDGE_SHARPNESS = 0x5A,
ENTITY_EDGE_LOD_SCALAR = 0x5B,
PARALLAX_HEIGHT_SCALE = 0x5C,
REFL_DISTORT_MIN = 0x5D,
REFL_DISTORT_MAX = 0x5E,
WAVE_REFL_DISTORT_NEAR = 0x5F,
WAVE_REFL_DISTORT_FAR = 0x60,
WAVE_REFR_DISTORT = 0x61,
DIFFUSE_TINT = 0x62,
FOG_MIN_DEPTH = 0x63,
FOG_MAX_DEPTH = 0x64,
SPEC_COLOR_WATER = 0x65,
SHININESS = 0x66,
BLOOM_THRESHOLD = 0x67,
BLOOM_MAGNITUDE = 0x68,
BLOOM_BLUR_SIZE = 0x69,
ADAPTATION_RATE = 0x6A,
TONEMAP_TECHNIQUE = 0x6B,
EXPOSURE = 0x6C,
AUTO_EXPOSURE = 0x6D,
AUTO_EXPOSURE_KEY_VALUE = 0x6E,
SHOULDER_STRENGTH = 0x6F,
LINEAR_STRENGTH = 0x70,
LINEAR_ANGLE = 0x71,
TOE_STRENGTH = 0x72,
TOE_NUMERATOR = 0x73,
TOE_DENOMINATOR = 0x74,
HABLE_WHITE_LEVEL = 0x75,
EXPONENTIAL_WHITE_LEVEL = 0x76,
LOGARITHMIC_WHITE_LEVEL = 0x77,
REINHARD_MODIFIED_WHITE_LEVEL = 0x78,
DRAGO_WHITE_LEVEL = 0x79,
LUMINANCE_SATURATION = 0x7A,
LUM_MAP_MIP_LEVEL = 0x7B,
BIAS = 0x7C,
SHADOW_COVERAGE_DISTANCE_SCALE = 0x7D,
SHADOW_HIGH_DETAIL_DISTANCE_SCALE = 0x7E,
SHADOW_INTENSITY = 0x7F,
CLOUD_INTERIOR_FOG_DEPTH_START = 0x80,
CLOUD_INTERIOR_FOG_DEPTH_END = 0x81,
CLOUD_INTERIOR_FOG_MAX = 0x82,
CLOUD_INTERIOR_FOG_OUTER_SHELL_OPACITY_FACTOR = 0x83,
CLOUD_INTERIOR_FOG_OPACITY_FACTOR = 0x84,
CLOUD_INTERIOR_FOG_COLOR_DEBUG = 0x85,
CLOUD_INTERIOR_FOG_NEARBY_TRANSITION_THRESHOLD = 0x86,
CLOUD_FRESNEL_DISTANCE_START = 0x87,
CLOUD_FRESNEL_DISTANCE_END = 0x88,
CLOUD_LIGHT_FALLOFF_START = 0x89,
CLOUD_LIGHT_FALLOFF_END = 0x8A,
CLOUD_LIGHT_SPOT_POWER = 0x8B,
CLOUD_RENDER_NORMALS = 0x8C,
CLOUDS0_ENABLED = 0x8D,
CLOUDS0_COLOR = 0x8E,
CLOUDS0_OPACITY = 0x8F,
CLOUDS0_EMISSIVE_STRENGTH = 0x90,
CLOUDS0_LIGHT_WRAP_STRENGTH = 0x91,
CLOUDS0_TRANSMISSION_STRENGTH = 0x92,
CLOUDS0_EDGE_HIGHLIGHT_COLOR = 0x93,
CLOUDS0_EDGE_HIGHLIGHT_TIGHTNESS = 0x94,
CLOUDS0_NORMAL_BEND_TIGHTNESS = 0x95,
CLOUDS0_ALTITUDE = 0x96,
CLOUDS0_THICKNESS = 0x97,
CLOUDS0_BOUNDS = 0x98,
CLOUDS0_DRIFT_VELOCITY = 0x99,
CLOUDS0_ANIMATION_SPEED = 0x9A,
CLOUDS0_ANIMATION_PAUSE = 0x9B,
CLOUDS1_ENABLED = 0x9C,
CLOUDS1_COLOR = 0x9D,
CLOUDS1_OPACITY = 0x9E,
CLOUDS1_EMISSIVE_STRENGTH = 0x9F,
CLOUDS1_LIGHT_WRAP_STRENGTH = 0xA0,
CLOUDS1_TRANSMISSION_STRENGTH = 0xA1,
CLOUDS1_EDGE_HIGHLIGHT_COLOR = 0xA2,
CLOUDS1_EDGE_HIGHLIGHT_TIGHTNESS = 0xA3,
CLOUDS1_NORMAL_BEND_TIGHTNESS = 0xA4,
CLOUDS1_ALTITUDE = 0xA5,
CLOUDS1_THICKNESS = 0xA6,
CLOUDS1_BOUNDS = 0xA7,
CLOUDS1_DRIFT_VELOCITY = 0xA8,
CLOUDS1_ANIMATION_SPEED = 0xA9,
CLOUDS1_ANIMATION_PAUSE = 0xAA,
CLOUDS2_ENABLED = 0xAB,
CLOUDS2_COLOR = 0xAC,
CLOUDS2_OPACITY = 0xAD,
CLOUDS2_EMISSIVE_STRENGTH = 0xAE,
CLOUDS2_LIGHT_WRAP_STRENGTH = 0xAF,
CLOUDS2_TRANSMISSION_STRENGTH = 0xB0,
CLOUDS2_EDGE_HIGHLIGHT_COLOR = 0xB1,
CLOUDS2_EDGE_HIGHLIGHT_TIGHTNESS = 0xB2,
CLOUDS2_NORMAL_BEND_TIGHTNESS = 0xB3,
CLOUDS2_ALTITUDE = 0xB4,
CLOUDS2_THICKNESS = 0xB5,
CLOUDS2_BOUNDS = 0xB6,
CLOUDS2_DRIFT_VELOCITY = 0xB7,
CLOUDS2_ANIMATION_SPEED = 0xB8,
CLOUDS2_ANIMATION_PAUSE = 0xB9,
CLOUDS3_ENABLED = 0xBA,
CLOUDS3_COLOR = 0xBB,
CLOUDS3_OPACITY = 0xBC,
CLOUDS3_EMISSIVE_STRENGTH = 0xBD,
CLOUDS3_LIGHT_WRAP_STRENGTH = 0xBE,
CLOUDS3_TRANSMISSION_STRENGTH = 0xBF,
CLOUDS3_EDGE_HIGHLIGHT_COLOR = 0xC0,
CLOUDS3_EDGE_HIGHLIGHT_TIGHTNESS = 0xC1,
CLOUDS3_NORMAL_BEND_TIGHTNESS = 0xC2,
CLOUDS3_ALTITUDE = 0xC3,
CLOUDS3_THICKNESS = 0xC4,
CLOUDS3_BOUNDS = 0xC5,
CLOUDS3_DRIFT_VELOCITY = 0xC6,
CLOUDS3_ANIMATION_SPEED = 0xC7,
CLOUDS3_ANIMATION_PAUSE = 0xC8,
CLOUDS4_ENABLED = 0xC9,
CLOUDS4_COLOR = 0xCA,
CLOUDS4_OPACITY = 0xCB,
CLOUDS4_EMISSIVE_STRENGTH = 0xCC,
CLOUDS4_LIGHT_WRAP_STRENGTH = 0xCD,
CLOUDS4_TRANSMISSION_STRENGTH = 0xCE,
CLOUDS4_EDGE_HIGHLIGHT_COLOR = 0xCF,
CLOUDS4_EDGE_HIGHLIGHT_TIGHTNESS = 0xD0,
CLOUDS4_NORMAL_BEND_TIGHTNESS = 0xD1,
CLOUDS4_ALTITUDE = 0xD2,
CLOUDS4_THICKNESS = 0xD3,
CLOUDS4_BOUNDS = 0xD4,
CLOUDS4_DRIFT_VELOCITY = 0xD5,
CLOUDS4_ANIMATION_SPEED = 0xD6,
CLOUDS4_ANIMATION_PAUSE = 0xD7,
RAYS_ENABLE_DEBUG_TEXTURES = 0xD8,
RAYS_NUMBER_OF_SLICES = 0xD9,
RAYS_NUMBER_OF_SAMPLES_PER_SLICE = 0xDA,
RAYS_EPIPOLAR_STEP_WIDTH = 0xDB,
RAYS_DEPTH_BREAK_THRESHOLD = 0xDC,
RAYS_FIX_UP_TRESHOLD = 0xDD,
RAYS_RAY_CASTING_DISTANCE = 0xDE,
RAYS_RAY_CASTING_STEP_WIDTH = 0xDF,
WIND_ANGLE = 0xE0,
WIND_SPEED = 0xE1,
WIND_OCTAVE_1_AMPLITUDE = 0xE2,
WIND_OCTAVE_1_FREQUENCY = 0xE3,
WIND_OCTAVE_2_AMPLITUDE = 0xE4,
WIND_OCTAVE_2_FREQUENCY = 0xE5,
WIND_OCTAVE_3_AMPLITUDE = 0xE6,
WIND_OCTAVE_3_FREQUENCY = 0xE7,
GRASS_FLEXIBILITY = 0xE8,
TALL_GRASS_FLEXIBILITY = 0xE9,
CROPS_FLEXIBILITY = 0xEA,
LEAVES_FLEXIBILITY = 0xEB,
FLOWERS_FLEXIBILITY = 0xEC,
MAX_FRAMERATE = 0xED,
FULLSCREEN = 0xEE,
SHOW_ADVANCED_VIDEO_SETTINGS = 0xEF,
SHOW_TONEMAP_SETTINGS = 0xF0,
GUI_SCALE = 0xF1,
SPLIT_SCREEN_GUI_SCALE = 0xF2,
SAFE_ZONE_X = 0xF3,
SAFE_ZONE_Y = 0xF4,
SCREEN_POSITION_X = 0xF5,
SCREEN_POSITION_Y = 0xF6,
UI_PROFILE = 0xF7,
SOUND = 0xF8,
MUSIC = 0xF9,
VR_SENSITIVITY = 0xFA,
VR_GAMMA = 0xFB,
RESET_PLAYER_ALIGNMENT = 0xFC,
VR_PARTICLE_VIEW_DISTANCE = 0xFD,
STUTTER_TURN = 0xFE,
STUTTER_TURN_SOUND = 0xFF,
HMD_POSITION_DISPLACEMENT = 0x100,
VR_VIEW_DISTANCE = 0x101,
VR_AUTO_JUMP = 0x102,
VR_HEAD_STEERING = 0x103,
STUTTER_CONSTANT_TIME_MODE = 0x104,
STEREO_RENDERING = 0x105,
VR_HUD_AT_TOP = 0x106,
VR_USES_NORMAL_HIT_FX = 0x107,
VR_USES_RED_FLASH_FOR_HIT = 0x108,
VR_RIGHTSTICK_PITCHASSIST = 0x109,
VR_RIGHTSTICK_DEADBAND = 0x10A,
VR_RIGHTSTICK_GAZEADJUST = 0x10B,
VR_GAZE_PITCH_BOOST = 0x10C,
VR_HUD_DRIFTS = 0x10D,
VR_LIVING_ROOM_CURSOR_CENTERED = 0x10E,
VR_LINEAR_JUMP = 0x10F,
VR_LINEAR_MOTION = 0x110,
VR_STICKY_MINING = 0x111,
VR_STICKY_MINING_HAND_POINTER = 0x112,
VR_TAP_TURN = 0x113,
VR_TAP_TURN_SENSITIVITY = 0x114,
VR_ROLL_TURN_SENSITIVITY = 0x115,
VR_ROLL_TURNING = 0x116,
VR_180_TURNING = 0x117,
VR_OPTIONS_COMFORT_CONTROLS = 0x118,
VR_SHOW_OPTIONS_SELECT_SCREEN = 0x119,
VR_LVR_HINT_TIME = 0x11A,
VR_MIRROR_TEXTURE = 0x11B,
VR_HAND_CONTROLS_ITEM = 0x11C,
VR_HAND_CONTROLS_HUD = 0x11D,
VR_HAND_POINTER = 0x11E,
VR_HANDS_VISIBLE = 0x11F,
VR_UI_MOUSE_SENSITIVITY = 0x120,
VR_MSAA = 0x121,
VR_LIVING_ROOM_MODE = 0x122,
VR_JOYSTICKAIM = 0x123,
VR_JOYSTICKAIM_SENSITIVITY = 0x124,
VR_RIGHTSTICK_PITCH_MAXANGLE = 0x125,
VR_RIGHTSTICK_PITCHASSIST_STEPPINGS = 0x126,
STORE_HAS_PURCHASED_COINS = 0x127,
SWITCH_DEBUG_COINS = 0x128,
SHOW_CHUNK_MAP = 0x129,
SHOW_SERVER_CHUNK_MAP = 0x12A,
DEBUG_DISABLE_RENDER_TERRAIN = 0x12B,
DEBUG_DISABLE_RENDER_ENTITIES = 0x12C,
DEBUG_DISABLE_RENDER_BLOCKENTITIES = 0x12D,
DEBUG_DISABLE_RENDER_PARTICLES = 0x12E,
DEBUG_DISABLE_RENDER_SKY = 0x12F,
DEBUG_DISABLE_RENDER_WEATHER = 0x130,
DEBUG_DISABLE_RENDER_HUD = 0x131,
DEBUG_DISABLE_RENDER_ITEM_IN_HAND = 0x132,
ENABLE_PROFILER_OUTPUT = 0x133,
SILENT_ADD_USER = 0x134,
BENCHMARK_MODE_TIME = 0x135,
DISABLE_CLIENT_BLOB_CACHE = 0x136,
FORCE_CLIENT_BLOB_CACHE = 0x137,
CONNECTION_QUALITY = 0x138,
SHOW_LATENCY_GRAPH = 0x139,
RENDER_BOUNDING_BOXES = 0x13A,
RENDER_PATHS = 0x13B,
RENDER_GOAL_STATE = 0x13C,
RENDER_COORDINATE_SYSTEM = 0x13D,
NEW_PARTICLE_SYSTEM = 0x13E,
DISABLE_RAIN = 0x13F,
AUTO_LOAD_LEVEL = 0x140,
ACHIEVEMENTS_ALWAYS_ENABLED = 0x141,
REALM_CREATE_WITHOUT_PURCHASE = 0x142,
USE_IPV6_ONLY = 0x143,
USE_RETAIL_XBOX_SANDBOX = 0x144,
USE_OVERRIDE_DATE = 0x145,
DISPLAY_OVERRIDE_DATETIME = 0x146,
LOAD_OVERRIDE_DATE = 0x147,
OVERRIDE_DATE = 0x148,
OVERRIDE_TIME_SCALE = 0x149,
OVERRIDE_DATE_TYPE = 0x14A,
DISPLAY_MARKETPLACE_DOCUMENT_ID = 0x14B,
MARKETPLACE_DOCUMENT_ID = 0x14C,
REALMS_ENVIRONMENT = 0x14D,
REALMS_ENDPOINT = 0x14E,
REALMS_ENDPOINT_PAYMENT = 0x14F,
REALMS_RELYING_PARTY = 0x150,
REALMS_RELYING_PARTY_PAYMENT = 0x151,
STORE_OFFER_QUERY_REQUIRES_XBL = 0x152,
RESET_CLIENT_ID = 0x153,
LOG_FLUSH_IMMEDIATE = 0x154,
LOG_TIMESTAMP = 0x155,
LOG_TRACE = 0x156,
LOG_APPEND = 0x157,
LOG_AREA = 0x158,
LOG_PRIORITY = 0x159,
LOG_THREAD = 0x15A,
LOG_PROCESS_ID = 0x15B,
LOG_MESSAGE_ID = 0x15C,
LOG_SILENT = 0x15D,
LOG_PRIORITY_FILTER = 0x15E,
LOG_AREA_FILTER_STRING = 0x15F,
LOG_CATEGORY_WORLD_GEN = 0x160,
LOG_CATEGORY_LOOT = 0x161,
LOG_CATEGORY_RENDER = 0x162,
LOG_CATEGORY_STRUCTURE = 0x163,
LOG_CATEGORY_UI = 0x164,
LOG_CATEGORY_ONLINE = 0x165,
DEBUG_HUD = 0x166,
SHOW_BUILD_INFO = 0x167,
LAST_GAME_VERSION_MAJOR = 0x168,
LAST_GAME_VERSION_MINOR = 0x169,
LAST_GAME_VERSION_PATCH = 0x16A,
LAST_GAME_VERSION_REVISION = 0x16B,
LAST_GAME_VERSION_BETA = 0x16C,
USE_OVERRIDE_PATCHNOTES_CLIENT_VERSION = 0x16D,
REALMS_SHOW_FRIEND_INVITES_ONLY = 0x16E,
REALMS_NUMBER_OF_OWNED_REALMS = 0x16F,
REALMS_NUMBER_OF_FRIENDS_REALMS = 0x170,
REALMS_VIEW_UPSELL_SCREEN_COUNT = 0x171,
SHOWN_RATINGS_PROMPT = 0x172,
SAVE_AND_QUIT_COUNT = 0x173,
REALMS_SHOW_REALMS_TRIAL_ON_PLAY_SCREEN = 0x174,
ALLOW_CELLULAR_DATA = 0x175,
AUTO_UPDATE_MODE = 0x176,
AUTO_UPDATE_ENABLED = 0x177,
WEBSOCKET_ENCRYPTION = 0x178,
TEXT_TO_SPEECH_DISCOVERED = 0x179,
TEXT_TO_SPEECH_AUTO_ENABLE = 0x17A,
CHAT_TEXT_TO_SPEECH = 0x17B,
UI_TEXT_TO_SPEECH = 0x17C,
OPEN_CHAT_MESSAGE = 0x17D,
SENSITIVITY = 0x17E,
SMOOTH_ROTATION_SPEED = 0x17F,
INVERT_MOUSE = 0x180,
AUTO_JUMP = 0x181,
FULL_KEYBOARD_GAMEPLAY = 0x182,
DESTROY_VIBRATION = 0x183,
RENDER_CLOUDS = 0x184,
TOGGLE_CROUCH = 0x185,
GAME_SENSITIVITY = 0x186,
VR_GAME_SENSITIVITY = 0x187,
MULTIPLAYER_GAME = 0x188,
CROSSPLATFORM_GAME = 0x189,
LAST_XUID = 0x18A,
HIDE_PAPERDOLL = 0x18B,
ASSERTIONS_DEBUG_BREAK = 0x18C,
ASSERTIONS_SHOW_DIALOG = 0x18D,
SHOW_DEV_CONSOLE_BUTTON = 0x18E,
DISPLAY_TREATMENTS_PANEL = 0x18F,
HIDE_KEYBOARD_TOOLTIPS = 0x190,
HIDE_KEYBOARD_TOOLTIPS_OVERRIDDEN = 0x191,
HIDE_TOOLTIPS = 0x192,
CLASSIC_BOX_SELECTION = 0x193,
VR_CLASSIC_BOX_SELECTION = 0x194,
DEBUG_ATTACH_POS = 0x195,
DEBUG_SHOW_MINECRAFT_TCUI_REPLACEMENT = 0x196,
SPLIT_SCREEN = 0x197,
HIDE_HUD = 0x198,
HIDE_HAND = 0x199,
VR_HIDE_HUD = 0x19A,
VR_HIDE_HAND = 0x19B,
INGAME_PLAYER_NAMES = 0x19C,
SPLITSCREEN_INGAME_PLAYER_NAMES = 0x19D,
INTERFACE_OPACITY = 0x19E,
SPLITSCREEN_INTERFACE_OPACITY = 0x19F,
ACK_AUTO_SAVE = 0x1A0,
REALMSPLUS_UPGRADENOTICE_STATE = 0x1A1,
SHOW_AUTO_SAVE_ICON = 0x1A2,
HAS_SET_SAFE_ZONE = 0x1A3,
FIND_MOBS = 0x1A4,
FIELD_OF_VIEW_TOGGLE = 0x1A5,
HIDE_GAMEPAD_CURSOR = 0x1A6,
ENABLE_MIXER_INTERACTIVE = 0x1A7,
AUTOMATION_UPLOAD_TOKEN = 0x1A8,
AUTOMATION_UPLOAD_LOGS = 0x1A9,
AUTOMATION_LOG_FLUSH_DELAY = 0x1AA,
AUTOMATION_FILE_UPLOAD_ENDPOINT = 0x1AB,
AUTOMATION_APPEND_DEBUGLOG_TIMESTAMP = 0x1AC,
AUTOMATION_UNIT_TEST_TAGS = 0x1AD,
AUTOMATION_FUNCTIONAL_TEST_TAGS = 0x1AE,
AUTOMATION_UNIT_BLACKLIST_TEST_TAGS = 0x1AF,
AUTOMATION_FUNCTIONAL_BLACKLIST_TEST_TAGS = 0x1B0,
AUTOMATION_TESTRUN_TIMED_OUT = 0x1B1,
AUTOMATION_TESTRUN_ID = 0x1B2,
AUTOMATION_REPEAT_COUNT = 0x1B3,
AUTOMATION_REPEAT_FAILURES_ONLY = 0x1B4,
AUTOMATION_PER_TESTCASE_TIMEOUT = 0x1B5,
AUTOMATION_QUIT_APP = 0x1B6,
LIGHTING_ADJUSTMENT_VALUE = 0x1B7,
HAS_SET_LIGHTING_ADJUSTMENT_VALUE = 0x1B8,
DEBUG_DISABLE_CONNECTED_STORAGE_PULL = 0x1B9,
DEBUG_DISABLE_CONNECTED_STORAGE_PUSH = 0x1BA,
HOTBAR_ONLY_TOUCH = 0x1BB,
TEST_ASSETS_AZURE_SAS = 0x1BC,
TEST_ASSETS_AZURE_URL = 0x1BD,
TEST_ASSETS_LOCAL_PATH = 0x1BE,
GAMEPAD_CURSOR_SENSITIVITY = 0x1BF,
SHOWN_PATCH_NOTICE = 0x1C0,
LAST_SHOWN_REALMS_ENDED_DATE = 0x1C1,
IGNORE_USER_INPUT = 0x1C2,
SHOWN_PLATFORM_NETWORK_CONNECT_CONFIRMATION = 0x1C3,
SCREEN_ANIMATIONS = 0x1C4,
GAMEPAD_SWAP_AB_BUTTONS = 0x1C5,
GAMEPAD_SWAP_XY_BUTTONS = 0x1C6,
FANCY_BUBBLES = 0x1C7,
SHOWN_PLATFORM_PREMIUM_UPSELL = 0x1C8,
TEST_TAGS_SERVICE_URL = 0x1C9,
EDU_FIRST_LOGIN = 0x1CA,
TEST_BRANCH_NAME = 0x1CB,
FUNCTIONAL_TEST_BLOCK_INPUT = 0x1CC,
FUNCTIONAL_TEST_BLOCKING_INPUT = 0x1CD,
AUTOMATION_MARKETPLACE_BOOT_TEST_BATCH = 0x1CE,
AUTOMATION_MARKETPLACE_BOOT_TEST_RUN_BATCH_COUNT = 0x1CF,
DEV_CONSOLE_PREVIOUS_MESSAGES = 0x1D0,
CODE_SCREEN_VIEW = 0x1D1,
CODE_SCREEN_FIRST_TIME = 0x1D2,
CODE_SCREEN_IDE = 0x1D3,
CHAT_COLOR_CODE = 0x1D4,
CHAT_FONT_SIZE = 0x1D5,
CHAT_LINE_SPACING = 0x1D6,
CHAT_MENTIONS_COLOR_CODE = 0x1D7,
CHAT_TYPEFACE = 0x1D8,
LIBRARY_WELCOME = 0x1D9,
CONTENT_LOG_FILE = 0x1DA,
CONTENT_LOG_GUI = 0x1DB,
PERF_TURTLE = 0x1DC,
GAMEPLAY_TIPS_ENABLED = 0x1DD,
GAMEPLAY_TIPS_SHOULD_BE_SHOWN = 0x1DE,
IAP_OWNING_ACCOUNT = 0x1DF,
LAST_PLAYFAB_ID = 0x1E0,
CONTROL_TIPS_SHOULD_BE_SHOWN = 0x1E1,
PLAYFAB_ENVIRONMENT = 0x1E2,
AD_STAY_SIGNED_IN = 0x1E3,
AD_USE_SINGLE_SIGN_ON = 0x1E4,
AD_SHOW_DEBUG_PANEL = 0x1E5,
AD_TOKEN_REFRESH_THRESHOLD = 0x1E6,
AD_DEV_CONFIG = 0x1E7,
RENDER_SCHEDULER_INFO = 0x1E8,
WINDOWS_STORE_MODE = 0x1E9,
INVENTORY_TIPS_SHOULD_BE_SHOWN = 0x1EA,
TREE_TIPS_SHOULD_BE_SHOWN = 0x1EB,
OPEN_INVENTORY_TIPS_SHOULD_BE_SHOWN = 0x1EC,
USE_DEFAULT_FONT_OVERRIDES = 0x1ED,
DAY_ONE_EXPERIENCE_COMPLETED = 0x1EE,
SELECT_CRAFTTABLE_TIPS_SHOULD_BE_SHOWN = 0x1EF,
PLACE_CRAFTTABLE_TIPS_SHOULD_BE_SHOWN = 0x1F0,
USE_CRAFTTABLE_TIPS_SHOULD_BE_SHOWN = 0x1F1,
MAKE_CRAFTTABLE_TIPS_SHOULD_BE_SHOWN = 0x1F2,
NEED_MORE_MATERIALS_TIPS_SHOULD_BE_SHOWN = 0x1F3,
IS_LEGACY_PLAYER = 0x1F4,
PLAYFAB_COMMERCE = 0x1F5,
DO_NOT_SHOW_MULTIPLAYER_ONLINE_SAFETY_WARNING = 0x1F6,
ONLY_TRUSTED_SKINS_ALLOWED = 0x1F7,
COUNT_5 = 0x1F8,
};

```
#### OptionOwnerType : __int32
```cpp
/* 81326 */
enum OptionOwnerType : __int32
{
User_0 = 0x0,
Machine = 0x1,
};

```
#### OptionResetFlags : __int32
```cpp
/* 81329 */
enum OptionResetFlags : __int32
{
None_30 = 0x1,
KeyboardMouse = 0x2,
Controller = 0x4,
Touch_0 = 0x8,
Video = 0x10,
Audio = 0x20,
Chat_0 = 0x40,
Accessibility = 0x80,
Controls = 0xE,
};

```
#### OptionType : __int32
```cpp
/* 81341 */
enum OptionType : __int32
{
Boolean_0 = 0x0,
InputModeBoolean = 0x1,
Float_5 = 0x2,
InputModeFloat = 0x3,
String_3 = 0x4,
Int_4 = 0x5,
Enum_0 = 0x6,
Vec3_0 = 0x7,
};

```
#### OsVersion : __int32
```cpp
/* 480115 */
enum OsVersion : __int32
{
Unspecified_0 = 0x0,
Windows10 = 0x1,
Windows8_1 = 0x2,
Windows7 = 0x3,
};

```
#### OwnerStorageEntity::EmptyInit : __int32
```cpp
/* 13178 */
enum OwnerStorageEntity::EmptyInit : __int32
{
NoValue_0 = 0x0,
};

```
#### OwnerStorageEntity::VariadicInit : __int32
```cpp
/* 13179 */
enum OwnerStorageEntity::VariadicInit : __int32
{
NonAmbiguous_0 = 0x0,
};

```
#### OwnerStorageFeature::EmptyInit : __int32
```cpp
/* 31074 */
enum OwnerStorageFeature::EmptyInit : __int32
{
NoValue_1 = 0x0,
};

```
#### OwnerStorageFeature::VariadicInit : __int32
```cpp
/* 31075 */
enum OwnerStorageFeature::VariadicInit : __int32
{
NonAmbiguous_1 = 0x0,
};

```
#### OwnerStorageSharePtr<EntityRegistryOwned>::EmptyInit : __int32
```cpp
/* 13168 */
enum OwnerStorageSharePtr<EntityRegistryOwned>::EmptyInit : __int32
{
};

```
#### OwnerStorageSharePtr<EntityRegistryOwned>::VariadicInit : __int32
```cpp
/* 104380 */
enum OwnerStorageSharePtr<EntityRegistryOwned>::VariadicInit : __int32
{
NonAmbiguous_3 = 0x0,
};

```
#### OwnerStorageSharePtr<PerlinSimplexNoise>::EmptyInit : __int32
```cpp
/* 191526 */
enum OwnerStorageSharePtr<PerlinSimplexNoise>::EmptyInit : __int32
{
};

```
#### OwnerStorageSharePtr<PerlinSimplexNoise>::VariadicInit : __int32
```cpp
/* 191527 */
enum OwnerStorageSharePtr<PerlinSimplexNoise>::VariadicInit : __int32
{
NonAmbiguous_4 = 0x0,
};

```
#### POIType : __int32
```cpp
/* 53670 */
enum POIType : __int32
{
InvalidPOI = 0xFFFFFFFF,
Bed_1 = 0x0,
MeetingArea = 0x1,
Jobsite = 0x2,
Count_9 = 0x3,
};

```
#### PackAccessAssetGenerationResult : __int32
```cpp
/* 422544 */
enum PackAccessAssetGenerationResult : __int32
{
ReadContentsFile = 0x0,
IteratedThroughDirectory = 0x1,
Failed_7 = 0x2,
AlreadyGenerated = 0x3,
};

```
#### PackAccessStrategyType : __int32
```cpp
/* 83334 */
enum PackAccessStrategyType : __int32
{
Directory_0 = 0x0,
Zip = 0x1,
DirectoryAndZip = 0x2,
Invalid_17 = 0x3,
};

```
#### PackCategory : __int32
```cpp
/* 5659 */
enum PackCategory : __int32
{
_Unknown_0 = 0x0,
_RealmsUnknown_0 = 0x1,
Standard = 0x2,
Premium = 0x3,
Custom_0 = 0x4,
Subpack = 0x5,
};

```
#### PackErrorType : __int32
```cpp
/* 5657 */
enum PackErrorType : __int32
{
None_6 = 0x0,
IncompletePackError = 0x1,
PackParseError = 0x2,
PackLoadError = 0x3,
UIError = 0x4,
PackSettingsError = 0x5,
};

```
#### PackIconType : __int32
```cpp
/* 5660 */
enum PackIconType : __int32
{
Default_0 = 0x0,
Bugged = 0x1,
};

```
#### PackManifest::PackRedownloadableState : __int32
```cpp
/* 5776 */
enum PackManifest::PackRedownloadableState : __int32
{
Redownloadable = 0x0,
NotRedownloadable = 0x1,
Unknown_2 = 0x2,
};

```
#### PackManifestFormat : __int8
```cpp
/* 5777 */
enum PackManifestFormat : __int8
{
V0 = 0x0,
V1 = 0x1,
V2 = 0x2,
};

```
#### PackOrigin : __int32
```cpp
/* 5658 */
enum PackOrigin : __int32
{
_Unknown = 0x0,
_RealmsUnknown = 0x1,
Package = 0x2,
Treatment = 0x3,
Dev = 0x4,
World = 0x5,
User = 0x6,
TempCache = 0x7,
PremiumCache = 0x8,
PremiumTempCache = 0x9,
};

```
#### PackParseErrorType : __int32
```cpp
/* 83185 */
enum PackParseErrorType : __int32
{
None_31 = 0x0,
NoPackAccess = 0x1,
UnsupportedFileFormat = 0x2,
IncompletePack = 0x3,
NoManifest = 0x4,
ParseError = 0x5,
MissingProperty = 0x6,
MissingPropertyUpgraded = 0x7,
WrongTypeProperty = 0x8,
EmptyProperty = 0x9,
EmptyPropertyUpgraded = 0xA,
InvalidProperty = 0xB,
MalformedPropertyUUID = 0xC,
MalformedPropertyUUIDUpgraded = 0xD,
MalformedPropertyVERSION = 0xE,
MalformedPropertyVERSIONUpgraded = 0xF,
DuplicateUUIDUpgraded = 0x10,
DuplicateUUID = 0x11,
InvalidPackTypeUpgraded = 0x12,
MissingModules = 0x13,
MissingDependency = 0x14,
MultipleModules = 0x15,
MultipleModulesUpgraded = 0x16,
UnsupportedFormatVersion = 0x17,
PackUpgraded = 0x18,
InvalidCapability = 0x19,
UnsupportedBaseGameVersionPatch = 0x1A,
IgnoredProperty = 0x1B,
VersionTooHigh = 0x1C,
VersionTooLow = 0x1D,
MinEngineVersionCapFormatVersion1 = 0x1E,
Count_17 = 0x1F,
};

```
#### PackScope : __int8
```cpp
/* 5775 */
enum PackScope : __int8
{
Global = 0x1,
AddOn = 0x2,
Level = 0x4,
World_0 = 0x6,
Any_0 = 0x7,
Default_1 = 0x7,
};

```
#### PackType : __int8
```cpp
/* 2176 */
enum PackType : __int8
{
Invalid_0 = 0x0,
Addon = 0x1,
Cached = 0x2,
CopyProtected = 0x3,
Behavior = 0x4,
PersonaPiece = 0x5,
Resources = 0x6,
Skins = 0x7,
WorldTemplate = 0x8,
Count = 0x9,
};

```
#### PacketPriority : __int32
```cpp
/* 64314 */
enum PacketPriority : __int32
{
IMMEDIATE_PRIORITY = 0x0,
HIGH_PRIORITY = 0x1,
MEDIUM_PRIORITY = 0x2,
LOW_PRIORITY = 0x3,
NUMBER_OF_PRIORITIES = 0x4,
};

```
#### PacketReadResult : __int32
```cpp
/* 72420 */
enum PacketReadResult : __int32
{
Valid_0 = 0x0,
Malformed = 0x1,
Fixed = 0x2,
};

```
#### PacketReliability : __int32
```cpp
/* 73241 */
enum PacketReliability : __int32
{
UNRELIABLE = 0x0,
UNRELIABLE_SEQUENCED = 0x1,
RELIABLE = 0x2,
RELIABLE_ORDERED = 0x3,
RELIABLE_SEQUENCED = 0x4,
UNRELIABLE_WITH_ACK_RECEIPT = 0x5,
RELIABLE_WITH_ACK_RECEIPT = 0x6,
RELIABLE_ORDERED_WITH_ACK_RECEIPT = 0x7,
NUMBER_OF_RELIABILITIES = 0x8,
};

```
#### PageContent::PageType : __int8
```cpp
/* 77463 */
enum PageContent::PageType : __int8
{
Text_0 = 0x0,
Photo = 0x1,
Count_15 = 0x2,
};

```
#### PaletteColor : __int8
```cpp
/* 79623 */
enum PaletteColor : __int8
{
White_0 = 0x0,
Orange_0 = 0x1,
Magenta_0 = 0x2,
LightBlue = 0x3,
Yellow_0 = 0x4,
LightGreen = 0x5,
Pink_0 = 0x6,
Gray_0 = 0x7,
Silver_0 = 0x8,
Cyan_0 = 0x9,
Purple_0 = 0xA,
Blue_0 = 0xB,
Brown_0 = 0xC,
Green_0 = 0xD,
Red_0 = 0xE,
Black_0 = 0xF,
Count_16 = 0x10,
};

```
#### PandaVariant : __int32
```cpp
/* 124192 */
enum PandaVariant : __int32
{
DEFAULT_0 = 0x0,
LAZY = 0x1,
WORRIED = 0x2,
PLAYFUL = 0x3,
BROWN = 0x4,
WEAK = 0x5,
AGGRESSIVE = 0x6,
COUNT_7 = 0x7,
};

```
#### ParticleType : __int32
```cpp
/* 34992 */
enum ParticleType : __int32
{
Undefined_3 = 0x0,
Bubble = 0x1,
BubbleManual = 0x2,
Crit = 0x3,
BlockForceField = 0x4,
Smoke = 0x5,
Explode = 0x6,
Evaporation = 0x7,
Flame = 0x8,
Lava = 0x9,
LargeSmoke = 0xA,
RedDust = 0xB,
RisingBorderDust = 0xC,
IconCrack = 0xD,
SnowballPoof = 0xE,
LargeExplode = 0xF,
HugeExplosion = 0x10,
MobFlame = 0x11,
Heart = 0x12,
Terrain = 0x13,
TownAura = 0x14,
Portal = 0x15,
MobPortal = 0x16,
WaterSplash = 0x17,
WaterSplashManual = 0x18,
WaterWake = 0x19,
DripWater = 0x1A,
DripLava = 0x1B,
DripHoney = 0x1C,
FallingDust = 0x1D,
MobSpell = 0x1E,
MobSpellAmbient = 0x1F,
MobSpellInstantaneous = 0x20,
Ink = 0x21,
Slime_0 = 0x22,
RainSplash = 0x23,
VillagerAngry = 0x24,
VillagerHappy = 0x25,
EnchantingTable = 0x26,
TrackingEmitter = 0x27,
Note = 0x28,
WitchSpell = 0x29,
CarrotBoost = 0x2A,
MobAppearance = 0x2B,
EndRod = 0x2C,
DragonBreath = 0x2D,
Spit = 0x2E,
Totem = 0x2F,
Food = 0x30,
FireworksStarter = 0x31,
Fireworks = 0x32,
FireworksOverlay = 0x33,
BalloonGas = 0x34,
ColoredFlame = 0x35,
Sparkler_0 = 0x36,
Conduit = 0x37,
BubbleColumnUp = 0x38,
BubbleColumnDown = 0x39,
Sneeze = 0x3A,
ShulkerBullet_0 = 0x3B,
Bleach = 0x3C,
DragonDestroyBlock = 0x3D,
MyceliumDust = 0x3E,
FallingBorderDust = 0x3F,
CampfireSmoke = 0x40,
CampfireSmokeTall = 0x41,
DragonBreathFire = 0x42,
DragonBreathTrail = 0x43,
_count_8 = 0x44,
};

```
#### PathCompletionType : __int8
```cpp
/* 57493 */
enum PathCompletionType : __int8
{
EMPTY = 0x0,
PARTIAL = 0x1,
FULL = 0x2,
};

```
#### PermissionCommand::Action : __int32
```cpp
/* 426142 */
enum PermissionCommand::Action : __int32
{
List_1 = 0x0,
Reload_0 = 0x1,
Set_0 = 0x2,
};

```
#### PermissionCommand::AvailableCommandPermissionPresets : __int32
```cpp
/* 426191 */
enum PermissionCommand::AvailableCommandPermissionPresets : __int32
{
Visitor_0 = 0x0,
Member_0 = 0x1,
Operator_1 = 0x2,
Undefined_12 = 0x3,
};

```
#### Pillager::State : __int32
```cpp
/* 171005 */
enum Pillager::State : __int32
{
Normal_8 = 0x0,
Hold_0 = 0x1,
Charging_0 = 0x2,
};

```
#### PillarAxis : __int32
```cpp
/* 230435 */
enum PillarAxis : __int32
{
Y_1 = 0x0,
X_2 = 0x1,
Z_2 = 0x2,
_count_51 = 0x3,
};

```
#### PistonBlock::Type : __int32
```cpp
/* 251026 */
enum PistonBlock::Type : __int32
{
Normal_13 = 0x0,
Sticky = 0x1,
};

```
#### PistonBlockActor::PistonState : __int8
```cpp
/* 13193 */
enum PistonBlockActor::PistonState : __int8
{
Retracted = 0x0,
Expanding = 0x1,
Expanded = 0x2,
Retracting = 0x3,
};

```
#### PlaceType : __int32
```cpp
/* 258224 */
enum PlaceType : __int32
{
Arbitrary_0 = 0x0,
Sequential = 0x1,
};

```
#### PlatformType : __int32
```cpp
/* 6933 */
enum PlatformType : __int32
{
Desktop_0 = 0x0,
Pocket = 0x1,
Console_0 = 0x2,
SetTopBox = 0x3,
};

```
#### PlayStatus : __int32
```cpp
/* 77455 */
enum PlayStatus : __int32
{
LoginSuccess = 0x0,
LoginFailed_ClientOld = 0x1,
LoginFailed_ServerOld = 0x2,
PlayerSpawn = 0x3,
LoginFailed_InvalidTenant = 0x4,
LoginFailed_EditionMismatchEduToVanilla = 0x5,
LoginFailed_EditionMismatchVanillaToEdu = 0x6,
LoginFailed_ServerFullSubClient = 0x7,
};

```
#### Player::DimensionState : __int32
```cpp
/* 77066 */
enum Player::DimensionState : __int32
{
Ready_0 = 0x0,
Pending = 0x1,
WaitingServerResponse = 0x2,
WaitingArea = 0x3,
WaitingRespawn = 0x4,
};

```
#### Player::PositionMode : __int8
```cpp
/* 77067 */
enum Player::PositionMode : __int8
{
Normal_4 = 0x0,
Respawn_0 = 0x1,
Teleport_1 = 0x2,
OnlyHeadRot = 0x3,
};

```
#### Player::SpawnPositionSource : __int32
```cpp
/* 88612 */
enum Player::SpawnPositionSource : __int32
{
Randomizer = 0x0,
Respawn_2 = 0x1,
Teleport_3 = 0x2,
Static = 0x3,
};

```
#### Player::SpawnPositionState : __int32
```cpp
/* 88611 */
enum Player::SpawnPositionState : __int32
{
InitializeSpawnPositionRandomizer = 0x0,
WaitForClientAck = 0x1,
ChangeDimension_0 = 0x2,
WaitForDimension = 0x3,
ChooseSpawnArea = 0x4,
CheckLoadedChunk = 0x5,
ChooseSpawnPosition = 0x6,
SpawnComplete = 0x7,
};

```
#### PlayerActionType : __int32
```cpp
/* 13195 */
enum PlayerActionType : __int32
{
};

```
#### PlayerActionType_0 : __int32
```cpp
/* 77458 */
enum PlayerActionType_0 : __int32
{
Unknown_29 = 0xFFFFFFFF,
StartDestroyBlock = 0x0,
AbortDestroyBlock = 0x1,
StopDestroyBlock = 0x2,
GetUpdatedBlock = 0x3,
DropItem = 0x4,
StartSleeping = 0x5,
StopSleeping = 0x6,
Respawn_1 = 0x7,
StartJump = 0x8,
StartSprinting = 0x9,
StopSprinting = 0xA,
StartSneaking = 0xB,
StopSneaking = 0xC,
DEPRECATED_ChangeDimension = 0xD,
ChangeDimensionAck = 0xE,
StartGliding = 0xF,
StopGliding = 0x10,
DenyDestroyBlock = 0x11,
CrackBlock = 0x12,
ChangeSkin = 0x13,
UpdatedEnchantingSeed = 0x14,
StartSwimming = 0x15,
StopSwimming = 0x16,
StartSpinAttack = 0x17,
StopSpinAttack = 0x18,
StartBuildingBlock = 0x19,
};

```
#### PlayerAuthInputPacket::InputData : __int32
```cpp
/* 80058 */
enum PlayerAuthInputPacket::InputData : __int32
{
Ascend = 0x0,
Descend = 0x1,
NorthJump = 0x2,
JumpDown = 0x3,
SprintDown = 0x4,
ChangeHeight = 0x5,
Jumping = 0x6,
AutoJumpingInWater = 0x7,
Sneaking = 0x8,
SneakDown = 0x9,
Up = 0xA,
Down = 0xB,
Left_0 = 0xC,
Right_0 = 0xD,
UpLeft = 0xE,
UpRight = 0xF,
WantUp = 0x10,
WantDown = 0x11,
WantDownSlow = 0x12,
WantUpSlow = 0x13,
Sprinting = 0x14,
AscendScaffolding = 0x15,
DescendScaffolding = 0x16,
SneakToggleDown = 0x17,
PersistSneak = 0x18,
INPUT_NUM = 0x19,
};

```
#### PlayerListPacketType : __int8
```cpp
/* 80065 */
enum PlayerListPacketType : __int8
{
Add_2 = 0x0,
Remove_1 = 0x1,
};

```
#### PlayerPermissionLevel : __int8
```cpp
/* 2411 */
enum PlayerPermissionLevel : __int8
{
Visitor = 0x0,
Member = 0x1,
Operator = 0x2,
Custom = 0x3,
};

```
#### PlayerRespawnState : __int8
```cpp
/* 77454 */
enum PlayerRespawnState : __int8
{
SearchingForSpawn = 0x0,
ReadyToSpawn = 0x1,
ClientReadyToSpawn = 0x2,
};

```
#### PlayerScoreSetFunction : __int8
```cpp
/* 80243 */
enum PlayerScoreSetFunction : __int8
{
Set = 0x0,
Add_3 = 0x1,
Subtract = 0x2,
};

```
#### PlayerSuspension::State : __int32
```cpp
/* 87673 */
enum PlayerSuspension::State : __int32
{
Suspend = 0x0,
Resume_0 = 0x1,
};

```
#### PlayerUISlot : __int32
```cpp
/* 79714 */
enum PlayerUISlot : __int32
{
CursorSelected = 0x0,
AnvilInput = 0x1,
AnvilMaterial = 0x2,
StoneCutterInput = 0x3,
Trade2Ingredient1 = 0x4,
Trade2Ingredient2 = 0x5,
TradeIngredient1 = 0x6,
TradeIngredient2 = 0x7,
MaterialReducerInput = 0x8,
LoomInput = 0x9,
LoomDye = 0xA,
LoomMaterial = 0xB,
CartographyInput = 0xC,
CartographyAdditional = 0xD,
EnchantingInput = 0xE,
EnchantingMaterial = 0xF,
GrindstoneInput = 0x10,
GrindstoneAdditional = 0x11,
CompoundCreatorInput1 = 0x12,
CompoundCreatorInput2 = 0x13,
CompoundCreatorInput3 = 0x14,
CompoundCreatorInput4 = 0x15,
CompoundCreatorInput5 = 0x16,
CompoundCreatorInput6 = 0x17,
CompoundCreatorInput7 = 0x18,
CompoundCreatorInput8 = 0x19,
CompoundCreatorInput9 = 0x1A,
BeaconPayment = 0x1B,
Crafting2x2Input1 = 0x1C,
Crafting2x2Input2 = 0x1D,
Crafting2x2Input3 = 0x1E,
Crafting2x2Input4 = 0x1F,
Crafting3x3Input1 = 0x20,
Crafting3x3Input2 = 0x21,
Crafting3x3Input3 = 0x22,
Crafting3x3Input4 = 0x23,
Crafting3x3Input5 = 0x24,
Crafting3x3Input6 = 0x25,
Crafting3x3Input7 = 0x26,
Crafting3x3Input8 = 0x27,
Crafting3x3Input9 = 0x28,
MaterialReducerOutput1 = 0x29,
MaterialReducerOutput2 = 0x2A,
MaterialReducerOutput3 = 0x2B,
MaterialReducerOutput4 = 0x2C,
MaterialReducerOutput5 = 0x2D,
MaterialReducerOutput6 = 0x2E,
MaterialReducerOutput7 = 0x2F,
MaterialReducerOutput8 = 0x30,
MaterialReducerOutput9 = 0x31,
CreatedItemOutput = 0x32,
_count_17 = 0x33,
};

```
#### PortalAxis : __int32
```cpp
/* 88949 */
enum PortalAxis : __int32
{
Unknown_33 = 0x0,
X_1 = 0x1,
Z_1 = 0x2,
_count_18 = 0x3,
};

```
#### Potion::PotionType : __int32
```cpp
/* 77460 */
enum Potion::PotionType : __int32
{
Undefined_9 = 0xFFFFFFFF,
Regular = 0x0,
Splash_0 = 0x1,
Lingering = 0x2,
};

```
#### Potion::PotionVariant : __int32
```cpp
/* 75384 */
enum Potion::PotionVariant : __int32
{
MOVESLOW = 0x0,
MOVESPEED = 0x1,
DIGSLOW = 0x2,
DIGSPEED = 0x3,
DAMAGEBOOST = 0x4,
HEAL = 0x5,
HARM = 0x6,
JUMP_0 = 0x7,
CONFUSION = 0x8,
REGEN = 0x9,
RESISTANCE = 0xA,
FIRERESISTANCE = 0xB,
WATERBREATH = 0xC,
INVISIBILITY = 0xD,
BLINDNESS = 0xE,
NIGHTVISION = 0xF,
HUNGER = 0x10,
WEAKNESS = 0x11,
POISON = 0x12,
WITHER = 0x13,
HEALTHBOOST = 0x14,
ABSORPTION = 0x15,
SATURATION = 0x16,
LEVITATION = 0x17,
TURTLEMASTER = 0x18,
SLOWFALL = 0x19,
BASE = 0x1A,
};

```
#### PressurePlateBlock::Sensitivity : __int32
```cpp
/* 251032 */
enum PressurePlateBlock::Sensitivity : __int32
{
EVERYTHING = 0x0,
MOBS = 0x1,
PLAYERS = 0x2,
};

```
#### PrismarineBlockType : __int32
```cpp
/* 183771 */
enum PrismarineBlockType : __int32
{
Default_16 = 0x0,
Dark = 0x1,
Bricks_0 = 0x2,
_count_41 = 0x3,
};

```
#### ProfanityFilterContext : __int32
```cpp
/* 109112 */
enum ProfanityFilterContext : __int32
{
None_41 = 0x0,
UIFrontEnd = 0x1,
UIInGame = 0x2,
AllUI = 0x3,
InGameChat = 0x4,
InGameItems = 0x8,
InGameName = 0x10,
All_4 = 0x1F,
};

```
#### Profession : __int32
```cpp
/* 171074 */
enum Profession : __int32
{
};

```
#### ProfilerLite::ScopeTag : __int32
```cpp
/* 603 */
enum ProfilerLite::ScopeTag : __int32
{
None = 0x0,
Root = 0x1,
BeginFrame = 0x2,
ClientInstance = 0x3,
EndFrame = 0x4,
Present = 0x5,
Input = 0x6,
ClientSimTick = 0x7,
ClientRealTick = 0x8,
ServerInstance = 0x9,
ServerSimTick = 0xA,
ServerRealTick = 0xB,
Render = 0xC,
RenderLevel = 0xD,
TickAndRenderUI = 0xE,
Last = 0xE,
SimTickFirst = 0x7,
SimTickLast = 0xB,
RenderTickFirst = 0xC,
RenderTickLast = 0xE,
};

```
#### ProjectileAnchor : __int32
```cpp
/* 58004 */
enum ProjectileAnchor : __int32
{
Origin = 0x0,
EyeHeight = 0x1,
Middle = 0x2,
Count_10 = 0x3,
};

```
#### ProjectileComponent::EAxis : __int32
```cpp
/* 58005 */
enum ProjectileComponent::EAxis : __int32
{
NONE_4 = 0xFFFFFFFF,
X_0 = 0x0,
Y = 0x1,
Z_0 = 0x2,
};

```
#### Projection : __int32
```cpp
/* 36134 */
enum Projection : __int32
{
Rigid = 0x0,
TerrainMatching = 0x1,
Invalid_9 = 0x2,
};

```
#### PurchasePath : __int32
```cpp
/* 45318 */
enum PurchasePath : __int32
{
Unknown_21 = 0xFFFFFFFF,
MinecoinScreen = 0x0,
InsufficientFunds = 0x1,
RealMoneyButton = 0x2,
Redeemed5x5 = 0x3,
Realms_0 = 0x4,
DurableCatalogOffer = 0x5,
};

```
#### PushNotificationType : __int32
```cpp
/* 45338 */
enum PushNotificationType : __int32
{
Achievement_0 = 0x0,
MultiplayerInvite = 0x1,
MultiplayerInviteRaw = 0x2,
FocusLost = 0x3,
BrazeModalDialog = 0x4,
BrazeToast = 0x5,
Toast = 0x6,
DeepLink = 0x7,
RemoveRequest = 0x8,
Unknown_22 = 0x63,
};

```
#### Raid::RaidState : __int32
```cpp
/* 52780 */
enum Raid::RaidState : __int32
{
PreparingGroup = 0x0,
PickingSpawnPoint = 0x1,
SpawningGroup = 0x2,
GroupInPlay = 0x3,
AwardingRewards = 0x4,
Finished = 0x5,
};

```
#### RailDirection : __int32
```cpp
/* 460187 */
enum RailDirection : __int32
{
NorthSouth = 0x0,
EastWest = 0x1,
AscendingEast_0 = 0x2,
AscendingWest_0 = 0x3,
AscendingNorth_0 = 0x4,
AscendingSouth_0 = 0x5,
SouthEast_0 = 0x6,
SouthWest_0 = 0x7,
NorthWest_0 = 0x8,
NorthEast_0 = 0x9,
};

```
#### RakNet::AdapterAttributes : __int32
```cpp
/* 73239 */
enum RakNet::AdapterAttributes : __int32
{
NO_ATTRIBUTES = 0x0,
IS_MULTICAST = 0x1,
IS_LOOPBACK = 0x2,
HAS_NO_GATEWAY = 0x4,
};

```
#### RakNet::ConnectionAttemptResult : __int32
```cpp
/* 73238 */
enum RakNet::ConnectionAttemptResult : __int32
{
CONNECTION_ATTEMPT_STARTED = 0x0,
INVALID_PARAMETER = 0x1,
CANNOT_RESOLVE_DOMAIN_NAME = 0x2,
ALREADY_CONNECTED_TO_ENDPOINT = 0x3,
CONNECTION_ATTEMPT_ALREADY_IN_PROGRESS = 0x4,
SECURITY_INITIALIZATION_FAILED = 0x5,
};

```
#### RakNet::ConnectionState : __int32
```cpp
/* 478071 */
enum RakNet::ConnectionState : __int32
{
IS_PENDING = 0x0,
IS_CONNECTING = 0x1,
IS_CONNECTED = 0x2,
IS_DISCONNECTING = 0x3,
IS_SILENTLY_DISCONNECTING = 0x4,
IS_DISCONNECTED = 0x5,
IS_NOT_CONNECTED = 0x6,
};

```
#### RakNet::InternalPacket::AllocationScheme : __int32
```cpp
/* 477995 */
enum RakNet::InternalPacket::AllocationScheme : __int32
{
NORMAL_0 = 0x0,
REF_COUNTED = 0x1,
STACK = 0x2,
};

```
#### RakNet::PI2_FailedConnectionAttemptReason : __int32
```cpp
/* 478076 */
enum RakNet::PI2_FailedConnectionAttemptReason : __int32
{
FCAR_CONNECTION_ATTEMPT_FAILED = 0x0,
FCAR_ALREADY_CONNECTED = 0x1,
FCAR_NO_FREE_INCOMING_CONNECTIONS = 0x2,
FCAR_SECURITY_PUBLIC_KEY_MISMATCH = 0x3,
FCAR_CONNECTION_BANNED = 0x4,
FCAR_INVALID_PASSWORD = 0x5,
FCAR_INCOMPATIBLE_PROTOCOL = 0x6,
FCAR_IP_RECENTLY_CONNECTED = 0x7,
FCAR_REMOTE_SYSTEM_REQUIRES_PUBLIC_KEY = 0x8,
FCAR_OUR_SYSTEM_REQUIRES_SECURITY = 0x9,
FCAR_PUBLIC_KEY_MISMATCH = 0xA,
};

```
#### RakNet::PI2_LostConnectionReason : __int32
```cpp
/* 478075 */
enum RakNet::PI2_LostConnectionReason : __int32
{
LCR_CLOSED_BY_USER = 0x0,
LCR_DISCONNECTION_NOTIFICATION = 0x1,
LCR_CONNECTION_LOST = 0x2,
};

```
#### RakNet::PluginReceiveResult : __int32
```cpp
/* 478074 */
enum RakNet::PluginReceiveResult : __int32
{
RR_STOP_PROCESSING_AND_DEALLOCATE = 0x0,
RR_CONTINUE_PROCESSING = 0x1,
RR_STOP_PROCESSING = 0x2,
};

```
#### RakNet::PublicKeyMode : __int32
```cpp
/* 478042 */
enum RakNet::PublicKeyMode : __int32
{
PKM_INSECURE_CONNECTION = 0x0,
PKM_ACCEPT_ANY_PUBLIC_KEY = 0x1,
PKM_USE_KNOWN_PUBLIC_KEY = 0x2,
PKM_USE_TWO_WAY_AUTHENTICATION = 0x3,
};

```
#### RakNet::RNS2BindResult : __int32
```cpp
/* 478073 */
enum RakNet::RNS2BindResult : __int32
{
BR_SUCCESS = 0x0,
BR_REQUIRES_RAKNET_SUPPORT_IPV6_DEFINE = 0x1,
BR_FAILED_TO_BIND_SOCKET = 0x2,
BR_FAILED_SEND_TEST = 0x3,
};

```
#### RakNet::RNS2Type : __int32
```cpp
/* 478145 */
enum RakNet::RNS2Type : __int32
{
RNS2T_WINDOWS_STORE_8 = 0x0,
RNS2T_PS3 = 0x1,
RNS2T_PS4 = 0x2,
RNS2T_CHROME = 0x3,
RNS2T_VITA = 0x4,
RNS2T_XBOX_360 = 0x5,
RNS2T_XBOX_720 = 0x6,
RNS2T_WINDOWS = 0x7,
RNS2T_LINUX = 0x8,
};

```
#### RakNet::RNSPerSecondMetrics : __int32
```cpp
/* 64311 */
enum RakNet::RNSPerSecondMetrics : __int32
{
USER_MESSAGE_BYTES_PUSHED = 0x0,
USER_MESSAGE_BYTES_SENT = 0x1,
USER_MESSAGE_BYTES_RESENT = 0x2,
USER_MESSAGE_BYTES_RECEIVED_PROCESSED = 0x3,
USER_MESSAGE_BYTES_RECEIVED_IGNORED = 0x4,
ACTUAL_BYTES_SENT = 0x5,
ACTUAL_BYTES_RECEIVED = 0x6,
RNS_PER_SECOND_METRICS_COUNT = 0x7,
};

```
#### RakNet::RakPeer::$1054D3269989E0175094BA1B08A2EDA8 : __int32
```cpp
/* 478069 */
enum RakNet::RakPeer::$1054D3269989E0175094BA1B08A2EDA8 : __int32
{
requestedConnectionList_Mutex = 0x0,
offlinePingResponse_Mutex = 0x1,
NUMBER_OF_RAKPEER_MUTEXES = 0x2,
};

```
#### RakNet::RakPeer::BufferedCommandStruct::$D8D77DCE4D37D1D6016B84EB664ECA65 : __int32
```cpp
/* 478050 */
enum RakNet::RakPeer::BufferedCommandStruct::$D8D77DCE4D37D1D6016B84EB664ECA65 : __int32
{
BCS_SEND = 0x0,
BCS_CLOSE_CONNECTION = 0x1,
BCS_GET_SOCKET = 0x2,
BCS_CHANGE_SYSTEM_ADDRESS = 0x3,
BCS_DO_NOTHING = 0x4,
};

```
#### RakNet::RakPeer::RemoteSystemStruct::ConnectMode : __int32
```cpp
/* 478031 */
enum RakNet::RakPeer::RemoteSystemStruct::ConnectMode : __int32
{
NO_ACTION = 0x0,
DISCONNECT_ASAP = 0x1,
DISCONNECT_ASAP_SILENTLY = 0x2,
DISCONNECT_ON_NO_ACK = 0x3,
REQUESTED_CONNECTION = 0x4,
HANDLING_CONNECTION_REQUEST = 0x5,
UNVERIFIED_SENDER = 0x6,
CONNECTED = 0x7,
};

```
#### RakNet::RakPeer::RequestedConnectionStruct::$FD3B22BB7AF8A0ABB9D04D1A9E595697 : __int32
```cpp
/* 478043 */
enum RakNet::RakPeer::RequestedConnectionStruct::$FD3B22BB7AF8A0ABB9D04D1A9E595697 : __int32
{
CONNECT = 0x1,
};

```
#### RakNet::StartupResult : __int32
```cpp
/* 63570 */
enum RakNet::StartupResult : __int32
{
RAKNET_STARTED = 0x0,
RAKNET_ALREADY_STARTED = 0x1,
INVALID_SOCKET_DESCRIPTORS = 0x2,
INVALID_MAX_CONNECTIONS = 0x3,
SOCKET_FAMILY_NOT_SUPPORTED = 0x4,
SOCKET_PORT_ALREADY_IN_USE = 0x5,
SOCKET_FAILED_TO_BIND = 0x6,
SOCKET_FAILED_TEST_SEND = 0x7,
PORT_CANNOT_BE_ZERO = 0x8,
FAILED_TO_CREATE_NETWORK_THREAD = 0x9,
COULD_NOT_GENERATE_GUID = 0xA,
STARTUP_OTHER_FAILURE = 0xB,
};

```
#### RakNetInstance::NATState : __int32
```cpp
/* 73237 */
enum RakNetInstance::NATState : __int32
{
NotStarted = 0x0,
PunchRequested = 0x1,
PunchStarted = 0x2,
PunchAddressRegistered = 0x3,
SendingPunchPings = 0x4,
PunchSucceeded = 0x5,
PunchFailed = 0x6,
};

```
#### RakNetServerLocator::protocolVersion : __int32
```cpp
/* 73588 */
enum RakNetServerLocator::protocolVersion : __int32
{
ipv4 = 0x4,
ipv6 = 0x6,
};

```
#### RakPeerHelper::IPVersion : __int32
```cpp
/* 73593 */
enum RakPeerHelper::IPVersion : __int32
{
IPv4_0 = 0x0,
IPv6_0 = 0x1,
COUNT_4 = 0x2,
};

```
#### RawInputType : __int8
```cpp
/* 44570 */
enum RawInputType : __int8
{
};

```
#### Realms::World::State : __int32
```cpp
/* 45316 */
enum Realms::World::State : __int32
{
Uninitialized = 0x0,
Closed = 0x1,
Open = 0x2,
End_0 = 0x3,
};

```
#### RecipeContainerBackgroundStyle : __int32
```cpp
/* 456085 */
enum RecipeContainerBackgroundStyle : __int32
{
Default_20 = 0x0,
GroupHeadCollapsed = 0x1,
GroupHeadExpanded = 0x2,
GroupItem = 0x3,
GroupItemRed = 0x4,
Count_27 = 0x5,
};

```
#### RedefinitionMode : __int8
```cpp
/* 74149 */
enum RedefinitionMode : __int8
{
KeepCurrent = 0x0,
UpdateToNewDefault = 0x1,
};

```
#### RegistrationType : __int32
```cpp
/* 99881 */
enum RegistrationType : __int32
{
MINECRAFT = 0x0,
CUSTOM = 0x1,
NONE_8 = 0x2,
};

```
#### RenderCapability : __int32
```cpp
/* 483788 */
enum RenderCapability : __int32
{
SuperFancyShading = 0x0,
LushLeaves = 0x1,
Atmospherics = 0x2,
EdgeHighlighting = 0x3,
Bloom = 0x4,
TerrainShadows = 0x5,
SuperDuperClouds = 0x6,
LightRays = 0x7,
DepthOfField = 0x8,
SuperDuperWater = 0x9,
CloudFog = 0xA,
FoliageWind = 0xB,
SkyTexture = 0xC,
ToneMap = 0xD,
COUNT_15 = 0xE,
};

```
#### RenderParam : __int32
```cpp
/* 115735 */
enum RenderParam : __int32
{
Unknown_38 = 0xFFFFFFFF,
FrameAlpha = 0x0,
Bob = 0x1,
ModelScale = 0x2,
AnimTime = 0x3,
DeltaTime = 0x4,
KeyFrameLerpTime = 0x5,
LifeTime = 0x6,
IsFirstPerson = 0x7,
NumRenderParams = 0x8,
};

```
#### RepeaterCapacitor::States : __int32
```cpp
/* 464259 */
enum RepeaterCapacitor::States : __int32
{
OFF = 0x0,
ON = 0x1,
OFF_LOCKED = 0x2,
ON_LOCKED = 0x3,
};

```
#### ReplaceItemCommand::TargetType : __int32
```cpp
/* 426462 */
enum ReplaceItemCommand::TargetType : __int32
{
Block_1 = 0x0,
Entity_7 = 0x1,
};

```
#### ResourceFileSystem : __int32
```cpp
/* 2550 */
enum ResourceFileSystem : __int32
{
UserPackage = 0x0,
AppPackage = 0x1,
Raw = 0x2,
RawPersistent = 0x3,
SettingsDir = 0x4,
ExternalDir = 0x5,
ServerPackage = 0x6,
DataDir = 0x7,
UserDir = 0x8,
ScreenshotsDir = 0x9,
StoreCache = 0xA,
Invalid_1 = 0xB,
};

```
#### ResourceInformation::ResourceType : __int32
```cpp
/* 5757 */
enum ResourceInformation::ResourceType : __int32
{
Invalid_7 = 0x0,
Resources_0 = 0x1,
DataAddOn = 0x2,
ScriptAddOn = 0x3,
ClientData = 0x4,
Interface = 0x5,
Mandatory = 0x6,
WorldTemplate_0 = 0x7,
Count_2 = 0x8,
};

```
#### ResourceLoadType : __int32
```cpp
/* 60434 */
enum ResourceLoadType : __int32
{
None_22 = 0x0,
Texture_0 = 0x1,
Sound_0 = 0x2,
MusicDefinition = 0x3,
Localization = 0x4,
Geometry_1 = 0x5,
TerrainAtlas = 0x6,
ItemAtlas = 0x7,
AnimatedAtlas = 0x8,
FontGlyph = 0x9,
BlockGraphics = 0xA,
Tessellator = 0xB,
Material_0 = 0xC,
Seasons = 0xD,
ActorResourceDefinition = 0xE,
UIDefinitions = 0xF,
UIDefinitionReferences = 0x10,
UIDefinitionReports = 0x11,
UIDefinitionResults = 0x12,
ActorSkeletalAnimation = 0x13,
ActorAnimationController = 0x14,
RenderController = 0x15,
ClientInstanceLoadResources = 0x16,
ItemRenderer = 0x17,
DynamicTextures = 0x18,
LevelRenderer = 0x19,
ParticleStaticResources = 0x1A,
FoliageColors = 0x1B,
ClearAndResetFontData = 0x1C,
FinalizeLoad = 0x1D,
ParticleEffect = 0x1E,
All_2 = 0x1F,
Count_11 = 0x1F,
};

```
#### ResourcePackResponse : __int8
```cpp
/* 77456 */
enum ResourcePackResponse : __int8
{
Cancel = 0x1,
Downloading = 0x2,
DownloadingFinished = 0x3,
ResourcePackStackFinished = 0x4,
};

```
#### ResourcePackStackType : __int32
```cpp
/* 5662 */
enum ResourcePackStackType : __int32
{
LEVEL = 0x0,
ADDON = 0x1,
GLOBAL = 0x2,
TREATMENT = 0x3,
BASE_GAME = 0x4,
SIZE = 0x5,
};

```
#### RespawnAnimation : __int32
```cpp
/* 169786 */
enum RespawnAnimation : __int32
{
NONE_10 = 0x0,
START = 0x1,
PREPARING_TO_SUMMON_PILLARS = 0x2,
SUMMONING_PILLARS = 0x3,
SUMMONING_DRAGON = 0x4,
END = 0x5,
};

```
#### RopeParams::Flags : __int32
```cpp
/* 291989 */
enum RopeParams::Flags : __int32
{
None_53 = 0x0,
DynamicResize = 0x2,
DynamicStretch = 0x4,
CollisionEnabled = 0x8,
};

```
#### RopeWave::Direction : __int32
```cpp
/* 88926 */
enum RopeWave::Direction : __int32
{
StartToEnd = 0x0,
EndToStart = 0x1,
};

```
#### Rotation : __int8
```cpp
/* 5803 */
enum Rotation : __int8
{
};

```
#### Rotation_0 : __int8
```cpp
/* 35193 */
enum Rotation_0 : __int8
{
None_14 = 0x0,
Rotate90 = 0x1,
Rotate180 = 0x2,
Rotate270 = 0x3,
Total = 0x4,
};

```
#### SPSCQueue<BatchedNetworkPeer::DataCallback,512>::AllocationMode : __int32
```cpp
/* 421278 */
enum SPSCQueue<BatchedNetworkPeer::DataCallback,512>::AllocationMode : __int32
{
CanAlloc_4 = 0x0,
CannotAlloc_4 = 0x1,
};

```
#### SandStoneType : __int32
```cpp
/* 183772 */
enum SandStoneType : __int32
{
Default_17 = 0x0,
Heiroglyphs = 0x1,
Cut = 0x2,
Smooth_1 = 0x3,
_count_42 = 0x4,
};

```
#### SandType : __int32
```cpp
/* 170973 */
enum SandType : __int32
{
Normal_7 = 0x0,
Red_1 = 0x1,
_count_24 = 0x2,
};

```
#### SaplingType : __int32
```cpp
/* 183773 */
enum SaplingType : __int32
{
Default_18 = 0x0,
Evergreen = 0x1,
Birch_3 = 0x2,
Jungle_5 = 0x3,
Acacia_3 = 0x4,
RoofedOak = 0x5,
_count_43 = 0x6,
};

```
#### SaveCommand::Mode : __int32
```cpp
/* 6500 */
enum SaveCommand::Mode : __int32
{
Hold = 0x0,
Resume = 0x1,
Query = 0x2,
};

```
#### SaveCommand::State : __int32
```cpp
/* 6615 */
enum SaveCommand::State : __int32
{
Idle = 0x0,
Saving = 0x1,
Complete = 0x2,
};

```
#### ScatterParams::CoordinateEvaluationOrder : __int32
```cpp
/* 192994 */
enum ScatterParams::CoordinateEvaluationOrder : __int32
{
XYZ_0 = 0x0,
XZY = 0x1,
YXZ = 0x2,
YZX = 0x3,
ZXY = 0x4,
ZYX = 0x5,
};

```
#### ScatterParams::RandomDistributionType : __int32
```cpp
/* 192993 */
enum ScatterParams::RandomDistributionType : __int32
{
SingleValued = 0x0,
Uniform_0 = 0x1,
Gaussian = 0x2,
Grid = 0x3,
};

```
#### ScorePacketType : __int8
```cpp
/* 80433 */
enum ScorePacketType : __int8
{
Change = 0x0,
Remove_2 = 0x1,
};

```
#### ScoreboardCommand::Action : __int32
```cpp
/* 426673 */
enum ScoreboardCommand::Action : __int32
{
Invalid_29 = 0x0,
Add_7 = 0x1,
List_2 = 0x2,
Operation = 0x3,
Random_3 = 0x4,
Remove_5 = 0x5,
Reset_1 = 0x6,
Set_1 = 0x7,
SetDisplay = 0x8,
Test_1 = 0x9,
};

```
#### ScoreboardCommand::Category : __int32
```cpp
/* 426624 */
enum ScoreboardCommand::Category : __int32
{
Objectives = 0x0,
Players_0 = 0x1,
};

```
#### ScoreboardIdentityPacketType : __int8
```cpp
/* 80489 */
enum ScoreboardIdentityPacketType : __int8
{
Update_0 = 0x0,
Remove_3 = 0x1,
};

```
#### ScriptApi::ApiScriptType : __int32
```cpp
/* 99154 */
enum ScriptApi::ApiScriptType : __int32
{
Server_2 = 0x0,
Client_2 = 0x1,
};

```
#### ScriptApi::ScriptObjectType : __int32
```cpp
/* 100495 */
enum ScriptApi::ScriptObjectType : __int32
{
UndefinedType = 0x0,
NullType = 0x1,
NumberType = 0x2,
StringType = 0x3,
BooleanType = 0x4,
ObjectType = 0x5,
ArrayType = 0x6,
FunctionType = 0x7,
};

```
#### ScriptApi::ScriptReportItemType : __int32
```cpp
/* 95270 */
enum ScriptApi::ScriptReportItemType : __int32
{
Error_3 = 0x0,
Warning_0 = 0x1,
_count_20 = 0x2,
};

```
#### ScriptLogType : __int32
```cpp
/* 99882 */
enum ScriptLogType : __int32
{
Error_4 = 0x0,
Warning_1 = 0x1,
Information = 0x2,
_count_21 = 0x3,
};

```
#### ScriptQueryComponent::ViewType : __int32
```cpp
/* 423827 */
enum ScriptQueryComponent::ViewType : __int32
{
Plain_0 = 0x0,
Spatial = 0x1,
};

```
#### SeaGrassType : __int32
```cpp
/* 183711 */
enum SeaGrassType : __int32
{
Default_15 = 0x0,
DoubleTop = 0x1,
DoubleBot = 0x2,
_count_36 = 0x3,
};

```
#### SeaPickleCount : __int32
```cpp
/* 232934 */
enum SeaPickleCount : __int32
{
One_Pickle = 0x0,
Two_Pickle = 0x1,
Three_Pickle = 0x2,
Four_Pickle = 0x3,
_count_52 = 0x4,
};

```
#### SemVersion::MatchType : __int32
```cpp
/* 5624 */
enum SemVersion::MatchType : __int32
{
Full = 0x0,
Partial = 0x1,
None_4 = 0x2,
};

```
#### SemVersion::ParseOption : __int32
```cpp
/* 5625 */
enum SemVersion::ParseOption : __int32
{
AllowAnyVersion = 0x0,
NoAnyVersion = 0x1,
};

```
#### SemanticConstraint : __int8
```cpp
/* 1541 */
enum SemanticConstraint : __int8
{
None_0 = 0x0,
RequiresCheatsEnabled = 0x1,
RequiresElevatedPermissions = 0x2,
RequiresHostPermissions = 0x4,
VALUE_MASK = 0x7,
};

```
#### SensibleDirections : __int32
```cpp
/* 288528 */
enum SensibleDirections : __int32
{
NORTH_1 = 0x0,
EAST_1 = 0x1,
SOUTH_1 = 0x2,
WEST_1 = 0x3,
};

```
#### ServerInstance::InstanceState : __int32
```cpp
/* 86445 */
enum ServerInstance::InstanceState : __int32
{
Running = 0x0,
Suspended = 0x1,
WaitingLeaveGame = 0x2,
Stopped = 0x3,
NotStarted_0 = 0x4,
};

```
#### ServerPlayer::NearbyActor::State : __int32
```cpp
/* 89357 */
enum ServerPlayer::NearbyActor::State : __int32
{
Unknown_34 = 0x0,
New_1 = 0x1,
Exist = 0x2,
DidExist = 0x3,
};

```
#### SetBlockCommand::SetBlockMode : __int32
```cpp
/* 426891 */
enum SetBlockCommand::SetBlockMode : __int32
{
Replace_2 = 0x0,
Destroy_1 = 0x1,
Keep_0 = 0x2,
};

```
#### SetTitlePacket::TitleType : __int32
```cpp
/* 80526 */
enum SetTitlePacket::TitleType : __int32
{
Clear = 0x0,
Reset_0 = 0x1,
Title = 0x2,
Subtitle = 0x3,
Actionbar = 0x4,
Times = 0x5,
TitleTextObject = 0x6,
SubtitleTextObject = 0x7,
ActionbarTextObject = 0x8,
};

```
#### ShowCreditsPacket::CreditsState : __int32
```cpp
/* 77413 */
enum ShowCreditsPacket::CreditsState : __int32
{
Start_0 = 0x0,
Finished_0 = 0x1,
};

```
#### Side : __int32
```cpp
/* 77457 */
enum Side : __int32
{
Left = 0x0,
Right = 0x1,
};

```
#### SignBlockActor::SignType : __int32
```cpp
/* 183753 */
enum SignBlockActor::SignType : __int32
{
Oak_2 = 0x0,
Spruce_2 = 0x1,
Birch_2 = 0x2,
Jungle_4 = 0x3,
Acacia_2 = 0x4,
DarkOak_2 = 0x5,
};

```
#### SimpleEventPacket::Subtype : __int32
```cpp
/* 77411 */
enum SimpleEventPacket::Subtype : __int32
{
UninitializedSubtype = 0x0,
EnableCommands = 0x1,
DisableCommands = 0x2,
UnlockWorldTemplateSettings = 0x3,
};

```
#### SkeletalHierarchyIndex : __int32
```cpp
/* 104582 */
enum SkeletalHierarchyIndex : __int32
{
Unknown_36 = 0xFFFFFFFF,
};

```
#### Skeleton::SkeletonType : __int32
```cpp
/* 114714 */
enum Skeleton::SkeletonType : __int32
{
DEFAULT = 0x0,
WITHER_0 = 0x1,
STRAY = 0x2,
};

```
#### SkullBlockActor::SkullType : __int32
```cpp
/* 170804 */
enum SkullBlockActor::SkullType : __int32
{
UNSET = 0xFFFFFFFF,
SKELETON = 0x0,
WITHER_1 = 0x1,
ZOMBIE = 0x2,
CHAR = 0x3,
CREEPER = 0x4,
DRAGON = 0x5,
COUNT_9 = 0x6,
};

```
#### SlabBlock::SlabType : __int32
```cpp
/* 460042 */
enum SlabBlock::SlabType : __int32
{
WoodSlab = 0x0,
StoneSlab = 0x1,
};

```
#### Slime::ClientEvent : __int8
```cpp
/* 171023 */
enum Slime::ClientEvent : __int8
{
None_44 = 0x0,
JustLanded = 0x1,
JustJumped = 0x2,
};

```
#### Social::ConnectionType : __int16
```cpp
/* 63699 */
enum Social::ConnectionType : __int16
{
Undefined_8 = 0xFFFF,
Local_3 = 0x0,
IPv4 = 0x1,
IPv6 = 0x2,
NAT = 0x3,
UPNP = 0x4,
UnknownIP = 0x5,
};

```
#### Social::Events::Measurement::AggregationType : __int32
```cpp
/* 43075 */
enum Social::Events::Measurement::AggregationType : __int32
{
Increment_0 = 0x0,
Sum = 0x1,
Min_0 = 0x2,
Max_0 = 0x3,
Average = 0x4,
};

```
#### Social::GamePublishSetting : __int32
```cpp
/* 5598 */
enum Social::GamePublishSetting : __int32
{
NoMultiPlay = 0x0,
InviteOnly = 0x1,
FriendsOnly = 0x2,
FriendsOfFriends = 0x3,
Public = 0x4,
};

```
#### Social::MultiplayerServiceIdentifier : __int32
```cpp
/* 45092 */
enum Social::MultiplayerServiceIdentifier : __int32
{
XboxLive = 0x0,
Nintendo = 0x1,
AdHoc = 0x2,
Playstation = 0x3,
EDU = 0x4,
Mock = 0x5,
Invalid_12 = 0xFFFFFFFF,
};

```
#### SoftEnumUpdateType : __int8
```cpp
/* 81090 */
enum SoftEnumUpdateType : __int8
{
Add_4 = 0x0,
Remove_4 = 0x1,
Replace = 0x2,
};

```
#### SolidityCheckType : __int8
```cpp
/* 123024 */
enum SolidityCheckType : __int8
{
CheckSolidBlocking = 0x0,
CheckCollisionShape = 0x1,
};

```
#### SpawnPositionType : __int32
```cpp
/* 77459 */
enum SpawnPositionType : __int32
{
PlayerRespawn = 0x0,
WorldSpawn = 0x1,
};

```
#### Spider::Type : __int32
```cpp
/* 171024 */
enum Spider::Type : __int32
{
Normal_9 = 0x0,
Cave = 0x1,
};

```
#### SpongeType : __int32
```cpp
/* 183728 */
enum SpongeType : __int32
{
Dry = 0x0,
Wet = 0x1,
_count_38 = 0x2,
};

```
#### StalkAndPounceOnTargetGoal::StalkAndPounceState : __int8
```cpp
/* 122839 */
enum StalkAndPounceOnTargetGoal::StalkAndPounceState : __int8
{
Stalking = 0x0,
Interested = 0x1,
Pouncing = 0x2,
Stuck = 0x3,
Done_1 = 0x4,
};

```
#### StalkThickness : __int32
```cpp
/* 227902 */
enum StalkThickness : __int32
{
Thin = 0x0,
Thick = 0x1,
_count_46 = 0x2,
};

```
#### StateTransitionEvent : __int32
```cpp
/* 452323 */
enum StateTransitionEvent : __int32
{
Entry = 0x0,
Exit = 0x1,
NumCategories = 0x2,
};

```
#### StoneBrickType : __int32
```cpp
/* 31916 */
enum StoneBrickType : __int32
{
Default_3 = 0x0,
Mossy = 0x1,
Cracked = 0x2,
Chiseled = 0x3,
Smooth = 0x4,
_count_6 = 0x5,
};

```
#### StoneSlabType : __int32
```cpp
/* 31472 */
enum StoneSlabType : __int32
{
SmoothStone = 0x0,
Sandstone = 0x1,
Wood = 0x2,
Cobblestone = 0x3,
Brick = 0x4,
StoneBrick = 0x5,
Quartz = 0x6,
NetherBrick = 0x7,
_count_5 = 0x8,
};

```
#### StoneSlabType2 : __int32
```cpp
/* 183653 */
enum StoneSlabType2 : __int32
{
RedSandstone = 0x0,
Purpur = 0x1,
PrismarineRough = 0x2,
PrismarineDark = 0x3,
PrismarineBrick = 0x4,
MossyCobblestone = 0x5,
SmoothSandstone = 0x6,
RedNetherBrick = 0x7,
_count_28 = 0x8,
};

```
#### StoneSlabType3 : __int32
```cpp
/* 183659 */
enum StoneSlabType3 : __int32
{
EndStoneBrick = 0x0,
SmoothRedSandstone = 0x1,
PolishedAndesite = 0x2,
Andesite = 0x3,
Diorite = 0x4,
PolishedDiorite = 0x5,
Granite = 0x6,
PolishedGranite = 0x7,
_count_29 = 0x8,
};

```
#### StoneSlabType4 : __int32
```cpp
/* 183647 */
enum StoneSlabType4 : __int32
{
MossyStoneBrick_0 = 0x0,
SmoothQuartz = 0x1,
Stone_1 = 0x2,
CutSandstone = 0x3,
CutRedSandstone = 0x4,
_count_27 = 0x5,
};

```
#### StoneType : __int32
```cpp
/* 183677 */
enum StoneType : __int32
{
Stone_2 = 0x0,
Granite_0 = 0x1,
GraniteSmooth = 0x2,
Diorite_0 = 0x3,
DioriteSmooth = 0x4,
Andesite_0 = 0x5,
AndesiteSmooth = 0x6,
_count_32 = 0x7,
};

```
#### StoragePermissionResult : __int8
```cpp
/* 6917 */
enum StoragePermissionResult : __int8
{
PermissionGranted = 0x0,
PermissionDenied = 0x1,
};

```
#### StorageVersion : __int32
```cpp
/* 5656 */
enum StorageVersion : __int32
{
Unknown_0 = 0x0,
OldV1 = 0x1,
OldV2 = 0x2,
OldV3 = 0x3,
LevelDB1 = 0x4,
LevelDBSubChunks = 0x5,
LevelDBSubChunkRawZip = 0x6,
LevelDBPaletted1 = 0x7,
LevelDBPalettedMultiBlockStorage = 0x8,
};

```
#### StrongholdPiece::SmallDoorType : __int32
```cpp
/* 31370 */
enum StrongholdPiece::SmallDoorType : __int32
{
OPENING = 0x0,
WOOD_DOOR = 0x1,
GRATES = 0x2,
IRON_DOOR = 0x3,
};

```
#### StructureBlockPaletteLoadResult : __int32
```cpp
/* 77452 */
enum StructureBlockPaletteLoadResult : __int32
{
Success_8 = 0x0,
MissingBlockPaletteField = 0x1,
ExpectedCompoundTagInBlockList = 0x2,
MissingBlockPositionDataField = 0x3,
ExpectedNumberAsStringWhenParsingBlockPositionData = 0x4,
ExpectedCompoundForBlockPositionData = 0x5,
ExpectedCompoundTagForBlockEntityData = 0x6,
ExpectedListTagForTickQueueData = 0x7,
ExpectedCompoundTagInTickQueueData = 0x8,
};

```
#### StructureBlockType : __int32
```cpp
/* 44548 */
enum StructureBlockType : __int32
{
Data = 0x0,
Save_0 = 0x1,
Load_0 = 0x2,
Corner = 0x3,
Invalid_10 = 0x4,
Export_0 = 0x5,
_count_15 = 0x6,
};

```
#### StructureFeatureType : __int8
```cpp
/* 37036 */
enum StructureFeatureType : __int8
{
Unknown_5 = 0x0,
EndCity = 0x1,
Fortress = 0x2,
Mineshaft = 0x3,
Monument = 0x4,
Stronghold = 0x5,
Temple = 0x6,
Village = 0x7,
WoodlandMansion = 0x8,
Shipwreck_0 = 0x9,
BuriedTreasure_0 = 0xA,
Ruins = 0xB,
PillagerOutpost_0 = 0xC,
_count_13 = 0xD,
};

```
#### StructureLoadResult : __int32
```cpp
/* 288522 */
enum StructureLoadResult : __int32
{
Success_13 = 0x0,
MissingFormatVersionField = 0x1,
InvalidFormatVersion = 0x2,
MissingSizeField = 0x3,
SizeIsNot3Elements = 0x4,
NegativeSize = 0x5,
MissingWorldOriginField = 0x6,
WorldOriginIsNot3Elements = 0x7,
MissingBlockIndicesField = 0x8,
BlockIndicesNot2Arrays = 0x9,
BlockIndicesIsNotAList = 0xA,
BlockIndicesListsNotSameSize = 0xB,
MismatchedSizeAndBlockIndicesSize = 0xC,
MissingPaletteField = 0xD,
FailedToLoadPalette = 0xE,
ExpectedCompoundTagInPaletteList = 0xF,
MissingEntitiesField = 0x10,
ExpectedCompoundTagInEntitiesList = 0x11,
};

```
#### StructurePieceType : __int32
```cpp
/* 31924 */
enum StructurePieceType : __int32
{
Unknown_3 = 0x0,
EndCityPiece = 0x45435450,
MineshaftRoom = 0x4D53524D,
MineshaftCorridor = 0x4D53434F,
MineshaftCrossing = 0x4D534352,
MineshaftStairs = 0x4D535354,
NetherFortressCrossing = 0x4E424352,
NetherFortressStartPiece = 0x4E425350,
NetherFortressStraight = 0x4E425354,
NetherFortressEndFiller = 0x4E424546,
NetherFortressRoomCrossing = 0x4E425243,
NetherFortressStairsRoom = 0x4E425352,
NetherFortressMonsterThrone = 0x4E424D54,
NetherCastleEntrance = 0x4E43454E,
NetherCastleStalkRoom = 0x4E435352,
NetherCastleSmallCorridor = 0x4E435343,
NetherCastleSmallCorridorCrossing = 0x4E434343,
NetherCastleSmallCorridorRightTurn = 0x4E435254,
NetherCastleSmallCorridorLeftTurn = 0x4E434C54,
NetherCastleCorridorStairs = 0x4E435354,
NetherCastleCorridorTBalcony = 0x4E434241,
OceanMonumentBuilding = 0x4F4D4255,
OceanMonumentEntryRoom = 0x4F4D4552,
OceanMonumentSimpleRoom = 0x4F4D5352,
OceanMonumentSimpleTopRoom = 0x4F4D5452,
OceanMonumentDoubleXRoom = 0x4F4D3258,
OceanMonumentDoubleYRoom = 0x4F4D3259,
OceanMonumentDoubleZRoom = 0x4F4D325A,
OceanMonumentDoubleXYRoom = 0x4F4D5859,
OceanMonumentDoubleYZRoom = 0x4F4D595A,
OceanMonumentCoreRoom = 0x4F4D4352,
OceanMonumentWingRoom = 0x4F4D5752,
OceanMonumentPenthouse = 0x4F4D5048,
DesertPyramid = 0x44535254,
Igloo = 0x49474C4F,
JunglePyramid = 0x4A4E474C,
WitchHut = 0x57544348,
StrongholdStairsDown = 0x53485344,
StrongholdStartPiece = 0x53485350,
StrongholdChestCorridor = 0x53484348,
StrongholdFillerCorridor = 0x53484649,
StrongholdFiveCrossing = 0x53483543,
StrongholdLeftTurn = 0x53484C54,
StrongholdRightTurn = 0x53485254,
StrongholdLibrary = 0x53484C49,
StrongholdPortalRoom = 0x53485052,
StrongholdPrisonHall = 0x53485048,
StrongholdRoomCrossing = 0x53485243,
StrongholdStraight = 0x53485354,
StrongholdStraightStairsDown = 0x53485353,
VillageWell = 0x56495745,
VillageStartPiece = 0x56495350,
VillageSimpleHouse = 0x56495348,
VillageSmallTemple = 0x56495354,
VillageBookHouse = 0x56494248,
VillageSmallHut = 0x56494854,
VillagePigHouse = 0x56495047,
VillageDoubleFarmland = 0x56494446,
VillageFarmland = 0x5649464C,
VillageSmithy = 0x5649534D,
VillageTwoRoomHouse = 0x56493252,
VillageLightPost = 0x56494C50,
VillageStraightRoad = 0x56495352,
WoodlandMansionPiece = 0x574C4D50,
Shipwreck = 0x53505752,
BuriedTreasure = 0x42525452,
OceanRuinsPiece = 0x4F435250,
};

```
#### StructureRedstoneSaveMode : __int8
```cpp
/* 44554 */
enum StructureRedstoneSaveMode : __int8
{
SavesToMemory = 0x0,
SavesToDisk = 0x1,
};

```
#### StructureTemplateRequestOperation : __int8
```cpp
/* 77451 */
enum StructureTemplateRequestOperation : __int8
{
None_26 = 0x0,
ExportFromSaveMode = 0x1,
ExportFromLoadMode = 0x2,
QuerySavedStructure = 0x3,
};

```
#### StructureTemplateResponseType : __int8
```cpp
/* 42308 */
enum StructureTemplateResponseType : __int8
{
};

```
#### StructureTemplateResponseType_0 : __int8
```cpp
/* 77453 */
enum StructureTemplateResponseType_0 : __int8
{
None_27 = 0x0,
Export_1 = 0x1,
Query_0 = 0x2,
};

```
#### StructureVoidType : __int32
```cpp
/* 230196 */
enum StructureVoidType : __int32
{
Void_0 = 0x0,
Air_1 = 0x1,
_count_49 = 0x2,
};

```
#### SubChunkBlockStorage::Type : __int8
```cpp
/* 253606 */
enum SubChunkBlockStorage::Type : __int8
{
Paletted1 = 0x1,
Paletted2 = 0x2,
Paletted3 = 0x3,
Paletted4 = 0x4,
Paletted5 = 0x5,
Paletted6 = 0x6,
Paletted8 = 0x8,
Paletted16 = 0x10,
};

```
#### SubChunkFormat : __int8
```cpp
/* 45384 */
enum SubChunkFormat : __int8
{
v17_0_0 = 0x0,
v1_3_0_0 = 0x1,
v17_0_badly_converted1 = 0x2,
v17_0_badly_converted2 = 0x3,
v17_0_badly_converted3 = 0x4,
v17_0_badly_converted4 = 0x5,
v17_0_badly_converted5 = 0x6,
v17_0_badly_converted6 = 0x7,
v1_3_0_2 = 0x8,
};

```
#### SubChunkInitMode : __int32
```cpp
/* 35032 */
enum SubChunkInitMode : __int32
{
All = 0x0,
AllButLast = 0x1,
None_12 = 0x2,
};

```
#### SubChunkRelighter::SubChunkToDoBitsClearMode : __int32
```cpp
/* 252864 */
enum SubChunkRelighter::SubChunkToDoBitsClearMode : __int32
{
AllSubChunkBorderBitsExceptTheOuterEdgeOfComputationBits = 0x0,
SetOuterEdgeOfComputationBits = 0x1,
};

```
#### SummonShape : __int32
```cpp
/* 88812 */
enum SummonShape : __int32
{
Circle = 0x0,
Line = 0x1,
Count_20 = 0x2,
};

```
#### SummonTarget : __int32
```cpp
/* 88813 */
enum SummonTarget : __int32
{
Self_1 = 0x0,
Target_0 = 0x1,
Count_21 = 0x2,
};

```
#### SuspiciousStewItem::SuspiciousStewType : __int32
```cpp
/* 183451 */
enum SuspiciousStewItem::SuspiciousStewType : __int32
{
Poppy = 0x0,
Cornflower = 0x1,
Tulip = 0x2,
AzureBluet = 0x3,
LilyOfTheValley = 0x4,
Dandelion = 0x5,
BlueOrchid = 0x6,
Allium = 0x7,
OxeyeDaisy = 0x8,
WitherRose = 0x9,
COUNT_12 = 0xA,
};

```
#### SweetBerryBushBlock::BerryStage : __int32
```cpp
/* 460045 */
enum SweetBerryBushBlock::BerryStage : __int32
{
Sapling = 0x0,
NoBerries = 0x1,
SomeBerries = 0x2,
FullBerries = 0x3,
};

```
#### Tag::Type : __int8
```cpp
/* 48666 */
enum Tag::Type : __int8
{
End_1 = 0x0,
Byte_0 = 0x1,
Short_0 = 0x2,
Int_2 = 0x3,
Int64_0 = 0x4,
Float_3 = 0x5,
Double = 0x6,
ByteArray = 0x7,
String_1 = 0x8,
List_0 = 0x9,
Compound = 0xA,
IntArray = 0xB,
};

```
#### TagCommand::Action : __int8
```cpp
/* 427273 */
enum TagCommand::Action : __int8
{
Add_8 = 0x0,
Remove_6 = 0x1,
List_3 = 0x2,
};

```
#### TallGrassType : __int32
```cpp
/* 31090 */
enum TallGrassType : __int32
{
Default_2 = 0x0,
Tall = 0x1,
Fern = 0x2,
Snow = 0x3,
_count_4 = 0x4,
};

```
#### TargetSelectionMethod : __int8
```cpp
/* 88785 */
enum TargetSelectionMethod : __int8
{
};

```
#### TargetSelectionMethod_0 : __int8
```cpp
/* 117056 */
enum TargetSelectionMethod_0 : __int8
{
Nearest = 0x0,
Random_2 = 0x1,
};

```
#### TaskGroupState : __int32
```cpp
/* 484303 */
enum TaskGroupState : __int32
{
Running_2 = 0x0,
Paused = 0x1,
Flush_0 = 0x2,
Sync_0 = 0x3,
};

```
#### TaskOptions : __int32
```cpp
/* 63712 */
enum TaskOptions : __int32
{
Default_7 = 0x0,
TaskProfiled = 0x1,
LinkPredecessor = 0x2,
};

```
#### TaskType : __int32
```cpp
/* 484374 */
enum TaskType : __int32
{
Flushable = 0x0,
};

```
#### TeleportCommand::FacingResult : __int32
```cpp
/* 427393 */
enum TeleportCommand::FacingResult : __int32
{
HaveFacing = 0x0,
NoFacing = 0x1,
Error_5 = 0x2,
};

```
#### TeleportCommand::TeleportAnalysis : __int32
```cpp
/* 427464 */
enum TeleportCommand::TeleportAnalysis : __int32
{
WontClip = 0x0,
WillClip = 0x1,
ChunksUnloaded = 0x2,
};

```
#### TemperatureCategory : __int32
```cpp
/* 191331 */
enum TemperatureCategory : __int32
{
Frozen_0 = 0x0,
};

```
#### TemplateLockState : __int8
```cpp
/* 5774 */
enum TemplateLockState : __int8
{
Undefined_1 = 0x0,
Enabled = 0x1,
Disabled = 0x2,
};

```
#### TestForBlocksCommand::Mode : __int32
```cpp
/* 427579 */
enum TestForBlocksCommand::Mode : __int32
{
All_9 = 0x0,
Masked_0 = 0x1,
};

```
#### TextPacketType : __int8
```cpp
/* 77445 */
enum TextPacketType : __int8
{
Raw_0 = 0x0,
Chat = 0x1,
Translate = 0x2,
Popup = 0x3,
JukeboxPopup = 0x4,
Tip = 0x5,
SystemMessage = 0x6,
Whisper = 0x7,
Announcement = 0x8,
TextObject = 0x9,
};

```
#### TickingAreaCommand::AddAreaType : __int32
```cpp
/* 427758 */
enum TickingAreaCommand::AddAreaType : __int32
{
Bounds = 0x0,
Circle_0 = 0x1,
};

```
#### TickingAreaCommand::Mode : __int32
```cpp
/* 427709 */
enum TickingAreaCommand::Mode : __int32
{
Add_9 = 0x0,
Remove_7 = 0x1,
RemoveAll = 0x2,
List_4 = 0x3,
};

```
#### TickingAreaCommand::TargetDimensions : __int32
```cpp
/* 427807 */
enum TickingAreaCommand::TargetDimensions : __int32
{
CurrentDimension = 0x0,
AllDimensions = 0x1,
};

```
#### TickingQueueType : __int8
```cpp
/* 36326 */
enum TickingQueueType : __int8
{
Internal_0 = 0x0,
Random_0 = 0x1,
};

```
#### TimeCommand::Mode : __int32
```cpp
/* 427946 */
enum TimeCommand::Mode : __int32
{
Set_2 = 0x0,
Add_10 = 0x1,
Query_1 = 0x2,
};

```
#### TimeCommand::Query : __int32
```cpp
/* 427995 */
enum TimeCommand::Query : __int32
{
DayTime = 0x0,
GameTime = 0x1,
Day = 0x2,
};

```
#### TimeCommand::TimeSpec : __int32
```cpp
/* 428044 */
enum TimeCommand::TimeSpec : __int32
{
Sunrise = 0x0,
Day_0 = 0x1,
Noon = 0x2,
Sunset = 0x3,
Night = 0x4,
Midnight = 0x5,
Unspecified = 0x6,
};

```
#### TitleCommand::Mode : __int32
```cpp
/* 428171 */
enum TitleCommand::Mode : __int32
{
Clear_1 = 0x0,
Reset_2 = 0x1,
Title_0 = 0x2,
Subtitle_0 = 0x3,
ActionBar = 0x4,
Times_0 = 0x5,
};

```
#### TitleRawCommand::Mode : __int32
```cpp
/* 428299 */
enum TitleRawCommand::Mode : __int32
{
Clear_2 = 0x0,
Reset_3 = 0x1,
Title_1 = 0x2,
Subtitle_1 = 0x3,
ActionBar_0 = 0x4,
Times_1 = 0x5,
};

```
#### Token::Type : __int32
```cpp
/* 117551 */
enum Token::Type : __int32
{
String_5 = 0x0,
Number = 0x1,
Bool_2 = 0x2,
};

```
#### Token::tokenize::$663C034D90AC1D8D8F9A30B68A82B4D9 : __int32
```cpp
/* 430694 */
enum Token::tokenize::$663C034D90AC1D8D8F9A30B68A82B4D9 : __int32
{
S_NONE = 0x0,
S_TOKEN = 0x1,
S_QUOTES = 0x2,
};

```
#### TorchFacing : __int32
```cpp
/* 227584 */
enum TorchFacing : __int32
{
Unknown_46 = 0x0,
West_0 = 0x1,
East_0 = 0x2,
North_0 = 0x3,
South_0 = 0x4,
Top_0 = 0x5,
_count_44 = 0x6,
};

```
#### TrackerType : __int32
```cpp
/* 5581 */
enum TrackerType : __int32
{
ClientPackets = 0x0,
ServerPackets = 0x1,
Xbox = 0x2,
HttpMisc = 0x3,
Count_0 = 0x4,
};

```
#### TransactionStatus : __int32
```cpp
/* 44610 */
enum TransactionStatus : __int32
{
};

```
#### TransferState : __int32
```cpp
/* 44669 */
enum TransferState : __int32
{
};

```
#### TrapDoorBlock::TrapDoorDir : __int8
```cpp
/* 460049 */
enum TrapDoorBlock::TrapDoorDir : __int8
{
DIR_EAST = 0x0,
DIR_WEST = 0x1,
DIR_SOUTH = 0x2,
DIR_NORTH = 0x3,
};

```
#### TrustedSkinFlag : __int8
```cpp
/* 74259 */
enum TrustedSkinFlag : __int8
{
Unset_0 = 0x0,
False = 0x1,
True = 0x2,
};

```
#### UIPackErrorType : __int32
```cpp
/* 85849 */
enum UIPackErrorType : __int32
{
None_35 = 0x0,
InvalidChildNames = 0x1,
ParseError_0 = 0x2,
MissingControl = 0x3,
MissingControlTarget = 0x4,
MissingArrayName = 0x5,
MissingCondition = 0x6,
MissingValue = 0x7,
MissingOperation = 0x8,
InvalidOperationName = 0x9,
};

```
#### UIProfile : __int32
```cpp
/* 480116 */
enum UIProfile : __int32
{
Classic_0 = 0x0,
Pocket_0 = 0x1,
Count_30 = 0x2,
};

```
#### UIScalingRules : __int32
```cpp
/* 6931 */
enum UIScalingRules : __int32
{
Desktop = 0x0,
PocketApple = 0x1,
PocketAndroid = 0x2,
PocketWindows = 0x3,
Console = 0x4,
HandheldConsole = 0x5,
};

```
#### UploadError : __int32
```cpp
/* 101407 */
enum UploadError : __int32
{
None_36 = 0x0,
ForbiddenContent = 0x1,
Unknown_35 = 0x2,
};

```
#### UploadState : __int32
```cpp
/* 101406 */
enum UploadState : __int32
{
Uninitialized_1 = 0x0,
Initializing = 0x1,
Progress = 0x2,
Exporting = 0x3,
Done_0 = 0x4,
Failed_6 = 0x5,
};

```
#### UpnpState : __int32
```cpp
/* 62643 */
enum UpnpState : __int32
{
Startup = 0x0,
UpnpRequested = 0x1,
UpnpStarted = 0x2,
UpnpSucceeded = 0x3,
UpnpFailed = 0x4,
Invalid_13 = 0x5,
};

```
#### UseAnimation : __int8
```cpp
/* 33513 */
enum UseAnimation : __int8
{
None_10 = 0x0,
Eat = 0x1,
Drink = 0x2,
Block_0 = 0x3,
Bow = 0x4,
Camera_0 = 0x5,
Spear = 0x6,
GlowStick = 0x7,
Sparkler = 0x8,
Crossbow = 0x9,
};

```
#### Util::NumberConversionResult : __int32
```cpp
/* 93422 */
enum Util::NumberConversionResult : __int32
{
Succeed = 0x0,
Invalid_20 = 0x1,
TooSmall = 0x2,
TooLarge = 0x3,
Count_22 = 0x4,
};

```
#### Util::removeAllColorCodes::RemoveAllColorCodesState : __int32
```cpp
/* 103850 */
enum Util::removeAllColorCodes::RemoveAllColorCodesState : __int32
{
Output = 0x0,
SawCodeByte1 = 0x1,
SawCodeByte2 = 0x2,
};

```
#### VRControllerType : __int64
```cpp
/* 6884 */
enum VRControllerType : __int64
{
Standard_0 = 0x0,
SingleTriggerGearVR = 0x1,
GearVR = 0x2,
MotionController = 0x3,
_count = 0x4,
};

```
#### VanillaBiomeTypes : __int32
```cpp
/* 42752 */
enum VanillaBiomeTypes : __int32
{
};

```
#### VanillaBiomeTypes_0 : __int32
```cpp
/* 115604 */
enum VanillaBiomeTypes_0 : __int32
{
Beach = 0x0,
Desert = 0x1,
ExtremeHills = 0x2,
Flat_0 = 0x3,
Forest_1 = 0x4,
Hell = 0x5,
Ice_1 = 0x6,
Jungle_3 = 0x7,
Mesa = 0x8,
MushroomIsland = 0x9,
Ocean_0 = 0xA,
Plain = 0xB,
River = 0xC,
Savanna_0 = 0xD,
StoneBeach = 0xE,
Swamp_0 = 0xF,
Taiga_0 = 0x10,
TheEnd_0 = 0x11,
DataDriven = 0x12,
};

```
#### VideoStreamConnectPacket::Action : __int8
```cpp
/* 81105 */
enum VideoStreamConnectPacket::Action : __int8
{
NONE_6 = 0x0,
CLOSE = 0x1,
};

```
#### WSConnectionResult : __int8
```cpp
/* 6406 */
enum WSConnectionResult : __int8
{
Failed = 0x0,
InvalidUri = 0x1,
ConnectionInProgress = 0x2,
Success_1 = 0x3,
};

```
#### WallBlockType : __int32
```cpp
/* 183770 */
enum WallBlockType : __int32
{
Cobblestone_1 = 0x0,
MossyCobblestone_0 = 0x1,
Granite_1 = 0x2,
Diorite_1 = 0x3,
Andesite_1 = 0x4,
Sandstone_0 = 0x5,
Brick_0 = 0x6,
StoneBrick_1 = 0x7,
MossyStoneBrick_1 = 0x8,
NetherBrick_0 = 0x9,
EndBrick = 0xA,
Prismarine = 0xB,
RedSandstone_0 = 0xC,
RedNetherBrick_0 = 0xD,
_count_40 = 0xE,
};

```
#### WeakStorageEntity::EmptyInit : __int32
```cpp
/* 13156 */
enum WeakStorageEntity::EmptyInit : __int32
{
NoValue = 0x0,
};

```
#### WeakStorageEntity::VariadicInit : __int32
```cpp
/* 13157 */
enum WeakStorageEntity::VariadicInit : __int32
{
NonAmbiguous = 0x0,
};

```
#### WeakStorageFeature::EmptyInit : __int32
```cpp
/* 31085 */
enum WeakStorageFeature::EmptyInit : __int32
{
NoValue_2 = 0x0,
};

```
#### WeakStorageFeature::VariadicInit : __int32
```cpp
/* 31086 */
enum WeakStorageFeature::VariadicInit : __int32
{
NonAmbiguous_2 = 0x0,
};

```
#### WeakStorageSharePtr<EntityRegistry>::EmptyInit : __int32
```cpp
/* 13162 */
enum WeakStorageSharePtr<EntityRegistry>::EmptyInit : __int32
{
};

```
#### WeakStorageSharePtr<EntityRegistry>::VariadicInit : __int32
```cpp
/* 13163 */
enum WeakStorageSharePtr<EntityRegistry>::VariadicInit : __int32
{
};

```
#### WeakStorageSharePtr<PerlinSimplexNoise>::EmptyInit : __int32
```cpp
/* 191529 */
enum WeakStorageSharePtr<PerlinSimplexNoise>::EmptyInit : __int32
{
};

```
#### WeakStorageSharePtr<PerlinSimplexNoise>::VariadicInit : __int32
```cpp
/* 191530 */
enum WeakStorageSharePtr<PerlinSimplexNoise>::VariadicInit : __int32
{
};

```
#### WeatherCommand::WeatherRequest : __int32
```cpp
/* 428598 */
enum WeatherCommand::WeatherRequest : __int32
{
Set_3 = 0x0,
Query_2 = 0x1,
};

```
#### WeatherCommand::WeatherType : __int32
```cpp
/* 428549 */
enum WeatherCommand::WeatherType : __int32
{
Clear_3 = 0x0,
Rain = 0x1,
Thunder_0 = 0x2,
};

```
#### WeirdoDirection : __int32
```cpp
/* 31931 */
enum WeirdoDirection : __int32
{
East = 0x0,
West = 0x1,
South = 0x2,
North = 0x3,
};

```
#### WhitelistCommand::Action : __int32
```cpp
/* 6683 */
enum WhitelistCommand::Action : __int32
{
List = 0x0,
On = 0x1,
Off = 0x2,
AddName = 0x3,
RemoveName = 0x4,
Reload = 0x5,
};

```
#### WoodType : __int32
```cpp
/* 35877 */
enum WoodType : __int32
{
Oak_1 = 0x0,
Spruce_1 = 0x1,
Birch_1 = 0x2,
Jungle_2 = 0x3,
Acacia = 0x4,
DarkOak = 0x5,
_count_12 = 0x6,
};

```
#### WoodlandMansionPieces::WoodlandMansionPiece::_addChest::SensibleDirections : __int32
```cpp
/* 288547 */
enum WoodlandMansionPieces::WoodlandMansionPiece::_addChest::SensibleDirections : __int32
{
NORTH_2 = 0x0,
EAST_2 = 0x1,
SOUTH_2 = 0x2,
WEST_2 = 0x3,
};

```
#### WorldConversionError : __int32
```cpp
/* 45327 */
enum WorldConversionError : __int32
{
};

```
#### WorldPacksHistoryFile::ParseResult : __int32
```cpp
/* 85907 */
enum WorldPacksHistoryFile::ParseResult : __int32
{
InvalidArrayOfPacks = 0x0,
InvalidPack = 0x1,
Success_9 = 0x2,
};

```
#### XXH_alignment : __int32
```cpp
/* 424367 */
enum XXH_alignment : __int32
{
XXH_aligned = 0x0,
XXH_unaligned = 0x1,
};

```
#### XXH_endianess : __int32
```cpp
/* 424366 */
enum XXH_endianess : __int32
{
XXH_bigEndian = 0x0,
XXH_littleEndian = 0x1,
};

```
#### Zombie::ZombieType : __int32
```cpp
/* 171000 */
enum Zombie::ZombieType : __int32
{
DEFAULT_1 = 0x0,
VILLAGER = 0x1,
HUSK = 0x2,
PIGZOMBIE = 0x3,
DROWNED = 0x4,
};

```
#### __ptrace_request : __int32
```cpp
/* 486223 */
enum __ptrace_request : __int32
{
PTRACE_TRACEME = 0x0,
PTRACE_PEEKTEXT = 0x1,
PTRACE_PEEKDATA = 0x2,
PTRACE_PEEKUSER = 0x3,
PTRACE_POKETEXT = 0x4,
PTRACE_POKEDATA = 0x5,
PTRACE_POKEUSER = 0x6,
PTRACE_CONT = 0x7,
PTRACE_KILL = 0x8,
PTRACE_SINGLESTEP = 0x9,
PTRACE_GETREGS = 0xC,
PTRACE_SETREGS = 0xD,
PTRACE_GETFPREGS = 0xE,
PTRACE_SETFPREGS = 0xF,
PTRACE_ATTACH = 0x10,
PTRACE_DETACH = 0x11,
PTRACE_GETFPXREGS = 0x12,
PTRACE_SETFPXREGS = 0x13,
PTRACE_SYSCALL = 0x18,
PTRACE_GET_THREAD_AREA = 0x19,
PTRACE_SET_THREAD_AREA = 0x1A,
PTRACE_ARCH_PRCTL = 0x1E,
PTRACE_SYSEMU = 0x1F,
PTRACE_SYSEMU_SINGLESTEP = 0x20,
PTRACE_SINGLEBLOCK = 0x21,
PTRACE_SETOPTIONS = 0x4200,
PTRACE_GETEVENTMSG = 0x4201,
PTRACE_GETSIGINFO = 0x4202,
PTRACE_SETSIGINFO = 0x4203,
PTRACE_GETREGSET = 0x4204,
PTRACE_SETREGSET = 0x4205,
PTRACE_SEIZE = 0x4206,
PTRACE_INTERRUPT = 0x4207,
PTRACE_LISTEN = 0x4208,
PTRACE_PEEKSIGINFO = 0x4209,
PTRACE_GETSIGMASK = 0x420A,
PTRACE_SETSIGMASK = 0x420B,
PTRACE_SECCOMP_GET_FILTER = 0x420C,
};

```
#### __socket_type : __int32
```cpp
/* 294340 */
enum __socket_type : __int32
{
SOCK_STREAM = 0x1,
SOCK_DGRAM = 0x2,
SOCK_RAW = 0x3,
SOCK_RDM = 0x4,
SOCK_SEQPACKET = 0x5,
SOCK_DCCP = 0x6,
SOCK_PACKET = 0xA,
SOCK_CLOEXEC = 0x80000,
SOCK_NONBLOCK = 0x800,
};

```
#### `anonymous namespace'::PriorityBucket : __int32
```cpp
/* 258294 */
enum `anonymous namespace'::PriorityBucket : __int32
{
BeforeUndergroundPass = 0x0,
UndergroundPass = 0x1,
BeforeSurfacePass = 0x2,
SurfacePass = 0x3,
BeforeSkyPass = 0x4,
SkyPass = 0x5,
FinalPass = 0x6,
_Count_6 = 0x7,
};

```
#### cg::ColorSpace : __int8
```cpp
/* 457059 */
enum cg::ColorSpace : __int8
{
Unknown_47 = 0x0,
sRGB_0 = 0x1,
Linear_0 = 0x2,
};

```
#### com::mojang::clacks::protocol::CheatsSetting : __int32
```cpp
/* 7924 */
enum com::mojang::clacks::protocol::CheatsSetting : __int32
{
ALLOW = 0x0,
DISALLOW = 0x1,
CheatsSetting_INT_MIN_SENTINEL_DO_NOT_USE_ = 0x80000000,
CheatsSetting_INT_MAX_SENTINEL_DO_NOT_USE_ = 0x7FFFFFFF,
};

```
#### com::mojang::clacks::protocol::DifficultySetting : __int32
```cpp
/* 7923 */
enum com::mojang::clacks::protocol::DifficultySetting : __int32
{
PEACEFUL = 0x0,
EASY = 0x1,
NORMAL = 0x2,
HARD = 0x3,
DifficultySetting_INT_MIN_SENTINEL_DO_NOT_USE_ = 0x80000000,
DifficultySetting_INT_MAX_SENTINEL_DO_NOT_USE_ = 0x7FFFFFFF,
};

```
#### com::mojang::clacks::protocol::MetricReport::MetricCase : __int32
```cpp
/* 8627 */
enum com::mojang::clacks::protocol::MetricReport::MetricCase : __int32
{
kBandwith = 0x1,
kLatency = 0x2,
kTickTime = 0x3,
METRIC_NOT_SET = 0x0,
};

```
#### com::mojang::clacks::protocol::PlayerType : __int32
```cpp
/* 7921 */
enum com::mojang::clacks::protocol::PlayerType : __int32
{
PRIMARY_PLAYER = 0x0,
SPLIT_SCREEN_PLAYER = 0x1,
PlayerType_INT_MIN_SENTINEL_DO_NOT_USE_ = 0x80000000,
PlayerType_INT_MAX_SENTINEL_DO_NOT_USE_ = 0x7FFFFFFF,
};

```
#### com::mojang::clacks::protocol::SaveState : __int32
```cpp
/* 7402 */
enum com::mojang::clacks::protocol::SaveState : __int32
{
IDLE = 0x0,
SAVING = 0x1,
COMPLETE = 0x2,
SaveState_INT_MIN_SENTINEL_DO_NOT_USE_ = 0x80000000,
SaveState_INT_MAX_SENTINEL_DO_NOT_USE_ = 0x7FFFFFFF,
};

```
#### com::mojang::clacks::protocol::Settings::SettingsCase : __int32
```cpp
/* 7922 */
enum com::mojang::clacks::protocol::Settings::SettingsCase : __int32
{
kDifficultySetting = 0x1,
kCheatsSetting = 0x2,
SETTINGS_NOT_SET = 0x0,
};

```
#### glm::ctor : __int32
```cpp
/* 5600 */
enum glm::ctor : __int32
{
uninitialize = 0x0,
};

```
#### glm::precision : __int32
```cpp
/* 5599 */
enum glm::precision : __int32
{
packed_highp = 0x0,
packed_mediump = 0x1,
packed_lowp = 0x2,
aligned_highp = 0x3,
aligned_mediump = 0x4,
aligned_lowp = 0x5,
aligned = 0x3,
highp = 0x0,
mediump = 0x1,
lowp = 0x2,
packed = 0x0,
defaultp = 0x0,
};

```
#### google_breakpad::MinidumpDescriptor::DumpMode : __int32
```cpp
/* 294187 */
enum google_breakpad::MinidumpDescriptor::DumpMode : __int32
{
kUninitialized = 0x0,
kWriteMinidumpToFile = 0x1,
kWriteMinidumpToFd = 0x2,
kWriteMicrodumpToConsole = 0x3,
};

```
#### google_breakpad::TypedMDRVA<MDRawContextAMD64>::AllocationState : __int32
```cpp
/* 485791 */
enum google_breakpad::TypedMDRVA<MDRawContextAMD64>::AllocationState : __int32
{
UNALLOCATED_2 = 0x0,
SINGLE_OBJECT_2 = 0x1,
ARRAY_2 = 0x2,
SINGLE_OBJECT_WITH_ARRAY_2 = 0x3,
};

```
#### google_breakpad::TypedMDRVA<MDRawDebug64>::AllocationState : __int32
```cpp
/* 485807 */
enum google_breakpad::TypedMDRVA<MDRawDebug64>::AllocationState : __int32
{
UNALLOCATED_6 = 0x0,
SINGLE_OBJECT_6 = 0x1,
ARRAY_6 = 0x2,
SINGLE_OBJECT_WITH_ARRAY_6 = 0x3,
};

```
#### google_breakpad::TypedMDRVA<MDRawDirectory>::AllocationState : __int32
```cpp
/* 485779 */
enum google_breakpad::TypedMDRVA<MDRawDirectory>::AllocationState : __int32
{
UNALLOCATED = 0x0,
SINGLE_OBJECT = 0x1,
ARRAY = 0x2,
SINGLE_OBJECT_WITH_ARRAY = 0x3,
};

```
#### google_breakpad::TypedMDRVA<MDRawExceptionStream>::AllocationState : __int32
```cpp
/* 485795 */
enum google_breakpad::TypedMDRVA<MDRawExceptionStream>::AllocationState : __int32
{
UNALLOCATED_3 = 0x0,
SINGLE_OBJECT_3 = 0x1,
ARRAY_3 = 0x2,
SINGLE_OBJECT_WITH_ARRAY_3 = 0x3,
};

```
#### google_breakpad::TypedMDRVA<MDRawHeader>::AllocationState : __int32
```cpp
/* 485782 */
enum google_breakpad::TypedMDRVA<MDRawHeader>::AllocationState : __int32
{
UNALLOCATED_0 = 0x0,
SINGLE_OBJECT_0 = 0x1,
ARRAY_0 = 0x2,
SINGLE_OBJECT_WITH_ARRAY_0 = 0x3,
};

```
#### google_breakpad::TypedMDRVA<MDRawLinkMap64>::AllocationState : __int32
```cpp
/* 485804 */
enum google_breakpad::TypedMDRVA<MDRawLinkMap64>::AllocationState : __int32
{
UNALLOCATED_5 = 0x0,
SINGLE_OBJECT_5 = 0x1,
ARRAY_5 = 0x2,
SINGLE_OBJECT_WITH_ARRAY_5 = 0x3,
};

```
#### google_breakpad::TypedMDRVA<MDRawSystemInfo>::AllocationState : __int32
```cpp
/* 485802 */
enum google_breakpad::TypedMDRVA<MDRawSystemInfo>::AllocationState : __int32
{
UNALLOCATED_4 = 0x0,
SINGLE_OBJECT_4 = 0x1,
ARRAY_4 = 0x2,
SINGLE_OBJECT_WITH_ARRAY_4 = 0x3,
};

```
#### google_breakpad::TypedMDRVA<MDString>::AllocationState : __int32
```cpp
/* 486268 */
enum google_breakpad::TypedMDRVA<MDString>::AllocationState : __int32
{
UNALLOCATED_7 = 0x0,
SINGLE_OBJECT_7 = 0x1,
ARRAY_7 = 0x2,
SINGLE_OBJECT_WITH_ARRAY_7 = 0x3,
};

```
#### google_breakpad::TypedMDRVA<unsigned int>::AllocationState : __int32
```cpp
/* 485784 */
enum google_breakpad::TypedMDRVA<unsigned int>::AllocationState : __int32
{
UNALLOCATED_1 = 0x0,
SINGLE_OBJECT_1 = 0x1,
ARRAY_1 = 0x2,
SINGLE_OBJECT_WITH_ARRAY_1 = 0x3,
};

```
#### gpr_clock_type : __int32
```cpp
/* 7946 */
enum gpr_clock_type : __int32
{
GPR_CLOCK_MONOTONIC = 0x0,
GPR_CLOCK_REALTIME = 0x1,
GPR_CLOCK_PRECISE = 0x2,
GPR_TIMESPAN = 0x3,
};

```
#### grpc_byte_buffer_type : __int32
```cpp
/* 8926 */
enum grpc_byte_buffer_type : __int32
{
GRPC_BB_RAW = 0x0,
};

```
#### grpc_call_error : __int32
```cpp
/* 9432 */
enum grpc_call_error : __int32
{
GRPC_CALL_OK = 0x0,
GRPC_CALL_ERROR = 0x1,
GRPC_CALL_ERROR_NOT_ON_SERVER = 0x2,
GRPC_CALL_ERROR_NOT_ON_CLIENT = 0x3,
GRPC_CALL_ERROR_ALREADY_ACCEPTED = 0x4,
GRPC_CALL_ERROR_ALREADY_INVOKED = 0x5,
GRPC_CALL_ERROR_NOT_INVOKED = 0x6,
GRPC_CALL_ERROR_ALREADY_FINISHED = 0x7,
GRPC_CALL_ERROR_TOO_MANY_OPERATIONS = 0x8,
GRPC_CALL_ERROR_INVALID_FLAGS = 0x9,
GRPC_CALL_ERROR_INVALID_METADATA = 0xA,
GRPC_CALL_ERROR_INVALID_MESSAGE = 0xB,
GRPC_CALL_ERROR_NOT_SERVER_COMPLETION_QUEUE = 0xC,
GRPC_CALL_ERROR_BATCH_TOO_BIG = 0xD,
GRPC_CALL_ERROR_PAYLOAD_TYPE_MISMATCH = 0xE,
GRPC_CALL_ERROR_COMPLETION_QUEUE_SHUTDOWN = 0xF,
};

```
#### grpc_completion_type : __int32
```cpp
/* 9433 */
enum grpc_completion_type : __int32
{
GRPC_QUEUE_SHUTDOWN = 0x0,
GRPC_QUEUE_TIMEOUT = 0x1,
GRPC_OP_COMPLETE = 0x2,
};

```
#### grpc_compression_algorithm : __int32
```cpp
/* 7960 */
enum grpc_compression_algorithm : __int32
{
GRPC_COMPRESS_NONE = 0x0,
GRPC_COMPRESS_DEFLATE = 0x1,
GRPC_COMPRESS_GZIP = 0x2,
GRPC_COMPRESS_STREAM_GZIP = 0x3,
GRPC_COMPRESS_ALGORITHMS_COUNT = 0x4,
};

```
#### grpc_compression_level : __int32
```cpp
/* 7959 */
enum grpc_compression_level : __int32
{
GRPC_COMPRESS_LEVEL_NONE = 0x0,
GRPC_COMPRESS_LEVEL_LOW = 0x1,
GRPC_COMPRESS_LEVEL_MED = 0x2,
GRPC_COMPRESS_LEVEL_HIGH = 0x3,
GRPC_COMPRESS_LEVEL_COUNT = 0x4,
};

```
#### grpc_connectivity_state : __int32
```cpp
/* 9418 */
enum grpc_connectivity_state : __int32
{
GRPC_CHANNEL_IDLE = 0x0,
GRPC_CHANNEL_CONNECTING = 0x1,
GRPC_CHANNEL_READY = 0x2,
GRPC_CHANNEL_TRANSIENT_FAILURE = 0x3,
GRPC_CHANNEL_SHUTDOWN = 0x4,
};

```
#### grpc_cq_completion_type : __int32
```cpp
/* 9404 */
enum grpc_cq_completion_type : __int32
{
GRPC_CQ_NEXT = 0x0,
GRPC_CQ_PLUCK = 0x1,
GRPC_CQ_CALLBACK = 0x2,
};

```
#### grpc_cq_polling_type : __int32
```cpp
/* 9405 */
enum grpc_cq_polling_type : __int32
{
GRPC_CQ_DEFAULT_POLLING = 0x0,
GRPC_CQ_NON_LISTENING = 0x1,
GRPC_CQ_NON_POLLING = 0x2,
};

```
#### grpc_op_type : __int32
```cpp
/* 9421 */
enum grpc_op_type : __int32
{
GRPC_OP_SEND_INITIAL_METADATA = 0x0,
GRPC_OP_SEND_MESSAGE = 0x1,
GRPC_OP_SEND_CLOSE_FROM_CLIENT = 0x2,
GRPC_OP_SEND_STATUS_FROM_SERVER = 0x3,
GRPC_OP_RECV_INITIAL_METADATA = 0x4,
GRPC_OP_RECV_MESSAGE = 0x5,
GRPC_OP_RECV_STATUS_ON_CLIENT = 0x6,
GRPC_OP_RECV_CLOSE_ON_SERVER = 0x7,
};

```
#### grpc_status_code : __int32
```cpp
/* 8936 */
enum grpc_status_code : __int32
{
GRPC_STATUS_OK = 0x0,
GRPC_STATUS_CANCELLED = 0x1,
GRPC_STATUS_UNKNOWN = 0x2,
GRPC_STATUS_INVALID_ARGUMENT = 0x3,
GRPC_STATUS_DEADLINE_EXCEEDED = 0x4,
GRPC_STATUS_NOT_FOUND = 0x5,
GRPC_STATUS_ALREADY_EXISTS = 0x6,
GRPC_STATUS_PERMISSION_DENIED = 0x7,
GRPC_STATUS_UNAUTHENTICATED = 0x10,
GRPC_STATUS_RESOURCE_EXHAUSTED = 0x8,
GRPC_STATUS_FAILED_PRECONDITION = 0x9,
GRPC_STATUS_ABORTED = 0xA,
GRPC_STATUS_OUT_OF_RANGE = 0xB,
GRPC_STATUS_UNIMPLEMENTED = 0xC,
GRPC_STATUS_INTERNAL = 0xD,
GRPC_STATUS_UNAVAILABLE = 0xE,
GRPC_STATUS_DATA_LOSS = 0xF,
GRPC_STATUS__DO_NOT_USE = 0xFFFFFFFF,
};

```
#### mce::ImageFormat : __int32
```cpp
/* 74241 */
enum mce::ImageFormat : __int32
{
Unknown_27 = 0x0,
RGB8Unorm = 0x1,
RGBA8Unorm = 0x2,
};

```
#### mce::ImageUsage : __int8
```cpp
/* 74242 */
enum mce::ImageUsage : __int8
{
};

```
#### mce::ImageUsage_0 : __int8
```cpp
/* 173108 */
enum mce::ImageUsage_0 : __int8
{
Unknown_41 = 0x0,
sRGB = 0x1,
Data_0 = 0x2,
};

```
#### mce::TextureFormat : __int32
```cpp
/* 457061 */
enum mce::TextureFormat : __int32
{
};

```
#### persona::AnimatedTextureType : __int32
```cpp
/* 74258 */
enum persona::AnimatedTextureType : __int32
{
None_24 = 0x0,
Face = 0x1,
Body32x32 = 0x2,
Body128x128 = 0x3,
};

```
#### persona::PersonaError : __int32
```cpp
/* 171755 */
enum persona::PersonaError : __int32
{
NoError_0 = 0x0,
ItemSelection = 0x1,
InvalidPersona = 0x3,
LoadingAppearanceTimeOut = 0x4,
};

```
#### persona::PieceSubType : __int32
```cpp
/* 171595 */
enum persona::PieceSubType : __int32
{
Unknown_40 = 0x0,
None_45 = 0x1,
Cape = 0x2,
Complexion = 0x3,
Count_23 = 0x4,
};

```
#### persona::PieceType : __int32
```cpp
/* 73850 */
enum persona::PieceType : __int32
{
Unknown_26 = 0x0,
Skeleton_0 = 0x1,
Body_0 = 0x2,
Skin = 0x3,
Bottom = 0x4,
Feet_1 = 0x5,
Dress = 0x6,
Top = 0x7,
High_Pants = 0x8,
Hands_0 = 0x9,
Outerwear = 0xA,
Back = 0xB,
FacialHair = 0xC,
Mouth_0 = 0xD,
Eyes_0 = 0xE,
Hair = 0xF,
FaceAccessory = 0x10,
Head_1 = 0x11,
Legs_0 = 0x12,
LeftLeg = 0x13,
RightLeg = 0x14,
Arms = 0x15,
LeftArm = 0x16,
RightArm = 0x17,
Capes = 0x18,
ClassicSkin = 0x19,
Count_12 = 0x1A,
};

```
#### persona::ProfileType : __int32
```cpp
/* 171437 */
enum persona::ProfileType : __int32
{
Legacy_0 = 0x0,
Persona1 = 0x1,
Persona2 = 0x2,
Persona3 = 0x3,
Persona4 = 0x4,
Persona5 = 0x5,
COUNT_10 = 0x6,
NOT_FOUND_0 = 0x7,
CUSTOM_0 = 0x8,
};

```
#### persona::Rarity : __int8
```cpp
/* 171675 */
enum persona::Rarity : __int8
{
None_46 = 0x0,
Common = 0x1,
Uncommon = 0x2,
Rare = 0x3,
Epic = 0x4,
Legendary = 0x5,
};

```
#### r_debug::$779A3ED0FCC279D8F3DE0A4A7B5F9A6A : __int32
```cpp
/* 486215 */
enum r_debug::$779A3ED0FCC279D8F3DE0A4A7B5F9A6A : __int32
{
RT_CONSISTENT = 0x0,
RT_ADD = 0x1,
RT_DELETE = 0x2,
};

```
#### typeid_t<CommandRegistry>::NewIDType : __int32
```cpp
/* 5679 */
enum typeid_t<CommandRegistry>::NewIDType : __int32
{
New = 0x0,
};

```
#### typeid_t<ContextAccessor>::NewIDType : __int32
```cpp
/* 421008 */
enum typeid_t<ContextAccessor>::NewIDType : __int32
{
New_3 = 0x0,
};

```
#### typeid_t<IDefinitionInstance>::NewIDType : __int32
```cpp
/* 48665 */
enum typeid_t<IDefinitionInstance>::NewIDType : __int32
{
New_0 = 0x0,
};

```
#### typeid_t<ScriptBinderComponent>::NewIDType : __int32
```cpp
/* 99879 */
enum typeid_t<ScriptBinderComponent>::NewIDType : __int32
{
New_2 = 0x0,
};

```
