#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Bezier
Summary:	Math::Bezier Perl module - solution of Bezier curves
Summary(pl):	Modu³ Perla Math::Bezier - obliczaj±cy krzywe Beziera
Name:		perl-Math-Bezier
Version:	0.01
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ba6874d8754e2d64ab9c7d15e0eb56c2
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements the algorithm for the solution of Bezier curves
as presented by Robert D. Miller in Graphics Gems V, "Quick and Simple
Bezier Curve Drawing".

%description -l pl
Ten modu³ jest implementacj± algorytmu obliczania krzywych Beziera
pokazanego przez Roberta D. Millera w Graphics Gems V "Quick and
Simple Bezier Curve Drawing".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/Bezier.pm
%{_mandir}/man3/*
