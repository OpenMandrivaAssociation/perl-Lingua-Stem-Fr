%define upstream_name    Lingua-Stem-Fr
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl French Stemming
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.bz2

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
%setup -q -n %{upstream_name}-%{upstream_version}

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

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 403389
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.02-4mdv2009.0
+ Revision: 241608
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Aug 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-2mdv2008.0
+ Revision: 67062
- rebuild


* Mon Jul 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdv2007.0
- first mdv release

