%define _requires_exceptions pear(PHPUnit/Framework.php)
%define prj Kolab_Filter

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-kolab-filter
Version:       0.1.9
Release:       %mkrel 4
Summary:       Postfix filters for the Kolab server
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
Source1:       nl_NL.po
BuildArch:     noarch
Requires(pre): php-pear
Requires:      php-pear-Net_LMTP
Requires:      horde-framework
Requires:      horde-icalendar
Requires:      horde-argv
Requires:      horde-mime
Requires:      horde-notification
Requires:      horde-util
Requires:      kolab-server
Requires:      php-pear-Net_SMTP
Requires:      php-pear-Mail
BuildRequires: horde-framework
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde

%description
The filters provided by this package implement the Kolab server
resource management as well as some Kolab server sender policies.

%prep
%setup -q -n %{prj}-%{version}
%__cp %{SOURCE0} %{prj}-%{version}.tgz

%build

%install
pear -d doc_dir=%{_docdir}/kolab \
  install --packagingroot %{buildroot} --nodeps --offline %{prj}-%{version}.tgz

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp %{_builddir}/package.xml %{buildroot}%{xmldir}/%{prj}.xml

%__install -d -m 755 %{buildroot}%{_mandir}/man1
%__mv %{buildroot}%{_docdir}/kolab/Kolab_Filter/man/man1/kolabfilter.1 %{buildroot}%{_mandir}/man1


%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%{_bindir}/kolabfilter
%{_bindir}/kolabmailboxfilter
%{_mandir}/man1/kolabfilter.1.*
%dir %{_docdir}/kolab
%dir %{_docdir}/kolab/Kolab_Filter
%{_docdir}/kolab/Kolab_Filter/COPYING
%dir %{peardir}/data
%dir %{peardir}/data/Kolab_Filter
%dir %{peardir}/data/Kolab_Filter/locale
%dir %{peardir}/data/Kolab_Filter/locale/de_DE
%dir %{peardir}/data/Kolab_Filter/locale/de_DE/LC_MESSAGES
%{peardir}/data/Kolab_Filter/locale/de_DE/LC_MESSAGES/Kolab_Filter.mo
%dir %{peardir}/data/Kolab_Filter/locale/fr_FR
%dir %{peardir}/data/Kolab_Filter/locale/fr_FR/LC_MESSAGES
%{peardir}/data/Kolab_Filter/locale/fr_FR/LC_MESSAGES/Kolab_Filter.mo
%dir %{peardir}/data/Kolab_Filter/locale/nl_NL
%dir %{peardir}/data/Kolab_Filter/locale/nl_NL/LC_MESSAGES
%{peardir}/data/Kolab_Filter/locale/nl_NL/LC_MESSAGES/Kolab_Filter.mo
%dir %{peardir}/data/Kolab_Filter/po
%{peardir}/data/Kolab_Filter/po/Kolab_Filter.pot
%{peardir}/data/Kolab_Filter/po/de_DE.po
%{peardir}/data/Kolab_Filter/po/fr_FR.po
%{peardir}/data/Kolab_Filter/po/nl_NL.po
%dir %{peardir}/Horde/Kolab
%dir %{peardir}/Horde/Kolab/Filter
%dir %{peardir}/Horde/Kolab/Filter/Transport
%{peardir}/Horde/Kolab/Filter/Base.php
%{peardir}/Horde/Kolab/Filter/Content.php
%{peardir}/Horde/Kolab/Filter/Incoming.php
%{peardir}/Horde/Kolab/Filter/Outlook.php
%{peardir}/Horde/Kolab/Filter/Response.php
%{peardir}/Horde/Kolab/Filter/Transport.php
%{peardir}/Horde/Kolab/Filter/Transport/DovecotLDA.php
%{peardir}/Horde/Kolab/Filter/Transport/LMTPTLS.php
%{peardir}/Horde/Kolab/Filter/Transport/drop.php
%{peardir}/Horde/Kolab/Filter/Transport/echo.php
%{peardir}/Horde/Kolab/Filter/Transport/lda.php
%{peardir}/Horde/Kolab/Filter/Transport/lmtp.php
%{peardir}/Horde/Kolab/Filter/Transport/smtp.php
%{peardir}/Horde/Kolab/Filter/Transport/stdout.php
%dir %{peardir}/Horde/Kolab/Resource
%{peardir}/Horde/Kolab/Resource.php
%{peardir}/Horde/Kolab/Resource/Epoch.php
%{peardir}/Horde/Kolab/Resource/Itip.php
%dir %{peardir}/Horde/Kolab/Test
%{peardir}/Horde/Kolab/Test/Filter.php
%dir %{peardir}/tests/Kolab_Filter
%dir %{peardir}/tests/Kolab_Filter/Horde
%dir %{peardir}/tests/Kolab_Filter/Horde/Kolab
%dir %{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/AllTests.php
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/ContentTest.php
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/FilterTest.php
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/IncomingTest.php
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/LoadTest.php
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/ResourceTest.php
%dir %{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/attendee_status_invitation.eml
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/empty2.ret
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/empty.eml
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/forged.eml
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/forged.ret
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/forged_trans.ret
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/invitation_forward.eml
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/invitation_forward.ret
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/longstring_invitation.eml
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/null.ret
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/privileged.ret
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/recur_invitation.eml
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/recur_invitation2.eml
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/recur_invitation.ret
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/simple2.ret
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/simple.eml
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/simple_out.ret
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/simple.ret
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/test.eml
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/tiny.eml
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/tiny.ret
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/vacation.eml
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/vacation.ret
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/validation.eml
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/validation.ret
%{peardir}/tests/Kolab_Filter/Horde/Kolab/Filter/fixtures/allday_invitation.eml


