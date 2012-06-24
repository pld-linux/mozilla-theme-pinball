Summary:	Great theme - it doesn't take much space
Summary(pl):	Przepi�kny motyw - idealny kompromis pomi�dzy rozmiarem i czytelno�ci�
Name:		mozilla-theme-pinball
Version:	1.0.7
%define		_realname	pinball
%define		_snap		%{version}_1.2.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.uk1.mozdev.org/rsync/themes/themes/%{_realname}_%{_snap}.jar
# Source0-md5:	8a1ebc6e95ac35cee081b9d2c135ddc5
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/themes/pinball.html
Requires(post,postun):	textutils
Requires:	mozilla >= 1.2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_chromedir	%{_libdir}/mozilla/chrome

%description
The great theme, very good in low resolutions (800x600) - it doesn't
take much space, but it's still nice.

%description -l pl
Przepi�kny motyw, kt�ry wy�mienicie nadaje si� do u�ywania w niskich
rozdzielczo�ciach (800x600), gdy� zajmuje niewielk� powierzchni� ekranu nie
trac�c przy tym na urodzie.

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
