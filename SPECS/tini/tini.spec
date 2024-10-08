Summary:        A tiny but valid init for containers
Name:           tini
Version:        0.19.0
Release:        4%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:            https://github.com/krallin/tini
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  sed

%description
Tini is the simplest init you could think of.

All Tini does is spawn a single child (Tini is meant to be run in a container),
and wait for it to exit all the while reaping zombies and performing signal
forwarding.

%package        static
Summary:        Standalone static build of %{name}

%description    static
This package contains a standalone static build of %{name}, meant to be used
inside a container.

%prep
%autosetup
# Do not strip binaries
sed -i CMakeLists.txt -e 's/ -Wl,-s//'

%build
mkdir build && cd build
%cmake ..
%make_build

%install
%make_install -C build

%files
%license LICENSE
%doc README.md
%{_bindir}/tini

%files static
%license LICENSE
%doc README.md
%{_bindir}/tini-static

%changelog
* Wed Aug 18 2021 Tom Fay <tomfay@microsoft.com> - 0.19.0-4
- Initial CBL-Mariner import from Fedora 35 (license: MIT).
- License verified

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.19.0-2
- Use cmake3 on el7

* Sun Jun 13 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.19.0-1
- Initial package
