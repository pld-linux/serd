#
# Conditional build:
%bcond_without	apidocs	# API documentation

Summary:	Lightweight C library for RDF syntax
Summary(pl.UTF-8):	Lekka biblioteka C do składni RDF
Name:		serd
Version:	0.32.4
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.xz
# Source0-md5:	553a9b50caa23a7c57732f83e6f80658
URL:		http://drobilla.net/software/serd/
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%if %{with apidocs}
BuildRequires:	doxygen
BuildRequires:	mandoc
BuildRequires:	python3 >= 1:3.6
BuildRequires:	python3-sphinx_lv2_theme
BuildRequires:	sphinx-pdg >= 2
BuildRequires:	sphinxygen
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Serd is a lightweight C library for RDF syntax which supports reading
and writing Turtle and NTriples.

Serd is not intended to be a swiss-army knife of RDF syntax, but
rather is suited to resource limited or performance critical
applications (e.g. converting many gigabytes of NTriples to Turtle),
or situations where a simple reader/writer with minimal dependencies
is ideal (e.g. in LV2 implementations or embedded applications).

%description -l pl.UTF-8
Serd to lekka biblioteka C do obsługi składni RDF, obsługująca odczyt
i zapis formatów Turtle i NTriples.

Serd nie ma na celu obsługi wszystkich aspektów składni RDF, jest
przeznaczony raczej do zastosowań z ograniczonymi zasobami lub
krytycznych pod względem wydajności (np. konwersji wielu gigabajtów z
formatu NTriples do Turtle), albo w sytuacjach, gdzie ideałem jest
prosty program czytający/zapisujący o minimalnych zależnościach (np. w
implementacjach LV2 lub środowiskach wbudowanych).

%package devel
Summary:	Header files for serd library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki serd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for serd library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki serd.

%package apidocs
Summary:	API documentation for serd library
Summary(pl.UTF-8):	Dokumentacja API biblioteki serd
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for serd library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki serd.

%prep
%setup -q

%build
%meson \
	--default-library=shared \
	%{!?with_apidocs:-Ddocs=disabled} \
	-Dman_html=disabled \
	-Dsinglehtml=disabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%if %{without apidocs}
# -Ddocs=disabled disables man page installation
install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p doc/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README.md
%attr(755,root,root) %{_bindir}/serdi
%attr(755,root,root) %{_libdir}/libserd-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libserd-0.so.0
%{_mandir}/man1/serdi.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libserd-0.so
%{_includedir}/serd-0
%{_pkgconfigdir}/serd-0.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%dir %{_docdir}/serd-0
%{_docdir}/serd-0/html
%endif
