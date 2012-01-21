%define		_state		stable
%define		orgname		kdegraphics-thumbnailers
%define		qtver		4.8.0

Summary:	K Desktop Environment - Thumbnailers for various graphic types
Name:		kde4-kdegraphics-thumbnailers
Version:	4.8.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	3676f3f233968b12d1bdac40931dde30
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdcraw-devel >= %{version}
BuildRequires:	kde4-libkexiv2-devel >= %{version}
Obsoletes:	kde4-kdegraphics-kfile < 4.6.99
Obsoletes:	kdegraphics-thumbnailers <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Thumbnailers for various graphic types.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/gsthumbnail.so
%attr(755,root,root) %{_libdir}/kde4/rawthumbnail.so
%{_datadir}/kde4/services/gsthumbnail.desktop
%{_datadir}/kde4/services/rawthumbnail.desktop
