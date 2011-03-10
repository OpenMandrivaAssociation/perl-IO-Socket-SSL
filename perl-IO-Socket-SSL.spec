%define upstream_name    IO-Socket-SSL
%define upstream_version 1.39

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1

Summary:        Nearly transparent SSL encapsulation for IO::Socket::INET
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{upstream_name}/
Source0:        http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Net::SSLeay) >= 1.21
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
Requires:       perl(Net::SSLeay) >= 1.21

%description
IO::Socket::SSL is a class implementing an object oriented
interface to SSL sockets. The class is a descendent of
IO::Socket::INET and provides a subset of the base class's
interface methods.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

