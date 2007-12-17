%define version 5.5.2
%define release %mkrel 2

%define libname %mklibname -d %{name}

Name:		dmalloc
Version:	%{version}
Release:	%{release}
Summary:	Debugging MALLOC
License:	BSD style
URL:		http://dmalloc.com/
Group:		Development/Other
Source:		http://dmalloc.com/releases/%{name}-%{version}.tgz
Requires:	%{libname} = %{version}

%package -n %{libname}
Summary:	Debugging MALLOC library
Group:		Development/Other
Provides:	dmalloc-devel = %{version}-%{release}
Provides:	libdmalloc-devel = %{version}-%{release} %mklibname %name
Obsoletes:	dmalloc-devel libdmalloc-devel %mklibname %name

%description
The debug memory allocation or "dmalloc" library has been designed
as a drop in replacement for the system's `malloc', `realloc',
`calloc', `free' and other memory management routines while providing
powerful debugging facilities configurable at runtime.  These
facilities include such things as memory-leak tracking, fence-post write
detection, file/line number reporting, and general logging of
statistics.

%description -n %{libname}
The debug memory allocation or "dmalloc" library has been designed
as a drop in replacement for the system's `malloc', `realloc',
`calloc', `free' and other memory management routines while providing
powerful debugging facilities configurable at runtime.  These
facilities include such things as memory-leak tracking, fence-post write
detection, file/line number reporting, and general logging of
statistics.

%prep
%setup -q
chmod -R o+rX .

%build
export CFLAGS=`echo %optflags | sed 's/-O2/-O0/'`

# testing program will segfault when building with -fPIC flag, so
# don't build shared library at all. Anyway this is for developers,
# so building static library is enough.
%configure2_5x --enable-threads

# test this puppy
make heavy

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc ChangeLog.1 INSTALL NEWS README RELEASE.html docs/NOTES docs/TODO docs/*.html
%{_bindir}/*

%files -n %libname
%defattr (-,root,root)
%{_includedir}/*
%{_libdir}/*.a
