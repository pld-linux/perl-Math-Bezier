#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	Bezier
Summary:	Math::Bezier Perl module - solution of Bezier curves
Summary(pl.UTF-8):	Moduł Perla Math::Bezier - obliczający krzywe Beziera
Name:		perl-Math-Bezier
Version:	0.01
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ba6874d8754e2d64ab9c7d15e0eb56c2
URL:		http://search.cpan.org/dist/Math-Bezier/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements the algorithm for the solution of Bezier curves
as presented by Robert D. Miller in Graphics Gems V, "Quick and Simple
Bezier Curve Drawing".

%description -l pl.UTF-8
Ten moduł jest implementacją algorytmu obliczania krzywych Beziera
pokazanego przez Roberta D. Millera w Graphics Gems V "Quick and
Simple Bezier Curve Drawing".

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
%doc Changes README
%{perl_vendorlib}/Math/Bezier.pm
%{_mandir}/man3/*
