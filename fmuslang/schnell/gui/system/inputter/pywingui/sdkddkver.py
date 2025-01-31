# sdkddkver.py
# Copyright (c) 2012 Maxim Kolosov

# _WIN32_WINNT version constants
_WIN32_WINNT_NT4 = 0x0400
_WIN32_WINNT_WIN2K = 0x0500
_WIN32_WINNT_WINXP = 0x0501
_WIN32_WINNT_WS03 = 0x0502
_WIN32_WINNT_LONGHORN = 0x0600

# _WIN32_IE_ version constants
_WIN32_IE_IE20 = 0x0200
_WIN32_IE_IE30 = 0x0300
_WIN32_IE_IE302 = 0x0302
_WIN32_IE_IE40 = 0x0400
_WIN32_IE_IE401 = 0x0401
_WIN32_IE_IE50 = 0x0500
_WIN32_IE_IE501 = 0x0501
_WIN32_IE_IE55 = 0x0550
_WIN32_IE_IE60 = 0x0600
_WIN32_IE_IE60SP1 = 0x0601
_WIN32_IE_IE60SP2 = 0x0603
_WIN32_IE_IE70 = 0x0700

# IE <-> OS version mapping
# NT4 supports IE versions 2.0 -> 6.0 SP1
_WIN32_IE_NT4 = _WIN32_IE_IE20
_WIN32_IE_NT4SP1 = _WIN32_IE_IE20
_WIN32_IE_NT4SP2 = _WIN32_IE_IE20
_WIN32_IE_NT4SP3 = _WIN32_IE_IE302
_WIN32_IE_NT4SP4 = _WIN32_IE_IE401
_WIN32_IE_NT4SP5 = _WIN32_IE_IE401
_WIN32_IE_NT4SP6 = _WIN32_IE_IE50
# Win98 supports IE versions 4.01 -> 6.0 SP1
_WIN32_IE_WIN98 = _WIN32_IE_IE401
# Win98SE supports IE versions 5.0 -> 6.0 SP1
_WIN32_IE_WIN98SE = _WIN32_IE_IE50
# WinME supports IE versions 5.5 -> 6.0 SP1
_WIN32_IE_WINME = _WIN32_IE_IE55
# Win2k supports IE versions 5.01 -> 6.0 SP1
_WIN32_IE_WIN2K = _WIN32_IE_IE501
_WIN32_IE_WIN2KSP1 = _WIN32_IE_IE501
_WIN32_IE_WIN2KSP2 = _WIN32_IE_IE501
_WIN32_IE_WIN2KSP3 = _WIN32_IE_IE501
_WIN32_IE_WIN2KSP4 = _WIN32_IE_IE501
_WIN32_IE_XP = _WIN32_IE_IE60
_WIN32_IE_XPSP1 = _WIN32_IE_IE60SP1
_WIN32_IE_XPSP2 = _WIN32_IE_IE60SP2
_WIN32_IE_WS03 = 0x0602
_WIN32_IE_WS03SP1 = _WIN32_IE_IE60SP2
_WIN32_IE_LONGHORN = _WIN32_IE_IE70


# NTDDI version constants
NTDDI_WIN2K = 0x05000000
NTDDI_WIN2KSP1 = 0x05000100
NTDDI_WIN2KSP2 = 0x05000200
NTDDI_WIN2KSP3 = 0x05000300
NTDDI_WIN2KSP4 = 0x05000400
NTDDI_WINXP = 0x05010000
NTDDI_WINXPSP1 = 0x05010100
NTDDI_WINXPSP2 = 0x05010200
NTDDI_WS03 = 0x05020000
NTDDI_WS03SP1 = 0x05020100
NTDDI_LONGHORN = 0x06000000

# masks for version macros
OSVERSION_MASK = 0xFFFF0000
SPVERSION_MASK = 0x0000FF00
SUBVERSION_MASK = 0x000000FF


# macros to extract various version fields from the NTDDI version
def OSVER(Version): return ((Version) & OSVERSION_MASK)
def SPVER(Version): return (((Version) & SPVERSION_MASK) >> 8)
def SUBVER(Version): return (((Version) & SUBVERSION_MASK) )


