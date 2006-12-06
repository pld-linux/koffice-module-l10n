# TODO:
# - missing obsoletes -- which ones??
%define		_name		koffice
%define		koffice_epoch	5
%define		kdelibs_epoch	9
Summary:	Koffice per package i18n files
Summary(pl):	Tłumaczenia Koffice podzielone wg. pakietów
Name:		%{_name}-module-l10n
Version:	1.6.1
Release:	1
Epoch:		5
License:	GPL
Group:		X11/Applications
URL:		http://i18n.kde.org/
#Source0:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-bg-%{version}.tar.bz2
##Source0-md5:	8daaeb614b3439490c2dd64a5ca6a90d
Source1:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ca-%{version}.tar.bz2
# Source1-md5:	2af9ee48900b76f13c7b205f9f44e454
Source2:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-cs-%{version}.tar.bz2
# Source2-md5:	a90d191f1d84bd5c8090ca6e004253c4
Source3:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-cy-%{version}.tar.bz2
# Source3-md5:	4f5d6aef468aeb4b80c6b079e1399110
Source4:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-da-%{version}.tar.bz2
# Source4-md5:	34ac13ce5bf8452f5f8b44686d03781a
Source5:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-de-%{version}.tar.bz2
# Source5-md5:	9ec1030ec8f55b4689a4664a3032050d
Source6:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-el-%{version}.tar.bz2
# Source6-md5:	c2028907c0675534694b5bad4c85ac0f
Source7:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-en_GB-%{version}.tar.bz2
# Source7-md5:	0c8edcc2fb6570ff7629e610580cac2f
Source8:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-es-%{version}.tar.bz2
# Source8-md5:	e3095320b087fdbaf9dea4ca7384c4e7
Source9:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-et-%{version}.tar.bz2
# Source9-md5:	d7e32d741c284880ff01530d956cd524
Source28:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-eu-%{version}.tar.bz2
# Source28-md5:	33bb005893d82eeebbc1dc62495e018a
Source10:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-fi-%{version}.tar.bz2
# Source10-md5:	dc0b99fe0b1c2f0bdc5823804cf5f7f7
Source11:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-fr-%{version}.tar.bz2
# Source11-md5:	74a658f3f323f016b202cc4e2063da19
Source12:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-hu-%{version}.tar.bz2
# Source12-md5:	406eef87386bea965c9d0ec224b0a6aa
Source13:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-it-%{version}.tar.bz2
# Source13-md5:	5fc389a6885af2acce7e5b9b48a9ce12
Source29:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ja-%{version}.tar.bz2
# Source29-md5:	39ba5b3618221ee6fa896aa16aa9f6a9
Source30:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-lv-%{version}.tar.bz2
# Source30-md5:	512650fbc0638ac0f0bae2864f295cca
Source31:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ms-%{version}.tar.bz2
# Source31-md5:	ff1d6abe79bf4b4239ebaccc2509c35e
Source14:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-nb-%{version}.tar.bz2
# Source14-md5:	65d3a4d15e8911faf43d1aa9c6f7b6a7
Source15:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-nl-%{version}.tar.bz2
# Source15-md5:	006bc0ff8b292fc8836c989d244a45bc
#Source16:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-nn-%{version}.tar.bz2
##Source16-md5:	12a451ca1384c776045a86aa3f0fecb5
Source17:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-pl-%{version}.tar.bz2
# Source17-md5:	ca6e0bd7de872e51f342cd153598981b
Source18:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-pt-%{version}.tar.bz2
# Source18-md5:	c4e59783b4b93a50c7e5e9b53c864caa
Source19:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-pt_BR-%{version}.tar.bz2
# Source19-md5:	71efdf80a256b20baece5e58f2d4527a
Source20:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ru-%{version}.tar.bz2
# Source20-md5:	d72bb7ce7fe685c4c92940dca4cf4bf8
Source32:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sk-%{version}.tar.bz2
# Source32-md5:	63b2d698040b2f5ece72e7ca67407669
Source21:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sl-%{version}.tar.bz2
# Source21-md5:	0c40d723b64bf15fbb8c78ebce17dcb3
Source22:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sr-%{version}.tar.bz2
# Source22-md5:	ff1137b214460cfc6c647643da08e098
Source23:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sr@Latn-%{version}.tar.bz2
# Source23-md5:	ed4eab803a7c0443ff3c4839e32757d1
Source24:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sv-%{version}.tar.bz2
# Source24-md5:	fd5ebf8d8480797f84121f9efcb00823
#Source25:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ta-%{version}.tar.bz2
##Source25-md5:	536e66f3b85923771f2af964b51a465e
#Source26:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-tg-%{version}.tar.bz2
##Source26-md5:	a38ec98b0f6437ddb93196f369a09485
Source33:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-tr-%{version}.tar.bz2
# Source33-md5:	909ed845836e7219a4cf6710ee128846
Source27:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-zh_CN-%{version}.tar.bz2
# Source27-md5:	055cf1eed59bc1e491063d4ffa883d9b
Source34:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-zh_TW-%{version}.tar.bz2
# Source34-md5:	230b02b893873f1fd55f002509549793
BuildRequires:	kdelibs >= %{kdelibs_epoch}:%{version}
BuildRequires:	kdelibs-devel
BuildRequires:	libxml2-progs >= 2.4.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KOffice - international support.

