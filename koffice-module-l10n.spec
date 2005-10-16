# TODO:
# - missing obsoletes
# - finish install and files

%define		_name		koffice
%define		koffice_epoch	5
%define		kdelibs_epoch	9
Summary:	Koffice per package i18n files
Summary(pl):	T³umaczenia Koffice podzielone wg. pakietów
Name:		%{_name}-module-l10n
Version:	1.4.2
Release:	0.1
Epoch:		5
Group:		X11/Applications
License:	GPL
Source0:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-bg-%{version}.tar.bz2
# Source0-md5:	ad980947860046ca4d5e0c8b23b7d3ab
Source1:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ca-%{version}.tar.bz2
# Source1-md5:	8a546eec2897af073bb564edf7150b6d
Source2:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-cs-%{version}.tar.bz2
# Source2-md5:	58e6c355e478ab459e6f0a5c86662f36
Source3:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-cy-%{version}.tar.bz2
# Source3-md5:	ed0c069797a89680d49bd396f80e94e1
Source4:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-da-%{version}.tar.bz2
# Source4-md5:	f6c3b0afcb299519f0663aa5a3ff3362
Source5:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-de-%{version}.tar.bz2
# Source5-md5:	2659e56e079bfdd133833a39497f80e6
Source6:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-el-%{version}.tar.bz2
# Source6-md5:	1aa341393b7ade4037ddeed77c73cacf
Source7:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-en_GB-%{version}.tar.bz2
# Source7-md5:	caf59bd82ac94ccbeaa4b907c218defa
Source8:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-es-%{version}.tar.bz2
# Source8-md5:	0f429120c8b27d1208f020a353aeb88d
Source9:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-et-%{version}.tar.bz2
# Source9-md5:	1ac8201573602a69e7d00b3332cb3bec
Source10:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-eu-%{version}.tar.bz2
# Source10-md5:	f8417721a49dd23f20115e102b0a8204
Source11:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-fi-%{version}.tar.bz2
# Source11-md5:	b4925a3bd6db8b6b787b0313e3695371
Source12:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-fr-%{version}.tar.bz2
# Source12-md5:	5f4e1d1f360a14e4ca2d24d2d85bf061
Source13:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-hu-%{version}.tar.bz2
# Source13-md5:	ba83bf5a84f1ae5e7b22c1611c89e8bd
Source14:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-it-%{version}.tar.bz2
# Source14-md5:	62609f289dc1ed216c7d075045159a04
Source15:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-nb-%{version}.tar.bz2
# Source15-md5:	9d8c327b3e6567d90258cec8b0694a2c
Source16:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-nl-%{version}.tar.bz2
# Source16-md5:	6328a285565add97cd55413e52541050
Source17:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-nn-%{version}.tar.bz2
# Source17-md5:	2e52095b2c9c879e101d274888d49fcc
Source18:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-pl-%{version}.tar.bz2
# Source18-md5:	78337154a7183cda46d34f80c6bf23e5
Source19:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-pt-%{version}.tar.bz2
# Source19-md5:	61e11d48f788275389f0b75e75b8de2b
Source20:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-pt_BR-%{version}.tar.bz2
# Source20-md5:	a559487f91f9bdf7eaf608f5d88c67c1
Source21:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ru-%{version}.tar.bz2
# Source21-md5:	a1527f53ed16ceed8c295614eedf7deb
Source22:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sl-%{version}.tar.bz2
# Source22-md5:	6d85c8b3f84b892471fd3cadd00aba37
Source23:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sr-%{version}.tar.bz2
# Source23-md5:	97d0fa5fdb458bbe5c8ef5317e15ed5c
Source24:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sr@Latn-%{version}.tar.bz2
# Source24-md5:	65e7e7939b3d538913ddcec261741f75
Source25:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sv-%{version}.tar.bz2
# Source25-md5:	897218187ef83afcd99406b62e352e69
Source26:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ta-%{version}.tar.bz2
# Source26-md5:	2c55f413ec8e02a667e37d967186dc86
Source27:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-tg-%{version}.tar.bz2
# Source27-md5:	c10cd70d7f1a9a397f768002625ad6f9
Source28:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-zh_CN-%{version}.tar.bz2
# Source28-md5:	5733aa59661f8828c66ef0d2335d4242
URL:		http://i18n.kde.org/
BuildRequires:	kdelibs >= %{kdelibs_epoch}:%{version}
BuildRequires:	kdelibs-devel
BuildRequires:	libxml2-progs >= 2.4.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KOffice - international support.

