Summary:	Logical Disk Manager (Dynamic Disk) Tool
Summary(pl):	Narzêdzie do patycji LDM ("dynamicznych dysków" Windows 2000/XP)
Name:		linux-ldm
Version:	0.0.4
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/linux-ntfs/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.sourceforge.net/pub/sourceforge/linux-ntfs/ldmdoc-0.1.tar.bz2
Patch0:		%{name}-build.patch
URL:		http://linux-ntfs.sf.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to dump or get information about LDM partitions. Contains LDM
documentation.

%description -l pl
Narzêdzie do zrzucania danych i uzyskiwania informacji o partycjach
LDM. Pakiet zawiera dokumentacjê do partycji LDM.

%prep
%setup -q -a1
%patch -p1

%build
#%{__make} -C test CC="%{__cc}" CFLAGS="%{rpmcflags}"
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags} %{!?debug:-fomit-frame-pointer}" \
	KERNELSRC="%{_kernelsrcdir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install test/ldminfo $RPM_BUILD_ROOT%{_bindir}

gzip -9nf AUTHORS ChangeLog README
rm -rf ldm/CVS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz ldm
%attr(755,root,root) %{_bindir}/*
