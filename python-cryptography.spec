%undefine _debugsource_packages
%define pname cryptography
%define name python-%{pname}

Summary:	crytographic recipes for python
Name:		python-%{pname}
Version:	46.0.3
Release:	1
License:	LGPLv2
Group:		Development/Python
Url:		https://github.com/pyca/cryptography
Source0:	https://github.com/pyca/cryptography/archive/%{version}/%{pname}-%{version}.tar.gz
# Generate using vendor_rust.py (Source100) with network on
Source1:	cryptography-%{version}-vendor.tar.bz2
Source100:	https://src.fedoraproject.org/rpms/python-cryptography/raw/rawhide/f/vendor_rust.py
Source1000:	%{name}.rpmlintrc
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(cffi)
BuildRequires:	python%{pyver}dist(maturin)
BuildRequires:	python%{pyver}dist(setuptools-rust) >= 1.8.0
BuildRequires:	python-six
BuildRequires:	python-distribute
BuildRequires:	rust
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

mkdir -p .cargo
cat >> .cargo/config << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "./vendor"
EOF

tar xf %{SOURCE1}

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%py_build

%install
%py_install

%files
%{py_platsitedir}/cryptography
%{py_platsitedir}/cryptography-*.*info

%files doc
%doc README.rst CHANGELOG.rst
