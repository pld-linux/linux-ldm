Summary:	Logical Disk Manager (Dynamic Disk) Tool
Summary(pl):	Narz�dzie do partycji LDM ("dynamicznych dysk�w" Windows 2000/XP)
Name:		linux-ldm
Version:	0.0.8
%define	docver	0.2
Release:	2
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/linux-ntfs/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.sourceforge.net/pub/sourceforge/linux-ntfs/ldmdoc-%{docver}.tar.bz2
Patch0:		%{name}-build.patch
URL:		http://linux-ntfs.sf.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to dump or get information about LDM partitions (Windows
2000/XP "dynamic disks"). Contains LDM documentation.

%description -l pl
Narz�dzie do zrzucania danych i uzyskiwania informacji o partycjach
LDM ("dynamicznych dysk�w" Windows 2000/XP). Pakiet zawiera
dokumentacj� do partycji LDM.

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