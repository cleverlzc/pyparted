Summary: python module for parted
Name: pyparted
Version: 1.6.7
Release: 2
License: GPL
Group: System Environment/Libraries
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: parted >= 1.6
BuildRequires: parted-devel >= 1.6, python-devel

%description
Python modules for the parted library.  It is used for manipulation
partition tables.

%prep
%setup -q

%build
export CFLAGS="-fPIC"
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README COPYING
%dir %{_libdir}/python?.?/site-packages/
%{_libdir}/python?.?/site-packages/*.so


%changelog
* Thu Jul 22 2004 Jeremy Katz <katzj@redhat.com> - 1.6.7-2
- build on ppc64 again

* Thu May 13 2004 Jeremy Katz <katzj@redhat.com> - 1.6.7-1
- fix build for newer versions of gcc (fix from Jeff Law)

* Tue Mar 16 2004 Jeremy Katz <katzj@redhat.com> 1.6.6-2
- fix PARTITION_PROTECTED definition (#118451)

* Fri Mar 12 2004 Jeremy Katz <katzj@redhat.com>
- Initial build split out into separate source from the parted package.
- Don't build on ppc64 right now due to parted build problems (#118183)
