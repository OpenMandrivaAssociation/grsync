Name:		grsync
Version:	1.2.1
Release:	%mkrel 1
Summary:	A GTK GUI for rsync
License:	GPLv2
Group:		File tools
URL:		http://www.opbyte.it/grsync/
Source0:	http://www.opbyte.it/release/%{name}-%{version}.tar.gz
Patch0:		grsync-1.0.0-dsofix.patch
BuildRequires:	pkgconfig
BuildRequires:	gtk+2-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	desktop-file-utils
BuildRequires:	dos2unix
BuildRequires:	intltool
BuildRequires:	imagemagick
Requires:	rsync

%description
Grsync is a GUI for rsync, the command line directory
synchronization tool. While it can work with remote
hosts, its focus is to synchronize local directories.

%prep
%setup -q
%patch0 -p1 -b .dsofix

%build
%configure2_5x --disable-unity
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

# Generate and install icons
%__mkdir_p %{buildroot}%{_iconsdir}/hicolor/{64x64,32x32,16x16,128x128}/apps
convert -scale 64 pixmaps/%{name}.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
convert -scale 32 pixmaps/%{name}.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 pixmaps/%{name}.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%__install -D -m644 pixmaps/%{name}.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/

# Desktop file
%__perl -p -i -e 's/grsync.png/grsync/g' %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Filesystem" \
  --add-category="X-MandrivaLinux-System-FileTools" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

# Fix EOLs
dos2unix NEWS AUTHORS README

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/mime/packages/grsync.xml
%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-grsync-session.png
%{_datadir}/pixmaps/grsync-busy.png
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*
%{_iconsdir}/hicolor/*/apps/%{name}.png

