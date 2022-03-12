#define debug_package %nil
%define pname cryptography
%define name python-%{pname}

Summary:	crytographic recipes for python
Name:		python-%{pname}
Version:	3.4.7
Release:	2
License:	LGPLv2
Group:		Development/Python
Url:		https://github.com/pyca/cryptography
Source0:	https://github.com/pyca/cryptography/archive/%{version}/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc
Patch0:		0001-fix-pkcs12-parse-ordering.-fixes-5872-5879.patch
Patch1:		0002-WIP-3.0.0-support-5250.patch
Patch2:		0003-switch-to-using-EVP_PKEY_derive-instead-of-DH_comput.patch
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools-rust)
BuildRequires:	python-six
BuildRequires:	python-cffi
BuildRequires:	python-distribute
Requires:	python-pkg-resources

%description
cryptography is a package which provides cryptographic recipes 
and primitives to Python developers.

cryptography includes both high level recipes, and low level
interfaces to common cryptographic algorithms such as symmetric
ciphers, message digests and key derivation functions.

%package doc
Summary:	Documentation for python-%{pname}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pname}-%{version} -p1

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%py_build

%install
%py_install

%files
%dir %{py_platsitedir}/cryptography
%{py_platsitedir}/cryptography/*
%{py_platsitedir}/cryptography-*.egg-info

%files doc
%doc README.rst CHANGELOG.rst
