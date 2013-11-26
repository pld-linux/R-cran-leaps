%define		fversion	%(echo %{version} |tr r -)
%define		modulename	leaps
Summary:	Regression subset selection
Summary(pl.UTF-8):	Wybór podzbioru regresji
Name:		R-cran-%{modulename}
Version:	2.9
Release:	2
License:	GPL v2+
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{version}.tar.gz
# Source0-md5:	ea03350869eeed25d64387402228ab09
BuildRequires:	R >= 2.10.0
BuildRequires:	gcc-fortran
Requires:	R >= 2.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regression subset selection including exhaustive search.

%description -l pl.UTF-8
Wybór podzbioru regresji obejmujący wyczerpujące wyszukiwanie.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,README}
%{_libdir}/R/library/%{modulename}
