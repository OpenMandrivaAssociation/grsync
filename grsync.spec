Name:		grsync
Version:	1.2.1
Release:	2
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



%changelog
* Thu Mar 29 2012 Andrey Bondrov <abondrov@mandriva.org> 1.2.1-1
+ Revision: 788211
- New version 1.2.1, disable Unity support, spec cleanup

* Tue Nov 01 2011 Andrey Bondrov <abondrov@mandriva.org> 1.2.0-1
+ Revision: 709232
- Add patch0 to fix linking
- New version 1.2.0

* Sun Aug 08 2010 trem <trem@mandriva.org> 1.1.1-1mdv2011.0
+ Revision: 567759
- update to 1.1.1

* Tue Apr 06 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.1.0-1mdv2010.1
+ Revision: 532019
- update to 1.1.0
- update file list

* Thu Feb 04 2010 Funda Wang <fwang@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 500816
- update to new version 1.0.0

* Tue Dec 01 2009 Funda Wang <fwang@mandriva.org> 0.9.3-1mdv2010.1
+ Revision: 472299
- new version 0.9.3

* Mon Oct 05 2009 trem <trem@mandriva.org> 0.9.2-1mdv2010.0
+ Revision: 454253
- update to 0.9.2

* Fri Jul 31 2009 Jani V√§limaa <wally@mandriva.org> 0.9.1-2mdv2010.0
+ Revision: 405007
- require rsync
- update summary and description
- fix icons
- new system menu location (upstream)
- update package group

* Sat Jun 27 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.1-1mdv2010.0
+ Revision: 389883
- Update to new version 0.9.1
- SPEC file clean-up
- Don't disable -Werror=format-security CFLAG

* Thu Jun 11 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.0-1mdv2010.0
+ Revision: 385185
- BuildRequires: intltool
- Update to new version 0.9.0

* Sun Jan 25 2009 trem <trem@mandriva.org> 0.6.2-1mdv2009.1
+ Revision: 333480
- update to 0.6.2
- add define Werror_cflags %%nil to compile

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.6.1-3mdv2009.0
+ Revision: 246646
- rebuild
- drop old menu
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Dec 14 2007 J√©r√¥me Soyer <saispo@mandriva.org> 0.6.1-1mdv2008.1
+ Revision: 119761
- New release 0.6.1

* Wed Jul 25 2007 trem <trem@mandriva.org> 0.6-1mdv2008.0
+ Revision: 55538
- new release 0.6


* Fri Jan 26 2007 Lenny Cartier <lenny@mandriva.com> 0.5.2-3mdv2007.0
+ Revision: 113730
- Buildrequires
- Buildrequires
- Update to 0.5.2
- Import grsync

* Fri Aug 18 2006 trem <trem@mandriva.org> 0.5-1mdv2007.0
- New release 0.5

* Mon Aug 07 2006 trem <trem@mandriva.org> 0.4.3-2mdv2007.0
- Migration to XDG menu (was not added in 0.4.3-1mdk)

* Mon Aug 07 2006 trem <trem@mandriva.org> 0.4.3-1mdk
- New release 0.4.3
- Migration to XDG menu

* Sun May 21 2006 trem <trem@mandriva.org> 0.4.2-1mdk
- New release 0.4.2

* Wed May 10 2006 trem <trem@mandriva.org> 0.4.1-3mdk
- Remove %%{_desktopdir} macro (not a standard macro)

* Fri May 05 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 0.4.1-2mdk
- Add BuildRequires

* Wed May 03 2006 trem <trem@mandriva.org> 0.4.1-1mdk
- New release 0.4.1

* Mon May 01 2006 trem <trem@mandriva.org> 0.4-1mdk
- New release 0.4

* Fri Apr 28 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 0.3.2-3mdk
- Fix BuildRequires

* Fri Apr 28 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 0.3.2-2mdk
- Fix BuildRequires

* Wed Apr 12 2006 trem <trem@mandriva.org> 0.3.2-1mdk
- New release 0.3.2

* Mon Feb 27 2006 trem <trem@mandriva.org> 0.3-1mdk
- New release 0.3

* Tue Feb 14 2006 Jerome Soyer <saispo@mandriva.org> 0.2.2-1mdk
- New release 0.2.2

* Thu Jan 12 2006 <trem@mandriva.org> 0.2-1mdk
- Initial build.

