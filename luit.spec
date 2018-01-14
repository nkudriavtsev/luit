Summary:    luit is a filter that can be run between an application and a UTF-8 terminal emulator
Name:       luit
Version:    2.0
Release:    20180109.1%{?dist}
License:    MIT
URL:        http://invisible-island.net/luit/luit.html
Source:     https://github.com/nkudriavtsev/luit/archive/master/luit.tar.gz

%description
Luit is a filter that can be run between an arbitrary application and
a UTF-8 terminal emulator. It will convert application output from
the locale's encoding into UTF-8, and convert terminal input from UTF-8 into
the locale's encoding. It is mainly used to support xterm.

%prep
%setup -q -n luit-master

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/luit
%{_mandir}/man1/luit.1*

%changelog
* Fri Jan 12 2018 Nicholas Kudriavtsev <nkudriavtsevg@gmail.com> - 2.0-20180109.1
- Initial spec file
