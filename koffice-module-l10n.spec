%define		_name		koffice
%define		koffice_epoch	5
%define		kdelibs_epoch	9
Summary:	Koffice per package i18n files
Summary(pl):	T³umaczenia Koffice podzielone wg. pakietów
Name:		%{_name}-module-i18n
Version:	1.3.4
Release:	6
Epoch:		5
Group:		X11/Applications
License:	GPL
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{_name}-%{version}/src/%{_name}-i18n-%{version}.tar.bz2
# Source0-md5:	6455f496f6031e810398ad6b065eb929
# Source0-size:	27798685
URL:		http://i18n.kde.org/
BuildRequires:	kdelibs >= %{kdelibs_epoch}:%{version}
BuildRequires:	kdelibs-devel
BuildRequires:	libxml2-progs >= 2.4.2
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
%setup -q -n %{_name}-i18n

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
kde_libs_htmldir="%{_kdedocdir}"; export kde_libs_htmldir

LDFLAGS="%{rpmldflags}"
#export UNSERMAKE=%{_datadir}/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure
%{__make} \
	RPM_OPT_FLAGS="%{rpmcflags}" \
	kde_htmldir="%{_kdedocdir}" \
	kde_libs_htmldir="%{_kdedocdir}"

%install
rm -rf $RPM_BUILD_ROOT
rm -rf *.lang

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}" \
	kde_libs_htmldir="%{_kdedocdir}"

# rename ven -> ve
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/ve{n,}

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
