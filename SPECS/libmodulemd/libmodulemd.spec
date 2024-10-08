%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib    ;print(get_python_lib())")}

Summary:        Module manipulating metadata files
Name:           libmodulemd
Version:        2.13.0
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/fedora-modularity/libmodulemd
Source0:        https://github.com/fedora-modularity/libmodulemd/releases/download/%{name}-%{version}/modulemd-%{version}.tar.xz
Group:          Applications/System
Vendor:         Microsoft Corporation
Distribution:   Mariner

Patch1:         test_v1_import_headers_timeout.patch

BuildRequires:  meson
BuildRequires:  clang-devel
BuildRequires:  gcc
BuildRequires:  glib
BuildRequires:  valgrind
BuildRequires:  gobject-introspection-devel
BuildRequires:  python3-pygobject
BuildRequires:  python3-pycodestyle
BuildRequires:  gtk-doc
BuildRequires:  libyaml-devel
Requires:       libyaml

%description
C Library for manipulating module metadata files

%package        devel
Summary:        Header and development files for libmodulemd
Requires:       libyaml-devel
Requires:       %{name} = %{version}-%{release}
%description    devel
It contains the libraries and header files.

%prep
%setup -q -n modulemd-%{version}
%patch1 -p1

%build
meson -Dprefix=%{_prefix} -Ddeveloper_build=false -Dbuild_api_v1=true -Dbuild_api_v2=true \
      -Dwith_py3_overrides=true -Dwith_py2_overrides=false \
      -Dwith_manpages=disabled -Dwith_docs=false build
cd build
ninja

%check
export LC_CTYPE=C.utf8
cd build
ninja test

%install
cd build
DESTDIR=%{buildroot}/ ninja install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README.md
%{_bindir}/modulemd-validator
%{_libdir}/girepository-1.0/Modulemd-2.0.typelib
%{_libdir}/libmodulemd.so.*
%{_datadir}/gir-1.0/Modulemd-2.0.gir
%{python3_sitelib}/*

%files  devel
%{_libdir}/libmodulemd.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/modulemd-2.0/*.h

%changelog
*   Mon Dec 06 2021 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 2.13.0-1
-   Update version to 2.13.0.
-   Update test_v1_import_headers_timeout.patch to sync with 2.13.0 sources
*   Tue Jan 05 2021 Andrew Phelps <anphel@microsoft.com> 2.5.0-5
-   Improve test reliability by increasing timeout.
*   Thu Nov 19 2020 Andrew Phelps <anphel@microsoft.com> 2.5.0-4
-   Fix check test.
*   Sat May 09 2020 Nick Samson <nisamson@microsoft.com> 2.5.0-3
-   Added %%license line automatically
*   Tue Apr 07 2020 Nicolas Ontiveros <niontive@microsoft.com> 2.5.0-2
-   Remove python3-autopep8 from BuildRequires.
*   Tue Mar 17 2020 Henry Beberman <henry.beberman@microsoft.com> 2.5.0-1
-   Update to 2.5.0. Source0 URL Fixed. License verified.
*   Wed Sep 25 2019 Saravanan Somasundaram <sarsoma@microsoft.com> 2.4.0-2
-   Initial CBL-Mariner import from Photon (license: Apache2).
*   Wed May 15 2019 Ankit Jain <ankitja@vmware.com> 2.4.0-1
-   Initial build. First version
