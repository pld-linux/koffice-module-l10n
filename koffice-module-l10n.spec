%define		_name		koffice
%define		koffice_epoch	5
%define		kdelibs_epoch	9
Summary:	Koffice per package i18n files
Summary(pl.UTF-8):	Tłumaczenia Koffice podzielone wg. pakietów
Name:		%{_name}-module-l10n
Version:	1.6.3
Release:	2
Epoch:		5
License:	GPL
Group:		X11/Applications
URL:		http://i18n.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-bg-%{version}.tar.bz2
# Source0-md5:	da3167fc536f51d8e32998ae203cd4b9
Source1:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ca-%{version}.tar.bz2
# Source1-md5:	5ec6aa3c1c613466a545e26bdb9dfd72
Source2:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-cs-%{version}.tar.bz2
# Source2-md5:	d893774830fa05b2450018ae70fcd267
Source3:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-cy-%{version}.tar.bz2
# Source3-md5:	6a100e050c3e6ae95733b24ce4d4f4cf
Source4:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-da-%{version}.tar.bz2
# Source4-md5:	fa9c878f7672d1b9881722f93a1dc1ce
Source5:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-de-%{version}.tar.bz2
# Source5-md5:	9153728550bc6101094bac42aefb7663
Source6:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-el-%{version}.tar.bz2
# Source6-md5:	be97b80ccaa0da028d8d04f263be5fed
Source7:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-en_GB-%{version}.tar.bz2
# Source7-md5:	468c3ac77b57de10e1cb7c99d184a443
Source8:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-es-%{version}.tar.bz2
# Source8-md5:	23f246f5bc86f8831e595f98c24c154e
Source9:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-et-%{version}.tar.bz2
# Source9-md5:	fdc1c81ae65bec5f7e56d76bcdbaa1af
Source10:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-eu-%{version}.tar.bz2
# Source10-md5:	3ca81163f7242bcad450342e1105ad89
Source11:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-fa-%{version}.tar.bz2
# Source11-md5:	63f5d0570660e47455e8ccd1a8c4bf02
Source12:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-fi-%{version}.tar.bz2
# Source12-md5:	98b3b306061c127b92d9e73d3641f687
Source13:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-fr-%{version}.tar.bz2
# Source13-md5:	01219310196ac9c8325c3d8c7456bcb3
Source14:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ga-%{version}.tar.bz2
# Source14-md5:	80f28f345dbae9b108b97701ab2a3b7b
Source15:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-gl-%{version}.tar.bz2
# Source15-md5:	84b9c65886a99599d99c7ea077875a88
Source16:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-hu-%{version}.tar.bz2
# Source16-md5:	088e5c503a9dedfa8d23a3fa11f596ca
Source17:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-it-%{version}.tar.bz2
# Source17-md5:	1aa3d67279e63f7c7919908c686f2281
Source18:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ja-%{version}.tar.bz2
# Source18-md5:	b0d886c7504a8b0bafb5095835e78c8a
Source19:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-km-%{version}.tar.bz2
# Source19-md5:	527e698b2907f90712239681f0ae0a9e
Source20:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-lv-%{version}.tar.bz2
# Source20-md5:	62386e1713216bd2709e1ce3fd150c8e
Source21:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ms-%{version}.tar.bz2
# Source21-md5:	1bf2fcf2c82464e038eed026eaa13fca
Source22:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-nb-%{version}.tar.bz2
# Source22-md5:	462ecb27a008482801ca3bd9e803b2d1
Source23:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-nds-%{version}.tar.bz2
# Source23-md5:	50702ef6c8d586e89280a2b42d2c5225
Source24:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ne-%{version}.tar.bz2
# Source24-md5:	bd95494b15f647dfcbe39d514811504a
Source25:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-nl-%{version}.tar.bz2
# Source25-md5:	a63c40510c0bb322dc1f6bb057759772
Source26:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-pl-%{version}.tar.bz2
# Source26-md5:	a174b73f3e2c0e579bf3775e481958dd
Source27:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-pt-%{version}.tar.bz2
# Source27-md5:	e74540534eae3d0b1cb4bbabf3da0ed0
Source28:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-pt_BR-%{version}.tar.bz2
# Source28-md5:	fe49fa2405b44044b69b5d1e2bcb15cf
Source29:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-ru-%{version}.tar.bz2
# Source29-md5:	e6be9bcea5e2b6e6aa4662f1530841ef
Source30:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sk-%{version}.tar.bz2
# Source30-md5:	aa49a6c5497dc201359c577ab77c8361
Source31:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sl-%{version}.tar.bz2
# Source31-md5:	18e3f2e81be91170fe551e4b47c2f907
Source32:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sr-%{version}.tar.bz2
# Source32-md5:	3eb97f2ef5f65b3637af397dca0d8fcb
Source33:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sr@Latn-%{version}.tar.bz2
# Source33-md5:	217064c12d6efe969a1bbdac2ef8aef0
Source34:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-sv-%{version}.tar.bz2
# Source34-md5:	c6c530010a64fb9e2880a3f33bb9276e
Source35:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-tr-%{version}.tar.bz2
# Source35-md5:	301f3a665f12d1b7f56fe9be93403812
Source36:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-uk-%{version}.tar.bz2
# Source36-md5:	f8a50375d4f280131a27e0bdfb0deb83
Source37:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-zh_CN-%{version}.tar.bz2
# Source37-md5:	a21490ebc1d0beedc565c070d4bdad25
Source38:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/koffice-l10n-zh_TW-%{version}.tar.bz2
# Source38-md5:	7c7c3787a45743ae9d06938829381d2e
BuildRequires:	kdelibs >= %{kdelibs_epoch}:%{version}
BuildRequires:	kdelibs-devel
BuildRequires:	libxml2-progs >= 2.4.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KOffice - international support.

