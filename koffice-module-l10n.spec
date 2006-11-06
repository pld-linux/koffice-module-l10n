# TODO:
# - missing obsoletes
# - finish install and files
# - unpackaged files list: http://glen.alkohol.ee/pld/koffice-module-l10n.txt

%define		_name		koffice
%define		koffice_epoch	5
%define		kdelibs_epoch	9
Summary:	Koffice per package i18n files
Summary(pl):	T³umaczenia Koffice podzielone wg. pakietów
Name:		%{_name}-module-l10n
Version:	1.6.0
Release:	0.1
Epoch:		5
License:	GPL
Group:		X11/Applications
URL:		http://i18n.kde.org/
#Source0:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-bg-%{version}.tar.bz2
##Source0-md5:	8daaeb614b3439490c2dd64a5ca6a90d
Source1:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ca-%{version}.tar.bz2
# Source1-md5:	b90e14bd3508bcc030096496ea87683a
Source2:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-cs-%{version}.tar.bz2
# Source2-md5:	21f9a7c3daf57aabf70111dded8a26a6
Source3:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-cy-%{version}.tar.bz2
# Source3-md5:	b1d03624474b91becd3ff64647f45087
Source4:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-da-%{version}.tar.bz2
# Source4-md5:	d1532dc1107f01752a9eeeb362666289
Source5:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-de-%{version}.tar.bz2
# Source5-md5:	21344257dcd9b418898fb5e348918171
Source6:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-el-%{version}.tar.bz2
# Source6-md5:	c00bbbf55de2d5d8aa68916ef6618ee3
Source7:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-en_GB-%{version}.tar.bz2
# Source7-md5:	eb4582f359eaada24a1dd96443636219
Source8:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-es-%{version}.tar.bz2
# Source8-md5:	81db059841e59cfee6371d10b12e82d7
Source9:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-et-%{version}.tar.bz2
# Source9-md5:	64b4dd81d61362599af0882d695dd175
Source28:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-eu-%{version}.tar.bz2
# Source28-md5:	c3c5dbfe0135896c41f749ff79c6744e
Source10:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-fi-%{version}.tar.bz2
# Source10-md5:	738bf409e16c08018b75f672abcb94a4
Source11:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-fr-%{version}.tar.bz2
# Source11-md5:	96a5871374f69c694be87e621f04f39e
Source12:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-hu-%{version}.tar.bz2
# Source12-md5:	01ea831cfbd136fecb1c7de8826e97b9
Source13:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-it-%{version}.tar.bz2
# Source13-md5:	73f17287697e54e61237a8cf7f6fc75f
Source29:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ja-%{version}.tar.bz2
# Source29-md5:	dd3f979c03f9bc4ae6393a54766b4a84
Source30:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-lv-%{version}.tar.bz2
# Source30-md5:	af51669631e18feef464e8d6778a41ad
Source31:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ms-%{version}.tar.bz2
# Source31-md5:	259be59d9bfe0e7fba7d96c1b5740614
Source14:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-nb-%{version}.tar.bz2
# Source14-md5:	ef631712fe58e8129823b0f53253e153
Source15:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-nl-%{version}.tar.bz2
# Source15-md5:	b9c572b04701226fdce5e9ae5817177c
#Source16:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-nn-%{version}.tar.bz2
##Source16-md5:	12a451ca1384c776045a86aa3f0fecb5
Source17:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-pl-%{version}.tar.bz2
# Source17-md5:	aaa167a7881f383b88696d34fd1903a5
Source18:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-pt-%{version}.tar.bz2
# Source18-md5:	c907923d13d2e2d15e09ac5be9259c96
Source19:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-pt_BR-%{version}.tar.bz2
# Source19-md5:	8d1be2180acdba3287c2936cc379b4c6
Source20:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ru-%{version}.tar.bz2
# Source20-md5:	0b895c8a86f0b3c6f31903c906e0dd08
Source32:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sk-%{version}.tar.bz2
# Source32-md5:	3bdbfb8532c3a3422345ff8693544b29
Source21:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sl-%{version}.tar.bz2
# Source21-md5:	6dfa4b30a8d246a46dddef1e3933cf36
Source22:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sr-%{version}.tar.bz2
# Source22-md5:	69681fe0a95a61b88aa5b9ee226fc320
Source23:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sr@Latn-%{version}.tar.bz2
# Source23-md5:	8ce2f6edd23a43b079fbec9c20cfe516
Source24:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sv-%{version}.tar.bz2
# Source24-md5:	774efb0a9c02776c58ca6cfe1930d327
#Source25:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ta-%{version}.tar.bz2
##Source25-md5:	536e66f3b85923771f2af964b51a465e
#Source26:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-tg-%{version}.tar.bz2
##Source26-md5:	a38ec98b0f6437ddb93196f369a09485
Source33:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-tr-%{version}.tar.bz2
# Source33-md5:	d941eddab83cc8991d4f218854d25f64
Source27:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-zh_CN-%{version}.tar.bz2
# Source27-md5:	a3fda356e170368d7fd88d0ce892307b
Source34:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-zh_TW-%{version}.tar.bz2
# Source34-md5:	17ec8363abee3dd45c1a4c103b023ff3
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