%description -l pl
KOffice - wsparcie dla wielu języków.

%package -n koffice-common-l10n
Summary:	Internationalization and localization files for koffice-common
Summary(pl):	Pliki umiędzynarodawiające dla koffice-common
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
Pliki umiędzynarodawiające dla koffice-common.

%package -n koffice-karbon-l10n
Summary:	Internationalization and localization files for karbon
Summary(pl):	Pliki umiędzynarodawiające dla karbona
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-karbon = %{koffice_epoch}:%{version}

%description -n koffice-karbon-l10n
Internationalization and localization files for karbon.

%description -n koffice-karbon-l10n -l pl
Pliki umiędzynarodawiające dla karbon.

%package -n koffice-kchart-l10n
Summary:	Internationalization and localization files for kchart
Summary(pl):	Pliki umiędzynarodawiające dla kcharta
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kchart = %{koffice_epoch}:%{version}

%description -n koffice-kchart-l10n
Internationalization and localization files for kchart.

%description -n koffice-kchart-l10n -l pl
Pliki umiędzynarodawiające dla kcharta.

%package -n koffice-kexi-l10n
Summary:	Internationalization and localization files for kexi
Summary(pl):	Pliki umiędzynarodawiające dla kexi
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kexi = %{koffice_epoch}:%{version}

%description -n koffice-kexi-l10n
Internationalization and localization files for kexi.

%description -n koffice-kexi-l10n -l pl
Pliki umiędzynarodawiające dla kexi.

%package -n koffice-kformula-l10n
Summary:	Internationalization and localization files for kformula
Summary(pl):	Pliki umiędzynarodawiające dla kformuli
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kformula = %{koffice_epoch}:%{version}

%description -n koffice-kformula-l10n
Internationalization and localization files for kformula.

%description -n koffice-kformula-l10n -l pl
Pliki umiędzynarodawiające dla kformuli.

%package -n koffice-kivio-l10n
Summary:	Internationalization and localization files for kivio
Summary(pl):	Pliki umiędzynarodawiające dla kivio
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kivio = %{koffice_epoch}:%{version}

%description -n koffice-kivio-l10n
Internationalization and localization files for kivio.

%description -n koffice-kivio-l10n -l pl
Pliki umiędzynarodawiające dla kivio.

%package -n koffice-kpresenter-l10n
Summary:	Internationalization and localization files for kpresenter
Summary(pl):	Pliki umiędzynarodawiające dla kpresentera
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kpresenter = %{koffice_epoch}:%{version}

%description -n koffice-kpresenter-l10n
Internationalization and localization files for kpresenter.

%description -n koffice-kpresenter-l10n -l pl
Pliki umiędzynarodawiające dla kpresentera.

