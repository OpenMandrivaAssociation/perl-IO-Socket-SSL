%define modname	IO-Socket-SSL

Summary:	Nearly transparent SSL encapsulation for IO::Socket::INET
Name:		perl-%{modname}
Version:	2.089
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/IO::Socket::SSL
Source0:	https://www.cpan.org/modules/by-module/IO/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Net::SSLeay)
BuildRequires:	perl(IO::Socket::INET6)
BuildRequires:	perl(JSON::PP)
BuildRequires:  perl(Test)

%description
IO::Socket::SSL is a class implementing an object oriented
interface to SSL sockets. The class is a descendent of
IO::Socket::INET and provides a subset of the base class's
interface methods.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
export SKIP_RNG_TEST=1
echo n |perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc README Changes docs
%{perl_vendorlib}/IO
%{_mandir}/man3/*
