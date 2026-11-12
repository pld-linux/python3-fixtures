#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Fixtures, reusable state for writing clean tests and more
Summary(pl.UTF-8):	Wyposażenie testów - stan wielokrotnego użytku pozwalający na pisanie czystych testów
Name:		python3-fixtures
Version:	4.3.2
Release:	1
License:	Apache v2.0 or BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/fixtures/
Source0:	https://files.pythonhosted.org/packages/source/f/fixtures/fixtures-%{version}.tar.gz
# Source0-md5:	0e499b47f75900f32282139d3e15cc5e
URL:		https://pypi.org/project/fixtures/
BuildRequires:	python3-build
BuildRequires:	python3-hatch-vcs
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
%if %{with tests}
BuildRequires:	python3-testtools >= 0.9.22
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.10
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
%{__python3} -m testtools.run tests.test_suite
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BSD COPYING GOALS NEWS README.rst
%{py3_sitescriptdir}/fixtures
%{py3_sitescriptdir}/fixtures-%{version}.dist-info
