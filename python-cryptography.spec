%define debug_package %nil
%define pname cryptography
%define name python-%{pname}

Summary:	crytographic recipes for python
Name:		python-%{pname}
Version:	3.2.1
Release:	1
Source0:	https://github.com/pyca/cryptography/archive/%{version}/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc
Patch0:		cryptography-3.2.1-openssl-3.0.patch
License:	LGPLv2
Group:		Development/Python
Url:		https://github.com/pyca/cryptography
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python3)
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
CFLAGS="%{optflags} -fno-strict-aliasing" python setup.py build

%install
python setup.py install --skip-build --root %{buildroot}

%files
%{py_platsitedir}/cryptography/
%{py_platsitedir}/cryptography-*.egg-info

%files doc
%doc README.rst CHANGELOG.rst
