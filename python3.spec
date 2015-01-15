%global pybasever 3.4

Name:		python3
Version:	3.4.2
Release:	6%{?dist}
Summary:	Version 3 of the Python programming language
Group:		Development/Languages
License:	Python
URL:		https://www.python.org/downloads/
Source0:	%{name}-%{version}.tar.gz
Provides:	python(abi) = %{pybasever}
Provides: 	/usr/local/bin/python
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Python 3 is a new version of the language that is incompatible with the 2.x line of releases. The language is mostly the same, but many details, especially how built-in objects like dictionaries and strings work, have changed considerably, and a lot of deprecated features have finally been removed.

%package libs
Summary:	Python 3 runtime libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description libs
This package contains files used to embed Python 3 into applications.

%package devel
Summary: 	Libraries and header files needed for Python 3 development
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains libraries and header files used to build applications with and native libraries for Python 3.

%package tools
Summary:	A collection of tools included with Python 3
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-tkinter = %{version}-%{release}

%description tools
This package contains several tools included with Python 3.

%package tkinter
Summary: 	A GUI toolkit for Python 3
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description tkinter
The Tkinter (Tk interface) program is a graphical user interface for Python scripting.

%package test
Summary: 	The test modules from the main python 3 package
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-tools = %{version}-%{release}

%description test
The test modules from the main package.
These are in a separate package to save space, as they are never used in production. You might want to install the python3-test package if you're developing python3 code that uses more than just unittestr and/or test_support.py

%package debug
Summary: 	Debug version of the Python 3 runtime
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-test = %{version}-%{release}
Requires:	%{name}-tkinter = %{version}-%{release}
Requires:	%{name}-tools = %{version}-%{release}

%description debug
python3-debug provides a version of the Python 3 runtime with numerous debugging features enabled, aimed at advanced Python users, such as developers of Python extension modules.

This verion uses more memory and will be slower than the regular Python 3 build, but is useful for tracking down reference-counting issues, and other bugs.

The bytecodes are unchanged, so that .pyc files are compatible between the two versions of Python 3, but the debugging features mean that C/C++ extension modules are ABI-incompatible with those built for the standard runtime.

It shares installation directories with the standard Python 3 runtime, so that .py and .pyc files can be shared. All compiled extension modules gain a "_d" suffix ("foo_d.so" rather than foo.so") so that each Python 3 implementation can load its own extensions.

%prep
%setup -q 

%build
%configure --with-pydebug --with-tsc --with-count-allocs --with-call-profile --without-ensurepip
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
chmod 0755 %{buildroot}%{_libdir}/libpython%{pybasever}dm.a

ln -s \
	%{_bindir}/python34dm \
	%{buildroot}%{_bindir}/python3-debug

#ln -s \
#	%{?scl:%{_bindir}/python} %{buildroot}/usr/local/bin/python
	

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc LICENSE README
%{?scl:%{_bindir}/python}
%{_bindir}/python3
%{_bindir}/python%{pybasever}
%{_bindir}/pydoc3
%{_bindir}/pydoc%{pybasever}
%{_bindir}/pyvenv
%{_bindir}/pyvenv-%{pybasever}
%{_bindir}/python%{pybasever}dm
%{_bindir}/python%{pybasever}dm-config
%{_mandir}/*/*

%files libs
%defattr(-,root,root,-)
%doc LICENSE README
/usr/lib/python%{pybasever}
%{_libdir}/python%{pybasever}/lib-dynload
%{_includedir}/python%{pybasever}dm
%{_libdir}/libpython%{pybasever}dm.a

%files devel
%defattr(-,root,root,-)
%doc LICENSE README
%{_bindir}/python3-config
%{_bindir}/python%{pybasever}-config
%{_libdir}/pkgconfig/python-%{pybasever}.pc
%{_libdir}/pkgconfig/python-%{pybasever}dm.pc
%{_libdir}/pkgconfig/python3.pc

%files tools
%defattr(-,root,root,-)
%doc LICENSE README
%{_bindir}/2to3
%{_bindir}/2to3-%{pybasever}
%{_bindir}/idle3
%{_bindir}/idle%{pybasever}

%files tkinter
%defattr(-,root,root,-)
%doc LICENSE README

%files test
%defattr(-,root,root,-)
%doc LICENSE README
%{_libdir}/python%{pybasever}/lib-dynload

%files debug
%defattr(-,root,root,-)
%doc LICENSE README
%{_bindir}/python3-debug

%changelog
* Wed Jan 14 2015 Sakib Jalal <sfj19@nbcs.rutgers.edu> - 3.4.2-6.ru6
- Actually fixed last requirement in python-libs.

* Wed Jan 14 2015 Sakib Jalal <sfj19@nbcs.rutgers.edu> - 3.4.2-5.ru6
- Fixed last requirement in python-libs.

* Wed Jan 14 2015 Sakib Jalal <sfj19@nbcs.rutgers.edu> - 3.4.2-4.ru6
- Trying to fix python(abi) with a provides statement.

* Wed Jan 14 2015 Sakib Jalal <sfj19@nbcs.rutgers.edu> - 3.4.2-3.ru6
- Fixing dependency errors.

* Tue Jan 13 2015 Sakib Jalal <sfj19@nbcs.rutgers.edu> - 3.4.2-2.ru6
- Cleaned up spec file.

* Fri Jan 13 2015 Sakib Jalal <sfj19@nbcs.rutgers.edu> - 3.4.2-1.ru6
- Python3 Rutgers first release.
