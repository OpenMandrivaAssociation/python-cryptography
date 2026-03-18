%undefine _debugsource_template
%define module cryptography

Name:		python-cryptography
Summary:	Crytographic recipes for python
Version:	46.0.5
Release:	1
License:	LGPLv2
Group:		Development/Python
URL:		https://github.com/pyca/cryptography
Source0:	https://github.com/pyca/cryptography/archive/%{version}/%{module}-%{version}.tar.gz
# Generate using vendor_rust.py (Source100) with network on
Source1:	cryptography-%{version}-vendor.tar.bz2
Source100:	https://src.fedoraproject.org/rpms/python-cryptography/raw/rawhide/f/vendor_rust.py
Source1000:	%{name}.rpmlintrc
# Patch0 for 46.0.5: https://github.com/pyca/cryptography/commit/43eb178ee3aae8d0060221118437b03c23570a41
# Patch0 should be able to be dropped in the next release (> 46.0.5) as it has been merged upstream.
Patch0:		https://github.com/pyca/cryptography/commit/43eb178ee3aae8d0060221118437b03c23570a41.patch#/fix-installing-stray-files-into-site-packages.patch

BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(cffi)
BuildRequires:	python%{pyver}dist(maturin)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-rust) >= 1.8.0
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python-six
BuildRequires:	python-distribute
BuildRequires:	rust-packaging
BuildRequires:	cargo
Requires:	python-pkg-resources

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
tar xf %{SOURCE1}
%cargo_prep -v vendor/

cat >> .cargo/config << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export RUSTFLAGS="-lpython%{pyver}"
%py_build

%install
%py_install

%files
%{py_platsitedir}/%{module}/
%{py_platsitedir}/%{module}-%{version}.dist-info/

%files doc
%doc README.rst CHANGELOG.rst
