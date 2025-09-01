#
# Conditional build:
%bcond_without	static_libs	# static libraries

Summary:	XCB util-cursor module
Summary(pl.UTF-8):	Moduł XCB util-cursor
Name:		xcb-util-cursor
Version:	0.1.6
Release:	1
License:	MIT
Group:		Libraries
#Source0:	https://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz
Source0:	https://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
# Source0-md5:	e85bccd1993992be07232f8b80a814c8
URL:		https://xcb.freedesktop.org/XcbUtil/
BuildRequires:	gperf
BuildRequires:	libxcb-devel >= 1.4
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xcb-proto >= 1.6
BuildRequires:	xcb-util-devel >= 0.3.9
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-renderutil-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.8
BuildRequires:	xz
Requires:	libxcb >= 1.4
Requires:	xcb-util >= 0.3.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

XCB util-cursor module provides the following library:
- cursor: port of libXcursor

%description -l pl.UTF-8
xcb-util udostępnia wiele bibliotek opartych powyżej libxcb (głównej
biblioteki protokołu X) oraz trochę bibliotek rozszerzeń. Te
eksperymentalne biblioteki udostępniają wygodne funkcje i interfejsy
czyniące surowy protokół X bardziej używalnym. Niektóre biblioteki
udostępniają także kod kliencki nie będący ściśle częścią protokołu X,
ale tradycyjnie dostarczany przez Xlib.

Moduł XCB util-cursor udostępnia następującą biliotekę:
- cursor: port biblioteki libXcursor

%package devel
Summary:	Header files for XCB util-cursor library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki XCB util-cursor
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxcb-devel >= 1.4
Requires:	xcb-util-devel >= 0.3.9
Requires:	xcb-util-image-devel
Requires:	xcb-util-renderutil-devel

%description devel
Header files for XCB util-cursor library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki XCB util-cursor.

%package static
Summary:	Static XCB util-cursor library
Summary(pl.UTF-8):	Statyczna biblioteka XCB util-cursor
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XCB util-cursor library.

%description static -l pl.UTF-8
Statyczna biblioteka XCB util-cursor.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libxcb-cursor.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README.md
%attr(755,root,root) %{_libdir}/libxcb-cursor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-cursor.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-cursor.so
%{_includedir}/xcb/xcb_cursor.h
%{_pkgconfigdir}/xcb-cursor.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxcb-cursor.a
%endif
