#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	Fast Window Switcher for EWHM window managers
Name:		iswitchwin
Version:	0.8
Release:	1
License:	GPL
Group:		Applications
Source0:	http://martinman.net/download/iswitchwin/%{name}-%{version}.tar.gz
# Source0-md5:	6a72faa7dc24dea974d63141d78c103b
URL:		http://martinman.net/software/iswitchwin.html
BuildRequires:	dbus-glib-devel
BuildRequires:	libglade2-devel
BuildRequires:	libwnck-devel	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
switchwin lets you easily switch between windows on your workspaces by
typing (part of) the caption of the desired window. It has been
inspired by iswitch-window.jl originally written by Topi Paavola
<tjp@iki.fi> for Sawfish window manager. iswitchwin uses libwnck to
control your window manager and has been primarily written for
Metacity and Gnome environment. It should work with any EWHM
compatibile window manager.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog BUGS README TODO
%attr(755,root,root) %{_bindir}/iswitchwin
%{_datadir}/%{name}/glade/iswitchwinui.glade