%package -n koffice-common-l10n
Summary:	Internationalization and localization files for koffice-common
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla koffice-common
Group:		X11/Applications
Requires:	%{_name}-common = %{koffice_epoch}:%{version}
Requires:	kdebase-core-i18n
Obsoletes:	koffice-i18n-base
# and the languages
Obsoletes:	koffice-i18n-Afrikaans
Obsoletes:	koffice-i18n-Arabic
Obsoletes:	koffice-i18n-Azerbaijani
Obsoletes:	koffice-i18n-Basque
Obsoletes:	koffice-i18n-Basque
Obsoletes:	koffice-i18n-Bosnian
Obsoletes:	koffice-i18n-Brazil_Portuguese
Obsoletes:	koffice-i18n-Breton
Obsoletes:	koffice-i18n-Bulgarian
Obsoletes:	koffice-i18n-Catalan
Obsoletes:	koffice-i18n-Chinese
Obsoletes:	koffice-i18n-Croatian
Obsoletes:	koffice-i18n-Cymraeg
Obsoletes:	koffice-i18n-Czech
Obsoletes:	koffice-i18n-Danish
Obsoletes:	koffice-i18n-Dutch
Obsoletes:	koffice-i18n-English
Obsoletes:	koffice-i18n-English_UK
Obsoletes:	koffice-i18n-Esperanto
Obsoletes:	koffice-i18n-Estonian
Obsoletes:	koffice-i18n-Farsi
Obsoletes:	koffice-i18n-Finnish
Obsoletes:	koffice-i18n-French
Obsoletes:	koffice-i18n-Galician
Obsoletes:	koffice-i18n-Gascon_occitan
Obsoletes:	koffice-i18n-German
Obsoletes:	koffice-i18n-Greek
Obsoletes:	koffice-i18n-Hebrew
Obsoletes:	koffice-i18n-Hindi
Obsoletes:	koffice-i18n-Hungarian
Obsoletes:	koffice-i18n-Icelandic
Obsoletes:	koffice-i18n-Indonesian
Obsoletes:	koffice-i18n-Irish
Obsoletes:	koffice-i18n-Italian
Obsoletes:	koffice-i18n-Japanese
Obsoletes:	koffice-i18n-Korean
Obsoletes:	koffice-i18n-Lao
Obsoletes:	koffice-i18n-Latvian
Obsoletes:	koffice-i18n-Lithuanian
Obsoletes:	koffice-i18n-Macedonian
Obsoletes:	koffice-i18n-Malay
Obsoletes:	koffice-i18n-Maltese
Obsoletes:	koffice-i18n-Maori
Obsoletes:	koffice-i18n-Mongolian
Obsoletes:	koffice-i18n-Northern_Sami
Obsoletes:	koffice-i18n-Northern_Sotho
Obsoletes:	koffice-i18n-Norwegian_Bokmaal
Obsoletes:	koffice-i18n-Norwegian_Nynorsk
Obsoletes:	koffice-i18n-Polish
Obsoletes:	koffice-i18n-Portuguese
Obsoletes:	koffice-i18n-Romanian
Obsoletes:	koffice-i18n-Russian
Obsoletes:	koffice-i18n-Serbian
Obsoletes:	koffice-i18n-Simplified_Chinese
Obsoletes:	koffice-i18n-Slovak
Obsoletes:	koffice-i18n-Slovenian
Obsoletes:	koffice-i18n-Spanish
Obsoletes:	koffice-i18n-Swati
Obsoletes:	koffice-i18n-Swedish
Obsoletes:	koffice-i18n-Tajik
Obsoletes:	koffice-i18n-Tamil
Obsoletes:	koffice-i18n-Thai
Obsoletes:	koffice-i18n-Turkish
Obsoletes:	koffice-i18n-Ukrainian
Obsoletes:	koffice-i18n-Upper_Sorbian
Obsoletes:	koffice-i18n-Uzbek
Obsoletes:	koffice-i18n-Venda
Obsoletes:	koffice-i18n-Vietnamese
Obsoletes:	koffice-i18n-Walloon
Obsoletes:	koffice-i18n-Xhosa
Obsoletes:	koffice-i18n-Zulu

