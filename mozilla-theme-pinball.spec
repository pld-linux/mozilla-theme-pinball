Summary:	Great theme - it doesn't take much space
Summary(pl):	Przepiêkny motyw - idealny kompromis pomiêdzy rozmiarem i czytelno¶ci±
Name:		mozilla-theme-pinball
Version:	2004.08.11
%define		_realname	pinball
%define		_snap		2004-08-11_1.7
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://mozilla-themes.schellen.net/%{_realname}_%{_snap}.jar
# Source0-md5:	c8330a28b2f13e09c6b5a3c5a5844719
Source1:	%{_realname}-installed-chrome.txt
URL:		http://mozilla-themes.schellen.net/
Requires(post,postun):	textutils
Requires:	mozilla >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
The great theme, very good in low resolutions (800x600) - it doesn't
take much space, but it's still nice.

%description -l pl
Przepiêkny motyw, który wy¶mienicie nadaje siê do u¿ywania w niskich
rozdzielczo¶ciach (800x600), gdy¿ zajmuje niewielk± powierzchniê
ekranu nie trac±c przy tym na urodzie.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
