Name:           mlocate
Version:        0.26
Release:        5%{?dist}
Summary:        An utility for finding files by name.
License:        GPL-2.0
URL:            https://pagure.io/mlocate
Source0:        http://releases.pagure.org/mlocate/%{name}-%{version}.tar.xz
Patch0:         0001-tests-updatedb-reduce-heirarchy-to-300-from-950.patch
%define sha1    %{name}=c6e6d81b25359c51c545f4b8ba0f3b469227fcbc
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Applications/File
BuildRequires:  sed
BuildRequires:  grep
BuildRequires:  xz
BuildRequires:  gettext

%description
mlocate is a locate/updatedb implementation.  The 'm' stands for "merging":
updatedb reuses the existing database to avoid rereading most of the file
system, which makes updatedb faster and does not trash the system caches as
much.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%configure \
	--localstatedir=%{_localstatedir}/lib \
	--enable-nls \
	--disable-rpath
make %{?_smp_mflags}

%check
make check

%install
make DESTDIR=%{buildroot} install
mv %{buildroot}/%{_bindir}/locate %{buildroot}/%{_bindir}/%{name}
mv %{buildroot}/%{_bindir}/updatedb %{buildroot}/%{_bindir}/updatedb.%{name}
mv %{buildroot}/%{_mandir}/man1/locate.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}*
%{_mandir}/*
%{_datarootdir}/locale/*
%{_localstatedir}/*

%changelog
* Mon Sep 26 2022 Muhammad Falak <mwani@microsoft.com> - 0.26-5
- Introduce patch to fix deep heirarchy test

* Sat May 09 2020 Nick Samson <nisamson@microsoft.com> - 0.26-4
- Added %%license line automatically

*   Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 0.26-3
-   Initial CBL-Mariner import from Photon (license: Apache2).
*   Thu Nov 15 2018 Sujay G <gsujay@vware.com> 0.26-2
-   Added %check section
*   Fri Jul 20 2018 Keerthana K <keerthanak@vmware.com> 0.26-1
-   Initial mlocate package for Photon.
