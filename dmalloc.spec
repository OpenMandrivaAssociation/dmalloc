%define version 5.4.2
%define release 1mdk

%define libname %mklibname %{name}

Name:		dmalloc
Version:	%{version}
Release:	%{release}
Summary:	Debugging MALLOC
License:	BSD style
URL:		http://dmalloc.com/
Group:		Development/Other
Source:		%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	%{libname} = %{version}-%{release}
Provides:	dmalloc-devel = %{version}-%{release}
Provides:	libdmalloc-devel = %{version}-%{release}
Obsoletes:	dmalloc-devel libdmalloc-devel

%package -n %{libname}
Summary:	Debugging MALLOC library
Group:		Development/Other

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
%makeinstall installinfo 
#INFOFILE=docs/%{name}.info

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc ChangeLog.1 INSTALL NEWS README RELEASE.html docs/NOTES docs/TODO docs/*.html
%{_bindir}/*
%{_infodir}/*
%{_includedir}/*

%files -n %{libname}
%defattr (-,root,root)
%{_libdir}/*.a
