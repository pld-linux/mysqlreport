Summary:	mysqlreport - friendly report of important MySQL status values
Name:		mysqlreport
Version:	3.5
Release:	1
License:	GPL v2
Group:		Applications/Databases
Source0:	http://hackmysql.com/scripts/%{name}-%{version}.tgz
# Source0-md5:	33a345f5e2c89b083a9ff0423f7fd7b4
URL:		http://hackmysql.com/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-DBD-mysql
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mysqlreport makes a friendly report of important MySQL status values.
mysqlreport transforms the values from SHOW STATUS into an
easy-to-read report that provides an in-depth understanding of how
well MySQL is running. mysqlreport is a better alternative (and
practically the only alternative) to manually interpreting SHOW
STATUS.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -Dp %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc mysqlreport*.html
%attr(755,root,root) %{_bindir}/%{name}