%description -l pl
KOffice - wsparcie dla wielu jêzyków.

%package -n koffice-common-i18n
Summary:	Internationalization and localization files for koffice-common
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla koffice-common
Group:		X11/Applications
Requires:	%{_name}-common = %{koffice_epoch}:%{version}
Requires:	kdebase-core-i18n
Obsoletes:	koffice-i18n-base
Obsoletes:	koffice-i18n-Afrikaans
Obsoletes:	koffice-i18n-Arabic
Obsoletes:	koffice-i18n-Azerbaijani
Obsoletes:	koffice-i18n-Bulgarian
Obsoletes:	koffice-i18n-Basque
Obsoletes:	koffice-i18n-Breton
Obsoletes:	koffice-i18n-Bosnian
Obsoletes:	koffice-i18n-Catalan
Obsoletes:	koffice-i18n-Czech
Obsoletes:	koffice-i18n-Cymraeg
Obsoletes:	koffice-i18n-Danish
Obsoletes:	koffice-i18n-German
Obsoletes:	koffice-i18n-Greek
Obsoletes:	koffice-i18n-English
Obsoletes:	koffice-i18n-English_UK
Obsoletes:	koffice-i18n-Esperanto
Obsoletes:	koffice-i18n-Spanish
Obsoletes:	koffice-i18n-Estonian
Obsoletes:	koffice-i18n-Basque
Obsoletes:	koffice-i18n-Farsi
Obsoletes:	koffice-i18n-Finnish
Obsoletes:	koffice-i18n-French
Obsoletes:	koffice-i18n-Irish
Obsoletes:	koffice-i18n-Galician
Obsoletes:	koffice-i18n-Hindi
Obsoletes:	koffice-i18n-Hebrew
Obsoletes:	koffice-i18n-Croatian
Obsoletes:	koffice-i18n-Hungarian
Obsoletes:	koffice-i18n-Upper_Sorbian
Obsoletes:	koffice-i18n-Indonesian
Obsoletes:	koffice-i18n-Icelandic
Obsoletes:	koffice-i18n-Italian
Obsoletes:	koffice-i18n-Japanese
Obsoletes:	koffice-i18n-Korean
Obsoletes:	koffice-i18n-Lithuanian
Obsoletes:	koffice-i18n-Lao
Obsoletes:	koffice-i18n-Latvian
Obsoletes:	koffice-i18n-Maori
Obsoletes:	koffice-i18n-Macedonian
Obsoletes:	koffice-i18n-Malay
Obsoletes:	koffice-i18n-Maltese
Obsoletes:	koffice-i18n-Mongolian
Obsoletes:	koffice-i18n-Dutch
Obsoletes:	koffice-i18n-Norwegian_Bokmaal
Obsoletes:	koffice-i18n-Norwegian_Nynorsk
Obsoletes:	koffice-i18n-Northern_Sotho
Obsoletes:	koffice-i18n-Gascon_occitan
Obsoletes:	koffice-i18n-Polish
Obsoletes:	koffice-i18n-Portuguese
Obsoletes:	koffice-i18n-Brazil_Portuguese
Obsoletes:	koffice-i18n-Romanian
Obsoletes:	koffice-i18n-Russian
Obsoletes:	koffice-i18n-Swati
Obsoletes:	koffice-i18n-Northern_Sami
Obsoletes:	koffice-i18n-Slovak
Obsoletes:	koffice-i18n-Slovenian
Obsoletes:	koffice-i18n-Serbian
Obsoletes:	koffice-i18n-Swedish
Obsoletes:	koffice-i18n-Tamil
Obsoletes:	koffice-i18n-Tajik
Obsoletes:	koffice-i18n-Thai
Obsoletes:	koffice-i18n-Turkish
Obsoletes:	koffice-i18n-Ukrainian
Obsoletes:	koffice-i18n-Uzbek
Obsoletes:	koffice-i18n-Venda
Obsoletes:	koffice-i18n-Vietnamese
Obsoletes:	koffice-i18n-Walloon
Obsoletes:	koffice-i18n-Xhosa
Obsoletes:	koffice-i18n-Simplified_Chinese
Obsoletes:	koffice-i18n-Chinese
Obsoletes:	koffice-i18n-Zulu

