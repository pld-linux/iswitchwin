Summary:	Fast Window Switcher for EWHM window managers
Summary(pl):	Narzêdzie do szybkiego prze³±czania okien dla zarz±dców okien EWHM
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

%description -l pl
switchwin pozwala ³atwo prze³±czaæ miêdzy oknami na obszarach
roboczych poprzez wpisywanie (czê¶ci) tytu³u po¿±danego okienka.
Narzêdzie zosta³o zainspirowane przez iswitch-window.jl oryginalnie
napisane przez Topi Paavolê <tjp@iki.fi> dla zarz±dcy okien Sawfish.
iswitchwin u¿ywa libwnck do sterowania zarz±dc± okien i zosta³o
napisane g³ównie dla Metacity i ¶rodowiska GNOME. Powinno dzia³aæ z
dowolnym zarz±dc± okien zgodnym z EWHM.

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
