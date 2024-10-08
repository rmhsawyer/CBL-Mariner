%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}
%define _python3_sitearch %(python3 -c "from distutils.sysconfig import get_python_lib; import sys; sys.stdout.write(get_python_lib(1))")
Summary:        Repodata downloading library
Name:           librepo
Version:        1.14.2
Release:        1%{?dist}
License:        LGPLv2+
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Applications/System
URL:            https://github.com/rpm-software-management/librepo
#Source0:       https://github.com/rpm-software-management/librepo/archive/%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  attr-devel
BuildRequires:  check
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  gcc
BuildRequires:  glib-devel
BuildRequires:  gpgme-devel
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  zchunk-devel
Requires:       curl-libs
Requires:       gpgme
Requires:       zchunk

%description
A library providing C and Python (libcURL like) API to downloading repository
metadata.

%package devel
Summary:        Repodata downloading library
Requires:       %{name} = %{version}-%{release}
Requires:       curl-devel
Requires:       curl-libs

%description devel
Development files for librepo.

%package -n python3-%{name}
%{?python_provide:%python_provide python3-%{name}}
Summary:        Python 3 bindings for the librepo library
Requires:       %{name} = %{version}-%{release}

%description -n python3-%{name}
Python 3 bindings for the librepo library.

%prep
%autosetup -p1
mkdir build-py3

%build

pushd build-py3
  %cmake -DPYTHON_DESIRED:FILEPATH=%{_bindir}/python3 -DENABLE_PYTHON_TESTS=%{!?with_pythontests:OFF} ..
  make %{?_smp_mflags}
popd

%check
pushd build-py3
make test
popd

%install
pushd build-py3
  make DESTDIR=%{buildroot} install
popd

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/

%files -n python3-%{name}
%{_python3_sitearch}/%{name}/

%changelog
* Mon Dec 06 2021 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 1.14.2-1
- Update version to 1.14.2.
- Remove python2 package and CVE patch CVE-2020-14352 not needed with latest version.

* Mon Jan 04 2021 Thomas Crain <thcrain@microsoft.com> - 1.11.0-4
- Enable package tests for both major python versions

* Tue Nov 10 2020 Thomas Crain <thcrain@microsoft.com> - 1.11.0-3
- Patch CVE-2020-14352
- Lint to Mariner style

* Sat May 09 2020 Nick Samson <nisamson@microsoft.com> - 1.11.0-2
- Added %%license line automatically

* Tue May 05 2020 Pawel Winogrodzki <pawelwi@microsoft.com> - 1.11.0-1
- Update version to 1.11.0.

* Fri Mar 13 2020 Paul Monson <paulmon@microsoft.com> - 1.10.3-1
- Update to version 1.10.3. License verified.

* Wed Sep 25 2019 Saravanan Somasundaram <sarsoma@microsoft.com> - 1.10.2-2
- Initial CBL-Mariner import from Photon (license: Apache2).

* Wed May 15 2019 Ankit Jain <ankitja@vmware.com> - 1.10.2-1
- Initial build. First version
