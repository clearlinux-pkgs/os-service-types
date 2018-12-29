#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : os-service-types
Version  : 1.4.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/ad/1b/7bc2b1f91e5e4c51c40fcbe6d4ebe068f8a96490a0e12f480f98940f4ba4/os-service-types-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ad/1b/7bc2b1f91e5e4c51c40fcbe6d4ebe068f8a96490a0e12f480f98940f4ba4/os-service-types-1.4.0.tar.gz
Summary  : Python library for consuming OpenStack sevice-types-authority data
Group    : Development/Tools
License  : Apache-2.0
Requires: os-service-types-license = %{version}-%{release}
Requires: os-service-types-python = %{version}-%{release}
Requires: os-service-types-python3 = %{version}-%{release}
Requires: pbr
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
os-service-types
        ================
        
        Python library for consuming OpenStack sevice-types-authority data
        
        The `OpenStack Service Types Authority`_ contains information about official
        OpenStack services and their historical ``service-type`` aliases.
        
        The data is in JSON and the latest data should always be used. This simple
        library exists to allow for easy consumption of the data, along with a built-in
        version of the data to use in case network access is for some reason not
        possible and local caching of the fetched data.

%package license
Summary: license components for the os-service-types package.
Group: Default

%description license
license components for the os-service-types package.


%package python
Summary: python components for the os-service-types package.
Group: Default
Requires: os-service-types-python3 = %{version}-%{release}

%description python
python components for the os-service-types package.


%package python3
Summary: python3 components for the os-service-types package.
Group: Default
Requires: python3-core

%description python3
python3 components for the os-service-types package.


%prep
%setup -q -n os-service-types-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545532190
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/os-service-types
cp LICENSE %{buildroot}/usr/share/package-licenses/os-service-types/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/os-service-types/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
