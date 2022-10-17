# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-cleo
Epoch: 100
Version: 1.0.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Create beautiful and testable command-line interfaces
License: MIT
URL: https://github.com/python-poetry/cleo/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Cleo is mostly a higher level wrapper for CliKit, so a lot of the
components and utilities comes from it. Refer to its documentation for
more information.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-cleo
Summary: Create beautiful and testable command-line interfaces
Requires: python3
Requires: python3-crashtest >= 0.4.1
Requires: python3-rapidfuzz >= 2.2.0
Provides: python3-cleo = %{epoch}:%{version}-%{release}
Provides: python3dist(cleo) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cleo = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cleo) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cleo = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cleo) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-cleo
Cleo is mostly a higher level wrapper for CliKit, so a lot of the
components and utilities comes from it. Refer to its documentation for
more information.

%files -n python%{python3_version_nodots}-cleo
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-cleo
Summary: Create beautiful and testable command-line interfaces
Requires: python3
Requires: python3-crashtest >= 0.4.1
Requires: python3-rapidfuzz >= 2.2.0
Provides: python3-cleo = %{epoch}:%{version}-%{release}
Provides: python3dist(cleo) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cleo = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cleo) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cleo = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cleo) = %{epoch}:%{version}-%{release}

%description -n python3-cleo
Cleo is mostly a higher level wrapper for CliKit, so a lot of the
components and utilities comes from it. Refer to its documentation for
more information.

%files -n python3-cleo
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
