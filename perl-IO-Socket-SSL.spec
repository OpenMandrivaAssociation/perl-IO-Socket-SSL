%define modname	IO-Socket-SSL
%define modver 2.068

Summary:	Nearly transparent SSL encapsulation for IO::Socket::INET
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/IO/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Net::SSLeay) >= 1.21
BuildRequires:	perl(IO::Socket::INET6)
BuildRequires:	perl(JSON::PP)
BuildRequires:  perl(Test)
Requires:	perl(Net::SSLeay) >= 1.21

%description
IO::Socket::SSL is a class implementing an object oriented
interface to SSL sockets. The class is a descendent of
IO::Socket::INET and provides a subset of the base class's
interface methods.

%prep
%setup -qn %{modname}-%{modver}

%build
export SKIP_RNG_TEST=1
echo n |perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc README Changes docs certs
%{perl_vendorlib}/IO
%{_mandir}/man3/*