if 'DECLSPEC_DEPRECATED_DDK' in globals():

	# deprecate in 2k or later
	if NTDDI_VERSION >= NTDDI_WIN2K:
		DECLSPEC_DEPRECATED_DDK_WIN2K = DECLSPEC_DEPRECATED_DDK
	else:
		DECLSPEC_DEPRECATED_DDK_WIN2K = 1

	# deprecate in XP or later
	if NTDDI_VERSION >= NTDDI_WINXP:
		DECLSPEC_DEPRECATED_DDK_WINXP = DECLSPEC_DEPRECATED_DDK
	else:
		DECLSPEC_DEPRECATED_DDK_WINXP = 1

	# deprecate in WS03 or later
	if NTDDI_VERSION >= NTDDI_WS03:
		DECLSPEC_DEPRECATED_DDK_WIN2003 = DECLSPEC_DEPRECATED_DDK
	else:
		DECLSPEC_DEPRECATED_DDK_WIN2003 = 1

	# deprecate in WS03 or later
	if NTDDI_VERSION >= NTDDI_LONGHORN:
		DECLSPEC_DEPRECATED_DDK_LONGHORN = DECLSPEC_DEPRECATED_DDK
	else:
		DECLSPEC_DEPRECATED_DDK_LONGHORN = 1


# if versions aren't already defined, default to most current
def NTDDI_VERSION_FROM_WIN32_WINNT(ver):
	from .version_microsoft import platform
	return ((ver << 8) + platform) << 8

_globals_ = globals()
if not '_WIN32_WINNT' in _globals_ and not '_CHICAGO_' in _globals_:
	#~ _WIN32_WINNT = 0x0600
	from .version_microsoft import WINVER
	_WIN32_WINNT = WINVER

# set NTDDI_VERSION based on _WIN32_WINNT
if _WIN32_WINNT:
	NTDDI_VERSION = NTDDI_VERSION_FROM_WIN32_WINNT(_WIN32_WINNT)
else:
	NTDDI_VERSION = 0x06000000

# set WINVER based on _WIN32_WINNT
if _WIN32_WINNT:
	WINVER = _WIN32_WINNT
else:
	WINVER = 0x0600

# set _WIN32_IE based on _WIN32_WINNT
if _WIN32_WINNT:
	if (_WIN32_WINNT <= _WIN32_WINNT_NT4):
		_WIN32_IE = _WIN32_IE_IE50
	elif (_WIN32_WINNT <= _WIN32_WINNT_WIN2K):
		_WIN32_IE = _WIN32_IE_IE501
	elif (_WIN32_WINNT <= _WIN32_WINNT_WINXP):
		_WIN32_IE = _WIN32_IE_IE60
	elif (_WIN32_WINNT <= _WIN32_WINNT_WS03):
		_WIN32_IE = 0x0602
	else:
		_WIN32_IE = 0x0700
else:
	_WIN32_IE = 0x0700

if __name__ == '__main__':
	print(('NTDDI_WIN2K\t%s,\t%d' % (hex(NTDDI_WIN2K), NTDDI_WIN2K)))
	print(('NTDDI_WINXP\t%s,\t%d' % (hex(NTDDI_WINXP), NTDDI_WINXP)))
	print(('NTDDI_WINXPSP1\t%s,\t%d' % (hex(NTDDI_WINXPSP1), NTDDI_WINXPSP1)))
	print(('NTDDI_WINXPSP2\t%s,\t%d' % (hex(NTDDI_WINXPSP2), NTDDI_WINXPSP2)))
	print(('NTDDI_LONGHORN\t%s,\t%d' % (hex(NTDDI_LONGHORN), NTDDI_LONGHORN)))
	print(('= NTDDI_VERSION\t%s,\t%d' % (hex(NTDDI_VERSION), NTDDI_VERSION)))
	from .version_microsoft import major, minor, build, platform, text
	print(('%d, %d, %d, %d, %s' % (major, minor, build, platform, text)))
