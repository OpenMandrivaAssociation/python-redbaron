%global pypi_name redbaron

Name:           python-%{pypi_name}
Version:        0.9.2
Release:        1
Summary:        Bottom-up approach to refactoring in python
License:        LGPLv3
URL:            https://github.com/PyCQA/redbaron
Source:         https://files.pythonhosted.org/packages/92/14/d04d376cca5108e62edeee2d2fc0261af6474d9aebe0b4334721785bc035/redbaron-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pypandoc)
BuildRequires:  python3dist(baron)
BuildRequires:  python3dist(pygments)

Requires: python3dist(baron)
Requires: python3dist(pygments)

Provides:	python-%{pypi_name} = %{EVRD}

%description
RedBaron is a python library and tool powerful enough to be used into IPython 
solely that intent to make the process of writing code that modify source code as easy and as simple as possible. 
That include writing custom refactoring, generic refactoring, tools, 
IDE or directly modifying you source code into IPython with a higher and more powerful abstraction than the advanced texts modification tools that you find in advanced text editors and IDE.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -vrf *.egg-info
sed -i -e 's/\r//' README.md

%build
%py_build

%install
%py_install

%files -n python-%{pypi_name}
%{python_sitelib}/%{pypi_name}/
%{python_sitelib}/%{pypi_name}-*.egg-info/
#{python_sitelib}/__pycache__/*
