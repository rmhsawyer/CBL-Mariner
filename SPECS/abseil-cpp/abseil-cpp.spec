Summary:        C++ Common Libraries
Name:           abseil-cpp
Version:        20211102.0
Release:        2%{?dist}
License:        ASL 2.0
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:            https://abseil.io
Source0:        https://github.com/abseil/abseil-cpp/archive/%{version}/%{name}-%{version}.tar.gz
# Workaround until GTest publishes a release including the "GTEST_FLAG_GET" macro.
# Currently only available in the "main" branch: https://github.com/google/googletest/commit/977cffc4423a2d6c0df3fc9a7b5253b8f79c3f18
Patch0:         gtest_build_fix.patch
# Workaround until GTest publishes a release including the "::testing::Conditional" matcher.
# Currently only available in the "main" branch: https://github.com/google/googletest/commit/8306020a3e9eceafec65508868d7ab5c63bb41f7
Patch1:         disabling_invalid_tests.patch

BuildRequires:  cmake >= 3.20.0
BuildRequires:  gcc
BuildRequires:  make

%if %{with_check}
BuildRequires:  gmock
BuildRequires:  gmock-devel
BuildRequires:  gtest
BuildRequires:  gtest-devel
%endif

%description
Abseil is an open-source collection of C++ library code designed to augment
the C++ standard library. The Abseil library code is collected from
Google's own C++ code base, has been extensively tested and used in
production, and is the same code we depend on in our daily coding lives.

In some cases, Abseil provides pieces missing from the C++ standard; in
others, Abseil provides alternatives to the standard for special needs we've
found through usage in the Google code base. We denote those cases clearly
within the library code we provide you.

Abseil is not meant to be a competitor to the standard library; we've just
found that many of these utilities serve a purpose within our code base,
and we now want to provide those resources to the C++ community as a whole.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
Development headers for %{name}

%prep
%autosetup -p1

%build
mkdir build
pushd build
%cmake \
  -DABSL_PROPAGATE_CXX_STD=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if %{with_check}
  -DABSL_FIND_GOOGLETEST=ON \
  -DABSL_USE_EXTERNAL_GOOGLETEST=ON \
  -DBUILD_TESTING=ON \
%else
  -DBUILD_TESTING=OFF \
%endif
  ..
%make_build

%install
pushd build
%make_install

%check
pushd build
ctest --output-on-failure -E 'absl_symbolize_test|absl_sysinfo_test'

%files
%license LICENSE
%doc FAQ.md README.md UPGRADES.md
%{_libdir}/libabsl_*.so.2111.*

%files devel
%{_includedir}/absl
%{_libdir}/cmake/absl
%{_libdir}/libabsl_*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon Jan 17 2022 Muhammad Falak <mwani@microsoft.com> - 20211102.0-2
- Exclude tests `absl_symbolize_test` & `absl_sysinfo_test`.

* Mon Nov 15 2021 Pawel Winogrodzki <pawelwi@microsoft.com> - 20211102.0-1
- Initial CBL-Mariner import from Fedora 34 (license: MIT).
- License verified.
- Updating to version 20211102.0.
- Removing redundant type fix patch.
- Adding patches removing use of unpublished GTest macros and matchers from the test code.

* Mon Mar 08 2021 Rich Mattes <richmattes@gmail.com> - 20200923.3-1
- Update to release 20200923.3

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200923.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 19 2020 Rich Mattes <richmattes@gmail.com> - 20200923.2-1
- Update to release 20200923.2
- Rebuild to fix tagging in koji (rhbz#1885561)

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200225.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200225.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 27 2020 Rich Mattes <richmattes@gmail.com> - 20200225.2-2
- Don't remove buildroot in install

* Sun May 24 2020 Rich Mattes <richmattes@gmail.com> - 20200225.2-1
- Initial package.
