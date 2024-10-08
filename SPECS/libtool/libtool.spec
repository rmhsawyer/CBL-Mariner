Summary:        Shared libraries, portable interface
Name:           libtool
Version:        2.4.6
Release:        8%{?dist}
License:        GPLv2
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Tools
URL:            https://www.gnu.org/software/libtool
Source0:        http://ftp.gnu.org/gnu/libtool/%{name}-%{version}.tar.xz

%description
It wraps the complexity of using shared libraries in a
consistent, portable interface.

%package -n libltdl
Summary:        Shared library files for %{name}
Group:          Development/Libraries
Provides:       %{name}-ltdl = %{version}-%{release}

%description -n libltdl
The libtool package contains the GNU libtool, a set of shell scripts which automatically configure UNIX and UNIX-like architectures to generically build shared libraries.
Libtool provides a consistent, portable interface which simplifies the process of using shared libraries.
Shared library files for libtool DLL library from the libtool package.

%package -n libltdl-devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       libltdl = %{version}
Provides:       %{name}-ltdl-devel = %{version}-%{release}
Provides:       %{name}-ltdl-devel%{?_isa} = %{version}-%{release}

%description -n libltdl-devel
The libtool package contains the GNU libtool, a set of shell scripts which automatically configure UNIX and UNIX-like architectures to generically build shared libraries.
Libtool provides a consistent, portable interface which simplifies the process of using shared libraries.
This package contains static libraries and header files need for development.

%prep
%autosetup

%build
%configure \
    --disable-silent-rules
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_infodir}

%check
make %{?_smp_mflags} check

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post -n libltdl -p /sbin/ldconfig
%postun -n libltdl -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING
%{_bindir}/libtoolize
%{_bindir}/libtool
%{_datadir}/aclocal/ltoptions.m4
%{_datadir}/aclocal/libtool.m4
%{_datadir}/aclocal/ltversion.m4
%{_datadir}/aclocal/lt~obsolete.m4
%{_datadir}/aclocal/ltdl.m4
%{_datadir}/aclocal/ltsugar.m4
%{_datadir}/aclocal/ltargz.m4
%{_mandir}/man1/libtool.1.gz
%{_mandir}/man1/libtoolize.1.gz
%{_datadir}/libtool/build-aux

%files -n libltdl-devel
%{_includedir}/libltdl/lt_dlloader.h
%{_includedir}/libltdl/lt_system.h
%{_includedir}/libltdl/lt_error.h
%{_includedir}/ltdl.h
%{_libdir}/libltdl.a
%{_libdir}/libltdl.so
%{_datadir}/libtool/*
%exclude %{_datadir}/libtool/build-aux

%files -n libltdl
%{_libdir}/libltdl.so.7
%{_libdir}/libltdl.so.7.3.1

%changelog
* Mon Aug 30 2021 Bala <balakumaran.kannan@microsoft.com> - 2.4.6-8
- Replaced build commands with rpm macros
- Corrected version in previous changelog
- License verified
- Removed sha1 macro

* Fri Feb 05 2021 Joe Schmitt <joschmit@microsoft.com> - 2.4.6-7
- Provide libtool-ltdl-devel%%{?_isa}

* Mon Sep 28 2020 Ruying Chen <v-ruyche@microsoft.com> 2.4.6-6
- Add explicit provides for libtool-ltdl, libtool-ltdl-devel

* Sat May 09 2020 Nick Samson <nisamson@microsoft.com> - 2.4.6-5
- Added %%license line automatically

* Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 2.4.6-4
- Initial CBL-Mariner import from Photon (license: Apache2).

* Fri Jun 23 2017 Xiaolin Li <xiaolinl@vmware.com> 2.4.6-3
- Move header file and source code to libltdl-devel package.

* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.4.6-2
- GA - Bump release of all rpms

* Wed Jan 13 2016 Xiaolin Li <xiaolinl@vmware.com> 2.4.6-1
- Updated to version 2.4.6

* Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 2.4.2-1
- Initial build.  First version
