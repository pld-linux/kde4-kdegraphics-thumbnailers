%define		_state		stable
%define		orgname		kdegraphics-thumbnailers
%define		qtver		4.7.4

Summary:	K Desktop Environment - Thumbnailers for various graphic types
Name:		kdegraphics-thumbnailers
Version:	4.7.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	177ccb5137308ad2a53a2046b4afb910
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libkdcraw-devel >= %{version}
BuildRequires:	libkexiv2-devel >= %{version}
Obsoletes:	kde4-kdegraphics-kfile < 4.6.99
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