%description -n koffice-common-l10n
Internationalization and localization files for koffice-common.

%description -n koffice-common-l10n -l pl
Pliki umiêdzynarodawiaj±ce dla koffice-common.

%package -n koffice-karbon-l10n
Summary:	Internationalization and localization files for karbon
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla karbona
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-karbon = %{koffice_epoch}:%{version}

%description -n koffice-karbon-l10n
Internationalization and localization files for karbon.

%description -n koffice-karbon-l10n -l pl
Pliki umiêdzynarodawiaj±ce dla karbon.

%package -n koffice-kchart-l10n
Summary:	Internationalization and localization files for kchart
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcharta
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kchart = %{koffice_epoch}:%{version}

%description -n koffice-kchart-l10n
Internationalization and localization files for kchart.

%description -n koffice-kchart-l10n -l pl
Pliki umiêdzynarodawiaj±ce dla kcharta.

%package -n koffice-kexi-l10n
Summary:	Internationalization and localization files for kexi
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kexi
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kexi = %{koffice_epoch}:%{version}

%description -n koffice-kexi-l10n
Internationalization and localization files for kexi.

%description -n koffice-kexi-l10n -l pl
Pliki umiêdzynarodawiaj±ce dla kexi.

%package -n koffice-kformula-l10n
Summary:	Internationalization and localization files for kformula
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kformuli
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kformula = %{koffice_epoch}:%{version}

%description -n koffice-kformula-l10n
Internationalization and localization files for kformula.

%description -n koffice-kformula-l10n -l pl
Pliki umiêdzynarodawiaj±ce dla kformuli.

%package -n koffice-kivio-l10n
Summary:	Internationalization and localization files for kivio
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kivio
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kivio = %{koffice_epoch}:%{version}

%description -n koffice-kivio-l10n
Internationalization and localization files for kivio.

%description -n koffice-kivio-l10n -l pl
Pliki umiêdzynarodawiaj±ce dla kivio.

%package -n koffice-kpresenter-l10n
Summary:	Internationalization and localization files for kpresenter
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpresentera
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kpresenter = %{koffice_epoch}:%{version}

%description -n koffice-kpresenter-l10n
Internationalization and localization files for kpresenter.

%description -n koffice-kpresenter-l10n -l pl
Pliki umiêdzynarodawiaj±ce dla kpresentera.

%package -n koffice-krita-l10n
Summary:	Internationalization and localization files for krita
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla krita
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-krita = %{koffice_epoch}:%{version}

%description -n koffice-krita-l10n
Internationalization and localization files for krita.

%description -n koffice-krita-l10n -l pl
Pliki umiêdzynarodawiaj±ce dla krita.

%package -n koffice-kspread-l10n
Summary:	Internationalization and localization files for kspread
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kspreada
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kspread = %{koffice_epoch}:%{version}

%description -n koffice-kspread-l10n
Internationalization and localization files for kspread.

%description -n koffice-kspread-l10n -l pl
Pliki umiêdzynarodawiaj±ce dla kspreada.

