Summary:	Great theme - it doesn't take much space
Summary(pl.UTF-8):   Przepiękny motyw - idealny kompromis pomiędzy rozmiarem i czytelnością
Name:		mozilla-theme-pinball
%define		_realname	pinball
Version:	2005.09.17
%define		_snap		2005-09-17_1.7
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://mozilla-themes.schellen.net/%{_realname}_%{_snap}.jar
# Source0-md5:	9c8ad2ebc19bd502ff1a793b425b93b8
Source1:	%{_realname}-installed-chrome.txt
URL:		http://mozilla-themes.schellen.net/
Requires(post,postun):	mozilla >= 5:1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 5:1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
The great theme, very good in low resolutions (800x600) - it doesn't
take much space, but it's still nice.

%description -l pl.UTF-8
Przepiękny motyw, który wyśmienicie nadaje się do używania w niskich
rozdzielczościach (800x600), gdyż zajmuje niewielką powierzchnię
ekranu nie tracąc przy tym na urodzie.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
