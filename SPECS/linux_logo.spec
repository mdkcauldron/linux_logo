Summary:	ASCII Tux (Linux Penguin)
Name:		linux_logo
Version:	5.11
Release:	%mkrel 5
License:	GPLv2
Group:		System/Configuration/Boot and Init
Source0:	http://www.deater.net/weave/vmwprod/linux_logo/%{name}-%{version}.tar.gz
Source1:    mga.logo
Source2:    linux_logo.service
Source3:    linux_logo.sysinit
Source4:    linux_logo.sysconfig
URL:		http://www.deater.net/weave/vmwprod/linux_logo/

%description
This package contains an ASCII Linux-Penguin.

%prep
%setup -q
install -m 644 %{SOURCE1} ./logos/distributions/mga.logo

echo "./logos/classic-no_periods_or_chars.logo" > logo_config
echo "./logos/distributions/mga.logo" >> logo_config
echo "./logos/banner.logo" >> logo_config
find -exec chmod go+r {} + 

%build
./configure --prefix=%{_prefix}
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
make install PREFIX=%{buildroot}%{_prefix}

%find_lang %{name}

mkdir -p %{buildroot}%{_initddir}
install -m 755 %{SOURCE3} %{buildroot}%{_initddir}/%name
mkdir -p %{buildroot}%{_sysconfdir}/sysinit
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysinit/%name
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/%name.service

%files -f %{name}.lang
%doc ANNOUNCE.logo BUGS CHANGES README TODO
%doc LINUX_LOGO.FAQ USAGE README.CUSTOM_LOGOS
%{_bindir}/linux_logo
%{_mandir}/man1/linux_logo.1*
%{_initddir}/%name
%config(noreplace) %{_sysconfdir}/sysinit/%name
%{_unitdir}/%name.service
