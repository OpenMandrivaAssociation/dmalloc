%define version 5.5.2
%define release %mkrel 7

%define libname %mklibname -d %{name}

Name:		dmalloc
Version:	%{version}
Release:	%{release}
Summary:	Debugging MALLOC
License:	BSD style
URL:		http://dmalloc.com/
Group:		Development/Other
Source:		http://dmalloc.com/releases/%{name}-%{version}.tgz
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 5.5.2-7mdv2011.0
+ Revision: 617794
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 5.5.2-6mdv2010.0
+ Revision: 428284
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 5.5.2-5mdv2009.0
+ Revision: 244418
- rebuild

* Fri Feb 22 2008 Thierry Vignaud <tv@mandriva.org> 5.5.2-3mdv2008.1
+ Revision: 173832
- rebuild b/c of missing subpackage on ia32
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 14 2007 Thierry Vignaud <tv@mandriva.org> 5.5.2-2mdv2008.1
+ Revision: 119840
- rebuild b/c of missing subpackage on ia32

* Mon Oct 22 2007 Thierry Vignaud <tv@mandriva.org> 5.5.2-1mdv2008.1
+ Revision: 101320
- info doc is no more build
- disable parallel make (broken)
- fix build
- new release

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 5.4.3-2mdv2008.0
+ Revision: 67939
- fix upgrade

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 5.4.3-1mdv2008.0
+ Revision: 67882
- cleanups
- new release
- libify
- add missing requires on info-install
- use %%mkrel
- Import dmalloc



* Sat Jan 29 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.4.2-1mdk
- 5.4.2
 
* Thu May 20 2004 Abel Cheung <deaddog@deaddog.org> 5.3.0-1mdk 
- New version
- libdify and change package splitting, allowing both 32bit and 64bit
  libraries to install
- Spec cleanup
- Build threaded and cxx library
- Use -O0, otherwise test program segfaults

* Fri Sep 05 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.2.1-1mdk
- 5.2.1

* Sun Jul 06 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.2.0-1mdk
- 5.2.0
 
* Tue Feb 11 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.8.2-3mdk
- add good provides (All my excuses to Lenny, the best packager I know)

* Tue Jan 14 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.8.2-2mdk
- reintroduce in contrib (need by lineakconf)
- split in %%name and %%name-devel

* Mon Jul 02 2001 Lenny Cartier <lenny@mandrakesoft.com> 4.8.2-1mdk
- updated to 4.8.2

* Tue Jan 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 4.8.1-1mdk
- updated to 4.8.1

* Tue Aug 29 2000 Lenny Cartier <lenny@mandrakesoft.com> 4.2.0-3mdk
- BM

* Wed Apr 26 2000 Lenny Cartier <lenny@mandrakesoft.com> 4.2.0-2mdk
- fix group 
- fix files section
- bzip2 patches

* Thu Feb 10 2000 Lenny Cartier <lenny@mandrakesoft.com>
- mandrake build