%description -l pl.UTF-8
KOffice - wsparcie dla wielu języków.

%package -n koffice-common-l10n
Summary:	Internationalization and localization files for koffice-common
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla koffice-common
Group:		X11/Applications
Requires:	%{_name}-common = %{koffice_epoch}:%{version}
Requires:	kdebase-core-i18n
# Hint:
# grep ^%files koffice-l10n.spec | awk '{printf("Obsoletes:\tkoffice-l10n-%s\n", $NF)}' > out
# obsolete pkgs from koffice-l10.spec
Obsoletes:	koffice-l10n-Basque
Obsoletes:	koffice-l10n-Brazil_Portuguese
Obsoletes:	koffice-l10n-Bulgarian
Obsoletes:	koffice-l10n-Catalan
Obsoletes:	koffice-l10n-Chinese
Obsoletes:	koffice-l10n-Cymraeg
Obsoletes:	koffice-l10n-Czech
Obsoletes:	koffice-l10n-Danish
Obsoletes:	koffice-l10n-Dutch
Obsoletes:	koffice-l10n-English_UK
Obsoletes:	koffice-l10n-Estonian
Obsoletes:	koffice-l10n-Farsi
Obsoletes:	koffice-l10n-Finnish
Obsoletes:	koffice-l10n-French
Obsoletes:	koffice-l10n-Galician
Obsoletes:	koffice-l10n-German
Obsoletes:	koffice-l10n-Greek
Obsoletes:	koffice-l10n-Hungarian
Obsoletes:	koffice-l10n-Irish
Obsoletes:	koffice-l10n-Italian
Obsoletes:	koffice-l10n-Japanese
Obsoletes:	koffice-l10n-Khmer
Obsoletes:	koffice-l10n-Latvian
Obsoletes:	koffice-l10n-Low_Saxon
Obsoletes:	koffice-l10n-Malay
Obsoletes:	koffice-l10n-Nepali
Obsoletes:	koffice-l10n-Norwegian_Bokmaal
Obsoletes:	koffice-l10n-Polish
Obsoletes:	koffice-l10n-Portuguese
Obsoletes:	koffice-l10n-Russian
Obsoletes:	koffice-l10n-Serbian
Obsoletes:	koffice-l10n-Simplified_Chinese
Obsoletes:	koffice-l10n-Slovak
Obsoletes:	koffice-l10n-Slovenian
Obsoletes:	koffice-l10n-Spanish
Obsoletes:	koffice-l10n-Swedish
Obsoletes:	koffice-l10n-Turkish
Obsoletes:	koffice-l10n-Ukrainian
# obsolete pkgs when they were called i18n
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
Obsoletes:	koffice-i18n-Khmer
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
Obsoletes:	koffice-i18n-base

%description -n koffice-common-l10n
Internationalization and localization files for koffice-common.

%description -n koffice-common-l10n -l pl.UTF-8
Pliki umiędzynarodawiające dla koffice-common.

%package -n koffice-karbon-l10n
Summary:	Internationalization and localization files for karbon
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla karbona
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-karbon = %{koffice_epoch}:%{version}

%description -n koffice-karbon-l10n
Internationalization and localization files for karbon.

%description -n koffice-karbon-l10n -l pl.UTF-8
Pliki umiędzynarodawiające dla karbon.

%package -n koffice-kchart-l10n
Summary:	Internationalization and localization files for kchart
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kcharta
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kchart = %{koffice_epoch}:%{version}

