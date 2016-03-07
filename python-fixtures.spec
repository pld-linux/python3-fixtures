#
# Conditional build:
%bcond_with	tests	# test target [as of 1.4.0 test_warnings fails in some cases]
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Fixtures, reusable state for writing clean tests and more
Summary(pl.UTF-8):	Wyposarzenie testów - stan wielokrotnego użytku pozwalający na pisanie czystych testów
Name:		python-fixtures
Version:	1.4.0
Release:	1
License:	Apache v2.0 or BSD
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/fixtures/
Source0:	https://pypi.python.org/packages/source/f/fixtures/fixtures-%{version}.tar.gz
# Source0-md5:	b706476cb754c9587e7308f9eb18e201
URL:		https://pypi.python.org/pypi/fixtures
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-pbr >= 0.11
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-mock
BuildRequires:	python-six
BuildRequires:	python-testtools >= 0.9.22
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-pbr >= 0.11
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-mock
BuildRequires:	python3-six
BuildRequires:	python3-testtools >= 0.9.22
%endif
%endif
Requires:	python-six
Requires:	python-testtools >= 0.9.22
%if "%{py_ver}" >= "2.7"
Requires:	python-modules >= 1:2.7
%else
Requires:	python-modules >= 1:2.6
Requires:	python-unittest2
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fixtures defines a Python contract for reusable state/support logic,
primarily for unit testing. Helper and adaption logic is included to
make it easy to write your own fixtures using the fixtures contract.
Glue code is provided that makes using fixtures that meet the Fixtures
contract in unittest compatible test cases easy and straight forward.

%description -l pl.UTF-8
Moduł fixtures (wyposarzenie) definiuje pythonowy kontrakt dla stanu
wielokrotnego użytku i logiki wspierającej, służące głównie do testów
jednostkowych. Dołączona jest logika pomocnicza i adaptująca, mająca
na celu ułatwienie pisania własnego wyposarzenia przy użyciu kontraktu
fixtures. Zapewniony jest kod sklejający, pozwalający na łatwe i
proste tworzenie wyposarzenia spełniającego kontrakt fixtures w
przypadkach testowych zgodnych z modułem unittest.

%package -n python3-fixtures
Summary:	Fixtures, reusable state for writing clean tests and more
Summary(pl.UTF-8):	Wyposarzenie testów - stan wielokrotnego użytku pozwalający na pisanie czystych testów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2
Requires:	python3-six
Requires:	python3-testtools >= 0.9.22

%description -n python3-fixtures
Fixtures defines a Python contract for reusable state/support logic,
primarily for unit testing. Helper and adaption logic is included to
make it easy to write your own fixtures using the fixtures contract.
Glue code is provided that makes using fixtures that meet the Fixtures
contract in unittest compatible test cases easy and straight forward.

%description -n python3-fixtures -l pl.UTF-8
Moduł fixtures (wyposarzenie) definiuje pythonowy kontrakt dla stanu
wielokrotnego użytku i logiki wspierającej, służące głównie do testów
jednostkowych. Dołączona jest logika pomocnicza i adaptująca, mająca
na celu ułatwienie pisania własnego wyposarzenia przy użyciu kontraktu
fixtures. Zapewniony jest kod sklejający, pozwalający na łatwe i
proste tworzenie wyposarzenia spełniającego kontrakt fixtures w
przypadkach testowych zgodnych z modułem unittest.

%prep
%setup -q -n fixtures-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS BSD COPYING ChangeLog GOALS NEWS README
%{py_sitescriptdir}/fixtures
%{py_sitescriptdir}/fixtures-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-fixtures
%defattr(644,root,root,755)
%doc AUTHORS BSD COPYING ChangeLog GOALS NEWS README
%{py3_sitescriptdir}/fixtures
%{py3_sitescriptdir}/fixtures-%{version}-py*.egg-info
%endif
