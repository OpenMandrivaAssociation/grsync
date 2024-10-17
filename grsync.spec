%global _legacy_common_support 1


Name:		grsync
Version:	1.3.1
Release:	1
Summary:	A GTK GUI for rsync
License:	GPLv2
Group:		File tools
URL:		https://www.opbyte.it/grsync/
Source0:    https://sourceforge.net/projects/grsync/files/grsync-%{version}.tar.gz
#Source0:	http://www.opbyte.it/release/%{name}-%{version}.tar.gz
# https://sourceforge.net/p/grsync/patches/9/?limit=25
#Patch0:     patch-src-callbacks.c.patch

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(gtk+-3.0)
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
%autopatch -p1

%build

%configure --disable-unity
%make_build

%install
%make_install

# Generate and install icons
%__mkdir_p %{buildroot}%{_iconsdir}/hicolor/{64x64,32x32,16x16,128x128}/apps
convert -scale 64 pixmaps/%{name}.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
convert -scale 32 pixmaps/%{name}.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 pixmaps/%{name}.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%__install -D -m644 pixmaps/%{name}.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/

# Desktop
desktop-file-install \
    --remove-category=Application \
    --add-category=FileTransfer \
    --add-category=GTK \
    --dir=%{buildroot}%{_datadir}/applications/ \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

# Fix EOLs
dos2unix NEWS AUTHORS README


%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/mime/packages/grsync.xml
%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-grsync-session.png
%{_datadir}/pixmaps/grsync-busy.png
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*
%{_iconsdir}/hicolor/*/apps/%{name}.png

