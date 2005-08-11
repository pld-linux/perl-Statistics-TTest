#
# Conditional build:
%bcond_without	tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Statistics
%define	pnam	TTest
Summary:	Statistics::TTest - Perl module to perform T-test on 2 independent samples
Summary(pl):	Statistics::TTest - modu³ Perla do wykonywania testu T na dwóch niezale¿nych próbkach
Name:		perl-Statistics-TTest
Version:	1.1.0
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	605466db48e2b16063abd16550e7d345
URL:		http://search.cpan.org/dist/Statistics-TTest/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Statistics-Descriptive >= 2.6
BuildRequires:	perl-Statistics-Distributions >= 0.7
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Statistical T-Test module to compare 2 independent
samples. It takes 2 array of point measures, compute the confidence
intervals using the PointEstimation module (which is also included in
this package) and use the T-statistic to test the null hypothesis. If
the null hypothesis is rejected, the difference will be given as the
lower_clm and upper_clm of the TTest object. 

%description -l pl
To jest modu³ statystyczny T-Test do porównywania dwóch niezale¿nych
próbek. Przyjmuje 2 tablice miar punktowych, oblicza przedzia³y
ufno¶ci przy u¿yciu modu³u PointEstimation (za³±czonego w tym
pakiecie) i u¿ywa statystyki T do sprawdzenia hipotezy zerowej. Je¶li
hipoteza zerowa jest odrzucona, zostanie podana ró¿nica jako lower_clm
i upper_clm obiektu TTest.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Statistics/*.pm
%{_mandir}/man3/*
