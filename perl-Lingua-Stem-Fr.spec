%define module  Lingua-Stem-Fr
%define name    perl-%{module}
%define version 0.02
%define release %mkrel 1

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Perl French Stemming
License:    GPL or Artistic
Group:      Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Lingua
%{_mandir}/man3*/*
