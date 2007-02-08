%define		fversion	%(echo %{version} |tr r -)
%define		modulename	leaps
Summary:	Regression subset selection
Summary(pl):	Wybór podzbioru regresji
Name:		R-cran-%{modulename}
Version:	2.7
Release:	2
License:	GPL v2+
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{version}.tar.gz
# Source0-md5:	551d8cd9a53d2eee7c13108577910a44
BuildRequires:	R-base >= 2.4.0
BuildRequires:	gcc-g77
Requires(post,postun):	R-base >= 2.4.0
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regression subset selection including exhaustive search.

%description -l pl
Wybór podzbioru regresji obejmuj±cy wyczerpuj±ce wyszukiwanie.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,README}
%{_libdir}/R/library/%{modulename}
