Summary:	Great theme - it doesn't take much space
Summary(pl):	Przepiêkny motyw - idealny kompromis pomiêdzy rozmiarem i czytelno¶ci±
Name:		mozilla-theme-pinball
Version:	1.0.3
%define		_realname	pinball
%define		_snap		%{version}_1.0-RC3
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/themes/%{_realname}_%{_snap}.jar
# Source0-md5:	8f9e2f6d2fd6ca319f6573a9b40245c0
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/skins/pinball.html
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_libdir}/mozilla/chrome

%description
The great theme, very good in low resolutions (800x600) - it doesn't
take much space, but it's still nice.

%description -l pl
Przepiêkny motyw, który wy¶mienicie nadaje siê do u¿ywania w niskich
rozdzielczo¶ciach (800x600), gdy¿ zajmuje niewielk± powierzchniê ekranu nie
trac±c przy tym na urodzie.

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
