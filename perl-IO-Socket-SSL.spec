%define module  IO-Socket-SSL
%define name    perl-%{module}
%define version 1.14
%define revision %{version}
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Nearly transparent SSL encapsulation for IO::Socket::INET
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}/
Source:         http://www.cpan.org/modules/by-module/IO/%{module}-%{revision}.tar.bz2
Requires:       perl(Net::SSLeay) >= 1.21
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Net::SSLeay) >= 1.21
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
IO::Socket::SSL is a class implementing an object oriented
interface to SSL sockets. The class is a descendent of
IO::Socket::INET and provides a subset of the base class's
interface methods.

%prep
%setup -q -n %{module}-%{revision}

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
%doc README Changes util docs certs
%{_mandir}/*/*
%{perl_vendorlib}/IO

