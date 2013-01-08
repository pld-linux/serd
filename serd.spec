Summary:	Lightweight C library for RDF syntax
Summary(pl.UTF-8):	Lekka biblioteka C do składni RDF
Name:		serd
Version:	0.18.2
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
# Source0-md5:	0569c21860b2ed2744e42884069a40a2
URL:		http://drobilla.net/software/serd/
BuildRequires:	python
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

%prep
%setup -q

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

./waf -v

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_bindir}/serdi
%attr(755,root,root) %{_libdir}/libserd-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libserd-0.so.0
%{_mandir}/man1/serdi.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libserd-0.so
%{_includedir}/serd-0
%{_pkgconfigdir}/serd-0.pc
