Summary:	Great theme - it doesn't take much space
Summary(pl):	Przepiêkny motyw - idealny kompromis pomiêdzy rozmiarem i czytelno¶ci±
Name:		mozilla-theme-pinball
%define		_realname	pinball
Version:	2004.09.15
%define		_snap		2004-09-15_1.7
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://mozilla-themes.schellen.net/%{_realname}_%{_snap}.jar
# Source0-md5:	05ba8980ee9b8380fce214db6d98f014
Source1:	%{_realname}-installed-chrome.txt
URL:		http://mozilla-themes.schellen.net/
Requires(post,postun):	mozilla >= 1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
