Summary:	ASCII Tux (Linux Penguin)
Name:		linux_logo
Version:	5.11
Release:	%mkrel 10
License:	GPLv2
Group:		System/Boot and Init
URL:		http://www.deater.net/weave/vmwprod/linux_logo/
Source0:	http://www.deater.net/weave/vmwprod/linux_logo/%{name}-%{version}.tar.gz

%description
This package contains an ASCII Linux-Penguin.

%prep
%setup -q

echo "./logos/classic-no_periods_or_chars.logo" > logo_config
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