%description -n koffice-kchart-l10n
Internationalization and localization files for kchart.

%description -n koffice-kchart-l10n -l pl.UTF-8
Pliki umiędzynarodawiające dla kcharta.

%package -n koffice-kexi-l10n
Summary:	Internationalization and localization files for kexi
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kexi
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kexi = %{koffice_epoch}:%{version}

%description -n koffice-kexi-l10n
Internationalization and localization files for kexi.

%description -n koffice-kexi-l10n -l pl.UTF-8
Pliki umiędzynarodawiające dla kexi.

%package -n koffice-kformula-l10n
Summary:	Internationalization and localization files for kformula
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kformuli
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kformula = %{koffice_epoch}:%{version}

%description -n koffice-kformula-l10n
Internationalization and localization files for kformula.

%description -n koffice-kformula-l10n -l pl.UTF-8
Pliki umiędzynarodawiające dla kformuli.

%package -n koffice-kivio-l10n
Summary:	Internationalization and localization files for kivio
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kivio
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kivio = %{koffice_epoch}:%{version}

%description -n koffice-kivio-l10n
Internationalization and localization files for kivio.

%description -n koffice-kivio-l10n -l pl.UTF-8
Pliki umiędzynarodawiające dla kivio.

%package -n koffice-kpresenter-l10n
Summary:	Internationalization and localization files for kpresenter
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kpresentera
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kpresenter = %{koffice_epoch}:%{version}

%description -n koffice-kpresenter-l10n
Internationalization and localization files for kpresenter.

%description -n koffice-kpresenter-l10n -l pl.UTF-8
Pliki umiędzynarodawiające dla kpresentera.

%package -n koffice-krita-l10n
Summary:	Internationalization and localization files for krita
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla krita
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-krita = %{koffice_epoch}:%{version}

%description -n koffice-krita-l10n
Internationalization and localization files for krita.

%description -n koffice-krita-l10n -l pl.UTF-8
Pliki umiędzynarodawiające dla krita.

%package -n koffice-kspread-l10n
Summary:	Internationalization and localization files for kspread
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kspreada
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kspread = %{koffice_epoch}:%{version}

%description -n koffice-kspread-l10n
Internationalization and localization files for kspread.

%description -n koffice-kspread-l10n -l pl.UTF-8
Pliki umiędzynarodawiające dla kspreada.

%package -n koffice-kugar-l10n
Summary:	Internationalization and localization files for kugar
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kugara
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kugar = %{koffice_epoch}:%{version}

%description -n koffice-kugar-l10n
Internationalization and localization files for kugar.

%description -n koffice-kugar-l10n -l pl.UTF-8
Pliki umiędzynarodawiające dla kugara.

%package -n koffice-kword-l10n
Summary:	Internationalization and localization files for kword
Summary(pl.UTF-8):	Pliki umiędzynarodawiające dla kworda
Group:		X11/Applications
Requires:	%{_name}-common-l10n = %{epoch}:%{version}-%{release}
Requires:	%{_name}-kword = %{koffice_epoch}:%{version}

%description -n koffice-kword-l10n
Internationalization and localization files for kword.

%description -n koffice-kword-l10n -l pl.UTF-8
Pliki umiędzynarodawiające dla kworda.

%prep
%setup -q -c -T %(seq -f '-a %g' 0 38 | xargs)

%build
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
		%{__make} install \
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

files="\
example \
graphite \
kdatabase \
kdgantt \
kplato \
"

for i in $files; do
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

files="\
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

for i in $files; do
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

%files -n koffice-common-l10n -f common.lang
%defattr(644,root,root,755)

%files -n koffice-karbon-l10n -f karbon.lang
%defattr(644,root,root,755)

%files -n koffice-kchart-l10n -f kchart.lang
%defattr(644,root,root,755)

%files -n koffice-kexi-l10n -f kexi.lang
%defattr(644,root,root,755)

%files -n koffice-kformula-l10n -f kformula.lang
%defattr(644,root,root,755)

%files -n koffice-kivio-l10n -f kivio.lang
%defattr(644,root,root,755)

%files -n koffice-kpresenter-l10n -f kpresenter.lang
%defattr(644,root,root,755)

%files -n koffice-krita-l10n -f krita.lang
%defattr(644,root,root,755)

%files -n koffice-kspread-l10n -f kspread.lang
%defattr(644,root,root,755)

%files -n koffice-kugar-l10n -f kugar.lang
%defattr(644,root,root,755)

%files -n koffice-kword-l10n -f kword.lang
%defattr(644,root,root,755)
