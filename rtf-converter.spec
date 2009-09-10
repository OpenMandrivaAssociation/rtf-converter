Summary:	Converts RTF files to HTML
Name:		rtf-converter
Version:	1.1
Release:	%mkrel 6
License:	GPL
Group:		Publishing
Source0:	http://www.kaitiaki.org.nz/download/%{name}_%{version}.tar.gz
# Source0-md5:	224c2855e68d1aea5c4f0230cbc1879b
URL:		http://www.kaitiaki.org.nz/download/
Patch0:		%{name}-cflags.patch
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

