%define	docver	0.2
Summary:	Logical Disk Manager (Dynamic Disk) Tool
Summary(pl):	Narzêdzie do partycji LDM ("dynamicznych dysków" Windows 2000/XP)
Name:		linux-ldm
Version:	0.0.8
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/linux-ntfs/%{name}-%{version}.tar.bz2
# Source0-md5:	bac558dc33633c746bb8c93f6861d231
Source1:	http://dl.sourceforge.net/linux-ntfs/ldmdoc-%{docver}.tar.bz2
# Source1-md5:	e232718f1d54bd7de87456d553c9f068
Patch0:		%{name}-build.patch
URL:		http://linux-ntfs.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to dump or get information about LDM partitions (Windows
2000/XP "dynamic disks"). Contains LDM documentation.

%description -l pl
Narzêdzie do zrzucania danych i uzyskiwania informacji o partycjach
LDM ("dynamicznych dysków" Windows 2000/XP). Pakiet zawiera
dokumentacjê do partycji LDM.

%prep
%setup -q -a1
%patch -p1

%build
%{__make} \
	CC="%{__cc}" \
	CPP="%{__cxx}" \
	OPT="%{rpmcflags} %{!?debug:-fomit-frame-pointer}" \
	KERNEL="%{_kernelsrcdir}"

mv -f ldmutil/README README.ldmutil

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install test/ldminfo ldmutil/ldmutil $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README* ldmdoc
%attr(755,root,root) %{_bindir}/*
