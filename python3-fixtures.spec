#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Fixtures, reusable state for writing clean tests and more
Summary(pl.UTF-8):	Wyposażenie testów - stan wielokrotnego użytku pozwalający na pisanie czystych testów
Name:		python3-fixtures
Version:	4.2.5
Release:	1
License:	Apache v2.0 or BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/fixtures/
Source0:	https://files.pythonhosted.org/packages/source/f/fixtures/fixtures-%{version}.tar.gz
# Source0-md5:	eed87ce62f459e8cc3fe489d4898e495
URL:		https://pypi.org/project/fixtures/
BuildRequires:	python3-build
BuildRequires:	python3-hatch-vcs
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
%if %{with tests}
BuildRequires:	python3-testtools >= 0.9.22
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fixtures defines a Python contract for reusable state/support logic,
primarily for unit testing. Helper and adaption logic is included to
make it easy to write your own fixtures using the fixtures contract.
Glue code is provided that makes using fixtures that meet the Fixtures
contract in unittest compatible test cases easy and straight forward.

%description -l pl.UTF-8
Moduł fixtures (wyposażenie) definiuje pythonowy kontrakt dla stanu
wielokrotnego użytku i logiki wspierającej, służące głównie do testów
jednostkowych. Dołączona jest logika pomocnicza i adaptująca, mająca
na celu ułatwienie pisania własnego wyposażenia przy użyciu kontraktu
fixtures. Zapewniony jest kod sklejający, pozwalający na łatwe i
proste tworzenie wyposażenia spełniającego kontrakt fixtures w
przypadkach testowych zgodnych z modułem unittest.

%prep
%setup -q -n fixtures-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m testtools.run fixtures.test_suite
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/fixtures/tests/_fixtures
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/fixtures/tests/test_*.py
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/fixtures/tests/__pycache__/test_*.py*
: >$RPM_BUILD_ROOT%{py3_sitescriptdir}/fixtures/tests/__init__.py
%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}/fixtures
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}/fixtures

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BSD COPYING ChangeLog GOALS NEWS README.rst
%{py3_sitescriptdir}/fixtures
%{py3_sitescriptdir}/fixtures-%{version}.dist-info