%package -n koffice-krita-l10n
Summary:	Internationalization and localization files for krita
Summary(pl):	Pliki umiędzynarodawiające dla krita
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-krita = %{koffice_epoch}:%{version}

%description -n koffice-krita-l10n
Internationalization and localization files for krita.

%description -n koffice-krita-l10n -l pl
Pliki umiędzynarodawiające dla krita.

%package -n koffice-kspread-l10n
Summary:	Internationalization and localization files for kspread
Summary(pl):	Pliki umiędzynarodawiające dla kspreada
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kspread = %{koffice_epoch}:%{version}

%description -n koffice-kspread-l10n
Internationalization and localization files for kspread.

%description -n koffice-kspread-l10n -l pl
Pliki umiędzynarodawiające dla kspreada.

%package -n koffice-kugar-l10n
Summary:	Internationalization and localization files for kugar
Summary(pl):	Pliki umiędzynarodawiające dla kugara
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kugar = %{koffice_epoch}:%{version}

%description -n koffice-kugar-l10n
Internationalization and localization files for kugar.

%description -n koffice-kugar-l10n -l pl
Pliki umiędzynarodawiające dla kugara.

%package -n koffice-kword-l10n
Summary:	Internationalization and localization files for kword
Summary(pl):	Pliki umiędzynarodawiające dla kworda
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kword = %{koffice_epoch}:%{version}

%description -n koffice-kword-l10n
Internationalization and localization files for kword.

%description -n koffice-kword-l10n -l pl
Pliki umiędzynarodawiające dla kworda.

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
	rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/*/${i}
done

%find_lang karbon		--with-kde
%find_lang kchart		--with-kde
%find_lang kexi			--with-kde
%find_lang kformula		--with-kde
%find_lang kivio		--with-kde
%find_lang kugar		--with-kde
%find_lang kpresenter	--with-kde
%find_lang krita		--with-kde
%find_lang kspread		--with-kde
%find_lang kword		--with-kde
%find_lang thesaurus	--with-kde
cat thesaurus.lang >> kword.lang
rm -f thesaurus.lang

kexi="kformdesigner"
for i in $kexi; do
	%find_lang $i --with-kde
	cat $i.lang >> kexi.lang
	rm -f $i.lang
done

plikez="\
desktop_koffice \
kfile_koffice \
kfile_ooo \
kfile_abiword \
kfile_gnumeric \
koconverter \
kofficefilters \
kounavail \
koproperty \
kscan_plugin \
kscreenshot_plugin \
koffice	\
koshell	\
"

for i in $plikez; do
	%find_lang $i --with-kde
	cat $i.lang >> common.lang
	rm -f $i.lang
done

kspread="\
kspreadcalc_calc \
kspreadinsertcalendar \
"

for i in $kspread; do
	%find_lang $i --with-kde
	cat $i.lang >> kspread.lang
	rm -f $i.lang
done

kword="\
kthesaurus \
thesaurus_tool \
"

for i in $kword; do
	%find_lang $i --with-kde
	cat $i.lang >> kword.lang
	rm -f $i.lang
done

for a in $RPM_BUILD_ROOT%{_datadir}/apps/koffice/autocorrect/*.xml; do
	t=${a##*autocorrect/}
	lang=${t%.xml}
	path=${a#$RPM_BUILD_ROOT}
	echo "%lang($lang) $path" >> common.lang
done

%clean
check_installed_files() {
	errors=0
	for a in *.lang; do
		pkg=${a%%.lang}

		rpmfile=%{_rpmdir}/%{_name}-$pkg-l10n-%{version}-%{release}.%{_target_cpu}.rpm
		if [ ! -f $rpmfile ]; then
			echo >&2 "Missing %%files section for $pkg"
			errors=1
		fi
	done
	if [ $errors -ne 0 ]; then
		exit 1
	fi
}
check_installed_files

rm -rf $RPM_BUILD_ROOT

%files -n koffice-common-l10n	-f common.lang
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