%package -n koffice-kugar-l10n
Summary:	Internationalization and localization files for kugar
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kugara
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kugar = %{koffice_epoch}:%{version}

%description -n koffice-kugar-l10n
Internationalization and localization files for kugar.

%description -n koffice-kugar-l10n -l pl
Pliki umiêdzynarodawiaj±ce dla kugara.

%package -n koffice-kword-l10n
Summary:	Internationalization and localization files for kword
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kworda
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kword = %{koffice_epoch}:%{version}

%description -n koffice-kword-l10n
Internationalization and localization files for kword.

%description -n koffice-kword-l10n -l pl
Pliki umiêdzynarodawiaj±ce dla kworda.

%prep
%setup -q -c -T %(seq -f '-a %g' 1 34 | egrep -v '^-a (16|25|26)$' | xargs)

%build
# broken
rm -rf koffice-l10n-es-*

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
if [ ! -f installed.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf $RPM_BUILD_ROOT

	for dir in koffice-l10n-*-%{version}; do
		cd "$dir"
		%{__make} -j1 install \
			DESTDIR=$RPM_BUILD_ROOT \
			kde_htmldir="%{_kdedocdir}" \
			kde_libs_htmldir="%{_kdedocdir}"
		cd ..
	done

	# remove zero-length file
	find $RPM_BUILD_ROOT%{_kdedocdir} -size 0 -print0 | xargs -0 rm -vf

	# remove empty language catalogs (= 1 message only)
	find $RPM_BUILD_ROOT%{_datadir}/locale -type f -name '*.mo' | xargs file | egrep ', 1 messages$' | cut -d: -f1 | xargs rm -vf

	touch installed.stamp
fi

rm -f *.lang

ziew="\
example \
graphite \
kdatabase \
kdgantt \
kplato \
"

for i in $ziew; do
	rm -rf $(find $RPM_BUILD_ROOT -name "$i*.mo")
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
for i in $kexi; do
	%find_lang $i --with-kde
	cat ${i}.lang >> kexi.lang
done

plikez="\
desktop_koffice \
kfile_koffice \
kfile_ooo \
koconverter \
kofficefilters \
kounavail \
kscan_plugin \
kscreenshot_plugin \
"

for i in $plikez; do
	%find_lang $i --with-kde
	cat ${i}.lang >> koffice.lang
done

kspread="\
kspreadcalc_calc \
kspreadinsertcalendar \
"

for i in $kspread; do
	%find_lang $i --with-kde
	cat ${i}.lang >> kspread.lang
done

kword="\
kthesaurus \
thesaurus_tool \
"

for i in $kword; do
	%find_lang $i --with-kde
	cat ${i}.lang >> kword.lang
done

for i in $RPM_BUILD_ROOT%{_datadir}/apps/koffice/autocorrect/*.xml; do
	z=`echo ${i}|sed -e "s|$RPM_BUILD_ROOT%{_datadir}/apps/koffice/autocorrect/||g" -e 's|\.xml||g'`
	echo "%lang(${z}) %{_datadir}/apps/koffice/autocorrect/${z}.xml" >> koffice.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -n koffice-common-l10n	-f koffice.lang
%defattr(644,root,root,755)
%files -n koffice-karbon-l10n	-f karbon.lang
%defattr(644,root,root,755)
%files -n koffice-kchart-l10n	-f kchart.lang
%defattr(644,root,root,755)
%files -n koffice-kexi-l10n	-f kexi.lang
%defattr(644,root,root,755)
%files -n koffice-kformula-l10n	-f kformula.lang
%defattr(644,root,root,755)
%files -n koffice-kivio-l10n	-f kivio.lang
%defattr(644,root,root,755)
%files -n koffice-kpresenter-l10n	-f kpresenter.lang
%defattr(644,root,root,755)
%files -n koffice-krita-l10n	-f krita.lang
%defattr(644,root,root,755)
%files -n koffice-kspread-l10n	-f kspread.lang
%defattr(644,root,root,755)
%files -n koffice-kugar-l10n	-f kugar.lang
%defattr(644,root,root,755)
%files -n koffice-kword-l10n	-f kword.lang
%defattr(644,root,root,755)
