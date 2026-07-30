%define upstream_name    Lingua-Stem-Fr
%define upstream_version 0.02
Name:		perl-%{upstream_name}
Version:	0.02
Release:	1

Summary:	Perl French Stemming
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Lingua-Stem-Fr
Source0:	https://cpan.metacpan.org/authors/id/S/SD/SDP/Lingua-Stem-Fr-0.02.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module use the a modified version of the Porter Stemming Algorithm to
return a stemmed words.

The algorithm is implemented as described in:
http://snowball.tartarus.org/french/stemmer.html
with some improvement.

The code is carefully crafted to work in conjunction with the Lingua::Stem
module by Benjamin Franz. This french version is based too, on the work of Aldo
Calpini (Italian Version)

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Lingua
%{_mandir}/man3*/*

