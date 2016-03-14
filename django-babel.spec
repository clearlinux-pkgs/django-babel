#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django-babel
Version  : 0.5.0
Release  : 4
URL      : https://pypi.python.org/packages/source/d/django-babel/django-babel-0.5.0.tar.gz
Source0  : https://pypi.python.org/packages/source/d/django-babel/django-babel-0.5.0.tar.gz
Summary  : Utilities for using Babel in Django
Group    : Development/Tools
License  : BSD-3-Clause
Requires: django-babel-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Tools for using Babel with Django
=================================
This package contains various utilities for integration of `Babel`_ into the
`Django`_ web framework:

%package python
Summary: python components for the django-babel package.
Group: Default

%description python
python components for the django-babel package.


%prep
%setup -q -n django-babel-0.5.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
