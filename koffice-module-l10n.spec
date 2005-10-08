# TODO:
# - missing obsoletes
# - finish install and files

%define		_name		koffice
%define		koffice_epoch	5
%define		kdelibs_epoch	9
Summary:	Koffice per package i18n files
Summary(pl):	T³umaczenia Koffice podzielone wg. pakietów
Name:		%{_name}-module-l10n
Version:	1.4.1
Release:	0.1
Epoch:		5
Group:		X11/Applications
License:	GPL
Source0:        ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-bg-%{version}.tar.bz2
# Source0-md5:  445f35bf43b60c7799df116bd90957ad
Source1:        ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ca-%{version}.tar.bz2
# Source1-md5:  f011aa527e4b476f18f1fda9a043f81b
Source2:        ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-cs-%{version}.tar.bz2
# Source2-md5:  8b56e381765bece8a32fec3b67e881c2
Source3:        ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-cy-%{version}.tar.bz2
# Source3-md5:  e15377d70faef67a91a361b421b8be84
Source4:        ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-da-%{version}.tar.bz2
# Source4-md5:  3bcda6ccf32a2b0916f5de47981be655
Source5:        ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-de-%{version}.tar.bz2
# Source5-md5:  b54a04db280a5b00f0105407c24ce49c
Source6:        ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-el-%{version}.tar.bz2
# Source6-md5:  a744de5d6e97a25257a809f7a0f79a11
Source7:        ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-en_GB-%{version}.tar.bz2
# Source7-md5:  deaaf836cce7efcd9c83d800a6b4e51b
Source8:        ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-es-%{version}.tar.bz2
# Source8-md5:  3872dfdfb6b12532218daf8f61f94282
Source9:        ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-et-%{version}.tar.bz2
# Source9-md5:  0ecd275357b76d245b2367a1925bda59
Source10:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-fi-%{version}.tar.bz2
# Source10-md5: a2e26094907dc77365266c215183c587
Source11:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-fr-%{version}.tar.bz2
# Source11-md5: 37a18640975a8a1ba38044a6ea7dbd37
Source12:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-hu-%{version}.tar.bz2
# Source12-md5: 95e046ab8097fda8b4f146b4a625b7a3
Source13:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-it-%{version}.tar.bz2
# Source13-md5: cac43b60ea3d01cfa0ac337bc0a296be
Source14:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-nb-%{version}.tar.bz2
# Source14-md5: 0d9c12a3881861377130801a3a431dd2
Source15:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-nl-%{version}.tar.bz2
# Source15-md5: a960e30b5bd883ed71ada339f238bb38
Source16:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-nn-%{version}.tar.bz2
# Source16-md5: 7e55ada0f26bc0125ae26ab7c7b1eae2
Source17:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-pl-%{version}.tar.bz2
# Source17-md5: c6c38ec4a42d2c2abd289b83e2398c21
Source18:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-pt-%{version}.tar.bz2
# Source18-md5: af2c79e0694d913a749a9591598641c5
Source19:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-pt_BR-%{version}.tar.bz2
# Source19-md5: 96f2a0ba7a249078e64ea319b8f27dc9
Source20:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ru-%{version}.tar.bz2
# Source20-md5: d198b6cc3574ea9305701a48324085bb
Source21:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sl-%{version}.tar.bz2
# Source21-md5: 3c27784f5630ca6f3b0cfbae89271176
Source22:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sr-%{version}.tar.bz2
# Source22-md5: f49d2141aa8bd2c68f0ab892cdc4e1a8
Source23:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sr@Latn-%{version}.tar.bz2
# Source23-md5: 41fecc81a0bfbce8eaf5f40e978be3fe
Source24:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sv-%{version}.tar.bz2
# Source24-md5: 58ffb4991e48caa73f434f30ca2b4761
Source25:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ta-%{version}.tar.bz2
# Source25-md5: 43e954db7f2af6f4c4f34a85a31e33d2
Source26:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-tg-%{version}.tar.bz2
# Source26-md5: 2e35a578c8afb853ef5c23e71c2d575e
Source27:       ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-zh_CN-%{version}.tar.bz2
# Source27-md5: 02491c50d888600dccd1685a9ef7ed6c
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
%setup -q -c -T -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27

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
kexi \
kformdesigner \
kontour \
kplato \
krita"

for i in $ziew ;
do
	rm -rf `find $RPM_BUILD_ROOT -name ${i}\*\.mo`
	rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/${i}
done

%find_lang kchart		--with-kde
%find_lang kformula		--with-kde
%find_lang kivio		--with-kde
%find_lang koffice		--with-kde
%find_lang koshell		--with-kde
cat koshell.lang >> koffice.lang
%find_lang kugar		--with-kde
%find_lang kpresenter		--with-kde
%find_lang kspread		--with-kde
%find_lang kword		--with-kde
%find_lang thesaurus		--with-kde
cat thesaurus.lang >> kword.lang

plikez="desktop_koffice \
xsltexportfilter \
kfile_koffice \
kfile_ooo \
koconverter \
kocryptfilter \
kounavail \
kscan_plugin \
xsltimportfilter \
xsltfilter"

for i in $plikez;
do
	%find_lang $i --with-kde
	cat ${i}.lang >> koffice.lang
done

%find_lang karbon --with-kde
%find_lang karbonepsfilter --with-kde
cat karbonepsfilter.lang >> karbon.lang
%find_lang kudesigner --with-kde
cat kudesigner.lang >> karbon.lang

kform="kformulalatexfilter \
kformulamathmlfilter \
kformulapngfilter \
kformulalib"

for i in $kform;
do
	%find_lang $i --with-kde
	cat ${i}.lang >> kformula.lang
done

%find_lang kpresenterkwordfilter --with-kde
cat kpresenterkwordfilter.lang >> kpresenter.lang

kspread="csvfilter \
kspreadcalc_calc \
kspreaddbasefilter \
kspreadexcelimportfilter \
kspreadlatexexportfilter \
kspreadopencalcfilter \
kspreadqprofilter"

for i in $kspread;
do
	%find_lang $i --with-kde
	cat ${i}.lang >> kspread.lang
done

kword="kthesaurus \
kwordabiwordfilter \
kwordasciifilter \
kwordhtmlexportfilter \
kwordhtmlimportfilter \
kwordlatexexportfilter \
kwordlatexfilter \
kwordlateximportfilter \
kwordmswordfilter \
kwordmswritefilter \
kwordoowriterfilter \
kwordpdfimport \
olefilterswinword97filter \
thesaurus_tool \
kwordhtmlfilter"

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
%files -n koffice-kformula-i18n	-f kformula.lang
%defattr(644,root,root,755)
%files -n koffice-kivio-i18n	-f kivio.lang
%defattr(644,root,root,755)
%files -n koffice-kpresenter-i18n	-f kpresenter.lang
%defattr(644,root,root,755)
%files -n koffice-kspread-i18n	-f kspread.lang
%defattr(644,root,root,755)
%files -n koffice-kugar-i18n	-f kugar.lang
%defattr(644,root,root,755)
%files -n koffice-kword-i18n	-f kword.lang
%defattr(644,root,root,755)
