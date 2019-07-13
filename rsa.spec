#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rsa
Version  : 3.4.2
Release  : 43
URL      : http://pypi.debian.net/rsa/rsa-3.4.2.tar.gz
Source0  : http://pypi.debian.net/rsa/rsa-3.4.2.tar.gz
Summary  : Pure-Python RSA implementation
Group    : Development/Tools
License  : Apache-2.0
Requires: rsa-bin
Requires: rsa-python3
Requires: rsa-python
Requires: pyasn1
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyasn1

BuildRequires : python3-dev
BuildRequires : setuptools

%description
Pure Python RSA implementation
==============================
[![PyPI](https://img.shields.io/pypi/v/rsa.svg)](https://pypi.python.org/pypi/rsa)
[![Build Status](https://travis-ci.org/sybrenstuvel/python-rsa.svg?branch=master)]
(https://travis-ci.org/sybrenstuvel/python-rsa)
[![Coverage Status](https://coveralls.io/repos/github/sybrenstuvel/python-rsa/badge.svg?branch=master)]
(https://coveralls.io/github/sybrenstuvel/python-rsa?branch=master)
[![Code Climate](https://img.shields.io/codeclimate/github/sybrenstuvel/python-rsa.svg)]
(https://codeclimate.com/github/sybrenstuvel/python-rsa)

%package bin
Summary: bin components for the rsa package.
Group: Binaries

%description bin
bin components for the rsa package.


%package python
Summary: python components for the rsa package.
Group: Default
Requires: rsa-python3

%description python
python components for the rsa package.


%package python3
Summary: python3 components for the rsa package.
Group: Default
Requires: python3-core

%description python3
python3 components for the rsa package.


%prep
%setup -q -n rsa-3.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523300732
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyrsa-decrypt
/usr/bin/pyrsa-decrypt-bigfile
/usr/bin/pyrsa-encrypt
/usr/bin/pyrsa-encrypt-bigfile
/usr/bin/pyrsa-keygen
/usr/bin/pyrsa-priv2pub
/usr/bin/pyrsa-sign
/usr/bin/pyrsa-verify

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
