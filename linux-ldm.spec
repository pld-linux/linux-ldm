%define	docver	0.3.2
Summary:	Logical Disk Manager (Dynamic Disk) Tool
Summary(pl.UTF-8):	Narzędzie do partycji LDM ("dynamicznych dysków" Windows 2000/XP)
Name:		linux-ldm
Version:	0.0.8
Release:	2
License:	GPL
Group:		Applications/System
Source0:	https://downloads.sourceforge.net/linux-ntfs/%{name}-%{version}.tar.bz2
# Source0-md5:	bac558dc33633c746bb8c93f6861d231
Source1:	https://downloads.sourceforge.net/linux-ntfs/ldmdoc-%{docver}.tar.gz
# Source1-md5:	28bfcc8b591ffab48b0ef23f5e675599
Patch0:		%{name}-build.patch
URL:		http://linux-ntfs.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to dump or get information about LDM partitions (Windows
2000/XP "dynamic disks"). Contains LDM documentation.

%description -l pl.UTF-8
Narzędzie do zrzucania danych i uzyskiwania informacji o partycjach
LDM ("dynamicznych dysków" Windows 2000/XP). Pakiet zawiera
dokumentację do partycji LDM.

%prep
%setup -q -a1
%patch -P0 -p1

%{__mv} ldmdoc-%{docver} ldmdoc

%build
%{__make} -C ldmutil \
	CPP="%{__cxx}" \
	OPT="%{rpmcxxflags} %{!?debug:-fomit-frame-pointer}"

%if 0
# relies on kernel parts
%{__make} -C test \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer} -include extra.h -I../linux/fs/partitions"
%endif

%{__mv} ldmutil/README README.ldmutil

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ldmutil/ldmutil $RPM_BUILD_ROOT%{_bindir}
#install test/ldminfo $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README* ldmdoc
%attr(755,root,root) %{_bindir}/ldmutil
