
%define module1_name discordo
%define module1_version 20231107

%define module_builddir $RPM_BUILD_DIR/%{module1_name}-%{version}-%{release}


Name: %{module1_name}
Version: %{module1_version}
Release: 1%{?dist}
Summary: Command-line discord client (written in Go)
License: MIT
URL: https://github.com/ayn2op/discordo/

BuildArch: x86_64
BuildRequires: golang
Requires: xclip

%description
This package provides a command-line discord client.


%prep
rm -rf %{module_builddir} ||:
mkdir -p %{module_builddir}/%{module1_name}-%{version}
cd %{module_builddir}/%{module1_name}-%{version}
git clone https://github.com/ayn2op/discordo
cd discordo
go build .

%install

# module 1
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/discordo/
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{module1_name}/
mkdir -p $RPM_BUILD_ROOT/usr/share/licenses/%{module1_name}/

install -m 0755 %{module_builddir}/%{name}-%{version}/discordo/discordo $RPM_BUILD_ROOT%{_bindir}/discordo
install %{module_builddir}/%{name}-%{version}/discordo/internal/config/config.yml $RPM_BUILD_ROOT%{_sysconfdir}/discordo/
install %{module_builddir}/%{name}-%{version}/discordo/docs/discordo.1 $RPM_BUILD_ROOT%{_mandir}/man1/discordo.1
install %{module_builddir}/%{name}-%{version}/discordo/README.md $RPM_BUILD_ROOT%{_docdir}/%{module1_name}/
install %{module_builddir}/%{name}-%{version}/discordo/docs/configuration.md $RPM_BUILD_ROOT%{_docdir}/%{module1_name}/
install %{module_builddir}/%{name}-%{version}/discordo/docs/faq.md $RPM_BUILD_ROOT%{_docdir}/%{module1_name}/
install %{module_builddir}/%{name}-%{version}/discordo/LICENSE $RPM_BUILD_ROOT/usr/share/licenses/%{module1_name}/LICENSE



%files -n %{module1_name}
%doc %{_docdir}/%{module1_name}/configuration.md
%doc %{_docdir}/%{module1_name}/faq.md
%doc %{_docdir}/%{module1_name}/README.md
%license /usr/share/licenses/%{module1_name}/LICENSE
%{_mandir}/man1/discordo.1*
%config %{_sysconfdir}/discordo/config.yml
%{_bindir}/discordo


%changelog
* Mon Nov 7 2023 Frederic Krueger <fkrueger-dev-discordo@holics.at> 20231107-1
- Initial spec file based on the github repository of discord by ayn2op

