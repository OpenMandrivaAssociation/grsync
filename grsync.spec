%define name grsync
%define version 0.6.1
%define release %mkrel 1

%define summary Grsync is a GUI (Graphical User Interface) for rsync

Summary: %{summary}
Name: 	 %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Networking/File transfer
URL: http://www.opbyte.it/grsync/
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  pkgconfig
BuildRequires:  gtk+2-devel perl-XML-Parser desktop-file-utils
BuildRequires:  dos2unix
%description
Grsync is a GUI (Graphical User Interface) for rsync, the commandline
directory synchronization tool. It makes use of the GTK2 libraries and
it is released under the GPL2. It is in beta stage and it supports only
a limited set of rsync features, but can be effectively used to
synchronize local directories. Only sources are available as of now,
they can be compiled on various flavours of unices having gtk and autotools,
but it should be possible to compile it under win too. Some ready-made
packages for linux distributions have been made by third parties.

%prep
%setup -q

perl -p -i -e 's/grsync.png/grsync/g' grsync.desktop

%build
%configure2_5x
%make


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

install -m644 pixmaps/%{name}.png -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 pixmaps/%{name}.png -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 pixmaps/%{name}.png -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png


desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="FileTransfer" \
  --add-category="X-MandrivaLinux-Internet-FileTransfer" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %{name}

dos2unix NEWS AUTHORS README

%clean
rm -rf $RPM_BUILD_ROOT


%post
%{update_menus}


%postun
%{clean_menus}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING INSTALL NEWS README
%{_bindir}/%{name}
%{_bindir}/%{name}-batch
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/grsync.png
%{_mandir}/*/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


