Summary:	ASCII Tux (Linux Penguin)
Name:		linux_logo
Version:	5.11
Release:	%mkrel 3
License:	GPLv2
Group:		System/Configuration/Boot and Init
Source0:	http://www.deater.net/weave/vmwprod/linux_logo/%{name}-%{version}.tar.gz
Source1:    mga.logo
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

%files -f %{name}.lang
%doc ANNOUNCE.logo BUGS CHANGES README TODO
%doc LINUX_LOGO.FAQ USAGE README.CUSTOM_LOGOS
%{_bindir}/linux_logo
%{_mandir}/man1/linux_logo.1*
