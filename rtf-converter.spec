Summary:	Converts RTF files to HTML
Name:		rtf-converter
Version:	1.1
Release:	10
License:	GPL
Group:		Publishing
Source0:	http://www.kaitiaki.org.nz/download/%{name}_%{version}.tar.gz
# Source0-md5:	224c2855e68d1aea5c4f0230cbc1879b
URL:		http://www.kaitiaki.org.nz/download/
Patch0:		%{name}-cflags.patch
Patch1:		rtf-converter-1.1-mdv-fix-gcc-4.3.patch
BuildRequires:	libstdc++-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The program is intended for command-line conversion of RTF to HTML. It
produces only the HTML body code which will need to be wrapped in BODY
tags and given an HTML header. It attempts to produce HTML 4.0
(strict) compliant html code.

%prep
%setup -q -n rtf
%patch0 -p1
%patch1 -p1 -b .gcc43

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README
%attr(755,root,root) %{_bindir}/rtf-converter

%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-9mdv2011.0
+ Revision: 614722
- the mass rebuild of 2010.1 packages

* Sat Dec 05 2009 Jérôme Brenier <incubusss@mandriva.org> 1.1-8mdv2010.1
+ Revision: 473649
+ rebuild (emptylog)

* Sat Dec 05 2009 Jérôme Brenier <incubusss@mandriva.org> 1.1-7mdv2010.1
+ Revision: 473644
- fix build with gcc >= 4.3

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Aug 26 2007 Gaëtan Lehmann <glehmann@mandriva.org> 1.1-3mdv2008.0
+ Revision: 71555
- rebuild


* Wed Aug 09 2006 glehmann
+ 08/09/06 21:10:58 (55150)
rebuild

* Sun Jul 30 2006 glehmann
+ 07/30/06 10:29:06 (42716)
Import rtf-converter

* Tue Jun 28 2005 <gaetan.lehmann@jouy.inra.fr> 1.1-1mdk
- initial mandirva contrib
- package stollen from PLD

