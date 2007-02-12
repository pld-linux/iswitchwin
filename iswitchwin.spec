Summary:	Fast Window Switcher for EWHM window managers
Summary(pl.UTF-8):   Narzędzie do szybkiego przełączania okien dla zarządców okien EWHM
Name:		iswitchwin
Version:	0.9
Release:	1
License:	GPL
Group:		Applications
Source0:	http://martinman.net/download/iswitchwin/%{name}-%{version}.tar.gz
# Source0-md5:	940dec25d63dbd3cca8fc1718a5de227
URL:		http://martinman.net/software/iswitchwin.html
BuildRequires:	dbus-glib-devel >= 0.35
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libwnck-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
switchwin lets you easily switch between windows on your workspaces by
typing (part of) the caption of the desired window. It has been
inspired by iswitch-window.jl originally written by Topi Paavola
<tjp@iki.fi> for Sawfish window manager. iswitchwin uses libwnck to
control your window manager and has been primarily written for
Metacity and Gnome environment. It should work with any EWHM
compatibile window manager.

%description -l pl.UTF-8
switchwin pozwala łatwo przełączać między oknami na obszarach
roboczych poprzez wpisywanie (części) tytułu pożądanego okienka.
Narzędzie zostało zainspirowane przez iswitch-window.jl oryginalnie
napisane przez Topi Paavolę <tjp@iki.fi> dla zarządcy okien Sawfish.
iswitchwin używa libwnck do sterowania zarządcą okien i zostało
napisane głównie dla Metacity i środowiska GNOME. Powinno działać z
dowolnym zarządcą okien zgodnym z EWHM.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog BUGS README TODO
%attr(755,root,root) %{_bindir}/iswitchwin
%{_datadir}/%{name}
