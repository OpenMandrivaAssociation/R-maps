%bcond_without bootstrap
%global packname  maps
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.2_6
Release:          2
Summary:          Draw Geographical Maps
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-6.tar.gz
%if %{without bootstrap}
Requires:         R-mapproj
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
%if %{without bootstrap}
BuildRequires:    R-mapproj
%endif

%description
Display of maps.  Projection code and larger maps are in separate packages
(mapproj and mapdata).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/mapdata


%changelog
* Wed Feb 22 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2_5-2
+ Revision: 778939
- Rebuild with proper dependencies

* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2_5-1
+ Revision: 776275
- Import R-maps
- Import R-maps

