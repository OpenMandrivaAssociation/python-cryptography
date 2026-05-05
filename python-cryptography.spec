%undefine _debugsource_template
%define module cryptography

Name:		python-cryptography
Summary:	Crytographic recipes for python
Version:	48.0.0
Release:	1
License:	Apache-2.0 OR BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/pyca/cryptography
Source0:	https://github.com/pyca/cryptography/archive/%{version}/%{module}-%{version}.tar.gz
# Generate using vendor_rust.py (Source100) with network on
Source1:	cryptography-%{version}-vendor.tar.bz2
Source100:	https://src.fedoraproject.org/rpms/python-cryptography/raw/rawhide/f/vendor_rust.py

BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(cffi)
BuildRequires:	python%{pyver}dist(maturin)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-rust) >= 1.8.0
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	rust-packaging
BuildRequires:	cargo

%description
%{name} is a package which provides cryptographic recipes
and primitives to Python developers.

%{name} includes both high level recipes, and low level
interfaces to common cryptographic algorithms such as symmetric
ciphers, message digests and key derivation functions.

%package doc
Summary:	Documentation for %{name}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{module}-%{version} -p1
tar xf %{S:1}
%cargo_prep -v vendor/

cat >> .cargo/config << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export RUSTFLAGS="-lpython%{pyver}"
%py_build

%install
%py_install

%files
%{py_platsitedir}/%{module}
%{py_platsitedir}/%{module}-%{version}.dist-info

%files doc
%doc README.rst CHANGELOG.rst
