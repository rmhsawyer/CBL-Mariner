Summary:        Compression and decompression routines
Name:           zlib
Version:        1.2.12
Release:        2%{?dist}
URL:            http://www.zlib.net/
License:        zlib
Group:          Applications/System
Vendor:         Microsoft Corporation
Distribution:   Mariner
Source0:        http://www.zlib.net/%{name}-%{version}.tar.xz
Patch0:         CVE-2022-37434.patch
%define sha1    zlib=e1cb0d5c92da8e9a8c2635dfa249c341dfd00322
%description
Compression and decompression routines
%package    devel
Summary:    Header and development files for zlib
Requires:   %{name} = %{version}
%description    devel
It contains the libraries and header files to create applications
for handling compiled objects.
%prep
%setup -q
%build
./configure \
    --prefix=%{_prefix}
make V=1 %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/%{_lib}
ln -sfv ../../lib/$(readlink %{buildroot}%{_libdir}/libz.so) %{buildroot}%{_libdir}/libz.so

%check
make  %{?_smp_mflags} check

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%files
%defattr(-,root,root)
%license README
%{_libdir}/libz.so.*

%files devel
%{_includedir}/zconf.h
%{_includedir}/zlib.h
%{_libdir}/pkgconfig/zlib.pc
%{_libdir}/libz.a
%{_libdir}/libz.so
%{_mandir}/man3/zlib.3.gz

%changelog
* Tue Aug 16 2022 Olivia Crain <oliviacrain@microsoft.com> - 1.2.12-2
- Add upstream patches for CVE-2022-37434
- Fix packaged license- actual license is contained within README
- License verified

*   Wed May 04 2022 Nick Samson <nisamson@microsoft.com> - 1.2.12-1
-   Upgraded to 1.2.12 to fix CVE-2018-25032
*   Sat May 09 2020 Nick Samson <nisamson@microsoft.com> - 1.2.11-3
-   Added %%license line automatically
*   Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 1.2.11-2
-   Initial CBL-Mariner import from Photon (license: Apache2).
*   Wed Apr 05 2017 Xiaolin Li <xiaolinl@vmware.com> 1.2.11-1
-   Updated to version 1.2.11.
*   Wed Dec 07 2016 Xiaolin Li <xiaolinl@vmware.com> 1.2.8-5
-   Moved man3 to devel subpackage.
*   Wed Oct 05 2016 ChangLee <changlee@vmware.com> 1.2.8-4
-   Modified %check
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.2.8-3
-   GA - Bump release of all rpms
*   Mon May 18 2015 Touseef Liaqat <tliaqat@vmware.com> 1.2.8-2
-   Update according to UsrMove.
*   Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 1.2.8-1
-   Initial build. First version
