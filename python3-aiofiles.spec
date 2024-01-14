#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	File support for asyncio
Summary(pl.UTF-8):	Obsługa plików dla asyncio
Name:		python3-aiofiles
# 23.2.x requires hatchling to build
Version:	23.1.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/aiofiles/
Source0:	https://files.pythonhosted.org/packages/source/a/aiofiles/aiofiles-%{version}.tar.gz
# Source0-md5:	d648a31366030470c97401741747065f
URL:		https://pypi.org/project/aiofiles/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 7.1.2
BuildRequires:	python3-pytest-asyncio >= 0.19.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aiofiles is an Apache 2 licensed library, written in Python, for
handling local disk files in asyncio applications.

%description -l pl.UTF-8
aiofiles to napisana w Pythonie, dostępna na licencji Apache 2
biblioteka do obsługi plików na dysku lokalnym w aplikacjach asyncio.

%prep
%setup -q -n aiofiles-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/aiofiles
%{py3_sitescriptdir}/aiofiles-%{version}-py*.egg-info
