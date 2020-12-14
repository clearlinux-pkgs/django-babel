#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django-babel
Version  : 0.6.2
Release  : 30
URL      : https://files.pythonhosted.org/packages/87/e2/a009668c03148a62bc1d9cb6a30769de1eeab12e70824b609d5b405b5f6e/django-babel-0.6.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/87/e2/a009668c03148a62bc1d9cb6a30769de1eeab12e70824b609d5b405b5f6e/django-babel-0.6.2.tar.gz
Summary  : Utilities for using Babel in Django
Group    : Development/Tools
License  : BSD-3-Clause
Requires: django-babel-license = %{version}-%{release}
Requires: django-babel-python = %{version}-%{release}
Requires: django-babel-python3 = %{version}-%{release}
Requires: Babel
Requires: Django
BuildRequires : Babel
BuildRequires : Django
BuildRequires : buildreq-distutils3

%description
=================================
        
        This package contains various utilities for integration of `Babel`_ into the

%package license
Summary: license components for the django-babel package.
Group: Default

%description license
license components for the django-babel package.


%package python
Summary: python components for the django-babel package.
Group: Default
Requires: django-babel-python3 = %{version}-%{release}

%description python
python components for the django-babel package.


%package python3
Summary: python3 components for the django-babel package.
Group: Default
Requires: python3-core
Provides: pypi(django_babel)
Requires: pypi(babel)
Requires: pypi(django)

%description python3
python3 components for the django-babel package.


%prep
%setup -q -n django-babel-0.6.2
cd %{_builddir}/django-babel-0.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583532813
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/django-babel
cp %{_builddir}/django-babel-0.6.2/COPYING %{buildroot}/usr/share/package-licenses/django-babel/ef9326d4a7684b004c434fcae02325c57b86d2e8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/django-babel/ef9326d4a7684b004c434fcae02325c57b86d2e8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