%description -n koffice-common-i18n
Internationalization and localization files for koffice-common.

%description -n koffice-common-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla koffice-common.

%package -n koffice-karbon-i18n
Summary:	Internationalization and localization files for karbon
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla karbona
Group:		X11/Applications
Requires:	%{_name}-karbon = %{koffice_epoch}:%{version}
Requires:	%{_name}-common-i18n = %{epoch}:%{version}-%{release}

%description -n koffice-karbon-i18n
Internationalization and localization files for karbon.

%description -n koffice-karbon-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla karbon.

%package -n koffice-kchart-i18n
Summary:	Internationalization and localization files for kchart
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcharta
Group:		X11/Applications
Requires:	%{_name}-kchart = %{koffice_epoch}:%{version}
Requires:	%{_name}-common-i18n = %{epoch}:%{version}-%{release}

%description -n koffice-kchart-i18n
Internationalization and localization files for kchart.

%description -n koffice-kchart-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcharta.

%package -n koffice-kexi-i18n
Summary:	Internationalization and localization files for kexi
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kexi
Group:		X11/Applications
Requires:	%{_name}-kexi = %{koffice_epoch}:%{version}
Requires:	%{_name}-common-i18n = %{epoch}:%{version}-%{release}

%description -n koffice-kexi-i18n
Internationalization and localization files for kexi.

%description -n koffice-kexi-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kexi.

%package -n koffice-kformula-i18n
Summary:	Internationalization and localization files for kformula
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kformuli
Group:		X11/Applications
Requires:	%{_name}-kformula = %{koffice_epoch}:%{version}
Requires:	%{_name}-common-i18n = %{epoch}:%{version}-%{release}

%description -n koffice-kformula-i18n
Internationalization and localization files for kformula.

%description -n koffice-kformula-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kformuli.

%package -n koffice-kivio-i18n
Summary:	Internationalization and localization files for kivio
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kivio
Group:		X11/Applications
Requires:	%{_name}-kivio = %{koffice_epoch}:%{version}
Requires:	%{_name}-common-i18n = %{epoch}:%{version}-%{release}

%description -n koffice-kivio-i18n
Internationalization and localization files for kivio.

%description -n koffice-kivio-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kivio.

%package -n koffice-kpresenter-i18n
Summary:	Internationalization and localization files for kpresenter
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpresentera
Group:		X11/Applications
Requires:	%{_name}-kpresenter = %{koffice_epoch}:%{version}
Requires:	%{_name}-common-i18n = %{epoch}:%{version}-%{release}

%description -n koffice-kpresenter-i18n
Internationalization and localization files for kpresenter.

%description -n koffice-kpresenter-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpresentera.

%package -n koffice-krita-i18n
Summary:	Internationalization and localization files for krita
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla krita
Group:		X11/Applications
Requires:	%{_name}-krita = %{koffice_epoch}:%{version}
Requires:	%{_name}-common-i18n = %{epoch}:%{version}-%{release}

%description -n koffice-krita-i18n
Internationalization and localization files for krita.

%description -n koffice-krita-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla krita.

%package -n koffice-kspread-i18n
Summary:	Internationalization and localization files for kspread
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kspreada
Group:		X11/Applications
Requires:	%{_name}-kspread = %{koffice_epoch}:%{version}
Requires:	%{_name}-common-i18n = %{epoch}:%{version}-%{release}

%description -n koffice-kspread-i18n
Internationalization and localization files for kspread.

%description -n koffice-kspread-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kspreada.

%package -n koffice-kugar-i18n
Summary:	Internationalization and localization files for kugar
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kugara
Group:		X11/Applications
Requires:	%{_name}-kugar = %{koffice_epoch}:%{version}
Requires:	%{_name}-common-i18n = %{epoch}:%{version}-%{release}

%description -n koffice-kugar-i18n
Internationalization and localization files for kugar.

%description -n koffice-kugar-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kugara.

%package -n koffice-kword-i18n
Summary:	Internationalization and localization files for kword
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kworda
Group:		X11/Applications
Requires:	%{_name}-kword = %{koffice_epoch}:%{version}
Requires:	%{_name}-common-i18n = %{epoch}:%{version}-%{release}

