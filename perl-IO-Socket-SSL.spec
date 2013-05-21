%define upstream_name    IO-Socket-SSL
%define upstream_version 1.76

Name:			perl-%{upstream_name}
Version:		%perl_convert_version %{upstream_version}
Release:		3

Summary:		Nearly transparent SSL encapsulation for IO::Socket::INET
License:		GPL+ or Artistic
Group:			Development/Perl
URL:			http://search.cpan.org/dist/%{upstream_name}/
Source0:		http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Net::SSLeay) >= 1.21
BuildRequires:	perl(IO::Socket::INET6)
BuildRequires:	perl(JSON::PP)
BuildArch:		noarch
Requires:		perl(Net::SSLeay) >= 1.21

%description
IO::Socket::SSL is a class implementing an object oriented
interface to SSL sockets. The class is a descendent of
IO::Socket::INET and provides a subset of the base class's
interface methods.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
export SKIP_RNG_TEST=1
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

# %%check
# export SKIP_RNG_TEST=1
# %{__make} test

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes util docs certs
%{_mandir}/*/*
%{perl_vendorlib}/IO


%changelog
* Mon Jan 23 2012 Oden Eriksson <oeriksson@mandriva.com> 1.540.0-1mdv2012.0
+ Revision: 766889
- make test don't work as we lack the needed devices in the iurt chroots (why?)
- try to disable the random checks
- 1.54
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x
- rebuild

* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.440.0-1
+ Revision: 682131
- update to new version 1.44

* Thu May 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.430.0-1
+ Revision: 673798
- update to new version 1.43

* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.400.0-1
+ Revision: 672852
- update to new version 1.40

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.390.0-2
+ Revision: 667210
- mass rebuild

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.390.0-1
+ Revision: 643395
- update to new version 1.39

* Mon Jan 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.380.0-1
+ Revision: 634472
- update to new version 1.38

* Sat Dec 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.370.0-1mdv2011.0
+ Revision: 620579
- update to new version 1.37

* Wed Dec 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.350.0-1mdv2011.0
+ Revision: 616213
- update to new version 1.35
- update to new version 1.34

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 1.330.0-1mdv2010.1
+ Revision: 526448
- update to 1.33

* Tue Feb 23 2010 Jérôme Quelin <jquelin@mandriva.org> 1.320.0-1mdv2010.1
+ Revision: 510078
- update to 1.32

* Sat Sep 26 2009 Jérôme Quelin <jquelin@mandriva.org> 1.310.0-1mdv2010.0
+ Revision: 449369
- update to 1.31

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 1.300.0-1mdv2010.0
+ Revision: 418655
- update to 1.30

* Sat Jul 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1.270.0-1mdv2010.0
+ Revision: 399598
- update to 1.27
- using %%perl_convert_version
- fixed license field

* Mon Jul 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.26-1mdv2010.0
+ Revision: 392998
- update to new version 1.26

* Fri Jul 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.25-1mdv2010.0
+ Revision: 391951
- update to new version 1.25

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-1mdv2010.0
+ Revision: 370134
- update to new version 1.24

* Tue Feb 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.23-1mdv2009.1
+ Revision: 344391
- update to new version 1.23

* Sun Jan 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.22-1mdv2009.1
+ Revision: 333405
- update to new version 1.22

* Fri Jan 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.21-1mdv2009.1
+ Revision: 332799
- update to new version 1.21

* Fri Jan 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2009.1
+ Revision: 330184
- update to new version 1.20

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.19-1mdv2009.1
+ Revision: 324505
- update to new version 1.19

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.18-1mdv2009.1
+ Revision: 305733
- update to new version 1.18

* Fri Oct 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.17-1mdv2009.1
+ Revision: 294664
- update to new version 1.17

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-1mdv2009.1
+ Revision: 292190
- update to new version 1.16

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.15-1mdv2009.0
+ Revision: 277950
- update to new version 1.15

* Thu Jul 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-1mdv2009.0
+ Revision: 236721
- update to new version 1.14

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.13-2mdv2009.0
+ Revision: 223798
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.13

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdv2008.1
+ Revision: 104553
- update to new version 1.12

* Sat Oct 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdv2008.1
+ Revision: 98019
- update to new version 1.11
- update to new version 1.11

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdv2008.0
+ Revision: 63958
- update to new version 1.08

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdv2008.0
+ Revision: 46638
- update to new version 1.07

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.06-1mdv2008.0
+ Revision: 20229
- 1.06


* Mon Sep 04 2006 Anssi Hannula <anssi@mandriva.org>
+ 2006-09-03 16:17:30 (59689)
Use module requires as per perl policy

* Fri Aug 18 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-17 22:40:50 (56700)
-Version 0.99.9

* Sun Aug 13 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-12 12:32:52 (55724)
Removed trailing dot from summary

* Sun Aug 13 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-12 12:29:08 (55723)
Version 0.998

* Sun Aug 06 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-05 20:50:25 (53359)
Fixed Bug 24144 Can't install perl-IO-Socket-SSL because perl-Net_SSLeay doesn't provide perl(Net_SSLeay)

* Sun Aug 06 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-05 20:34:41 (53357)
import perl-IO-Socket-SSL-0.99.7-1mdv2007.0

* Sat Aug 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.99.7-1mdv2007.0
- New version (upstream version 0.997)
- dropped fileno patch (merged)

* Sat May 06 2006 Scott Karns <scottk@mandriva.org> 0.97-5mdk
- Restored versioned Requires for perl-Net_SSLeay

* Sat May 06 2006 Scott Karns <scottk@mandriva.org> 0.97-4mdk
- patched fileno == 0 bug in fileno method
- Updated to comply with Mandriva perl packaging policies

* Sat Jan 28 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.97-3mdk
- add BuildRequires: perl-Net_SSLeay

* Fri Jan 27 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.97-2mdk
- Add tests, update BuildRequires

* Tue Jul 19 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.97-1mdk
- 0.97

* Tue Jul 13 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.96-1mdk
- 0.96.
- Removed MANIFEST.

