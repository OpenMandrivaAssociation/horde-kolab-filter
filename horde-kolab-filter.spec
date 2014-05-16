%define peardir %(pear config-get php_dir 2> /dev/null || echo %{_datadir}/pear)
%define xmldir  /var/lib/pear
%define __noautoreq /usr/bin/php

Summary:		Postfix filters for the Kolab server

Name:		horde-kolab-filter
Version: 	0.1.9
Release: 	9
License: 	LGPLv2.1
Group:		Networking/Mail
Source0: 	http://pear.horde.org/get/Kolab_Filter-%{version}.tgz
URL: 		http://pear.horde.org/package/Kolab_Filter
BuildRequires: 	php-pear >= 1.4.7
Requires: 	horde >= 0.0.2
Requires:	horde-icalendar >= 0.0.3
Requires:	horde-argv
Requires:	horde-mime >= 0.0.2
Requires:	horde-util >= 0.0.2
Requires:	horde-kolab-server >= 0.2.0
Requires:	php-pear >= 1.4.0b1
BuildRequires: 	php-pear >= 1.4.7
BuildRequires: 	php-pear-channel-horde
Requires: 	php-pear-channel-horde
BuildArch: 	noarch

%description
The filters provided by this package implement the Kolab
 server resource management as well as some Kolab server sender
 policies.

%prep
%setup -c -T
pear -v -c pearrc \
        -d php_dir=%{peardir} \
        -d doc_dir=/docs \
        -d bin_dir=%{_bindir} \
        -d data_dir=%{peardir}/data \
        -d test_dir=%{peardir}/tests \
        -d ext_dir=%{_libdir} \
        -s

%build

%install
pear -c pearrc install --nodeps --packagingroot %{buildroot} %{SOURCE0}
        
# Clean up unnecessary files
rm pearrc
rm %{buildroot}/%{peardir}/.filemap
rm %{buildroot}/%{peardir}/.lock
rm -rf %{buildroot}/%{peardir}/.registry
rm -rf %{buildroot}%{peardir}/.channels
rm %{buildroot}%{peardir}/.depdb
rm %{buildroot}%{peardir}/.depdblock

mv %{buildroot}/docs .


# Install XML package description
mkdir -p %{buildroot}%{xmldir}
tar -xzf %{SOURCE0} package.xml
cp -p package.xml %{buildroot}%{xmldir}/Kolab_Filter.xml

%clean

%post
pear install --nodeps --soft --force --register-only %{xmldir}/Kolab_Filter.xml

%postun
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/Kolab_Filter
fi

%files
%doc docs/Kolab_Filter/*
%{peardir}/*
%{_bindir}/*
%{xmldir}/Kolab_Filter.xml