%description -n koffice-kword-i18n
Internationalization and localization files for kword.

%description -n koffice-kword-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kworda.

%prep
%setup -q -c -T -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
kde_libs_htmldir="%{_kdedocdir}"; export kde_libs_htmldir

LDFLAGS="%{rpmldflags}"
#export UNSERMAKE=%{_datadir}/unsermake/unsermake

for dir in koffice-l10n-*-%{version}; do
	cd "$dir"
	%configure
	%{__make} \
		RPM_OPT_FLAGS="%{rpmcflags}" \
		kde_htmldir="%{_kdedocdir}" \
		kde_libs_htmldir="%{_kdedocdir}"
	cd ..
done

%install
rm -rf $RPM_BUILD_ROOT
rm -rf *.lang

for dir in koffice-l10n-*-%{version}; do
	cd "$dir"
	%{__make} -j1 install \
		DESTDIR=$RPM_BUILD_ROOT \
		kde_htmldir="%{_kdedocdir}" \
		kde_libs_htmldir="%{_kdedocdir}"
	cd ..
done

ziew="example \
graphite \
kdatabase \
kdgantt \
kplato"

for i in $ziew ;
do
	rm -rf `find $RPM_BUILD_ROOT -name ${i}\*\.mo`
	rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/${i}
done

%find_lang karbon		--with-kde
%find_lang kchart		--with-kde
%find_lang kexi			--with-kde
%find_lang kformula		--with-kde
%find_lang kivio		--with-kde
%find_lang koffice		--with-kde
%find_lang koshell		--with-kde
cat koshell.lang >> koffice.lang
%find_lang kugar		--with-kde
%find_lang kpresenter		--with-kde
%find_lang krita		--with-kde
%find_lang kspread		--with-kde
%find_lang kword		--with-kde
%find_lang thesaurus		--with-kde
cat thesaurus.lang >> kword.lang

kexi="kformdesigner"
for i in $kexi;
do
	%find_lang $i --with-kde
	cat ${i}.lang >> kexi.lang
done

plikez="desktop_koffice \
kfile_koffice \
kfile_ooo \
koconverter \
kofficefilters \
kounavail \
kscan_plugin \
kscreenshot_plugin"

for i in $plikez;
do
	%find_lang $i --with-kde
	cat ${i}.lang >> koffice.lang
done

kspread="kspreadcalc_calc \
kspreadinsertcalendar"

for i in $kspread;
do
	%find_lang $i --with-kde
	cat ${i}.lang >> kspread.lang
done

kword="kthesaurus \
thesaurus_tool"

for i in $kword;
do
	%find_lang $i --with-kde
	cat ${i}.lang >> kword.lang
done

for i in $RPM_BUILD_ROOT%{_datadir}/apps/koffice/autocorrect/*.xml
do
	z=`echo ${i}|sed -e "s|$RPM_BUILD_ROOT%{_datadir}/apps/koffice/autocorrect/||g" -e 's|\.xml||g'`
	echo "%lang(${z}) %{_datadir}/apps/koffice/autocorrect/${z}.xml" >> koffice.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -n koffice-common-i18n	-f koffice.lang
%defattr(644,root,root,755)
%files -n koffice-karbon-i18n	-f karbon.lang
%defattr(644,root,root,755)
%files -n koffice-kchart-i18n	-f kchart.lang
%defattr(644,root,root,755)
%files -n koffice-kexi-i18n	-f kexi.lang
%defattr(644,root,root,755)
%files -n koffice-kformula-i18n	-f kformula.lang
%defattr(644,root,root,755)
%files -n koffice-kivio-i18n	-f kivio.lang
%defattr(644,root,root,755)
%files -n koffice-kpresenter-i18n	-f kpresenter.lang
%defattr(644,root,root,755)
%files -n koffice-krita-i18n	-f krita.lang
%defattr(644,root,root,755)
%files -n koffice-kspread-i18n	-f kspread.lang
%defattr(644,root,root,755)
%files -n koffice-kugar-i18n	-f kugar.lang
%defattr(644,root,root,755)
%files -n koffice-kword-i18n	-f kword.lang
%defattr(644,root,root,755)
