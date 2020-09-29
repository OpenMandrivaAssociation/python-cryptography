%define debug_package %nil
%define pname cryptography
%define name python-%{pname}

Summary:	crytographic recipes for python
Name:		python-%{pname}
Version:	2.9.2
Release:	2
Source0:	https://github.com/pyca/cryptography/archive/%{version}.tar.gz
Source100:	%{name}.rpmlintrc
License:	LGPLv2
Group:		Development/Python
Url:		https://github.com/pyca/cryptography
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-six
BuildRequires:	python-cffi
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-six
BuildRequires:	python2-cffi
BuildRequires:	python-distribute
BuildRequires:	python2-distribute
Requires:	python-pkg-resources

%description
cryptography is a package which provides cryptographic recipes 
and primitives to Python developers.

cryptography includes both high level recipes, and low level
interfaces to common cryptographic algorithms such as symmetric
ciphers, message digests and key derivation functions.

%package -n python2-%{pname}
Summary:	cryptographic recipes for python
Group:		Development/Python
Requires:	python2-pkg-resources

%description -n python2-%{pname}
cryptography is a package which provides cryptographic recipes
and primitives to Python developers.

cryptography includes both high level recipes, and low level
interfaces to common cryptographic algorithms such as symmetric
ciphers, message digests and key derivation functions.

%package doc
Summary:	Documentation for python-%{pname}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
%setup -qn %{pname}-%{version}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
CFLAGS="%{optflags} -fno-strict-aliasing" python setup.py build

pushd %{py2dir}
CFLAGS="%{optflags} -fno-strict-aliasing" %{__python2} setup.py build
popd

%install
python setup.py install --skip-build --root %{buildroot}

pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd

%files
%{py_platsitedir}/cryptography/
%{py_platsitedir}/cryptography-*.egg-info

%files -n python2-%{pname}
%{py2_platsitedir}/cryptography
%{py2_platsitedir}/cryptography-*.egg-info

%files doc
%doc README.rst CHANGELOG.rst
