%global commit f4e1dd5d158dd0e839e87289670908839e9a5bc0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner SaltyPaws
%global project calculator_pi
%global plugin calculator

Name: opencpn-plugin-%{plugin}
Summary: Calculator plugin for OpenCPN
Version: 1.6
Release: 1.%{shortcommit}%{?dist}
License: GPLv2+

Source0: https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{shortcommit}.tar.gz

BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: tinyxml-devel
BuildRequires: wxGTK3-devel
BuildRequires: zlib-devel

Requires: opencpn%{_isa}
Enhances: opencpn%{_isa}

%description
The calculator plugin allows you to carry out all nautical
calculations, without having to leave the OpenCPN environment. The
scientific calculator is capable of working with, and retaining
variables.

%prep
%autosetup -n %{project}-%{commit}

sed -i -e s'/SET(PREFIX_LIB lib)/SET(PREFIX_LIB %{_lib})/' cmake/PluginInstall.cmake

mkdir build

%build

cd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make_build

%install

cd build
mkdir -p %{buildroot}%{_bindir}
%make_install

%find_lang opencpn-%{plugin}_pi

%files -f build/opencpn-%{plugin}_pi.lang

%{_libdir}/opencpn/lib%{plugin}_pi.so
